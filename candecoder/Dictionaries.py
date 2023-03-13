from candecoder.inverter_funcs import *

decoder_funcs = {
    "Inverter1_Temperatures1": temperatures1,
    "Inverter1_Temperatures2": temperatures2,
    "Inverter1_Temperatures3": temperatures3,
    "Inverter1_Analog_Input_Voltages": None,
    "Inverter1_Digital_Input_Status": digital_input_status,
    "Inverter1_Motor_Position_Information": motor_position_information,
    "Inverter1_Current_Information": current_information,
    "Inverter1_Voltage_Information": voltage_information,
    "Inverter1_Flux_Information": flux_information,
    "Inverter1_Internal_Voltages": internal_voltages,
    "Inverter1_Internal_States": None,
    "Inverter1_Fault_Codes": fault_codes,
    "Inverter1_Torque_&_Timer_Information": torque_and_timer_information,
    "Inverter1_Modulation_Index_&_Flux_Weakening_Output_Information": modulation_index,
    "Inverter1_Firmware_Information": firmware,
    "Inverter1_Diagnostic_Data": diagnostic_data,
    "Inverter1_High_Speed_Message": high_speed_message,
    "Inverter2_Temperatures1": temperatures1,
    "Inverter2_Temperatures2": temperatures2,
    "Inverter2_Temperatures3": temperatures3,
    "Inverter2_Analog_Input_Voltages": None,
    "Inverter2_Digital_Input_Status": digital_input_status,
    "Inverter2_Motor_Position_Information": motor_position_information,
    "Inverter2_Current_Information": current_information,
    "Inverter2_Voltage_Information": voltage_information,
    "Inverter2_Flux_Information": flux_information,
    "Inverter2_Internal_Voltages": internal_voltages,
    "Inverter2_Internal_States": None,
    "Inverter2_Fault_Codes": fault_codes,
    "Inverter2_Torque_&_Timer_Information": torque_and_timer_information,
    "Inverter2_Modulation_Index_&_Flux_Weakening_Output_Information": modulation_index,
    "Inverter2_Firmware_Information": firmware,
    "Inverter2_Diagnostic_Data": diagnostic_data,
    "Inverter2_High_Speed_Message": high_speed_message,
}

canid_to_message = {
    "00A0": "Inverter1_Temperatures1",
    "00A1": "Inverter1_Temperatures2",
    "00A2": "Inverter1_Temperatures3",
    "00A3": "Inverter1_Analog_Input_Voltages",
    "00A4": "Inverter1_Digital_Input_Status",
    "00A5": "Inverter1_Motor_Position_Information",
    "00A6": "Inverter1_Current_Information",
    "00A7": "Inverter1_Voltage_Information",
    "00A8": "Inverter1_Flux_Information",
    "00A9": "Inverter1_Internal_Voltages",
    "00AA": "Inverter1_Internal_States",
    "00AB": "Inverter1_Fault_Codes",
    "00AC": "Inverter1_Torque_&_Timer_Information",
    "00AD": "Inverter1_Modulation_Index_&_Flux_Weakening_Output_Information",
    "00AE": "Inverter1_Firmware_Information",
    "00AF": "Inverter1_Diagnostic_Data",
    "00B0": "Inverter1_High_Speed_Message",
    "00D0": "Inverter2_Temperatures1",
    "00D1": "Inverter2_Temperatures2",
    "00D2": "Inverter2_Temperatures3",
    "00D3": "Inverter2_Analog_Input_Voltages",
    "00D4": "Inverter2_Digital_Input_Status",
    "00D5": "Inverter2_Motor_Position_Information",
    "00D6": "Inverter2_Current_Information",
    "00D7": "Inverter2_Voltage_Information",
    "00D8": "Inverter2_Flux_Information",
    "00D9": "Inverter2_Internal_Voltages",
    "00DA": "Inverter2_Internal_States",
    "00DB": "Inverter2_Fault_Codes",
    "00DC": "Inverter2_Torque_&_Timer_Information",
    "00DD": "Inverter2_Modulation_Index_&_Flux_Weakening_Output_Information",
    "00DE": "Inverter2_Firmware_Information",
    "00DF": "Inverter2_Diagnostic_Data",
    "00E0": "Inverter2_High_Speed_Message",
}