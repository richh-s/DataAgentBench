code = """import json
import pandas as pd
import re
from collections import Counter

# Load users who registered in 2016
users_2016 = var_call_BT9GUpvGlH81l5W9DAOKKJ4X
user_set = set([d['user_id'] for d in users_2016 if d.get('user_id') and d.get('user_id') != 'None'])

# Load reviews (from file path)
with open(var_call_NAI5BdMciir97GYCfhMVlJ7f, 'r') as f:
    reviews = json.load(f)

# Load businesses
with open(var_call_iWqGTj1qhUME9LQ7CkFmihjf, 'r') as f:
    businesses = json.load(f)

# DataFrame for reviews
df_reviews = pd.DataFrame(reviews)
if df_reviews.empty:
    df_reviews = pd.DataFrame(columns=['review_id','user_id','business_ref','date'])

# Normalize user_id
df_reviews['user_id'] = df_reviews['user_id'].where(df_reviews['user_id'] != 'None', None)

# Parse dates and filter on/after 2016-01-01
df_reviews['date_parsed'] = pd.to_datetime(df_reviews['date'], errors='coerce')
df_reviews = df_reviews[df_reviews['date_parsed'] >= pd.to_datetime('2016-01-01')]

# Filter to users registered in 2016
df_reviews = df_reviews[df_reviews['user_id'].isin(user_set)]

# Map business_ref to business_id
if not df_reviews.empty:
    df_reviews['business_id'] = df_reviews['business_ref'].str.replace('businessref_', 'businessid_', regex=False)
else:
    df_reviews['business_id'] = pd.Series(dtype=str)

# Simple category extraction
def extract_categories(desc):
    if not desc or not isinstance(desc, str):
        return []
    s = desc
    s_low = s.lower()
    # keywords to locate the start of categories
    kws = ['offers a range of services in', 'offers a wide range of services, including',
           'offers a diverse range of services and products in the fields of', 'offers a range of services, including',
           'offers a variety of services including', 'in the category of', 'in the fields of', 'in the category', 'including', 'offers a wide range of services', 'offers']
    pos = None
    for kw in kws:
        i = s_low.find(kw)
        if i != -1:
            pos = i + len(kw)
            break
    if pos is None:
        return []
    rest = s[pos:]
    # remove any 'located at' fragments
    rest = re.split(r'located at', rest, flags=re.IGNORECASE)[0]
    # replace ' and ' and ' & ' with commas
    rest = re.sub(r'\s+and\s+|\s*&\s*', ',', rest, flags=re.IGNORECASE)
    # split on commas, slashes, semicolons, pipes
    parts = re.split(r',|/|;|\|', rest)
    cats = []
    for p in parts:
        # strip surrounding punctuation and whitespace
        p = re.sub(r"^[\s\.,:;\"']+|[\s\.,:;\"']+$", '', p)
        if not p:
            continue
        # drop segments that look like addresses by checking for digits or 'located'
        if re.search(r'\d', p) or 'located' in p.lower():
            continue
        # remove filler words
        p = re.sub(r'\b(services|service|products|product|including|offers|offering|offers a range of|offers a wide range of|offers a diverse range of|the fields of|the category of)\b', '', p, flags=re.IGNORECASE).strip()
        if not p:
            continue
        # split further on '&' or ' and '
        sub = re.split(r'\s*&\s*|\s+and\s+', p)
        for ssub in sub:
            ssub = ssub.strip()
            if not ssub:
                continue
            # remove trailing words like 'services'
            ssub = re.sub(r'\b(services|service|products|product)\b', '', ssub, flags=re.IGNORECASE).strip()
            if len(ssub) >= 2:
                cats.append(ssub)
    # deduplicate while preserving order
    seen = set(); out = []
    for c in cats:
        key = c.lower()
        if key not in seen:
            seen.add(key); out.append(c)
    return out

# Build mapping from business_id to categories
biz_cat = {}
for b in businesses:
    bid = b.get('business_id')
    desc = b.get('description', '')
    cats = extract_categories(desc)
    if cats:
        biz_cat[bid] = cats

# Count reviews per category
counter = Counter()
for bid in df_reviews['business_id'].tolist():
    cats = biz_cat.get(bid)
    if not cats:
        continue
    for c in cats:
        counter[c] += 1

# Top 5
top5 = counter.most_common(5)
result = [{'category': k, 'review_count': v} for k, v in top5]

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_xVWR4py9CToFptWsS3Y27BJ4': ['business', 'checkin'], 'var_call_gPc7FrJHmGpMknNmh1A0Sacv': ['review', 'tip', 'user'], 'var_call_52Im5mebgtntnu5ujIInKq9F': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_DOU9wsYAjfEPGlTozFExh1uR': [{'user_id': 'userid_286', 'yelping_since': '15 Jan 2009, 16:40'}, {'user_id': 'userid_1331', 'yelping_since': '13 Jul 2010, 15:42'}, {'user_id': 'userid_1880', 'yelping_since': '2010-09-07 23:24:36'}, {'user_id': 'userid_271', 'yelping_since': 'October 23, 2011 at 07:47 PM'}, {'user_id': 'userid_534', 'yelping_since': '2011-08-30 13:46:26'}, {'user_id': 'userid_1997', 'yelping_since': '2009-12-02 18:54:31'}, {'user_id': 'userid_1386', 'yelping_since': '2009-04-15 12:46:06'}, {'user_id': 'userid_237', 'yelping_since': 'October 04, 2009 at 05:59 PM'}, {'user_id': 'userid_596', 'yelping_since': '20 Apr 2008, 16:55'}, {'user_id': 'userid_948', 'yelping_since': '2007-07-28 22:22:09'}], 'var_call_BT9GUpvGlH81l5W9DAOKKJ4X': [{'user_id': 'userid_1231'}, {'user_id': 'userid_343'}, {'user_id': 'userid_746'}, {'user_id': 'userid_505'}, {'user_id': 'userid_898'}, {'user_id': 'userid_144'}, {'user_id': 'userid_1927'}, {'user_id': 'userid_1109'}, {'user_id': 'userid_1950'}, {'user_id': 'userid_1316'}, {'user_id': 'userid_805'}, {'user_id': 'userid_1182'}, {'user_id': 'userid_431'}, {'user_id': 'userid_1287'}, {'user_id': 'userid_151'}, {'user_id': 'userid_1274'}, {'user_id': 'userid_1158'}, {'user_id': 'userid_643'}, {'user_id': 'userid_1558'}, {'user_id': 'userid_1542'}, {'user_id': 'userid_508'}, {'user_id': 'userid_435'}, {'user_id': 'userid_1398'}, {'user_id': 'userid_958'}, {'user_id': 'userid_68'}, {'user_id': 'userid_145'}, {'user_id': 'userid_518'}, {'user_id': 'userid_1879'}, {'user_id': 'userid_1981'}, {'user_id': 'userid_64'}, {'user_id': 'userid_211'}, {'user_id': 'userid_308'}, {'user_id': 'userid_1444'}, {'user_id': 'userid_1179'}, {'user_id': 'userid_677'}, {'user_id': 'userid_537'}, {'user_id': 'userid_208'}, {'user_id': 'userid_1397'}, {'user_id': 'userid_324'}, {'user_id': 'userid_795'}, {'user_id': 'userid_863'}, {'user_id': 'userid_100'}, {'user_id': 'userid_1333'}, {'user_id': 'userid_1636'}, {'user_id': 'userid_38'}, {'user_id': 'userid_1850'}, {'user_id': 'userid_401'}, {'user_id': 'userid_711'}, {'user_id': 'userid_729'}, {'user_id': 'userid_1505'}, {'user_id': 'userid_374'}, {'user_id': 'userid_1315'}, {'user_id': 'userid_597'}, {'user_id': 'userid_386'}, {'user_id': 'userid_1978'}, {'user_id': 'userid_862'}, {'user_id': 'userid_1068'}, {'user_id': 'userid_1708'}, {'user_id': 'userid_522'}, {'user_id': 'userid_1246'}, {'user_id': 'userid_339'}, {'user_id': 'userid_1786'}, {'user_id': 'userid_1661'}, {'user_id': 'userid_152'}, {'user_id': 'userid_1376'}, {'user_id': 'userid_851'}, {'user_id': 'userid_1940'}, {'user_id': 'userid_216'}, {'user_id': 'userid_39'}, {'user_id': 'userid_850'}, {'user_id': 'userid_1419'}, {'user_id': 'userid_425'}, {'user_id': 'userid_582'}, {'user_id': 'userid_333'}, {'user_id': 'userid_1288'}, {'user_id': 'userid_252'}, {'user_id': 'userid_676'}, {'user_id': 'userid_361'}, {'user_id': 'userid_1675'}, {'user_id': 'userid_1490'}, {'user_id': 'userid_123'}, {'user_id': 'userid_227'}, {'user_id': 'userid_510'}, {'user_id': 'userid_577'}, {'user_id': 'userid_242'}, {'user_id': 'userid_771'}, {'user_id': 'userid_1350'}, {'user_id': 'userid_1077'}, {'user_id': 'userid_1013'}, {'user_id': 'userid_1030'}, {'user_id': 'userid_1902'}, {'user_id': 'userid_367'}, {'user_id': 'userid_257'}, {'user_id': 'userid_598'}, {'user_id': 'userid_847'}, {'user_id': 'userid_1343'}, {'user_id': 'userid_792'}, {'user_id': 'userid_673'}, {'user_id': 'userid_243'}, {'user_id': 'userid_1072'}, {'user_id': 'userid_369'}, {'user_id': 'userid_622'}, {'user_id': 'userid_1758'}, {'user_id': 'userid_1856'}, {'user_id': 'userid_384'}, {'user_id': 'userid_1533'}, {'user_id': 'userid_1736'}, {'user_id': 'userid_1161'}, {'user_id': 'userid_359'}, {'user_id': 'userid_318'}, {'user_id': 'userid_1871'}, {'user_id': 'userid_655'}, {'user_id': 'userid_108'}, {'user_id': 'userid_131'}, {'user_id': 'userid_1760'}, {'user_id': 'userid_935'}, {'user_id': 'userid_1139'}, {'user_id': 'userid_210'}, {'user_id': 'userid_70'}, {'user_id': 'userid_25'}, {'user_id': 'userid_1101'}, {'user_id': 'userid_97'}, {'user_id': 'userid_1624'}, {'user_id': 'userid_1739'}, {'user_id': 'userid_942'}, {'user_id': 'userid_945'}, {'user_id': 'userid_842'}, {'user_id': 'userid_986'}, {'user_id': 'userid_1717'}, {'user_id': 'userid_1351'}, {'user_id': 'userid_406'}, {'user_id': 'userid_230'}, {'user_id': 'userid_914'}, {'user_id': 'userid_593'}, {'user_id': 'userid_1083'}, {'user_id': 'userid_742'}, {'user_id': 'userid_1938'}, {'user_id': 'userid_356'}, {'user_id': 'userid_876'}, {'user_id': 'userid_1431'}, {'user_id': 'userid_424'}, {'user_id': 'userid_686'}, {'user_id': 'userid_527'}, {'user_id': 'userid_641'}, {'user_id': 'userid_1346'}, {'user_id': 'userid_1766'}, {'user_id': 'userid_207'}, {'user_id': 'userid_1070'}, {'user_id': 'userid_989'}, {'user_id': 'userid_927'}, {'user_id': 'userid_244'}, {'user_id': 'userid_1816'}, {'user_id': 'userid_1756'}, {'user_id': 'userid_393'}, {'user_id': 'userid_1409'}, {'user_id': 'userid_197'}, {'user_id': 'userid_1178'}, {'user_id': 'userid_526'}, {'user_id': 'userid_90'}, {'user_id': 'userid_661'}, {'user_id': 'userid_238'}, {'user_id': 'userid_1897'}, {'user_id': 'userid_241'}, {'user_id': 'userid_1262'}, {'user_id': 'userid_1727'}, {'user_id': 'userid_1105'}, {'user_id': 'userid_744'}, {'user_id': 'userid_1263'}], 'var_call_NAI5BdMciir97GYCfhMVlJ7f': 'file_storage/call_NAI5BdMciir97GYCfhMVlJ7f.json', 'var_call_iWqGTj1qhUME9LQ7CkFmihjf': 'file_storage/call_iWqGTj1qhUME9LQ7CkFmihjf.json'}

exec(code, env_args)
