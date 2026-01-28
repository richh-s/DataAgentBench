code = """import json
import pandas as pd

# Get the result from storage
business_data = locals()['var_functions.query_db:12']

print(f"Number of businesses retrieved: {len(business_data)}")
print(f"Sample data: {business_data[:3]}")

# Function to check if business has parking
import ast

def has_parking(attributes):
    if not attributes:
        return False
    
    # Check BikeParking
    bike_parking = attributes.get('BikeParking')
    if bike_parking == 'True':
        return True
    
    # Check BusinessParking
    business_parking = attributes.get('BusinessParking')
    if business_parking:
        try:
            # Parse the BusinessParking string which looks like a dict
            if isinstance(business_parking, str):
                # Try to parse it as a dict
                parking_dict = ast.literal_eval(business_parking)
                # Check if any parking type is True
                if any(parking_dict.values()):
                    return True
        except:
            # If parsing fails, check if it's a simple True/False
            if business_parking == 'True':
                return True
    
    return False

# Count businesses with parking
businesses_with_parking = []
for business in business_data:
    business_id = business['business_id']
    attributes = business.get('attributes', {})
    
    if has_parking(attributes):
        businesses_with_parking.append(business_id)

print(f"Businesses with parking: {len(businesses_with_parking)}")
print(f"Business IDs: {businesses_with_parking}")

# __RESULT__:
print("__RESULT__:")
print(json.dumps({
    'total_businesses_checked': len(business_data),
    'businesses_with_parking': businesses_with_parking,
    'count': len(businesses_with_parking)
}))"""

env_args = {'var_functions.list_db:0': ['review', 'tip', 'user'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [{'business_ref': 'businessref_6'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_71'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_29'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_44'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_81'}, {'business_ref': 'businessref_33'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_52'}, {'business_ref': 'businessref_89'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_60'}, {'business_ref': 'businessref_12'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_31'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_51'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_72'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_85'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_56'}, {'business_ref': 'businessref_90'}, {'business_ref': 'businessref_97'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_92'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_95'}, {'business_ref': 'businessref_61'}, {'business_ref': 'businessref_49'}, {'business_ref': 'businessref_10'}, {'business_ref': 'businessref_23'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_50'}, {'business_ref': 'businessref_76'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_3'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_69'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_70'}, {'business_ref': 'businessref_18'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_34'}, {'business_ref': 'businessref_21'}, {'business_ref': 'businessref_4'}], 'var_functions.execute_python:10': {'business_refs': ['businessref_6', 'businessref_47', 'businessref_91', 'businessref_71', 'businessref_46', 'businessref_73', 'businessref_25', 'businessref_66', 'businessref_59', 'businessref_29', 'businessref_79', 'businessref_13', 'businessref_44', 'businessref_67', 'businessref_15', 'businessref_81', 'businessref_33', 'businessref_43', 'businessref_17', 'businessref_24', 'businessref_52', 'businessref_89', 'businessref_36', 'businessref_60', 'businessref_12', 'businessref_99', 'businessref_31', 'businessref_80', 'businessref_51', 'businessref_86', 'businessref_8', 'businessref_72', 'businessref_62', 'businessref_85', 'businessref_57', 'businessref_56', 'businessref_90', 'businessref_97', 'businessref_37', 'businessref_40', 'businessref_92', 'businessref_83', 'businessref_95', 'businessref_61', 'businessref_49', 'businessref_10', 'businessref_23', 'businessref_45', 'businessref_82', 'businessref_35', 'businessref_77', 'businessref_50', 'businessref_76', 'businessref_27', 'businessref_3', 'businessref_20', 'businessref_28', 'businessref_22', 'businessref_69', 'businessref_14', 'businessref_70', 'businessref_18', 'businessref_26', 'businessref_68', 'businessref_34', 'businessref_21', 'businessref_4'], 'business_ids': ['6', '47', '91', '71', '46', '73', '25', '66', '59', '29', '79', '13', '44', '67', '15', '81', '33', '43', '17', '24', '52', '89', '36', '60', '12', '99', '31', '80', '51', '86', '8', '72', '62', '85', '57', '56', '90', '97', '37', '40', '92', '83', '95', '61', '49', '10', '23', '45', '82', '35', '77', '50', '76', '27', '3', '20', '28', '22', '69', '14', '70', '18', '26', '68', '34', '21', '4']}, 'var_functions.query_db:12': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'True', 'NoiseLevel': "u'quiet'", 'WiFi': "u'no'"}}, {'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'BikeParking': 'True'}}]}

exec(code, env_args)
