code = """import json, re, pandas as pd

path = var_call_T510Ao6i0TxmddffPDTMhiVD
with open(path, 'r', encoding='utf-8') as f:
    biz_docs = json.load(f)

rev = pd.DataFrame(var_call_ZP3ZSc7Fi2jCZf32I1KdCQDC)
if rev.empty:
    top5 = []
else:
    rev['review_cnt'] = rev['review_cnt'].astype(int)

    biz = pd.DataFrame([{'business_id': d.get('business_id'), 'description': d.get('description','')} for d in biz_docs])
    rev['business_id'] = rev['business_ref'].str.replace('businessref_', 'businessid_', regex=False)
    merged = rev.merge(biz, on='business_id', how='left')

    def extract_cats(desc):
        if not isinstance(desc, str):
            return []
        m = re.search(r"categories? of (.*)$", desc, flags=re.IGNORECASE)
        if not m:
            m = re.search(r"services in (.*)$", desc, flags=re.IGNORECASE)
        if not m:
            return []
        s = m.group(1).strip()
        s = re.sub(r"\.$", "", s)
        s = re.sub(r"^the categories of ", "", s, flags=re.IGNORECASE).strip()
        parts = [p.strip() for p in s.split(',')]
        # remove surrounding quotes without using backslash escapes
        cleaned = []
        for p in parts:
            if len(p) >= 2 and ((p[0]==p[-1] and p[0] in ["'", '"'])):
                p = p[1:-1]
            cleaned.append(p.strip())
        return [p for p in cleaned if p]

    rows = []
    for _, r in merged.iterrows():
        for c in extract_cats(r.get('description','')):
            rows.append({'category': c, 'review_cnt': int(r['review_cnt'])})

    cat_df = pd.DataFrame(rows)
    if cat_df.empty:
        top5 = []
    else:
        top5 = (cat_df.groupby('category', as_index=False)['review_cnt'].sum()
                .sort_values(['review_cnt','category'], ascending=[False, True])
                .head(5)
                .to_dict(orient='records'))

print('__RESULT__:')
print(json.dumps(top5))"""

env_args = {'var_call_KTlrlFaUWiQLTKcVcPlUk7d2': ['review', 'tip', 'user'], 'var_call_PRAfoJJEJTDOPFMNcbslcWv8': ['checkin', 'business'], 'var_call_ZP3ZSc7Fi2jCZf32I1KdCQDC': [{'business_ref': 'businessref_13', 'review_cnt': '1'}, {'business_ref': 'businessref_79', 'review_cnt': '1'}, {'business_ref': 'businessref_74', 'review_cnt': '2'}, {'business_ref': 'businessref_66', 'review_cnt': '2'}, {'business_ref': 'businessref_15', 'review_cnt': '1'}, {'business_ref': 'businessref_33', 'review_cnt': '2'}, {'business_ref': 'businessref_36', 'review_cnt': '2'}, {'business_ref': 'businessref_60', 'review_cnt': '2'}, {'business_ref': 'businessref_12', 'review_cnt': '1'}, {'business_ref': 'businessref_6', 'review_cnt': '1'}, {'business_ref': 'businessref_31', 'review_cnt': '1'}, {'business_ref': 'businessref_53', 'review_cnt': '1'}, {'business_ref': 'businessref_57', 'review_cnt': '2'}, {'business_ref': 'businessref_86', 'review_cnt': '1'}, {'business_ref': 'businessref_62', 'review_cnt': '1'}, {'business_ref': 'businessref_37', 'review_cnt': '1'}, {'business_ref': 'businessref_26', 'review_cnt': '1'}, {'business_ref': 'businessref_68', 'review_cnt': '1'}, {'business_ref': 'businessref_41', 'review_cnt': '1'}, {'business_ref': 'businessref_10', 'review_cnt': '1'}, {'business_ref': 'businessref_96', 'review_cnt': '2'}, {'business_ref': 'businessref_98', 'review_cnt': '1'}, {'business_ref': 'businessref_14', 'review_cnt': '1'}, {'business_ref': 'businessref_20', 'review_cnt': '1'}, {'business_ref': 'businessref_45', 'review_cnt': '3'}, {'business_ref': 'businessref_92', 'review_cnt': '2'}], 'var_call_T510Ao6i0TxmddffPDTMhiVD': 'file_storage/call_T510Ao6i0TxmddffPDTMhiVD.json'}

exec(code, env_args)
