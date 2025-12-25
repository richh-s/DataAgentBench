code = """import json, pandas as pd

# load full results from files
with open(var_call_2oPlhtJ6vOKf9GFoBCGjfW9w, 'r') as f:
    review_data = json.load(f)
with open(var_call_3Yskp8Eeeyq9jlWDb6XITYHQ, 'r') as f:
    tip_data = json.load(f)
with open(var_call_ihPaLwXAXMBbngjVH4xTPVTn, 'r') as f:
    biz_attr_data = json.load(f)

review_df = pd.DataFrame(review_data)
tip_df = pd.DataFrame(tip_data)

# keep only rows where 'year' looks like a 4-digit year and equals '2018'
review_df['year_str'] = review_df['year'].astype(str)
review_2018 = review_df[review_df['year_str'].str.fullmatch(r'\d{4}') & (review_df['year_str'] == '2018')]

tip_df['year_str'] = tip_df['year'].astype(str)
tip_2018 = tip_df[tip_df['year_str'].str.fullmatch(r'\d{4}') & (tip_df['year_str'] == '2018')]

# businesses with any review or tip in 2018
biz_2018_refs = pd.Index(review_2018['business_ref']).union(tip_2018['business_ref'])

# map businessref_# to businessid_#
# prefix replacement
biz_2018_ids = biz_2018_refs.str.replace('businessref_', 'businessid_', regex=False)

biz_attr_df = pd.DataFrame(biz_attr_data)

# normalize attributes: check for BusinessParking or BikeParking keys and if they are not "False" or "None"

has_parking = []
for _, row in biz_attr_df.iterrows():
    attrs = row.get('attributes') or {}
    bp = attrs.get('BusinessParking')
    bk = attrs.get('BikeParking')
    offers = False
    if bp is not None and str(bp) not in ['False', 'None']:
        offers = True
    if bk is not None and str(bk) not in ['False', 'None']:
        offers = True
    has_parking.append(offers)

biz_attr_df['offers_parking_or_bike'] = has_parking

# filter businesses that offered parking or bike parking
biz_parking_ids = set(biz_attr_df[biz_attr_df['offers_parking_or_bike']]['business_id'])

# intersect with businesses that had reviews/tips in 2018
count = len(set(biz_2018_ids) & biz_parking_ids)

result = json.dumps(count)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_ihPaLwXAXMBbngjVH4xTPVTn': 'file_storage/call_ihPaLwXAXMBbngjVH4xTPVTn.json', 'var_call_2oPlhtJ6vOKf9GFoBCGjfW9w': 'file_storage/call_2oPlhtJ6vOKf9GFoBCGjfW9w.json', 'var_call_3Yskp8Eeeyq9jlWDb6XITYHQ': 'file_storage/call_3Yskp8Eeeyq9jlWDb6XITYHQ.json'}

exec(code, env_args)
