from candecoder.inverter_types import signed_int, grab_byte


def temperatures1(data):
    return {
        "ModA": (signed_int(data[0], data[1]) / 10., "degC"),
        "ModB": (signed_int(data[2], data[3]) / 10., "degC"),
        "ModC": (signed_int(data[4], data[5]) / 10., "degC"),
        "GateDriverBoard": (signed_int(data[6], data[7]) / 10., "degC")
    }

def temperatures2(data):
    return {
        "ControlBoardTemperature": (signed_int(data[0], data[1]) / 10., "degC"),
        "RTD1Temperature": (signed_int(data[2], data[3]) / 10., "degC"),
        "RTD2Temperature": (signed_int(data[4], data[5]) / 10., "degC"),
        "RTD3Temperature": (signed_int(data[6], data[7]) / 10., "degC")
    }

def temperatures3(data):
    return {
        "RTD4Temperature": (signed_int(data[0], data[1]) / 10., "degC"),
        "RTD5Temperature": (signed_int(data[2], data[3]) / 10., "degC"),
        "MotorTemperature": (signed_int(data[4], data[5]) / 10., "degC"),
        "TorqueShudder": (signed_int(data[6], data[7]) / 10., "nM")
    }

def fault_codes(data):
    return {
        "Hardware Gate/Desaturation Fault": grab_byte(data[0], 0),
        "Accelerator Shorted": grab_byte(data[0], 1),
        "Accelerator Open": grab_byte(data[0], 2),
        "Current Sensor Low": grab_byte(data[0], 3),
        "Current Sensor High": grab_byte(data[0], 4),
        "Module Temperature Low": grab_byte(data[0], 5),
        "Module Temperature High": grab_byte(data[0], 6),
        "Control PCB Temperature Low": grab_byte(data[0], 7),
        "Control PCB Temperature High": grab_byte(data[1], 0),
        "Gate Drive PCB Temperature Low": grab_byte(data[1], 1),
        "Gate Drive PCB Temperature High": grab_byte(data[1], 2),
        "5V Sense Voltage Low": grab_byte(data[1], 3),
        "5V Sense Voltage High": grab_byte(data[1], 4),
        "12V Sense Voltage Low": grab_byte(data[1], 5),
        "12V Sense Voltage High": grab_byte(data[1], 6),
        "2.5V Sense Voltage Low": grab_byte(data[1], 7),
        "2.5 Sense Voltage High": grab_byte(data[2], 0),
        "1.5 Sense Voltage Low": grab_byte(data[2], 1),
        "1.5 Sense Voltage High": grab_byte(data[2], 2),
        "DC Bus Voltage High": grab_byte(data[2], 3),
        "DC Bus Voltage Low": grab_byte(data[2], 4),
        "Pre-charge Timeout": grab_byte(data[2], 5),
        "Pre-charge Voltage Failure": grab_byte(data[2], 6),
        "EEPROM Checksum Invalid": grab_byte(data[2], 7),
        "EEPRIM Data Out of Range": grab_byte(data[3], 0),
        "EEPROM Update Required": grab_byte(data[3], 1),
        "Hardware DC Bus Over-Voltage during initialization": grab_byte(data[3], 2),
        "Gen 3: Reserved / Gen 5: Gate Drive Initialization": grab_byte(data[3], 3),
        "Reserved": grab_byte(data[3], 4),
        "Brake Shorted": grab_byte(data[3], 5),
        "Brake Open": grab_byte(data[3], 6),
        "Motor Over-speed Fault": grab_byte(data[3], 7),
        "Over-current Fault": grab_byte(data[4], 0),
        "Over-voltage Fault": grab_byte(data[4], 1),
        "Inverter Over-temperature Fault": grab_byte(data[4], 2),
        "Accelerator Input Shorted Fault": grab_byte(data[4], 3),
        "Accelerator Input Open Fault": grab_byte(data[4], 4),
        "Direction Command Fault": grab_byte(data[4], 5),
        "Inverter Response Time-out Fault": grab_byte(data[4], 6),
        "Hardware Gate/Desaturation Fault": grab_byte(data[4], 7),
        "Hardware Over-current Fault": grab_byte(data[5], 0),
        "Under-voltage Fault": grab_byte(data[5], 1),
        "CAN Command Message Lost Fault": grab_byte(data[5], 2),
        "Motor Over-temperature Fault": grab_byte(data[5], 3),
        "Reserved": grab_byte(data[5], 4),
        "Reserved": grab_byte(data[5], 5),
        "Reserved": grab_byte(data[5], 6),
        "Brake Input Shorted Fault": grab_byte(data[5], 7),
        "Brake Input Open Fault": grab_byte(data[6], 0),
        "Module A Over-temperature Fault": grab_byte(data[6], 1),
        "Module B Over-temperature Fault": grab_byte(data[6], 2),
        "Module C Over-temperature Fault": grab_byte(data[6], 3),
        "PCB Over-temperature Fault": grab_byte(data[6], 4),
        "Gate Drive Board 1 Over-temperature Fault": grab_byte(data[6], 5),
        "Gate Drive Board 2 Over-temperature Fault": grab_byte(data[6], 6),
        "Gate Drive Board 3 Over-temperature Fault": grab_byte(data[6], 7),
        "Current Sensor Fault": grab_byte(data[7], 0),
        "Gen 3: Reserved / Gen 5: Gate Drive Over-Volage": grab_byte(data[7], 1),
        "Gen 3: Hardware DC Bus Over-Voltage Fault / Gen 5: Reserved": grab_byte(data[7], 2),
        "Gen 3: Reserved / Gen 5: Hardware DC Bus Over-voltage Fault": grab_byte(data[7], 3),
        "Reserved": grab_byte(data[7], 4),
        "Resolved Not Connected": grab_byte(data[7], 5),
        "Reserved": grab_byte(data[7], 6)
    }

