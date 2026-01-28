code = """import json, pandas as pd, re

reviews = pd.DataFrame(var_call_2OwzcntsbNFMBevaleufna2F)
reviews['review_cnt'] = reviews['review_cnt'].astype(int)
reviews['business_id'] = reviews['business_ref'].str.replace('businessref_', 'businessid_', regex=False)

# Load businesses from json file
path = var_call_f23avzkli3GcgQquxJkEz9C9
with open(path, 'r', encoding='utf-8') as f:
    biz = json.load(f)

biz_df = pd.DataFrame(biz)

# derive categories from explicit field if present else parse from description tail after 'including'

def extract_cats(row):
    if 'categories' in row and row['categories'] not in (None, ''):
        c = row['categories']
        if isinstance(c, list):
            return c
        if isinstance(c, str):
            return [x.strip() for x in c.split(',') if x.strip()]
    desc = row.get('description')
    if not isinstance(desc, str):
        return []
    m = re.search(r'including (.+?)(?:\.|$)', desc, flags=re.IGNORECASE|re.DOTALL)
    if not m:
        m = re.search(r'categories? of (.+?)(?:\.|$)', desc, flags=re.IGNORECASE|re.DOTALL)
    if not m:
        return []
    part = m.group(1)
    part = part.replace(' and ', ', ')
    part = part.replace("'", "")
    cats = [x.strip() for x in part.split(',') if x.strip()]
    return cats

biz_df['cat_list'] = biz_df.apply(extract_cats, axis=1)

merged = reviews.merge(biz_df[['business_id','cat_list']], on='business_id', how='left')
merged = merged.explode('cat_list')
merged = merged.dropna(subset=['cat_list'])

cat_totals = merged.groupby('cat_list', as_index=False)['review_cnt'].sum().sort_values('review_cnt', ascending=False)

top5 = cat_totals.head(5)
result = top5.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_DnI8iplgqOO0Oe1ksLK3gARI': [{'user_id': 'userid_746'}, {'user_id': 'userid_1109'}, {'user_id': 'userid_1950'}, {'user_id': 'userid_1316'}, {'user_id': 'userid_1182'}, {'user_id': 'userid_151'}, {'user_id': 'userid_1158'}, {'user_id': 'userid_508'}, {'user_id': 'userid_435'}, {'user_id': 'userid_958'}, {'user_id': 'userid_1879'}, {'user_id': 'userid_308'}, {'user_id': 'userid_1179'}, {'user_id': 'userid_324'}, {'user_id': 'userid_863'}, {'user_id': 'userid_100'}, {'user_id': 'userid_1333'}, {'user_id': 'userid_1636'}, {'user_id': 'userid_1850'}, {'user_id': 'userid_711'}, {'user_id': 'userid_729'}, {'user_id': 'userid_1505'}, {'user_id': 'userid_1315'}, {'user_id': 'userid_1708'}, {'user_id': 'userid_1661'}, {'user_id': 'userid_850'}, {'user_id': 'userid_1675'}, {'user_id': 'userid_227'}, {'user_id': 'userid_577'}, {'user_id': 'userid_257'}, {'user_id': 'userid_598'}, {'user_id': 'userid_847'}, {'user_id': 'userid_673'}, {'user_id': 'userid_1856'}, {'user_id': 'userid_384'}, {'user_id': 'userid_935'}, {'user_id': 'userid_210'}, {'user_id': 'userid_1101'}, {'user_id': 'userid_945'}, {'user_id': 'userid_842'}, {'user_id': 'userid_1351'}, {'user_id': 'userid_230'}, {'user_id': 'userid_593'}, {'user_id': 'userid_1431'}, {'user_id': 'userid_686'}, {'user_id': 'userid_527'}, {'user_id': 'userid_244'}, {'user_id': 'userid_393'}, {'user_id': 'userid_1178'}, {'user_id': 'userid_526'}, {'user_id': 'userid_90'}, {'user_id': 'userid_238'}, {'user_id': 'userid_1105'}], 'var_call_ZhdgckPlZcGrn1K4L6xlw7JJ': ['checkin', 'business'], 'var_call_2OwzcntsbNFMBevaleufna2F': [{'business_ref': 'businessref_13', 'review_cnt': '1'}, {'business_ref': 'businessref_79', 'review_cnt': '1'}, {'business_ref': 'businessref_74', 'review_cnt': '2'}, {'business_ref': 'businessref_66', 'review_cnt': '2'}, {'business_ref': 'businessref_15', 'review_cnt': '1'}, {'business_ref': 'businessref_33', 'review_cnt': '2'}, {'business_ref': 'businessref_36', 'review_cnt': '2'}, {'business_ref': 'businessref_60', 'review_cnt': '2'}, {'business_ref': 'businessref_12', 'review_cnt': '1'}, {'business_ref': 'businessref_31', 'review_cnt': '1'}, {'business_ref': 'businessref_53', 'review_cnt': '1'}, {'business_ref': 'businessref_57', 'review_cnt': '2'}, {'business_ref': 'businessref_86', 'review_cnt': '1'}, {'business_ref': 'businessref_62', 'review_cnt': '1'}, {'business_ref': 'businessref_37', 'review_cnt': '1'}, {'business_ref': 'businessref_92', 'review_cnt': '2'}, {'business_ref': 'businessref_41', 'review_cnt': '1'}, {'business_ref': 'businessref_10', 'review_cnt': '1'}, {'business_ref': 'businessref_45', 'review_cnt': '3'}, {'business_ref': 'businessref_96', 'review_cnt': '2'}, {'business_ref': 'businessref_98', 'review_cnt': '1'}, {'business_ref': 'businessref_14', 'review_cnt': '1'}, {'business_ref': 'businessref_20', 'review_cnt': '1'}, {'business_ref': 'businessref_6', 'review_cnt': '1'}, {'business_ref': 'businessref_26', 'review_cnt': '1'}, {'business_ref': 'businessref_68', 'review_cnt': '1'}], 'var_call_f23avzkli3GcgQquxJkEz9C9': 'file_storage/call_f23avzkli3GcgQquxJkEz9C9.json'}

exec(code, env_args)
