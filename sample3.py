import spacy
import pandas as pd

# Load the English language model in spaCy
nlp = spacy.load("en_core_web_sm")

# Sample DataFrame with a 'text' column
df = pd.DataFrame({'text': ['I love visiting France and Italy.', 'Germany is a beautiful country.', 'Spain has amazing food.']})

# List of keywords
keywords = ['love', 'beautiful', 'amazing']

# Function to extract words from a list of keywords from text using spaCy
def extract_keywords(text):
    doc = nlp(text)
    extracted_words = []
    for token in doc:
        if token.text.lower() in keywords:
            extracted_words.append(token.text)
    return extracted_words

# Apply the function to the 'text' column
df['extracted_words'] = df['text'].apply(extract_keywords)

# Display the updated DataFrame
print(df)
