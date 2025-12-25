code = """import json
import re

businesses = locals()['var_function-call-1537264372374228069']

def extract_categories(desc):
    if not desc:
        return []
    # Try different patterns
    # Pattern 1: services in ... .
    # Pattern 2: services, including ... .
    # Pattern 3: services including ... .
    # Pattern 4: destination for ... .
    # Pattern 5: fields of ... .
    
    # We want to capture everything from the keyword to the end period.
    match = re.search(r"(?:services in|services, including|services including|destination for|fields of) (.+?)\.$", desc)
    if match:
        cat_str = match.group(1)
        # Handle " and " which might be the separator for the last item
        cat_str = re.sub(r",? and ", ", ", cat_str)
        cats = [c.strip() for c in cat_str.split(',')]
        # Filter out empty strings
        cats = [c for c in cats if c]
        return cats
    return []

debug_info = []
for b in businesses[:10]:
    cats = extract_categories(b['description'])
    debug_info.append({"desc": b['description'], "cats": cats})

print("__RESULT__:")
print(json.dumps(debug_info, indent=2))"""

env_args = {'var_function-call-2084756888653713256': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-1537264372374228069': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_function-call-4420950461246935437': 'file_storage/function-call-4420950461246935437.json', 'var_function-call-2756658905368286981': {'category': '', 'business_count': 4, 'average_rating': 4.042231319405232}}

exec(code, env_args)
