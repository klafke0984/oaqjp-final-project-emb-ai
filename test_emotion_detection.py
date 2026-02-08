'''
    This module is used for testing the different emotions provided by
    IBM's Watson NLP library. Different emotions are tested as follows:
    joy, anger, sadness, disgust and fear
'''

# Import all required modules
import unittest
from EmotionDetection import emotion_detector

# Create the class for testing all the emotions
class TestEmotionDetection(unittest.TestCase):

    # Function to test emotion: 'joy'
    def test_joy_emotion(self):
        emotion = emotion_detector('I am glad this happened')
        self.assertEqual(emotion['dominant_emotion'], 'joy')

    # Function to test emotion: 'anger'
    def test_anger_emotion(self):
        emotion = emotion_detector('I am really mad about this')
        self.assertEqual(emotion['dominant_emotion'], 'anger')
    
    # Function to test emotion: 'disgust'
    def test_disgust_emotion(self):
        emotion = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(emotion['dominant_emotion'], 'disgust')

    # Function to test emotion: 'sadness'
    def test_sadness_emotion(self):
        emotion = emotion_detector('I am so sad about this')
        self.assertEqual(emotion['dominant_emotion'], 'sadness')

    # Function to test emotion: 'fear'
    def test_fear_emotion(self):
        emotion = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(emotion['dominant_emotion'], 'fear')

# Run the test suite if the module is called directly
if __name__ == '__main__':
    unittest.main()