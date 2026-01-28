code = """import json
import pandas as pd
from collections import Counter

# Load files
with open(var_call_SO6OXFp6NgGUk5F6Iw4heqeq, 'r') as f:
    reviews = json.load(f)
with open(var_call_U0YlWfK21jXVxwd3fJUSipUf, 'r') as f:
    businesses = json.load(f)

rev_df = pd.DataFrame(reviews)
bus_df = pd.DataFrame(businesses)

# Parse dates: normalize by removing ' at ' and commas
rev_df['date_clean'] = rev_df['date'].astype(str).str.replace(' at ', ' ', regex=False).str.replace(',', '', regex=False)
rev_df['parsed_date'] = pd.to_datetime(rev_df['date_clean'], errors='coerce')
rev_df = rev_df[rev_df['parsed_date'].notna()]
rev_df = rev_df[rev_df['parsed_date'] >= pd.to_datetime('2016-01-01')]

# Build business description map
bus_map = {b['business_id']: (b.get('description') or '') for b in businesses}

# Category extraction heuristic
def extract_categories(desc):
    if not desc or not isinstance(desc, str):
        return []
    s = desc
    s_lower = s.lower()
    # prefer substring after certain keywords
    keywords = ['the category of', 'the fields of', 'providing a range of services in', 'provides a range of services in', 'offers a range of services in', 'offers a diverse range of services and products in', 'offers a diverse range of services in', 'offers a range of services and products in', 'offers', 'provides', 'providing']
    for kw in keywords:
        if kw in s_lower:
            idx = s_lower.rfind(kw)
            s = s[idx + len(kw):]
            break
    # remove location-like prefixes such as 'located at ... in'
    if 'located at' in s_lower:
        # try to remove up to the last ' in '
        parts = s.lower().split(' in ')
        if len(parts) > 1:
            s = parts[-1]
    # split by commas and ' and '
    parts = [p.strip() for p in s.replace(';', ',').replace('/', ',').split(',') if p.strip()]
    cats = []
    for p in parts:
        # split on ' and '
        subparts = [sp.strip() for sp in p.split(' and ') if sp.strip()]
        for sp in subparts:
            # remove trailing phrases
            for tail in ['to meet all your travel and transportation needs.', 'and products', 'and products.', 'and products in', 'in the fields of', 'in the category of']:
                if sp.lower().endswith(tail):
                    sp = sp[: -len(tail)].strip()
            # clean
            sp = sp.strip('. ')
            # discard if looks like address or contains digits
            if any(ch.isdigit() for ch in sp):
                continue
            if len(sp) < 2:
                continue
            cats.append(sp)
    return cats

counter = Counter()
miss = 0
for _, row in rev_df.iterrows():
    bref = row.get('business_ref')
    if not isinstance(bref, str):
        continue
    busid = bref.replace('businessref_', 'businessid_')
    desc = bus_map.get(busid, '')
    if not desc:
        miss += 1
        continue
    cats = extract_categories(desc)
    if not cats:
        # fallback: take last up to 5 comma-separated tokens
        parts = [p.strip() for p in desc.split(',') if p.strip()]
        parts = parts[-5:]
        cats = [p for p in parts if not any(ch.isdigit() for ch in p)]
    for c in cats:
        counter[c] += 1

top5 = counter.most_common(5)
result = [{'category': c, 'review_count': int(n)} for c, n in top5]

if not result:
    out = {'error': 'no result'}
else:
    out = result

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_H3tNkkJnVg4GKZ7CuRooowRi': ['checkin', 'business'], 'var_call_KjmjxSa7bYKHSxtVJBsHv8vA': ['review', 'tip', 'user'], 'var_call_VeTYA7Tv10AamPtT470mCXGK': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_QqpnNFWg63Ba6V9KqXrPbVQF': [{'user_id': 'userid_286', 'yelping_since': '15 Jan 2009, 16:40'}, {'user_id': 'userid_1331', 'yelping_since': '13 Jul 2010, 15:42'}, {'user_id': 'userid_1880', 'yelping_since': '2010-09-07 23:24:36'}, {'user_id': 'userid_271', 'yelping_since': 'October 23, 2011 at 07:47 PM'}, {'user_id': 'userid_534', 'yelping_since': '2011-08-30 13:46:26'}, {'user_id': 'userid_1997', 'yelping_since': '2009-12-02 18:54:31'}, {'user_id': 'userid_1386', 'yelping_since': '2009-04-15 12:46:06'}, {'user_id': 'userid_237', 'yelping_since': 'October 04, 2009 at 05:59 PM'}, {'user_id': 'userid_596', 'yelping_since': '20 Apr 2008, 16:55'}, {'user_id': 'userid_948', 'yelping_since': '2007-07-28 22:22:09'}], 'var_call_SO6OXFp6NgGUk5F6Iw4heqeq': 'file_storage/call_SO6OXFp6NgGUk5F6Iw4heqeq.json', 'var_call_U0YlWfK21jXVxwd3fJUSipUf': 'file_storage/call_U0YlWfK21jXVxwd3fJUSipUf.json'}

exec(code, env_args)
