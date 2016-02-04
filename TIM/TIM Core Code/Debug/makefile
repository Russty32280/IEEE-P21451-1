################################################################################
# Automatically-generated file. Do not edit!
################################################################################

SHELL = cmd.exe

CG_TOOL_ROOT := D:/Code Composer/ccsv6/tools/compiler/ti-cgt-msp430_4.4.3

ORDERED_OBJS += \
$(GEN_CMDS__FLAG) \
"./TIM1.obj" \
"./TIM_Core.obj" \
"./buffer.obj" \
"./buffer_printf.obj" \
"./charReceiverList.obj" \
"./hal_uart.obj" \
"./itemBuffer.obj" \
"./list.obj" \
"./main.obj" \
"./random_int.obj" \
"./subsys.obj" \
"./task.obj" \
"./timing.obj" \
"./uart.obj" \
"../lnk_msp430f5529.cmd" \
-l"libc.a" \
-l"libmath.a" \

-include ../makefile.init

RM := DEL /F
RMDIR := RMDIR /S/Q

# All of the sources participating in the build are defined here
-include sources.mk
-include subdir_vars.mk
-include subdir_rules.mk
-include objects.mk

ifneq ($(MAKECMDGOALS),clean)
ifneq ($(strip $(S_DEPS)),)
-include $(S_DEPS)
endif
ifneq ($(strip $(S_UPPER_DEPS)),)
-include $(S_UPPER_DEPS)
endif
ifneq ($(strip $(S62_DEPS)),)
-include $(S62_DEPS)
endif
ifneq ($(strip $(C64_DEPS)),)
-include $(C64_DEPS)
endif
ifneq ($(strip $(ASM_DEPS)),)
-include $(ASM_DEPS)
endif
ifneq ($(strip $(CC_DEPS)),)
-include $(CC_DEPS)
endif
ifneq ($(strip $(S55_DEPS)),)
-include $(S55_DEPS)
endif
ifneq ($(strip $(C67_DEPS)),)
-include $(C67_DEPS)
endif
ifneq ($(strip $(C??_DEPS)),)
-include $(C??_DEPS)
endif
ifneq ($(strip $(CLA_DEPS)),)
-include $(CLA_DEPS)
endif
ifneq ($(strip $(CPP_DEPS)),)
-include $(CPP_DEPS)
endif
ifneq ($(strip $(S??_DEPS)),)
-include $(S??_DEPS)
endif
ifneq ($(strip $(C_DEPS)),)
-include $(C_DEPS)
endif
ifneq ($(strip $(C62_DEPS)),)
-include $(C62_DEPS)
endif
ifneq ($(strip $(CXX_DEPS)),)
-include $(CXX_DEPS)
endif
ifneq ($(strip $(C++_DEPS)),)
-include $(C++_DEPS)
endif
ifneq ($(strip $(ASM_UPPER_DEPS)),)
-include $(ASM_UPPER_DEPS)
endif
ifneq ($(strip $(K_DEPS)),)
-include $(K_DEPS)
endif
ifneq ($(strip $(C43_DEPS)),)
-include $(C43_DEPS)
endif
ifneq ($(strip $(S67_DEPS)),)
-include $(S67_DEPS)
endif
ifneq ($(strip $(SA_DEPS)),)
-include $(SA_DEPS)
endif
ifneq ($(strip $(S43_DEPS)),)
-include $(S43_DEPS)
endif
ifneq ($(strip $(OPT_DEPS)),)
-include $(OPT_DEPS)
endif
ifneq ($(strip $(S64_DEPS)),)
-include $(S64_DEPS)
endif
ifneq ($(strip $(C_UPPER_DEPS)),)
-include $(C_UPPER_DEPS)
endif
ifneq ($(strip $(C55_DEPS)),)
-include $(C55_DEPS)
endif
endif

-include ../makefile.defs

# Add inputs and outputs from these tool invocations to the build variables 
EXE_OUTPUTS += \
P21451_TIM.out \

EXE_OUTPUTS__QUOTED += \
"P21451_TIM.out" \

BIN_OUTPUTS += \
P21451_TIM.hex \

BIN_OUTPUTS__QUOTED += \
"P21451_TIM.hex" \


# All Target
all: P21451_TIM.out

# Tool invocations
P21451_TIM.out: $(OBJS) $(CMD_SRCS) $(GEN_CMDS)
	@echo 'Building target: $@'
	@echo 'Invoking: MSP430 Linker'
	"D:/Code Composer/ccsv6/tools/compiler/ti-cgt-msp430_4.4.3/bin/cl430" -vmspx --abi=eabi --data_model=restricted --use_hw_mpy=F5 --advice:power=all -g --define=__MSP430F5529__ --diag_warning=225 --display_error_number --diag_wrap=off --silicon_errata=CPU21 --silicon_errata=CPU22 --silicon_errata=CPU23 --silicon_errata=CPU40 --printf_support=minimal -z -m"P21451_TIM.map" --heap_size=160 --stack_size=160 --cinit_hold_wdt=on -i"D:/Code Composer/ccsv6/ccs_base/msp430/include" -i"D:/Code Composer/ccsv6/tools/compiler/ti-cgt-msp430_4.4.3/lib" -i"D:/Code Composer/ccsv6/tools/compiler/ti-cgt-msp430_4.4.3/include" -i"D:/Code Composer/ccsv6/ccs_base/msp430/lib/5xx_6xx_FRxx" --reread_libs --warn_sections --display_error_number --diag_wrap=off --xml_link_info="P21451_TIM_linkInfo.xml" --use_hw_mpy=F5 --rom_model -o "P21451_TIM.out" $(ORDERED_OBJS)
	@echo 'Finished building target: $@'
	@echo ' '

P21451_TIM.hex: $(EXE_OUTPUTS)
	@echo 'Invoking: MSP430 Hex Utility'
	"D:/Code Composer/ccsv6/tools/compiler/ti-cgt-msp430_4.4.3/bin/hex430" --memwidth=8 --romwidth=8 -o "P21451_TIM.hex" $(EXE_OUTPUTS__QUOTED)
	@echo 'Finished building: $@'
	@echo ' '

# Other Targets
clean:
	-$(RM) $(EXE_OUTPUTS__QUOTED)$(BIN_OUTPUTS__QUOTED)
	-$(RM) "TIM1.pp" "TIM_Core.pp" "buffer.pp" "buffer_printf.pp" "charReceiverList.pp" "hal_uart.pp" "itemBuffer.pp" "list.pp" "main.pp" "random_int.pp" "subsys.pp" "task.pp" "timing.pp" "uart.pp" 
	-$(RM) "TIM1.obj" "TIM_Core.obj" "buffer.obj" "buffer_printf.obj" "charReceiverList.obj" "hal_uart.obj" "itemBuffer.obj" "list.obj" "main.obj" "random_int.obj" "subsys.obj" "task.obj" "timing.obj" "uart.obj" 
	-@echo 'Finished clean'
	-@echo ' '

.PHONY: all clean dependents
.SECONDARY:

-include ../makefile.targets

