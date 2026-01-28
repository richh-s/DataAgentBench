code = """import json, re, statistics

# Data from previous tool calls
biz_records = var_call_l3KGrxWBWhdIMDnvgCj5VtJt
review_avgs = var_call_nf152aN2U29miZjCmvnk0SYL

# Build review avg map
avg_map = {r['business_ref']: float(r['avg_rating']) for r in review_avgs}

# Helper to extract categories from description
def extract_categories(desc):
    if not desc:
        return []
    desc = desc.replace('\n',' ').strip()
    # phrases to look for
    phrases = ['including', 'in the fields of', 'in the fields of the', 'in the fields of services', 'in the fields', 'in the', 'in ', 'for ']
    idx = None
    phrase_found = None
    for p in phrases:
        i = desc.lower().find(p)
        if i != -1:
            # choose the earliest occurrence after the word 'services' or generally the first occurrence
            idx = i + len(p)
            phrase_found = p
            break
    if idx is None:
        # fallback: try split by 'offers' and take part after
        m = re.search(r'offers.*(?:in|including|for)\s', desc, flags=re.IGNORECASE)
        if m:
            idx = m.end()
        else:
            # take last comma separated tail as best effort
            parts = desc.split(',')
            if len(parts) > 1:
                tail = parts[-1]
                return [tail.strip().rstrip('.')]
            return []
    tail = desc[idx:]
    # truncate at next period
    tail = tail.split('.')[0]
    # replace ' and ' with ', '
    tail = tail.replace(' and ', ', ')
    # split by commas
    items = [it.strip().strip('.') for it in tail.split(',') if it.strip()]
    # Filter out obvious non-category words
    filtered = []
    for it in items:
        # remove leading words like 'a', 'the'
        it_clean = re.sub(r"^(a |the )", '', it, flags=re.IGNORECASE).strip()
        # discard if too short
        if len(it_clean) < 2:
            continue
        filtered.append(it_clean)
    return filtered

# Map business_id to categories
biz_cats = {}
for b in biz_records:
    bid = b.get('business_id')
    desc = b.get('description','')
    cats = extract_categories(desc)
    biz_cats[bid] = cats

# Aggregate counts
from collections import Counter, defaultdict
cat_counts = Counter()
cat_to_biz = defaultdict(list)
for bid, cats in biz_cats.items():
    for c in cats:
        cat_counts[c] += 1
        cat_to_biz[c].append(bid)

if not cat_counts:
    result = {"category": None, "business_count": 0, "average_rating": None}
else:
    # find category with max count
    max_count = max(cat_counts.values())
    # if multiple, pick the one with highest average rating afterwards; but spec asks largest number -> pick any with max
    top_cats = [c for c,v in cat_counts.items() if v==max_count]
    # choose the top category (lexicographically smallest for determinism)
    top_cats.sort()
    top_cat = top_cats[0]
    # compute average rating across businesses in this category
    ratings = []
    for bid in cat_to_biz[top_cat]:
        bref = bid.replace('businessid_','businessref_')
        if bref in avg_map:
            ratings.append(avg_map[bref])
    avg_rating = None
    if ratings:
        avg_rating = sum(ratings)/len(ratings)
    result = {"category": top_cat, "business_count": max_count, "average_rating": avg_rating}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_aJBuum9quwEiIiBoenDTl0OL': [{'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'business_id': 'businessid_88', 'name': 'Impact Guns', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'attributes': 'None'}, {'business_id': 'businessid_33', 'name': 'J&Q Nails', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}], 'var_call_nf152aN2U29miZjCmvnk0SYL': [{'business_ref': 'businessref_81', 'avg_rating': '3.6666666666666665', 'review_count': '6'}, {'business_ref': 'businessref_93', 'avg_rating': '2.857142857142857', 'review_count': '7'}, {'business_ref': 'businessref_67', 'avg_rating': '3.3260869565217392', 'review_count': '46'}, {'business_ref': 'businessref_15', 'avg_rating': '3.5294117647058822', 'review_count': '17'}, {'business_ref': 'businessref_54', 'avg_rating': '3.5', 'review_count': '10'}, {'business_ref': 'businessref_33', 'avg_rating': '3.5217391304347827', 'review_count': '23'}, {'business_ref': 'businessref_89', 'avg_rating': '3.04', 'review_count': '25'}, {'business_ref': 'businessref_24', 'avg_rating': '3.289473684210526', 'review_count': '38'}, {'business_ref': 'businessref_36', 'avg_rating': '4.090909090909091', 'review_count': '44'}, {'business_ref': 'businessref_12', 'avg_rating': '3.730769230769231', 'review_count': '26'}, {'business_ref': 'businessref_60', 'avg_rating': '2.0', 'review_count': '32'}, {'business_ref': 'businessref_52', 'avg_rating': '4.166666666666667', 'review_count': '6'}, {'business_ref': 'businessref_43', 'avg_rating': '3.0476190476190474', 'review_count': '21'}, {'business_ref': 'businessref_48', 'avg_rating': '3.3846153846153846', 'review_count': '13'}, {'business_ref': 'businessref_17', 'avg_rating': '3.9', 'review_count': '10'}, {'business_ref': 'businessref_31', 'avg_rating': '1.5', 'review_count': '14'}, {'business_ref': 'businessref_78', 'avg_rating': '5.0', 'review_count': '6'}, {'business_ref': 'businessref_99', 'avg_rating': '3.2', 'review_count': '5'}, {'business_ref': 'businessref_51', 'avg_rating': '3.9714285714285715', 'review_count': '35'}, {'business_ref': 'businessref_53', 'avg_rating': '3.7142857142857144', 'review_count': '7'}, {'business_ref': 'businessref_80', 'avg_rating': '1.8888888888888888', 'review_count': '9'}, {'business_ref': 'businessref_19', 'avg_rating': '3.3333333333333335', 'review_count': '6'}, {'business_ref': 'businessref_57', 'avg_rating': '1.9047619047619047', 'review_count': '42'}, {'business_ref': 'businessref_85', 'avg_rating': '3.3863636363636362', 'review_count': '44'}, {'business_ref': 'businessref_86', 'avg_rating': '3.739130434782609', 'review_count': '46'}, {'business_ref': 'businessref_37', 'avg_rating': '3.2083333333333335', 'review_count': '24'}, {'business_ref': 'businessref_42', 'avg_rating': '4.083333333333333', 'review_count': '12'}, {'business_ref': 'businessref_97', 'avg_rating': '4.294117647058823', 'review_count': '17'}, {'business_ref': 'businessref_8', 'avg_rating': '2.8222222222222224', 'review_count': '45'}, {'business_ref': 'businessref_90', 'avg_rating': '1.0', 'review_count': '3'}, {'business_ref': 'businessref_72', 'avg_rating': '4.6', 'review_count': '5'}, {'business_ref': 'businessref_56', 'avg_rating': '2.3333333333333335', 'review_count': '6'}, {'business_ref': 'businessref_62', 'avg_rating': '3.0', 'review_count': '7'}, {'business_ref': 'businessref_95', 'avg_rating': '2.1666666666666665', 'review_count': '6'}, {'business_ref': 'businessref_40', 'avg_rating': '4.476190476190476', 'review_count': '21'}, {'business_ref': 'businessref_61', 'avg_rating': '2.4705882352941178', 'review_count': '17'}, {'business_ref': 'businessref_92', 'avg_rating': '4.575757575757576', 'review_count': '33'}, {'business_ref': 'businessref_94', 'avg_rating': '4.066666666666666', 'review_count': '30'}, {'business_ref': 'businessref_7', 'avg_rating': '3.75', 'review_count': '16'}, {'business_ref': 'businessref_63', 'avg_rating': '2.8333333333333335', 'review_count': '6'}, {'business_ref': 'businessref_83', 'avg_rating': '4.833333333333333', 'review_count': '6'}, {'business_ref': 'businessref_34', 'avg_rating': '3.3333333333333335', 'review_count': '9'}, {'business_ref': 'businessref_21', 'avg_rating': '2.0285714285714285', 'review_count': '35'}, {'business_ref': 'businessref_26', 'avg_rating': '1.7083333333333333', 'review_count': '24'}, {'business_ref': 'businessref_68', 'avg_rating': '1.7619047619047619', 'review_count': '21'}, {'business_ref': 'businessref_88', 'avg_rating': '3.212121212121212', 'review_count': '33'}, {'business_ref': 'businessref_65', 'avg_rating': '3.8333333333333335', 'review_count': '18'}, {'business_ref': 'businessref_4', 'avg_rating': '5.0', 'review_count': '7'}, {'business_ref': 'businessref_64', 'avg_rating': '3.7142857142857144', 'review_count': '7'}, {'business_ref': 'businessref_10', 'avg_rating': '4.1875', 'review_count': '16'}, {'business_ref': 'businessref_23', 'avg_rating': '3.4444444444444446', 'review_count': '9'}, {'business_ref': 'businessref_49', 'avg_rating': '4.166666666666667', 'review_count': '6'}, {'business_ref': 'businessref_84', 'avg_rating': '5.0', 'review_count': '4'}, {'business_ref': 'businessref_11', 'avg_rating': '4.2', 'review_count': '10'}, {'business_ref': 'businessref_41', 'avg_rating': '4.0', 'review_count': '4'}, {'business_ref': 'businessref_82', 'avg_rating': '4.309523809523809', 'review_count': '42'}, {'business_ref': 'businessref_35', 'avg_rating': '4.125', 'review_count': '8'}, {'business_ref': 'businessref_45', 'avg_rating': '3.3863636363636362', 'review_count': '44'}, {'business_ref': 'businessref_47', 'avg_rating': '3.9047619047619047', 'review_count': '42'}, {'business_ref': 'businessref_16', 'avg_rating': '3.024390243902439', 'review_count': '41'}, {'business_ref': 'businessref_46', 'avg_rating': '4.181818181818182', 'review_count': '44'}, {'business_ref': 'businessref_91', 'avg_rating': '4.911111111111111', 'review_count': '45'}, {'business_ref': 'businessref_1', 'avg_rating': '4.333333333333333', 'review_count': '6'}, {'business_ref': 'businessref_55', 'avg_rating': '4.918918918918919', 'review_count': '37'}, {'business_ref': 'businessref_73', 'avg_rating': '5.0', 'review_count': '5'}, {'business_ref': 'businessref_6', 'avg_rating': '4.0', 'review_count': '37'}, {'business_ref': 'businessref_71', 'avg_rating': '3.268292682926829', 'review_count': '41'}, {'business_ref': 'businessref_38', 'avg_rating': '3.1176470588235294', 'review_count': '17'}, {'business_ref': 'businessref_32', 'avg_rating': '3.4285714285714284', 'review_count': '7'}, {'business_ref': 'businessref_30', 'avg_rating': '3.6', 'review_count': '5'}, {'business_ref': 'businessref_66', 'avg_rating': '2.1818181818181817', 'review_count': '44'}, {'business_ref': 'businessref_9', 'avg_rating': '4.435897435897436', 'review_count': '39'}, {'business_ref': 'businessref_25', 'avg_rating': '4.444444444444445', 'review_count': '36'}, {'business_ref': 'businessref_2', 'avg_rating': '4.769230769230769', 'review_count': '13'}, {'business_ref': 'businessref_74', 'avg_rating': '2.8333333333333335', 'review_count': '6'}, {'business_ref': 'businessref_96', 'avg_rating': '3.8863636363636362', 'review_count': '44'}, {'business_ref': 'businessref_22', 'avg_rating': '2.8181818181818183', 'review_count': '11'}, {'business_ref': 'businessref_20', 'avg_rating': '3.2142857142857144', 'review_count': '42'}, {'business_ref': 'businessref_18', 'avg_rating': '1.8181818181818181', 'review_count': '11'}, {'business_ref': 'businessref_14', 'avg_rating': '3.4', 'review_count': '25'}, {'business_ref': 'businessref_3', 'avg_rating': '2.0', 'review_count': '4'}, {'business_ref': 'businessref_69', 'avg_rating': '4.222222222222222', 'review_count': '9'}, {'business_ref': 'businessref_98', 'avg_rating': '1.2', 'review_count': '5'}, {'business_ref': 'businessref_28', 'avg_rating': '4.055555555555555', 'review_count': '18'}, {'business_ref': 'businessref_70', 'avg_rating': '4.777777777777778', 'review_count': '9'}, {'business_ref': 'businessref_79', 'avg_rating': '4.627906976744186', 'review_count': '43'}, {'business_ref': 'businessref_44', 'avg_rating': '2.9285714285714284', 'review_count': '42'}, {'business_ref': 'businessref_13', 'avg_rating': '3.9166666666666665', 'review_count': '12'}, {'business_ref': 'businessref_87', 'avg_rating': '3.3333333333333335', 'review_count': '6'}, {'business_ref': 'businessref_59', 'avg_rating': '4.6', 'review_count': '30'}, {'business_ref': 'businessref_5', 'avg_rating': '1.6', 'review_count': '5'}, {'business_ref': 'businessref_29', 'avg_rating': '3.9047619047619047', 'review_count': '21'}, {'business_ref': 'businessref_58', 'avg_rating': '4.166666666666667', 'review_count': '6'}, {'business_ref': 'businessref_39', 'avg_rating': '4.125', 'review_count': '8'}, {'business_ref': 'businessref_100', 'avg_rating': '4.0', 'review_count': '4'}, {'business_ref': 'businessref_77', 'avg_rating': '2.5476190476190474', 'review_count': '42'}, {'business_ref': 'businessref_27', 'avg_rating': '3.3214285714285716', 'review_count': '28'}, {'business_ref': 'businessref_50', 'avg_rating': '2.4285714285714284', 'review_count': '7'}, {'business_ref': 'businessref_76', 'avg_rating': '3.5555555555555554', 'review_count': '9'}, {'business_ref': 'businessref_75', 'avg_rating': '4.0', 'review_count': '5'}], 'var_call_fbnX7WxR8BhB6j0GeaVboLTm': [{'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool'}, {'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar'}, {'business_id': 'businessid_88', 'name': 'Impact Guns'}, {'business_id': 'businessid_33', 'name': 'J&Q Nails'}, {'business_id': 'businessid_92', 'name': 'Luminosity'}], 'var_call_XcIj3tnTLt3lRPa8dAToQ2oC': [{'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool'}, {'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar'}, {'business_id': 'businessid_88', 'name': 'Impact Guns'}, {'business_id': 'businessid_33', 'name': 'J&Q Nails'}, {'business_id': 'businessid_92', 'name': 'Luminosity'}], 'var_call_l3KGrxWBWhdIMDnvgCj5VtJt': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'name': 'Luminosity', 'review_count': '39', 'is_open': '1', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'True', 'NoiseLevel': "u'quiet'", 'WiFi': "u'no'"}, 'hours': {'Monday': '10:0-21:0', 'Tuesday': '10:0-21:0', 'Wednesday': '10:0-21:0', 'Thursday': '10:0-21:0', 'Friday': '10:0-21:0', 'Saturday': '10:0-21:0', 'Sunday': '11:0-18:0'}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}]}

exec(code, env_args)
