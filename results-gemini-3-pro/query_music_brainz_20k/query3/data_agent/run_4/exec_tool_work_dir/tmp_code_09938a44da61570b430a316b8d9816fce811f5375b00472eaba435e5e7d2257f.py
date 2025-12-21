code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-3331083869601689377'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-11133696600522148060'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

df_sales['track_id'] = df_sales['track_id'].astype(str)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

def normalize_text(text):
    if text is None:
        return ""
    text = str(text).lower().strip()
    text = re.sub(r'^\d+[\.\-\s]+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()

df['norm_title'] = df['title'].apply(normalize_text)

# Check for variants
groovey_matches = df[df['norm_title'].str.contains("groov", na=False)]
friends_matches = df[df['norm_title'].str.contains("all my friends say", na=False)]

print("__RESULT__:")
print(json.dumps({
    "groovey_variants": groovey_matches[['title', 'artist', 'total_revenue']].to_dict(orient='records'),
    "friends_variants": friends_matches[['title', 'artist', 'total_revenue']].to_dict(orient='records')
}))"""

env_args = {'var_function-call-3331083869601689377': 'file_storage/function-call-3331083869601689377.json', 'var_function-call-11133696600522148060': 'file_storage/function-call-11133696600522148060.json', 'var_function-call-2938307876171220754': [{'norm_title': '', 'norm_artist': 'unknown', 'total_revenue': 65286.36}, {'norm_title': 'none', 'norm_artist': 'unknown', 'total_revenue': 14647.52}, {'norm_title': 'groovey', 'norm_artist': 'rich matteson', 'total_revenue': 4379.75}, {'norm_title': 'all my friends say album version', 'norm_artist': 'luke bryan', 'total_revenue': 4311.59}, {'norm_title': 'the fire still burns', 'norm_artist': 'russ ballard', 'total_revenue': 4102.45}], 'var_function-call-9944138461387281347': [{'norm_title': 'groovey', 'norm_artist': 'rich matteson', 'total_revenue': 4379.75}, {'norm_title': 'all my friends say album version', 'norm_artist': 'luke bryan', 'total_revenue': 4311.59}, {'norm_title': 'the fire still burns', 'norm_artist': 'russ ballard', 'total_revenue': 4102.45}, {'norm_title': 'here i am nevins dirtyrock club mix reedit', 'norm_artist': 'sertab erener', 'total_revenue': 3863.69}, {'norm_title': 'happy together', 'norm_artist': 'the turtles', 'total_revenue': 3773.49}, {'norm_title': 'vostok', 'norm_artist': 'craig padilla', 'total_revenue': 3767.95}, {'norm_title': 'christmas in my heart', 'norm_artist': 'candi staton', 'total_revenue': 3744.97}, {'norm_title': 'september in the rain', 'norm_artist': 'the ralph sharon trio', 'total_revenue': 3732.72}, {'norm_title': 'the power of love rob searle club mix', 'norm_artist': 'frankie goes to hollywood', 'total_revenue': 3697.5299999999997}, {'norm_title': 'suddenly bt radio edit', 'norm_artist': 'bt', 'total_revenue': 3696.46}]}

exec(code, env_args)
