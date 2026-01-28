code = """import json
from collections import Counter
with open(var_call_SAZGzLxLXbN199MGBjTmNm1v,'r') as f:
    businesses = json.load(f)
keys = Counter()
for doc in businesses:
    keys.update(doc.keys())

# inspect possible category-like fields and sample values
samples = []
for doc in businesses[:50]:
    samples.append({k: doc.get(k) for k in doc.keys()})

# look for description field values
descs = [doc.get('description') for doc in businesses if 'description' in doc]

result = {
    'key_counts': keys.most_common(),
    'num_with_description': sum(1 for d in businesses if 'description' in d),
    'sample_with_description': descs[:5],
    'sample_names': [doc.get('name') for doc in businesses[:50]]
}
import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_PfBFEnOqSxBmE3yZz4jDYeYE': ['business', 'checkin'], 'var_call_NjmNYE8FrhRYoKqDZPZ3zDE6': ['review', 'tip', 'user'], 'var_call_SAZGzLxLXbN199MGBjTmNm1v': 'file_storage/call_SAZGzLxLXbN199MGBjTmNm1v.json', 'var_call_y40HEuxeyQN0L9Kcca7Zn9Up': 'file_storage/call_y40HEuxeyQN0L9Kcca7Zn9Up.json', 'var_call_OYr07TAIM4tYqxzrmcLlah9K': {'category': None, 'business_count': 0, 'average_rating': None}, 'var_call_cJwCo0GamawHsfMO6EaPGwZr': {'total_documents': 100, 'most_common_keys': [['_id', 20], ['business_id', 20], ['name', 20], ['attributes', 20]], 'has_categories_count': 0, 'possible_fields_counts': {'categories': 0, 'categoriesList': 0, 'category': 0, 'Category': 0}, 'sample_first_5': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'attributes': 'None'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}]}}

exec(code, env_args)
