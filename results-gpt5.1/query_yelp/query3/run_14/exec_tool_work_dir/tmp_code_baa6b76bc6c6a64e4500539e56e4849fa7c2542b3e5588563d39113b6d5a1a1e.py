code = """import json, pandas as pd

reviews = var_call_rvAQ1G5MnOrBozjE3H0hxKCg

# normalize business_ref to business_id by replacing prefix
review_biz_ids = set()
for r in reviews:
    br = r['business_ref']
    if br.startswith('businessref_'):
        bid = 'businessid_' + br.split('businessref_')[1]
        review_biz_ids.add(bid)

# load full business attributes file
path = var_call_E091RA4vcp0Lc5PhxWwYqeet
with open(path, 'r') as f:
    business_records = json.load(f)

count = 0
for b in business_records:
    bid = b.get('business_id')
    if bid not in review_biz_ids:
        continue
    attrs = b.get('attributes')
    if not attrs or attrs == 'None':
        continue
    has_bike = False
    has_parking = False
    if isinstance(attrs, dict):
        bike = attrs.get('BikeParking')
        park = attrs.get('BusinessParking')
        # treat any non-None value as offering the feature
        if bike and bike != 'None' and bike != 'False':
            has_bike = True
        if park and park != 'None' and park != 'False':
            has_parking = True
    if has_bike or has_parking:
        count += 1

result = json.dumps(count)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_jk6oGdchPK1uyUY9DLrtw7mD': ['business', 'checkin'], 'var_call_rvAQ1G5MnOrBozjE3H0hxKCg': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}], 'var_call_E091RA4vcp0Lc5PhxWwYqeet': 'file_storage/call_E091RA4vcp0Lc5PhxWwYqeet.json'}

exec(code, env_args)
