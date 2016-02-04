/*! \file TIM_Core.h
	\brief Core functionality for a P21451-2 TIM utilizing MSP430 Architecture.

	\details This file contains the core funcitonality to communicate from an NCAP to
	a TIM over UART. The current implementaiton is limited in its funcitonality, however,
	as more work is done, we will continue to update this file. The Transducer Interface Module (TIM)
	is one of the three main entities in a IEEE P21451 Smart Transducer Network. The heirarchy of this
	network can be seen in the figure below. This TIM will communicate to only ONE NCAP, however,
	it is not limited to just communication over UART.

	Currently, this implementation only supports ReadTransducerChannelData, WriteTransducerChannelData, ReadMetaTEDS, and MetaTEDSInit.
	This was done to show the core functionality behind the network, and also lay out the foundation for future work.

	To test out this code, open up a UART Channel with putty with Baud Rate 115200
	and use the following syntax for sending messages:

	"$XXX,YYY" Where XXX is a function ID, and YYY is a channel ID. Currently the only
	functionIDs supported are "000", "128", "160" for "Write to all transducers/Write to a specific Channel",
	"Read all Transducers/Read Specific Transducer", "Reading Meta/Channel TEDS" respectively.
	What determines which function each message commands (X/Y) is the ChannelID. If the ChannelID = 000, then it
	is assumed that the NCAP wants global functionality, otherwise it performs local functions.

	Some of the functions will only reply over UART a success message which currently are place holders for the proper response.

	It is reccomended that for testing the code, you turn on Local Echo and well as local line editing in your
	serial terminal.


	\image html P21451_Diagram.png


	\author Russell Trafford
	\date 12/22/2015

 */

#ifndef TIM_CORE_H_
#define TIM_CORE_H_

/*!
	\def UART_CHANNEL
	Default UART channel as laid out in UART.c.
 */
#define UART_CHANNEL 1

/*!
	\struct META_TEDS
	\brief Contains all basic Information for the TIM; calls upon the MetaTEDSInit() function in TIM1.h.

	All TIMs on a network need a TEDS to tell the NCAP what exactly it is capable of. The
	first type of TEDS the NCAP will attempt to read is the MetaTEDS which contains information about
	how many sensor channels there are, worst case sampling times, as well as other communication
	and initialization information. The fields and their applicable data types can be found in the
	IEEE P21451-2 documentation.
 */

