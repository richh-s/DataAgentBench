code = """import pandas as pd
import json
import re

# Load data
review_data = locals()['var_function-call-7918765920421337806']
business_file = locals()['var_function-call-9190861179560460242']

with open(business_file, 'r') as f:
    business_data = json.load(f)

reviews_df = pd.DataFrame(review_data)
business_df = pd.DataFrame(business_data)

if not reviews_df.empty:
    reviews_df['business_id'] = reviews_df['business_ref'].str.replace('businessref_', 'businessid_')
    reviews_df['review_cnt'] = reviews_df['review_cnt'].astype(int)

merged = pd.merge(reviews_df, business_df, on='business_id', how='inner')

def extract_categories(desc):
    if not isinstance(desc, str):
        return []
    
    # Patterns
    patterns = [
        r"including\s+",
        r"services in\s+",
        r"destination for\s+",
        r"specializes in\s+",
        r"categories of\s+'?",
        r"fields of\s+",
        r"ranging from\s+",
        r"category of\s+'?"
    ]
    
    best_match = None
    best_start = -1
    
    for pat in patterns:
        # Find iter to get all matches? usually one.
        for match in re.finditer(pat, desc, re.IGNORECASE):
            if match.start() > best_start:
                best_start = match.start()
                best_match = match
    
    if not best_match:
        return []
    
    # Extract content after the match
    cats_str = desc[best_match.end():]
    
    # End markers
    end_markers = [
        ", providing", ", offering", ", making it", ", to meet", 
        " providing", " offering", " making it", " to meet",
        ", catering to", " catering to"
    ]
    
    for marker in end_markers:
        idx = cats_str.find(marker)
        if idx != -1:
            cats_str = cats_str[:idx]
            
    # Cleanup
    if cats_str.endswith('.'):
        cats_str = cats_str[:-1]
    if cats_str.endswith("'"):
        cats_str = cats_str[:-1]
    
    # "ranging from X, Y, to Z"
    # Replace ", to " with ", " only if "ranging from" was the pattern? 
    # Or generically.
    # "ranging from" pattern might be useful context.
    # If "ranging from" is the best match, handle "to".
    if "ranging from" in best_match.group(0).lower():
        # Handle the ", to " or " to " before the last item
        # Regex to replace " to " or ", to " with ", "
        cats_str = re.sub(r",?\s+to\s+", ", ", cats_str)
    
    # Split
    parts = cats_str.split(',')
    cats = []
    for i, part in enumerate(parts):
        part = part.strip()
        if i == len(parts) - 1:
            if part.lower().startswith("and "):
                part = part[4:]
        if part:
            cats.append(part)
            
    return cats

category_counts = {}

for _, row in merged.iterrows():
    cats = extract_categories(row['description'])
    cnt = row['review_cnt']
    for c in cats:
        category_counts[c] = category_counts.get(c, 0) + cnt

sorted_cats = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)

print("__RESULT__:")
print(json.dumps(sorted_cats[:10]))"""

