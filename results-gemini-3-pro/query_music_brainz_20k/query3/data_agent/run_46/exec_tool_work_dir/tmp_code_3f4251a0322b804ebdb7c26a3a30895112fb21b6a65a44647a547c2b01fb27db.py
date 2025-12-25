code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-8471687202024638385'], 'r') as f:
    tracks = pd.DataFrame(json.load(f))
with open(locals()['var_function-call-8471687202024637006'], 'r') as f:
    sales = pd.DataFrame(json.load(f))

# Convert revenue to float
sales['total_revenue'] = pd.to_numeric(sales['total_revenue'])

# Merge
df = pd.merge(tracks, sales, on='track_id')

# Helper function to clean text
def clean_text(text):
    if not isinstance(text, str):
        return ""
    return text.lower().strip()

# Clean artist and title
# Handle "Artist - Title" in title field when artist is missing
def extract_artist_title(row):
    title = row['title']
    artist = row['artist']
    
    # Normalize nulls
    if artist in [None, 'None', '[unknown]', '']:
        artist = None
    
    if title is None:
        title = ""
        
    if artist is None:
        # Try to split by " - "
        if " - " in title:
            parts = title.split(" - ", 1)
            return parts[0].strip(), parts[1].strip()
        else:
            return "unknown", title.strip() # Keep unknown if we can't split
    else:
        return artist, title

# Apply extraction
df[['clean_artist', 'clean_title_raw']] = df.apply(lambda x: pd.Series(extract_artist_title(x)), axis=1)

# Further cleaning of title
def normalize_title(t):
    t = t.lower()
    # Remove leading numbers/punctuation like "01-", "007 ", "12. "
    t = re.sub(r'^\d+[-.\s]+', '', t)
    # Remove content in parenthesis/brackets
    t = re.sub(r'\(.*?\)', '', t)
    t = re.sub(r'\[.*?\]', '', t)
    # Remove "feat." and following
    t = re.sub(r'\bfeat\..*', '', t)
    # Remove non-alphanumeric chars (optional, maybe keep spaces)
    t = re.sub(r'[^\w\s]', '', t)
    return t.strip()

def normalize_artist(a):
    a = a.lower()
    # Remove "feat." and following
    a = re.sub(r'\bfeat\..*', '', a)
    return a.strip()

df['norm_title'] = df['clean_title_raw'].apply(normalize_title)
df['norm_artist'] = df['clean_artist'].apply(normalize_artist)

# Group by norm_artist and norm_title
grouped = df.groupby(['norm_artist', 'norm_title'])['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

# Display top 10
print("__RESULT__:")
print(grouped.head(10).to_json(orient='records'))"""

env_args = {'var_function-call-10791029874110747991': [{'COUNT(*)': '19375'}], 'var_function-call-10791029874110750228': [{'count(DISTINCT track_id)': '19375'}], 'var_function-call-8471687202024638385': 'file_storage/function-call-8471687202024638385.json', 'var_function-call-8471687202024637006': 'file_storage/function-call-8471687202024637006.json'}

exec(code, env_args)