typedef struct{
	uint32_t MetaTEDSLength; /**< Total length in Bytes of the MetaTEDS excluding this field*/
	uint8_t IEEE1451WGNum; /**< Working Group Number for which the following TEDs Template is laid out*/
	uint8_t TEDSVersionNum; /**< Specifies the version number of the TEDS that corresponds to the particular part of the standard which the TEDS are from */
	uint8_t CH0IndCalExtKey; /**< The value in this field indicates the highest functional address for writing the industry-implemented Calibration TEDS extension that is available in the STIM for CHANNEL_ZERO. */
	uint8_t CH0IndDataExtKey; /**< The value in this field indicates the highest functional address for writing the industry-implemented nonvolatile data field extensions that is available in the STIM for CHANNEL_ZERO. */
	uint8_t CH0TEDSExtKey; /**< The value in this field indicates the highest functional address for writing the industry-implemented TEDS extensions that is available in the STIM for CHANNEL_ZERO. */
	uint8_t CH0EUAppKey; /**< This field indicates the presence of End-Users’ Application-Specific TEDS function in CHANNEL_ZERO. */
	uint8_t WCChanDataLen; /**< This field specifies the maximum value of the Channel Data Model Length for all the implemented channels.*/
	uint16_t WCChanDataRep; /**< This field specifies the maximum value of the Channel Data Repetitions for all the implemented channels.*/
	uint32_t CH0WrTEDSLen; /**< This field specifies the length in bytes available for each CHANNEL_ZERO user-writable TEDS.*/
	float TWU; /**< This field specifies the maximum value of the Channel Update Time (twu) for all the implemented channels in seconds.*/
	float TGWS; /**< This field specifies the minimum time (tgws), in seconds, between the end of a global write frame and the application of a global trigger.*/
	float TGRS; /**< This field specifies the minimum time (tgrs), in seconds, between the receipt of a global trigger acknowledge and the beginning of a global read frame.*/
	float TWSP; /**< This field specifies the maximum value (twsp), in seconds, of the channel sampling period for all implemented channels. */
	float TWWUT; /**< This field specifies the minimum time, in seconds, that is necessary between application of power to the STIM and instigation of the first transducer data transfer.*/
	float CRT; /**< This field specifies the longest time, in seconds, that the STIM takes to process any command.*/
	float THS; /**< This field specifies the longest time (ths), in seconds, for the STIM to remove the trigger acknowledge signal
after the trigger signal is removed by the NCAP, or for the STIM to remove the data transport acknowledge
signal after the data transport is inactivated by the NCAP.*/
	float TLAT; /**< This field specifies the longest time (tlat), in seconds, that a STIM shall take to detect the removal of the data
transport enable signal.*/
	float TTH; /**< This field specifies the maximum individual hold-off time, in seconds, imposed by the STIM before the first
byte, or between bytes, of any data transfer addressed to TEDS functions. */
	float TOH; /**< This field specifies the maximum individual hold-off time, in seconds, imposed by the STIM before the first
byte, or between bytes, of any data transfer addressed to operational functions.*/
	uint32_t MDR; /**< This field specifies the maximum data rate, in bits per second, supported by the STIM interface.*/
	uint16_t ChanGroupLen; /**< This field specifies the total number of bytes in the Channel Grouping data sub-block.*/
	uint8_t  NumChanGroup; /**< This field specifies the number of discrete channel groupings defined in this STIM’s Meta-TEDS.*/
	uint16_t MTChecksum; /**< This field contains the checksum for the complete Meta-TEDS data block.*/
	char GloballyUID[10]; /**< Globally Unique Identifier, as generated by an algorithm laid out in the Standard.  */
}META_TEDS;

/*!
	\struct CHANNEL_TEDS
	\brief Contains all basic Information for each channel of a TIM; there needs to be N copies where N is the number of channels on the TIM.

	Every Channel attached to a TIM needs to have a set of TEDS to be able tell the NCAP about what is connected to the TIM.
 */

