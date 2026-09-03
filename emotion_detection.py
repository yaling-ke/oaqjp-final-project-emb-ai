import flask, requests

def emotion_detector(text_to_analyze): # Define a function named emotion_detector that take a string input text_to_analyze
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL for the emotion analysis server
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    myobj = { "raw_document": { "text": text_to_analyze } } # Create a dictionary with the text to be analyzed
    
    response = requests.post(url, json=myobj, headers=headers) # Send a POST request to the API with the text and headers# Send a POST request to the API with the text and headers
    return response.text
