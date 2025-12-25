code = """import json
import pandas as pd

business_data = locals()['var_function-call-14774226153059884967']['results']

credit_card_businesses = []
for business in business_data:
    attributes = business.get('attributes')
    if attributes and isinstance(attributes, dict):
        if attributes.get('BusinessAcceptsCreditCards') == 'True':
            credit_card_businesses.append({
                'business_id': business['business_id'],
                'description': business['description']
            })

credit_card_businesses_df = pd.DataFrame(credit_card_businesses)

def extract_categories(description):
    if 'services in' in description:
        start_index = description.find('services in') + len('services in')
    elif 'services, including' in description:
        start_index = description.find('services, including') + len('services, including')
    else:
        return []
    
    categories_str = description[start_index:].strip().split('.')[0]
    categories = [cat.strip() for cat in categories_str.split(',')]
    return categories

credit_card_businesses_df['categories'] = credit_card_businesses_df['description'].apply(extract_categories)


business_categories = credit_card_businesses_df.explode('categories')
business_categories['business_id_cleaned'] = business_categories['business_id'].apply(lambda x: x.replace('businessid_', ''))

print('__RESULT__:')
print(business_categories.to_json(orient='records'))"""

env_args = {'var_function-call-3971061945851831954': ['checkin', 'business'], 'var_function-call-14774226153059884967': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'attributes': 'None', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
