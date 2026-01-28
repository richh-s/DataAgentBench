code = """import json, re

# Load the business docs from the stored JSON file path
fp = var_call_3n7CuaG7JdRRHiQckUQOKYDh
with open(fp, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Helper to determine if WiFi is offered
def wifi_offered(val):
    if val is None:
        return False
    s = str(val).lower()
    return 'no' not in s

# Extract state from description using regex
state_counts = {}
state_business_ids = {}

for d in docs:
    wifi_val = None
    if 'attributes' in d and d['attributes'] and 'WiFi' in d['attributes']:
        wifi_val = d['attributes']['WiFi']
    if not wifi_offered(wifi_val):
        continue
    desc = d.get('description','') or ''
    # find pattern like ", XX," where XX are two letters
    m = re.search(r',\s*([A-Z]{2})[,\s]', desc)
    if not m:
        # try lowercase or variations
        m = re.search(r',\s*([A-Za-z]{2})[,\s]', desc)
    if not m:
        continue
    state = m.group(1).upper()
    state_counts[state] = state_counts.get(state, 0) + 1
    state_business_ids.setdefault(state, []).append(d['business_id'])

if not state_counts:
    result = {"top_state": None, "count": 0, "business_ids": [], "business_refs": []}
else:
    # find state with max count (if tie, pick the first sorted)
    max_count = max(state_counts.values())
    top_states = [s for s,c in state_counts.items() if c==max_count]
    top_states.sort()
    top_state = top_states[0]
    biz_ids = state_business_ids[top_state]
    biz_refs = [bid.replace('businessid_','businessref_') for bid in biz_ids]
    result = {"top_state": top_state, "count": max_count, "business_ids": biz_ids, "business_refs": biz_refs}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_1o2zFCOf1hHTSbMhk4XAjGii': [{'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'attributes': {'WiFi': "u'no'"}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_92', 'name': 'Luminosity', 'attributes': {'WiFi': "u'no'"}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'business_id': 'businessid_64', 'name': 'Nail Care Salon', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'business_id': 'businessid_54', 'name': '7-Eleven', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'business_id': 'businessid_91', 'name': 'Cafe Porche and snowbar', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}], 'var_call_3n7CuaG7JdRRHiQckUQOKYDh': 'file_storage/call_3n7CuaG7JdRRHiQckUQOKYDh.json'}

exec(code, env_args)
