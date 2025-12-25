code = """import json

# Load SQL result
sql_result = locals()['var_function-call-16624978320130190117']
business_counts = {row['business_ref'].replace('businessref_', 'businessid_'): int(row['review_count']) for row in sql_result}

# Load Mongo result
# The tool output for the Mongo query is stored in 'var_function-call-16525585691167775123'
# However, if the output was a file path (because it was large), I should load it.
# The tool description says: "If a tool result is large, the next message will include a preview ... and the storage entry will be the .json file path".
# The previous message showed a JSON list, not a file path. But maybe it was a partial list?
# Let's check the type of the variable.

mongo_data = locals()['var_function-call-16525585691167775123']

if isinstance(mongo_data, str) and mongo_data.endswith('.json'):
    with open(mongo_data, 'r') as f:
        mongo_docs = json.load(f)
else:
    mongo_docs = mongo_data

print(f"SQL Business Count: {len(business_counts)}")
print(f"Mongo Docs Count: {len(mongo_docs)}")

# Parse descriptions
categories_count = {}

for doc in mongo_docs:
    bid = doc['business_id']
    desc = doc.get('description', '')
    if not desc:
        continue
    
    # Extract categories
    # Patterns:
    # "... services in [CATS]."
    # "... services, including [CATS]."
    # "... including [CATS]."
    # "... destination for [CATS]."
    
    cats_str = ""
    if "services in " in desc:
        cats_str = desc.split("services in ")[-1]
    elif "services including " in desc:
        cats_str = desc.split("services including ")[-1]
    elif "including " in desc:
        cats_str = desc.split("including ")[-1]
    elif "destination for " in desc:
        cats_str = desc.split("destination for ")[-1]
    else:
        # Fallback or unknown format
        pass
    
    if cats_str:
        # Remove trailing period
        if cats_str.endswith('.'):
            cats_str = cats_str[:-1]
        
        # Split by comma
        cats = [c.strip() for c in cats_str.split(',')]
        
        # Add counts
        count = business_counts.get(bid, 0)
        for c in cats:
            # Handle "and X" in the last item? e.g. "Beauty & Spas, and Waxing"
            if c.startswith('and '):
                c = c[4:]
            categories_count[c] = categories_count.get(c, 0) + count

# Sort top 5
sorted_cats = sorted(categories_count.items(), key=lambda x: x[1], reverse=True)[:5]
print("__RESULT__:")
print(json.dumps(sorted_cats))"""

