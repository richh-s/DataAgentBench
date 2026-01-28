code = """import json
import pandas as pd

with open(var_call_By0YsQSKO0TUH7HYGOuh2IE3, 'r') as f:
    businesses = json.load(f)
with open(var_call_TlPasEwRwrpoipslO3NtzTX9, 'r') as f:
    reviews = json.load(f)

df_b = pd.DataFrame(businesses)
df_r = pd.DataFrame(reviews)

# ensure columns
for col in ['attributes','categories','description','business_id']:
    if col not in df_b.columns:
        df_b[col] = None

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

df_b['accepts_cc'] = df_b['attributes'].apply(accepts_cc)

# extract categories
def categories_from_row(row):
    c = row.get('categories')
    if c and not (isinstance(c, str) and c.lower() == 'none'):
        if isinstance(c, list):
            return [str(x).strip() for x in c if str(x).strip()]
        return [p.strip() for p in str(c).split(',') if p.strip()]
    desc = row.get('description')
    if not isinstance(desc, str):
        return []
    low = desc.lower()
    idx = low.rfind(' in ')
    if idx != -1:
        sub = desc[idx+4:]
        dot = sub.find('.')
        if dot != -1:
            sub = sub[:dot]
        sub = sub.replace(' and ', ',').replace(' & ', ',').replace(';', ',')
        parts = [p.strip().strip("'\"") for p in sub.split(',') if p.strip()]
        parts = [p for p in parts if not any(ch.isdigit() for ch in p) and len(p) > 1]
        return parts
    return []

# apply
df_b['category_list'] = df_b.apply(categories_from_row, axis=1)

# map to business_ref
def to_ref(bid):
    if isinstance(bid, str):
        return bid.replace('businessid_', 'businessref_')
    return None

df_b['business_ref'] = df_b['business_id'].apply(to_ref)

# filter accepts credit
acc = df_b[df_b['accepts_cc'] == True].copy()

# explode categories
acc = acc.explode('category_list')
acc['category_list'] = acc['category_list'].apply(lambda x: x.strip() if isinstance(x, str) else x)
acc = acc[acc['category_list'].notna() & (acc['category_list'] != '')]

result = {'category': None, 'business_count': 0, 'average_rating': None}

if not acc.empty:
    counts = acc.groupby('category_list')['business_id'].nunique().sort_values(ascending=False)
    top_cat = counts.index[0]
    top_count = int(counts.iloc[0])
    refs = set(acc[acc['category_list'] == top_cat]['business_ref'].dropna().tolist())
    # prepare reviews
    if not df_r.empty:
        df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
    else:
        df_r['rating'] = pd.Series(dtype=float)
    sel = df_r[df_r['business_ref'].isin(refs)]
    if len(sel) > 0:
        avg = round(float(sel['rating'].mean()), 2)
    else:
        avg = None
    result = {'category': top_cat, 'business_count': top_count, 'average_rating': avg}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_zYWWfxdtpjIy5owlOM4SaGDn': ['business', 'checkin'], 'var_call_mHA3vgr16eyfCZYaS9qPg3uP': ['review', 'tip', 'user'], 'var_call_By0YsQSKO0TUH7HYGOuh2IE3': 'file_storage/call_By0YsQSKO0TUH7HYGOuh2IE3.json', 'var_call_TlPasEwRwrpoipslO3NtzTX9': 'file_storage/call_TlPasEwRwrpoipslO3NtzTX9.json', 'var_call_y3E5KsRHzfEDIvVCCDQoNDKU': {'category': None, 'business_count': 0, 'average_rating': None}, 'var_call_4EyBBhMx0IX87GBMEIVF9q5X': 'file_storage/call_4EyBBhMx0IX87GBMEIVF9q5X.json', 'var_call_5gb3J7A0uHjJTrUuB8IRGuPQ': {'category': None, 'business_count': 0, 'average_rating': None}, 'var_call_SQnWJqlQg4SiEy3h3gQSfFwa': {'total_businesses': 100, 'attributes_nonnull': 100, 'accepts_cc_count': 75, 'sample_accepts': [{'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'business_id': 'businessid_88', 'name': 'Impact Guns', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'business_id': 'businessid_33', 'name': 'J&Q Nails', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}, {'business_id': 'businessid_92', 'name': 'Luminosity', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'True', 'NoiseLevel': "u'quiet'", 'WiFi': "u'no'"}}, {'business_id': 'businessid_64', 'name': 'Nail Care Salon', 'attributes': {'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': True, 'valet': False}", 'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'True', 'WiFi': "u'free'"}}, {'business_id': 'businessid_52', 'name': 'Architectural Antiques of Indianapolis', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'BikeParking': 'True'}}, {'business_id': 'businessid_29', 'name': "Aster's Floral Shop", 'attributes': {'BikeParking': 'True', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '2', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsDelivery': 'None'}}, {'business_id': 'businessid_10', 'name': 'China Wok', 'attributes': {'RestaurantsGoodForGroups': 'True', 'RestaurantsDelivery': 'False', 'RestaurantsTakeOut': 'True', 'HasTV': 'True', 'BusinessAcceptsCreditCards': 'True', 'Ambience': "{'touristy': False, 'hipster': False, 'romantic': False, 'divey': False, 'intimate': False, 'trendy': False, 'upscale': False, 'classy': False, 'casual': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}", 'BusinessParking': "{u'valet': False, u'garage': False, u'street': False, u'lot': True, u'validated': False}"}}, {'business_id': 'businessid_61', 'name': 'Brandon Family Medical Care', 'attributes': {'ByAppointmentOnly': 'True', 'BusinessAcceptsCreditCards': 'True'}}]}}

exec(code, env_args)
