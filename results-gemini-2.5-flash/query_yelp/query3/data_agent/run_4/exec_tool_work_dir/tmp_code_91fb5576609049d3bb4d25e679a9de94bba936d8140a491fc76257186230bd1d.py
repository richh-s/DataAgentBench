code = """import json
import pandas as pd

business_data = locals()['var_function-call-3791233074324712529']

parking_businesses = set()

for business in business_data:
    attributes = business.get('attributes')
    if attributes and isinstance(attributes, dict):
        business_parking = attributes.get('BusinessParking')
        bike_parking = attributes.get('BikeParking')

        has_parking = False
        if business_parking:
            try:
                # BusinessParking is a string representation of a dict
                parking_dict = eval(business_parking) # Using eval as the string format looks like a Python dict
                if any(parking_dict.values()):
                    has_parking = True
            except (TypeError, ValueError, SyntaxError):
                pass # Ignore if parsing fails
        
        if bike_parking and str(bike_parking).lower() == 'true':
            has_parking = True

        if has_parking:
            parking_businesses.add(business['business_id'])


result = len(parking_businesses)

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-11225216062189703582': [{'business_ref': 'businessref_71'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_69'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_92'}], 'var_function-call-2181022083988587196': {'collection': 'business', 'filter': {'business_id': {'$in': ['businessid_71', 'businessid_46', 'businessid_25', 'businessid_43', 'businessid_57', 'businessid_68', 'businessid_45', 'businessid_69', 'businessid_28', 'businessid_92']}}, 'projection': {'_id': 0, 'business_id': 1, 'attributes': 1}}, 'var_function-call-3791233074324712529': [{'business_id': 'businessid_92', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'True', 'NoiseLevel': "u'quiet'", 'WiFi': "u'no'"}}, {'business_id': 'businessid_71', 'attributes': {'BusinessAcceptsCreditCards': 'True'}}, {'business_id': 'businessid_28', 'attributes': 'None'}, {'business_id': 'businessid_57', 'attributes': {'BusinessAcceptsCreditCards': 'False', 'BusinessAcceptsBitcoin': 'False', 'ByAppointmentOnly': 'False'}}, {'business_id': 'businessid_45', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}", 'RestaurantsPriceRange2': '2', 'BikeParking': 'True', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsTakeOut': 'True', 'DogsAllowed': 'False', 'Caters': 'True', 'NoiseLevel': "u'quiet'", 'GoodForKids': 'True', 'RestaurantsDelivery': 'True'}}]}

exec(code, env_args)
