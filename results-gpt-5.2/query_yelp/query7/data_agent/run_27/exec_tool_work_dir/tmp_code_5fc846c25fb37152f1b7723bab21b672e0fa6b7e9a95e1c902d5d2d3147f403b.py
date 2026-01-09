code = """import json, pandas as pd
from datetime import datetime

users_2016 = set(r['user_id'] for r in var_call_Kpmz3oJeQYH20gA9RSpMHuji)

# load reviews (may be file path)
rev_data = var_call_Ba2LxGjHppXyhBPAGNMiNEmz
if isinstance(rev_data, str):
    with open(rev_data, 'r') as f:
        reviews = json.load(f)
else:
    reviews = rev_data

# parse date robustly to year
fmts = [
    '%Y-%m-%d %H:%M:%S',
    '%Y-%m-%d %H:%M:%S.%f',
    '%d %b %Y, %H:%M',
    '%d %b %Y, %H:%M:%S',
    '%B %d, %Y at %I:%M %p',
    '%b %d, %Y at %I:%M %p',
]

def year_from(s):
    if s is None:
        return None
    s = str(s)
    # fast path
    if len(s)>=4 and s[:4].isdigit():
        try:
            return int(s[:4])
        except:
            pass
    for fmt in fmts:
        try:
            return datetime.strptime(s, fmt).year
        except:
            continue
    # last resort: find 4-digit year
    import re
    m = re.search(r'(19|20)\\d{2}', s)
    return int(m.group(0)) if m else None

# filter reviews by users and year>=2016
filtered = []
for r in reviews:
    uid = r.get('user_id')
    if uid in users_2016:
        y = year_from(r.get('date'))
        if y is not None and y >= 2016:
            filtered.append({'business_ref': r.get('business_ref')})

rev_df = pd.DataFrame(filtered)
if rev_df.empty:
    out = json.dumps([])
    print('__RESULT__:')
    print(out)
    raise SystemExit

# count reviews per business_ref
biz_counts = rev_df.value_counts('business_ref').reset_index()
biz_counts.columns = ['business_ref','review_count_from_2016_users']

# business categories mapping
biz_meta = var_call_aenOMx1GPmhjoagPLgtnG3d3
meta_rows = []
for b in biz_meta:
    bid = b.get('business_id')
    if not bid:
        continue
    bref = 'businessref_' + bid.split('businessid_')[-1]
    cats = b.get('categories')
    if cats is None:
        # try infer from name/description? skip
        cat_list = []
    elif isinstance(cats, list):
        cat_list = cats
    else:
        # assume comma-separated string
        cat_list = [c.strip() for c in str(cats).split(',') if c.strip()]
    for c in cat_list:
        meta_rows.append({'business_ref': bref, 'category': c})

meta_df = pd.DataFrame(meta_rows)
# join counts to categories
merged = biz_counts.merge(meta_df, on='business_ref', how='inner')
cat_totals = merged.groupby('category', as_index=False)['review_count_from_2016_users'].sum()
cat_totals = cat_totals.sort_values('review_count_from_2016_users', ascending=False).head(5)

out = cat_totals.to_json(orient='records')
print('__RESULT__:')
print(out)"""

