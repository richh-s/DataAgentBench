code = """import pandas as pd
import json
import re

with open(locals()['var_function-call-12792199908109322560'], 'r') as f:
    tracks = pd.DataFrame(json.load(f))

with open(locals()['var_function-call-4064444512275497395'], 'r') as f:
    sales = pd.DataFrame(json.load(f))

sales['revenue'] = pd.to_numeric(sales['total_revenue'])
sales['track_id'] = sales['track_id'].astype(str)
tracks['track_id'] = tracks['track_id'].astype(str)

df = pd.merge(sales, tracks, on='track_id', how='left')

def clean_str(s):
    if s is None:
        return ""
    return str(s).lower().strip()

def parse_artist_title(row):
    title = row['title']
    artist = row['artist']
    
    if artist is None or artist.lower() in ['none', '[unknown]', '']:
        if title and ' - ' in title:
            parts = title.split(' - ', 1)
            return clean_str(parts[0]), clean_str(parts[1])
        else:
            return "unknown", clean_str(title)
    
    return clean_str(artist), clean_str(title)

canonical_data = []
for _, row in df.iterrows():
    canonical_data.append(parse_artist_title(row))

df['clean_artist'] = [x[0] for x in canonical_data]
df['clean_title'] = [x[1] for x in canonical_data]

# Safer normalization: just remove specific punctuation or just whitespace
def normalize(s):
    # Remove punctuation characters but keep letters/numbers (unicode aware)
    # Using regex \w matches [a-zA-Z0-9_] and unicode alphanumerics depending on flags, 
    # but simplest is just remove specific punctuation or keep it simple.
    # Let's just strip extra whitespace and rely on lower case.
    # Maybe remove things in brackets? e.g. "(live)" or "(remix)"? 
    # The prompt warns about duplicates not matching exactly.
    # "The Rolling Stones" vs "Rolling Stones"?
    # Let's remove non-alphanumeric but keep unicode.
    # \W matches any character which is not a word character.
    # But in Python 3 re, with default flags, \w matches [a-zA-Z0-9_].
    # To match unicode we need to accept more.
    # Let's just remove specific punctuation: . , - ( ) [ ]
    s = re.sub(r'[\.\,\-\(\)\[\]]', '', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip()

df['norm_artist'] = df['clean_artist'].apply(normalize)
df['norm_title'] = df['clean_title'].apply(normalize)

df['group_key'] = df['norm_artist'] + "|||" + df['norm_title']

result = df.groupby('group_key')['revenue'].sum().reset_index()
result = result.sort_values('revenue', ascending=False)

top_entries = result.head(5).to_dict(orient='records')

# Get details for top 1
top_key = top_entries[0]['group_key']
rep_row = df[df['group_key'] == top_key].iloc[0]

output = {
    "top_song_key": top_key,
    "revenue": top_entries[0]['revenue'],
    "representative_title": rep_row['title'],
    "representative_artist": rep_row['artist'],
    "top_5": top_entries
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_function-call-4064444512275497395': 'file_storage/function-call-4064444512275497395.json', 'var_function-call-12792199908109322560': 'file_storage/function-call-12792199908109322560.json', 'var_function-call-6049788629291501520': {'top_song_key': '|||', 'revenue': 203103.18, 'representative_title': 'Приходи - Зн@менатель', 'representative_artist': 'Сплин', 'clean_title': 'приходи - зн@менатель', 'clean_artist': 'сплин'}}

exec(code, env_args)
