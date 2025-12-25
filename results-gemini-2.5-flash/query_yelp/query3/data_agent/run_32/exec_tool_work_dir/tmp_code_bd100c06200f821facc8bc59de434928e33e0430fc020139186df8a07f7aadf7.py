code = """import json
import pandas as pd

business_data_raw_list = locals()['var_function-call-10826148883321482514']['results']
business_data = [json.loads(item) for item in business_data_raw_list]

parking_businesses = []
for business in business_data:
    attributes = business.get('attributes')
    if attributes is None:
        continue
    
    business_parking = attributes.get('BusinessParking')
    bike_parking = attributes.get('BikeParking')

    has_parking = False
    if business_parking is not None and business_parking != 'False':
        if isinstance(business_parking, str):
            try:
                # eval() is used because the string representation of the dictionary might contain single quotes
                parking_dict = eval(business_parking)
                if any(parking_dict.values()):
                    has_parking = True
            except (NameError, SyntaxError):
                pass # Handle cases where eval fails for malformed strings

    if bike_parking == 'True':
        has_parking = True

    if has_parking:
        parking_businesses.append(business['business_id'])

print('__RESULT__:')
print(json.dumps(parking_businesses))"""

env_args = {'var_function-call-10826148883321482514': [{'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'business_id': 'businessid_41', 'attributes': 'None'}, {'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}]}

exec(code, env_args)
