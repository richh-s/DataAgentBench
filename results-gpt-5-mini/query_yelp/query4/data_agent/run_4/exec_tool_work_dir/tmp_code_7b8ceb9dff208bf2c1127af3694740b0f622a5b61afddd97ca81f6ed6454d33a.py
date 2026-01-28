code = """import json
from collections import defaultdict

# Load the large business collection result from file
with open(var_call_uTF1KdpbcWSo56QLKVyoIoEB, 'r') as f:
    businesses = json.load(f)

# Load reviews
with open(var_call_NY7FGyJVQeNLQWO6v3kUr6kw, 'r') as f:
    reviews = json.load(f)

# List of businesses that accept credit cards (from earlier query)
accept_list = var_call_zIinwH1z4Us9gBmDryUNZqzV
accept_ids = set(d['business_id'] for d in accept_list)

# Map business_id -> primary category
biz_category = {}
for b in businesses:
    bid = b.get('business_id')
    if bid in accept_ids:
        cat = b.get('categories')
        if cat is None:
            primary = None
        elif isinstance(cat, list):
            primary = cat[0] if len(cat)>0 else None
        else:
            # assume string of categories separated by comma
            try:
                primary = cat.split(',')[0].strip()
            except Exception:
                primary = str(cat)
        biz_category[bid] = primary

# Count businesses per category (unique business count)
category_to_bizids = defaultdict(set)
for bid, cat in biz_category.items():
    category_to_bizids[cat].add(bid)

# Map business_ref -> list of ratings
rev_map = defaultdict(list)
for r in reviews:
    bref = r.get('business_ref')
    rating = r.get('rating')
    try:
        rating = int(rating)
    except:
        try:
            rating = float(rating)
        except:
            continue
    rev_map[bref].append(rating)

# Aggregate ratings per category across all reviews of businesses in that category
category_ratings = defaultdict(list)
for cat, bids in category_to_bizids.items():
    for bid in bids:
        # convert businessid_X to businessref_X
        bref = bid.replace('businessid_', 'businessref_')
        ratings = rev_map.get(bref, [])
        category_ratings[cat].extend(ratings)

# Compute counts and average ratings
results = []
for cat, bids in category_to_bizids.items():
    count = len(bids)
    ratings = category_ratings.get(cat, [])
    if ratings:
        avg = sum(ratings)/len(ratings)
        avg = round(avg, 2)
    else:
        avg = None
    results.append({'category': cat, 'business_count': count, 'average_rating': avg})

# Find category with largest number of businesses
if not results:
    final = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    # sort by business_count desc, then category name asc (None last)
    def sort_key(x):
        return (-x['business_count'], (x['category'] is None, x['category']))
    results_sorted = sorted(results, key=sort_key)
    final = results_sorted[0]

import json as _json
print("__RESULT__:")
print(_json.dumps(final))"""

