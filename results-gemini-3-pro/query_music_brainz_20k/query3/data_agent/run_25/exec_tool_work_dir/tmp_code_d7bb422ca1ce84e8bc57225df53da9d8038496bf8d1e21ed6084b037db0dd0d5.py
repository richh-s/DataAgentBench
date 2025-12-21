code = """import json
import pandas as pd
import re

# Load data
with open(var_function_call_4051379680636231128, 'r') as f:
    sales_data = json.load(f)
with open(var_function_call_8323022647669375919, 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_sales['revenue_usd'] = pd.to_numeric(df_sales['total_revenue'])

df_tracks = pd.DataFrame(tracks_data)

# Merge
df = pd.merge(df_sales, df_tracks, on='track_id')

# Helper to normalize
def clean_str(s):
    if not s or s.lower() in ['none', '[unknown]', 'unknown']:
        return ""
    # Remove non-alphanumeric
    return re.sub(r'[^a-z0-9]', '', s.lower())

def extract_artist_title(row):
    t = row['title']
    a = row['artist']
    
    # Handle missing artist by checking "Artist - Title" pattern in title
    if (not a or a.lower() in ['none', '[unknown]', 'unknown']) and t and ' - ' in t:
        parts = t.split(' - ', 1)
        # Assume first part is artist
        a = parts[0]
        t = parts[1]
    
    # Clean
    t_clean = clean_str(t)
    a_clean = clean_str(a)
    
    return a_clean, t_clean, t, a

results = {}

for idx, row in df.iterrows():
    a_clean, t_clean, t_orig, a_orig = extract_artist_title(row)
    
    # Key for grouping
    # If artist is still empty, just use title. 
    # But risky if title is generic. 
    # Let's use tuple.
    key = (a_clean, t_clean)
    
    rev = row['revenue_usd']
    
    if key not in results:
        results[key] = {
            'total_revenue': 0.0,
            'titles': [],
            'artists': []
        }
    
    results[key]['total_revenue'] += rev
    results[key]['titles'].append(t_orig)
    results[key]['artists'].append(a_orig)

# Convert to list
final_list = []
for key, val in results.items():
    # Pick most common title/artist for display
    from collections import Counter
    # Filter out None/bad values for display
    valid_titles = [x for x in val['titles'] if x and x.lower() != 'none']
    valid_artists = [x for x in val['artists'] if x and x.lower() not in ['none', '[unknown]']]
    
    disp_title = Counter(valid_titles).most_common(1)[0][0] if valid_titles else (val['titles'][0] if val['titles'] else "Unknown")
    disp_artist = Counter(valid_artists).most_common(1)[0][0] if valid_artists else (val['artists'][0] if val['artists'] else "Unknown")
    
    final_list.append({
        'key': key,
        'revenue': val['total_revenue'],
        'display_title': disp_title,
        'display_artist': disp_artist
    })

# Sort by revenue
final_list.sort(key=lambda x: x['revenue'], reverse=True)

print("__RESULT__:")
print(json.dumps(final_list[:10]))"""

env_args = {'var_function-call-4051379680636231128': 'file_storage/function-call-4051379680636231128.json', 'var_function-call-8323022647669375919': 'file_storage/function-call-8323022647669375919.json'}

exec(code, env_args)
