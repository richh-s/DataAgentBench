code = """import json, re, pandas as pd

reviews = pd.DataFrame(var_call_85wIkUNkaspkeR3pA6MHBjyn)
# map businessref_X -> businessid_X
reviews['business_id'] = reviews['business_ref'].str.replace('businessref_', 'businessid_', regex=False)

# load businesses descriptions
path = var_call_LxeiyvBxQSV2Wehw0E2lblLL
with open(path, 'r') as f:
    biz = json.load(f)

biz_df = pd.DataFrame(biz)
biz_df = biz_df[['business_id','description']]

# extract categories after 'providing' or 'including' or 'featuring' etc; take substring after 'categories of'
pat = re.compile(r"(?:services (?:in|include|including)|options ranging from|menu featuring|specializes in|offering(?:s)?(?: within)?|dishes in the category of|products in categories such as|providing a range of services in|providing expert care for all your residential maintenance needs\.|providing a range of services in)[: ]*(.*)", re.IGNORECASE)

def extract(desc):
    if not isinstance(desc,str):
        return []
    m = pat.search(desc)
    s = m.group(1) if m else desc
    # cut at last period
    s = s.split('.') [0]
    # remove quotes
    s = s.replace("'","")
    # split by commas and 'and'
    parts = re.split(r",| and | to | perfect for | making it | offering a ", s)
    cats=[]
    for p in parts:
        p=p.strip()
        if not p:
            continue
        # remove leading filler
        p=re.sub(r"^(the|a|an)\s+","",p,flags=re.I)
        # discard obvious non-category words
        if len(p)<=2:
            continue
        cats.append(p)
    return cats

biz_df['categories_extracted']=biz_df['description'].apply(extract)

# join and explode categories
merged = reviews.merge(biz_df, on='business_id', how='left')
expl = merged.explode('categories_extracted')
expl = expl.dropna(subset=['categories_extracted'])

# count reviews per category (total reviews)
counts = expl.groupby('categories_extracted').size().reset_index(name='total_reviews').sort_values('total_reviews', ascending=False)

top5 = counts.head(5)
result = top5.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_1CCZAQCwems5A21IgGCp7zgZ': [{'user_id': 'userid_746'}, {'user_id': 'userid_1109'}, {'user_id': 'userid_1950'}, {'user_id': 'userid_1316'}, {'user_id': 'userid_1182'}, {'user_id': 'userid_151'}, {'user_id': 'userid_1158'}, {'user_id': 'userid_508'}, {'user_id': 'userid_435'}, {'user_id': 'userid_958'}, {'user_id': 'userid_1879'}, {'user_id': 'userid_308'}, {'user_id': 'userid_1179'}, {'user_id': 'userid_324'}, {'user_id': 'userid_863'}, {'user_id': 'userid_100'}, {'user_id': 'userid_1333'}, {'user_id': 'userid_1636'}, {'user_id': 'userid_1850'}, {'user_id': 'userid_711'}, {'user_id': 'userid_729'}, {'user_id': 'userid_1505'}, {'user_id': 'userid_1315'}, {'user_id': 'userid_1708'}, {'user_id': 'userid_1661'}, {'user_id': 'userid_850'}, {'user_id': 'userid_1675'}, {'user_id': 'userid_227'}, {'user_id': 'userid_577'}, {'user_id': 'userid_257'}, {'user_id': 'userid_598'}, {'user_id': 'userid_847'}, {'user_id': 'userid_673'}, {'user_id': 'userid_1856'}, {'user_id': 'userid_384'}, {'user_id': 'userid_935'}, {'user_id': 'userid_210'}, {'user_id': 'userid_1101'}, {'user_id': 'userid_945'}, {'user_id': 'userid_842'}, {'user_id': 'userid_1351'}, {'user_id': 'userid_230'}, {'user_id': 'userid_593'}, {'user_id': 'userid_1431'}, {'user_id': 'userid_686'}, {'user_id': 'userid_527'}, {'user_id': 'userid_244'}, {'user_id': 'userid_393'}, {'user_id': 'userid_1178'}, {'user_id': 'userid_526'}, {'user_id': 'userid_90'}, {'user_id': 'userid_238'}, {'user_id': 'userid_1105'}], 'var_call_85wIkUNkaspkeR3pA6MHBjyn': [{'user_id': 'userid_1101', 'business_ref': 'businessref_74', 'review_id': 'reviewid_318'}, {'user_id': 'userid_1105', 'business_ref': 'businessref_57', 'review_id': 'reviewid_1049'}, {'user_id': 'userid_863', 'business_ref': 'businessref_96', 'review_id': 'reviewid_454'}, {'user_id': 'userid_308', 'business_ref': 'businessref_45', 'review_id': 'reviewid_1065'}, {'user_id': 'userid_729', 'business_ref': 'businessref_74', 'review_id': 'reviewid_704'}, {'user_id': 'userid_935', 'business_ref': 'businessref_53', 'review_id': 'reviewid_84'}, {'user_id': 'userid_1856', 'business_ref': 'businessref_41', 'review_id': 'reviewid_1110'}, {'user_id': 'userid_435', 'business_ref': 'businessref_96', 'review_id': 'reviewid_655'}, {'user_id': 'userid_1178', 'business_ref': 'businessref_10', 'review_id': 'reviewid_1239'}, {'user_id': 'userid_1109', 'business_ref': 'businessref_66', 'review_id': 'reviewid_515'}, {'user_id': 'userid_593', 'business_ref': 'businessref_31', 'review_id': 'reviewid_44'}, {'user_id': 'userid_1182', 'business_ref': 'businessref_92', 'review_id': 'reviewid_65'}, {'user_id': 'userid_230', 'business_ref': 'businessref_26', 'review_id': 'reviewid_1216'}, {'user_id': 'userid_244', 'business_ref': 'businessref_98', 'review_id': 'reviewid_781'}, {'user_id': 'userid_1316', 'business_ref': 'businessref_45', 'review_id': 'reviewid_334'}, {'user_id': 'userid_324', 'business_ref': 'businessref_45', 'review_id': 'reviewid_124'}, {'user_id': 'userid_1850', 'business_ref': 'businessref_36', 'review_id': 'reviewid_957'}, {'user_id': 'userid_686', 'business_ref': 'businessref_14', 'review_id': 'reviewid_1174'}, {'user_id': 'userid_1950', 'business_ref': 'businessref_86', 'review_id': 'reviewid_1502'}, {'user_id': 'userid_945', 'business_ref': 'businessref_57', 'review_id': 'reviewid_919'}, {'user_id': 'userid_1179', 'business_ref': 'businessref_13', 'review_id': 'reviewid_926'}, {'user_id': 'userid_1879', 'business_ref': 'businessref_68', 'review_id': 'reviewid_1457'}, {'user_id': 'userid_850', 'business_ref': 'businessref_36', 'review_id': 'reviewid_1576'}, {'user_id': 'userid_958', 'business_ref': 'businessref_60', 'review_id': 'reviewid_1677'}, {'user_id': 'userid_1661', 'business_ref': 'businessref_20', 'review_id': 'reviewid_160'}, {'user_id': 'userid_210', 'business_ref': 'businessref_15', 'review_id': 'reviewid_1207'}, {'user_id': 'userid_151', 'business_ref': 'businessref_62', 'review_id': 'reviewid_1635'}, {'user_id': 'userid_100', 'business_ref': 'businessref_33', 'review_id': 'reviewid_1966'}, {'user_id': 'userid_598', 'business_ref': 'businessref_37', 'review_id': 'reviewid_1791'}, {'user_id': 'userid_746', 'business_ref': 'businessref_92', 'review_id': 'reviewid_1986'}, {'user_id': 'userid_1675', 'business_ref': 'businessref_66', 'review_id': 'reviewid_1137'}, {'user_id': 'userid_1505', 'business_ref': 'businessref_33', 'review_id': 'reviewid_1555'}, {'user_id': 'userid_842', 'business_ref': 'businessref_6', 'review_id': 'reviewid_1408'}, {'user_id': 'userid_257', 'business_ref': 'businessref_12', 'review_id': 'reviewid_1388'}, {'user_id': 'userid_1333', 'business_ref': 'businessref_79', 'review_id': 'reviewid_62'}, {'user_id': 'userid_711', 'business_ref': 'businessref_60', 'review_id': 'reviewid_280'}], 'var_call_91HniXgWkAAYUlX2Uymp9EuO': ['checkin', 'business'], 'var_call_dUYQmTmwp63K9OzowKnxpcDo': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails'}], 'var_call_dqyXoyUf23UADAh02lR0BZqn': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_call_LxeiyvBxQSV2Wehw0E2lblLL': 'file_storage/call_LxeiyvBxQSV2Wehw0E2lblLL.json'}

exec(code, env_args)
