code = """import json, re, pandas as pd

# reviews per business_ref from DuckDB
rev = pd.DataFrame(var_call_GpdgAF6N0KRAU6iGKXHG9TkZ)
rev['review_cnt'] = rev['review_cnt'].astype(int)
# convert businessref_X -> businessid_X
rev['business_id'] = rev['business_ref'].str.replace('businessref_', 'businessid_', regex=False)

# load businesses from mongo result file
path = var_call_PqJb15DHM9zZ90xRRb404HqP
with open(path, 'r', encoding='utf-8') as f:
    biz = json.load(f)
biz_df = pd.DataFrame(biz)[['business_id','description']]

# extract categories after 'categories of' or 'category of'
pattern = re.compile(r"categor(?:y|ies) of (.*?)(?:\.|$)", re.IGNORECASE | re.DOTALL)

def extract_cats(desc):
    if not isinstance(desc, str):
        return []
    m = pattern.search(desc)
    if not m:
        # fallback: try 'including' list
        m2 = re.search(r"including (.*?)(?:\.|$)", desc, flags=re.IGNORECASE|re.DOTALL)
        if not m2:
            return []
        s = m2.group(1)
    else:
        s = m.group(1)
    s = s.replace("'", "")
    parts = [p.strip() for p in s.split(',')]
    out=[]
    for p in parts:
        if not p:
            continue
        # drop leading conjunctions
        p = re.sub(r"^(and|to)\s+", "", p, flags=re.IGNORECASE).strip()
        if p:
            out.append(p)
    return out

biz_df['categories'] = biz_df['description'].map(extract_cats)

merged = rev.merge(biz_df, on='business_id', how='left')
expl = merged.explode('categories')
expl = expl.dropna(subset=['categories'])
cat_totals = expl.groupby('categories', as_index=False)['review_cnt'].sum().sort_values('review_cnt', ascending=False)

top5 = cat_totals.head(5)
result = top5.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_QqJ3htiUxPVaptebsn4TA9Ch': ['review', 'tip', 'user'], 'var_call_9335pl3EVda1s3GM0F35Yb1h': ['business', 'checkin'], 'var_call_GpdgAF6N0KRAU6iGKXHG9TkZ': [{'business_ref': 'businessref_13', 'review_cnt': '1'}, {'business_ref': 'businessref_79', 'review_cnt': '1'}, {'business_ref': 'businessref_74', 'review_cnt': '2'}, {'business_ref': 'businessref_66', 'review_cnt': '2'}, {'business_ref': 'businessref_15', 'review_cnt': '1'}, {'business_ref': 'businessref_33', 'review_cnt': '2'}, {'business_ref': 'businessref_6', 'review_cnt': '1'}, {'business_ref': 'businessref_36', 'review_cnt': '2'}, {'business_ref': 'businessref_60', 'review_cnt': '2'}, {'business_ref': 'businessref_12', 'review_cnt': '1'}, {'business_ref': 'businessref_31', 'review_cnt': '1'}, {'business_ref': 'businessref_53', 'review_cnt': '1'}, {'business_ref': 'businessref_57', 'review_cnt': '2'}, {'business_ref': 'businessref_86', 'review_cnt': '1'}, {'business_ref': 'businessref_62', 'review_cnt': '1'}, {'business_ref': 'businessref_37', 'review_cnt': '1'}, {'business_ref': 'businessref_92', 'review_cnt': '2'}, {'business_ref': 'businessref_26', 'review_cnt': '1'}, {'business_ref': 'businessref_68', 'review_cnt': '1'}, {'business_ref': 'businessref_41', 'review_cnt': '1'}, {'business_ref': 'businessref_10', 'review_cnt': '1'}, {'business_ref': 'businessref_45', 'review_cnt': '3'}, {'business_ref': 'businessref_96', 'review_cnt': '2'}, {'business_ref': 'businessref_98', 'review_cnt': '1'}, {'business_ref': 'businessref_14', 'review_cnt': '1'}, {'business_ref': 'businessref_20', 'review_cnt': '1'}], 'var_call_PqJb15DHM9zZ90xRRb404HqP': 'file_storage/call_PqJb15DHM9zZ90xRRb404HqP.json'}

exec(code, env_args)
