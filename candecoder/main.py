import pandas as pd
from candecoder.Dictionaries import canid_to_message, decoder_funcs


def decode_message_by_id(can_id: str, data: list[int]) -> dict:
    message = canid_to_message[can_id]
    function = decoder_funcs[message]
    variables = function(data)
    for key in list(variables.keys()):
        variables[f"{message}_{key}"] = variables.pop(key)
    return variables


def decode_all_messages(data: pd.DataFrame) -> dict:
    pass