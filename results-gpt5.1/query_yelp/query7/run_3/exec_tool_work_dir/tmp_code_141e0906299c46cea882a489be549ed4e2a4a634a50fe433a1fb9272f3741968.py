code = """import json, re, pandas as pd
from datetime import datetime

# Load full user and review data
with open(var_call_H5oAfc6fgumo1D74oBhkVxge, 'r') as f:
    users = json.load(f)
with open(var_call_SVKpH2LrQLyLXUK8g1QS9khS, 'r') as f:
    reviews = json.load(f)

# Helper to parse heterogeneous date formats and return year
FORMATS = [
    '%Y-%m-%d %H:%M:%S',
    '%Y-%m-%d %H:%M',
    '%Y-%m-%d',
    '%d %b %Y, %H:%M',
    '%d %b %Y, %H:%M:%S',
    '%b %d, %Y at %I:%M %p',
    '%B %d, %Y at %I:%M %p',
    '%d %b %Y, %H:%M',
    '%d %b %Y, %H:%M',
]

MONTHS = {m: i for i, m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}
SHORT_MONTHS = {m: i for i, m in enumerate(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], start=1)}

def parse_year(s):
    if not s:
        return None
    s = s.strip()
    # Try direct integer year at start or end
    m = re.search(r'(20\d{2}|19\d{2})', s)
    if m:
        return int(m.group(1))
    return None

# Determine users who registered in 2016
user_years = []
for u in users:
    y = parse_year(u.get('yelping_since'))
    if y is not None:
        user_years.append({'user_id': u['user_id'], 'year': y})

user_df = pd.DataFrame(user_years)
users_2016 = set(user_df[user_df['year'] == 2016]['user_id'])

# Filter reviews from those users, and from 2016 onward
review_rows = []
for r in reviews:
    uid = r.get('user_id')
    if uid is None or uid not in users_2016:
        continue
    year = parse_year(r.get('date'))
    if year is None or year < 2016:
        continue
    review_rows.append({'user_id': uid, 'business_ref': r['business_ref'], 'year': year})

rev_df = pd.DataFrame(review_rows)

# Map business_id to categories
biz_df = pd.DataFrame(var_call_VwligYNNqq4bOoECdHebqSi6)

# business data currently only has business_id, no categories in projection; mock categories if missing
if 'categories' not in biz_df.columns:
    categories_map = {}
else:
    categories_map = dict(zip(biz_df['business_id'], biz_df['categories']))

# Build mapping from business_ref to categories via prefix change
cat_counts = {}
for _, row in rev_df.iterrows():
    bref = row['business_ref']
    bid = 'businessid_' + bref.split('_',1)[1]
    cats = categories_map.get(bid)
    if not cats:
        continue
    # categories might be a list or comma-separated string
    if isinstance(cats, str):
        parts = [c.strip() for c in cats.split(',') if c.strip()]
    else:
        parts = list(cats)
    for c in parts:
        cat_counts[c] = cat_counts.get(c, 0) + 1

# Get top 5
top5 = sorted(cat_counts.items(), key=lambda x: x[1], reverse=True)[:5]

result = [{'category': c, 'total_reviews_from_2016_users_since_2016': n} for c, n in top5]

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_HbBhOOgRluRPawcYPjv2O0YN': [{'business_id': 'businessid_49'}, {'business_id': 'businessid_47'}, {'business_id': 'businessid_88'}, {'business_id': 'businessid_41'}, {'business_id': 'businessid_33'}, {'business_id': 'businessid_74'}, {'business_id': 'businessid_92'}, {'business_id': 'businessid_64'}, {'business_id': 'businessid_52'}, {'business_id': 'businessid_29'}, {'business_id': 'businessid_10'}, {'business_id': 'businessid_61'}, {'business_id': 'businessid_54'}, {'business_id': 'businessid_8'}, {'business_id': 'businessid_59'}, {'business_id': 'businessid_91'}, {'business_id': 'businessid_83'}, {'business_id': 'businessid_93'}, {'business_id': 'businessid_1'}, {'business_id': 'businessid_24'}, {'business_id': 'businessid_95'}, {'business_id': 'businessid_50'}, {'business_id': 'businessid_26'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_89'}, {'business_id': 'businessid_32'}, {'business_id': 'businessid_70'}, {'business_id': 'businessid_42'}, {'business_id': 'businessid_71'}, {'business_id': 'businessid_97'}, {'business_id': 'businessid_14'}, {'business_id': 'businessid_3'}, {'business_id': 'businessid_35'}, {'business_id': 'businessid_28'}, {'business_id': 'businessid_57'}, {'business_id': 'businessid_27'}, {'business_id': 'businessid_75'}, {'business_id': 'businessid_34'}, {'business_id': 'businessid_2'}, {'business_id': 'businessid_19'}, {'business_id': 'businessid_48'}, {'business_id': 'businessid_67'}, {'business_id': 'businessid_7'}, {'business_id': 'businessid_51'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_100'}, {'business_id': 'businessid_5'}, {'business_id': 'businessid_63'}, {'business_id': 'businessid_45'}, {'business_id': 'businessid_68'}, {'business_id': 'businessid_6'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_78'}, {'business_id': 'businessid_79'}, {'business_id': 'businessid_66'}, {'business_id': 'businessid_55'}, {'business_id': 'businessid_30'}, {'business_id': 'businessid_80'}, {'business_id': 'businessid_15'}, {'business_id': 'businessid_96'}, {'business_id': 'businessid_11'}, {'business_id': 'businessid_73'}, {'business_id': 'businessid_4'}, {'business_id': 'businessid_77'}, {'business_id': 'businessid_18'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_86'}, {'business_id': 'businessid_53'}, {'business_id': 'businessid_40'}, {'business_id': 'businessid_44'}, {'business_id': 'businessid_43'}, {'business_id': 'businessid_72'}, {'business_id': 'businessid_9'}, {'business_id': 'businessid_20'}, {'business_id': 'businessid_37'}, {'business_id': 'businessid_56'}, {'business_id': 'businessid_62'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_39'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_31'}, {'business_id': 'businessid_85'}, {'business_id': 'businessid_25'}, {'business_id': 'businessid_82'}, {'business_id': 'businessid_58'}, {'business_id': 'businessid_12'}, {'business_id': 'businessid_99'}, {'business_id': 'businessid_60'}, {'business_id': 'businessid_21'}, {'business_id': 'businessid_98'}, {'business_id': 'businessid_16'}, {'business_id': 'businessid_46'}, {'business_id': 'businessid_22'}, {'business_id': 'businessid_36'}, {'business_id': 'businessid_69'}, {'business_id': 'businessid_23'}, {'business_id': 'businessid_38'}, {'business_id': 'businessid_81'}, {'business_id': 'businessid_13'}, {'business_id': 'businessid_17'}], 'var_call_H5oAfc6fgumo1D74oBhkVxge': 'file_storage/call_H5oAfc6fgumo1D74oBhkVxge.json', 'var_call_SVKpH2LrQLyLXUK8g1QS9khS': 'file_storage/call_SVKpH2LrQLyLXUK8g1QS9khS.json', 'var_call_VwligYNNqq4bOoECdHebqSi6': [{'business_id': 'businessid_49'}, {'business_id': 'businessid_47'}, {'business_id': 'businessid_88'}, {'business_id': 'businessid_41'}, {'business_id': 'businessid_33'}, {'business_id': 'businessid_74'}, {'business_id': 'businessid_92'}, {'business_id': 'businessid_64'}, {'business_id': 'businessid_52'}, {'business_id': 'businessid_29'}, {'business_id': 'businessid_10'}, {'business_id': 'businessid_61'}, {'business_id': 'businessid_54'}, {'business_id': 'businessid_8'}, {'business_id': 'businessid_59'}, {'business_id': 'businessid_91'}, {'business_id': 'businessid_83'}, {'business_id': 'businessid_93'}, {'business_id': 'businessid_1'}, {'business_id': 'businessid_24'}, {'business_id': 'businessid_95'}, {'business_id': 'businessid_50'}, {'business_id': 'businessid_26'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_89'}, {'business_id': 'businessid_32'}, {'business_id': 'businessid_70'}, {'business_id': 'businessid_42'}, {'business_id': 'businessid_71'}, {'business_id': 'businessid_97'}, {'business_id': 'businessid_14'}, {'business_id': 'businessid_3'}, {'business_id': 'businessid_35'}, {'business_id': 'businessid_28'}, {'business_id': 'businessid_57'}, {'business_id': 'businessid_27'}, {'business_id': 'businessid_75'}, {'business_id': 'businessid_34'}, {'business_id': 'businessid_2'}, {'business_id': 'businessid_19'}, {'business_id': 'businessid_48'}, {'business_id': 'businessid_67'}, {'business_id': 'businessid_7'}, {'business_id': 'businessid_51'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_100'}, {'business_id': 'businessid_5'}, {'business_id': 'businessid_63'}, {'business_id': 'businessid_45'}, {'business_id': 'businessid_68'}, {'business_id': 'businessid_6'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_78'}, {'business_id': 'businessid_79'}, {'business_id': 'businessid_66'}, {'business_id': 'businessid_55'}, {'business_id': 'businessid_30'}, {'business_id': 'businessid_80'}, {'business_id': 'businessid_15'}, {'business_id': 'businessid_96'}, {'business_id': 'businessid_11'}, {'business_id': 'businessid_73'}, {'business_id': 'businessid_4'}, {'business_id': 'businessid_77'}, {'business_id': 'businessid_18'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_86'}, {'business_id': 'businessid_53'}, {'business_id': 'businessid_40'}, {'business_id': 'businessid_44'}, {'business_id': 'businessid_43'}, {'business_id': 'businessid_72'}, {'business_id': 'businessid_9'}, {'business_id': 'businessid_20'}, {'business_id': 'businessid_37'}, {'business_id': 'businessid_56'}, {'business_id': 'businessid_62'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_39'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_31'}, {'business_id': 'businessid_85'}, {'business_id': 'businessid_25'}, {'business_id': 'businessid_82'}, {'business_id': 'businessid_58'}, {'business_id': 'businessid_12'}, {'business_id': 'businessid_99'}, {'business_id': 'businessid_60'}, {'business_id': 'businessid_21'}, {'business_id': 'businessid_98'}, {'business_id': 'businessid_16'}, {'business_id': 'businessid_46'}, {'business_id': 'businessid_22'}, {'business_id': 'businessid_36'}, {'business_id': 'businessid_69'}, {'business_id': 'businessid_23'}, {'business_id': 'businessid_38'}, {'business_id': 'businessid_81'}, {'business_id': 'businessid_13'}, {'business_id': 'businessid_17'}]}

exec(code, env_args)
