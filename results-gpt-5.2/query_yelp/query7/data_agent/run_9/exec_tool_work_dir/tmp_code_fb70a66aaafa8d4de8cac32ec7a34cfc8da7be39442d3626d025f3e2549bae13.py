code = """import json, re, pandas as pd

# load reviews counts by business_ref
reviews = var_call_nUqi0mgV7W1SMZyGSmc6zggB
rdf = pd.DataFrame(reviews)
if rdf.empty:
    out = json.dumps([])
    print('__RESULT__:')
    print(out)
    raise SystemExit

rdf['review_cnt'] = pd.to_numeric(rdf['review_cnt'])

# load businesses metadata from file
path = var_call_vvWGBR2LEwErnhjwIf7W2dhg
with open(path, 'r', encoding='utf-8') as f:
    biz = json.load(f)
bdf = pd.DataFrame(biz)

# derive categories from description (the dataset doesn't expose a categories field)
cat_re = re.compile(r"provid(?:ing|es) (?:a range of services in|essential services in the categories of|a diverse range of services and products in the fields of|a range of services including|a range of services in the categories of|a range of services in|a diverse selection of|a delightful array of options ranging from|a delightful mix of|a range of services|a diverse range of services|a diverse selection of|a range of|a premier destination for|a variety of services including|a variety of services|a selection of|a destination for)\s*(.*?)(?:\.|$)", re.IGNORECASE)

cats = []
for desc in bdf.get('description', pd.Series([None]*len(bdf))).fillna('').tolist():
    m = cat_re.search(desc)
    if m:
        tail = m.group(1)
        # strip location phrases
        tail = re.sub(r"\s*Located at.*", "", tail, flags=re.IGNORECASE)
        # split
        parts = [p.strip(" '\"") for p in re.split(r",|\band\b", tail) if p.strip(" '\"")]
        parts = [p for p in parts if len(p)>0]
        # de-dup while preserving order
        seen=set(); uniq=[]
        for p in parts:
            if p not in seen:
                seen.add(p); uniq.append(p)
        cats.append(uniq)
    else:
        # attempt: look for "offers" then list
        m2 = re.search(r"offers (?:a|an) .*? in (.*?)(?:\.|$)", desc, flags=re.IGNORECASE)
        if m2:
            tail=m2.group(1)
            parts=[p.strip(" '\"") for p in re.split(r",|\band\b", tail) if p.strip(" '\"")]
            cats.append(parts)
        else:
            cats.append([])

bdf['categories_list'] = cats

# map businessref -> businessid
rdf['business_id'] = rdf['business_ref'].str.replace('businessref_', 'businessid_', regex=False)

merged = rdf.merge(bdf[['business_id','categories_list']], on='business_id', how='left')

# explode categories
expl = merged.explode('categories_list').dropna(subset=['categories_list'])
expl = expl.rename(columns={'categories_list':'category'})

# aggregate
agg = expl.groupby('category', as_index=False)['review_cnt'].sum().sort_values(['review_cnt','category'], ascending=[False, True]).head(5)

out = agg.to_json(orient='records')
print('__RESULT__:')
print(out)"""

