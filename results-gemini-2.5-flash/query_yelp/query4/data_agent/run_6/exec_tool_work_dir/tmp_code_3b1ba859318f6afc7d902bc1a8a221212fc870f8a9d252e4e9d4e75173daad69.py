code = """import pandas as pd
import json

df_businesses = pd.DataFrame(json.loads(locals()['var_function-call-3945483735470021639']))

def extract_categories(description):
    if isinstance(description, str):
        start_phrases = [
            "providing a range of services in ",
            "offers a range of services including ",
            "offers a wide range of services, including ",
            "offers a diverse range of services and products in the fields of ",
            "offers a premier destination for "
        ]
        for phrase in start_phrases:
            if phrase in description:
                categories_str = description.split(phrase, 1)[1]
                return [cat.strip() for cat in categories_str.replace('.', '').split(',')] # remove periods and split by comma
    return []

df_businesses['categories'] = df_businesses['description'].apply(extract_categories)

business_categories = []
for _, row in df_businesses.iterrows():
    for category in row['categories']:
        business_categories.append({'business_id': row['business_id'], 'category': category})

df_business_categories = pd.DataFrame(business_categories)

category_counts = df_business_categories['category'].value_counts().reset_index()
category_counts.columns = ['category', 'business_count']

most_common_category = category_counts.loc[category_counts['business_count'].idxmax()]

result = {'most_common_category': most_common_category['category'], 'business_count': most_common_category['business_count'], 'business_ids': df_business_categories[df_business_categories['category'] == most_common_category['category']]['business_id'].tolist()}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-14538774891075137081': ['checkin', 'business'], 'var_function-call-1127616868687047460': [], 'var_function-call-18220773453091609842': [{'_id': '6859a000fe8b31cd7362e2ab', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'_id': '6859a000fe8b31cd7362e2ac', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2ad', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'_id': '6859a000fe8b31cd7362e2ae', 'attributes': 'None'}, {'_id': '6859a000fe8b31cd7362e2af', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}, {'_id': '6859a000fe8b31cd7362e2b0', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '4', 'BikeParking': 'False'}}, {'_id': '6859a000fe8b31cd7362e2b1', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'True', 'NoiseLevel': "u'quiet'", 'WiFi': "u'no'"}}, {'_id': '6859a000fe8b31cd7362e2b2', 'attributes': {'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': True, 'valet': False}", 'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'True', 'WiFi': "u'free'"}}, {'_id': '6859a000fe8b31cd7362e2b3', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'BikeParking': 'True'}}, {'_id': '6859a000fe8b31cd7362e2b4', 'attributes': {'BikeParking': 'True', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '2', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsDelivery': 'None'}}], 'var_function-call-3945483735470021639': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}]}

exec(code, env_args)
