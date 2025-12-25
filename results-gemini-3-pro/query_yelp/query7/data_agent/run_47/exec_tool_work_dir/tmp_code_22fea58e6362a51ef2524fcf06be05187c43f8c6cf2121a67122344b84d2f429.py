code = """import json

# IDs we looked for
counts_data = locals()['var_function-call-12637187437118360065']
if isinstance(counts_data, str):
    counts_data = json.loads(counts_data)
review_counts = counts_data['counts']
target_ids = set(review_counts.keys())

# IDs we found
desc_data = locals()['var_function-call-596267005130533481']
if isinstance(desc_data, str):
    if desc_data.endswith('.json'):
        with open(desc_data, 'r') as f:
            businesses = json.load(f)
    else:
        businesses = json.loads(desc_data)
else:
    businesses = desc_data

found_ids = set(b['business_id'] for b in businesses)
missing_ids = list(target_ids - found_ids)

b45_desc = "Not Found"
for b in businesses:
    if b['business_id'] == 'businessid_45':
        b45_desc = b.get('description')
        break

print("__RESULT__:")
print(json.dumps({"missing": missing_ids, "b45_desc": b45_desc}))"""

env_args = {'var_function-call-15696234175843027394': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-9418626010781047011': [{'business_ref': 'businessref_13', 'review_count': '1'}, {'business_ref': 'businessref_79', 'review_count': '1'}, {'business_ref': 'businessref_6', 'review_count': '2'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_9', 'review_count': '1'}, {'business_ref': 'businessref_33', 'review_count': '3'}, {'business_ref': 'businessref_15', 'review_count': '1'}, {'business_ref': 'businessref_36', 'review_count': '2'}, {'business_ref': 'businessref_60', 'review_count': '2'}, {'business_ref': 'businessref_12', 'review_count': '1'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_51', 'review_count': '2'}, {'business_ref': 'businessref_8', 'review_count': '1'}, {'business_ref': 'businessref_57', 'review_count': '2'}, {'business_ref': 'businessref_86', 'review_count': '1'}, {'business_ref': 'businessref_97', 'review_count': '1'}, {'business_ref': 'businessref_62', 'review_count': '1'}, {'business_ref': 'businessref_72', 'review_count': '1'}, {'business_ref': 'businessref_37', 'review_count': '1'}, {'business_ref': 'businessref_31', 'review_count': '1'}, {'business_ref': 'businessref_26', 'review_count': '1'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}, {'business_ref': 'businessref_45', 'review_count': '3'}, {'business_ref': 'businessref_96', 'review_count': '2'}, {'business_ref': 'businessref_98', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}, {'business_ref': 'businessref_92', 'review_count': '2'}], 'var_function-call-12637187437118360065': {'ids': ['businessid_13', 'businessid_79', 'businessid_6', 'businessid_74', 'businessid_66', 'businessid_9', 'businessid_33', 'businessid_15', 'businessid_36', 'businessid_60', 'businessid_12', 'businessid_53', 'businessid_51', 'businessid_8', 'businessid_57', 'businessid_86', 'businessid_97', 'businessid_62', 'businessid_72', 'businessid_37', 'businessid_31', 'businessid_26', 'businessid_68', 'businessid_41', 'businessid_10', 'businessid_45', 'businessid_96', 'businessid_98', 'businessid_14', 'businessid_20', 'businessid_92'], 'counts': {'businessid_13': 1, 'businessid_79': 1, 'businessid_6': 2, 'businessid_74': 2, 'businessid_66': 2, 'businessid_9': 1, 'businessid_33': 3, 'businessid_15': 1, 'businessid_36': 2, 'businessid_60': 2, 'businessid_12': 1, 'businessid_53': 1, 'businessid_51': 2, 'businessid_8': 1, 'businessid_57': 2, 'businessid_86': 1, 'businessid_97': 1, 'businessid_62': 1, 'businessid_72': 1, 'businessid_37': 1, 'businessid_31': 1, 'businessid_26': 1, 'businessid_68': 1, 'businessid_41': 1, 'businessid_10': 1, 'businessid_45': 3, 'businessid_96': 2, 'businessid_98': 1, 'businessid_14': 1, 'businessid_20': 1, 'businessid_92': 2}}, 'var_function-call-596267005130533481': [{'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}], 'var_function-call-7828907003675331541': [['Nail Salons', 3], ['Hair Removal', 3], ['Beauty & Spas', 3], ['and Waxing', 3], ['Candy Stores', 2]], 'var_function-call-16164348200264985742': [['Nail Salons', 3], ['Hair Removal', 3], ['Beauty & Spas', 3], ['Waxing', 3], ['Candy Stores', 2], ['Specialty Food', 2], ['Food', 2], ['Internal Medicine', 1], ['Doctors', 1], ['Health & Medical', 1]]}

exec(code, env_args)
