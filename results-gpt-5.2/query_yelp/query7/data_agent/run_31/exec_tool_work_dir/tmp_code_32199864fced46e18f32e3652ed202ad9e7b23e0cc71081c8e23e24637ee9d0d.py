code = """import json, re, pandas as pd

rev = pd.DataFrame(var_call_DwS3KlY4thYYyT24H7ClNXzh)
rev['review_count'] = rev['review_count'].astype(int)

biz_src = var_call_pGWO7eLiKDU3lrgV9yXyfZTA
if isinstance(biz_src, str):
    with open(biz_src, 'r') as f:
        biz_records = json.load(f)
else:
    biz_records = biz_src
biz = pd.DataFrame(biz_records)

pat = re.compile(r'(?:services in|categories of)\s+([^\.]+)', re.IGNORECASE)

def extract_cats(desc):
    if not isinstance(desc, str):
        return []
    m = pat.search(desc)
    if not m:
        return []
    s = m.group(1)
    s = s.replace(' and ', ', ')
    parts = [p.strip(" \"'") for p in s.split(',')]
    return [p for p in parts if p]

biz['cats'] = biz['description'].apply(extract_cats)
biz['biz_suffix'] = biz['business_id'].str.replace('businessid_','', regex=False)

merged = rev.merge(biz[['biz_suffix','cats']], on='biz_suffix', how='left')
exp = merged.explode('cats').dropna(subset=['cats'])
cat_counts = exp.groupby('cats', as_index=False)['review_count'].sum().sort_values('review_count', ascending=False)

top5 = cat_counts.head(5)
print('__RESULT__:')
print(json.dumps(top5.to_dict(orient='records')))"""

env_args = {'var_call_DwS3KlY4thYYyT24H7ClNXzh': [{'biz_suffix': '41', 'review_count': '1'}, {'biz_suffix': '98', 'review_count': '1'}, {'biz_suffix': '74', 'review_count': '2'}, {'biz_suffix': '92', 'review_count': '2'}, {'biz_suffix': '26', 'review_count': '1'}, {'biz_suffix': '13', 'review_count': '1'}, {'biz_suffix': '79', 'review_count': '1'}, {'biz_suffix': '96', 'review_count': '2'}, {'biz_suffix': '86', 'review_count': '1'}, {'biz_suffix': '53', 'review_count': '1'}, {'biz_suffix': '20', 'review_count': '1'}, {'biz_suffix': '15', 'review_count': '1'}, {'biz_suffix': '36', 'review_count': '2'}, {'biz_suffix': '6', 'review_count': '1'}, {'biz_suffix': '12', 'review_count': '1'}, {'biz_suffix': '45', 'review_count': '3'}, {'biz_suffix': '57', 'review_count': '2'}, {'biz_suffix': '60', 'review_count': '2'}, {'biz_suffix': '62', 'review_count': '1'}, {'biz_suffix': '37', 'review_count': '1'}, {'biz_suffix': '31', 'review_count': '1'}, {'biz_suffix': '68', 'review_count': '1'}, {'biz_suffix': '66', 'review_count': '2'}, {'biz_suffix': '14', 'review_count': '1'}, {'biz_suffix': '10', 'review_count': '1'}, {'biz_suffix': '33', 'review_count': '2'}], 'var_call_pGWO7eLiKDU3lrgV9yXyfZTA': 'file_storage/call_pGWO7eLiKDU3lrgV9yXyfZTA.json'}

exec(code, env_args)
