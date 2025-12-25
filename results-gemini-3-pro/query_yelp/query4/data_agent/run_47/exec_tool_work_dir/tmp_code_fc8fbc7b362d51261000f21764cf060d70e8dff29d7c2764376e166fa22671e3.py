code = """import pandas as pd
import json
import re

businesses = locals()['var_function-call-16846015196450619013']
ratings = locals()['var_function-call-10185072251343187390']

# Map ratings
rating_map = {}
for r in ratings:
    # business_ref (businessref_123) -> business_id (businessid_123)
    bid = r['business_ref'].replace('businessref_', 'businessid_')
    rating_map[bid] = float(r['stars'])

category_stats = {}

patterns = [
    r"providing a range of services in\s+(.*?)(?:\.|$)",
    r"including\s+(.*?)(?:\.|$)",
    r"in the fields of\s+(.*?)(?:\.|$)",
    r"destination for\s+(.*?)(?:\.|$)"
]

debug_log = []

for b in businesses:
    bid = b['business_id']
    if bid not in rating_map:
        continue
    
    rating = rating_map[bid]
    desc = b['description']
    
    cats_str = None
    for pat in patterns:
        match = re.search(pat, desc)
        if match:
            cats_str = match.group(1)
            break
    
    if not cats_str:
        debug_log.append(f"Could not parse: {desc}")
        continue
        
    # Clean up and split
    # Replace ", and " with "," and " and " with ","
    # Be careful not to break names like "B & B" if they existed, but " and " is usually a separator here.
    # Given the examples: "Child Care & Day Care" uses &. " and " is separator.
    temp_str = cats_str.replace(", and ", ",").replace(" and ", ",")
    cats = [c.strip() for c in temp_str.split(',') if c.strip()]
    
    for cat in cats:
        if cat not in category_stats:
            category_stats[cat] = {'ratings': [], 'count': 0}
        category_stats[cat]['ratings'].append(rating)
        category_stats[cat]['count'] += 1

# Find max
max_cat = None
max_count = -1
final_avg = 0

all_results = []

for cat, stats in category_stats.items():
    cnt = stats['count']
    avg = sum(stats['ratings']) / len(stats['ratings'])
    all_results.append({"category": cat, "count": cnt, "avg_rating": avg})
    
    if cnt > max_count:
        max_count = cnt
        max_cat = cat
        final_avg = avg
    elif cnt == max_count:
        # If tie, we'll just keep the first one or mention it. 
        # Usually looking for a single answer.
        pass

# Sort by count desc to see top
all_results.sort(key=lambda x: x['count'], reverse=True)

print("__RESULT__:")
print(json.dumps(all_results[0:5]))"""

