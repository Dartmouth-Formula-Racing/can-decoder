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
        "MotorSpeed": (signed_int(data[2], data[3]) / 10., "rpm"),
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