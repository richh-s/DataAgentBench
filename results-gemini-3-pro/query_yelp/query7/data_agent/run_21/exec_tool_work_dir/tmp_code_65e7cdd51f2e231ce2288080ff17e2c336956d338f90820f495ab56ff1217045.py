code = """import json

# Load SQL result
sql_result = locals()['var_function-call-16624978320130190117']
# Map business_id -> review_count
# Note: SQL result has 'business_ref' (e.g. businessref_1), Mongo has 'business_id' (e.g. businessid_1)
business_counts = {}
for row in sql_result:
    bid = row['business_ref'].replace('businessref_', 'businessid_')
    # ensure review_count is int
    count = int(row['review_count'])
    business_counts[bid] = count

# Load Mongo result from file
mongo_file_path = locals()['var_function-call-6573041892300133864']
with open(mongo_file_path, 'r') as f:
    mongo_docs = json.load(f)

categories_total = {}

for doc in mongo_docs:
    bid = doc['business_id']
    if bid not in business_counts:
        continue
    
    count = business_counts[bid]
    desc = doc.get('description', '')
    if not desc:
        continue
        
    # Extract categories
    # Common patterns:
    # "services in [A, B, C]."
    # "services including [A, B, C]."
    # "including [A, B, C]."
    # "destination for [A, B, C]."
    # "categories of [A, B, C]." (seen in one example: "categories of 'Restaurants, Chinese'")
    # "category of 'Restaurants, Chinese'."
    
    cats_str = ""
    
    # Try specific markers
    markers = [
        "services in the categories of ",
        "services in the category of ",
        "services in ",
        "services including ",
        "including ",
        "destination for ",
        "categories of "
    ]
    
    # We want to find the marker that appears latest in the string? 
    # Or just try them in order. The descriptions seem to use one main phrase near the end.
    
    found_cats = None
    
    # Check for quotes like "'Restaurants, Chinese'"
    if "'" in desc:
        parts = desc.split("'")
        # likely the categories are inside quotes if the text says "category of '...'"
        # Search for a part that looks like a list
        for p in parts:
            if ',' in p or (p[0].isupper() and len(p) > 3): 
                # Heuristic: categories often capitalized and separated by commas
                # But 'Restaurants, Chinese' is a good hint.
                # Let's verify if "category of" is present.
                pass
    
    # Let's try splitting by the markers
    for marker in markers:
        if marker in desc:
            # Take the part after the marker
            temp = desc.split(marker)[-1]
            # If there are multiple markers, this might get the last part which is good.
            # But "including" might be part of "services including".
            # "services in" is safer than "including" if both exist?
            # Actually, just taking the last split is usually correct if the sentence ends with categories.
            cats_str = temp
            break # Found a marker?
            # Wait, "services in" matches "services in the categories of".
            # So I should order markers by length (longest first) to match the most specific one.
    
    # Re-order markers by length descending
    markers.sort(key=len, reverse=True)
    
    for marker in markers:
        if marker in desc:
            cats_str = desc.split(marker)[-1]
            break
            
    if cats_str:
        # cleanup
        cats_str = cats_str.strip()
        if cats_str.endswith('.'):
            cats_str = cats_str[:-1]
        
        # specific cleanup for quotes if present, e.g. 'Restaurants, Chinese'
        if cats_str.startswith("'") and cats_str.endswith("'"):
            cats_str = cats_str[1:-1]
        
        # Split
        cats = [c.strip() for c in cats_str.split(',')]
        
        for c in cats:
            # Clean "and X"
            if c.lower().startswith('and '):
                c = c[4:]
            
            # Additional cleanup
            c = c.strip()
            
            if c:
                categories_total[c] = categories_total.get(c, 0) + count

# Sort top 5
top_cats = sorted(categories_total.items(), key=lambda x: x[1], reverse=True)[:5]
print("__RESULT__:")
print(json.dumps(top_cats))"""

