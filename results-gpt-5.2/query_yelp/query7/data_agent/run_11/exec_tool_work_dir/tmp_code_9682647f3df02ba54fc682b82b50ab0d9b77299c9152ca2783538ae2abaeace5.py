code = """import json, pandas as pd, re

reviews = pd.DataFrame(var_call_2CBKDzcU7jt7nr7GkfaE6tnX)
reviews['review_cnt'] = reviews['review_cnt'].astype(int)
reviews['business_id'] = reviews['business_ref'].str.replace('businessref_', 'businessid_', regex=False)

# load business docs from file
path = var_call_FYsdlrUOprJScBmmmV1jmhKm
with open(path, 'r') as f:
    biz_docs = json.load(f)
biz = pd.DataFrame(biz_docs)

# extract categories from description using simple split after 'categories of' or 'including'

def extract_categories(desc):
    if not isinstance(desc, str):
        return []
    m = re.search(r"(?:categories of|including|in the categories of)\s*(.*)", desc, flags=re.IGNORECASE)
    tail = m.group(1) if m else desc
    # remove location leading text
    tail = re.sub(r"^Located at[^,]*,?\s*", "", tail)
    # keep text after 'offers' if present
    if 'offers' in tail:
        tail = tail.split('offers',1)[-1]
    # find a segment with category-like comma-separated capitalized words
    # Use last sentence fragment
    tail = tail.split('making it',1)[0]
    tail = tail.replace("'","")
    parts = re.split(r"\.|;|:|\bperfect for\b", tail)
    cand = parts[0]
    # categories are often after 'including'
    if re.search(r"including", desc, re.I):
        cand = desc.split('including',1)[-1]
    cand = cand.replace('and',' , ')
    cats = [c.strip() for c in cand.split(',')]
    # filter obviously non-categories
    bad_prefix = ('Located at','This ','this ')
    out=[]
    for c in cats:
        c=re.sub(r"\s+",' ',c).strip()
        c=re.sub(r"^(a |an |the )",'',c,flags=re.I)
        if len(c)<2: continue
        if any(c.startswith(bp) for bp in bad_prefix): continue
        # remove trailing phrases
        c=re.sub(r"\bto meet.*$",'',c,flags=re.I).strip()
        c=re.sub(r"\bfor all.*$",'',c,flags=re.I).strip()
        if len(c)<2: continue
        out.append(c)
    # de-dup preserve order
    seen=set(); res=[]
    for c in out:
        if c not in seen:
            seen.add(c); res.append(c)
    return res

biz['cat_list'] = biz['description'].apply(extract_categories)

merged = reviews.merge(biz[['business_id','cat_list']], on='business_id', how='left')
rows=[]
for _, r in merged.iterrows():
    for c in (r['cat_list'] if isinstance(r['cat_list'], list) else []):
        rows.append((c, int(r['review_cnt'])))
cat_df = pd.DataFrame(rows, columns=['category','review_cnt'])

top5 = (cat_df.groupby('category', as_index=False)['review_cnt'].sum()
            .sort_values(['review_cnt','category'], ascending=[False, True])
            .head(5))

print('__RESULT__:')
print(json.dumps(top5.to_dict(orient='records')))"""