env_args = {'var_function-call-32349011982437097': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-16846015196450619013': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_function-call-10185072251343187390': [{'business_ref': 'businessref_79', 'stars': '4.627906976744186'}, {'business_ref': 'businessref_44', 'stars': '2.9285714285714284'}, {'business_ref': 'businessref_13', 'stars': '3.9166666666666665'}, {'business_ref': 'businessref_87', 'stars': '3.3333333333333335'}, {'business_ref': 'businessref_47', 'stars': '3.9047619047619047'}, {'business_ref': 'businessref_16', 'stars': '3.024390243902439'}, {'business_ref': 'businessref_46', 'stars': '4.181818181818182'}, {'business_ref': 'businessref_91', 'stars': '4.911111111111111'}, {'business_ref': 'businessref_1', 'stars': '4.333333333333333'}, {'business_ref': 'businessref_55', 'stars': '4.918918918918919'}, {'business_ref': 'businessref_73', 'stars': '5.0'}, {'business_ref': 'businessref_6', 'stars': '4.0'}, {'business_ref': 'businessref_71', 'stars': '3.268292682926829'}, {'business_ref': 'businessref_38', 'stars': '3.1176470588235294'}, {'business_ref': 'businessref_32', 'stars': '3.4285714285714284'}, {'business_ref': 'businessref_30', 'stars': '3.6'}, {'business_ref': 'businessref_66', 'stars': '2.1818181818181817'}, {'business_ref': 'businessref_9', 'stars': '4.435897435897436'}, {'business_ref': 'businessref_25', 'stars': '4.444444444444445'}, {'business_ref': 'businessref_2', 'stars': '4.769230769230769'}, {'business_ref': 'businessref_74', 'stars': '2.8333333333333335'}, {'business_ref': 'businessref_59', 'stars': '4.6'}, {'business_ref': 'businessref_5', 'stars': '1.6'}, {'business_ref': 'businessref_29', 'stars': '3.9047619047619047'}, {'business_ref': 'businessref_58', 'stars': '4.166666666666667'}, {'business_ref': 'businessref_39', 'stars': '4.125'}, {'business_ref': 'businessref_100', 'stars': '4.0'}, {'business_ref': 'businessref_81', 'stars': '3.6666666666666665'}, {'business_ref': 'businessref_93', 'stars': '2.857142857142857'}, {'business_ref': 'businessref_67', 'stars': '3.3260869565217392'}, {'business_ref': 'businessref_15', 'stars': '3.5294117647058822'}, {'business_ref': 'businessref_54', 'stars': '3.5'}, {'business_ref': 'businessref_33', 'stars': '3.5217391304347827'}, {'business_ref': 'businessref_89', 'stars': '3.04'}, {'business_ref': 'businessref_24', 'stars': '3.289473684210526'}, {'business_ref': 'businessref_36', 'stars': '4.090909090909091'}, {'business_ref': 'businessref_12', 'stars': '3.730769230769231'}, {'business_ref': 'businessref_60', 'stars': '2.0'}, {'business_ref': 'businessref_52', 'stars': '4.166666666666667'}, {'business_ref': 'businessref_43', 'stars': '3.0476190476190474'}, {'business_ref': 'businessref_48', 'stars': '3.3846153846153846'}, {'business_ref': 'businessref_17', 'stars': '3.9'}, {'business_ref': 'businessref_31', 'stars': '1.5'}, {'business_ref': 'businessref_78', 'stars': '5.0'}, {'business_ref': 'businessref_99', 'stars': '3.2'}, {'business_ref': 'businessref_51', 'stars': '3.9714285714285715'}, {'business_ref': 'businessref_53', 'stars': '3.7142857142857144'}, {'business_ref': 'businessref_80', 'stars': '1.8888888888888888'}, {'business_ref': 'businessref_19', 'stars': '3.3333333333333335'}, {'business_ref': 'businessref_57', 'stars': '1.9047619047619047'}, {'business_ref': 'businessref_85', 'stars': '3.3863636363636362'}, {'business_ref': 'businessref_86', 'stars': '3.739130434782609'}, {'business_ref': 'businessref_37', 'stars': '3.2083333333333335'}, {'business_ref': 'businessref_42', 'stars': '4.083333333333333'}, {'business_ref': 'businessref_97', 'stars': '4.294117647058823'}, {'business_ref': 'businessref_8', 'stars': '2.8222222222222224'}, {'business_ref': 'businessref_90', 'stars': '1.0'}, {'business_ref': 'businessref_72', 'stars': '4.6'}, {'business_ref': 'businessref_56', 'stars': '2.3333333333333335'}, {'business_ref': 'businessref_62', 'stars': '3.0'}, {'business_ref': 'businessref_95', 'stars': '2.1666666666666665'}, {'business_ref': 'businessref_40', 'stars': '4.476190476190476'}, {'business_ref': 'businessref_61', 'stars': '2.4705882352941178'}, {'business_ref': 'businessref_92', 'stars': '4.575757575757576'}, {'business_ref': 'businessref_94', 'stars': '4.066666666666666'}, {'business_ref': 'businessref_7', 'stars': '3.75'}, {'business_ref': 'businessref_63', 'stars': '2.8333333333333335'}, {'business_ref': 'businessref_83', 'stars': '4.833333333333333'}, {'business_ref': 'businessref_34', 'stars': '3.3333333333333335'}, {'business_ref': 'businessref_21', 'stars': '2.0285714285714285'}, {'business_ref': 'businessref_26', 'stars': '1.7083333333333333'}, {'business_ref': 'businessref_68', 'stars': '1.7619047619047619'}, {'business_ref': 'businessref_88', 'stars': '3.212121212121212'}, {'business_ref': 'businessref_65', 'stars': '3.8333333333333335'}, {'business_ref': 'businessref_4', 'stars': '5.0'}, {'business_ref': 'businessref_64', 'stars': '3.7142857142857144'}, {'business_ref': 'businessref_10', 'stars': '4.1875'}, {'business_ref': 'businessref_23', 'stars': '3.4444444444444446'}, {'business_ref': 'businessref_49', 'stars': '4.166666666666667'}, {'business_ref': 'businessref_84', 'stars': '5.0'}, {'business_ref': 'businessref_11', 'stars': '4.2'}, {'business_ref': 'businessref_41', 'stars': '4.0'}, {'business_ref': 'businessref_77', 'stars': '2.5476190476190474'}, {'business_ref': 'businessref_27', 'stars': '3.3214285714285716'}, {'business_ref': 'businessref_50', 'stars': '2.4285714285714284'}, {'business_ref': 'businessref_76', 'stars': '3.5555555555555554'}, {'business_ref': 'businessref_75', 'stars': '4.0'}, {'business_ref': 'businessref_96', 'stars': '3.8863636363636362'}, {'business_ref': 'businessref_22', 'stars': '2.8181818181818183'}, {'business_ref': 'businessref_20', 'stars': '3.2142857142857144'}, {'business_ref': 'businessref_18', 'stars': '1.8181818181818181'}, {'business_ref': 'businessref_14', 'stars': '3.4'}, {'business_ref': 'businessref_3', 'stars': '2.0'}, {'business_ref': 'businessref_69', 'stars': '4.222222222222222'}, {'business_ref': 'businessref_98', 'stars': '1.2'}, {'business_ref': 'businessref_28', 'stars': '4.055555555555555'}, {'business_ref': 'businessref_70', 'stars': '4.777777777777778'}, {'business_ref': 'businessref_82', 'stars': '4.309523809523809'}, {'business_ref': 'businessref_35', 'stars': '4.125'}, {'business_ref': 'businessref_45', 'stars': '3.3863636363636362'}]}

exec(code, env_args)
