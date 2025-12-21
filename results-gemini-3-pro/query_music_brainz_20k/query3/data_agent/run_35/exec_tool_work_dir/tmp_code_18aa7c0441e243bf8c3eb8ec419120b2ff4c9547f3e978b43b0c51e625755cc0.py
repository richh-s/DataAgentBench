code = """import json
import re
import pandas as pd

# Load data
with open(locals()['var_function-call-2634326689479579170'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-2634326689479580217'], 'r') as f:
    tracks_data = json.load(f)

# Convert to DataFrames
df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

# Convert revenue to float
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])

# Merge sales and tracks
# We want to keep all sales, so left join on sales.
# (Though all sold tracks should exist in tracks table, hopefully)
df_merged = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Normalization function
def normalize_text(text):
    if not isinstance(text, str):
        return ""
    # Lowercase
    text = text.lower()
    # Remove text in parentheses/brackets (e.g., "(live)", "[remix]")
    # This might be aggressive if the title is ONLY inside parentheses, but usually it's "Title (info)"
    text = re.sub(r'\([^)]*\)', '', text)
    text = re.sub(r'\[[^]]*\]', '', text)
    # Remove leading numbering like "01-", "01 ", "1.", "001-"
    text = re.sub(r'^\s*\d+[\.\-\s]+', '', text)
    # Remove special characters / punctuation (keep alphanumeric and spaces)
    text = re.sub(r'[^\w\s]', ' ', text)
    # Replace multiple spaces with single space
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def clean_artist(text):
    if not isinstance(text, str):
        return "unknown"
    norm = normalize_text(text)
    if norm in ["none", "unknown", "", "null"]:
        return "unknown"
    return norm

# Apply normalization
df_merged['norm_title'] = df_merged['title'].apply(normalize_text)
df_merged['norm_artist'] = df_merged['artist'].apply(clean_artist)

# Filter out rows where title became empty (if any)
df_merged = df_merged[df_merged['norm_title'] != ""]

# Group by normalized title and artist
# If artist is unknown, we might group purely by title, or keep it as a separate group "title - unknown".
# Given the query asks for "Which song", usually title + artist defines the song.
# If artist is unknown, it's risky to merge with other unknown artists with same title, but maybe duplicate tracks have the same (unknown) artist.
grouped = df_merged.groupby(['norm_title', 'norm_artist'])['total_revenue'].sum().reset_index()

# Sort by revenue
grouped = grouped.sort_values(by='total_revenue', ascending=False)

# Get top result
top_song = grouped.iloc[0]

# Retrieve original title/artist for the top group to display nicely
# We can find one example from the original dataframe that matches the normalized keys
mask = (df_merged['norm_title'] == top_song['norm_title']) & (df_merged['norm_artist'] == top_song['norm_artist'])
original_example = df_merged[mask].iloc[0]

result = {
    "norm_title": top_song['norm_title'],
    "norm_artist": top_song['norm_artist'],
    "revenue": top_song['total_revenue'],
    "example_title": original_example['title'],
    "example_artist": original_example['artist']
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-2634326689479579170': 'file_storage/function-call-2634326689479579170.json', 'var_function-call-2634326689479580217': 'file_storage/function-call-2634326689479580217.json'}

exec(code, env_args)
