code = """import json
import re
import pandas as pd

businesses_path = var_call_5kJVrgXIvN0Edazsc7HFYBgI
reviews_path = var_call_QYZaFbgIPmrqZ0Z5w0n7PI7g

with open(businesses_path, 'r') as f:
    businesses = json.load(f)
with open(reviews_path, 'r') as f:
    reviews = json.load(f)

triggers = [
    'offers a diverse range of services and products in',
    'offers a range of services in the fields of',
    'offers a wide range of services, including',
    'offers a wide range of services including',
    'offers a range of services including',
    'offers a range of services and products in',
    'in the category of',
    'in the categories of',
    'in the category',
    'categories of',
    'this business specializes in',
    'specializes in',
    'specialises in',
    'this business offers',
    'offers a variety of services including',
    'offers a variety of services',
    'offers a range of services',
    'offers a range',
    'offers',
    'including',
    'provides',
    'provides services in',
    'in the fields of',
    'in the fields',
    'in',
]

pattern = re.compile(r'(?i)(?:' + '|'.join(re.escape(t) for t in triggers) + r')\s*[:\-\s]*')

rows = []
for doc in businesses:
    bid = doc.get('business_id')
    desc = doc.get('description') or ''
    desc = desc.strip()
    cats = []
    if desc:
        # find last match of pattern
        last_match = None
        for m in pattern.finditer(desc):
            last_match = m
        if last_match:
            seg = desc[last_match.end():]
        else:
            seg = desc
        # take up to first sentence terminator
        seg = re.split(r'[\.\!\?]', seg)[0]
        # remove any leading location fragments like 'Located at ...,' if still present
        seg = re.sub(r'^[Ll]ocated at[^,\.]*[,\.\s]*', '', seg).strip()
        # truncate at phrases like 'to meet' or 'for all your' or 'making it' to avoid long tails
        seg = re.split(r'\b(to meet|making it|to provide|to serve|for all your|perfect for|making it a|ideal for)\b', seg)[0].strip()
        # split into candidate tokens
        parts = re.split(r',|/|;|\||\band\b|\s&\s', seg)
        for p in parts:
            p = p.strip()
            if not p:
                continue
            # remove parenthesis
            p = re.sub(r"\(.*?\)", '', p).strip()
            # strip surrounding quotes and whitespace
            p = p.strip("'\" ")
            # remove leading generic phrases
            p = re.sub(r'^(this establishment|this business|this facility|the establishment|the business|the facility)\s+', '', p, flags=re.IGNORECASE).strip()
            p = re.sub(r'^(offers a range of services in|offers a variety of services in|offers a range of services|offers a variety of services)\s+', '', p, flags=re.IGNORECASE).strip()
            # remove trailing generics
            p = re.sub(r'\s*(and more|and services|and products)$', '', p, flags=re.IGNORECASE).strip()
            # filter out addresses or long phrases containing digits or address words
            lower = p.lower()
            if not p:
                continue
            if any(ch.isdigit() for ch in p):
                continue
            if any(addr in lower for addr in ['ste ', 'suite', 'blvd', 'road', 'rd', 'ave', 'street', 'lane', 'hwy', 'drive', 'pkwy', 'highway']):
                continue
            if len(p) > 80:
                continue
            cats.append(p)
    # dedupe preserve order
    seen = set()
    cats_u = []
    for c in cats:
        if c not in seen:
            seen.add(c)
            cats_u.append(c)
    rows.append({'business_id': bid, 'categories': cats_u})

# Build DataFrame and explode
df = pd.DataFrame(rows)
if df.empty:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    df_ex = df.explode('categories')
    if 'categories' not in df_ex.columns or df_ex['categories'].dropna().empty:
        result = {'category': None, 'business_count': 0, 'average_rating': None}
    else:
        df_ex = df_ex[df_ex['categories'].notna()]
        df_ex['categories'] = df_ex['categories'].str.strip()
        # normalize some ampersands
        df_ex['categories'] = df_ex['categories'].str.replace('&', '&', regex=False)
        # count unique businesses per category
        cat_counts = df_ex.groupby('categories')['business_id'].nunique().reset_index()
        cat_counts = cat_counts.rename(columns={'categories': 'category', 'business_id': 'business_count'})
        cat_counts = cat_counts.sort_values(by=['business_count', 'category'], ascending=[False, True])
        top = cat_counts.iloc[0]
        top_category = top['category']
        top_count = int(top['business_count'])
        biz_ids = set(df_ex[df_ex['categories'] == top_category]['business_id'].unique())

        # process reviews
        df_r = pd.DataFrame(reviews)
        if 'rating' in df_r.columns:
            df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
        else:
            df_r['rating'] = pd.Series(dtype='float')
        if 'business_ref' in df_r.columns:
            df_r['business_id'] = df_r['business_ref'].apply(lambda x: x.replace('businessref_', 'businessid_') if isinstance(x, str) else None)
        else:
            df_r['business_id'] = None
        df_r_cat = df_r[df_r['business_id'].isin(biz_ids)]
        if df_r_cat.empty:
            avg = None
        else:
            avg = round(float(df_r_cat['rating'].mean()), 2)
        result = {'category': top_category, 'business_count': top_count, 'average_rating': (None if avg is None else avg)}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_NeumhbNtYh7RIqIMjxGLdY3e': ['checkin', 'business'], 'var_call_yJeK0J3aYKtbIkDeETPJZWaP': ['review', 'tip', 'user'], 'var_call_5kJVrgXIvN0Edazsc7HFYBgI': 'file_storage/call_5kJVrgXIvN0Edazsc7HFYBgI.json', 'var_call_QYZaFbgIPmrqZ0Z5w0n7PI7g': 'file_storage/call_QYZaFbgIPmrqZ0Z5w0n7PI7g.json', 'var_call_YjJC0VopQuMgq5f2rYcJ7a7n': {'category': None, 'business_count': 0, 'average_rating': None}, 'var_call_5lJRX3ne1c6ql1kvUOPQTGXF': [], 'var_call_A9JencJUo1qHNPTfBWZ42ph7': 'file_storage/call_A9JencJUo1qHNPTfBWZ42ph7.json', 'var_call_uxwhrrGVHMrvMk4un5Qes1Eh': {'category': None, 'business_count': 0, 'average_rating': None}, 'var_call_sBXu0Rr5Ol9prv15c3X1Thb1': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'business_id': 'businessid_64', 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'business_id': 'businessid_52', 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.'}, {'business_id': 'businessid_29', 'description': 'Located at 41 Haddon Ave in Collingswood, NJ, this versatile establishment offers a range of services including Wedding Planning, Flowers & Gifts, Event Planning & Services, Financial Services, Shopping, and Florists.'}, {'business_id': 'businessid_10', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}, {'business_id': 'businessid_61', 'description': 'Located at 1218 Millennium Pkwy in Brandon, FL, this facility provides essential services in the categories of Medical Centers, Health & Medical.'}, {'business_id': 'businessid_54', 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'business_id': 'businessid_8', 'description': 'This Philadelphia, PA location offers a range of services including Hotels & Travel, Taxis, Transportation, Local Services, and Automotive to meet all your travel and transportation needs.'}, {'business_id': 'businessid_59', 'description': 'Located at 4403 Chestnut St in Philadelphia, PA, this vibrant spot offers a delightful mix of Food, Bubble Tea, Restaurants, Sandwiches, Vietnamese, Cafes, perfect for a casual meal or a refreshing drink.'}, {'business_id': 'businessid_91', 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}, {'business_id': 'businessid_83', 'description': 'Located at 13002 Seminole Blvd, Ste 10-11 in Largo, FL, this business specializes in Optometrists, Health & Medical, Eyewear & Opticians, Ophthalmologists, Doctors, Shopping, offering a range of eye care services and products.'}, {'business_id': 'businessid_93', 'description': 'Located at 914 Edwardsville Rd in Troy, IL, this vibrant spot offers a diverse menu featuring American (New) cuisine, along with a lively atmosphere perfect for nightlife, bars, restaurants, and sports bars.'}, {'business_id': 'businessid_1', 'description': 'Located in Pennsauken, NJ, this business specializes in Home Services, Pool & Hot Tub Service, providing expert care for all your residential maintenance needs.'}, {'business_id': 'businessid_24', 'description': 'Located at 4663 Maryland Ave in Saint Louis, MO, this delightful spot offers a tempting selection of treats in the categories of Food, Ice Cream & Frozen Yogurt.'}]}

exec(code, env_args)
