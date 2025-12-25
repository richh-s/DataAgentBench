code = """import json
import pandas as pd
import re

# Load reviews
with open(locals()['var_function-call-3068052922151227449'], 'r') as f:
    reviews_data = json.load(f)

df_reviews = pd.DataFrame(reviews_data)
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'])
business_ratings = df_reviews.groupby('business_ref')['rating'].mean().reset_index()
business_ratings.rename(columns={'rating': 'avg_rating'}, inplace=True)

# Load businesses
with open(locals()['var_function-call-627413835105465887'], 'r') as f:
    businesses_data = json.load(f)

df_biz = pd.DataFrame(businesses_data)
df_biz['business_ref'] = df_biz['business_id'].str.replace('businessid_', 'businessref_')
df_biz = pd.merge(df_biz, business_ratings, on='business_ref', how='left')

def extract_categories(desc):
    if not desc:
        return []
    
    # Pre-cleaning
    desc = desc.replace(" and ", ", ") # Replace ' and ' with ', ' to help splitting, but be careful with names. 
    # Actually, better to split by comma, then handle 'and' in the last element.
    
    # We will try to find the start of the list.
    # We look for the LAST occurrence of any of these phrases.
    start_phrases = [
        "categories of ",
        "category of ",
        "fields of ",
        "specializes in ",
        "including ",
        "ranging from ",
        "destination for ",
        "services in ",
        "selection of ",
        "perfect for ",
        "menu featuring "
    ]
    
    best_start_idx = -1
    best_phrase_len = 0
    
    for phrase in start_phrases:
        idx = desc.rfind(phrase)
        if idx != -1:
            # If we found a phrase that starts later, or same position but longer (unlikely to overlap much)
            if idx > best_start_idx:
                best_start_idx = idx
                best_phrase_len = len(phrase)
    
    extracted_text = ""
    if best_start_idx != -1:
        extracted_text = desc[best_start_idx + best_phrase_len:]
    else:
        return [] # Couldn't find a pattern
        
    # Now look for end phrases in the extracted text
    end_phrases = [
        " to meet",
        " making it",
        " for all",
        " offering a",
        " along with", # This might cut off the second part of a sentence like in biz_93
        " cuisine"
    ]
    
    # For biz_93: "...menu featuring American (New) cuisine, along with a lively atmosphere perfect for nightlife..."
    # If I selected "menu featuring ", text is "American (New) cuisine, along with ... perfect for nightlife..."
    # " cuisine" is an end phrase. result: "American (New)".
    # But I miss "nightlife...".
    # This is tricky.
    
    # What if I scan for multiple lists?
    # e.g. iterate through the string and find all non-overlapping matches of "start_phrase ... end_phrase/EOL".
    # But that's complicated.
    
    # Let's assume the "Last occurrence" strategy works for most.
    # For biz_93, "perfect for" is later than "menu featuring".
    # So "perfect for" -> "nightlife, bars, restaurants, and sports bars."
    # We miss "American (New)".
    # However, "American (New)" is a category too.
    # Maybe I should concatenate all found lists?
    
    # Let's try extracting from ALL start phrases found.
    
    categories = []
    
    # Find all occurrences
    hits = []
    for phrase in start_phrases:
        for match in re.finditer(re.escape(phrase), desc):
            hits.append((match.start(), match.end()))
            
    # Sort hits by start position
    hits.sort()
    
    # Process each hit
    for i, (start, end) in enumerate(hits):
        # Text starts at 'end'
        # It goes until the next hit start, or an end phrase, or EOS.
        
        limit = len(desc)
        # If there is a next hit, stop before it? 
        # But "services in X, including Y". "including" is inside X? No.
        # "services in Education, ... including ..."
        # Usually they are separate clauses.
        
        text_chunk = desc[end:]
        
        # Truncate at nearest end_phrase
        min_end_idx = len(text_chunk)
        for ep in end_phrases:
            ep_idx = text_chunk.find(ep)
            if ep_idx != -1 and ep_idx < min_end_idx:
                min_end_idx = ep_idx
                
        # Also truncate if we hit the start of another known phrase?
        # Maybe.
        
        final_chunk = text_chunk[:min_end_idx]
        
        # Split and clean
        # Remove quotes
        final_chunk = final_chunk.replace("'", "").replace('"', "")
        
        parts = final_chunk.split(',')
        for part in parts:
            part = part.strip()
            # Remove trailing period
            part = part.rstrip('.')
            # Remove 'and ' prefix
            if part.lower().startswith('and '):
                part = part[4:].strip()
            
            # Additional cleanup
            # Sometimes "category of 'Restaurants, Chinese'" -> "Restaurants", "Chinese"
            # handled by replace("'") and split(',')
            
            if part and len(part) > 2: # Filter noise
                # Check if part contains specific unwanted words like "categories such as"
                if "categories such as" in part:
                     part = part.replace("categories such as", "")
                     
                categories.append(part.strip())

    return list(set(categories)) # Unique

df_biz['categories'] = df_biz['description'].apply(extract_categories)

df_exploded = df_biz.explode('categories')
df_exploded = df_exploded.dropna(subset=['categories'])
df_exploded = df_exploded[df_exploded['categories'] != '']

# Group
category_stats = df_exploded.groupby('categories').agg(
    business_count=('business_id', 'nunique'),
    avg_rating=('avg_rating', 'mean')
).reset_index()

category_stats = category_stats.sort_values(by=['business_count', 'avg_rating'], ascending=[False, False])

print("__RESULT__:")
print(category_stats.head(10).to_json(orient='records'))"""

env_args = {'var_function-call-8593270392887686596': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-14324828282752974334': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_function-call-3068052922151227449': 'file_storage/function-call-3068052922151227449.json', 'var_function-call-8582768185476685854': [{'categories': 'Beauty & Spas', 'business_count': 3, 'avg_rating': 4.0007528703}, {'categories': 'Blow Dry/Out Services', 'business_count': 2, 'avg_rating': 4.2402597403}, {'categories': 'Hair Salons', 'business_count': 2, 'avg_rating': 4.2402597403}, {'categories': 'Child Care & Day Care', 'business_count': 1, 'avg_rating': 4.1666666667}, {'categories': 'Active Life', 'business_count': 1, 'avg_rating': 3.2121212121}], 'var_function-call-2461736223281114095': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-627413835105465887': 'file_storage/function-call-627413835105465887.json'}

exec(code, env_args)
