import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#ltk.download('punkt')
#ltk.download('stopwords')

stop_words = set(stopwords.words('english'))

text = "Why am I having this sore throat?"
tokens = word_tokenize(text.lower())
keywords = [word for word in tokens if word.isalnum() and word not in stop_words]

print("Extracted keywords:", keywords)