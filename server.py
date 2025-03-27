from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):

    def test_emotion_detector(self):
        # Caso 1
        result_1 = emotion_detector("I'm glad this happened")
        self.assertEqual(result_1['dominant_emotion'], 'joy')
    
        # Caso 2
        result_2 = emotion_detector("I'm really angry about this")
        self.assertEqual(result_2['dominant_emotion'], 'anger')
    
        # Caso 3
        result_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

        # Caso 4
        result_3 = emotion_detector("I'm so sad about this")
        self.assertEqual(result_3['dominant_emotion'], 'sadness')

        # Caso 5
        result_3 = emotion_detector("I'm really afraid this will happen")
        self.assertEqual(result_3['dominant_emotion'], 'fear')

unittest.main()