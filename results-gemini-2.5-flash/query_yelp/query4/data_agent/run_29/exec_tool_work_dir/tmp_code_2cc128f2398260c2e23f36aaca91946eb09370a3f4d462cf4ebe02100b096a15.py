code = """import json
import pandas as pd

# Correctly parse the business data
business_data_raw_string = locals()['var_function-call-484881266664202551']['results'][0]
start_idx = business_data_raw_string.find('[')
end_idx = business_data_raw_string.rfind(']')
json_string = business_data_raw_string[start_idx : end_idx + 1]
business_data = json.loads(json_string)
credit_card_businesses_df = pd.DataFrame(business_data)

# Extract categories
def extract_categories(description):
    if 'services in' in description:
        start_index = description.find('services in') + len('services in')
    elif 'services, including' in description:
        start_index = description.find('services, including') + len('services, including')
    else:
        return []
    
    categories_str = description[start_index:].strip().split('.')[0]
    categories = [cat.strip() for cat in categories_str.split(',') if cat.strip()]
    return categories

credit_card_businesses_df['categories'] = credit_card_businesses_df['description'].apply(extract_categories)
business_categories = credit_card_businesses_df.explode('categories')
business_categories['business_id_cleaned'] = business_categories['business_id'].apply(lambda x: x.replace('businessid_', ''))

# Load and clean review data
with open(locals()['var_function-call-14738479038160461792'], 'r') as f:
    review_data = json.load(f)
review_df = pd.DataFrame(review_data)
review_df['business_ref_cleaned'] = review_df['business_ref'].apply(lambda x: x.replace('businessref_', ''))
review_df['rating'] = pd.to_numeric(review_df['rating'])

# Merge dataframes
merged_df = pd.merge(business_categories, review_df, left_on='business_id_cleaned', right_on='business_ref_cleaned', how='inner')

# Group and aggregate
category_stats = merged_df.groupby('categories').agg(
    num_businesses=('business_id_cleaned', 'nunique'),
    average_rating=('rating', 'mean')
).reset_index()

# Find the category with the largest number of businesses
largest_category = category_stats.loc[category_stats['num_businesses'].idxmax()]

result = {
    'category': largest_category['categories'],
    'num_businesses': largest_category['num_businesses'],
    'average_rating': largest_category['average_rating']
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-3971061945851831954': ['checkin', 'business'], 'var_function-call-14774226153059884967': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'attributes': 'None', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-12964448864886771801': ['review', 'tip', 'user'], 'var_function-call-484881266664202551': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_function-call-14738479038160461792': 'file_storage/function-call-14738479038160461792.json'}

exec(code, env_args)
