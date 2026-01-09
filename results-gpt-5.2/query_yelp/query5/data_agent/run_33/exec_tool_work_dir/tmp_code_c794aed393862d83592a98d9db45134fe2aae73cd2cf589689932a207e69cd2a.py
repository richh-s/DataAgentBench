code = """import json, re, pandas as pd

path = var_call_F9xXFmVfBcesujSM6jiNZREw
with open(path, 'r') as f:
    businesses = json.load(f)

def extract_state(desc: str):
    if not isinstance(desc, str):
        return None
    m = re.search(r"\b([A-Z]{2})\b(?=,?\s*(?:this|This)\b)", desc)
    if m:
        return m.group(1)
    m = re.search(r"\b([A-Z]{2})\b\s*(?:\d{5})(?:-\d{4})?\b", desc)
    if m:
        return m.group(1)
    m = re.search(r"\b([A-Z]{2})\b\s*,\s*(?:this|This)\b", desc)
    if m:
        return m.group(1)
    return None

rows=[]
for b in businesses:
    rows.append({
        'business_id': b.get('business_id'),
        'state': extract_state(b.get('description',''))
    })
df=pd.DataFrame(rows).dropna(subset=['business_id','state'])
# count per state
state_counts = df.groupby('state')['business_id'].nunique().sort_values(ascending=False)
if state_counts.empty:
    result = {'state': None, 'wifi_business_count': 0, 'avg_rating': None}
else:
    top_state = state_counts.index[0]
    top_ids = df.loc[df['state']==top_state, 'business_id'].unique().tolist()
    # map to businessref prefix
    top_refs = [bid.replace('businessid_', 'businessref_', 1) for bid in top_ids]
    result = {'top_state': top_state, 'wifi_business_count': int(state_counts.iloc[0]), 'top_refs': top_refs}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_IybcZWyw9661CESDZMUz9zpC': [], 'var_call_1nlZKyh6xNpOyVieFrtzLZfP': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'True', 'NoiseLevel': "u'quiet'", 'WiFi': "u'no'"}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64', 'attributes': {'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': True, 'valet': False}", 'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'True', 'WiFi': "u'free'"}, 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'_id': '6859a000fe8b31cd7362e2b7', 'business_id': 'businessid_54', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'WheelchairAccessible': 'True', 'RestaurantsDelivery': 'True', 'RestaurantsTakeOut': 'True', 'RestaurantsPriceRange2': '1', 'WiFi': "u'free'"}, 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91', 'attributes': {'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'WiFi': "u'free'", 'WheelchairAccessible': 'True', 'Caters': 'True', 'HasTV': 'True', 'HappyHour': 'False', 'Ambience': "{'touristy': None, 'hipster': None, 'romantic': None, 'divey': None, 'intimate': True, 'trendy': None, 'upscale': None, 'classy': True, 'casual': True}", 'RestaurantsDelivery': 'True', 'RestaurantsPriceRange2': '2', 'GoodForKids': 'True', 'RestaurantsAttire': "u'casual'", 'BikeParking': 'True', 'OutdoorSeating': 'True', 'NoiseLevel': "u'quiet'", 'RestaurantsGoodForGroups': 'True', 'RestaurantsTakeOut': 'True', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsReservations': 'False', 'GoodForMeal': "{'dessert': None, 'latenight': None, 'lunch': True, 'dinner': None, 'brunch': True, 'breakfast': True}", 'Alcohol': "u'beer_and_wine'", 'RestaurantsTableService': 'True', 'Corkage': 'False', 'BYOB': 'True'}, 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}], 'var_call_F9xXFmVfBcesujSM6jiNZREw': 'file_storage/call_F9xXFmVfBcesujSM6jiNZREw.json'}

exec(code, env_args)
