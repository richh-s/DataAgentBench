code = """import json, pandas as pd, re

reviews = pd.DataFrame(var_call_U91T7ialAJ7rNXZq2sdclbIp)
reviews['review_cnt'] = reviews['review_cnt'].astype(int)

path = var_call_t2qPLLOnAQj8nKlwWwkaJcO1
with open(path, 'r') as f:
    biz = json.load(f)

biz_df = pd.DataFrame(biz)

# Extract categories from description: text after 'including' up to period
# Fallback: grab last clause after 'categories of'

def extract_cats(desc):
    if not isinstance(desc, str):
        return []
    m = re.search(r"including (.+?)\.", desc, flags=re.IGNORECASE)
    if not m:
        m = re.search(r"categories? of (.+?)\.", desc, flags=re.IGNORECASE)
    if not m:
        return []
    s = m.group(1)
    # remove quotes and conjunctions
    s = s.replace("'", "")
    parts = [p.strip() for p in s.split(',')]
    parts = [p for p in parts if p and p.lower() not in {'and'}]
    return parts

biz_df['categories'] = biz_df['description'].apply(extract_cats)

# Map business_ref -> business_id by prefix swap
reviews['business_id'] = reviews['business_ref'].str.replace('businessref_', 'businessid_', regex=False)

merged = reviews.merge(biz_df[['business_id','categories']], on='business_id', how='left')
merged = merged.explode('categories')
merged = merged.dropna(subset=['categories'])
merged['categories'] = merged['categories'].astype(str)

cat_totals = merged.groupby('categories', as_index=False)['review_cnt'].sum().sort_values('review_cnt', ascending=False)

top5 = cat_totals.head(5)
result = top5.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_U91T7ialAJ7rNXZq2sdclbIp': [{'business_ref': 'businessref_13', 'review_cnt': '1'}, {'business_ref': 'businessref_79', 'review_cnt': '1'}, {'business_ref': 'businessref_74', 'review_cnt': '2'}, {'business_ref': 'businessref_66', 'review_cnt': '2'}, {'business_ref': 'businessref_15', 'review_cnt': '1'}, {'business_ref': 'businessref_33', 'review_cnt': '2'}, {'business_ref': 'businessref_31', 'review_cnt': '1'}, {'business_ref': 'businessref_53', 'review_cnt': '1'}, {'business_ref': 'businessref_57', 'review_cnt': '2'}, {'business_ref': 'businessref_86', 'review_cnt': '1'}, {'business_ref': 'businessref_62', 'review_cnt': '1'}, {'business_ref': 'businessref_37', 'review_cnt': '1'}, {'business_ref': 'businessref_92', 'review_cnt': '2'}, {'business_ref': 'businessref_26', 'review_cnt': '1'}, {'business_ref': 'businessref_68', 'review_cnt': '1'}, {'business_ref': 'businessref_41', 'review_cnt': '1'}, {'business_ref': 'businessref_10', 'review_cnt': '1'}, {'business_ref': 'businessref_45', 'review_cnt': '3'}, {'business_ref': 'businessref_96', 'review_cnt': '2'}, {'business_ref': 'businessref_98', 'review_cnt': '1'}, {'business_ref': 'businessref_14', 'review_cnt': '1'}, {'business_ref': 'businessref_20', 'review_cnt': '1'}, {'business_ref': 'businessref_6', 'review_cnt': '1'}, {'business_ref': 'businessref_36', 'review_cnt': '2'}, {'business_ref': 'businessref_60', 'review_cnt': '2'}, {'business_ref': 'businessref_12', 'review_cnt': '1'}], 'var_call_t2qPLLOnAQj8nKlwWwkaJcO1': 'file_storage/call_t2qPLLOnAQj8nKlwWwkaJcO1.json'}

exec(code, env_args)