env_args = {'var_call_nUqi0mgV7W1SMZyGSmc6zggB': [{'business_ref': 'businessref_13', 'review_cnt': '1'}, {'business_ref': 'businessref_79', 'review_cnt': '1'}, {'business_ref': 'businessref_6', 'review_cnt': '1'}, {'business_ref': 'businessref_74', 'review_cnt': '2'}, {'business_ref': 'businessref_66', 'review_cnt': '2'}, {'business_ref': 'businessref_36', 'review_cnt': '2'}, {'business_ref': 'businessref_60', 'review_cnt': '2'}, {'business_ref': 'businessref_12', 'review_cnt': '1'}, {'business_ref': 'businessref_31', 'review_cnt': '1'}, {'business_ref': 'businessref_57', 'review_cnt': '2'}, {'business_ref': 'businessref_86', 'review_cnt': '1'}, {'business_ref': 'businessref_62', 'review_cnt': '1'}, {'business_ref': 'businessref_37', 'review_cnt': '1'}, {'business_ref': 'businessref_92', 'review_cnt': '2'}, {'business_ref': 'businessref_26', 'review_cnt': '1'}, {'business_ref': 'businessref_68', 'review_cnt': '1'}, {'business_ref': 'businessref_53', 'review_cnt': '1'}, {'business_ref': 'businessref_45', 'review_cnt': '3'}, {'business_ref': 'businessref_96', 'review_cnt': '2'}, {'business_ref': 'businessref_98', 'review_cnt': '1'}, {'business_ref': 'businessref_14', 'review_cnt': '1'}, {'business_ref': 'businessref_20', 'review_cnt': '1'}, {'business_ref': 'businessref_15', 'review_cnt': '1'}, {'business_ref': 'businessref_33', 'review_cnt': '2'}, {'business_ref': 'businessref_41', 'review_cnt': '1'}, {'business_ref': 'businessref_10', 'review_cnt': '1'}], 'var_call_j49UyM24eRN1cb3wKTwTcSnW': [{'business_id': 'businessid_49'}, {'business_id': 'businessid_47'}, {'business_id': 'businessid_88'}, {'business_id': 'businessid_41'}, {'business_id': 'businessid_33'}, {'business_id': 'businessid_74'}, {'business_id': 'businessid_92'}, {'business_id': 'businessid_64'}, {'business_id': 'businessid_52'}, {'business_id': 'businessid_29'}, {'business_id': 'businessid_10'}, {'business_id': 'businessid_61'}, {'business_id': 'businessid_54'}, {'business_id': 'businessid_8'}, {'business_id': 'businessid_59'}, {'business_id': 'businessid_91'}, {'business_id': 'businessid_83'}, {'business_id': 'businessid_93'}, {'business_id': 'businessid_1'}, {'business_id': 'businessid_24'}, {'business_id': 'businessid_95'}, {'business_id': 'businessid_50'}, {'business_id': 'businessid_26'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_89'}, {'business_id': 'businessid_32'}, {'business_id': 'businessid_70'}, {'business_id': 'businessid_42'}, {'business_id': 'businessid_71'}, {'business_id': 'businessid_97'}, {'business_id': 'businessid_14'}, {'business_id': 'businessid_3'}, {'business_id': 'businessid_35'}, {'business_id': 'businessid_28'}, {'business_id': 'businessid_57'}, {'business_id': 'businessid_27'}, {'business_id': 'businessid_75'}, {'business_id': 'businessid_34'}, {'business_id': 'businessid_2'}, {'business_id': 'businessid_19'}, {'business_id': 'businessid_48'}, {'business_id': 'businessid_67'}, {'business_id': 'businessid_7'}, {'business_id': 'businessid_51'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_100'}, {'business_id': 'businessid_5'}, {'business_id': 'businessid_63'}, {'business_id': 'businessid_45'}, {'business_id': 'businessid_68'}, {'business_id': 'businessid_6'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_78'}, {'business_id': 'businessid_79'}, {'business_id': 'businessid_66'}, {'business_id': 'businessid_55'}, {'business_id': 'businessid_30'}, {'business_id': 'businessid_80'}, {'business_id': 'businessid_15'}, {'business_id': 'businessid_96'}, {'business_id': 'businessid_11'}, {'business_id': 'businessid_73'}, {'business_id': 'businessid_4'}, {'business_id': 'businessid_77'}, {'business_id': 'businessid_18'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_86'}, {'business_id': 'businessid_53'}, {'business_id': 'businessid_40'}, {'business_id': 'businessid_44'}, {'business_id': 'businessid_43'}, {'business_id': 'businessid_72'}, {'business_id': 'businessid_9'}, {'business_id': 'businessid_20'}, {'business_id': 'businessid_37'}, {'business_id': 'businessid_56'}, {'business_id': 'businessid_62'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_39'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_31'}, {'business_id': 'businessid_85'}, {'business_id': 'businessid_25'}, {'business_id': 'businessid_82'}, {'business_id': 'businessid_58'}, {'business_id': 'businessid_12'}, {'business_id': 'businessid_99'}, {'business_id': 'businessid_60'}, {'business_id': 'businessid_21'}, {'business_id': 'businessid_98'}, {'business_id': 'businessid_16'}, {'business_id': 'businessid_46'}, {'business_id': 'businessid_22'}, {'business_id': 'businessid_36'}, {'business_id': 'businessid_69'}, {'business_id': 'businessid_23'}, {'business_id': 'businessid_38'}, {'business_id': 'businessid_81'}, {'business_id': 'businessid_13'}, {'business_id': 'businessid_17'}], 'var_call_vvWGBR2LEwErnhjwIf7W2dhg': 'file_storage/call_vvWGBR2LEwErnhjwIf7W2dhg.json'}

exec(code, env_args)
