code = """import json, re, pandas as pd

reviews = pd.DataFrame(var_call_vIcJ1OGF9f2ze48lAPw8T3lu)
reviews['review_cnt'] = reviews['review_cnt'].astype(int)

# load businesses from json file path
path = var_call_sZu4hRMNRDty0gP3jxzIGioT
with open(path, 'r') as f:
    biz = json.load(f)
biz_df = pd.DataFrame(biz)

# parse categories from description: take substring after 'including' or 'in the categories of'
pat = re.compile(r"(?:including|in the categories of)\s+(.*?)(?:\.|, making| to meet| offering| providing| specializing| perfect|$)", re.IGNORECASE)

def extract_cats(desc):
    if not isinstance(desc, str):
        return []
    m = pat.search(desc)
    s = m.group(1) if m else desc
    # split by comma and 'and'
    parts = re.split(r",|\band\b", s)
    cats = []
    for p in parts:
        p = p.strip().strip("\"").strip("'")
        if not p:
            continue
        # drop leading phrases
        p = re.sub(r"^(the categories of|categories of|category of)\s+", "", p, flags=re.I).strip()
        # remove trailing filler
        p = re.sub(r"\bfor all your.*$", "", p, flags=re.I).strip()
        if p:
            cats.append(p)
    return cats

biz_df['categories_list'] = biz_df['description'].apply(extract_cats)

# map businessid->businessref
biz_df['business_ref'] = biz_df['business_id'].str.replace('businessid_', 'businessref_', regex=False)

merged = reviews.merge(biz_df[['business_ref','categories_list']], on='business_ref', how='left')

rows = []
for _, r in merged.iterrows():
    cnt = int(r['review_cnt'])
    cats = r['categories_list'] if isinstance(r['categories_list'], list) else []
    for c in cats:
        rows.append((c, cnt))

cat_df = pd.DataFrame(rows, columns=['category','reviews'])
agg = cat_df.groupby('category', as_index=False)['reviews'].sum().sort_values(['reviews','category'], ascending=[False, True]).head(5)
result = agg.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_vIcJ1OGF9f2ze48lAPw8T3lu': [{'business_ref': 'businessref_13', 'review_cnt': '1'}, {'business_ref': 'businessref_79', 'review_cnt': '1'}, {'business_ref': 'businessref_74', 'review_cnt': '2'}, {'business_ref': 'businessref_66', 'review_cnt': '2'}, {'business_ref': 'businessref_15', 'review_cnt': '1'}, {'business_ref': 'businessref_33', 'review_cnt': '2'}, {'business_ref': 'businessref_6', 'review_cnt': '1'}, {'business_ref': 'businessref_31', 'review_cnt': '1'}, {'business_ref': 'businessref_36', 'review_cnt': '2'}, {'business_ref': 'businessref_60', 'review_cnt': '2'}, {'business_ref': 'businessref_12', 'review_cnt': '1'}, {'business_ref': 'businessref_53', 'review_cnt': '1'}, {'business_ref': 'businessref_57', 'review_cnt': '2'}, {'business_ref': 'businessref_86', 'review_cnt': '1'}, {'business_ref': 'businessref_62', 'review_cnt': '1'}, {'business_ref': 'businessref_37', 'review_cnt': '1'}, {'business_ref': 'businessref_92', 'review_cnt': '2'}, {'business_ref': 'businessref_26', 'review_cnt': '1'}, {'business_ref': 'businessref_68', 'review_cnt': '1'}, {'business_ref': 'businessref_45', 'review_cnt': '3'}, {'business_ref': 'businessref_96', 'review_cnt': '2'}, {'business_ref': 'businessref_98', 'review_cnt': '1'}, {'business_ref': 'businessref_14', 'review_cnt': '1'}, {'business_ref': 'businessref_20', 'review_cnt': '1'}, {'business_ref': 'businessref_41', 'review_cnt': '1'}, {'business_ref': 'businessref_10', 'review_cnt': '1'}], 'var_call_sZPcNlq02FqWOOxqSYbvfJl7': ['checkin', 'business'], 'var_call_U76Z79Unrw13mnq7D5ZIs4RM': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails'}], 'var_call_WaBumCD70TQTswzwgRx7U1xN': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_sZu4hRMNRDty0gP3jxzIGioT': 'file_storage/call_sZu4hRMNRDty0gP3jxzIGioT.json'}

exec(code, env_args)
