""" Tests for the EmotionDetection package"""
from EmotionDetection.emotion_detection import emotion_detector
import unittest
import json

class TestEmotionDetection(unittest.TestCase):
  def test_emotion_detector_joy(self):
    result_1 = emotion_detector('I am glad this happened')
    #Convert string to dictionary
    emotions_dict_1 = json.loads(result_1)
    self.assertEqual(emotions_dict_1['dominant_emotion'],'joy')

  def test_emotion_detector_anger(self):
    result_2 = emotion_detector('I am really mad about this')
    #Convert string to dictionary
    emotions_dict_2 = json.loads(result_2)
    self.assertEqual(emotions_dict_2['dominant_emotion'],'anger')

  def test_emotion_detector_disgust(self):
    result_3 = emotion_detector('I feel disgusted just hearing about this')
    #Convert string to dictionary
    emotions_dict_3 = json.loads(result_3)
    self.assertEqual(emotions_dict_3['dominant_emotion'],'disgust')

  def test_emotion_detector_sadness(self):
    result_4 = emotion_detector('I am so sad about this')
    #Convert string to dictionary
    emotions_dict_4 = json.loads(result_4)
    self.assertEqual(emotions_dict_4['dominant_emotion'],'sadness')

  def test_emotion_detector_fear(self):
    result_5 = emotion_detector('I am really afraid that this will happen')
    #Convert string to dictionary
    emotions_dict_5 = json.loads(result_5)
    self.assertEqual(emotions_dict_5['dominant_emotion'],'fear')

unittest.main()
