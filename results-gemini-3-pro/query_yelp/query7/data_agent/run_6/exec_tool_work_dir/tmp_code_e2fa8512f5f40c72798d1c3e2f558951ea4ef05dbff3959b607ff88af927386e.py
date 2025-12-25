code = """import pandas as pd
import json

# Load data
review_data = locals()['var_function-call-7918765920421337806']
business_data = locals()['var_function-call-1067328606079441968']

if isinstance(review_data, str) and review_data.endswith('.json'):
    with open(review_data, 'r') as f:
        review_data = json.load(f)
if isinstance(business_data, str) and business_data.endswith('.json'):
    with open(business_data, 'r') as f:
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
    markers = [
        "providing a range of services in ",
        "including ",
        "destination for ",
        "offers a range of services in "
    ]
    cats_str = ""
    for m in markers:
        if m in desc:
            cats_str = desc.split(m)[-1]
            break
            
    if not cats_str:
        return []
    if cats_str.endswith('.'):
        cats_str = cats_str[:-1]
    
    parts = cats_str.split(',')
    cats = []
    for i, part in enumerate(parts):
        part = part.strip()
        if i == len(parts) - 1:
            if part.startswith("and "):
                part = part[4:]
        cats.append(part)
    return cats

# Debug: Print top businesses by review count and their extracted categories
top_biz = merged.sort_values('review_cnt', ascending=False).head(10)
debug_list = []
for _, row in top_biz.iterrows():
    cats = extract_categories(row['description'])
    debug_list.append({
        "bid": row['business_id'],
        "cnt": row['review_cnt'],
        "cats": cats,
        "desc": row['description'][:50] + "..."
    })

category_counts = {}
for _, row in merged.iterrows():
    cats = extract_categories(row['description'])
    cnt = row['review_cnt']
    for c in cats:
        if c:
            category_counts[c] = category_counts.get(c, 0) + cnt

sorted_cats = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)
result = sorted_cats[:10]

print("__RESULT__:")
print(json.dumps({"debug": debug_list, "top_cats": result}))"""

env_args = {'var_function-call-13184127885606183163': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-13184127885606185882': [{'user_id': 'userid_286', 'name': 'Todd', 'review_count': '376', 'yelping_since': '15 Jan 2009, 16:40', 'useful': '1373', 'funny': '723', 'cool': '639', 'elite': '2010,2011,2012,2013,2014'}], 'var_function-call-2289511813020618995': [{'date': 'August 01, 2016 at 03:44 AM'}], 'var_function-call-7918765920421337806': [{'business_ref': 'businessref_79', 'review_cnt': '8'}, {'business_ref': 'businessref_44', 'review_cnt': '4'}, {'business_ref': 'businessref_13', 'review_cnt': '3'}, {'business_ref': 'businessref_6', 'review_cnt': '4'}, {'business_ref': 'businessref_71', 'review_cnt': '1'}, {'business_ref': 'businessref_91', 'review_cnt': '2'}, {'business_ref': 'businessref_46', 'review_cnt': '1'}, {'business_ref': 'businessref_1', 'review_cnt': '1'}, {'business_ref': 'businessref_47', 'review_cnt': '1'}, {'business_ref': 'businessref_16', 'review_cnt': '1'}, {'business_ref': 'businessref_55', 'review_cnt': '1'}, {'business_ref': 'businessref_9', 'review_cnt': '3'}, {'business_ref': 'businessref_74', 'review_cnt': '2'}, {'business_ref': 'businessref_25', 'review_cnt': '1'}, {'business_ref': 'businessref_66', 'review_cnt': '2'}, {'business_ref': 'businessref_29', 'review_cnt': '1'}, {'business_ref': 'businessref_39', 'review_cnt': '1'}, {'business_ref': 'businessref_67', 'review_cnt': '5'}, {'business_ref': 'businessref_15', 'review_cnt': '3'}, {'business_ref': 'businessref_33', 'review_cnt': '5'}, {'business_ref': 'businessref_81', 'review_cnt': '1'}, {'business_ref': 'businessref_36', 'review_cnt': '3'}, {'business_ref': 'businessref_12', 'review_cnt': '4'}, {'business_ref': 'businessref_60', 'review_cnt': '4'}, {'business_ref': 'businessref_89', 'review_cnt': '3'}, {'business_ref': 'businessref_17', 'review_cnt': '1'}, {'business_ref': 'businessref_43', 'review_cnt': '3'}, {'business_ref': 'businessref_31', 'review_cnt': '1'}, {'business_ref': 'businessref_99', 'review_cnt': '1'}, {'business_ref': 'businessref_53', 'review_cnt': '1'}, {'business_ref': 'businessref_51', 'review_cnt': '3'}, {'business_ref': 'businessref_37', 'review_cnt': '6'}, {'business_ref': 'businessref_57', 'review_cnt': '7'}, {'business_ref': 'businessref_8', 'review_cnt': '4'}, {'business_ref': 'businessref_56', 'review_cnt': '1'}, {'business_ref': 'businessref_62', 'review_cnt': '2'}, {'business_ref': 'businessref_86', 'review_cnt': '4'}, {'business_ref': 'businessref_97', 'review_cnt': '1'}, {'business_ref': 'businessref_72', 'review_cnt': '1'}, {'business_ref': 'businessref_85', 'review_cnt': '1'}, {'business_ref': 'businessref_42', 'review_cnt': '1'}, {'business_ref': 'businessref_40', 'review_cnt': '3'}, {'business_ref': 'businessref_7', 'review_cnt': '2'}, {'business_ref': 'businessref_92', 'review_cnt': '2'}, {'business_ref': 'businessref_61', 'review_cnt': '1'}, {'business_ref': 'businessref_88', 'review_cnt': '4'}, {'business_ref': 'businessref_21', 'review_cnt': '4'}, {'business_ref': 'businessref_26', 'review_cnt': '4'}, {'business_ref': 'businessref_68', 'review_cnt': '1'}, {'business_ref': 'businessref_4', 'review_cnt': '1'}, {'business_ref': 'businessref_23', 'review_cnt': '1'}, {'business_ref': 'businessref_41', 'review_cnt': '1'}, {'business_ref': 'businessref_10', 'review_cnt': '1'}, {'business_ref': 'businessref_45', 'review_cnt': '5'}, {'business_ref': 'businessref_82', 'review_cnt': '2'}, {'business_ref': 'businessref_76', 'review_cnt': '1'}, {'business_ref': 'businessref_14', 'review_cnt': '3'}, {'business_ref': 'businessref_3', 'review_cnt': '2'}, {'business_ref': 'businessref_96', 'review_cnt': '4'}, {'business_ref': 'businessref_98', 'review_cnt': '3'}, {'business_ref': 'businessref_22', 'review_cnt': '1'}, {'business_ref': 'businessref_20', 'review_cnt': '1'}], 'var_function-call-1067328606079441968': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-4650774661373333341': [['Beauty & Spas', 6], ['Nail Salons', 5], ['Hair Removal', 5], ['Waxing', 5], ['Gun/Rifle Ranges', 4]]}

exec(code, env_args)
