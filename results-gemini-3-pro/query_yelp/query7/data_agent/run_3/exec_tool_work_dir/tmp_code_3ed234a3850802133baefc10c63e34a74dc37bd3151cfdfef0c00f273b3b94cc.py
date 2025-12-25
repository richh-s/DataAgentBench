code = """import json
import re

# Load businesses from file
with open(locals()['var_function-call-16696071647236250875'], 'r') as f:
    businesses = json.load(f)

ref_to_count_data = locals()['var_function-call-6194161909839924865']
if isinstance(ref_to_count_data, str):
    ref_to_count = json.loads(ref_to_count_data)['ref_to_count']
else:
    ref_to_count = ref_to_count_data['ref_to_count']

category_counts = {}

def extract_categories(description):
    if not description:
        return []
    
    # Normalize spaces
    text = " " + description + " "
    
    # Patterns that precede the category list
    # We want the LAST occurrence of any of these patterns.
    # Patterns:
    # " including "
    # " in the fields of "
    # " destination for "
    # " seeking "
    # " services in "
    # " specializes in "
    # " specialize in "
    
    patterns = [
        r" including ",
        r" in the fields of ",
        r" destination for ",
        r" seeking ",
        r" services in ",
        r" specializes in ",
        r" specialize in "
    ]
    
    best_start = -1
    
    for p in patterns:
        matches = list(re.finditer(p, text))
        if matches:
            last_match = matches[-1]
            if last_match.end() > best_start:
                best_start = last_match.end()
    
    if best_start == -1:
        # Fallback: maybe split by " offers " and take last part?
        # Or look for " ... "
        return []
        
    cats_str = text[best_start:]
    
    # Remove trailing period and spaces
    cats_str = cats_str.strip()
    if cats_str.endswith('.'):
        cats_str = cats_str[:-1]
    
    # "A, B, and C" -> "A, B, C"
    # "A, B and C" -> "A, B, C"
    cats_str = re.sub(r",?\s+and\s+", ", ", cats_str)
    
    # Split
    cats = [c.strip() for c in cats_str.split(',') if c.strip()]
    
    # Filter out common non-category words if any?
    # e.g. "to meet all your..." is sometimes at the end.
    # "to meet all your vehicle needs"
    # "to meet various home improvement..."
    # "making it a must-visit..."
    
    # Check for " to meet " or " making it " in the extracted string and cut it off.
    # Because these phrases appear AFTER the list in some templates.
    # Example: "... including Tires ... to meet all your vehicle needs."
    
    cutoff_patterns = [
        r" to meet ",
        r" making it "
    ]
    
    for cp in cutoff_patterns:
        match = re.search(cp, cats_str) # Check in the string we extracted
        # But wait, if we split by comma first, we might have "Oil Change Stations to meet all your..."
        # So we should clean cats_str first.
        pass
    
    # Let's clean cats_str based on cutoffs
    for cp in cutoff_patterns:
        match = re.search(cp, cats_str)
        if match:
            cats_str = cats_str[:match.start()]
    
    # Re-split
    cats = [c.strip() for c in cats_str.split(',') if c.strip()]
    
    return cats

# Debug extraction for a few to ensure correctness
debug_log = []

for b in businesses:
    bid = b['business_id']
    if bid in ref_to_count:
        count = int(ref_to_count[bid])
        cats = extract_categories(b.get('description', ''))
        
        # Log for debugging (first 5 and any high count ones)
        if count >= 3:
            debug_log.append({"bid": bid, "count": count, "cats": cats})
            
        for c in cats:
            category_counts[c] = category_counts.get(c, 0) + count

sorted_cats = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)
top5 = sorted_cats[:5]

print("__RESULT__:")
print(json.dumps({"top5": top5, "debug_log": debug_log}))"""

