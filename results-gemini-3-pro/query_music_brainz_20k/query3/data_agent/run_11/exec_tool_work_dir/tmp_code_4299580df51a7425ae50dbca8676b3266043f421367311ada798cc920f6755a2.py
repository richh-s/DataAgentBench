code = """import pandas as pd
import json
import re

# Load data
with open('var_function-call-16976298203827158307.json', 'r') as f:
    sales_data = json.load(f)
with open('var_function-call-10581686767626383820.json', 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])

df_tracks = pd.DataFrame(tracks_data)

# Merge
df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Basic cleaning function
def clean_string(s):
    if not s or s == 'None' or s == '[unknown]':
        return ''
    return str(s).lower().strip()

def normalize_title(title):
    if not title: return ""
    s = title.lower()
    # Remove track numbers like "01 -", "001-", "1." at start
    s = re.sub(r'^\d+[\s\.\-]*', '', s)
    # Remove content in parenthesis/brackets often used for extra info
    # But be careful not to remove essential title parts. 
    # Valid song names: "(I Can't Get No) Satisfaction". 
    # Metadata: "Title (live)", "Title (remix)", "Title (2008 remastered)".
    # For now, let's keep it simple: strip specific keywords or just trim whitespace.
    # Actually, the hint mentions "different year formats or minor attribute variations".
    # Let's try to strip purely metadata-like parens if possible, or just exact match on cleaned string.
    # Let's try aggressive cleaning: remove everything in parens?
    # No, "(Sittin' On) The Dock of the Bay".
    # Let's just normalize whitespace and case first.
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def normalize_artist(artist):
    if not artist or artist in ['None', '[unknown]']:
        return None
    return artist.lower().strip()

# Apply cleaning
df['clean_title'] = df['title'].apply(normalize_title)
df['clean_artist'] = df['artist'].apply(normalize_artist)

# Handle "Artist - Title" in title if artist is missing
# (This is a heuristic based on the data preview: "Daniel Balavoine - L'enfant aux yeux d'Italie")
def extract_artist_title(row):
    t = row['clean_title']
    a = row['clean_artist']
    
    if not a and ' - ' in t:
        parts = t.split(' - ', 1)
        return parts[0].strip(), parts[1].strip() # New artist, New title
    
    return a, t

# Apply extraction
extracted = df.apply(extract_artist_title, axis=1)
df['final_artist'] = [x[0] for x in extracted]
df['final_title'] = [x[1] for x in extracted]

# Now, group by final_artist and final_title
# Fill NA artist with 'unknown' for grouping
df['group_artist'] = df['final_artist'].fillna('unknown')
df['group_title'] = df['final_title']

# Aggregation
grouped = df.groupby(['group_artist', 'group_title'])['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

print("__RESULT__:")
print(grouped.head(20).to_json(orient='records'))"""

env_args = {'var_function-call-16976298203827158307': 'file_storage/function-call-16976298203827158307.json', 'var_function-call-10581686767626383820': 'file_storage/function-call-10581686767626383820.json'}

exec(code, env_args)
