code = """import json, re
from collections import defaultdict

# Get business data from file
business_file = locals()['var_functions.query_db:38']
business_data = json.load(open(business_file, 'r'))

print('Total businesses loaded:', len(business_data))

# Extract categories from description
def get_categories(description):
    if not description:
        return ['Miscellaneous']
    
    # Find main category phrase in description
    desc_lower = description.lower()
    
    # Look for patterns like "in [X, Y, Z]" or "offers X, Y, Z"
    if 'services in' in desc_lower:
        match = re.search(r'services in ([^\.\,]+)', desc_lower)
        if match:
            items = match.group(1).split(',')
            return [item.strip().title() for item in items if item.strip()]
    
    if 'offers a range of' in desc_lower:
        match = re.search(r'offers a range of ([^\.\,]+)', desc_lower)
        if match:
            items = re.split(r',\s*|\sand\s', match.group(1))
            return [item.strip().title() for item in items if item.strip()]
    
    if 'offers a' in desc_lower and 'array' in desc_lower:
        match = re.search(r'offers a [\w\s]+ array of ([^\.\,]+)', desc_lower)
        if match:
            items = re.split(r',\s*|\sand\s', match.group(1))
            return [item.strip().title() for item in items if item.strip()]
    
    if 'category' in desc_lower:
        match = re.search(r"category of '([^']+)'", desc_lower)
        if match:
            return [match.group(1).title()]
    
    return ['Miscellaneous']

# Process businesses
category_count = defaultdict(int)
accepted_cc = []

for business in business_data:
    attrs = business.get('attributes', {})
    if attrs and isinstance(attrs, dict) and attrs.get('BusinessAcceptsCreditCards') == 'True':
        accepted_cc.append(business['business_id'])
        desc = business.get('description', '') or ''
        categories = get_categories(desc)
        for cat in categories:
            category_count[cat] += 1

# Find top category
top = max(category_count.items(), key=lambda x: x[1]) if category_count else (None, 0)
print('Top category:', top)
print('Total CC businesses:', len(accepted_cc))

result = {
    'total_cc_businesses': len(accepted_cc),
    'top_category': top[0],
    'top_category_count': top[1],
    'sample': dict(list(category_count.items())[:10])
}
print('Sample categories:', result['sample'])
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['checkin', 'business'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['review', 'tip', 'user'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:24': {'count': 100, 'first_keys': ['business_id', 'name', 'attributes', 'description']}, 'var_functions.query_db:26': [{'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'attributes': 'None', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.query_db:28': [{'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'name': 'Impact Guns', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'attributes': 'None', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'name': 'J&Q Nails', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.execute_python:36': {'type': "<class 'list'>", 'is_list': True, 'length': 5, 'first_item_keys': ['business_id', 'name', 'attributes', 'description']}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:40': {'total_cc_businesses': 75, 'top_category': 'Miscellaneous', 'top_category_count': 27, 'business_ids_in_top': ['businessid_92', 'businessid_54', 'businessid_93', 'businessid_95', 'businessid_32', 'businessid_27', 'businessid_2', 'businessid_48', 'businessid_76', 'businessid_63', 'businessid_87', 'businessid_55', 'businessid_96', 'businessid_65', 'businessid_86', 'businessid_53', 'businessid_43', 'businessid_9', 'businessid_20', 'businessid_62', 'businessid_94', 'businessid_90', 'businessid_85', 'businessid_21', 'businessid_16', 'businessid_46', 'businessid_13'], 'all_category_counts': {'Education': 1, 'Services': 3, 'Gun/Rifle Ranges': 1, 'Services Including Nail Salons': 1, 'Miscellaneous': 27, 'Nail Salons': 1, 'Antiques': 1, 'Services Including Wedding Planning': 1, 'Restaurants': 3, 'Chinese': 1, 'The Categories Of Medical Centers': 1, 'Services Including Hotels & Travel': 1, 'Options Ranging From Food': 1, 'Optometrists': 1, 'Food': 1, 'A Variety Of Offerings': 1, 'Products In Categories Such As Books': 1, 'Services Including Dry Cleaning & Laundry': 1, 'Automotive': 2, 'Body Shops': 1, 'Products Across Various Categories': 1, 'Services Including Contractors': 1, 'The Categories Of Home & Garden': 1, 'Vietnamese': 1, 'Solutions Including Home Services': 1, 'The Categories Of Food': 1, 'The Categories Of Beauty & Spas': 1, 'Fast Food': 1, 'Products': 2, 'Cosmetic Dentists': 1, 'Home Services': 1, 'Health & Medical': 1, 'Hotels & Travel': 1, 'Products In Categories Such As Home Decor': 1, 'Venues & Event Spaces': 1, 'Options': 2, 'Fitness & Instruction': 1, 'Automotive Services': 1, 'Options In The Categories Of Food': 1, 'Options For Customers': 1, 'Real Estate': 1, 'The Field Of Doctors': 1, 'Hair Salons': 1, 'Services Including Barbers': 1, 'Shopping': 1}}, 'var_functions.query_db:42': [{'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'name': 'Impact Guns', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'attributes': 'None', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'name': 'J&Q Nails', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.query_db:46': [{'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'name': 'Impact Guns', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'attributes': 'None', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'name': 'J&Q Nails', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