env_args = {'var_call_2CBKDzcU7jt7nr7GkfaE6tnX': [{'business_ref': 'businessref_13', 'review_cnt': '1'}, {'business_ref': 'businessref_79', 'review_cnt': '1'}, {'business_ref': 'businessref_6', 'review_cnt': '1'}, {'business_ref': 'businessref_15', 'review_cnt': '1'}, {'business_ref': 'businessref_33', 'review_cnt': '2'}, {'business_ref': 'businessref_36', 'review_cnt': '2'}, {'business_ref': 'businessref_60', 'review_cnt': '2'}, {'business_ref': 'businessref_12', 'review_cnt': '1'}, {'business_ref': 'businessref_31', 'review_cnt': '1'}, {'business_ref': 'businessref_53', 'review_cnt': '1'}, {'business_ref': 'businessref_74', 'review_cnt': '2'}, {'business_ref': 'businessref_66', 'review_cnt': '2'}, {'business_ref': 'businessref_57', 'review_cnt': '2'}, {'business_ref': 'businessref_86', 'review_cnt': '1'}, {'business_ref': 'businessref_62', 'review_cnt': '1'}, {'business_ref': 'businessref_37', 'review_cnt': '1'}, {'business_ref': 'businessref_26', 'review_cnt': '1'}, {'business_ref': 'businessref_68', 'review_cnt': '1'}, {'business_ref': 'businessref_92', 'review_cnt': '2'}, {'business_ref': 'businessref_41', 'review_cnt': '1'}, {'business_ref': 'businessref_10', 'review_cnt': '1'}, {'business_ref': 'businessref_45', 'review_cnt': '3'}, {'business_ref': 'businessref_96', 'review_cnt': '2'}, {'business_ref': 'businessref_98', 'review_cnt': '1'}, {'business_ref': 'businessref_14', 'review_cnt': '1'}, {'business_ref': 'businessref_20', 'review_cnt': '1'}], 'var_call_OhjG1AQ6yfWpSnh7X7et9NeG': [{'business_id': 'businessid_49'}, {'business_id': 'businessid_47'}, {'business_id': 'businessid_88'}, {'business_id': 'businessid_41'}, {'business_id': 'businessid_33'}, {'business_id': 'businessid_74'}, {'business_id': 'businessid_92'}, {'business_id': 'businessid_64'}, {'business_id': 'businessid_52'}, {'business_id': 'businessid_29'}, {'business_id': 'businessid_10'}, {'business_id': 'businessid_61'}, {'business_id': 'businessid_54'}, {'business_id': 'businessid_8'}, {'business_id': 'businessid_59'}, {'business_id': 'businessid_91'}, {'business_id': 'businessid_83'}, {'business_id': 'businessid_93'}, {'business_id': 'businessid_1'}, {'business_id': 'businessid_24'}, {'business_id': 'businessid_95'}, {'business_id': 'businessid_50'}, {'business_id': 'businessid_26'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_89'}, {'business_id': 'businessid_32'}, {'business_id': 'businessid_70'}, {'business_id': 'businessid_42'}, {'business_id': 'businessid_71'}, {'business_id': 'businessid_97'}, {'business_id': 'businessid_14'}, {'business_id': 'businessid_3'}, {'business_id': 'businessid_35'}, {'business_id': 'businessid_28'}, {'business_id': 'businessid_57'}, {'business_id': 'businessid_27'}, {'business_id': 'businessid_75'}, {'business_id': 'businessid_34'}, {'business_id': 'businessid_2'}, {'business_id': 'businessid_19'}, {'business_id': 'businessid_48'}, {'business_id': 'businessid_67'}, {'business_id': 'businessid_7'}, {'business_id': 'businessid_51'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_100'}, {'business_id': 'businessid_5'}, {'business_id': 'businessid_63'}, {'business_id': 'businessid_45'}, {'business_id': 'businessid_68'}, {'business_id': 'businessid_6'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_78'}, {'business_id': 'businessid_79'}, {'business_id': 'businessid_66'}, {'business_id': 'businessid_55'}, {'business_id': 'businessid_30'}, {'business_id': 'businessid_80'}, {'business_id': 'businessid_15'}, {'business_id': 'businessid_96'}, {'business_id': 'businessid_11'}, {'business_id': 'businessid_73'}, {'business_id': 'businessid_4'}, {'business_id': 'businessid_77'}, {'business_id': 'businessid_18'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_86'}, {'business_id': 'businessid_53'}, {'business_id': 'businessid_40'}, {'business_id': 'businessid_44'}, {'business_id': 'businessid_43'}, {'business_id': 'businessid_72'}, {'business_id': 'businessid_9'}, {'business_id': 'businessid_20'}, {'business_id': 'businessid_37'}, {'business_id': 'businessid_56'}, {'business_id': 'businessid_62'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_39'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_31'}, {'business_id': 'businessid_85'}, {'business_id': 'businessid_25'}, {'business_id': 'businessid_82'}, {'business_id': 'businessid_58'}, {'business_id': 'businessid_12'}, {'business_id': 'businessid_99'}, {'business_id': 'businessid_60'}, {'business_id': 'businessid_21'}, {'business_id': 'businessid_98'}, {'business_id': 'businessid_16'}, {'business_id': 'businessid_46'}, {'business_id': 'businessid_22'}, {'business_id': 'businessid_36'}, {'business_id': 'businessid_69'}, {'business_id': 'businessid_23'}, {'business_id': 'businessid_38'}, {'business_id': 'businessid_81'}, {'business_id': 'businessid_13'}, {'business_id': 'businessid_17'}], 'var_call_34fHWOgUJBDtZwdS2zTwRtdb': [], 'var_call_FYsdlrUOprJScBmmmV1jmhKm': 'file_storage/call_FYsdlrUOprJScBmmmV1jmhKm.json'}

exec(code, env_args)