def digital_input_status(data):
    return {
        "DigitalInput0": (data[0], "boolean"),
        "DigitalInput1": (data[1], "boolean"),
        "DigitalInput2": (data[2], "boolean"),
        "DigitalInput3": (data[3], "boolean"),
        "DigitalInput4": (data[4], "boolean"),
        "DigitalInput5": (data[5], "boolean"),
        "DigitalInput6": (data[6], "boolean"),
        "DigitalInput7": (data[7], "boolean"),
    }

def motor_position_information(data):
    return {
        "MotorAngle(Electrical)": (signed_int(data[0], data[1]) / 10., "deg"),
        "MotorSpeed": (signed_int(data[2], data[3]), "rpm"),
        "ElectricalOutputFrequency": (signed_int(data[4], data[5]) / 10., "hz"),
        "DeltaResolverFiltered": (signed_int(data[6], data[7]) / 10., "deg")
    }

def current_information(data):
    return {
        "PhaseACurrent": (signed_int(data[0], data[1]) / 10., "amps"),
        "PhaseBCurrent": (signed_int(data[2], data[3]) / 10., "amps"),
        "PhaseCCurrent": (signed_int(data[4], data[5]) / 10., "amps"),
        "DCBusCurrent": (signed_int(data[6], data[7]) / 10., "amps")
    }

def voltage_information(data):
    return {
        "BCBusVoltage": (signed_int(data[0],data[1]) / 10., "volts"),
        "OutputVoltage": (signed_int(data[2], data[3]) / 10., "volts"),
        "VAB_Vd_Voltage": (signed_int(data[4], data[5]) / 10., "volts"),
        "VBC_Vq_Voltage": (signed_int(data[6], data[7]) / 10., "volts")
    }

def flux_information(data):
    return {
        "FluxCommand": (signed_int(data[0], data[1]) / 1000., "Webers"),
        "FluxFeedback": (signed_int(data[2], data[3]) / 1000., "Webers"),
        "IdFeedback": (signed_int(data[4], data[5]) / 1000.), # not sure
        "IqFeedback": (signed_int(data[6], data[7]) / 1000.) #not sure
    }

def internal_voltages(data):
    return {
        "1.5VReferenceVoltage": (signed_int(data[0], data[1]) / 10., "volts"),
        "2.5VReferenceVoltage": (signed_int(data[2], data[3]) / 10., "volts"),
        "4.0VReferenceVoltage": (signed_int(data[4], data[5]) / 10., "volts"),
        "12VSystemVoltage": (signed_int(data[6], data[7]) / 10., "volts")
    }

