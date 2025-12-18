code = """import json
import ast

business_data = locals()['var_function-call-13209217514639810891']

count = 0
for business in business_data:
    attributes = business.get('attributes', {})
    
    has_parking = False
    if 'BusinessParking' in attributes and attributes['BusinessParking'] != 'None':
        try:
            parking_dict = ast.literal_eval(attributes['BusinessParking'])
            if isinstance(parking_dict, dict):
                if any(parking_dict.values()):
                    has_parking = True
        except (ValueError, SyntaxError):
            pass
            
    if 'BikeParking' in attributes and attributes['BikeParking'] == 'True':
        has_parking = True

    if has_parking:
        count += 1

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_function-call-15969302131400067117': [{'business_ref': 'businessref_44'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_6'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_29'}, {'business_ref': 'businessref_81'}, {'business_ref': 'businessref_33'}, {'business_ref': 'businessref_60'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_56'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_10'}, {'business_ref': 'businessref_76'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_18'}, {'business_ref': 'businessref_25'}], 'var_function-call-949915295182459995': ['businessid_44', 'businessid_13', 'businessid_47', 'businessid_6', 'businessid_91', 'businessid_59', 'businessid_29', 'businessid_81', 'businessid_33', 'businessid_60', 'businessid_36', 'businessid_43', 'businessid_56', 'businessid_86', 'businessid_68', 'businessid_45', 'businessid_10', 'businessid_76', 'businessid_28', 'businessid_14', 'businessid_18', 'businessid_25'], 'var_function-call-13209217514639810891': [{'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}, {'business_id': 'businessid_29', 'attributes': {'BikeParking': 'True', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '2', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsDelivery': 'None'}}, {'business_id': 'businessid_10', 'attributes': {'RestaurantsGoodForGroups': 'True', 'RestaurantsDelivery': 'False', 'RestaurantsTakeOut': 'True', 'HasTV': 'True', 'BusinessAcceptsCreditCards': 'True', 'Ambience': "{'touristy': False, 'hipster': False, 'romantic': False, 'divey': False, 'intimate': False, 'trendy': False, 'upscale': False, 'classy': False, 'casual': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}", 'BusinessParking': "{u'valet': False, u'garage': False, u'street': False, u'lot': True, u'validated': False}"}}, {'business_id': 'businessid_59', 'attributes': {'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsTakeOut': 'None', 'RestaurantsDelivery': 'None', 'HasTV': 'True', 'Ambience': "{'touristy': False, 'hipster': None, 'romantic': None, 'divey': None, 'intimate': None, 'trendy': None, 'upscale': False, 'classy': None, 'casual': True}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}"}}]}

exec(code, env_args)
