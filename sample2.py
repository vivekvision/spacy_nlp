import spacy
import pandas as pd

# Load the English language model in spaCy
nlp = spacy.load("en_core_web_sm")

# Sample DataFrame with a 'text' column
df = pd.DataFrame({'text': ['I love visiting France and Italy.', 'Germany is a beautiful country.', 'Spain has amazing food.']})

# Function to extract country names from text using spaCy
def extract_country_names(text):
    doc = nlp(text)
    country_names = []
    for ent in doc.ents:
        if ent.label_ == 'GPE':  # Filter entities labeled as geopolitical entities (countries, cities, etc.)
            country_names.append(ent.text)
    return country_names

# Apply the function to the 'text' column
df['country_names'] = df['text'].apply(extract_country_names)

# Display the updated DataFrame
print(df)
