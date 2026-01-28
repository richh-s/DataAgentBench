code = """import json
import pandas as pd

# Load stored query results
with open(var_call_By0YsQSKO0TUH7HYGOuh2IE3, 'r') as f:
    businesses = json.load(f)
with open(var_call_TlPasEwRwrpoipslO3NtzTX9, 'r') as f:
    reviews = json.load(f)

b = pd.DataFrame(businesses)
r = pd.DataFrame(reviews)

# Ensure columns
for col in ['attributes','categories','description','business_id']:
    if col not in b.columns:
        b[col] = None

# detect accepts credit cards

def accepts_cc(attr):
    if attr is None:
        return False
    if isinstance(attr, dict):
        v = attr.get('BusinessAcceptsCreditCards')
        if v is None:
            return False
        return 'true' in str(v).lower()
    s = str(attr).lower()
    return ('businessacceptscreditcards' in s and 'true' in s)

b['accepts_cc'] = b['attributes'].apply(accepts_cc)

# extract categories from description using string methods

def extract_categories_from_description(desc):
    if not isinstance(desc, str):
        return []
    s = desc
    low = s.lower()
    candidates = []
    # try patterns in order
    patterns = [
        'offers',
        'in the fields of',
        'in the category of',
        'category of',
        'including',
        'offers a range of services in the fields of',
        'offers a diverse range of services and products in the fields of',
    ]
    for pat in patterns:
        idx = low.find(pat)
        if idx != -1:
            # find ' in ' after 'offers' pattern if pattern == 'offers'
            start = None
            if pat == 'offers':
                in_idx = low.find(' in ', idx)
                if in_idx != -1:
                    start = in_idx + 4
                else:
                    start = idx + len(pat)
            elif pat.startswith('offers'):
                in_idx = low.find(' in ', idx)
                if in_idx != -1:
                    start = in_idx + 4
                else:
                    start = idx + len(pat)
            else:
                start = idx + len(pat)
            # take substring until the next period
            sub = s[start:]
            dot = sub.find('.')
            if dot != -1:
                sub = sub[:dot]
            # replace connectors with commas
            sub2 = sub.replace('&', ',').replace('/', ',').replace(' and ', ',')
            parts = [p.strip().strip('\"\'') for p in sub2.split(',') if p.strip()]
            # filter out parts that look like addresses (contain digits) or are too short
            filtered = []
            for p in parts:
                if any(ch.isdigit() for ch in p):
                    continue
                # remove trailing words like 'services' or 'products'
                for suffix in ['services', 'products', 'shopping', 'food', 'and', 'offers']:
                    if p.lower().endswith(' ' + suffix):
                        p = p[:-(len(suffix)+1)].strip()
                if len(p) >= 2:
                    filtered.append(p)
            if filtered:
                return filtered
    return []

# build category list

def categories_from_row(row):
    c = row.get('categories')
    if c and not (isinstance(c, str) and c.lower()=='none'):
        if isinstance(c, list):
            return [str(x).strip() for x in c if str(x).strip()]
        return [p.strip() for p in str(c).split(',') if p.strip()]
    return extract_categories_from_description(row.get('description'))

b['category_list'] = b.apply(categories_from_row, axis=1)

# map to business_ref
b['business_ref'] = b['business_id'].apply(lambda x: x.replace('businessid_','businessref_') if isinstance(x,str) else None)

# filter businesses that accept credit cards
acc = b[b['accepts_cc'] == True].copy()

# explode category_list
if 'category_list' not in acc.columns:
    acc['category_list'] = [[] for _ in range(len(acc))]
acc = acc.explode('category_list')
acc['category_list'] = acc['category_list'].apply(lambda x: x.strip() if isinstance(x,str) else x)
acc = acc[acc['category_list'].notna() & (acc['category_list']!='')]

result = {'category': None, 'business_count': 0, 'average_rating': None}

if not acc.empty:
    counts = acc.groupby('category_list')['business_id'].nunique().sort_values(ascending=False)
    top_cat = counts.index[0]
    top_count = int(counts.iloc[0])
    refs = set(acc[acc['category_list']==top_cat]['business_ref'].dropna().tolist())
    # prepare reviews
    if not r.empty:
        r['rating'] = pd.to_numeric(r['rating'], errors='coerce')
    else:
        r['rating'] = pd.Series(dtype=float)
    sel = r[r['business_ref'].isin(refs)]
    if len(sel) > 0:
        avg = round(float(sel['rating'].mean()),2)
    else:
        avg = None
    result = {'category': top_cat, 'business_count': top_count, 'average_rating': avg}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_zYWWfxdtpjIy5owlOM4SaGDn': ['business', 'checkin'], 'var_call_mHA3vgr16eyfCZYaS9qPg3uP': ['review', 'tip', 'user'], 'var_call_By0YsQSKO0TUH7HYGOuh2IE3': 'file_storage/call_By0YsQSKO0TUH7HYGOuh2IE3.json', 'var_call_TlPasEwRwrpoipslO3NtzTX9': 'file_storage/call_TlPasEwRwrpoipslO3NtzTX9.json', 'var_call_y3E5KsRHzfEDIvVCCDQoNDKU': {'category': None, 'business_count': 0, 'average_rating': None}, 'var_call_4EyBBhMx0IX87GBMEIVF9q5X': 'file_storage/call_4EyBBhMx0IX87GBMEIVF9q5X.json', 'var_call_5gb3J7A0uHjJTrUuB8IRGuPQ': {'category': None, 'business_count': 0, 'average_rating': None}, 'var_call_SQnWJqlQg4SiEy3h3gQSfFwa': {'total_businesses': 100, 'attributes_nonnull': 100, 'accepts_cc_count': 75, 'sample_accepts': [{'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'business_id': 'businessid_88', 'name': 'Impact Guns', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'business_id': 'businessid_33', 'name': 'J&Q Nails', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}, {'business_id': 'businessid_92', 'name': 'Luminosity', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'True', 'NoiseLevel': "u'quiet'", 'WiFi': "u'no'"}}, {'business_id': 'businessid_64', 'name': 'Nail Care Salon', 'attributes': {'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': True, 'valet': False}", 'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'True', 'WiFi': "u'free'"}}, {'business_id': 'businessid_52', 'name': 'Architectural Antiques of Indianapolis', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'BikeParking': 'True'}}, {'business_id': 'businessid_29', 'name': "Aster's Floral Shop", 'attributes': {'BikeParking': 'True', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '2', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsDelivery': 'None'}}, {'business_id': 'businessid_10', 'name': 'China Wok', 'attributes': {'RestaurantsGoodForGroups': 'True', 'RestaurantsDelivery': 'False', 'RestaurantsTakeOut': 'True', 'HasTV': 'True', 'BusinessAcceptsCreditCards': 'True', 'Ambience': "{'touristy': False, 'hipster': False, 'romantic': False, 'divey': False, 'intimate': False, 'trendy': False, 'upscale': False, 'classy': False, 'casual': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}", 'BusinessParking': "{u'valet': False, u'garage': False, u'street': False, u'lot': True, u'validated': False}"}}, {'business_id': 'businessid_61', 'name': 'Brandon Family Medical Care', 'attributes': {'ByAppointmentOnly': 'True', 'BusinessAcceptsCreditCards': 'True'}}]}}

exec(code, env_args)
