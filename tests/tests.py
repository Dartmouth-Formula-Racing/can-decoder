import unittest
from candecoder import decode_message_by_id
from candecoder import decode_all_messages

class TestTemperatures1(unittest.TestCase):

    def test_example_method(self):
        self.assertEqual(
            decode_message_by_id("00A0", [0, 1, 2, 3, 4, 5, 6, 7]),
            {
                "Inverter1_Temperatures1_ModA": (25.6, "degC"),
                "Inverter1_Temperatures1_ModB": (77, "degC"),
                "Inverter1_Temperatures1_ModC": (128.4, "degC"),
                "Inverter1_Temperatures1_GateDriverBoard": (179.8, "degC")
            }
        )

if __name__ == '__main__':
    unittest.main()