def modulation_index(data):
    return {
        "ModulationIndex": (signed_int(data[0], data[1]) / 100.),
        "FluxWeakeningOutput": (signed_int(data[2], data[3]) / 10., "amps"),
        "IdCommand": (signed_int(data[4], data[5]), data[6], data[7] / 10.),
        "IqCommand": (signed_int(data[2], data[3]) / 10.)
    }

def high_speed_message(data):
    return {
        "TorqueCommand": (signed_int(data[0], data[1]) / 10., "N-m"),
        "TorqueFeedback": (signed_int(data[2], data[3]) / 10., "N-m"),
        "MotorSpeed": (signed_int(data[4], data[5]) / 10., "rpm"),
        "DCBusVoltage": (signed_int(data[6], data[7]) / 10., "volts")
    }


def extract_by_range(data, start_bit, stop_bit):
    x = data[0] + 256 * data[1] + 256**2 * data[2] + 256**3 * data[3] + 256**4 * data[4] + 256**5 * data[5] + 256**6 * data[6] + 256**7 * data[7]
    base_mask = 2 ** (stop_bit - start_bit) - 1
    mask = base_mask << start_bit
    return (mask & x) >> start_bit

def torque_and_timer_information(data):
    return {
        "CommandedTorque": (signed_int(data[0], data[1]) / 10., "N-m"),
        "TorqueFeedback": (signed_int(data[2], data[3]) / 10., "N-m"),
        "PowerOnTimer": (signed_int(data[4], data[5]) + (256 ** 2) * signed_int(data[6], data[7])) / 10.
    }

def firmware(data):
    return {
        "EEPROMVersion": (signed_int(data[0], data[1]), "Version"),
        "SoftwareVersion": (signed_int(data[2], data[3]), "Version"),
        "DateCode": (signed_int(data[4], data[5]), "mmdd"),
        "DateCode": (signed_int(data[6], data[7]), "yyyy")
    }

def diagnostic_data(data):
        if data[1] == 0:
            return {
                "RecordNumber": (data[0], ""),
                "gamma_resolver": (signed_int(data[1], data[2]), ""),
                "gamma_observer": (signed_int(data[4], data[5]), ""),
                "sin_corr": (signed_int(data[6], data[7]), ""),
                "0": (signed_int(data[1]), ""),

            }
        if data[1] == 1:
            return {
                "RecordNumber": (data[0], ""),
                "cos_corr": (signed_int(data[1], data[2]), ""),
                "la_corr": (signed_int(data[4], data[5]), ""),
                "lb_corr": (signed_int(data[6], data[7]), ""),
                "1": (signed_int(data[1]), ""),
            }

        if data[1] == 2:
            return {
                "RecordNumber": (data[0], ""),
                "lc_corr": (signed_int(data[1], data[2]), ""),
                "Vdc": (signed_int(data[4], data[5]), ""),
                "iq_cmd": (signed_int(data[6], data[7]), ""),
                "2": (signed_int(data[1]), ""),
            }
        if data[1] == 3:
            return {
                "RecordNumber": (data[0], ""),
                "id_cmd": (signed_int(data[1], data[2]), ""),
                "modulation": (signed_int(data[4], data[5]), ""),
                "flux_weak_out": (signed_int(data[6], data[7]), ""),
                "3": (signed_int(data[1]), ""),
            }

        if data[1] == 4:
            return {
                "RecordNumber": (data[0], ""),
                "vq_cmd": (signed_int(data[1], data[2]), ""),
                "vd_cmd": (signed_int(data[4], data[5]), ""),
                "vqs_cmd": (signed_int(data[6], data[7]), ""),
                "4": (signed_int(data[1]), ""),
            }

        if data[1] == 5:
            return {
                "RecordNumber": (data[0], ""),
                "12Vvoltage/PWM Frequency": (signed_int(data[1], data[2]), ""),
                "run_faults(lo)": (signed_int(data[4], data[5]), ""),
                "run_faults(hi)": (signed_int(data[6], data[7]), ""),
                "5": (signed_int(data[1]), ""),

            }