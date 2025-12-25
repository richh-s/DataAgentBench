code = """import json

# Load data
reviews_data = locals()['var_function-call-6979422116729000224']
businesses_data = locals()['var_function-call-218007213437508844'] # The filtered one

if isinstance(reviews_data, str):
    with open(reviews_data, 'r') as f:
        reviews_data = json.load(f)
if isinstance(businesses_data, str):
    with open(businesses_data, 'r') as f:
        businesses_data = json.load(f)

# Create lookup for counts
review_counts = {}
for item in reviews_data:
    ref = item['business_ref']
    bid = ref.replace('businessref_', 'businessid_')
    count = int(item['count'])
    review_counts[bid] = count

category_counts = {}

patterns = [
    "in the category of ",
    "in the fields of ",
    "providing a range of services in ",
    "services, including ",
    "services including ",
    "destination for ",
    "services in "
]

for bus in businesses_data:
    bid = bus['business_id']
    if bid in review_counts:
        desc = bus.get('description', '')
        cats_str = None
        
        for p in patterns:
            if p in desc:
                cats_str = desc.split(p)[-1]
                break
        
        if cats_str:
            if cats_str.endswith('.'):
                cats_str = cats_str[:-1]
            
            # Remove quotes if present (e.g., 'Restaurants, Chinese')
            cats_str = cats_str.replace("'", "")

            parts = [c.strip() for c in cats_str.split(',')]
            
            final_cats = []
            for part in parts:
                if part.lower().startswith('and '):
                    part = part[4:]
                final_cats.append(part)
            
            cnt = review_counts[bid]
            for cat in final_cats:
                category_counts[cat] = category_counts.get(cat, 0) + cnt

sorted_cats = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)
print("__RESULT__:")
print(json.dumps(sorted_cats[:10])) # Print top 10 to see ties"""

env_args = {'var_function-call-3096126179957635233': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-6979422116729000224': [{'business_ref': 'businessref_36', 'count': '2'}, {'business_ref': 'businessref_60', 'count': '2'}, {'business_ref': 'businessref_12', 'count': '1'}, {'business_ref': 'businessref_53', 'count': '1'}, {'business_ref': 'businessref_51', 'count': '2'}, {'business_ref': 'businessref_8', 'count': '1'}, {'business_ref': 'businessref_57', 'count': '2'}, {'business_ref': 'businessref_86', 'count': '1'}, {'business_ref': 'businessref_97', 'count': '1'}, {'business_ref': 'businessref_62', 'count': '1'}, {'business_ref': 'businessref_72', 'count': '1'}, {'business_ref': 'businessref_37', 'count': '1'}, {'business_ref': 'businessref_13', 'count': '1'}, {'business_ref': 'businessref_79', 'count': '1'}, {'business_ref': 'businessref_26', 'count': '1'}, {'business_ref': 'businessref_68', 'count': '1'}, {'business_ref': 'businessref_41', 'count': '1'}, {'business_ref': 'businessref_10', 'count': '1'}, {'business_ref': 'businessref_45', 'count': '3'}, {'business_ref': 'businessref_96', 'count': '2'}, {'business_ref': 'businessref_98', 'count': '1'}, {'business_ref': 'businessref_14', 'count': '1'}, {'business_ref': 'businessref_20', 'count': '1'}, {'business_ref': 'businessref_6', 'count': '2'}, {'business_ref': 'businessref_92', 'count': '2'}, {'business_ref': 'businessref_33', 'count': '3'}, {'business_ref': 'businessref_15', 'count': '1'}, {'business_ref': 'businessref_74', 'count': '2'}, {'business_ref': 'businessref_66', 'count': '2'}, {'business_ref': 'businessref_9', 'count': '1'}, {'business_ref': 'businessref_31', 'count': '1'}], 'var_function-call-3603034238412166639': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-10180997389381951357': [['Nail Salons', 3], ['Hair Removal', 3], ['Beauty & Spas', 3], ['Waxing', 3], ['Internal Medicine', 1]], 'var_function-call-13263095011932863035': ['businessid_36', 'businessid_60', 'businessid_12', 'businessid_53', 'businessid_51', 'businessid_8', 'businessid_57', 'businessid_86', 'businessid_97', 'businessid_62', 'businessid_72', 'businessid_37', 'businessid_13', 'businessid_79', 'businessid_26', 'businessid_68', 'businessid_41', 'businessid_10', 'businessid_45', 'businessid_96', 'businessid_98', 'businessid_14', 'businessid_20', 'businessid_6', 'businessid_92', 'businessid_33', 'businessid_15', 'businessid_74', 'businessid_66', 'businessid_9', 'businessid_31'], 'var_function-call-218007213437508844': [{'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}]}

exec(code, env_args)
