code = """import pandas as pd
import json
import re

# Load reviews
reviews = locals()['var_function-call-17721523080154030816']
df_reviews = pd.DataFrame(reviews)
# Fix IDs
df_reviews['business_id'] = df_reviews['business_ref'].str.replace('businessref_', 'businessid_')
# Count reviews per business
business_review_counts = df_reviews['business_id'].value_counts().to_dict()

# Load business descriptions (Directly as list)
businesses = locals()['var_function-call-16441248379087631793']

category_counts = {}

delimiters = [
    "services in ",
    "including ",
    "seeking ",
    "fields of ",
    "category of "
]

for b in businesses:
    bid = b['business_id']
    desc = b.get('description', '')
    count = business_review_counts.get(bid, 0)
    
    if count == 0:
        continue
        
    # Extract categories
    cats_str = ""
    
    max_idx = -1
    selected_delimiter = ""
    
    for d in delimiters:
        idx = desc.rfind(d)
        if idx != -1:
            if idx > max_idx:
                max_idx = idx
                selected_delimiter = d
                
    if max_idx != -1:
        cats_str = desc[max_idx + len(selected_delimiter):]
    else:
        pass # Handle cases with no match if necessary
        
    # Clean the string
    cats_str = cats_str.strip()
    if cats_str.endswith('.'):
        cats_str = cats_str[:-1]
    
    cats_str = cats_str.replace("'", "").replace('"', "")
    
    cats_list = [c.strip() for c in cats_str.split(',')]
    
    final_cats = []
    for c in cats_list:
        if c.lower().startswith('and '):
            c = c[4:]
        c = c.strip()
        if c:
            final_cats.append(c)
            
    # Add to totals
    for cat in final_cats:
        category_counts[cat] = category_counts.get(cat, 0) + count

# Convert to list and sort
sorted_cats = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)
top_5 = sorted_cats[:5]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-14075298590519107228': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-14075298590519106417': [{'user_id': 'userid_746'}, {'user_id': 'userid_1109'}, {'user_id': 'userid_1950'}, {'user_id': 'userid_1316'}, {'user_id': 'userid_1182'}, {'user_id': 'userid_151'}, {'user_id': 'userid_1158'}, {'user_id': 'userid_508'}, {'user_id': 'userid_435'}, {'user_id': 'userid_958'}, {'user_id': 'userid_1879'}, {'user_id': 'userid_308'}, {'user_id': 'userid_1179'}, {'user_id': 'userid_324'}, {'user_id': 'userid_863'}, {'user_id': 'userid_100'}, {'user_id': 'userid_1333'}, {'user_id': 'userid_1636'}, {'user_id': 'userid_1850'}, {'user_id': 'userid_711'}, {'user_id': 'userid_729'}, {'user_id': 'userid_1505'}, {'user_id': 'userid_1315'}, {'user_id': 'userid_1708'}, {'user_id': 'userid_1661'}, {'user_id': 'userid_850'}, {'user_id': 'userid_1675'}, {'user_id': 'userid_227'}, {'user_id': 'userid_577'}, {'user_id': 'userid_257'}, {'user_id': 'userid_598'}, {'user_id': 'userid_847'}, {'user_id': 'userid_673'}, {'user_id': 'userid_1856'}, {'user_id': 'userid_384'}, {'user_id': 'userid_935'}, {'user_id': 'userid_210'}, {'user_id': 'userid_1101'}, {'user_id': 'userid_945'}, {'user_id': 'userid_842'}, {'user_id': 'userid_1351'}, {'user_id': 'userid_230'}, {'user_id': 'userid_593'}, {'user_id': 'userid_1431'}, {'user_id': 'userid_686'}, {'user_id': 'userid_527'}, {'user_id': 'userid_244'}, {'user_id': 'userid_393'}, {'user_id': 'userid_1178'}, {'user_id': 'userid_526'}, {'user_id': 'userid_90'}, {'user_id': 'userid_238'}, {'user_id': 'userid_1105'}], 'var_function-call-17721523080154030816': [{'business_ref': 'businessref_8'}, {'business_ref': 'businessref_74'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_96'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_74'}, {'business_ref': 'businessref_6'}, {'business_ref': 'businessref_53'}, {'business_ref': 'businessref_41'}, {'business_ref': 'businessref_96'}, {'business_ref': 'businessref_10'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_31'}, {'business_ref': 'businessref_92'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_98'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_51'}, {'business_ref': 'businessref_33'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_60'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_97'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_72'}, {'business_ref': 'businessref_33'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_92'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_51'}, {'business_ref': 'businessref_33'}, {'business_ref': 'businessref_6'}, {'business_ref': 'businessref_12'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_9'}, {'business_ref': 'businessref_60'}], 'var_function-call-15960414796294856725': {'unique_count': 31, 'ids': ['businessid_45', 'businessid_33', 'businessid_57', 'businessid_6', 'businessid_96', 'businessid_92', 'businessid_74', 'businessid_36', 'businessid_60', 'businessid_51', 'businessid_66', 'businessid_31', 'businessid_8', 'businessid_53', 'businessid_41', 'businessid_98', 'businessid_26', 'businessid_10', 'businessid_14', 'businessid_68', 'businessid_13', 'businessid_86', 'businessid_20', 'businessid_15', 'businessid_97', 'businessid_62', 'businessid_72', 'businessid_37', 'businessid_12', 'businessid_79', 'businessid_9'], 'counts': [{'business_id': 'businessid_45', 'review_count': 3}, {'business_id': 'businessid_33', 'review_count': 3}, {'business_id': 'businessid_57', 'review_count': 2}, {'business_id': 'businessid_6', 'review_count': 2}, {'business_id': 'businessid_96', 'review_count': 2}, {'business_id': 'businessid_92', 'review_count': 2}, {'business_id': 'businessid_74', 'review_count': 2}, {'business_id': 'businessid_36', 'review_count': 2}, {'business_id': 'businessid_60', 'review_count': 2}, {'business_id': 'businessid_51', 'review_count': 2}, {'business_id': 'businessid_66', 'review_count': 2}, {'business_id': 'businessid_31', 'review_count': 1}, {'business_id': 'businessid_8', 'review_count': 1}, {'business_id': 'businessid_53', 'review_count': 1}, {'business_id': 'businessid_41', 'review_count': 1}, {'business_id': 'businessid_98', 'review_count': 1}, {'business_id': 'businessid_26', 'review_count': 1}, {'business_id': 'businessid_10', 'review_count': 1}, {'business_id': 'businessid_14', 'review_count': 1}, {'business_id': 'businessid_68', 'review_count': 1}, {'business_id': 'businessid_13', 'review_count': 1}, {'business_id': 'businessid_86', 'review_count': 1}, {'business_id': 'businessid_20', 'review_count': 1}, {'business_id': 'businessid_15', 'review_count': 1}, {'business_id': 'businessid_97', 'review_count': 1}, {'business_id': 'businessid_62', 'review_count': 1}, {'business_id': 'businessid_72', 'review_count': 1}, {'business_id': 'businessid_37', 'review_count': 1}, {'business_id': 'businessid_12', 'review_count': 1}, {'business_id': 'businessid_79', 'review_count': 1}, {'business_id': 'businessid_9', 'review_count': 1}]}, 'var_function-call-16441248379087631793': [{'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}]}

exec(code, env_args)
