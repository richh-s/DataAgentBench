code = """import json, pandas as pd

# load reviews (large) from file
path = var_call_rbPRpqlHONh0kt4ssCNRNk1r
with open(path, 'r') as f:
    reviews = json.load(f)

df = pd.DataFrame(reviews)
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
avg = df.groupby('gmap_id', as_index=False)['rating'].mean().rename(columns={'rating':'avg_rating'})
# filter avg>=4
avg = avg[avg['avg_rating'] >= 4.0].copy()

# Since no massage therapy businesses found in business_description by text search, return empty list
result = []
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_wh2YdOWUZ2rSeRIN4AR0hyqE': [], 'var_call_rbPRpqlHONh0kt4ssCNRNk1r': 'file_storage/call_rbPRpqlHONh0kt4ssCNRNk1r.json', 'var_call_qVcwOhNdnN8XKEhkAJG8opxY': []}

exec(code, env_args)
