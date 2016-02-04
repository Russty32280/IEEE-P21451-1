/**
 * @file subsys.h
 *
 * @defgroup subsys Subsystem Module
 *
 *  Created on: Mar 12, 2014
 *      @author: Michael
 *
 * @version 2014.03.26 changed SystemTick to SubsystemTick so the Task Management Module can own SystemTick()
 * @version 2.0.1 added version, setup SYSTEM subsystem, changed warning messages to priority WARNING and set default priority to ERROR to suppress messages
 * @version 3.1.1 removed log levels and redueced to mute or unmute. Moved
 *     receiver functionality to UART module. Changed callback to take argc
 *     argv inputs and added parsing to create argc and argv.
 * @{
 */
#ifndef SUBSYS_H_
#define SUBSYS_H_

/////////////////////////MMmmbbbb
#define SYSTEM_VERSION 0x03010001u ///< subsystem module version number

#ifndef RECEIVE_MAX_LENGTH
#define RECEIVE_MAX_LENGTH 64 ///< default length of receive line for commands
#endif
#define RECEIVE_START_CHAR '$' ///< start character for command lines
#define RECEIVE_STOP_CHAR '\r' ///< stop character for command lines
#define RECEIVE_MAX_ARGC 8 ///< max number of arguments after the command name

/** Version typedef to store software version of subsystem
 *
 * The version is split into three numbers:
 * major.minor.build
 * where major and minor are 0-255 and build is 0-65535
 * build should be incremented as frequently as possible (automatically on build
 * if possible with the compiler)
 */
typedef struct {
        uint16_t build; /**< build number*/
        uint8_t minor; /**< minor version*/
        uint8_t major; /**< major version*/
} version_mmb_t;
/// version union
typedef union {
    uint32_t word; /**< 32 bit version */
    version_mmb_t v; /**< major.minor.build struct*/
} version_t;

/** @page sys_receive SubSystem module command interface
 *
 * If bi-directional communication is available (e.g. UART) then the
 * user can interface with the SubSystem module in real time using the
 * module's command interface.
 *
 * A command can be sent to the module in the following format:
 * @code
 * $command -f0
 * @endcode
 * Where the $ indicates the start of the command, command is the name of the
 * command and -f8 is a flag with a value of 8. \n
 * Valid system flags are @c -s, @c -l and @c -g
 *
 * The commands available are:
 *
 * @c version (or @c ver) - will output a list of subsystems and their version.
 * No flags are applicable.
 *
 * @c level (or @c lev) - if no flags are given @c level will output level a
 * list of valid level codes and their names as used in the log messages. If a
 * @c -l flag is given but not a @c -s flag then the level specified with the
 * @c -l flag is set as the global level. If the @c -l and @c -s flags are given
 * then set the level specified with the @c -l flag for the subsystem specified
 * with the @c -s flag. If a @c -g flag is given it will set the global log
 * level to the specified value. The global log level will for any message from
 * any subsystem to be logged if its level is at the global level or below.
 *
 * @c subsystem (or @c sub or @c sys or @c system) - will output a list of
 * valid subsystem codes and their associated subsystem names and their current
 * log level setting as used by the log message functions. The @c -s flag can
 * be used to return only information about the specified subsystem.
 *
 * Example usage:
 * @code
 * $version
 *
 * $sub
 *
 * $level
 *
 * $level -l0
 *
 * $level -s0 -l2
 * @endcode
 *
 * In the above example:
 * - output the subsystems and their versions
 * - output the subsystems and their codes
 * - output the log levels and their codes
 * - set the global log level to 0 (OFF)
 * - set the log level for subsystem 0 (SYSTEM) is set to 2 (ERROR).
 *
 * The end result is that no messages would be logged unless they were SYSTEM
 * messages with a priority level greater than or equal to ERROR (note higher
 * priority is lower numerically).
 *
 * Additionally commands may be forwarded to the callback of compatible subsystems
 * using the following format
 * @code
 * $12 command <anything goes>
 * $MUH play
 * @endcode
 * In the first line subsystem index 12 is sent the command string starting
 * after the space. In the second line a module named MUH is sent a command
 * "play"
 *
 * @todo MM Update this comment block
 */

