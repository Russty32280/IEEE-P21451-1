#include "system.h"
#ifndef _TASK_H_
#error "Please include task.h in system.h"
#endif
#ifndef _LIST_H_
#error "list.h must be included in system.h and list.c must be in your project"
#endif

#ifndef MAX_TASK_LENGTH
#define MAX_TASK_LENGTH 20
#endif

// helper function to roll the time
void RollTimer(void);

/// task structure
typedef struct task_t {
    task_fn_t fn; /**< function to run */
    void * pointer; /**< pointer to pass to the task function if it is set */
    tint_t time; /**< the time the task was added to the queue or the time the task last ran */
    tint_t period; /**< the period for repeating the task if it is to be repeated */
} task_t;

task_t task_array[MAX_TASK_LENGTH];
list_link_t task_links[MAX_TASK_LENGTH];
list_t task_list;

uint8_t sort_tasks(task_t* a, task_t* b);

uint8_t sort_tasks(task_t* a, task_t* b) {
    // if task a is scheduled before b then return 1
    // if task a is scheduled at the same time or after b
    // then return 0
    if (a->time < b->time) return 1;
    return 0;
}

uint8_t identify_task(void * fn_and_ptr[], task_t * task);

uint8_t identify_task(void * fn_and_ptr[], task_t * task) {
    // check if the function pointer matches
    if (task->fn == fn_and_ptr[0]) {
        // check if the pointer matches or if it is 0
        // thus if it is 0 it will not care what the pointer is
        if(task->pointer == fn_and_ptr[1] || fn_and_ptr[1] == 0) return 1;
    }
    return 0;
}

void Task_Init(void) {
    // use flag so module only gets initialized once
    static uint8_t init_flag = 0;
    if(init_flag) return;
    init_flag = 1;
    // make sure the timing module is initialized
    Timing_Init();
    // initialize the list, set the sort function pointer, set the identify function pointer
    List_Init(&task_list, sizeof(task_t), &task_array[0], MAX_TASK_LENGTH, (void*)&task_links);
    List_SetSortFunction(&task_list, (sort_fn_t)sort_tasks);
    List_SetIdentifyFunction(&task_list, (identify_fn_t)identify_task);
    // schedule the timer to be rolled over
    Task_Schedule(RollTimer, 0, TASK_ROLL_TIME, TASK_ROLL_TIME);
#ifdef _EVENT_H_
    Event_Init();
#endif
}

void SystemTick(void) {
    task_t * task_ptr;
    // check if any tasks need to be linked into the queue
    List_Link(&task_list);

    task_ptr = List_GetFirst(&task_list);
    if (task_ptr) {
        if (task_ptr->time <= TimeNow()) {
            // Unlink the front of the list
            List_UnlinkFirst(&task_list);
            if(task_ptr->pointer) {
                // if a pointer is used cast to the correct fn pointer type and run
                ((task_fn_pointer_input_t)task_ptr->fn)(task_ptr->pointer);
            }else task_ptr->fn();
            if (task_ptr->period) {
                task_ptr->time += task_ptr->period;
                List_LinkItem(&task_list, task_ptr);
            } else {
                List_Remove(&task_list, task_ptr);
            }
        }
    }
#ifdef _EVENT_H_
    Event_Tick();
#endif
}

void Task_Queue(task_fn_t fn, void * pointer) {
    task_t * task_ptr;
    task_ptr = List_AddIndirect(&task_list);
    if (task_ptr == 0) return;

    task_ptr->fn = fn;
    task_ptr->time = TimeNow();
    task_ptr->period = 0;
    task_ptr->pointer = pointer;
}

void Task_Schedule(task_fn_t fn, void * pointer,
        tint_t delay, tint_t period) {
    task_t * task_ptr;
    task_ptr = List_AddIndirect(&task_list);
    if (task_ptr == 0) return;

    // load the function, priority, next time to run, and period
    task_ptr->fn = fn;
    task_ptr->time = TimeNow() + delay;
    task_ptr->period = period;
    task_ptr->pointer = pointer;
}

void Task_Remove(task_fn_t fn, void * pointer) {
    void * fn_and_pointer[2];
    task_t* task_ptr;
    fn_and_pointer[0] = fn;
    fn_and_pointer[1] = pointer;
    // remove all tasks that match
    task_ptr = List_GetItem(&task_list, &fn_and_pointer);
    while (task_ptr) {
        List_Remove(&task_list, task_ptr);
        // don't keep looking if the function and pointer were specified
        // it will be the users responsibility to call Task_Remove if they
        // added multiple tasks with the same input pointer
        if(pointer) break;
        task_ptr = List_GetItem(&task_list, &fn_and_pointer);
    }
}

void RollTimer(void) {
    tint_t time;
    task_t * task;
    // get the current time
    time = TimeNow();
    // for each task
    task = List_GetFirst(&task_list);
    while (task) {
        // if time is in the future then roll it
        // otherwise just let it be as TimeSince will handle the roll
        if (task->time > time) {
            // rolled task time = task time - current time
            // since current time is about to be set to 0
            task->time = task->time - time;
        }
        task = List_GetNext(&task_list, task);
    }

    // reset the system time and set the rollover time
    Timing_Roll();
}

// delay a set number of milliseconds but call SystemTick() while we wait so
// we will run system processes while we wait

void WaitMs(tint_t wait) {
    tint_t time;
    // get the current time
    time = TimeNow();
    // while time since time is less than or equal to wait
    while (TimeSince(time) <= wait) {
        // call SystemTick()
        SystemTick();
    }
}

uint8_t Task_IsScheduled(task_fn_t fn) {
    task_t * task;
    task = List_GetItem(&task_list, &fn);
    if(task) return 1;
    return 0;
}
