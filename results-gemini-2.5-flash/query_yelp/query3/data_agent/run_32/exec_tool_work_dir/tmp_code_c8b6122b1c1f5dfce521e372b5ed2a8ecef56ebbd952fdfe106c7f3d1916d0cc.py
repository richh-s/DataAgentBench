code = """import json
import pandas as pd

business_data_raw_string = locals()['var_function-call-17467070963102253074']['results'][0]
business_data = json.loads(business_data_raw_string)

parking_businesses = []
for business in business_data:
    attributes = business.get('attributes')
    if attributes is None or attributes == 'None':
        continue
    
    business_parking = attributes.get('BusinessParking')
    bike_parking = attributes.get('BikeParking')

    has_parking = False
    # Check for BusinessParking
    if business_parking is not None and str(business_parking).lower() != 'false':
        if isinstance(business_parking, str):
            try:
                # eval() is used because the string representation of the dictionary might contain single quotes
                parking_dict = eval(business_parking)
                if any(parking_dict.values()):
                    has_parking = True
            except (NameError, SyntaxError):
                pass # Handle cases where eval fails for malformed strings or is not a dict string
        elif isinstance(business_parking, dict):
             if any(business_parking.values()):
                    has_parking = True

    # Check for BikeParking
    if str(bike_parking).lower() == 'true':
        has_parking = True

    if has_parking:
        parking_businesses.append(business['business_id'])

print('__RESULT__:')
print(json.dumps(list(set(parking_businesses))))"""

env_args = {'var_function-call-10826148883321482514': [{'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'business_id': 'businessid_41', 'attributes': 'None'}, {'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}], 'var_function-call-17467070963102253074': [{'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'business_id': 'businessid_41', 'attributes': 'None'}, {'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}]}

exec(code, env_args)
