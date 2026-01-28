code = """import json
import pandas as pd
import string

# Load data files from storage variables
tracks_path = var_call_G6FzIukjR2235Ty5bjIQGYlP
sales_path = var_call_eYAcjsmmXFAqyHeMDoIpuKVU

with open(tracks_path, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
with open(sales_path, 'r', encoding='utf-8') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# normalize literal strings representing nulls
null_literals = set(['none', 'nan', '[unknown]', '', None])
for col in tracks_df.columns:
    tracks_df[col] = tracks_df[col].apply(lambda x: None if (x is None) or (isinstance(x, str) and x.strip().lower() in null_literals) else x)
for col in sales_df.columns:
    sales_df[col] = sales_df[col].apply(lambda x: None if (x is None) or (isinstance(x, str) and x.strip().lower() in null_literals) else x)

# types
tracks_df['track_id'] = tracks_df['track_id'].astype(int)
sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)

# simple extraction: if artist missing, and title contains ' - ' assume left is artist
def extract_fields(row):
    title = row.get('title') or ''
    artist = row.get('artist') or ''
    t = title
    a = artist
    if (a is None or str(a).strip()=='' ) and ' - ' in str(t):
        parts = str(t).split(' - ', 1)
        if len(parts)==2 and any(c.isalpha() for c in parts[0]):
            a = parts[0].strip()
            t = parts[1].strip()
    return t, a

tracks_df['ex_title'], tracks_df['ex_artist'] = zip(*tracks_df.apply(extract_fields, axis=1))

# normalization helper: lowercase, remove punctuation
trans = str.maketrans('', '', string.punctuation)

def normalize(s):
    if s is None:
        return ''
    s2 = str(s).lower().strip()
    s2 = s2.translate(trans)
    s2 = ' '.join(s2.split())
    return s2

tracks_df['norm_title'] = tracks_df['ex_title'].apply(normalize)
tracks_df['norm_artist'] = tracks_df['ex_artist'].apply(normalize)
tracks_df['norm_artist'] = tracks_df['norm_artist'].replace('', 'unknown')

tracks_df['canon_key'] = tracks_df['norm_title'] + '||' + tracks_df['norm_artist']

# representative title/artist per canonical key: choose first non-empty original
rep = tracks_df.groupby('canon_key').agg({'ex_title': lambda x: next((v for v in x if v and str(v).strip()), ''), 'ex_artist': lambda x: next((v for v in x if v and str(v).strip()), '')}).reset_index()

# map sales to canon
track_to_key = tracks_df.set_index('track_id')['canon_key'].to_dict()
sales_df['canon_key'] = sales_df['track_id'].map(track_to_key)
sales_df = sales_df[sales_df['canon_key'].notnull()]

# aggregate revenue by canon key
rev = sales_df.groupby('canon_key', dropna=False)['revenue_usd'].sum().reset_index()
rev = rev.merge(rep, on='canon_key', how='left')

if rev.shape[0]==0:
    result = {'title': None, 'artist': None, 'total_revenue_usd': 0.0}
else:
    rev['revenue_usd'] = rev['revenue_usd'].astype(float)
    max_row = rev.loc[rev['revenue_usd'].idxmax()]
    title = max_row['ex_title'] if max_row['ex_title']!='' else None
    artist = max_row['ex_artist'] if max_row['ex_artist']!='' else None
    result = {'title': title, 'artist': artist, 'total_revenue_usd': round(float(max_row['revenue_usd']), 2)}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_G6FzIukjR2235Ty5bjIQGYlP': 'file_storage/call_G6FzIukjR2235Ty5bjIQGYlP.json', 'var_call_eYAcjsmmXFAqyHeMDoIpuKVU': 'file_storage/call_eYAcjsmmXFAqyHeMDoIpuKVU.json'}

exec(code, env_args)