env_args = {'var_function-call-13184127885606183163': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-13184127885606185882': [{'user_id': 'userid_286', 'name': 'Todd', 'review_count': '376', 'yelping_since': '15 Jan 2009, 16:40', 'useful': '1373', 'funny': '723', 'cool': '639', 'elite': '2010,2011,2012,2013,2014'}], 'var_function-call-2289511813020618995': [{'date': 'August 01, 2016 at 03:44 AM'}], 'var_function-call-7918765920421337806': [{'business_ref': 'businessref_79', 'review_cnt': '8'}, {'business_ref': 'businessref_44', 'review_cnt': '4'}, {'business_ref': 'businessref_13', 'review_cnt': '3'}, {'business_ref': 'businessref_6', 'review_cnt': '4'}, {'business_ref': 'businessref_71', 'review_cnt': '1'}, {'business_ref': 'businessref_91', 'review_cnt': '2'}, {'business_ref': 'businessref_46', 'review_cnt': '1'}, {'business_ref': 'businessref_1', 'review_cnt': '1'}, {'business_ref': 'businessref_47', 'review_cnt': '1'}, {'business_ref': 'businessref_16', 'review_cnt': '1'}, {'business_ref': 'businessref_55', 'review_cnt': '1'}, {'business_ref': 'businessref_9', 'review_cnt': '3'}, {'business_ref': 'businessref_74', 'review_cnt': '2'}, {'business_ref': 'businessref_25', 'review_cnt': '1'}, {'business_ref': 'businessref_66', 'review_cnt': '2'}, {'business_ref': 'businessref_29', 'review_cnt': '1'}, {'business_ref': 'businessref_39', 'review_cnt': '1'}, {'business_ref': 'businessref_67', 'review_cnt': '5'}, {'business_ref': 'businessref_15', 'review_cnt': '3'}, {'business_ref': 'businessref_33', 'review_cnt': '5'}, {'business_ref': 'businessref_81', 'review_cnt': '1'}, {'business_ref': 'businessref_36', 'review_cnt': '3'}, {'business_ref': 'businessref_12', 'review_cnt': '4'}, {'business_ref': 'businessref_60', 'review_cnt': '4'}, {'business_ref': 'businessref_89', 'review_cnt': '3'}, {'business_ref': 'businessref_17', 'review_cnt': '1'}, {'business_ref': 'businessref_43', 'review_cnt': '3'}, {'business_ref': 'businessref_31', 'review_cnt': '1'}, {'business_ref': 'businessref_99', 'review_cnt': '1'}, {'business_ref': 'businessref_53', 'review_cnt': '1'}, {'business_ref': 'businessref_51', 'review_cnt': '3'}, {'business_ref': 'businessref_37', 'review_cnt': '6'}, {'business_ref': 'businessref_57', 'review_cnt': '7'}, {'business_ref': 'businessref_8', 'review_cnt': '4'}, {'business_ref': 'businessref_56', 'review_cnt': '1'}, {'business_ref': 'businessref_62', 'review_cnt': '2'}, {'business_ref': 'businessref_86', 'review_cnt': '4'}, {'business_ref': 'businessref_97', 'review_cnt': '1'}, {'business_ref': 'businessref_72', 'review_cnt': '1'}, {'business_ref': 'businessref_85', 'review_cnt': '1'}, {'business_ref': 'businessref_42', 'review_cnt': '1'}, {'business_ref': 'businessref_40', 'review_cnt': '3'}, {'business_ref': 'businessref_7', 'review_cnt': '2'}, {'business_ref': 'businessref_92', 'review_cnt': '2'}, {'business_ref': 'businessref_61', 'review_cnt': '1'}, {'business_ref': 'businessref_88', 'review_cnt': '4'}, {'business_ref': 'businessref_21', 'review_cnt': '4'}, {'business_ref': 'businessref_26', 'review_cnt': '4'}, {'business_ref': 'businessref_68', 'review_cnt': '1'}, {'business_ref': 'businessref_4', 'review_cnt': '1'}, {'business_ref': 'businessref_23', 'review_cnt': '1'}, {'business_ref': 'businessref_41', 'review_cnt': '1'}, {'business_ref': 'businessref_10', 'review_cnt': '1'}, {'business_ref': 'businessref_45', 'review_cnt': '5'}, {'business_ref': 'businessref_82', 'review_cnt': '2'}, {'business_ref': 'businessref_76', 'review_cnt': '1'}, {'business_ref': 'businessref_14', 'review_cnt': '3'}, {'business_ref': 'businessref_3', 'review_cnt': '2'}, {'business_ref': 'businessref_96', 'review_cnt': '4'}, {'business_ref': 'businessref_98', 'review_cnt': '3'}, {'business_ref': 'businessref_22', 'review_cnt': '1'}, {'business_ref': 'businessref_20', 'review_cnt': '1'}], 'var_function-call-1067328606079441968': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-4650774661373333341': [['Beauty & Spas', 6], ['Nail Salons', 5], ['Hair Removal', 5], ['Waxing', 5], ['Gun/Rifle Ranges', 4]], 'var_function-call-16516714872070185592': {'debug': [{'bid': 'businessid_33', 'cnt': 5, 'cats': ['Nail Salons', 'Hair Removal', 'Beauty & Spas', 'Waxing'], 'desc': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, t...'}, {'bid': 'businessid_88', 'cnt': 4, 'cats': ['Gun/Rifle Ranges', 'Active Life'], 'desc': 'Located at 11655 W Executive Dr in Boise, ID, this...'}, {'bid': 'businessid_47', 'cnt': 1, 'cats': ['Hair Salons', 'Beauty & Spas', 'Hair Stylists', 'Skin Care', 'Blow Dry/Out Services', 'Makeup Artists'], 'desc': 'Located at 9916 Clayton Rd in St. Louis, MO, this ...'}, {'bid': 'businessid_41', 'cnt': 1, 'cats': ['Internal Medicine', 'Doctors', 'Health & Medical'], 'desc': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint P...'}], 'top_cats': [['Beauty & Spas', 6], ['Nail Salons', 5], ['Hair Removal', 5], ['Waxing', 5], ['Gun/Rifle Ranges', 4], ['Active Life', 4], ['Hair Salons', 1], ['Hair Stylists', 1], ['Skin Care', 1], ['Blow Dry/Out Services', 1]]}, 'var_function-call-8117212579834221731': {'collection': 'business', 'filter': {'business_id': {'$in': ['businessid_79', 'businessid_44', 'businessid_13', 'businessid_6', 'businessid_71', 'businessid_91', 'businessid_46', 'businessid_1', 'businessid_47', 'businessid_16', 'businessid_55', 'businessid_9', 'businessid_74', 'businessid_25', 'businessid_66', 'businessid_29', 'businessid_39', 'businessid_67', 'businessid_15', 'businessid_33', 'businessid_81', 'businessid_36', 'businessid_12', 'businessid_60', 'businessid_89', 'businessid_17', 'businessid_43', 'businessid_31', 'businessid_99', 'businessid_53', 'businessid_51', 'businessid_37', 'businessid_57', 'businessid_8', 'businessid_56', 'businessid_62', 'businessid_86', 'businessid_97', 'businessid_72', 'businessid_85', 'businessid_42', 'businessid_40', 'businessid_7', 'businessid_92', 'businessid_61', 'businessid_88', 'businessid_21', 'businessid_26', 'businessid_68', 'businessid_4', 'businessid_23', 'businessid_41', 'businessid_10', 'businessid_45', 'businessid_82', 'businessid_76', 'businessid_14', 'businessid_3', 'businessid_96', 'businessid_98', 'businessid_22', 'businessid_20']}}, 'projection': {'business_id': 1, 'description': 1}, 'limit': 1000}, 'var_function-call-9190861179560460242': 'file_storage/function-call-9190861179560460242.json'}

exec(code, env_args)
