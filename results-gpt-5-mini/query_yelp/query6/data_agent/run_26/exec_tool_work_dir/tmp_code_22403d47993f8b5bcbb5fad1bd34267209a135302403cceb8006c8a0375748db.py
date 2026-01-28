code = """import pandas as pd
import json
import datetime as dt

# Load the query_db result file path
path = var_call_eodFZgiCk2MAnJxGGDBoIAdi
# Read JSON
df = pd.read_json(path)

# Ensure rating numeric
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

# Initial parse with pandas
df['parsed'] = pd.to_datetime(df['date'], errors='coerce', infer_datetime_format=True)

# Define additional formats to try for unparsed dates
formats = [
    '%B %d, %Y at %I:%M %p',
    '%d %B %Y, %H:%M',
    '%Y-%m-%d %H:%M:%S',
    '%d %b %Y, %H:%M',
    '%d %b %Y, %H:%M:%S',
    '%B %d, %Y',
    '%d %B %Y',
    '%d %b %Y',
    '%Y-%m-%d',
]

mask = df['parsed'].isna()

def try_parse(x):
    for fmt in formats:
        try:
            return dt.datetime.strptime(x, fmt)
        except Exception:
            continue
    return pd.NaT

if mask.any():
    df.loc[mask, 'parsed'] = df.loc[mask, 'date'].apply(try_parse)

# Filter between 2016-01-01 and 2016-06-30 inclusive
start = pd.Timestamp('2016-01-01')
end = pd.Timestamp('2016-06-30 23:59:59')
mask_period = df['parsed'].notna() & df['parsed'].between(start, end)

df_period = df.loc[mask_period].copy()

# Group by business_ref
if df_period.empty:
    result = {'error': 'no_reviews_in_range'}
else:
    grp = df_period.groupby('business_ref').agg(cnt=('rating', 'size'), avg_rating=('rating', 'mean')).reset_index()
    grp = grp[grp['cnt'] >= 5]
    if grp.empty:
        result = {'error': 'no_business_with_min_reviews'}
    else:
        grp_sorted = grp.sort_values(by=['avg_rating', 'cnt'], ascending=[False, False]).reset_index(drop=True)
        top = grp_sorted.iloc[0]
        business_ref = top['business_ref']
        business_id = business_ref.replace('businessref_', 'businessid_')
        result = {
            'business_ref': business_ref,
            'business_id': business_id,
            'avg_rating': float(round(top['avg_rating'], 4)),
            'review_count_in_period': int(top['cnt'])
        }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_KQBxdG2747m3smLJmBLncixS': ['checkin', 'business'], 'var_call_ntTOrFGkEtp4mAZgtNUDTygk': ['review', 'tip', 'user'], 'var_call_eodFZgiCk2MAnJxGGDBoIAdi': 'file_storage/call_eodFZgiCk2MAnJxGGDBoIAdi.json'}

exec(code, env_args)
