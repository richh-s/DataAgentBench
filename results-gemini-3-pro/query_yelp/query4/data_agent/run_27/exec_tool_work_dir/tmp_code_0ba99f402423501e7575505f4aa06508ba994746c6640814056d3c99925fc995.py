code = """import json
import pandas as pd
import re

# Load reviews
with open(locals()['var_function-call-3068052922151227449'], 'r') as f:
    reviews_data = json.load(f)

df_reviews = pd.DataFrame(reviews_data)
# Convert rating to numeric
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'])

# Calculate average rating per business
business_ratings = df_reviews.groupby('business_ref')['rating'].mean().reset_index()
business_ratings.rename(columns={'rating': 'avg_rating'}, inplace=True)

# Load businesses
businesses_data = locals()['var_function-call-14324828282752974334']
df_biz = pd.DataFrame(businesses_data)

# Normalize business_id
# businessid_X -> businessref_X
df_biz['business_ref'] = df_biz['business_id'].str.replace('businessid_', 'businessref_')

# Merge ratings
df_biz = pd.merge(df_biz, business_ratings, on='business_ref', how='left')

# Parse categories
def extract_categories(desc):
    if not desc:
        return []
    
    # Patterns to look for
    patterns = [
        r"services in (.*)",
        r"including (.*)",
        r"destination for (.*)",
        r"fields of (.*)"
    ]
    
    found_text = None
    for pat in patterns:
        match = re.search(pat, desc)
        if match:
            found_text = match.group(1)
            break # Take the first match? The order in list matters. 
            # "including" is very common, might match early. 
            # "services in" is more specific.
            # Maybe I should try to find the one that occurs latest in the string?
            # Or just the one that matches.
            
    # Let's try to be more robust.
    # The patterns in the sample were at the end.
    # "providing a range of services in ..."
    # "including ..."
    # "destination for ..."
    # "fields of ..."
    
    # Let's try to match the specific phrases seen in samples
    phrases = [
        "providing a range of services in ",
        "offers a wide range of services, including ",
        "offers a range of services including ",
        "premier destination for ",
        "products in the fields of "
    ]
    
    text_to_split = None
    for phrase in phrases:
        if phrase in desc:
            text_to_split = desc.split(phrase)[-1]
            break
            
    # Fallback if specific phrases don't match, try simpler ones
    if not text_to_split:
        simple_phrases = ["services in ", "including ", "destination for ", "fields of "]
        for phrase in simple_phrases:
            if phrase in desc:
                text_to_split = desc.split(phrase)[-1]
                break
                
    if text_to_split:
        # Remove trailing period
        text_to_split = text_to_split.strip().rstrip('.')
        # Split by comma and 'and'
        # Replace ' and ' with ',' first?
        # "Cat1, Cat2, and Cat3" -> "Cat1, Cat2, Cat3"
        # "Cat1 and Cat2" -> "Cat1, Cat2"
        # Be careful with "Bed and Breakfast"
        
        # Usually Yelp categories are comma separated, with 'and' for the last one if it's a list.
        # But "Beauty & Spas" has '&'.
        
        # Let's split by ',' first
        parts = text_to_split.split(',')
        categories = []
        for part in parts:
            part = part.strip()
            if part.startswith('and '):
                part = part[4:].strip()
            categories.append(part)
        
        # Verify if the last part contains "and" that splits two categories
        # e.g. "Cat1, Cat2 and Cat3" -> parts=["Cat1", "Cat2 and Cat3"] if split only by comma?
        # No, "Cat1, Cat2, and Cat3" splits to ["Cat1", "Cat2", "and Cat3"]
        # But "Cat1 and Cat2" (no comma) would be one part.
        
        # Let's refine splitting.
        # If the string contains ", and", split by that too.
        
        final_cats = []
        for cat in categories:
            # Check if there is " and " inside a category string that implies two categories
            # This is hard because "Bed and Breakfast" exists.
            # However, looking at the samples: "Education, Elementary Schools, ... and Montessori Schools"
            # It seems the 'and' is a separator for the last item.
            # I'll rely on the comma splitting mainly.
            # If a part starts with "and ", remove it.
            if cat.lower().startswith('and '):
                cat = cat[4:]
            if cat:
                final_cats.append(cat)
        return final_cats
        
    return []

df_biz['categories'] = df_biz['description'].apply(extract_categories)

# Explode
df_exploded = df_biz.explode('categories')

# Drop rows with no category
df_exploded = df_exploded.dropna(subset=['categories'])

# Filter out empty categories
df_exploded = df_exploded[df_exploded['categories'] != '']

# Group by category
category_stats = df_exploded.groupby('categories').agg(
    business_count=('business_id', 'nunique'),
    avg_rating=('avg_rating', 'mean')
).reset_index()

# Sort
category_stats = category_stats.sort_values(by='business_count', ascending=False)

print("__RESULT__:")
print(category_stats.head(5).to_json(orient='records'))"""

env_args = {'var_function-call-8593270392887686596': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-14324828282752974334': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_function-call-3068052922151227449': 'file_storage/function-call-3068052922151227449.json'}

exec(code, env_args)
