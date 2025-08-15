# Remote ML Model Execution using GCP

![Python](https://img.shields.io/badge/Python-3.9-blue)
![GCP](https://img.shields.io/badge/Google%20Cloud-Functions-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

## 📌 Overview
This project demonstrates a **cloud-based machine learning inference system** using **Google Cloud Platform (GCP)**.  
A trained **crop prediction model** is stored in **Google Cloud Storage (GCS)** and executed remotely via **Google Cloud Functions**, allowing real-time predictions from any local machine without heavy computation requirements.

The architecture ensures that:
- **Computation happens entirely in the cloud**.
- The **local environment only sends input and receives predictions**.
- Integration with **Google Cloud SDK** ensures secure and seamless communication.

---

## 🚀 Features
- Cloud-hosted ML model deployment using **Google Cloud Functions**.
- Model storage & retrieval from **Google Cloud Storage**.
- JSON-based input for flexibility, easy integrtion.
- Real-time predictions via **cURL** or Python requests.
- No local computational overhead.

---

## 🛠️ Tech Stack
- **Python 3.9+**
- **Google Cloud Functions**
- **Google Cloud Storage**
- **Joblib** for model loading
- **JSON** for data exchange
- **Google Cloud SDK** for authentication

---

## 📂 Project Structure

.
├── crop_model.pkl       # Trained Random Forest model (stored in GCS in production)
├── input.json           # Sample JSON input for predictions
├── main.py              # Cloud Function entry point
└── requirements.txt     # Python dependencies


## ⚙️ Setup & Deployment

1- Install Google Cloud SDK
Download & install: https://cloud.google.com/sdk/docs/install

Authenticate:

gcloud auth login
gcloud config set project <your-gcp-project-id>
(Replace <your-gcp-project-id> with your own project ID)

2- Create and upload your .pkl file
gcloud storage buckets create [BUCKET_NAME] --location=[REGION] #creates a bucket
#specify the bucket name and region acording to your gcp setup.
gcloud storage cp crop_model.pkl gs://[your-bucket-name]  

2- Enable Required GCP Services

gcloud services enable cloudfunctions.googleapis.com
gcloud services enable storage.googleapis.com

4- Deploy Cloud Function

gcloud functions deploy predict \
  --runtime python310 \
  --trigger-http \
  --allow-unauthenticated \
  --source=. \
  --entry-point=predict \

  #you will receive a url after execution this command
  #Send Prediction Request via cURL

curl -X POST <your-cloud-function-url> \
  -H "Content-Type: application/json" \
  -d @input.json
(Replace <your-cloud-function-url> with your deployed function URL)

Example Response
{
  "prediction": "Wheat"
}

📈 Example Workflow

- User sends JSON input from local terminal.
- Data is sent securely to the Google Cloud Function.
- Model is loaded from Google Cloud Storage.
- Prediction is generated and returned instantly.
  

🔮 Future Work

- Add a frontend dashboard for easier predictions without cURL.
- Enable multiple ML models and selection via API.
- Implement authentication & API keys for better security.
- Add logging and monitoring for usage analytics.
- Expand to real-time streaming data predictions (e.g., IoT integration).

📜 License
This project is licensed under the MIT License — you are free to use, modify, and distribute it.

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

✨ Author
Shifa Thamkin S
📧 Email: utstshifa@gmail.com
🌐 GitHub: utshifa
