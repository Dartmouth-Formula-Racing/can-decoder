from candecoder.inverter_types import signed_int


def temperatures1(data):
    return {
        "ModA": (signed_int(data[0], data[1]), "degC"),
        "ModB": (signed_int(data[2], data[3]), "degC"),
        "ModC": (signed_int(data[4], data[5]), "degC"),
        "GateDriverBoard": (signed_int(data[6], data[7]), "degC"),
    }

def temperatures2(data):
    return {
        "ControlBoardTemperature": (signed_int(data[0], data[1]), "degC"),
        "RTD1Temperature": (signed_int(data[2], data[3]), "degC"),
        "RTD2Temperature": (signed_int(data[4], data[5]), "degC"),
        "RTD3Temperature": (signed_int(data[6], data[7]), "degC")
    }