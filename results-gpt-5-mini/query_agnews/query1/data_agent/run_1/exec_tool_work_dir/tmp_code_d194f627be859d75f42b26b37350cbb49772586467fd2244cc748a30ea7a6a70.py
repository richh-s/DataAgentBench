code = """import json
import pandas as pd

# Load the large result from the articles_database query stored in the provided file path
with open(var_call_Qou0eOXFIEtUoD6P5VjTfhlz, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Ensure title and description are strings
df['title'] = df['title'].astype(str)
df['description'] = df['description'].astype(str)

# Compute description length
df['description_length'] = df['description'].map(len)

# Define sports-related keywords for classification
sports_keywords = [
    'football','soccer','basketball','baseball','cricket','tennis','golf',
    'match','tournament','season','coach','player','team','scored','goal','win',
    'defeat','league','cup','olympic','race','innings','touchdown','quarterback',
    'foul','penalty','strike','goalkeeper','hat-trick','run','runs','inning'
]

# Function to classify as sports based on presence of any keyword in title or description
def is_sports(row):
    text = (row['title'] + ' ' + row['description']).lower()
    return any(kw in text for kw in sports_keywords)

# Apply classifier
df['is_sports'] = df.apply(is_sports, axis=1)

# Filter sports articles
sports_df = df[df['is_sports']]

# If no sports articles found, return empty string
if sports_df.empty:
    result = json.dumps("")
else:
    # Find article(s) with maximum description length
    max_len = int(sports_df['description_length'].max())
    candidates = sports_df[sports_df['description_length'] == max_len]
    # Choose the first candidate's title
    title = candidates.iloc[0]['title']
    result = json.dumps(title)

print("__RESULT__:")
print(result)"""

env_args = {'var_call_Qou0eOXFIEtUoD6P5VjTfhlz': 'file_storage/call_Qou0eOXFIEtUoD6P5VjTfhlz.json'}

exec(code, env_args)
