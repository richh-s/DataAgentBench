code = """import json

# Load data
reviews = locals()['var_function-call-18032970780558021669']
if isinstance(reviews, str):
    with open(reviews, 'r') as f:
        reviews = json.load(f)

businesses_raw = locals()['var_function-call-8499360852962511908']
if isinstance(businesses_raw, str):
    with open(businesses_raw, 'r') as f:
        businesses_raw = json.load(f)

def extract_categories(desc):
    # Order of checking might matter.
    separators = [
        "in the category of '",
        "in the fields of ",
        "services in ",
        "including ",
        "destination for "
    ]
    
    part = None
    used_sep = None
    for sep in separators:
        if sep in desc:
            part = desc.split(sep, 1)[1]
            used_sep = sep
            break
    
    if not part:
        # Fallback or specific pattern check?
        return []
    
    # Clean up the part
    # If "category of '", there might be a closing quote
    if used_sep == "in the category of '":
        part = part.rstrip("'.") # remove closing quote and period
    else:
        part = part.rstrip(".") # remove trailing period

    # Split
    # Sometimes " and " is used as a delimiter? usually comma.
    cats = [c.strip() for c in part.split(',')]
    
    cleaned_cats = []
    for c in cats:
        # Remove "and " if it's the last element starting with it
        if c.lower().startswith('and '):
            c = c[4:]
        
        # Remove quotes if they remained
        c = c.replace("'", "")
        
        if c:
            cleaned_cats.append(c)
    return cleaned_cats

business_cat_map = {}
for b in businesses_raw:
    bid = b['business_id']
    desc = b.get('description', '')
    cats = extract_categories(desc)
    business_cat_map[bid] = cats

# Aggregate
category_counts = {}
for r in reviews:
    bref = r['business_ref']
    bid = bref.replace('businessref_', 'businessid_')
    count = int(r['review_cnt'])
    
    cats = business_cat_map.get(bid, [])
    for cat in cats:
        category_counts[cat] = category_counts.get(cat, 0) + count

# Sort
sorted_cats = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)
top_5 = sorted_cats[:5]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-6734760019395436049': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-18032970780558021669': [{'business_ref': 'businessref_13', 'review_cnt': '1'}, {'business_ref': 'businessref_79', 'review_cnt': '1'}, {'business_ref': 'businessref_74', 'review_cnt': '2'}, {'business_ref': 'businessref_66', 'review_cnt': '2'}, {'business_ref': 'businessref_9', 'review_cnt': '1'}, {'business_ref': 'businessref_33', 'review_cnt': '3'}, {'business_ref': 'businessref_15', 'review_cnt': '1'}, {'business_ref': 'businessref_36', 'review_cnt': '2'}, {'business_ref': 'businessref_60', 'review_cnt': '2'}, {'business_ref': 'businessref_12', 'review_cnt': '1'}, {'business_ref': 'businessref_53', 'review_cnt': '1'}, {'business_ref': 'businessref_51', 'review_cnt': '2'}, {'business_ref': 'businessref_8', 'review_cnt': '1'}, {'business_ref': 'businessref_57', 'review_cnt': '2'}, {'business_ref': 'businessref_86', 'review_cnt': '1'}, {'business_ref': 'businessref_97', 'review_cnt': '1'}, {'business_ref': 'businessref_62', 'review_cnt': '1'}, {'business_ref': 'businessref_72', 'review_cnt': '1'}, {'business_ref': 'businessref_37', 'review_cnt': '1'}, {'business_ref': 'businessref_31', 'review_cnt': '1'}, {'business_ref': 'businessref_92', 'review_cnt': '2'}, {'business_ref': 'businessref_26', 'review_cnt': '1'}, {'business_ref': 'businessref_68', 'review_cnt': '1'}, {'business_ref': 'businessref_41', 'review_cnt': '1'}, {'business_ref': 'businessref_10', 'review_cnt': '1'}, {'business_ref': 'businessref_45', 'review_cnt': '3'}, {'business_ref': 'businessref_96', 'review_cnt': '2'}, {'business_ref': 'businessref_98', 'review_cnt': '1'}, {'business_ref': 'businessref_14', 'review_cnt': '1'}, {'business_ref': 'businessref_20', 'review_cnt': '1'}, {'business_ref': 'businessref_6', 'review_cnt': '2'}], 'var_function-call-7576662622308867332': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-376789801749649970': [['Nail Salons', 3], ['Hair Removal', 3], ['Beauty & Spas', 3], ['Waxing', 3], ['Internal Medicine', 1]], 'var_function-call-9509976609072817396': ['businessid_13', 'businessid_79', 'businessid_74', 'businessid_66', 'businessid_9', 'businessid_33', 'businessid_15', 'businessid_36', 'businessid_60', 'businessid_12', 'businessid_53', 'businessid_51', 'businessid_8', 'businessid_57', 'businessid_86', 'businessid_97', 'businessid_62', 'businessid_72', 'businessid_37', 'businessid_31', 'businessid_92', 'businessid_26', 'businessid_68', 'businessid_41', 'businessid_10', 'businessid_45', 'businessid_96', 'businessid_98', 'businessid_14', 'businessid_20', 'businessid_6'], 'var_function-call-13199999958921324742': '{"collection": "business", "filter": {"business_id": {"$in": ["businessid_13", "businessid_79", "businessid_74", "businessid_66", "businessid_9", "businessid_33", "businessid_15", "businessid_36", "businessid_60", "businessid_12", "businessid_53", "businessid_51", "businessid_8", "businessid_57", "businessid_86", "businessid_97", "businessid_62", "businessid_72", "businessid_37", "businessid_31", "businessid_92", "businessid_26", "businessid_68", "businessid_41", "businessid_10", "businessid_45", "businessid_96", "businessid_98", "businessid_14", "businessid_20", "businessid_6"]}}, "projection": {"business_id": 1, "description": 1}}', 'var_function-call-8499360852962511908': [{'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}]}

exec(code, env_args)
