code = """import json
import pandas as pd
import re

# Read the full data from the files
with open('functions.query_db_10', 'r') as f:
    businesses = json.load(f)

with open('functions.query_db_12', 'r') as f:
    reviews = json.load(f)

# Convert to DataFrames
df_business = pd.DataFrame(businesses)
df_reviews = pd.DataFrame(reviews)

# Standardize the IDs by removing prefixes
df_business['business_id_clean'] = df_business['business_id'].str.replace('businessid_', '')
df_reviews['business_id_clean'] = df_reviews['business_ref'].str.replace('businessref_', '')

# Filter businesses that accept credit cards
accepts_cc = []
for _, row in df_business.iterrows():
    attrs = row['attributes']
    is_cc = False
    if isinstance(attrs, dict) and attrs.get('BusinessAcceptsCreditCards'):
        if str(attrs['BusinessAcceptsCreditCards']).lower() == 'true':
            is_cc = True
    accepts_cc.append(is_cc)

df_business['accepts_cc'] = accepts_cc
cc_businesses = df_business[df_business['accepts_cc']].copy()

# Extract categories from descriptions
def get_categories(desc):
    if not desc or pd.isna(desc):
        return []
    cats = []
    
    # Pattern for "services in A, B, and C"
    m1 = re.search(r'services in (.+?)(?:\.|, providing|$)', desc, re.I)
    if m1:
        parts = re.split(r',\s*|\sand\s', m1.group(1))
        cats.extend([p.strip() for p in parts if p.strip()])
    
    # Pattern for "category of 'X, Y'"
    m2 = re.search(r"category of '(.+?)'", desc, re.I)
    if m2:
        parts = re.split(r',\s*', m2.group(1))
        cats.extend([p.strip() for p in parts if p.strip()])
    
    # Pattern for "fields of X, Y"
    m3 = re.search(r'fields of (.+?)(?:\.|, making|$)', desc, re.I)
    if m3:
        parts = re.split(r',\s*', m3.group(1))
        cats.extend([p.strip() for p in parts if p.strip()])
    
    return [c for c in cats if len(c) > 2]

cc_businesses['categories'] = cc_businesses['description'].apply(get_categories)

# Count businesses per category
cat_counts = {}
cat_biz_ids = {}

for _, row in cc_businesses.iterrows():
    biz_id = row['business_id_clean']
    for cat in row['categories']:
        cat_counts[cat] = cat_counts.get(cat, 0) + 1
        if cat not in cat_biz_ids:
            cat_biz_ids[cat] = []
        cat_biz_ids[cat].append(biz_id)

# Find top category
if cat_counts:
    top_cat = max(cat_counts.items(), key=lambda x: x[1])
    top_cat_name = top_cat[0]
    top_cat_count = top_cat[1]
    
    # Get ratings for businesses in top category
    top_biz_ids = cat_biz_ids[top_cat_name]
    top_ratings = df_reviews[df_reviews['business_id_clean'].isin(top_biz_ids)]['rating'].astype(float)
    avg_rating = top_ratings.mean() if len(top_ratings) > 0 else 0
    
    result = {
        'top_category': top_cat_name,
        'business_count': int(top_cat_count),
        'average_rating': round(float(avg_rating), 2)
    }
else:
    result = {'top_category': None, 'business_count': 0, 'average_rating': 0}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['business', 'checkin'], 'var_functions.query_db:2': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'attributes': 'None'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['review', 'tip', 'user'], 'var_functions.query_db:8': [{'review_id': 'reviewid_135', 'user_id': 'userid_548', 'business_ref': 'businessref_34', 'rating': '2', 'useful': '0', 'funny': '0', 'cool': '0', 'text': "Sure, it's cheap, but there isn't much to see. I think you'd have to have a big interest in the topic to find it exciting, and kids would be bored. I think it only lasted maybe 10-15 minutes. Our tour person was somewhat knowledgeable and seemed into it, but he didn't give us much time to read the information on each level. I had to take photos of the plaques to read later, and half of them need replacing, as they are so sun-bleached they're virtually unreadable (tour guide said they're being replaced soon and that the other half were already replaced). I really thought it needed to be higher up to give a good view. The Lewis and Clark State Historic Site just down the road was more interesting and free. If you live around here like I do and have nothing better to do, you might want to give it a go if the topic interests you, but if you're a tourist, this is not something you should waste your time on.", 'date': 'August 01, 2016 at 03:44 AM'}, {'review_id': 'reviewid_1067', 'user_id': 'userid_213', 'business_ref': 'businessref_89', 'rating': '5', 'useful': '2', 'funny': '0', 'cool': '0', 'text': 'Very good service but a little pricey for the services your receive. Clean and sanitary too', 'date': 'June 14, 2021 at 11:39 AM'}, {'review_id': 'reviewid_871', 'user_id': 'userid_616', 'business_ref': 'businessref_82', 'rating': '4', 'useful': '0', 'funny': '0', 'cool': '0', 'text': 'My friend and I enjoyed a fantastic meal at Miles Table and I can\'t wait to return! Given that it was half-price-burger-day, I felt the need to give the falafel burger a shot. It was delicious! I\'m not always a falafel fan, but this "burger" was awesome. The brioche bun was the perfect consistency and the portion of fries was plentiful. My friend enjoyed the cobb salad (though she requested balsamic dressing instead of buttermilk and she received buttermilk). The restaurant is quaint and has ample seating. While you order at the counter, our "server" (I believe her name was Sarah) was fantastic and made sure we had everything we needed. Overall, this is a great spot and I will be back soon...I may have to make it a weekly lunch staple!', 'date': '29 May 2013, 23:01'}, {'review_id': 'reviewid_314', 'user_id': 'userid_1903', 'business_ref': 'businessref_66', 'rating': '2', 'useful': '1', 'funny': '2', 'cool': '1', 'text': "This location is not one of my favorites people here get pretty rude sometimes no one looks happy it's hit or miss with the food sometimes it's awesome other times terrible I always get honey walnut shrimp for an extra 1.25 which is retarded and Beijing beef I enjoy the rice n the noodles but idk do if u dare", 'date': '21 May 2016, 18:48'}, {'review_id': 'reviewid_487', 'user_id': 'None', 'business_ref': 'businessref_95', 'rating': '1', 'useful': '0', 'funny': '0', 'cool': '0', 'text': 'Terrible service. I was charged twice for online order and they refused to refund me. Numerous times this has happened', 'date': 'November 01, 2021 at 05:11 PM'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
