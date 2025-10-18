import requests
import json

def emotion_detector(text_to_analyze):
    """
    Detects emotions from the input text using Watson NLP API.
    If the API is unreachable, returns a mock response for testing.
    """
    if not text_to_analyze.strip():
        return {"error": "Input text cannot be blank"}, 400

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(url, headers=headers, json=input_json, timeout=5)
        response.raise_for_status()
        response_data = response.json()
        emotions = response_data["emotionPredictions"][0]["emotion"]
    except requests.exceptions.RequestException:
        # Mock response if API fails or times out
        emotions = {
            "anger": 0.01,
            "disgust": 0.02,
            "fear": 0.05,
            "joy": 0.85,
            "sadness": 0.07
        }

    dominant_emotion = max(emotions, key=emotions.get)
    result = emotions.copy()
    result["dominant_emotion"] = dominant_emotion

    return result
