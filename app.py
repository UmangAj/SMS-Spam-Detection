import streamlit as st
import pickle
import string
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize, sent_tokenize, PorterStemmer
import nltk
import pandas as pd

lemmatizer = WordNetLemmatizer()
nltk.download('punkt_tab')
nltk.download('wordnet')

def data_preprocessing(df):
    
    df['clean_text'] = df['Text'].apply(lambda x:x.lower())
    df['clean_text'] = df['clean_text'].apply(lambda x:x.translate(str.maketrans('', '', string.punctuation)))
    df['clean_text'] = df['clean_text'].apply(lambda x:word_tokenize(x))
    df['clean_text'] = df['clean_text'].apply(lambda x:[lemmatizer.lemmatize(i, 'v') for i in x])
    df['clean_text'] = df['clean_text'].apply(lambda x:" ".join(x))
    
    return df[['clean_text']]


try:

	model = pickle.load(open('model.pkl', 'rb'))

	st.title('SMS Spam Detection')
	st.write('#### Enter your sms/email to check spam or not:')

	input_sms = st.text_area(" ", label_visibility='collapsed')

	if st.button('Predict'):

		if not input_sms:
			st.warning('Please enter a sms/email.')

		else:
			input_sms = pd.DataFrame({'Text': [input_sms]})

			prediction = model.predict(input_sms)[0]

			if prediction == 0:
			    st.write('#### Entered sms is :- Not Spam')
			else:
			    st.write('#### Entered sms is :- Spam')

except Exception as e:
	st.error("This service is currently unavailable. Please try again later.")