env_args = {'var_function-call-1926116299167403223': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-8817279312995942582': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-3835436407834537059': [{'yelping_since': '15 Jan 2009, 16:40'}, {'yelping_since': '13 Jul 2010, 15:42'}, {'yelping_since': '2010-09-07 23:24:36'}, {'yelping_since': 'October 23, 2011 at 07:47 PM'}, {'yelping_since': '2011-08-30 13:46:26'}], 'var_function-call-8705705535669765239': [{'date': 'August 01, 2016 at 03:44 AM'}, {'date': 'June 14, 2021 at 11:39 AM'}, {'date': '29 May 2013, 23:01'}, {'date': '21 May 2016, 18:48'}, {'date': 'November 01, 2021 at 05:11 PM'}], 'var_function-call-16624978320130190117': [{'business_ref': 'businessref_79', 'review_count': '8'}, {'business_ref': 'businessref_44', 'review_count': '4'}, {'business_ref': 'businessref_13', 'review_count': '3'}, {'business_ref': 'businessref_9', 'review_count': '3'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_25', 'review_count': '1'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_29', 'review_count': '1'}, {'business_ref': 'businessref_39', 'review_count': '1'}, {'business_ref': 'businessref_67', 'review_count': '5'}, {'business_ref': 'businessref_15', 'review_count': '3'}, {'business_ref': 'businessref_33', 'review_count': '5'}, {'business_ref': 'businessref_81', 'review_count': '1'}, {'business_ref': 'businessref_36', 'review_count': '3'}, {'business_ref': 'businessref_12', 'review_count': '4'}, {'business_ref': 'businessref_60', 'review_count': '4'}, {'business_ref': 'businessref_89', 'review_count': '3'}, {'business_ref': 'businessref_6', 'review_count': '4'}, {'business_ref': 'businessref_71', 'review_count': '1'}, {'business_ref': 'businessref_91', 'review_count': '2'}, {'business_ref': 'businessref_46', 'review_count': '1'}, {'business_ref': 'businessref_1', 'review_count': '1'}, {'business_ref': 'businessref_47', 'review_count': '1'}, {'business_ref': 'businessref_16', 'review_count': '1'}, {'business_ref': 'businessref_55', 'review_count': '1'}, {'business_ref': 'businessref_17', 'review_count': '1'}, {'business_ref': 'businessref_43', 'review_count': '3'}, {'business_ref': 'businessref_31', 'review_count': '1'}, {'business_ref': 'businessref_99', 'review_count': '1'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_51', 'review_count': '3'}, {'business_ref': 'businessref_37', 'review_count': '6'}, {'business_ref': 'businessref_57', 'review_count': '7'}, {'business_ref': 'businessref_8', 'review_count': '4'}, {'business_ref': 'businessref_56', 'review_count': '1'}, {'business_ref': 'businessref_62', 'review_count': '2'}, {'business_ref': 'businessref_86', 'review_count': '4'}, {'business_ref': 'businessref_97', 'review_count': '1'}, {'business_ref': 'businessref_72', 'review_count': '1'}, {'business_ref': 'businessref_85', 'review_count': '1'}, {'business_ref': 'businessref_42', 'review_count': '1'}, {'business_ref': 'businessref_40', 'review_count': '3'}, {'business_ref': 'businessref_7', 'review_count': '2'}, {'business_ref': 'businessref_92', 'review_count': '2'}, {'business_ref': 'businessref_61', 'review_count': '1'}, {'business_ref': 'businessref_23', 'review_count': '1'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}, {'business_ref': 'businessref_45', 'review_count': '5'}, {'business_ref': 'businessref_82', 'review_count': '2'}, {'business_ref': 'businessref_76', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '3'}, {'business_ref': 'businessref_3', 'review_count': '2'}, {'business_ref': 'businessref_96', 'review_count': '4'}, {'business_ref': 'businessref_98', 'review_count': '3'}, {'business_ref': 'businessref_22', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}, {'business_ref': 'businessref_88', 'review_count': '4'}, {'business_ref': 'businessref_21', 'review_count': '4'}, {'business_ref': 'businessref_26', 'review_count': '4'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_4', 'review_count': '1'}], 'var_function-call-420097590862934078': {'collection': 'business', 'filter': {'business_id': {'$in': ['businessid_79', 'businessid_44', 'businessid_13', 'businessid_9', 'businessid_74', 'businessid_25', 'businessid_66', 'businessid_29', 'businessid_39', 'businessid_67', 'businessid_15', 'businessid_33', 'businessid_81', 'businessid_36', 'businessid_12', 'businessid_60', 'businessid_89', 'businessid_6', 'businessid_71', 'businessid_91', 'businessid_46', 'businessid_1', 'businessid_47', 'businessid_16', 'businessid_55', 'businessid_17', 'businessid_43', 'businessid_31', 'businessid_99', 'businessid_53', 'businessid_51', 'businessid_37', 'businessid_57', 'businessid_8', 'businessid_56', 'businessid_62', 'businessid_86', 'businessid_97', 'businessid_72', 'businessid_85', 'businessid_42', 'businessid_40', 'businessid_7', 'businessid_92', 'businessid_61', 'businessid_23', 'businessid_41', 'businessid_10', 'businessid_45', 'businessid_82', 'businessid_76', 'businessid_14', 'businessid_3', 'businessid_96', 'businessid_98', 'businessid_22', 'businessid_20', 'businessid_88', 'businessid_21', 'businessid_26', 'businessid_68', 'businessid_4']}}, 'projection': {'business_id': 1, 'description': 1}}, 'var_function-call-16525585691167775123': [{'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}], 'var_function-call-217928265536561876': [{'_id': '6859a000fe8b31cd7362e2e0', 'business_id': 'businessid_79', 'name': 'Pit Stop HQ', 'review_count': '65', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '6:30-19:0', 'Tuesday': '6:30-19:0', 'Wednesday': '6:30-19:0', 'Thursday': '6:30-19:0', 'Friday': '6:30-19:0', 'Saturday': '8:0-17:0', 'Sunday': '8:0-17:0'}, 'description': 'Located at 838-842 Christian St in Philadelphia, PA, this establishment offers a wide range of services including Pet Groomers, Pet Stores, Pet Training, Dog Walkers, Pet Services, Pets, and Pet Sitting.'}]}

exec(code, env_args)
