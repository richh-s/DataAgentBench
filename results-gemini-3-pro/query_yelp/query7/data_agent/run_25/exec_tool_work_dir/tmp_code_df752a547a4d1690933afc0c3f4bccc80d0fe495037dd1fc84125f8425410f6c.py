code = """import json
import re
from collections import defaultdict

# Load SQL result
sql_res = locals()['var_function-call-15186839526067618743']
ref_to_count = {}
for row in sql_res:
    ref = row['business_ref']
    count = int(row['count'])
    bid = ref.replace('businessref_', 'businessid_')
    ref_to_count[bid] = count

# Load Mongo result from file
mongo_file_path = locals()['var_function-call-11097870204815074633']
with open(mongo_file_path, 'r') as f:
    mongo_res = json.load(f)

# Markers
markers = [
    "including ",
    "destination for ",
    "services in ",
    "seeking ",
    "selection of ", 
    "offering ",
    "in the fields of ",
    "category of "
]

category_stats = defaultdict(int)

for doc in mongo_res:
    bid = doc.get('business_id')
    desc = doc.get('description', '')
    if not bid or not desc:
        continue
    
    # Only process if in our count list
    if bid not in ref_to_count:
        continue
        
    count = ref_to_count[bid]
    
    # Clean desc
    clean_desc = desc.strip()
    if clean_desc.endswith('.'):
        clean_desc = clean_desc[:-1]
    
    # Find marker
    best_marker_pos = -1
    best_marker_len = 0
    
    for m in markers:
        idx = clean_desc.rfind(m)
        if idx != -1:
            if idx > best_marker_pos:
                best_marker_pos = idx
                best_marker_len = len(m)
                
    if best_marker_pos != -1:
        cat_str = clean_desc[best_marker_pos + best_marker_len:]
        
        # Remove quotes if present (e.g. 'Restaurants, Chinese')
        cat_str = cat_str.replace("'", "").replace('"', "")
        
        # Split
        cats = [c.strip() for c in cat_str.split(',')]
        clean_cats = []
        for i, c in enumerate(cats):
            if i == len(cats) - 1:
                if c.startswith('and '):
                    c = c[4:]
            c = c.strip()
            if c:
                clean_cats.append(c)
        
        for cat in clean_cats:
            category_stats[cat] += count

# Sort
top_cats = sorted(category_stats.items(), key=lambda x: x[1], reverse=True)

print("__RESULT__:")
print(json.dumps(top_cats[:10]))"""

