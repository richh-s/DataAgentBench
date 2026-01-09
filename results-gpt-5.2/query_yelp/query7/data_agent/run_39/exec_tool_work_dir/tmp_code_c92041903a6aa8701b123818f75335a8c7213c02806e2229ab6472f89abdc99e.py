code = """import json, pandas as pd, re

# reviews counts by business_ref
reviews = pd.DataFrame(var_call_EHNSD0YqfT7ilnHB9alByXVA)
reviews['review_cnt'] = reviews['review_cnt'].astype(int)

# load businesses from file if needed
biz_data = var_call_cSxe9UorZLamdxI6dnU8CxvZ
if isinstance(biz_data, str):
    with open(biz_data, 'r', encoding='utf-8') as f:
        businesses = json.load(f)
else:
    businesses = biz_data
biz = pd.DataFrame(businesses)

# derive categories: prefer explicit fields if present, else parse from description after 'categories of'
def extract_categories(row):
    for key in ['categories','category']:
        if key in row and row[key] and isinstance(row[key], str):
            return [c.strip() for c in row[key].split(',') if c.strip()]
        if key in row and row[key] and isinstance(row[key], list):
            return [str(c).strip() for c in row[key] if str(c).strip()]
    desc = row.get('description')
    if isinstance(desc, str):
        # try to capture after 'services in' or 'categories of' up to period
        m = re.search(r"(?:services in|categories of|category of)\s+(.*?)(?:\.|$)", desc, flags=re.IGNORECASE)
        if m:
            txt = m.group(1)
            txt = txt.strip(" '“”\"")
            return [c.strip() for c in txt.split(',') if c.strip()]
    return []

biz['categories_list'] = biz.apply(lambda r: extract_categories(r.to_dict()), axis=1)

# map business_ref -> business_id
reviews['business_id'] = reviews['business_ref'].str.replace('businessref_', 'businessid_', regex=False)

merged = reviews.merge(biz[['business_id','categories_list']], on='business_id', how='left')
merged = merged.explode('categories_list')
merged = merged[merged['categories_list'].notna() & (merged['categories_list']!='')]

cat_totals = (merged.groupby('categories_list', as_index=False)['review_cnt'].sum()
              .sort_values(['review_cnt','categories_list'], ascending=[False, True]))

top5 = cat_totals.head(5)
result = top5.rename(columns={'categories_list':'category','review_cnt':'total_reviews'}).to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_EHNSD0YqfT7ilnHB9alByXVA': [{'business_ref': 'businessref_13', 'review_cnt': '1'}, {'business_ref': 'businessref_79', 'review_cnt': '1'}, {'business_ref': 'businessref_74', 'review_cnt': '2'}, {'business_ref': 'businessref_66', 'review_cnt': '2'}, {'business_ref': 'businessref_6', 'review_cnt': '1'}, {'business_ref': 'businessref_15', 'review_cnt': '1'}, {'business_ref': 'businessref_33', 'review_cnt': '2'}, {'business_ref': 'businessref_36', 'review_cnt': '2'}, {'business_ref': 'businessref_60', 'review_cnt': '2'}, {'business_ref': 'businessref_12', 'review_cnt': '1'}, {'business_ref': 'businessref_31', 'review_cnt': '1'}, {'business_ref': 'businessref_53', 'review_cnt': '1'}, {'business_ref': 'businessref_57', 'review_cnt': '2'}, {'business_ref': 'businessref_86', 'review_cnt': '1'}, {'business_ref': 'businessref_62', 'review_cnt': '1'}, {'business_ref': 'businessref_37', 'review_cnt': '1'}, {'business_ref': 'businessref_92', 'review_cnt': '2'}, {'business_ref': 'businessref_26', 'review_cnt': '1'}, {'business_ref': 'businessref_68', 'review_cnt': '1'}, {'business_ref': 'businessref_45', 'review_cnt': '3'}, {'business_ref': 'businessref_96', 'review_cnt': '2'}, {'business_ref': 'businessref_98', 'review_cnt': '1'}, {'business_ref': 'businessref_14', 'review_cnt': '1'}, {'business_ref': 'businessref_20', 'review_cnt': '1'}, {'business_ref': 'businessref_41', 'review_cnt': '1'}, {'business_ref': 'businessref_10', 'review_cnt': '1'}], 'var_call_cSxe9UorZLamdxI6dnU8CxvZ': 'file_storage/call_cSxe9UorZLamdxI6dnU8CxvZ.json'}

exec(code, env_args)
