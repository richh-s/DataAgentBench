code = """import json
import re

def parse_description_for_categories(description_text):
    if not description_text:
        return []
    
    categories_found = []
    
    # Patterns to extract explicit category lists
    explicit_patterns = [
        r"(?:services in|fields of|including|offers a wide range of services|offers a diverse range of services and products in the fields of|premier destination for|specializing in|featuring|type of business is)\s+([\w\s,&/\-]+(?:\band\b\s+[\w\s,&/\-]+)*)",
    ]
    
    category_raw_string = ""
    for pattern in explicit_patterns:
        match = re.search(pattern, description_text, re.IGNORECASE)
        if match:
            category_raw_string = match.group(1).strip()
            break
            
    # Fallback if no explicit pattern matched, try to find capitalized words/phrases
    if not category_raw_string:
        potential_categories_from_text = re.findall(r"[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*", description_text)
        category_raw_string = ", ".join(potential_categories_from_text)

    if not category_raw_string:
        return []

    # Split the extracted string by common delimiters
    split_categories = re.split(r"[,&/]", category_raw_string)
    
    # Define common non-category keywords for filtering
    non_category_keywords = {
        "located at", "unit", "road", "drive", "pike", "street", "avenue", "blvd", "in", "us", "hwy",
        "w", "e", "s", "n", "facility", "establishment", "destination", "business", "environment",
        "range", "wide", "diverse", "services", "products", "fields", "etc", "providing", "offers",
        "features", "specializes", "area", "town", "city", "this", "for", "a", "the", "of", "and",
        "local", "medical", "health", "life", "child", "care", "day", "elementary", "schools",
        "beauty", "spa", "salons", "hair", "skincare", "makeup", "artists", "dentists", "cosmetics", 
        "tanning", "teeth", "whitening", "shopping", "active", "gun", "rifle", "ranges", 
        "preschools", "montessori", "supply", "place", "center", "home"
    }
    
    final_categories = []
    for cat in split_categories:
        cleaned_cat = cat.strip()
        if cleaned_cat and len(cleaned_cat) > 1: 
            is_keyword = False
            for keyword in non_category_keywords:
                # Check if the keyword is a substring of the cleaned category (case-insensitive)
                if keyword.lower() in cleaned_cat.lower():
                    is_keyword = True
                    break
            if not is_keyword:
                final_categories.append(cleaned_cat)

    return list(set(final_categories))


# Access the raw output from the query_db tool.
# It's a dictionary -> 'query_db_response' key -> 'results' key -> list of strings.
# The actual data is in the first string of this list.
raw_output_dict = locals()['var_function-call-10659396319710554069']
raw_output_string_list = raw_output_dict['query_db_response']['results']

business_data = []
if raw_output_string_list:
    full_output_string = raw_output_string_list[0]
    
    # Extract the JSON array string from the full output string.
    # The JSON array starts after "The result is:\n" and ends before the final newline.
    json_start_tag = "The result is:\n"
    json_start_index = full_output_string.find(json_start_tag)
    
    if json_start_index != -1:
        # Get the substring that contains the JSON array
        json_string_candidate = full_output_string[json_start_index + len(json_start_tag):].strip()
        
        # Remove any trailing newlines or extra characters after the JSON array
        # Ensure the string starts with '[' and ends with ']' for proper JSON parsing
        if json_string_candidate.startswith("[") and json_string_candidate.endswith("]"):
            business_data = json.loads(json_string_candidate)

business_categories = {}
business_id_to_categories = {}

for record in business_data:
    business_id = record.get("business_id")
    description = record.get("description")
    
    if business_id and description:
        categories = parse_description_for_categories(description)
        business_id_to_categories[business_id] = categories

        for category in categories:
            business_categories[category] = business_categories.get(category, 0) + 1

most_common_category = None
max_businesses = 0

for category, count in business_categories.items():
    if count > max_businesses:
        max_businesses = count
        most_common_category = category

business_ids_for_most_common_category = []
if most_common_category:
    for business_id, categories_list in business_id_to_categories.items():
        if most_common_category in categories_list:
            business_ids_for_most_common_category.append(business_id)

# Convert business_id to business_ref format for the next query to user_database
business_refs_for_most_common_category = []
for bid in business_ids_for_most_common_category:
    business_refs_for_most_common_category.append(bid.replace("businessid_", "businessref_"))

output = {
    "most_common_category": most_common_category,
    "max_businesses_in_category": max_businesses,
    "business_refs_for_most_common_category": business_refs_for_most_common_category
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_function-call-12894765245162637948': [{'_id': '6859a000fe8b31cd7362e2ab', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-11309226368549867683': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_function-call-15140377174569186594': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_function-call-18013218081133412030': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_function-call-316610574023932290': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_function-call-10659396319710554069': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_function-call-7311156690576688476': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}]}

exec(code, env_args)