env_args = {'var_call_xBdMThlqxRYUalUplSeHG6Cl': ['business', 'checkin'], 'var_call_ueymrqyIPaJ3LmTPMWcfdIMq': ['review', 'tip', 'user'], 'var_call_uTF1KdpbcWSo56QLKVyoIoEB': 'file_storage/call_uTF1KdpbcWSo56QLKVyoIoEB.json', 'var_call_NY7FGyJVQeNLQWO6v3kUr6kw': 'file_storage/call_NY7FGyJVQeNLQWO6v3kUr6kw.json', 'var_call_zIinwH1z4Us9gBmDryUNZqzV': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92'}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64'}, {'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52'}, {'_id': '6859a000fe8b31cd7362e2b4', 'business_id': 'businessid_29'}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10'}, {'_id': '6859a000fe8b31cd7362e2b6', 'business_id': 'businessid_61'}, {'_id': '6859a000fe8b31cd7362e2b7', 'business_id': 'businessid_54'}, {'_id': '6859a000fe8b31cd7362e2b8', 'business_id': 'businessid_8'}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91'}, {'_id': '6859a000fe8b31cd7362e2bb', 'business_id': 'businessid_83'}, {'_id': '6859a000fe8b31cd7362e2bc', 'business_id': 'businessid_93'}, {'_id': '6859a000fe8b31cd7362e2be', 'business_id': 'businessid_24'}, {'_id': '6859a000fe8b31cd7362e2bf', 'business_id': 'businessid_95'}, {'_id': '6859a000fe8b31cd7362e2c1', 'business_id': 'businessid_26'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84'}, {'_id': '6859a000fe8b31cd7362e2c3', 'business_id': 'businessid_89'}, {'_id': '6859a000fe8b31cd7362e2c4', 'business_id': 'businessid_32'}, {'_id': '6859a000fe8b31cd7362e2c7', 'business_id': 'businessid_71'}, {'_id': '6859a000fe8b31cd7362e2c8', 'business_id': 'businessid_97'}, {'_id': '6859a000fe8b31cd7362e2c9', 'business_id': 'businessid_14'}, {'_id': '6859a000fe8b31cd7362e2ca', 'business_id': 'businessid_3'}, {'_id': '6859a000fe8b31cd7362e2ce', 'business_id': 'businessid_27'}, {'_id': '6859a000fe8b31cd7362e2cf', 'business_id': 'businessid_75'}, {'_id': '6859a000fe8b31cd7362e2d1', 'business_id': 'businessid_2'}, {'_id': '6859a000fe8b31cd7362e2d3', 'business_id': 'businessid_48'}, {'_id': '6859a000fe8b31cd7362e2d4', 'business_id': 'businessid_67'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76'}, {'_id': '6859a000fe8b31cd7362e2d8', 'business_id': 'businessid_100'}, {'_id': '6859a000fe8b31cd7362e2da', 'business_id': 'businessid_63'}, {'_id': '6859a000fe8b31cd7362e2db', 'business_id': 'businessid_45'}, {'_id': '6859a000fe8b31cd7362e2dc', 'business_id': 'businessid_68'}, {'_id': '6859a000fe8b31cd7362e2dd', 'business_id': 'businessid_6'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87'}, {'_id': '6859a000fe8b31cd7362e2e1', 'business_id': 'businessid_66'}, {'_id': '6859a000fe8b31cd7362e2e2', 'business_id': 'businessid_55'}, {'_id': '6859a000fe8b31cd7362e2e3', 'business_id': 'businessid_30'}, {'_id': '6859a000fe8b31cd7362e2e5', 'business_id': 'businessid_15'}, {'_id': '6859a000fe8b31cd7362e2e6', 'business_id': 'businessid_96'}, {'_id': '6859a000fe8b31cd7362e2e7', 'business_id': 'businessid_11'}, {'_id': '6859a000fe8b31cd7362e2e8', 'business_id': 'businessid_73'}, {'_id': '6859a000fe8b31cd7362e2e9', 'business_id': 'businessid_4'}, {'_id': '6859a000fe8b31cd7362e2ea', 'business_id': 'businessid_77'}, {'_id': '6859a000fe8b31cd7362e2eb', 'business_id': 'businessid_18'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65'}, {'_id': '6859a000fe8b31cd7362e2ed', 'business_id': 'businessid_86'}, {'_id': '6859a000fe8b31cd7362e2ee', 'business_id': 'businessid_53'}, {'_id': '6859a000fe8b31cd7362e2ef', 'business_id': 'businessid_40'}, {'_id': '6859a000fe8b31cd7362e2f0', 'business_id': 'businessid_44'}, {'_id': '6859a000fe8b31cd7362e2f1', 'business_id': 'businessid_43'}, {'_id': '6859a000fe8b31cd7362e2f3', 'business_id': 'businessid_9'}, {'_id': '6859a000fe8b31cd7362e2f4', 'business_id': 'businessid_20'}, {'_id': '6859a000fe8b31cd7362e2f5', 'business_id': 'businessid_37'}, {'_id': '6859a000fe8b31cd7362e2f7', 'business_id': 'businessid_62'}, {'_id': '6859a000fe8b31cd7362e2f8', 'business_id': 'businessid_94'}, {'_id': '6859a000fe8b31cd7362e2fa', 'business_id': 'businessid_90'}, {'_id': '6859a000fe8b31cd7362e2fb', 'business_id': 'businessid_31'}, {'_id': '6859a000fe8b31cd7362e2fc', 'business_id': 'businessid_85'}, {'_id': '6859a000fe8b31cd7362e2fd', 'business_id': 'businessid_25'}, {'_id': '6859a000fe8b31cd7362e2fe', 'business_id': 'businessid_82'}, {'_id': '6859a000fe8b31cd7362e2ff', 'business_id': 'businessid_58'}, {'_id': '6859a000fe8b31cd7362e302', 'business_id': 'businessid_60'}, {'_id': '6859a000fe8b31cd7362e303', 'business_id': 'businessid_21'}, {'_id': '6859a000fe8b31cd7362e304', 'business_id': 'businessid_98'}, {'_id': '6859a000fe8b31cd7362e305', 'business_id': 'businessid_16'}, {'_id': '6859a000fe8b31cd7362e306', 'business_id': 'businessid_46'}, {'_id': '6859a000fe8b31cd7362e307', 'business_id': 'businessid_22'}, {'_id': '6859a000fe8b31cd7362e308', 'business_id': 'businessid_36'}, {'_id': '6859a000fe8b31cd7362e30b', 'business_id': 'businessid_38'}, {'_id': '6859a000fe8b31cd7362e30c', 'business_id': 'businessid_81'}, {'_id': '6859a000fe8b31cd7362e30d', 'business_id': 'businessid_13'}, {'_id': '6859a000fe8b31cd7362e30e', 'business_id': 'businessid_17'}]}

exec(code, env_args)
