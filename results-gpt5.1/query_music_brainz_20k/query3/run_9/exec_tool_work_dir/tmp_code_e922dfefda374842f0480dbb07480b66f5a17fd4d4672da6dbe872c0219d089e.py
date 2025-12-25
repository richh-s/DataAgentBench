code = """import json, pandas as pd

with open(var_call_eAbl87riO9C50I6r8WYYp1Wr, 'r') as f:
    tracks = pd.DataFrame(json.load(f))
with open(var_call_VRAVcWeTEQ0ay2IfBgsMCmLG, 'r') as f:
    sales = pd.DataFrame(json.load(f))

# Fix dtypes for numeric fields safely
def to_int_safe(s):
    try:
        return int(s)
    except Exception:
        return None

sales['track_id'] = sales['track_id'].apply(to_int_safe)
tracks['track_id'] = tracks['track_id'].apply(to_int_safe)

# Clean revenue_usd: ensure numeric, coerce errors to NaN then fill 0
sales['revenue_usd'] = pd.to_numeric(sales['revenue_usd'], errors='coerce').fillna(0.0)

# Basic cleaning for entity resolution
for col in ['title','artist','album','year','language']:
    tracks[col] = tracks[col].astype(str).str.strip().str.lower()

tracks['canon_key'] = tracks['title'] + '|' + tracks['artist']
none_like = set(['none','[unknown]','nan',''])
mask_simple = tracks['artist'].isin(none_like)
tracks.loc[mask_simple, 'canon_key'] = tracks.loc[mask_simple, 'title']

track_to_key = tracks.set_index('track_id')['canon_key']

sales = sales.merge(track_to_key.rename('canon_key'), left_on='track_id', right_index=True, how='left')

agg = sales.groupby('canon_key', dropna=False)['revenue_usd'].sum().reset_index()

meta = tracks.groupby('canon_key').agg({
    'title': lambda x: x.mode().iloc[0] if not x.mode().empty else x.iloc[0],
    'artist': lambda x: x.mode().iloc[0] if not x.mode().empty else x.iloc[0]
}).reset_index()

result = agg.merge(meta, on='canon_key', how='left')

idx = result['revenue_usd'].idxmax()
row = result.loc[idx]

answer = {
    'title': row['title'],
    'artist': row['artist'],
    'total_revenue_usd': float(row['revenue_usd'])
}

out = json.dumps(answer)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_eAbl87riO9C50I6r8WYYp1Wr': 'file_storage/call_eAbl87riO9C50I6r8WYYp1Wr.json', 'var_call_VRAVcWeTEQ0ay2IfBgsMCmLG': 'file_storage/call_VRAVcWeTEQ0ay2IfBgsMCmLG.json', 'var_call_U4ujmcCMuMYqKUrow8OTZDMN': ['tracks'], 'var_call_z6w5fqyp3wHBzdOWne92oERI': ['sales']}

exec(code, env_args)
