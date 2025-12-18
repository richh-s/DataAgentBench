code = """import pandas as pd
import json

businesses_data = locals()['var_function-call-8642277954975931809']
credit_card_businesses = []

for biz in businesses_data:
    business_id = biz.get('business_id')
    attributes = biz.get('attributes', {})
    if 'categories' in attributes:
        categories_str = attributes['categories']
        # Categories are often a comma-separated string, sometimes with 'u'' prefix from MongoDB.
        # Clean up the string and split into a list.
        categories = [c.strip().replace("u'", "") for c in categories_str.split(',') if c.strip()]
        for category in categories:
            credit_card_businesses.append({'business_id': business_id, 'category': category})
    elif 'description' in biz and 'categories' in biz['description']:
        # Fallback to description if categories are not in attributes
        # Assuming categories in description are also comma-separated
        description_categories_str = biz['description']['categories']
        categories = [c.strip().replace("u'", "") for c in description_categories_str.split(',') if c.strip()]
        for category in categories:
            credit_card_businesses.append({'business_id': business_id, 'category': category})


credit_card_df = pd.DataFrame(credit_card_businesses)
print("__RESULT__:")
print(credit_card_df.to_json(orient='records'))"""

env_args = {'var_function-call-15794123019526283746': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {}}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {}}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'attributes': {}}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'attributes': {}}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'attributes': {}}], 'var_function-call-8642277954975931809': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'True', 'NoiseLevel': "u'quiet'", 'WiFi': "u'no'"}}]}

exec(code, env_args)
