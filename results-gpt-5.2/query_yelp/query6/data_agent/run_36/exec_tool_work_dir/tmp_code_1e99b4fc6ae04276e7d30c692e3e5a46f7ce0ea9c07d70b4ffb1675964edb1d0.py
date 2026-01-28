code = """import json, re, pandas as pd

df = pd.DataFrame(var_call_vrWGX0jlriIZfSbvmKptrNqu)
df['avg_rating'] = df['avg_rating'].astype(float)
df['review_cnt'] = df['review_cnt'].astype(int)

dfb = pd.DataFrame(var_call_V5CGLZkdtOzTiDn6pufC8vvb)

# map businessref_X -> businessid_X
id_map = {row['business_ref']: 'businessid_' + row['business_ref'].split('_',1)[1] for _, row in df.iterrows()}
df['business_id'] = df['business_ref'].map(id_map)

merged = df.merge(dfb, on='business_id', how='left')

# extract category list from description after 'featuring' or 'in'
def extract_category(desc):
    if not isinstance(desc, str):
        return None
    m = re.search(r'featuring\s+([^\.]+)\.', desc, flags=re.IGNORECASE)
    if m:
        return m.group(1).strip()
    m = re.search(r'offers\s+.*?in\s+([^\.]+)\.', desc, flags=re.IGNORECASE)
    if m:
        return m.group(1).strip()
    return None

merged['category'] = merged['description'].apply(extract_category)

best = merged.sort_values(['avg_rating','review_cnt'], ascending=[False,False]).head(1).iloc[0]
out = {
    'business_name': best['name'],
    'business_ref': best['business_ref'],
    'avg_rating': float(best['avg_rating']),
    'review_count_in_period': int(best['review_cnt']),
    'category': best['category']
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_vrWGX0jlriIZfSbvmKptrNqu': [{'business_ref': 'businessref_9', 'avg_rating': '4.545454545454546', 'review_cnt': '11'}, {'business_ref': 'businessref_37', 'avg_rating': '3.6', 'review_cnt': '5'}], 'var_call_V5CGLZkdtOzTiDn6pufC8vvb': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}, {'business_id': 'businessid_37', 'name': 'Orangetheory Fitness Carrollwood', 'description': 'Located at 13122 N Dale Mabry Hwy in Tampa, FL, this facility offers a comprehensive range of services in Fitness & Instruction, Gyms, Boot Camps, Trainers, Active Life, and Interval Training Gyms.'}]}

exec(code, env_args)
