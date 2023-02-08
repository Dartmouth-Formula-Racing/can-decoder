from candecoder.inverter_types import signed_int


def temperatures1(data):
    return {
        "ModA": (signed_int(data[0], data[1]) / 10., "degC"),
        "ModB": (signed_int(data[2], data[3]) / 10., "degC"),
        "ModC": (signed_int(data[4], data[5]) / 10., "degC"),
        "GateDriverBoard": (signed_int(data[6], data[7]) / 10., "degC"),
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
    return mask & x >> start_bit

