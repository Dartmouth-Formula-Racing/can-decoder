import unittest
from candecoder import decode_message_by_id
from candecoder import decode_all_messages


class TestInverterMessages(unittest.TestCase):

    def test_inverter1_temperatures1(self):
        self.assertEqual(
            decode_message_by_id("00A0", [0, 1, 2, 3, 4, 5, 6, 7]),
            {
                "Inverter1_Temperatures1_ModA": (25.6, "degC"),
                "Inverter1_Temperatures1_ModB": (77, "degC"),
                "Inverter1_Temperatures1_ModC": (128.4, "degC"),
                "Inverter1_Temperatures1_GateDriverBoard": (179.8, "degC")
            }
        )

    def test_inverter2_temperatures1(self):
        self.assertEqual(
            decode_message_by_id("00C0", [0, 1, 2, 3, 4, 5, 6, 7]),
            {
                "Inverter2_Temperatures1_ModA": (25.6, "degC"),
                "Inverter2_Temperatures1_ModB": (77, "degC"),
                "Inverter2_Temperatures1_ModC": (128.4, "degC"),
                "Inverter2_Temperatures1_GateDriverBoard": (179.8, "degC")
            }
        )

    def test_inverter1_temperatures2(self):
        self.assertEqual(
            decode_message_by_id("00A1", [1, 0, 2, 0, 3, 0, 4, 0]),
            {
                "Inverter1_Temperatures2_ControlBoard": (0.1, "degC"),
                "Inverter1_Temperatures2_RTD1": (0.2, "degC"),
                "Inverter1_Temperatures2_RTD2": (0.3, "degC"),
                "Inverter1_Temperatures2_RTD3": (0.4, "degC")
            }
        )

    def test_inverter2_temperatures2(self):
        self.assertEqual(
            decode_message_by_id("00C1", [1, 0, 2, 0, 3, 0, 4, 0]),
            {
                "Inverter2_Temperatures2_ControlBoard": (0.1, "degC"),
                "Inverter2_Temperatures2_RTD1": (0.2, "degC"),
                "Inverter2_Temperatures2_RTD2": (0.3, "degC"),
                "Inverter2_Temperatures2_RTD3": (0.4, "degC")
            }
        )

if __name__ == '__main__':
    unittest.main()