/** @page subsys_init Subsystem module initialization
 *
 * Below are three example of how a subsystem could initialize itself.
 *
 * @code
 * // define the version
 * #define TASK_VERSION (version_t)0x01010014u
 *
 * // initialize module to log EVERYTHING and to use "task" to refer
 * // to this subsystem in output messages
 * SubsystemInit(TASK, EVERYTHING, "task", TASK_VERSION);
 *
 * // or another way to do the same thing
 *
 * #define TASK_VERSION_MAJOR 1
 * #define TASK_VERSION_MINOR 1
 * #define TASK_VERSION_BUILD 20
 *
 * version_t task_version;
 * task_version.major = TASK_VERSION_MAJOR;
 * task_version.minor = TASK_VERSION_MINOR;
 * task_version.build = TASK_VERSION_BUILD;
 *
 * SubsystemInit(TASK, EVERYTHING, "task", task_version);
 *
 * // or to do it all in one line
 * uint8_t task_id;
 * task_id = SubsystemInit(EVERYTHING, "task", (version_t)0x01010014u);
 * LogMsG(task_id, WARNING, "Crap hit the fan");
 * @endcode
 *
 * @todo MM Update this comment block
 */


 /** GetLogTimestamp must be defined so that it returns a integer (up to 32 bits)
  * timestamp
  */
 #define GetLogTimestamp() TimeNow()

// use Push_printf to log messages to the log buffer LOG_BUF
 /** Logs the null terminated string at the pointer (str)
  *
  * Same as LogMsg() without the header in the beginning and without the CRLF at
  * the end.
  *
  * This function is implemented using Push_vprintf. See Push_printf() for supported
  * flags/features.
  *
  * Will log the string to the buffer defined by LOG_BUF (typically tx0)
  *
  * @param str pointer to string to log
  * @param ... variable number of replacement parameters for the str string
  *
  * Example usage:
  * @code
  *   LogStr("oops I crapped my pants");
  *   LogStr("System Index %d, System Name %s.", SYSTEM, GetSubsystemName(SYSTEM));
  * @endcode
  */
void LogStr(char * str, ...);

/** Logs the message at the pointer (str) with a timestamp and subsystem name
 *
 * Before logging the message the function will check the current log setting of
 * the subsystem and to determine if the message should be logged
 *
 * This function is implemented using Push_vprintf. See Push_printf() for supported
 * flags/features.
 *
 * Will log the string to the buffer defined by SUSSYS_UART
 *
 * @param subsystem_id subsystem id
 * @param str pointer to message to log
 * @param ... variable number of replacement parameters for the str string
 *
 * Example usage:
 * @code
 *   LogMsg(sys.id, "oops I crapped my pants");
 *   LogMsg(sys.id, "System Index %d, System Name %s.", sys.id, GetSubsystemName(SYSTEM));
 * @endcode
 */
void LogMsg(uint8_t subsystem_id, char * str, ...);

/** Initialize settings for a subsystem - critical for proper logging and command interface
 *
 * If a module/subsystem uses logging it should call this function
 * with the appropriate inputs when the subsystem is initializing.
 *
 * @return subsystem index
 * @param name pointer to name of the subsystem (recommended to make the name
 *        8 characters or less)
 * @param version software version of subsystem, see #version_t for more info
 * @param callback callback function to be called when the user inputs a command
 * in the form of "$name var1 var2 var3...". Where name is the name passed to
 * this function. The callback will be passed the number of arguments, @c argc ,
 * and a array of pointers to the argument strings, @c argv.
 */
uint8_t Subsystem_Init(char * name, version_t version, void (*callback)(int argc, char *argv[]));

/** Register a callback function for a subsystem
 *
 * When a command is received by the logging module for the subsystem @c sys
 * the @c callback function will be executed and passed the number of 
 * arguments @c argc and a array (vector) of pointer to the argument strungs
 * @c argv.
 *
 * The callback is set by Subsystem_Init(), this function can be used to update
 * the callback.
 *
 * @param subsystem_id - subsystem to register the callback for
 * @param callback - function pointer to the function to run when a command is
 * received for the subsystem.
 */
void Subsystem_RegisterCallback(uint8_t subsystem_id, void (*callback)(int argc, char *argv[]));

/** Return a pointer to a string corresponding to the name of the subsystem
 *
 * The name returned is the one set by SubsystemInit()
 *
 * @param subsystem_id
 * @return - pointer to a null terminated string corresponding to the name of the subsystem
 */
char *GetSubsystemName(uint8_t subsystem_id);

/** Turn echo featuren on (default is off) */
void Log_EchoOn(void);

/** Turn echo feature off */
void Log_EchoOff(void);

/** Get status of echo setting
 * 
 * @return echo setting, 1 if echo is on
 */
uint8_t Log_GetEcho(void);

/**
 * Log header (timestamp and subsystem name)
 *
 * @param subsystem_id subsystem id (index)
 */
void Log_Header(uint8_t subsystem_id);

/** @}*/


extern void ReceiveChar(char c);

#endif /* SUBSYS_H_ */
