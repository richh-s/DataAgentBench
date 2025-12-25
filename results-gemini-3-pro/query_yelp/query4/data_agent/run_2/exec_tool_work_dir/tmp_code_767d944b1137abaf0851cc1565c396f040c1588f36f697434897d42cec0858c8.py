code = """import json
import re
import pandas as pd

# Load data
businesses = locals()['var_function-call-8691904066156103415']
ratings_data = locals()['var_function-call-11622318169406008056']

# Create ratings map
# ratings_data has keys: business_ref, total_rating, review_count
ratings_map = {}
for r in ratings_data:
    # Convert businessref_X to businessid_X
    bid = r['business_ref'].replace('businessref_', 'businessid_')
    ratings_map[bid] = {
        'total_rating': float(r['total_rating']),
        'review_count': int(r['review_count'])
    }

# Parse categories
category_businesses = {} # category -> set of business_ids

triggers = ["services in", "including", "destination for", "fields of"]

for b in businesses:
    desc = b.get('description', '')
    bid = b.get('business_id')
    
    # Find the trigger
    matched_text = None
    # We look for the last occurrence of any trigger, or just the one that works.
    # The structure is usually "... [trigger] [Categories]."
    
    # Let's try to split by the trigger
    best_idx = -1
    best_trigger_len = 0
    
    for t in triggers:
        idx = desc.rfind(t)
        if idx != -1:
            # We want the rightmost trigger? Usually these sentences end with the list.
            if idx > best_idx:
                best_idx = idx
                best_trigger_len = len(t)
    
    if best_idx != -1:
        # Extract content after trigger
        content = desc[best_idx + best_trigger_len:].strip()
        # Remove trailing period
        if content.endswith('.'):
            content = content[:-1]
        
        # Split by comma
        raw_cats = content.split(',')
        clean_cats = []
        for i, cat in enumerate(raw_cats):
            cat = cat.strip()
            if i == len(raw_cats) - 1 and cat.startswith('and '):
                cat = cat[4:].strip()
            if cat:
                clean_cats.append(cat)
        
        for cat in clean_cats:
            if cat not in category_businesses:
                category_businesses[cat] = set()
            category_businesses[cat].add(bid)

# Find top category
max_count = 0
top_category = None

for cat, bids in category_businesses.items():
    count = len(bids)
    if count > max_count:
        max_count = count
        top_category = cat

# Calculate average rating for top category
avg_rating = 0.0
if top_category:
    bids = category_businesses[top_category]
    total_stars = 0.0
    total_reviews = 0
    
    for bid in bids:
        if bid in ratings_map:
            total_stars += ratings_map[bid]['total_rating']
            total_reviews += ratings_map[bid]['review_count']
            
    if total_reviews > 0:
        avg_rating = total_stars / total_reviews

result = {
    "top_category": top_category,
    "business_count": max_count,
    "average_rating": avg_rating
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-9017458627095519762': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-9017458627095520879': [{'review_id': 'reviewid_135', 'user_id': 'userid_548', 'business_ref': 'businessref_34', 'rating': '2', 'useful': '0', 'funny': '0', 'cool': '0', 'text': "Sure, it's cheap, but there isn't much to see. I think you'd have to have a big interest in the topic to find it exciting, and kids would be bored. I think it only lasted maybe 10-15 minutes. Our tour person was somewhat knowledgeable and seemed into it, but he didn't give us much time to read the information on each level. I had to take photos of the plaques to read later, and half of them need replacing, as they are so sun-bleached they're virtually unreadable (tour guide said they're being replaced soon and that the other half were already replaced). I really thought it needed to be higher up to give a good view. The Lewis and Clark State Historic Site just down the road was more interesting and free. If you live around here like I do and have nothing better to do, you might want to give it a go if the topic interests you, but if you're a tourist, this is not something you should waste your time on.", 'date': 'August 01, 2016 at 03:44 AM'}], 'var_function-call-8691904066156103415': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_function-call-11622318169406008056': [{'business_ref': 'businessref_79', 'total_rating': '199.0', 'review_count': '43'}, {'business_ref': 'businessref_44', 'total_rating': '123.0', 'review_count': '42'}, {'business_ref': 'businessref_13', 'total_rating': '47.0', 'review_count': '12'}, {'business_ref': 'businessref_87', 'total_rating': '20.0', 'review_count': '6'}, {'business_ref': 'businessref_47', 'total_rating': '164.0', 'review_count': '42'}, {'business_ref': 'businessref_16', 'total_rating': '124.0', 'review_count': '41'}, {'business_ref': 'businessref_46', 'total_rating': '184.0', 'review_count': '44'}, {'business_ref': 'businessref_91', 'total_rating': '221.0', 'review_count': '45'}, {'business_ref': 'businessref_1', 'total_rating': '26.0', 'review_count': '6'}, {'business_ref': 'businessref_55', 'total_rating': '182.0', 'review_count': '37'}, {'business_ref': 'businessref_73', 'total_rating': '25.0', 'review_count': '5'}, {'business_ref': 'businessref_6', 'total_rating': '148.0', 'review_count': '37'}, {'business_ref': 'businessref_71', 'total_rating': '134.0', 'review_count': '41'}, {'business_ref': 'businessref_38', 'total_rating': '53.0', 'review_count': '17'}, {'business_ref': 'businessref_32', 'total_rating': '24.0', 'review_count': '7'}, {'business_ref': 'businessref_30', 'total_rating': '18.0', 'review_count': '5'}, {'business_ref': 'businessref_66', 'total_rating': '96.0', 'review_count': '44'}, {'business_ref': 'businessref_9', 'total_rating': '173.0', 'review_count': '39'}, {'business_ref': 'businessref_25', 'total_rating': '160.0', 'review_count': '36'}, {'business_ref': 'businessref_2', 'total_rating': '62.0', 'review_count': '13'}, {'business_ref': 'businessref_74', 'total_rating': '17.0', 'review_count': '6'}, {'business_ref': 'businessref_59', 'total_rating': '138.0', 'review_count': '30'}, {'business_ref': 'businessref_5', 'total_rating': '8.0', 'review_count': '5'}, {'business_ref': 'businessref_29', 'total_rating': '82.0', 'review_count': '21'}, {'business_ref': 'businessref_58', 'total_rating': '25.0', 'review_count': '6'}, {'business_ref': 'businessref_39', 'total_rating': '33.0', 'review_count': '8'}, {'business_ref': 'businessref_100', 'total_rating': '16.0', 'review_count': '4'}, {'business_ref': 'businessref_81', 'total_rating': '22.0', 'review_count': '6'}, {'business_ref': 'businessref_93', 'total_rating': '20.0', 'review_count': '7'}, {'business_ref': 'businessref_67', 'total_rating': '153.0', 'review_count': '46'}, {'business_ref': 'businessref_15', 'total_rating': '60.0', 'review_count': '17'}, {'business_ref': 'businessref_54', 'total_rating': '35.0', 'review_count': '10'}, {'business_ref': 'businessref_33', 'total_rating': '81.0', 'review_count': '23'}, {'business_ref': 'businessref_89', 'total_rating': '76.0', 'review_count': '25'}, {'business_ref': 'businessref_24', 'total_rating': '125.0', 'review_count': '38'}, {'business_ref': 'businessref_36', 'total_rating': '180.0', 'review_count': '44'}, {'business_ref': 'businessref_12', 'total_rating': '97.0', 'review_count': '26'}, {'business_ref': 'businessref_60', 'total_rating': '64.0', 'review_count': '32'}, {'business_ref': 'businessref_52', 'total_rating': '25.0', 'review_count': '6'}, {'business_ref': 'businessref_43', 'total_rating': '64.0', 'review_count': '21'}, {'business_ref': 'businessref_48', 'total_rating': '44.0', 'review_count': '13'}, {'business_ref': 'businessref_17', 'total_rating': '39.0', 'review_count': '10'}, {'business_ref': 'businessref_31', 'total_rating': '21.0', 'review_count': '14'}, {'business_ref': 'businessref_78', 'total_rating': '30.0', 'review_count': '6'}, {'business_ref': 'businessref_99', 'total_rating': '16.0', 'review_count': '5'}, {'business_ref': 'businessref_51', 'total_rating': '139.0', 'review_count': '35'}, {'business_ref': 'businessref_53', 'total_rating': '26.0', 'review_count': '7'}, {'business_ref': 'businessref_80', 'total_rating': '17.0', 'review_count': '9'}, {'business_ref': 'businessref_19', 'total_rating': '20.0', 'review_count': '6'}, {'business_ref': 'businessref_57', 'total_rating': '80.0', 'review_count': '42'}, {'business_ref': 'businessref_85', 'total_rating': '149.0', 'review_count': '44'}, {'business_ref': 'businessref_86', 'total_rating': '172.0', 'review_count': '46'}, {'business_ref': 'businessref_37', 'total_rating': '77.0', 'review_count': '24'}, {'business_ref': 'businessref_42', 'total_rating': '49.0', 'review_count': '12'}, {'business_ref': 'businessref_97', 'total_rating': '73.0', 'review_count': '17'}, {'business_ref': 'businessref_8', 'total_rating': '127.0', 'review_count': '45'}, {'business_ref': 'businessref_90', 'total_rating': '3.0', 'review_count': '3'}, {'business_ref': 'businessref_72', 'total_rating': '23.0', 'review_count': '5'}, {'business_ref': 'businessref_56', 'total_rating': '14.0', 'review_count': '6'}, {'business_ref': 'businessref_62', 'total_rating': '21.0', 'review_count': '7'}, {'business_ref': 'businessref_95', 'total_rating': '13.0', 'review_count': '6'}, {'business_ref': 'businessref_40', 'total_rating': '94.0', 'review_count': '21'}, {'business_ref': 'businessref_61', 'total_rating': '42.0', 'review_count': '17'}, {'business_ref': 'businessref_92', 'total_rating': '151.0', 'review_count': '33'}, {'business_ref': 'businessref_94', 'total_rating': '122.0', 'review_count': '30'}, {'business_ref': 'businessref_7', 'total_rating': '60.0', 'review_count': '16'}, {'business_ref': 'businessref_63', 'total_rating': '17.0', 'review_count': '6'}, {'business_ref': 'businessref_83', 'total_rating': '29.0', 'review_count': '6'}, {'business_ref': 'businessref_34', 'total_rating': '30.0', 'review_count': '9'}, {'business_ref': 'businessref_21', 'total_rating': '71.0', 'review_count': '35'}, {'business_ref': 'businessref_26', 'total_rating': '41.0', 'review_count': '24'}, {'business_ref': 'businessref_68', 'total_rating': '37.0', 'review_count': '21'}, {'business_ref': 'businessref_88', 'total_rating': '106.0', 'review_count': '33'}, {'business_ref': 'businessref_65', 'total_rating': '69.0', 'review_count': '18'}, {'business_ref': 'businessref_4', 'total_rating': '35.0', 'review_count': '7'}, {'business_ref': 'businessref_64', 'total_rating': '26.0', 'review_count': '7'}, {'business_ref': 'businessref_10', 'total_rating': '67.0', 'review_count': '16'}, {'business_ref': 'businessref_23', 'total_rating': '31.0', 'review_count': '9'}, {'business_ref': 'businessref_49', 'total_rating': '25.0', 'review_count': '6'}, {'business_ref': 'businessref_84', 'total_rating': '20.0', 'review_count': '4'}, {'business_ref': 'businessref_11', 'total_rating': '42.0', 'review_count': '10'}, {'business_ref': 'businessref_41', 'total_rating': '16.0', 'review_count': '4'}, {'business_ref': 'businessref_82', 'total_rating': '181.0', 'review_count': '42'}, {'business_ref': 'businessref_35', 'total_rating': '33.0', 'review_count': '8'}, {'business_ref': 'businessref_45', 'total_rating': '149.0', 'review_count': '44'}, {'business_ref': 'businessref_77', 'total_rating': '107.0', 'review_count': '42'}, {'business_ref': 'businessref_27', 'total_rating': '93.0', 'review_count': '28'}, {'business_ref': 'businessref_50', 'total_rating': '17.0', 'review_count': '7'}, {'business_ref': 'businessref_76', 'total_rating': '32.0', 'review_count': '9'}, {'business_ref': 'businessref_75', 'total_rating': '20.0', 'review_count': '5'}, {'business_ref': 'businessref_96', 'total_rating': '171.0', 'review_count': '44'}, {'business_ref': 'businessref_22', 'total_rating': '31.0', 'review_count': '11'}, {'business_ref': 'businessref_20', 'total_rating': '135.0', 'review_count': '42'}, {'business_ref': 'businessref_18', 'total_rating': '20.0', 'review_count': '11'}, {'business_ref': 'businessref_14', 'total_rating': '85.0', 'review_count': '25'}, {'business_ref': 'businessref_3', 'total_rating': '8.0', 'review_count': '4'}, {'business_ref': 'businessref_69', 'total_rating': '38.0', 'review_count': '9'}, {'business_ref': 'businessref_98', 'total_rating': '6.0', 'review_count': '5'}, {'business_ref': 'businessref_28', 'total_rating': '73.0', 'review_count': '18'}, {'business_ref': 'businessref_70', 'total_rating': '43.0', 'review_count': '9'}]}

exec(code, env_args)
