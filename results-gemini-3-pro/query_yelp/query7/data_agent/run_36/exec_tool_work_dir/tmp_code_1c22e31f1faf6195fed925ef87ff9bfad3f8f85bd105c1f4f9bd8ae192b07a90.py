code = """import json
import re

# Load data
sql_data = locals()['var_function-call-700104084572947078'] # [{"business_ref": "...", "count": ...}]
mongo_data = locals()['var_function-call-18445929683046463822'] # [{"business_id": "...", "description": "..."}]

# Create a map of business_id -> count
# Convert ref to id
counts_map = {}
for row in sql_data:
    bid = row['business_ref'].replace('businessref_', 'businessid_')
    counts_map[bid] = int(row['count'])

# Category aggregation
category_counts = {}

def extract_categories(desc):
    # Patterns to look for
    patterns = [
        r"services in (.*)",
        r"services including (.*)",
        r"seeking (.*)",
        r"category of (.*)"
    ]
    
    text_part = None
    for pat in patterns:
        match = re.search(pat, desc)
        if match:
            text_part = match.group(1)
            break
            
    if not text_part:
        # Fallback or maybe the description is just the categories? Unlikely based on examples.
        # Let's try to capture the last sentence or part?
        return []

    # Clean the text
    # Remove trailing dot
    if text_part.endswith('.'):
        text_part = text_part[:-1]
    
    # Remove quotes if present (e.g. 'Restaurants, Chinese')
    text_part = text_part.replace("'", "")
    
    # Split by comma
    cats = [c.strip() for c in text_part.split(',')]
    
    # Handle "and" in the last element e.g. "Beauty & Spas, and Waxing"
    if cats:
        last = cats[-1]
        if last.startswith('and '):
            cats[-1] = last[4:]
            
    return cats

# Process each business
matched_count = 0
for bus in mongo_data:
    bid = bus.get('business_id')
    desc = bus.get('description', '')
    
    if bid in counts_map:
        matched_count += 1
        count = counts_map[bid]
        cats = extract_categories(desc)
        for cat in cats:
            category_counts[cat] = category_counts.get(cat, 0) + count

# Sort and get top 5
sorted_cats = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)
top_5 = sorted_cats[:5]

print("__RESULT__:")
print(json.dumps({
    "top_5": top_5,
    "total_sql_businesses": len(sql_data),
    "total_mongo_businesses": len(mongo_data),
    "matched_businesses": matched_count
}))"""

env_args = {'var_function-call-12603055113156843865': ['review', 'tip', 'user'], 'var_function-call-700104084572947078': [{'business_ref': 'businessref_13', 'count': '1'}, {'business_ref': 'businessref_79', 'count': '1'}, {'business_ref': 'businessref_6', 'count': '2'}, {'business_ref': 'businessref_74', 'count': '2'}, {'business_ref': 'businessref_66', 'count': '2'}, {'business_ref': 'businessref_9', 'count': '1'}, {'business_ref': 'businessref_33', 'count': '3'}, {'business_ref': 'businessref_15', 'count': '1'}, {'business_ref': 'businessref_36', 'count': '2'}, {'business_ref': 'businessref_60', 'count': '2'}, {'business_ref': 'businessref_12', 'count': '1'}, {'business_ref': 'businessref_31', 'count': '1'}, {'business_ref': 'businessref_53', 'count': '1'}, {'business_ref': 'businessref_51', 'count': '2'}, {'business_ref': 'businessref_8', 'count': '1'}, {'business_ref': 'businessref_57', 'count': '2'}, {'business_ref': 'businessref_86', 'count': '1'}, {'business_ref': 'businessref_97', 'count': '1'}, {'business_ref': 'businessref_62', 'count': '1'}, {'business_ref': 'businessref_72', 'count': '1'}, {'business_ref': 'businessref_37', 'count': '1'}, {'business_ref': 'businessref_92', 'count': '2'}, {'business_ref': 'businessref_26', 'count': '1'}, {'business_ref': 'businessref_68', 'count': '1'}, {'business_ref': 'businessref_41', 'count': '1'}, {'business_ref': 'businessref_10', 'count': '1'}, {'business_ref': 'businessref_96', 'count': '2'}, {'business_ref': 'businessref_98', 'count': '1'}, {'business_ref': 'businessref_14', 'count': '1'}, {'business_ref': 'businessref_20', 'count': '1'}, {'business_ref': 'businessref_45', 'count': '3'}], 'var_function-call-15859765085273258938': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-15860727362228958578': {'business_id': {'$in': ['businessid_13', 'businessid_79', 'businessid_6', 'businessid_74', 'businessid_66', 'businessid_9', 'businessid_33', 'businessid_15', 'businessid_36', 'businessid_60', 'businessid_12', 'businessid_31', 'businessid_53', 'businessid_51', 'businessid_8', 'businessid_57', 'businessid_86', 'businessid_97', 'businessid_62', 'businessid_72', 'businessid_37', 'businessid_92', 'businessid_26', 'businessid_68', 'businessid_41', 'businessid_10', 'businessid_96', 'businessid_98', 'businessid_14', 'businessid_20', 'businessid_45']}}, 'var_function-call-18445929683046463822': [{'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}]}

exec(code, env_args)
