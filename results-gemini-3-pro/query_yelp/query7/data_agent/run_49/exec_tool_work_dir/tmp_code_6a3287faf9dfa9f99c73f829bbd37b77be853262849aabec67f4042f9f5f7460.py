code = """import json
import collections

# Load the SQL result (business_ref, review_count)
sql_results = locals()['var_function-call-15326417403435364251']

# Load the Mongo result (business_id, description)
file_path = locals()['var_function-call-17537099463024753879']
with open(file_path, 'r') as f:
    businesses = json.load(f)

business_dict = {b['business_id']: b['description'] for b in businesses}

# Markers for extraction
markers = [
    " including ", 
    " services in ", 
    " products in the fields of ",
    " products in categories such as ",
    " category of ",
    " categories of ",
    " categories including ",
    " destination for ", 
    " offerings within the ",
]

def extract_categories(desc):
    last_marker = None
    max_index = -1
    
    for m in markers:
        idx = desc.rfind(m)
        if idx > max_index:
            max_index = idx
            last_marker = m
            
    cats = []
    if max_index != -1:
        cats_str = desc[max_index + len(last_marker):]
        if cats_str.endswith('.'):
            cats_str = cats_str[:-1]
        
        raw_cats = [c.strip() for c in cats_str.split(',')]
        
        for i, c in enumerate(raw_cats):
            if i == len(raw_cats) - 1:
                if c.lower().startswith('and '):
                    c = c[4:].strip()
                if c.lower().endswith(' categories'):
                    c = c[:-11].strip()
                elif c.lower().endswith(' category'):
                    c = c[:-9].strip()
            
            # Normalize
            c = c.title()
            
            if len(c) > 2:
                cats.append(c)
    
    return cats

category_counts = collections.defaultdict(int)

for row in sql_results:
    b_ref = row['business_ref']
    # Ensure review_count is int
    count = int(row['review_count'])
    
    if b_ref.startswith('businessref_'):
        b_id = 'businessid_' + b_ref.split('_')[1]
    else:
        continue
        
    if b_id in business_dict:
        desc = business_dict[b_id]
        cats = extract_categories(desc)
        
        for c in cats:
            category_counts[c] += count

sorted_cats = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)
top_5 = sorted_cats[:5]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-5698163021041009861': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-1905680649121532952': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-15469961143952026078': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-15326417403435364251': [{'business_ref': 'businessref_79', 'review_count': '8'}, {'business_ref': 'businessref_57', 'review_count': '7'}, {'business_ref': 'businessref_37', 'review_count': '6'}, {'business_ref': 'businessref_67', 'review_count': '5'}, {'business_ref': 'businessref_33', 'review_count': '5'}, {'business_ref': 'businessref_45', 'review_count': '5'}, {'business_ref': 'businessref_88', 'review_count': '4'}, {'business_ref': 'businessref_21', 'review_count': '4'}, {'business_ref': 'businessref_26', 'review_count': '4'}, {'business_ref': 'businessref_44', 'review_count': '4'}, {'business_ref': 'businessref_6', 'review_count': '4'}, {'business_ref': 'businessref_12', 'review_count': '4'}, {'business_ref': 'businessref_60', 'review_count': '4'}, {'business_ref': 'businessref_8', 'review_count': '4'}, {'business_ref': 'businessref_86', 'review_count': '4'}, {'business_ref': 'businessref_96', 'review_count': '4'}, {'business_ref': 'businessref_13', 'review_count': '3'}, {'business_ref': 'businessref_9', 'review_count': '3'}, {'business_ref': 'businessref_15', 'review_count': '3'}, {'business_ref': 'businessref_36', 'review_count': '3'}, {'business_ref': 'businessref_89', 'review_count': '3'}, {'business_ref': 'businessref_43', 'review_count': '3'}, {'business_ref': 'businessref_51', 'review_count': '3'}, {'business_ref': 'businessref_40', 'review_count': '3'}, {'business_ref': 'businessref_14', 'review_count': '3'}, {'business_ref': 'businessref_98', 'review_count': '3'}, {'business_ref': 'businessref_91', 'review_count': '2'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_62', 'review_count': '2'}, {'business_ref': 'businessref_7', 'review_count': '2'}, {'business_ref': 'businessref_92', 'review_count': '2'}, {'business_ref': 'businessref_82', 'review_count': '2'}, {'business_ref': 'businessref_3', 'review_count': '2'}, {'business_ref': 'businessref_71', 'review_count': '1'}, {'business_ref': 'businessref_46', 'review_count': '1'}, {'business_ref': 'businessref_1', 'review_count': '1'}, {'business_ref': 'businessref_47', 'review_count': '1'}, {'business_ref': 'businessref_16', 'review_count': '1'}, {'business_ref': 'businessref_55', 'review_count': '1'}, {'business_ref': 'businessref_25', 'review_count': '1'}, {'business_ref': 'businessref_81', 'review_count': '1'}, {'business_ref': 'businessref_17', 'review_count': '1'}, {'business_ref': 'businessref_31', 'review_count': '1'}, {'business_ref': 'businessref_99', 'review_count': '1'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_56', 'review_count': '1'}, {'business_ref': 'businessref_97', 'review_count': '1'}, {'business_ref': 'businessref_72', 'review_count': '1'}, {'business_ref': 'businessref_85', 'review_count': '1'}, {'business_ref': 'businessref_42', 'review_count': '1'}, {'business_ref': 'businessref_61', 'review_count': '1'}, {'business_ref': 'businessref_23', 'review_count': '1'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}, {'business_ref': 'businessref_29', 'review_count': '1'}, {'business_ref': 'businessref_39', 'review_count': '1'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_4', 'review_count': '1'}, {'business_ref': 'businessref_76', 'review_count': '1'}, {'business_ref': 'businessref_22', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}], 'var_function-call-8104407225367862777': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-3049709378688433688': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-17537099463024753879': 'file_storage/function-call-17537099463024753879.json', 'var_function-call-6449824825237537072': [{'bid': 'businessid_57', 'desc': 'Located at 13605 W Hillsborough Ave in Tampa, FL, this versatile establishment offers a range of services and dining options, including Movers, American (New), Landscape Architects, Food, Home Services, Self Storage, Local Services, Restaurants.', 'cats': ['Movers', 'American (New)', 'Landscape Architects', 'Food', 'Home Services', 'Self Storage', 'Local Services', 'Restaurants']}, {'bid': 'businessid_93', 'desc': 'Located at 914 Edwardsville Rd in Troy, IL, this vibrant spot offers a diverse menu featuring American (New) cuisine, along with a lively atmosphere perfect for nightlife, bars, restaurants, and sports bars.', 'cats': ['nightlife', 'bars', 'restaurants', 'sports bars']}, {'bid': 'businessid_70', 'desc': 'Located at 4500 Shores Dr, Ste 2 in Metairie, LA, this business specializes in a range of offerings within the Home Services, Plumbing categories.', 'cats': ['Home Services', 'Plumbing categories']}, {'bid': 'businessid_29', 'desc': 'Located at 41 Haddon Ave in Collingswood, NJ, this versatile establishment offers a range of services including Wedding Planning, Flowers & Gifts, Event Planning & Services, Financial Services, Shopping, and Florists.', 'cats': ['Wedding Planning', 'Flowers & Gifts', 'Event Planning & Services', 'Financial Services', 'Shopping', 'Florists']}, {'bid': 'businessid_49', 'desc': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.', 'cats': ['Education', 'Elementary Schools', 'Child Care & Day Care', 'Local Services', 'Preschools', 'Montessori Schools']}]}

exec(code, env_args)
