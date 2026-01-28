code = """import json
import re

# Load business data from file
file_path = locals()['var_functions.query_db:4']
with open(file_path, 'r') as f:
    business_data = json.load(f)

# Example records to inspect
sample_records = business_data[:10]

results = []
for rec in sample_records:
    desc = rec.get('description', '')
    # Try different patterns
    patterns = [
        r'in [^,]+, ([A-Z]{2})[,.]',     # "in City, XX," or "in City, XX."
        r'This [^,]+, ([A-Z]{2})',       # "This City, XX"
        r'located at [^,]+, ([A-Z]{2})', # "located at address, XX"
    ]
    
    found_state = None
    for pattern in patterns:
        match = re.search(pattern, desc, re.I)
        if match:
            found_state = match.group(1).upper()
            break
    
    results.append({
        'business_id': rec.get('business_id'),
        'description': desc[:100] + '...' if len(desc) > 100 else desc,
        'found_state': found_state
    })

print('__RESULT__:')
print(json.dumps(results, indent=2)[:2000])"""

env_args = {'var_functions.query_db:0': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.list_db:2': ['review', 'tip', 'user'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:12': {'record_count': 100}, 'var_functions.execute_python:14': {'top_state': None, 'total_reviews_top_state': 0, 'businesses_in_top_state': 0, 'state_review_sums': {}}}

exec(code, env_args)