typedef struct {
	uint32_t ChanTEDSLen; /**< This field specifies the total number of bytes in the channel TEDS data block excluding this field. */
	uint8_t CalKey; /**< The calibration capabilities of the TIM. */
	uint8_t ChanIndCalExtKey; /**< The value in this field indicates the highest functional address for writing the industry-implemented Calibration TEDS extension that is available in the STIM for this channel. */
	uint8_t ChanIndDataExtKey; /**< The value in this field indicates the highest functional address for writing the industry-implemented nonvolatile data field extensions that is available in the STIM for this channel.*/
	uint8_t ChanTEDSExtKey; /**< The value in this field indicates the highest functional address for writing the industry-implemented TEDS
extensions that is available in the STIM for this channel.*/
	uint8_t ChanEUAppKey; /**< This field indicates the presence of End-Users’ Application-Specific TEDS function for this channel. */
	uint8_t ChanWriteLen; /**< This field specifies the length in bytes available for each individual user-writable TEDS associated with this
channel, such as Calibration TEDS, Calibration Identification TEDS, or End-User’s Application-Specific
TEDS.*/
	uint8_t ChanTypeKey; /**< This field specifies the channel transducer type.*/
	float LowRangeLmt; /**< For sensors, this shall be the lowest valid value for transducer data after correction is applied, interpreted in
the units specified by the Physical Units field of the Channel TEDS. For actuators, this shall be the lowest valid value for transducer data before correction is applied, interpreted
in the units specified by the physical units field of the channel TEDS.*/
	float UppRangeLmt; /**< For sensors, this shall be the highest valid value for transducer data after correction is applied, interpreted in
the units specified by the Physical Units field of the Channel TEDS. For actuators, this shall be the highest valid value for transducer data before correction is applied, interpreted
in the units specified by the Physical Units field of the Channel TEDS.*/
	float WCUncert; /**< This field specifies the “Combined Standard Uncertainty”.*/
	uint8_t SelfTestKey; /**< This field defines the self-test capabilities of the transducer.*/
	uint8_t ChanDataMod; /**< This field describes the data model used when addressing read transducer data or write transducer data for
this channel.*/
	uint8_t ChanDataModLen; /**< This field specifies the number of bytes in the representation of the selected Channel Data Model.*/
	uint16_t ChanModSigBits; /**< When the Channel Data Model is N-byte integer (enumeration zero) or N-byte fraction (enumeration three),
the value of this field is the number of bits that are significant. When the Channel Data Model is N-byte integer or N-byte fraction, the Channel Model Significant Bits
shall not exceed eight times the Channel Model Data Length. When the Channel Data Model is N-byte fraction, the significant data bits shall be left-justified within the
byte stream. When the Channel Data Model is single- or double-precision real (enumerations one or two), the value of
this field is the number of bits in the STIM’s signal converter.*/
	uint16_t ChanDataReps; /**< The number L of repetitions of the transducer value produced or required by a single trigger.*/
	float SerOrigin; /**< For the case where the Channel Data Repetitions is greater than zero, the Series Origin represents the value
of the independent variable associated with the first datum returned in a data set. */
	float SerInc; /**< For the case where the Channel Data Repetitions is greater than zero, the series increment represents the
spacing between values of the independent variable associated with successive members of the data set.*/
	float ChanTU; /**< This field specifies the maximum time (tu), in seconds, between the receipt of a trigger and the issue of trigger
acknowledge for this channel.*/
	float ChanTWS; /**< This field specifies the minimum time (tws), in seconds, between the end of a write frame and the application
of a trigger. */
	float ChanTRS; /**< This field specifies the minimum time (trs), in seconds, between the trigger acknowledge and the beginning
of a read frame.*/
	float ChanTSP; /**< The Channel Sampling Period (tsp) shall be the minimum sampling period of the channel transducer unencumbered by read or write considerations.*/
	float ChanTWU; /**< This field specifies the period of time, in seconds, in which the device stabilizes its performance to predefined tolerances after the application of power to the transducer.*/
	float ChanTCH; /**< This field specifies the maximum aggregated time (tch) that the STIM will spend holding off the data transport during a complete data transfer addressed to read transducer data or write transducer data and this
channel, assuming the Maximum Data Rate is used. */
	float TimeCorr; /**< This field specifies the time offset, in seconds, between the issue of global trigger acknowledge and when this
channel actually sampled the sensor or updated the actuator. */
	float TrigAcc; /**< This field specifies the accuracy, in seconds, of the Timing Correction.*/
	uint8_t EvtSeqOpt; /**< An event sequence sensor has the option of changeable pattern, upper threshold, and/or hysteresis. It also has
the option of detecting inconsistencies in settings of these parameters.*/
	uint16_t ChanChkSum; /**< This field contains the checksum for the complete Channel TEDS data block. The checksum shall be the
one’s complement of the sum (modulo 216) of all the data structure’s preceding bytes, including the initial
length field and excluding the checksum field.*/
	char SerUnits[10]; /**< This field specifies the maximum time (tu), in seconds, between the receipt of a trigger and the issue of trigger
acknowledge for this channel. */
	char PhysUnits[10]; /**< This field defines the physical units that apply to the transducer data.*/
} CHANNEL_TEDS;


/*! \fn void TIM_Init(void)
	\brief Runs UART and TEDS Initialization

	\details Initializes the TIM by registering the UART reciever as well as calling MetaTEDSInit() to load the MetaTEDs into memory.

	\todo Implement and call the ChannelTEDS Init funciton.
	\todo Add in support for other connection mediums (NRF, SPI, etc).
 */

void TIM_Init(void);


#endif /* TIM_CORE_H_ */
