code = """import json
import re
import pandas as pd

# Load previous results
review_counts = locals()['var_function-call-5972648691991730698']
# review_counts is a list of dicts: [{'business_ref': '...', 'review_cnt': '...'}]

# Load business info
with open(locals()['var_function-call-1274174809454323435'], 'r') as f:
    business_info = json.load(f)

# Create a map of business_id -> categories
# Handle prefix difference: businessref_ -> businessid_
# review_counts keys use 'businessref_', business_info keys use 'businessid_'
# So businessref_X corresponds to businessid_X

def extract_categories(description):
    # known start phrases
    start_phrases = [
        "services in ",
        "services, including ",
        "services including ",
        "destination for ",
        "seeking ",
        "category of '",
        "categories of ",
        "specializes in ",
        "offerings, including ",
        "categories such as ",
        "mix of ",
        "menu featuring ",
        "within the "
    ]
    
    # known end phrases (to be stripped from the end)
    end_phrases = [
        " options for every palate",
        " options",
        " services",
        " categories",
        " cuisine",
        " enthusiasts",
        "'" # for category of '...'
    ]
    
    # Patterns to cut off the tail if it continues with a new clause
    cut_patterns = [
        r", making",
        r", providing",
        r", perfect",
        r" to meet",
        r" perfect for"
    ]
    
    text = description
    found_start = False
    extracted_text = ""
    
    for phrase in start_phrases:
        if phrase in text:
            # take the last occurrence? or first? usually first relevant match.
            # But "services in" might appear in "providing a range of services in..."
            # Let's take the part after the phrase.
            parts = text.split(phrase)
            if len(parts) > 1:
                extracted_text = parts[-1]
                found_start = True
                break
    
    if not found_start:
        return []

    # Clean up the end
    if extracted_text.endswith("."):
        extracted_text = extracted_text[:-1]
        
    for pat in cut_patterns:
        if re.search(pat, extracted_text):
            extracted_text = re.split(pat, extracted_text)[0]
            
    for phrase in end_phrases:
        if extracted_text.endswith(phrase):
            extracted_text = extracted_text[:-len(phrase)]
            
    # Split by commas and "and"
    # Example: "A, B, C, and D" -> ["A", "B", "C", "D"]
    # Replace " and " with ", "
    extracted_text = extracted_text.replace(", and ", ", ")
    extracted_text = extracted_text.replace(" and ", ", ") # careful with "Home and Garden" -> "Home", "Garden"?
    # "Home & Garden" is usually a category. "Food and Drink"?
    # Yelp categories often use "&". "Bed & Breakfast".
    # If " and " is used as a separator, it's tricky.
    # Look at examples: "Education, Elementary Schools, ..., and Montessori Schools." -> ", and "
    # "Gun/Rifle Ranges, Active Life" -> ","
    # "Nail Salons, ..., and Waxing" -> ", and "
    # "Cosmetics & Beauty Supply, ..., and Hair Salons."
    # "Home Services, Plumbing"
    # "Tires, ..., and Oil Change Stations"
    
    # Safe bet: split by ", " then handle "and " at the beginning of the last item if present.
    # But I replaced ", and " with ", ".
    # What about "Food, and Burgers"? -> "Food, Burgers"
    
    cats = [c.strip() for c in extracted_text.split(", ")]
    
    # Clean up individual categories
    clean_cats = []
    for c in cats:
        # sometimes the last item might start with "and " if I didn't catch ", and "
        if c.lower().startswith("and "):
            c = c[4:]
        if c:
            clean_cats.append(c)
            
    return clean_cats

# Process businesses
business_cats = {} # business_id -> list of categories
for b in business_info:
    bid = b['business_id']
    cats = extract_categories(b.get('description', ''))
    business_cats[bid] = cats

# Aggregate reviews
category_counts = {}

for record in review_counts:
    bref = record['business_ref']
    # convert to bid
    bid = bref.replace("businessref_", "businessid_")
    
    count = int(record['review_cnt'])
    
    if bid in business_cats:
        cats = business_cats[bid]
        for c in cats:
            category_counts[c] = category_counts.get(c, 0) + count

# Sort by count
sorted_cats = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)

print("__RESULT__:")
print(json.dumps(sorted_cats[:10])) # Print top 10 to see"""

env_args = {'var_function-call-4607218864018501541': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-5972648691991730698': [{'business_ref': 'businessref_13', 'review_cnt': '1'}, {'business_ref': 'businessref_79', 'review_cnt': '1'}, {'business_ref': 'businessref_6', 'review_cnt': '2'}, {'business_ref': 'businessref_74', 'review_cnt': '2'}, {'business_ref': 'businessref_66', 'review_cnt': '2'}, {'business_ref': 'businessref_9', 'review_cnt': '1'}, {'business_ref': 'businessref_33', 'review_cnt': '3'}, {'business_ref': 'businessref_15', 'review_cnt': '1'}, {'business_ref': 'businessref_36', 'review_cnt': '2'}, {'business_ref': 'businessref_60', 'review_cnt': '2'}, {'business_ref': 'businessref_12', 'review_cnt': '1'}, {'business_ref': 'businessref_31', 'review_cnt': '1'}, {'business_ref': 'businessref_53', 'review_cnt': '1'}, {'business_ref': 'businessref_51', 'review_cnt': '2'}, {'business_ref': 'businessref_8', 'review_cnt': '1'}, {'business_ref': 'businessref_57', 'review_cnt': '2'}, {'business_ref': 'businessref_86', 'review_cnt': '1'}, {'business_ref': 'businessref_97', 'review_cnt': '1'}, {'business_ref': 'businessref_62', 'review_cnt': '1'}, {'business_ref': 'businessref_72', 'review_cnt': '1'}, {'business_ref': 'businessref_37', 'review_cnt': '1'}, {'business_ref': 'businessref_92', 'review_cnt': '2'}, {'business_ref': 'businessref_26', 'review_cnt': '1'}, {'business_ref': 'businessref_68', 'review_cnt': '1'}, {'business_ref': 'businessref_41', 'review_cnt': '1'}, {'business_ref': 'businessref_10', 'review_cnt': '1'}, {'business_ref': 'businessref_45', 'review_cnt': '3'}, {'business_ref': 'businessref_96', 'review_cnt': '2'}, {'business_ref': 'businessref_98', 'review_cnt': '1'}, {'business_ref': 'businessref_14', 'review_cnt': '1'}, {'business_ref': 'businessref_20', 'review_cnt': '1'}], 'var_function-call-9176172678891447068': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-17753523269390261685': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-1274174809454323435': 'file_storage/function-call-1274174809454323435.json'}

exec(code, env_args)