env_args = {'var_function-call-1926116299167403223': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-8817279312995942582': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-3835436407834537059': [{'yelping_since': '15 Jan 2009, 16:40'}, {'yelping_since': '13 Jul 2010, 15:42'}, {'yelping_since': '2010-09-07 23:24:36'}, {'yelping_since': 'October 23, 2011 at 07:47 PM'}, {'yelping_since': '2011-08-30 13:46:26'}], 'var_function-call-8705705535669765239': [{'date': 'August 01, 2016 at 03:44 AM'}, {'date': 'June 14, 2021 at 11:39 AM'}, {'date': '29 May 2013, 23:01'}, {'date': '21 May 2016, 18:48'}, {'date': 'November 01, 2021 at 05:11 PM'}], 'var_function-call-16624978320130190117': [{'business_ref': 'businessref_79', 'review_count': '8'}, {'business_ref': 'businessref_44', 'review_count': '4'}, {'business_ref': 'businessref_13', 'review_count': '3'}, {'business_ref': 'businessref_9', 'review_count': '3'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_25', 'review_count': '1'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_29', 'review_count': '1'}, {'business_ref': 'businessref_39', 'review_count': '1'}, {'business_ref': 'businessref_67', 'review_count': '5'}, {'business_ref': 'businessref_15', 'review_count': '3'}, {'business_ref': 'businessref_33', 'review_count': '5'}, {'business_ref': 'businessref_81', 'review_count': '1'}, {'business_ref': 'businessref_36', 'review_count': '3'}, {'business_ref': 'businessref_12', 'review_count': '4'}, {'business_ref': 'businessref_60', 'review_count': '4'}, {'business_ref': 'businessref_89', 'review_count': '3'}, {'business_ref': 'businessref_6', 'review_count': '4'}, {'business_ref': 'businessref_71', 'review_count': '1'}, {'business_ref': 'businessref_91', 'review_count': '2'}, {'business_ref': 'businessref_46', 'review_count': '1'}, {'business_ref': 'businessref_1', 'review_count': '1'}, {'business_ref': 'businessref_47', 'review_count': '1'}, {'business_ref': 'businessref_16', 'review_count': '1'}, {'business_ref': 'businessref_55', 'review_count': '1'}, {'business_ref': 'businessref_17', 'review_count': '1'}, {'business_ref': 'businessref_43', 'review_count': '3'}, {'business_ref': 'businessref_31', 'review_count': '1'}, {'business_ref': 'businessref_99', 'review_count': '1'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_51', 'review_count': '3'}, {'business_ref': 'businessref_37', 'review_count': '6'}, {'business_ref': 'businessref_57', 'review_count': '7'}, {'business_ref': 'businessref_8', 'review_count': '4'}, {'business_ref': 'businessref_56', 'review_count': '1'}, {'business_ref': 'businessref_62', 'review_count': '2'}, {'business_ref': 'businessref_86', 'review_count': '4'}, {'business_ref': 'businessref_97', 'review_count': '1'}, {'business_ref': 'businessref_72', 'review_count': '1'}, {'business_ref': 'businessref_85', 'review_count': '1'}, {'business_ref': 'businessref_42', 'review_count': '1'}, {'business_ref': 'businessref_40', 'review_count': '3'}, {'business_ref': 'businessref_7', 'review_count': '2'}, {'business_ref': 'businessref_92', 'review_count': '2'}, {'business_ref': 'businessref_61', 'review_count': '1'}, {'business_ref': 'businessref_23', 'review_count': '1'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}, {'business_ref': 'businessref_45', 'review_count': '5'}, {'business_ref': 'businessref_82', 'review_count': '2'}, {'business_ref': 'businessref_76', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '3'}, {'business_ref': 'businessref_3', 'review_count': '2'}, {'business_ref': 'businessref_96', 'review_count': '4'}, {'business_ref': 'businessref_98', 'review_count': '3'}, {'business_ref': 'businessref_22', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}, {'business_ref': 'businessref_88', 'review_count': '4'}, {'business_ref': 'businessref_21', 'review_count': '4'}, {'business_ref': 'businessref_26', 'review_count': '4'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_4', 'review_count': '1'}], 'var_function-call-420097590862934078': {'collection': 'business', 'filter': {'business_id': {'$in': ['businessid_79', 'businessid_44', 'businessid_13', 'businessid_9', 'businessid_74', 'businessid_25', 'businessid_66', 'businessid_29', 'businessid_39', 'businessid_67', 'businessid_15', 'businessid_33', 'businessid_81', 'businessid_36', 'businessid_12', 'businessid_60', 'businessid_89', 'businessid_6', 'businessid_71', 'businessid_91', 'businessid_46', 'businessid_1', 'businessid_47', 'businessid_16', 'businessid_55', 'businessid_17', 'businessid_43', 'businessid_31', 'businessid_99', 'businessid_53', 'businessid_51', 'businessid_37', 'businessid_57', 'businessid_8', 'businessid_56', 'businessid_62', 'businessid_86', 'businessid_97', 'businessid_72', 'businessid_85', 'businessid_42', 'businessid_40', 'businessid_7', 'businessid_92', 'businessid_61', 'businessid_23', 'businessid_41', 'businessid_10', 'businessid_45', 'businessid_82', 'businessid_76', 'businessid_14', 'businessid_3', 'businessid_96', 'businessid_98', 'businessid_22', 'businessid_20', 'businessid_88', 'businessid_21', 'businessid_26', 'businessid_68', 'businessid_4']}}, 'projection': {'business_id': 1, 'description': 1}}, 'var_function-call-16525585691167775123': [{'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}], 'var_function-call-217928265536561876': [{'_id': '6859a000fe8b31cd7362e2e0', 'business_id': 'businessid_79', 'name': 'Pit Stop HQ', 'review_count': '65', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '6:30-19:0', 'Tuesday': '6:30-19:0', 'Wednesday': '6:30-19:0', 'Thursday': '6:30-19:0', 'Friday': '6:30-19:0', 'Saturday': '8:0-17:0', 'Sunday': '8:0-17:0'}, 'description': 'Located at 838-842 Christian St in Philadelphia, PA, this establishment offers a wide range of services including Pet Groomers, Pet Stores, Pet Training, Dog Walkers, Pet Services, Pets, and Pet Sitting.'}], 'var_function-call-12933666651297917399': [['Beauty & Spas', 6], ['Nail Salons', 5], ['Hair Removal', 5], ['Waxing', 5], ['Gun/Rifle Ranges', 4]], 'var_function-call-14403012090627612668': {'collection': 'business', 'filter': {'business_id': {'$in': ['businessid_79', 'businessid_44', 'businessid_13', 'businessid_9', 'businessid_74', 'businessid_25', 'businessid_66', 'businessid_29', 'businessid_39', 'businessid_67', 'businessid_15', 'businessid_33', 'businessid_81', 'businessid_36', 'businessid_12', 'businessid_60', 'businessid_89', 'businessid_6', 'businessid_71', 'businessid_91', 'businessid_46', 'businessid_1', 'businessid_47', 'businessid_16', 'businessid_55', 'businessid_17', 'businessid_43', 'businessid_31', 'businessid_99', 'businessid_53', 'businessid_51', 'businessid_37', 'businessid_57', 'businessid_8', 'businessid_56', 'businessid_62', 'businessid_86', 'businessid_97', 'businessid_72', 'businessid_85', 'businessid_42', 'businessid_40', 'businessid_7', 'businessid_92', 'businessid_61', 'businessid_23', 'businessid_41', 'businessid_10', 'businessid_45', 'businessid_82', 'businessid_76', 'businessid_14', 'businessid_3', 'businessid_96', 'businessid_98', 'businessid_22', 'businessid_20', 'businessid_88', 'businessid_21', 'businessid_26', 'businessid_68', 'businessid_4']}}, 'projection': {'business_id': 1, 'description': 1}, 'limit': 1000}, 'var_function-call-6573041892300133864': 'file_storage/function-call-6573041892300133864.json'}

exec(code, env_args)
