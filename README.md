# SMS/Email Spam Detection Model

## Overview
This project is an **NLP and Machine Learning-based Spam Detection Model** that classifies whether an entered SMS or email is **spam or not**. It leverages **machine learning techniques** to provide accurate predictions.

Additionally, a **Streamlit-based web application** has been developed and deployed on **Streamlit Cloud**, allowing users to easily test the model.

## Features
- Detects spam messages in **SMS and emails**
- Uses **Machine Learning/NLP** techniques for classification
- User-friendly **Streamlit application**
- **Deployed on Streamlit Cloud** for online access

## Installation
To run the model locally, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone <repo_link>
   cd <repo_directory>
   ```

2. **Create a virtual environment and activate it:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app:**
   ```sh
   streamlit run app.py
   ```

## Usage
1. Open the Streamlit web application.
2. Enter an SMS or email message.
3. Click the "Predict" button.
4. The model will display whether the message is **spam or not spam**.

## Deployment
The application is deployed on **Streamlit Cloud**. You can access it here: [Spam-Detection-Model](<https://detection-spam-message.streamlit.app/>)

## Technologies Used
- Python
- Streamlit
- Scikit-learn / Any other ML library used
- NLP techniques for text classification
