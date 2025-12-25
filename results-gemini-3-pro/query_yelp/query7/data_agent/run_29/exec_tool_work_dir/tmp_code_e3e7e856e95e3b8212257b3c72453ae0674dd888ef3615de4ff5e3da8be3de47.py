code = """import json
import re

review_counts_data = locals()['var_function-call-16670192247171742864']
businesses_data = locals()['var_function-call-4437089832935452948']

review_counts = {}
for item in review_counts_data:
    ref = item['business_ref']
    try:
        count = int(item['count'])
    except:
        count = 0
    bid = ref.replace('businessref_', 'businessid_')
    review_counts[bid] = count

regex_pattern = re.compile(r"(?:providing a range of services in|offers a wide range of services, including|offers enthusiasts a premier destination for|offers a range of services in|offers a range of services including|offers a range of services, including)\s+(.*?)[\.]?$")

matched_count = 0
total_reviewed_businesses = 0
unmatched_descriptions = []

for b in businesses_data:
    bid = b['business_id']
    desc = b.get('description', '')
    cnt = review_counts.get(bid, 0)
    if cnt == 0:
        continue
    
    total_reviewed_businesses += 1
    match = regex_pattern.search(desc)
    if match:
        matched_count += 1
    else:
        unmatched_descriptions.append(desc)

print("__RESULT__:")
print(json.dumps({
    "total_reviewed": total_reviewed_businesses,
    "matched": matched_count,
    "unmatched_samples": unmatched_descriptions[:5]
}))"""

env_args = {'var_function-call-12185322744222826645': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-16670192247171742864': [{'business_ref': 'businessref_53', 'count': '1'}, {'business_ref': 'businessref_51', 'count': '2'}, {'business_ref': 'businessref_6', 'count': '2'}, {'business_ref': 'businessref_8', 'count': '1'}, {'business_ref': 'businessref_57', 'count': '2'}, {'business_ref': 'businessref_86', 'count': '1'}, {'business_ref': 'businessref_97', 'count': '1'}, {'business_ref': 'businessref_62', 'count': '1'}, {'business_ref': 'businessref_72', 'count': '1'}, {'business_ref': 'businessref_37', 'count': '1'}, {'business_ref': 'businessref_26', 'count': '1'}, {'business_ref': 'businessref_68', 'count': '1'}, {'business_ref': 'businessref_41', 'count': '1'}, {'business_ref': 'businessref_10', 'count': '1'}, {'business_ref': 'businessref_45', 'count': '3'}, {'business_ref': 'businessref_96', 'count': '2'}, {'business_ref': 'businessref_98', 'count': '1'}, {'business_ref': 'businessref_14', 'count': '1'}, {'business_ref': 'businessref_20', 'count': '1'}, {'business_ref': 'businessref_92', 'count': '2'}, {'business_ref': 'businessref_74', 'count': '2'}, {'business_ref': 'businessref_66', 'count': '2'}, {'business_ref': 'businessref_9', 'count': '1'}, {'business_ref': 'businessref_33', 'count': '3'}, {'business_ref': 'businessref_15', 'count': '1'}, {'business_ref': 'businessref_36', 'count': '2'}, {'business_ref': 'businessref_60', 'count': '2'}, {'business_ref': 'businessref_12', 'count': '1'}, {'business_ref': 'businessref_13', 'count': '1'}, {'business_ref': 'businessref_79', 'count': '1'}, {'business_ref': 'businessref_31', 'count': '1'}], 'var_function-call-16670192247171740429': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-4437089832935452948': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-13931071069181009919': ['Nail Salons', 'Hair Removal', 'Beauty & Spas', 'and Waxing', 'Internal Medicine'], 'var_function-call-9403604578176661805': ['Nail Salons', 'Hair Removal', 'Beauty & Spas', 'Waxing', 'Internal Medicine'], 'var_function-call-1031799342516971348': {'count': 31, 'sample': [{'business_ref': 'businessref_53', 'count': '1'}, {'business_ref': 'businessref_51', 'count': '2'}, {'business_ref': 'businessref_6', 'count': '2'}, {'business_ref': 'businessref_8', 'count': '1'}, {'business_ref': 'businessref_57', 'count': '2'}]}, 'var_function-call-15149235868305864548': [['Nail Salons', 3], ['Hair Removal', 3], ['Beauty & Spas', 3], ['Waxing', 3], ['Internal Medicine', 1], ['Doctors', 1], ['Health & Medical', 1]]}

exec(code, env_args)
