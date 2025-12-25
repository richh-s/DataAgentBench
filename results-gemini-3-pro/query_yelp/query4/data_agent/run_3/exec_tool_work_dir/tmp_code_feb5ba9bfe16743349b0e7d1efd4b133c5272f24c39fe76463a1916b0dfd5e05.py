code = """import json
import re

# Load the data
file_path = locals()['var_function-call-195301347354716395']
with open(file_path, 'r') as f:
    data = json.load(f)

category_counts = {}
category_businesses = {}

# Markers that introduce a list of categories
markers = [
    "categories of ",
    "services in ",
    "including ",
    "fields of ",
    "destination for ",
    "specializes in ",
    "selection of " # "selection of Antiques..."
]

# Markers that might end the list if it's not at the end of the sentence
end_markers = [
    ", offering",
    ", making",
    ", along with",
    ", to meet"
]

def clean_category(c):
    # Remove quotes if present
    c = c.replace("'", "").replace('"', "")
    # Remove trailing period
    if c.endswith('.'):
        c = c[:-1]
    return c.strip()

for item in data:
    desc = item.get('description', '')
    bid = item.get('business_id')
    
    # Identify the start of the list
    best_idx = -1
    best_marker_len = 0
    
    for m in markers:
        # We look for the last occurrence to be safe, but usually it's unique
        idx = desc.rfind(m)
        if idx != -1:
            # Heuristic: the marker should probably be in the second half of the text
            # or we take the rightmost one.
            if idx > best_idx:
                best_idx = idx
                best_marker_len = len(m)
    
    if best_idx != -1:
        # Extract text after marker
        cat_section = desc[best_idx + best_marker_len:]
        
        # Check for end markers
        for em in end_markers:
            e_idx = cat_section.find(em)
            if e_idx != -1:
                cat_section = cat_section[:e_idx]
        
        # Clean up
        if cat_section.endswith('.'):
            cat_section = cat_section[:-1]
        
        # Split
        # Handle " and " for the last item
        cat_section = cat_section.replace(' and ', ', ')
        raw_cats = cat_section.split(',')
        
        current_cats = []
        for rc in raw_cats:
            c = clean_category(rc)
            if c:
                # Basic validation: Yelp categories are usually Title Case or '&'
                # e.g. "Beauty & Spas", "Fast Food"
                # Reject if too long (likely a sentence fragment)
                if len(c) > 50: 
                    continue
                current_cats.append(c)
        
        for c in current_cats:
            if c not in category_counts:
                category_counts[c] = 0
                category_businesses[c] = []
            category_counts[c] += 1
            category_businesses[c].append(bid)

# Find top category
if category_counts:
    top_category = max(category_counts, key=category_counts.get)
    top_count = category_counts[top_category]
    # We only need the business_ids for the top category
    top_businesses = category_businesses[top_category]
else:
    top_category = None
    top_count = 0
    top_businesses = []

result = {
    "top_category": top_category,
    "count": top_count,
    "business_ids_count": len(top_businesses),
    "business_ids_sample": top_businesses[:10] # just to verify
}
# Save the full list of IDs to a file or keep in memory if small enough? 
# I'll output the IDs in a subsequent step if needed, or I can store them in a variable.
# But I can't store in a variable from execute_python directly other than printing.
# So I will print the full list if it's not too huge, or write to a temp file.
# Given the instructions, I should print the result.
# I will print the list of IDs.

result["all_business_ids"] = top_businesses

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-364485386677142330': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-15368553860358527870': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_function-call-980639404814378188': {'top_category': 'Beauty & Spas', 'count': 3, 'business_ids': ['businessid_47', 'businessid_33', 'businessid_92']}, 'var_function-call-595090544956915019': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-195301347354716395': 'file_storage/function-call-195301347354716395.json'}

exec(code, env_args)
