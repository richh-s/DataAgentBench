code = """import json
import re

# Load data
businesses = locals()['var_function-call-1645223637297393125']
reviews_list = locals()['var_function-call-9976948011086362930']

# Create review stats lookup
review_stats = {}
for r in reviews_list:
    review_stats[r['business_ref']] = {
        'sum': float(r['sum_rating']),
        'count': int(r['count_rating'])
    }

# Categories tracking
category_businesses = {} # category -> set of business_refs

for b in businesses:
    # Convert ID
    b_id = b['business_id']
    b_ref = b_id.replace('businessid_', 'businessref_')
    
    # Parse categories
    desc = b.get('description', '')
    match = re.search(r"providing a range of services in (.*?)(?:\.|$)", desc)
    if match:
        cat_str = match.group(1)
        # Split by comma
        raw_cats = cat_str.split(',')
        cleaned_cats = []
        for rc in raw_cats:
            rc = rc.strip()
            if rc.startswith('and '):
                rc = rc[4:]
            if rc:
                cleaned_cats.append(rc)
        
        for cat in cleaned_cats:
            if cat not in category_businesses:
                category_businesses[cat] = set()
            category_businesses[cat].add(b_ref)

# Find top category
max_count = 0
top_category = None

for cat, b_refs in category_businesses.items():
    count = len(b_refs)
    if count > max_count:
        max_count = count
        top_category = cat
    elif count == max_count:
        # Tie breaking? usually not needed or take first.
        pass

# Calculate average rating for top category
avg_rating = 0
if top_category:
    total_sum = 0
    total_count = 0
    for b_ref in category_businesses[top_category]:
        if b_ref in review_stats:
            total_sum += review_stats[b_ref]['sum']
            total_count += review_stats[b_ref]['count']
    
    if total_count > 0:
        avg_rating = total_sum / total_count

result = {
    "top_category": top_category,
    "business_count": max_count,
    "average_rating": avg_rating
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-2924133759051617891': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-1645223637297393125': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_function-call-9976948011086362930': [{'business_ref': 'businessref_47', 'sum_rating': '164.0', 'count_rating': '42'}, {'business_ref': 'businessref_16', 'sum_rating': '124.0', 'count_rating': '41'}, {'business_ref': 'businessref_46', 'sum_rating': '184.0', 'count_rating': '44'}, {'business_ref': 'businessref_91', 'sum_rating': '221.0', 'count_rating': '45'}, {'business_ref': 'businessref_1', 'sum_rating': '26.0', 'count_rating': '6'}, {'business_ref': 'businessref_55', 'sum_rating': '182.0', 'count_rating': '37'}, {'business_ref': 'businessref_73', 'sum_rating': '25.0', 'count_rating': '5'}, {'business_ref': 'businessref_6', 'sum_rating': '148.0', 'count_rating': '37'}, {'business_ref': 'businessref_71', 'sum_rating': '134.0', 'count_rating': '41'}, {'business_ref': 'businessref_38', 'sum_rating': '53.0', 'count_rating': '17'}, {'business_ref': 'businessref_32', 'sum_rating': '24.0', 'count_rating': '7'}, {'business_ref': 'businessref_30', 'sum_rating': '18.0', 'count_rating': '5'}, {'business_ref': 'businessref_79', 'sum_rating': '199.0', 'count_rating': '43'}, {'business_ref': 'businessref_44', 'sum_rating': '123.0', 'count_rating': '42'}, {'business_ref': 'businessref_13', 'sum_rating': '47.0', 'count_rating': '12'}, {'business_ref': 'businessref_87', 'sum_rating': '20.0', 'count_rating': '6'}, {'business_ref': 'businessref_66', 'sum_rating': '96.0', 'count_rating': '44'}, {'business_ref': 'businessref_9', 'sum_rating': '173.0', 'count_rating': '39'}, {'business_ref': 'businessref_25', 'sum_rating': '160.0', 'count_rating': '36'}, {'business_ref': 'businessref_2', 'sum_rating': '62.0', 'count_rating': '13'}, {'business_ref': 'businessref_74', 'sum_rating': '17.0', 'count_rating': '6'}, {'business_ref': 'businessref_59', 'sum_rating': '138.0', 'count_rating': '30'}, {'business_ref': 'businessref_5', 'sum_rating': '8.0', 'count_rating': '5'}, {'business_ref': 'businessref_29', 'sum_rating': '82.0', 'count_rating': '21'}, {'business_ref': 'businessref_58', 'sum_rating': '25.0', 'count_rating': '6'}, {'business_ref': 'businessref_39', 'sum_rating': '33.0', 'count_rating': '8'}, {'business_ref': 'businessref_100', 'sum_rating': '16.0', 'count_rating': '4'}, {'business_ref': 'businessref_81', 'sum_rating': '22.0', 'count_rating': '6'}, {'business_ref': 'businessref_93', 'sum_rating': '20.0', 'count_rating': '7'}, {'business_ref': 'businessref_67', 'sum_rating': '153.0', 'count_rating': '46'}, {'business_ref': 'businessref_15', 'sum_rating': '60.0', 'count_rating': '17'}, {'business_ref': 'businessref_54', 'sum_rating': '35.0', 'count_rating': '10'}, {'business_ref': 'businessref_33', 'sum_rating': '81.0', 'count_rating': '23'}, {'business_ref': 'businessref_89', 'sum_rating': '76.0', 'count_rating': '25'}, {'business_ref': 'businessref_24', 'sum_rating': '125.0', 'count_rating': '38'}, {'business_ref': 'businessref_36', 'sum_rating': '180.0', 'count_rating': '44'}, {'business_ref': 'businessref_12', 'sum_rating': '97.0', 'count_rating': '26'}, {'business_ref': 'businessref_60', 'sum_rating': '64.0', 'count_rating': '32'}, {'business_ref': 'businessref_52', 'sum_rating': '25.0', 'count_rating': '6'}, {'business_ref': 'businessref_43', 'sum_rating': '64.0', 'count_rating': '21'}, {'business_ref': 'businessref_48', 'sum_rating': '44.0', 'count_rating': '13'}, {'business_ref': 'businessref_17', 'sum_rating': '39.0', 'count_rating': '10'}, {'business_ref': 'businessref_31', 'sum_rating': '21.0', 'count_rating': '14'}, {'business_ref': 'businessref_78', 'sum_rating': '30.0', 'count_rating': '6'}, {'business_ref': 'businessref_99', 'sum_rating': '16.0', 'count_rating': '5'}, {'business_ref': 'businessref_51', 'sum_rating': '139.0', 'count_rating': '35'}, {'business_ref': 'businessref_53', 'sum_rating': '26.0', 'count_rating': '7'}, {'business_ref': 'businessref_80', 'sum_rating': '17.0', 'count_rating': '9'}, {'business_ref': 'businessref_19', 'sum_rating': '20.0', 'count_rating': '6'}, {'business_ref': 'businessref_57', 'sum_rating': '80.0', 'count_rating': '42'}, {'business_ref': 'businessref_85', 'sum_rating': '149.0', 'count_rating': '44'}, {'business_ref': 'businessref_86', 'sum_rating': '172.0', 'count_rating': '46'}, {'business_ref': 'businessref_37', 'sum_rating': '77.0', 'count_rating': '24'}, {'business_ref': 'businessref_42', 'sum_rating': '49.0', 'count_rating': '12'}, {'business_ref': 'businessref_97', 'sum_rating': '73.0', 'count_rating': '17'}, {'business_ref': 'businessref_8', 'sum_rating': '127.0', 'count_rating': '45'}, {'business_ref': 'businessref_90', 'sum_rating': '3.0', 'count_rating': '3'}, {'business_ref': 'businessref_72', 'sum_rating': '23.0', 'count_rating': '5'}, {'business_ref': 'businessref_56', 'sum_rating': '14.0', 'count_rating': '6'}, {'business_ref': 'businessref_62', 'sum_rating': '21.0', 'count_rating': '7'}, {'business_ref': 'businessref_95', 'sum_rating': '13.0', 'count_rating': '6'}, {'business_ref': 'businessref_40', 'sum_rating': '94.0', 'count_rating': '21'}, {'business_ref': 'businessref_61', 'sum_rating': '42.0', 'count_rating': '17'}, {'business_ref': 'businessref_92', 'sum_rating': '151.0', 'count_rating': '33'}, {'business_ref': 'businessref_94', 'sum_rating': '122.0', 'count_rating': '30'}, {'business_ref': 'businessref_7', 'sum_rating': '60.0', 'count_rating': '16'}, {'business_ref': 'businessref_63', 'sum_rating': '17.0', 'count_rating': '6'}, {'business_ref': 'businessref_83', 'sum_rating': '29.0', 'count_rating': '6'}, {'business_ref': 'businessref_34', 'sum_rating': '30.0', 'count_rating': '9'}, {'business_ref': 'businessref_21', 'sum_rating': '71.0', 'count_rating': '35'}, {'business_ref': 'businessref_26', 'sum_rating': '41.0', 'count_rating': '24'}, {'business_ref': 'businessref_68', 'sum_rating': '37.0', 'count_rating': '21'}, {'business_ref': 'businessref_88', 'sum_rating': '106.0', 'count_rating': '33'}, {'business_ref': 'businessref_65', 'sum_rating': '69.0', 'count_rating': '18'}, {'business_ref': 'businessref_4', 'sum_rating': '35.0', 'count_rating': '7'}, {'business_ref': 'businessref_82', 'sum_rating': '181.0', 'count_rating': '42'}, {'business_ref': 'businessref_35', 'sum_rating': '33.0', 'count_rating': '8'}, {'business_ref': 'businessref_45', 'sum_rating': '149.0', 'count_rating': '44'}, {'business_ref': 'businessref_77', 'sum_rating': '107.0', 'count_rating': '42'}, {'business_ref': 'businessref_27', 'sum_rating': '93.0', 'count_rating': '28'}, {'business_ref': 'businessref_50', 'sum_rating': '17.0', 'count_rating': '7'}, {'business_ref': 'businessref_76', 'sum_rating': '32.0', 'count_rating': '9'}, {'business_ref': 'businessref_75', 'sum_rating': '20.0', 'count_rating': '5'}, {'business_ref': 'businessref_96', 'sum_rating': '171.0', 'count_rating': '44'}, {'business_ref': 'businessref_22', 'sum_rating': '31.0', 'count_rating': '11'}, {'business_ref': 'businessref_20', 'sum_rating': '135.0', 'count_rating': '42'}, {'business_ref': 'businessref_18', 'sum_rating': '20.0', 'count_rating': '11'}, {'business_ref': 'businessref_14', 'sum_rating': '85.0', 'count_rating': '25'}, {'business_ref': 'businessref_3', 'sum_rating': '8.0', 'count_rating': '4'}, {'business_ref': 'businessref_69', 'sum_rating': '38.0', 'count_rating': '9'}, {'business_ref': 'businessref_98', 'sum_rating': '6.0', 'count_rating': '5'}, {'business_ref': 'businessref_28', 'sum_rating': '73.0', 'count_rating': '18'}, {'business_ref': 'businessref_70', 'sum_rating': '43.0', 'count_rating': '9'}, {'business_ref': 'businessref_64', 'sum_rating': '26.0', 'count_rating': '7'}, {'business_ref': 'businessref_10', 'sum_rating': '67.0', 'count_rating': '16'}, {'business_ref': 'businessref_23', 'sum_rating': '31.0', 'count_rating': '9'}, {'business_ref': 'businessref_49', 'sum_rating': '25.0', 'count_rating': '6'}, {'business_ref': 'businessref_84', 'sum_rating': '20.0', 'count_rating': '4'}, {'business_ref': 'businessref_11', 'sum_rating': '42.0', 'count_rating': '10'}, {'business_ref': 'businessref_41', 'sum_rating': '16.0', 'count_rating': '4'}]}

exec(code, env_args)