env_args = {'var_function-call-3891137707094233373': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-1343556735504055917': [{'user_id': 'userid_286', 'name': 'Todd', 'review_count': '376', 'yelping_since': '15 Jan 2009, 16:40', 'useful': '1373', 'funny': '723', 'cool': '639', 'elite': '2010,2011,2012,2013,2014'}], 'var_function-call-8066950819881996006': [{'date': 'August 01, 2016 at 03:44 AM'}], 'var_function-call-15186839526067618743': [{'business_ref': 'businessref_79', 'count': '8'}, {'business_ref': 'businessref_44', 'count': '4'}, {'business_ref': 'businessref_13', 'count': '3'}, {'business_ref': 'businessref_36', 'count': '3'}, {'business_ref': 'businessref_12', 'count': '4'}, {'business_ref': 'businessref_60', 'count': '4'}, {'business_ref': 'businessref_89', 'count': '3'}, {'business_ref': 'businessref_6', 'count': '4'}, {'business_ref': 'businessref_71', 'count': '1'}, {'business_ref': 'businessref_91', 'count': '2'}, {'business_ref': 'businessref_46', 'count': '1'}, {'business_ref': 'businessref_1', 'count': '1'}, {'business_ref': 'businessref_47', 'count': '1'}, {'business_ref': 'businessref_16', 'count': '1'}, {'business_ref': 'businessref_55', 'count': '1'}, {'business_ref': 'businessref_17', 'count': '1'}, {'business_ref': 'businessref_43', 'count': '3'}, {'business_ref': 'businessref_53', 'count': '1'}, {'business_ref': 'businessref_51', 'count': '3'}, {'business_ref': 'businessref_31', 'count': '1'}, {'business_ref': 'businessref_99', 'count': '1'}, {'business_ref': 'businessref_37', 'count': '6'}, {'business_ref': 'businessref_57', 'count': '7'}, {'business_ref': 'businessref_8', 'count': '4'}, {'business_ref': 'businessref_56', 'count': '1'}, {'business_ref': 'businessref_62', 'count': '2'}, {'business_ref': 'businessref_86', 'count': '4'}, {'business_ref': 'businessref_97', 'count': '1'}, {'business_ref': 'businessref_72', 'count': '1'}, {'business_ref': 'businessref_85', 'count': '1'}, {'business_ref': 'businessref_42', 'count': '1'}, {'business_ref': 'businessref_40', 'count': '3'}, {'business_ref': 'businessref_7', 'count': '2'}, {'business_ref': 'businessref_92', 'count': '2'}, {'business_ref': 'businessref_61', 'count': '1'}, {'business_ref': 'businessref_88', 'count': '4'}, {'business_ref': 'businessref_21', 'count': '4'}, {'business_ref': 'businessref_26', 'count': '4'}, {'business_ref': 'businessref_68', 'count': '1'}, {'business_ref': 'businessref_4', 'count': '1'}, {'business_ref': 'businessref_23', 'count': '1'}, {'business_ref': 'businessref_41', 'count': '1'}, {'business_ref': 'businessref_10', 'count': '1'}, {'business_ref': 'businessref_45', 'count': '5'}, {'business_ref': 'businessref_82', 'count': '2'}, {'business_ref': 'businessref_76', 'count': '1'}, {'business_ref': 'businessref_14', 'count': '3'}, {'business_ref': 'businessref_3', 'count': '2'}, {'business_ref': 'businessref_96', 'count': '4'}, {'business_ref': 'businessref_98', 'count': '3'}, {'business_ref': 'businessref_22', 'count': '1'}, {'business_ref': 'businessref_20', 'count': '1'}, {'business_ref': 'businessref_67', 'count': '5'}, {'business_ref': 'businessref_15', 'count': '3'}, {'business_ref': 'businessref_33', 'count': '5'}, {'business_ref': 'businessref_81', 'count': '1'}, {'business_ref': 'businessref_9', 'count': '3'}, {'business_ref': 'businessref_74', 'count': '2'}, {'business_ref': 'businessref_25', 'count': '1'}, {'business_ref': 'businessref_66', 'count': '2'}, {'business_ref': 'businessref_29', 'count': '1'}, {'business_ref': 'businessref_39', 'count': '1'}], 'var_function-call-4838191203870289089': ['businessid_79', 'businessid_44', 'businessid_13', 'businessid_36', 'businessid_12', 'businessid_60', 'businessid_89', 'businessid_6', 'businessid_71', 'businessid_91', 'businessid_46', 'businessid_1', 'businessid_47', 'businessid_16', 'businessid_55', 'businessid_17', 'businessid_43', 'businessid_53', 'businessid_51', 'businessid_31', 'businessid_99', 'businessid_37', 'businessid_57', 'businessid_8', 'businessid_56', 'businessid_62', 'businessid_86', 'businessid_97', 'businessid_72', 'businessid_85', 'businessid_42', 'businessid_40', 'businessid_7', 'businessid_92', 'businessid_61', 'businessid_88', 'businessid_21', 'businessid_26', 'businessid_68', 'businessid_4', 'businessid_23', 'businessid_41', 'businessid_10', 'businessid_45', 'businessid_82', 'businessid_76', 'businessid_14', 'businessid_3', 'businessid_96', 'businessid_98', 'businessid_22', 'businessid_20', 'businessid_67', 'businessid_15', 'businessid_33', 'businessid_81', 'businessid_9', 'businessid_74', 'businessid_25', 'businessid_66', 'businessid_29', 'businessid_39'], 'var_function-call-2917400293631955427': [{'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}], 'var_function-call-9955137736692533419': [['Beauty & Spas', 6], ['Nail Salons', 5], ['Hair Removal', 5], ['Waxing', 5], ['Gun/Rifle Ranges', 4], ['Active Life', 4], ['Candy Stores', 2], ['Specialty Food', 2], ['Food', 2], ['Hair Salons', 1]], 'var_function-call-1314043831015204111': 5, 'var_function-call-13751158235908471675': [{'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'name': 'Candy Barrel', 'review_count': '7', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '4', 'BikeParking': 'False'}, 'hours': 'None', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}], 'var_function-call-5655619489006702013': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-11097870204815074633': 'file_storage/function-call-11097870204815074633.json'}

exec(code, env_args)
