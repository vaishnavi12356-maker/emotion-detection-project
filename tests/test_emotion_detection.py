import unittest
from emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        result = emotion_detector("I am very happy today!")
        self.assertIn("dominant_emotion", result)

    def test_sadness(self):
        result = emotion_detector("I am feeling very sad.")
        self.assertIn("dominant_emotion", result)

    def test_blank_input(self):
        result, status = emotion_detector("")
        self.assertEqual(status, 400)
        self.assertIn("error", result)

if __name__ == '__main__':
    unittest.main()
