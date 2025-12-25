code = """import json
import re
import pandas as pd

# Load SQL result
sql_data = locals()['var_function-call-4854865074449366240']
# Reconstruct reviews_map
reviews_map = {}
for row in sql_data:
    bid = row['business_ref'].replace('businessref_', 'businessid_')
    cnt = int(row['review_count'])
    reviews_map[bid] = cnt

# Load Mongo result
# The previous tool result for Mongo is stored in a file because it was likely large (though the preview showed 5). 
# Wait, if it's large, the system message says: "The next message will include a preview ... and the storage entry will be the .json file path".
# But the message for Mongo query result `var_function-call-4986375679061116475` said: "The result is: [...]" and showed 5 items. 
# It did NOT give a file path. It gave the content directly.
# However, usually if it shows [...] it means it's a list. If it was truncated, it would be explicitly stated or I should check if it's a list of 5 or more.
# Let's check if `var_function-call-4986375679061116475` is a list or a string path.
# Actually, the tool output format is a dictionary with 'results' key which is a list of strings? No.
# The `query_db` returns a list of records.
# If the previous output was the full list, then I can just use it.
# BUT, 5 records is very small. I suspect it's a preview or I need to handle it carefully.
# Let's inspect the type of `var_function-call-4986375679061116475`.

mongo_data = locals()['var_function-call-4986375679061116475']

# If mongo_data is a string and ends with .json, it's a file path.
if isinstance(mongo_data, str) and mongo_data.endswith('.json'):
    with open(mongo_data, 'r') as f:
        mongo_records = json.load(f)
else:
    mongo_records = mongo_data

# Filter businesses
target_businesses = set(reviews_map.keys())
relevant_businesses = [b for b in mongo_records if b['business_id'] in target_businesses]

# Parse categories and count reviews
category_counts = {}

# Regex patterns
# "services in X, Y, and Z."
# "services, including X, Y, and Z."
# "destination for X, Y."
pattern = re.compile(r"(?:services in|services, including|services including|destination for) (.*?)(?:\.$|$)", re.IGNORECASE)

for b in relevant_businesses:
    bid = b['business_id']
    desc = b.get('description', '')
    count = reviews_map[bid]
    
    match = pattern.search(desc)
    if match:
        cats_str = match.group(1)
        # Split by comma
        parts = cats_str.split(',')
        cleaned_cats = []
        for i, part in enumerate(parts):
            p = part.strip()
            if i == len(parts) - 1:
                # Last part might have "and "
                if p.lower().startswith('and '):
                    p = p[4:].strip()
            if p:
                cleaned_cats.append(p)
        
        for cat in cleaned_cats:
            category_counts[cat] = category_counts.get(cat, 0) + count

# Sort and get top 5
sorted_cats = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)
top_5 = sorted_cats[:5]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-394759627508976658': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-4854865074449366240': [{'business_ref': 'businessref_13', 'review_count': '1'}, {'business_ref': 'businessref_79', 'review_count': '1'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_9', 'review_count': '1'}, {'business_ref': 'businessref_33', 'review_count': '3'}, {'business_ref': 'businessref_15', 'review_count': '1'}, {'business_ref': 'businessref_36', 'review_count': '2'}, {'business_ref': 'businessref_60', 'review_count': '2'}, {'business_ref': 'businessref_12', 'review_count': '1'}, {'business_ref': 'businessref_31', 'review_count': '1'}, {'business_ref': 'businessref_6', 'review_count': '2'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_51', 'review_count': '2'}, {'business_ref': 'businessref_92', 'review_count': '2'}, {'business_ref': 'businessref_26', 'review_count': '1'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_45', 'review_count': '3'}, {'business_ref': 'businessref_96', 'review_count': '2'}, {'business_ref': 'businessref_98', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}, {'business_ref': 'businessref_8', 'review_count': '1'}, {'business_ref': 'businessref_57', 'review_count': '2'}, {'business_ref': 'businessref_86', 'review_count': '1'}, {'business_ref': 'businessref_97', 'review_count': '1'}, {'business_ref': 'businessref_62', 'review_count': '1'}, {'business_ref': 'businessref_72', 'review_count': '1'}, {'business_ref': 'businessref_37', 'review_count': '1'}], 'var_function-call-6691035616520908423': {'business_ids': ['businessid_13', 'businessid_79', 'businessid_74', 'businessid_66', 'businessid_9', 'businessid_33', 'businessid_15', 'businessid_36', 'businessid_60', 'businessid_12', 'businessid_31', 'businessid_6', 'businessid_53', 'businessid_51', 'businessid_92', 'businessid_26', 'businessid_68', 'businessid_45', 'businessid_96', 'businessid_98', 'businessid_14', 'businessid_20', 'businessid_41', 'businessid_10', 'businessid_8', 'businessid_57', 'businessid_86', 'businessid_97', 'businessid_62', 'businessid_72', 'businessid_37'], 'reviews_map': {'businessid_13': '1', 'businessid_79': '1', 'businessid_74': '2', 'businessid_66': '2', 'businessid_9': '1', 'businessid_33': '3', 'businessid_15': '1', 'businessid_36': '2', 'businessid_60': '2', 'businessid_12': '1', 'businessid_31': '1', 'businessid_6': '2', 'businessid_53': '1', 'businessid_51': '2', 'businessid_92': '2', 'businessid_26': '1', 'businessid_68': '1', 'businessid_45': '3', 'businessid_96': '2', 'businessid_98': '1', 'businessid_14': '1', 'businessid_20': '1', 'businessid_41': '1', 'businessid_10': '1', 'businessid_8': '1', 'businessid_57': '2', 'businessid_86': '1', 'businessid_97': '1', 'businessid_62': '1', 'businessid_72': '1', 'businessid_37': '1'}}, 'var_function-call-4986375679061116475': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
