code = """import json, re, pandas as pd

with open(var_call_rWm2Cmud0IFfuaXolk88ya99, 'r') as f:
    business_data = json.load(f)
with open(var_call_PKusBbTTfo6UnBTeje8wlkuZ, 'r') as f:
    review_data = json.load(f)

state_pattern = re.compile(r',\s*([A-Z]{2})\b')
rows = []
for b in business_data:
    desc = b.get('description') or ''
    m = state_pattern.search(desc)
    if not m:
        continue
    state = m.group(1)
    bid = b['business_id']
    rows.append({'business_id': bid, 'state': state})

biz_df = pd.DataFrame(rows)

review_rows = []
for r in review_data:
    bref = r['business_ref']
    num = bref.replace('businessref_', '')
    bid = 'businessid_' + num
    review_rows.append({'business_id': bid, 'rating': int(r['rating'])})

rev_df = pd.DataFrame(review_rows)

merged = rev_df.merge(biz_df, on='business_id', how='inner')

agg = merged.groupby('state').agg(review_count=('rating', 'size'), avg_rating=('rating', 'mean')).reset_index()

top = agg.sort_values(['review_count', 'state'], ascending=[False, True]).iloc[0]

result = {
    'state': top['state'],
    'review_count': int(top['review_count']),
    'average_rating': round(float(top['avg_rating']), 3)
}

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_Bxs950sZ5rio9iVFYpZeb92a': 'file_storage/call_Bxs950sZ5rio9iVFYpZeb92a.json', 'var_call_PKusBbTTfo6UnBTeje8wlkuZ': 'file_storage/call_PKusBbTTfo6UnBTeje8wlkuZ.json', 'var_call_rWm2Cmud0IFfuaXolk88ya99': 'file_storage/call_rWm2Cmud0IFfuaXolk88ya99.json', 'var_call_c3QaRDkGeChs0yDmPTtLk4FC': {'sample_keys': ['business_id', 'description']}}

exec(code, env_args)
