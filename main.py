import pickle
import json
from flask import Request
import joblib
from google.cloud import storage
import numpy as np
from io import BytesIO

def predict(request: Request):
    # Parse input from JSON body
    request_json = request.get_json()
    input_data = request_json.get('data', [])
    print(request_json,input_data)

    # Load model from GCS
    storage_client = storage.Client()
    bucket = storage_client.bucket('rfbuc')
    blob = bucket.blob('crop_model.pkl')
    model_bytes = blob.download_as_bytes()
    print("model type:",type(model_bytes))
    model=joblib.load(BytesIO(model_bytes))
   
    # Predict
    input_array = np.array(input_data)  # wrap in array if single sample
    prediction = model.predict(input_array).tolist()
    print("prediction:",prediction)


    return json.dumps({'prediction': prediction})




