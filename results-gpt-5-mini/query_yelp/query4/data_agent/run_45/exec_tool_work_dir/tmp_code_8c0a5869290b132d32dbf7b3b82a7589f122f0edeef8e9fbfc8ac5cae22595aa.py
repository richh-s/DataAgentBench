code = """import json
from collections import Counter
with open(var_call_7oXHbp7Wt1huh37rUPVR1WE5, 'r') as f:
    businesses = json.load(f)

key_counter = Counter()
examples = {}
for b in businesses:
    for k in b.keys():
        key_counter[k]+=1
    # store first example
    if len(examples) < 5:
        examples[b.get('business_id')] = b

res = {'keys_counts': key_counter, 'examples_first_5': examples}
print('__RESULT__:')
import json
print(json.dumps(res, default=str))"""

env_args = {'var_call_tQod4WpsZZ0iGs8eN9r24z3L': ['business', 'checkin'], 'var_call_HXyX9Uhr94AH0xmlZr2p5i88': ['review', 'tip', 'user'], 'var_call_7oXHbp7Wt1huh37rUPVR1WE5': 'file_storage/call_7oXHbp7Wt1huh37rUPVR1WE5.json', 'var_call_kAnS6MmOjvKHyymYKR3mmpXQ': 'file_storage/call_kAnS6MmOjvKHyymYKR3mmpXQ.json', 'var_call_XXnr7iNttN1XqWuaXcJOZkaW': {'category': None, 'business_count': 0, 'average_rating': None}, 'var_call_h926EbCCFTcwULY7IezTOYCU': {'total_businesses': 100, 'businesses_accepting_credit_cards': 75, 'businesses_with_categories_field': 0, 'top_categories_among_credit_accepting': [], 'examples_missing_categories': [{'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'business_id': 'businessid_88', 'name': 'Impact Guns', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'attributes': 'None'}, {'business_id': 'businessid_33', 'name': 'J&Q Nails', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}]}}

exec(code, env_args)
