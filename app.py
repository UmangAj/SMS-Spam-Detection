import streamlit as st
import pickle
import string
from nltk.stem.porter import PorterStemmer
import nltk

ps = PorterStemmer()
nltk.download('punkt_tab')

def data_preprocessing(text):
	text = text.lower()
	text = nltk.word_tokenize(text)

	y = []
	for i in text:
		if i.isalnum():
			y.append(i)

	text = y[:]
	y.clear()

	for i in text:
		if i not in string.punctuation:
			y.append(i)

	text = y[:]
	y.clear()

	for i in text:
		y.append(ps.stem(i))

	return " ".join(y)
	
try:

	model = pickle.load(open('model.pkl', 'rb'))

	st.title('SMS Spam Detection')
	st.write('#### Enter your sms/email to check spam or not:')

	input_sms = st.text_area(" ", label_visibility='collapsed')

	if st.button('Predict'):

		if not input_sms:
			st.warning('Please enter a sms/email.')

		else:
			user_clean_input = data_preprocessing(input_sms)

			prediction = model.predict([user_clean_input])[0]

			if prediction == 0:
			    st.write('#### Entered sms is :- Not Spam')
			else:
			    st.write('#### Entered sms is :- Spam')

except Exception as e:
	st.error("This service is currently unavailable. Please try again later.")