env_args = {'var_function-call-3544115677963916868': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-6297594079857768035': [{'date': 'August 01, 2016 at 03:44 AM'}], 'var_function-call-7818004591109711849': [{'yelping_since': '15 Jan 2009, 16:40'}], 'var_function-call-17723116888847404317': [{'business_ref': 'businessref_79', 'review_count': '4'}, {'business_ref': 'businessref_13', 'review_count': '3'}, {'business_ref': 'businessref_44', 'review_count': '2'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_51', 'review_count': '3'}, {'business_ref': 'businessref_37', 'review_count': '2'}, {'business_ref': 'businessref_57', 'review_count': '4'}, {'business_ref': 'businessref_8', 'review_count': '1'}, {'business_ref': 'businessref_86', 'review_count': '1'}, {'business_ref': 'businessref_97', 'review_count': '1'}, {'business_ref': 'businessref_72', 'review_count': '1'}, {'business_ref': 'businessref_42', 'review_count': '1'}, {'business_ref': 'businessref_21', 'review_count': '2'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_88', 'review_count': '1'}, {'business_ref': 'businessref_26', 'review_count': '1'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_45', 'review_count': '4'}, {'business_ref': 'businessref_82', 'review_count': '1'}, {'business_ref': 'businessref_76', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '2'}, {'business_ref': 'businessref_3', 'review_count': '2'}, {'business_ref': 'businessref_96', 'review_count': '2'}, {'business_ref': 'businessref_20', 'review_count': '1'}, {'business_ref': 'businessref_92', 'review_count': '1'}, {'business_ref': 'businessref_40', 'review_count': '1'}, {'business_ref': 'businessref_6', 'review_count': '4'}, {'business_ref': 'businessref_71', 'review_count': '1'}, {'business_ref': 'businessref_16', 'review_count': '1'}, {'business_ref': 'businessref_29', 'review_count': '1'}, {'business_ref': 'businessref_39', 'review_count': '1'}, {'business_ref': 'businessref_15', 'review_count': '3'}, {'business_ref': 'businessref_33', 'review_count': '3'}, {'business_ref': 'businessref_67', 'review_count': '1'}, {'business_ref': 'businessref_9', 'review_count': '3'}, {'business_ref': 'businessref_74', 'review_count': '1'}, {'business_ref': 'businessref_25', 'review_count': '1'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_60', 'review_count': '2'}, {'business_ref': 'businessref_12', 'review_count': '1'}, {'business_ref': 'businessref_31', 'review_count': '1'}], 'var_function-call-6194161909839924865': {'business_ids': ['businessid_79', 'businessid_13', 'businessid_44', 'businessid_53', 'businessid_51', 'businessid_37', 'businessid_57', 'businessid_8', 'businessid_86', 'businessid_97', 'businessid_72', 'businessid_42', 'businessid_21', 'businessid_68', 'businessid_88', 'businessid_26', 'businessid_41', 'businessid_45', 'businessid_82', 'businessid_76', 'businessid_14', 'businessid_3', 'businessid_96', 'businessid_20', 'businessid_92', 'businessid_40', 'businessid_6', 'businessid_71', 'businessid_16', 'businessid_29', 'businessid_39', 'businessid_15', 'businessid_33', 'businessid_67', 'businessid_9', 'businessid_74', 'businessid_25', 'businessid_66', 'businessid_60', 'businessid_12', 'businessid_31'], 'ref_to_count': {'businessid_79': '4', 'businessid_13': '3', 'businessid_44': '2', 'businessid_53': '1', 'businessid_51': '3', 'businessid_37': '2', 'businessid_57': '4', 'businessid_8': '1', 'businessid_86': '1', 'businessid_97': '1', 'businessid_72': '1', 'businessid_42': '1', 'businessid_21': '2', 'businessid_68': '1', 'businessid_88': '1', 'businessid_26': '1', 'businessid_41': '1', 'businessid_45': '4', 'businessid_82': '1', 'businessid_76': '1', 'businessid_14': '2', 'businessid_3': '2', 'businessid_96': '2', 'businessid_20': '1', 'businessid_92': '1', 'businessid_40': '1', 'businessid_6': '4', 'businessid_71': '1', 'businessid_16': '1', 'businessid_29': '1', 'businessid_39': '1', 'businessid_15': '3', 'businessid_33': '3', 'businessid_67': '1', 'businessid_9': '3', 'businessid_74': '1', 'businessid_25': '1', 'businessid_66': '2', 'businessid_60': '2', 'businessid_12': '1', 'businessid_31': '1'}}, 'var_function-call-14769216288746942785': [{'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'name': 'Candy Barrel', 'review_count': '7', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '4', 'BikeParking': 'False'}, 'hours': 'None', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'name': 'Luminosity', 'review_count': '39', 'is_open': '1', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'True', 'NoiseLevel': "u'quiet'", 'WiFi': "u'no'"}, 'hours': {'Monday': '10:0-21:0', 'Tuesday': '10:0-21:0', 'Wednesday': '10:0-21:0', 'Thursday': '10:0-21:0', 'Friday': '10:0-21:0', 'Saturday': '10:0-21:0', 'Sunday': '11:0-18:0'}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_function-call-8142142678291684881': [['Beauty & Spas', 4], ['Nail Salons', 3], ['Hair Removal', 3], ['Waxing', 3], ['Health & Medical', 2]], 'var_function-call-13037031994024003652': [{'bid': 'businessid_88', 'desc': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.', 'cats': ['Gun/Rifle Ranges', 'Active Life']}, {'bid': 'businessid_41', 'desc': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.', 'cats': ['Internal Medicine', 'Doctors', 'Health & Medical']}, {'bid': 'businessid_33', 'desc': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.', 'cats': ['Nail Salons', 'Hair Removal', 'Beauty & Spas', 'Waxing']}, {'bid': 'businessid_74', 'desc': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.', 'cats': ['Candy Stores', 'Specialty Food', 'Food']}, {'bid': 'businessid_92', 'desc': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.', 'cats': ['Cosmetics & Beauty Supply', 'Cosmetic Dentists', 'Tanning', 'Teeth Whitening', 'Beauty & Spas', 'Dentists', 'Shopping', 'Blow Dry/Out Services', 'Health & Medical', 'Spray Tanning', 'Hair Salons']}], 'var_function-call-14833417244031979949': [], 'var_function-call-2575079599416849823': [{'_id': '6859a000fe8b31cd7362e2e0', 'business_id': 'businessid_79', 'name': 'Pit Stop HQ', 'review_count': '65', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '6:30-19:0', 'Tuesday': '6:30-19:0', 'Wednesday': '6:30-19:0', 'Thursday': '6:30-19:0', 'Friday': '6:30-19:0', 'Saturday': '8:0-17:0', 'Sunday': '8:0-17:0'}, 'description': 'Located at 838-842 Christian St in Philadelphia, PA, this establishment offers a wide range of services including Pet Groomers, Pet Stores, Pet Training, Dog Walkers, Pet Services, Pets, and Pet Sitting.'}], 'var_function-call-16696071647236250875': 'file_storage/function-call-16696071647236250875.json'}

exec(code, env_args)