env_args = {'var_call_Kpmz3oJeQYH20gA9RSpMHuji': [{'user_id': 'userid_746'}, {'user_id': 'userid_1109'}, {'user_id': 'userid_1950'}, {'user_id': 'userid_1316'}, {'user_id': 'userid_1182'}, {'user_id': 'userid_151'}, {'user_id': 'userid_1158'}, {'user_id': 'userid_508'}, {'user_id': 'userid_435'}, {'user_id': 'userid_958'}, {'user_id': 'userid_1879'}, {'user_id': 'userid_308'}, {'user_id': 'userid_1179'}, {'user_id': 'userid_324'}, {'user_id': 'userid_863'}, {'user_id': 'userid_100'}, {'user_id': 'userid_1333'}, {'user_id': 'userid_1636'}, {'user_id': 'userid_1850'}, {'user_id': 'userid_711'}, {'user_id': 'userid_729'}, {'user_id': 'userid_1505'}, {'user_id': 'userid_1315'}, {'user_id': 'userid_1708'}, {'user_id': 'userid_1661'}, {'user_id': 'userid_850'}, {'user_id': 'userid_1675'}, {'user_id': 'userid_227'}, {'user_id': 'userid_577'}, {'user_id': 'userid_257'}, {'user_id': 'userid_598'}, {'user_id': 'userid_847'}, {'user_id': 'userid_673'}, {'user_id': 'userid_1856'}, {'user_id': 'userid_384'}, {'user_id': 'userid_935'}, {'user_id': 'userid_210'}, {'user_id': 'userid_1101'}, {'user_id': 'userid_945'}, {'user_id': 'userid_842'}, {'user_id': 'userid_1351'}, {'user_id': 'userid_230'}, {'user_id': 'userid_593'}, {'user_id': 'userid_1431'}, {'user_id': 'userid_686'}, {'user_id': 'userid_527'}, {'user_id': 'userid_244'}, {'user_id': 'userid_393'}, {'user_id': 'userid_1178'}, {'user_id': 'userid_526'}, {'user_id': 'userid_90'}, {'user_id': 'userid_238'}, {'user_id': 'userid_1105'}], 'var_call_Ba2LxGjHppXyhBPAGNMiNEmz': 'file_storage/call_Ba2LxGjHppXyhBPAGNMiNEmz.json', 'var_call_aenOMx1GPmhjoagPLgtnG3d3': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'name': 'Candy Barrel'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'name': 'Luminosity'}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64', 'name': 'Nail Care Salon'}, {'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52', 'name': 'Architectural Antiques of Indianapolis'}, {'_id': '6859a000fe8b31cd7362e2b4', 'business_id': 'businessid_29', 'name': "Aster's Floral Shop"}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10', 'name': 'China Wok'}, {'_id': '6859a000fe8b31cd7362e2b6', 'business_id': 'businessid_61', 'name': 'Brandon Family Medical Care'}, {'_id': '6859a000fe8b31cd7362e2b7', 'business_id': 'businessid_54', 'name': '7-Eleven'}, {'_id': '6859a000fe8b31cd7362e2b8', 'business_id': 'businessid_8', 'name': 'Uber'}, {'_id': '6859a000fe8b31cd7362e2b9', 'business_id': 'businessid_59', 'name': 'Chestnut St. Cafe'}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91', 'name': 'Cafe Porche and snowbar'}, {'_id': '6859a000fe8b31cd7362e2bb', 'business_id': 'businessid_83', 'name': 'Eyeglass World'}, {'_id': '6859a000fe8b31cd7362e2bc', 'business_id': 'businessid_93', 'name': "Callahan's Corner"}, {'_id': '6859a000fe8b31cd7362e2bd', 'business_id': 'businessid_1', 'name': 'Spa Guy Dave'}, {'_id': '6859a000fe8b31cd7362e2be', 'business_id': 'businessid_24', 'name': 'FroYo Frozen Yogurt'}, {'_id': '6859a000fe8b31cd7362e2bf', 'business_id': 'businessid_95', 'name': 'Subway'}, {'_id': '6859a000fe8b31cd7362e2c0', 'business_id': 'businessid_50', 'name': "Arby's"}, {'_id': '6859a000fe8b31cd7362e2c1', 'business_id': 'businessid_26', 'name': "McDonald's"}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84', 'name': 'Gamestop'}, {'_id': '6859a000fe8b31cd7362e2c3', 'business_id': 'businessid_89', 'name': 'King of Prussia Laundromat'}, {'_id': '6859a000fe8b31cd7362e2c4', 'business_id': 'businessid_32', 'name': 'The Recovery Room Bar & Grill'}, {'_id': '6859a000fe8b31cd7362e2c5', 'business_id': 'businessid_70', 'name': "Lenny's Plumbing"}, {'_id': '6859a000fe8b31cd7362e2c6', 'business_id': 'businessid_42', 'name': 'Dobbs Tire & Auto Centers'}, {'_id': '6859a000fe8b31cd7362e2c7', 'business_id': 'businessid_71', 'name': 'Lithia Ford Lincoln of Boise'}, {'_id': '6859a000fe8b31cd7362e2c8', 'business_id': 'businessid_97', 'name': 'Executive Auto Body'}, {'_id': '6859a000fe8b31cd7362e2c9', 'business_id': 'businessid_14', 'name': 'Ross Dress for Less'}, {'_id': '6859a000fe8b31cd7362e2ca', 'business_id': 'businessid_3', 'name': 'Mr. Dry Out'}, {'_id': '6859a000fe8b31cd7362e2cb', 'business_id': 'businessid_35', 'name': 'Bywood Seafood Market'}, {'_id': '6859a000fe8b31cd7362e2cc', 'business_id': 'businessid_28', 'name': 'Battleground Hospital For Animals'}, {'_id': '6859a000fe8b31cd7362e2cd', 'business_id': 'businessid_57', 'name': 'Big Boys Moving And Storage'}, {'_id': '6859a000fe8b31cd7362e2ce', 'business_id': 'businessid_27', 'name': 'Egg Roll King Two'}, {'_id': '6859a000fe8b31cd7362e2cf', 'business_id': 'businessid_75', 'name': 'Light World'}, {'_id': '6859a000fe8b31cd7362e2d0', 'business_id': 'businessid_34', 'name': 'Lewis and Clark Confluence Tower'}, {'_id': '6859a000fe8b31cd7362e2d1', 'business_id': 'businessid_2', 'name': 'Bloom'}, {'_id': '6859a000fe8b31cd7362e2d2', 'business_id': 'businessid_19', 'name': 'Kallejon 813'}, {'_id': '6859a000fe8b31cd7362e2d3', 'business_id': 'businessid_48', 'name': 'The Loop Taste of Chicago'}, {'_id': '6859a000fe8b31cd7362e2d4', 'business_id': 'businessid_67', 'name': "Hanoi's Pho"}, {'_id': '6859a000fe8b31cd7362e2d5', 'business_id': 'businessid_7', 'name': 'Eagle Luxe Reel Theatre'}, {'_id': '6859a000fe8b31cd7362e2d6', 'business_id': 'businessid_51', 'name': "Gram's Place"}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76', 'name': 'Big Lots'}, {'_id': '6859a000fe8b31cd7362e2d8', 'business_id': 'businessid_100', 'name': 'Service First Heating & Air Conditioning'}, {'_id': '6859a000fe8b31cd7362e2d9', 'business_id': 'businessid_5', 'name': 'Simply Done Cafe'}, {'_id': '6859a000fe8b31cd7362e2da', 'business_id': 'businessid_63', 'name': 'The Iron Shop'}, {'_id': '6859a000fe8b31cd7362e2db', 'business_id': 'businessid_45', 'name': 'The Fresh Market'}, {'_id': '6859a000fe8b31cd7362e2dc', 'business_id': 'businessid_68', 'name': 'Brow Art'}, {'_id': '6859a000fe8b31cd7362e2dd', 'business_id': 'businessid_6', 'name': 'The Jungle'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87', 'name': 'Jordans Fish and Chicken'}, {'_id': '6859a000fe8b31cd7362e2df', 'business_id': 'businessid_78', 'name': 'PennDOT'}, {'_id': '6859a000fe8b31cd7362e2e0', 'business_id': 'businessid_79', 'name': 'Pit Stop HQ'}, {'_id': '6859a000fe8b31cd7362e2e1', 'business_id': 'businessid_66', 'name': 'Panda Express'}, {'_id': '6859a000fe8b31cd7362e2e2', 'business_id': 'businessid_55', 'name': 'Uptown Snoballs and Ice Cream'}, {'_id': '6859a000fe8b31cd7362e2e3', 'business_id': 'businessid_30', 'name': 'Dalco Home Remodeling'}, {'_id': '6859a000fe8b31cd7362e2e4', 'business_id': 'businessid_80', 'name': 'New Orleans Eye Specialists'}, {'_id': '6859a000fe8b31cd7362e2e5', 'business_id': 'businessid_15', 'name': 'Take 5 Oil Change'}, {'_id': '6859a000fe8b31cd7362e2e6', 'business_id': 'businessid_96', 'name': 'Farmhaus Restaurant'}, {'_id': '6859a000fe8b31cd7362e2e7', 'business_id': 'businessid_11', 'name': 'Allan Link,DMD - The DentaLink'}, {'_id': '6859a000fe8b31cd7362e2e8', 'business_id': 'businessid_73', 'name': 'Biggest Little Pools'}, {'_id': '6859a000fe8b31cd7362e2e9', 'business_id': 'businessid_4', 'name': 'Dentistry for Children and Adolescents - St. Charles'}, {'_id': '6859a000fe8b31cd7362e2ea', 'business_id': 'businessid_77', 'name': 'Holiday Inn Philadelphia Stadium'}, {'_id': '6859a000fe8b31cd7362e2eb', 'business_id': 'businessid_18', 'name': 'Sleep Number'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65', 'name': "Pat Flynn's Public House"}, {'_id': '6859a000fe8b31cd7362e2ed', 'business_id': 'businessid_86', 'name': "Humpty's Dumplings"}, {'_id': '6859a000fe8b31cd7362e2ee', 'business_id': 'businessid_53', 'name': 'Samwich'}, {'_id': '6859a000fe8b31cd7362e2ef', 'business_id': 'businessid_40', 'name': 'Artesano Gallery & Iron Works'}, {'_id': '6859a000fe8b31cd7362e2f0', 'business_id': 'businessid_44', 'name': 'Fishtown Diner'}, {'_id': '6859a000fe8b31cd7362e2f1', 'business_id': 'businessid_43', 'name': 'Taco Bell'}, {'_id': '6859a000fe8b31cd7362e2f2', 'business_id': 'businessid_72', 'name': 'VE MOTORS'}, {'_id': '6859a000fe8b31cd7362e2f3', 'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe'}, {'_id': '6859a000fe8b31cd7362e2f4', 'business_id': 'businessid_20', 'name': 'Chick-fil-A'}, {'_id': '6859a000fe8b31cd7362e2f5', 'business_id': 'businessid_37', 'name': 'Orangetheory Fitness Carrollwood'}, {'_id': '6859a000fe8b31cd7362e2f6', 'business_id': 'businessid_56', 'name': 'Orkin'}, {'_id': '6859a000fe8b31cd7362e2f7', 'business_id': 'businessid_62', 'name': 'Winn Dixie'}, {'_id': '6859a000fe8b31cd7362e2f8', 'business_id': 'businessid_94', 'name': 'Taste of Europe'}, {'_id': '6859a000fe8b31cd7362e2f9', 'business_id': 'businessid_39', 'name': 'TITLE Boxing Club'}, {'_id': '6859a000fe8b31cd7362e2fa', 'business_id': 'businessid_90', 'name': "Long John Silver's"}, {'_id': '6859a000fe8b31cd7362e2fb', 'business_id': 'businessid_31', 'name': 'Island Way Car Wash'}, {'_id': '6859a000fe8b31cd7362e2fc', 'business_id': 'businessid_85', 'name': 'Insomnia Cookies'}, {'_id': '6859a000fe8b31cd7362e2fd', 'business_id': 'businessid_25', 'name': 'Great Harvest Bread Co'}, {'_id': '6859a000fe8b31cd7362e2fe', 'business_id': 'businessid_82', 'name': 'Miles Table'}, {'_id': '6859a000fe8b31cd7362e2ff', 'business_id': 'businessid_58', 'name': 'GOLFTEC Westshore'}, {'_id': '6859a000fe8b31cd7362e300', 'business_id': 'businessid_12', 'name': 'Atlantic Trap & Gill Pub'}, {'_id': '6859a000fe8b31cd7362e301', 'business_id': 'businessid_99', 'name': 'Glenora Pizza'}, {'_id': '6859a000fe8b31cd7362e302', 'business_id': 'businessid_60', 'name': 'Walmart'}, {'_id': '6859a000fe8b31cd7362e303', 'business_id': 'businessid_21', 'name': 'Ford of Port Richey'}, {'_id': '6859a000fe8b31cd7362e304', 'business_id': 'businessid_98', 'name': 'Brookmont Apartment Homes'}, {'_id': '6859a000fe8b31cd7362e305', 'business_id': 'businessid_16', 'name': 'Fox and Hound English Pub and Grille'}, {'_id': '6859a000fe8b31cd7362e306', 'business_id': 'businessid_46', 'name': 'Salt + Smoke'}, {'_id': '6859a000fe8b31cd7362e307', 'business_id': 'businessid_22', 'name': 'Main Line Spine'}, {'_id': '6859a000fe8b31cd7362e308', 'business_id': 'businessid_36', 'name': 'Pho & Beyond'}, {'_id': '6859a000fe8b31cd7362e309', 'business_id': 'businessid_69', 'name': 'Cobs Bread'}, {'_id': '6859a000fe8b31cd7362e30a', 'business_id': 'businessid_23', 'name': 'Harbor Freight'}, {'_id': '6859a000fe8b31cd7362e30b', 'business_id': 'businessid_38', 'name': 'Philadelphia Hair Studio'}, {'_id': '6859a000fe8b31cd7362e30c', 'business_id': 'businessid_81', 'name': 'Fantastic Sams Cut & Color'}, {'_id': '6859a000fe8b31cd7362e30d', 'business_id': 'businessid_13', 'name': 'Avian Glen Winery'}, {'_id': '6859a000fe8b31cd7362e30e', 'business_id': 'businessid_17', 'name': 'Whitemarsh Jewelers'}]}

exec(code, env_args)
