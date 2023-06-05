import spacy
import pandas as pd

# first load the English language model using spacy.load("en_core_web_sm"). Then define a function extract_country_names 
# that takes a text input, processes it with spaCy, and extracts the named entities labeled as geopolitical entities (GPE).

# Load the English language model in spaCy
nlp = spacy.load("en_core_web_sm")

# Sample DataFrame with a 'text' column
df = pd.DataFrame({'text': ['I love visiting France and Italy.', 'Germany is a beautiful country.', 'Spain has amazing food.']})

# Function to extract country names from text using spaCy
# it returns a list with country names
def extract_country_names(text):
    doc = nlp(text)
    country_names = []
    for ent in doc.ents:
        if ent.label_ == 'GPE':  # Filter entities labeled as geopolitical entities (countries, cities, etc.)
            country_names.append(ent.text)
    return country_names

# use the apply function along with a lambda function to apply the extract_country_names function to each element of the 'text' column.

# Apply the function to the 'text' column and count the country names
df['country_count'] = df['text'].apply(lambda x: len(extract_country_names(x)))

# Display the updated DataFrame
print(df)
