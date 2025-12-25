code = """import json
import pandas as pd
import re

# Load data
reviews_data = locals()['var_function-call-3924307552519664893']
biz_file = locals()['var_function-call-1355989582875878614']

if isinstance(reviews_data, str) and reviews_data.endswith('.json'):
    with open(reviews_data, 'r') as f:
        reviews_data = json.load(f)

with open(biz_file, 'r') as f:
    biz_data = json.load(f)

df_reviews = pd.DataFrame(reviews_data)
df_biz = pd.DataFrame(biz_data)

# Convert business_ref to business_id
df_reviews['business_id'] = df_reviews['business_ref'].str.replace('businessref_', 'businessid_')
df_reviews['cnt'] = df_reviews['cnt'].astype(int)

# Merge
merged = pd.merge(df_reviews, df_biz, on='business_id', how='inner')

def extract_categories(desc):
    if not desc:
        return []
    
    cats = []
    
    # Keywords that introduce a list of categories
    # Note: longer phrases first to avoid partial matches
    keywords = [
        'services in', 
        'including', 
        'destination for', 
        'seeking', 
        'fields of', 
        'categories of', 
        'category of', 
        'specializes in', 
        'mix of', 
        'featuring', 
        'categories such as', 
        'perfect for',
        'within the'
    ]
    
    # Regex pattern
    # We want to find a keyword, then capture text until a "stop phrase" or end of string.
    # Stop phrases: " to ", " making it ", " along with ", ".", " offering"
    
    pattern = r'(?:' + '|'.join(re.escape(k) for k in keywords) + r')\s+((?:(?!(?:\.| to | making it | along with | offering )).)+)'
    
    matches = re.findall(pattern, desc, re.IGNORECASE)
    
    for m in matches:
        raw_list = m
        # Cleanup end of string
        # Remove trailing words that are not categories
        # " cuisine", " categories", " enthusiasts", " options", " needs", " services", " products"
        # We can do this by regex replacement at the end of string
        raw_list = re.sub(r'\s+(cuisine|categories|enthusiasts|options|needs|services|products|offerings)$', '', raw_list, flags=re.IGNORECASE)
        
        # Remove quotes if present (e.g. 'Restaurants, Chinese')
        raw_list = raw_list.replace("'", "")
        
        # Split by comma
        items = raw_list.split(',')
        
        for item in items:
            item = item.strip()
            # Remove "and " if it's the last item (e.g. "and Waxing")
            if item.lower().startswith('and '):
                item = item[4:].strip()
            
            if item:
                # Normalize to Title Case to group "nightlife" and "Nightlife"
                # But "American (New)" should handle parens correctly.
                # string.title() might mess up "(New)". "American (new)"
                # Let's just capitalize first letter of words?
                # Or just use the string as is if it looks like a category, or title() it.
                # Simple title() is probably fine for this task.
                cats.append(item.title())
                
    return cats

category_counts = {}

for _, row in merged.iterrows():
    cats = extract_categories(row['description'])
    count = row['cnt']
    # If no categories found, maybe inspect? But for now just skip.
    for c in cats:
        category_counts[c] = category_counts.get(c, 0) + count

# Sort top 5
sorted_cats = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)
top_5 = sorted_cats[:5]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-16910836398196145970': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-3924307552519664893': [{'business_ref': 'businessref_13', 'cnt': '1'}, {'business_ref': 'businessref_79', 'cnt': '1'}, {'business_ref': 'businessref_74', 'cnt': '2'}, {'business_ref': 'businessref_66', 'cnt': '2'}, {'business_ref': 'businessref_9', 'cnt': '1'}, {'business_ref': 'businessref_33', 'cnt': '3'}, {'business_ref': 'businessref_15', 'cnt': '1'}, {'business_ref': 'businessref_6', 'cnt': '2'}, {'business_ref': 'businessref_36', 'cnt': '2'}, {'business_ref': 'businessref_60', 'cnt': '2'}, {'business_ref': 'businessref_12', 'cnt': '1'}, {'business_ref': 'businessref_31', 'cnt': '1'}, {'business_ref': 'businessref_53', 'cnt': '1'}, {'business_ref': 'businessref_51', 'cnt': '2'}, {'business_ref': 'businessref_8', 'cnt': '1'}, {'business_ref': 'businessref_57', 'cnt': '2'}, {'business_ref': 'businessref_86', 'cnt': '1'}, {'business_ref': 'businessref_97', 'cnt': '1'}, {'business_ref': 'businessref_62', 'cnt': '1'}, {'business_ref': 'businessref_72', 'cnt': '1'}, {'business_ref': 'businessref_37', 'cnt': '1'}, {'business_ref': 'businessref_92', 'cnt': '2'}, {'business_ref': 'businessref_26', 'cnt': '1'}, {'business_ref': 'businessref_68', 'cnt': '1'}, {'business_ref': 'businessref_41', 'cnt': '1'}, {'business_ref': 'businessref_10', 'cnt': '1'}, {'business_ref': 'businessref_45', 'cnt': '3'}, {'business_ref': 'businessref_96', 'cnt': '2'}, {'business_ref': 'businessref_98', 'cnt': '1'}, {'business_ref': 'businessref_14', 'cnt': '1'}, {'business_ref': 'businessref_20', 'cnt': '1'}], 'var_function-call-8088175071135996982': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-9218989260110529031': [['Nail Salons', 3], ['Hair Removal', 3], ['Beauty & Spas', 3], ['and Waxing', 3], ['Internal Medicine', 1]], 'var_function-call-1355989582875878614': 'file_storage/function-call-1355989582875878614.json'}

exec(code, env_args)
