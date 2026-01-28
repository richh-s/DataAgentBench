code = """import json
import pandas as pd
import re

businesses_path = var_call_5kJVrgXIvN0Edazsc7HFYBgI
reviews_path = var_call_QYZaFbgIPmrqZ0Z5w0n7PI7g

with open(businesses_path, 'r') as f:
    businesses = json.load(f)
with open(reviews_path, 'r') as f:
    reviews = json.load(f)

rows = []
for doc in businesses:
    bid = doc.get('business_id')
    desc = (doc.get('description') or '').strip()
    cats = []
    if desc:
        # split by comma, drop fragments that look like addresses (contain digits)
        frags = [f.strip() for f in desc.split(',') if f.strip()]
        frags = [f for f in frags if not re.search(r'\d', f)]
        for frag in frags:
            # split by 'including' or 'including:' to get list
            if 'including' in frag.lower():
                frag = frag[frag.lower().find('including') + len('including'):].strip()
            # split by phrases 'offers', 'offers a', 'offers a range', 'this establishment offers', 'this business specializes in'
            for marker in ['offers a range of services in', 'offers a wide range of services', 'offers a range of services', 'offers a range', 'offers a diverse range of services and products in', 'offers', 'this establishment offers', 'this business specializes in', 'this business offers', 'specializes in', 'specialises in', 'provides services in', 'provides', 'in the category of']:
                il = frag.lower()
                if marker in il:
                    frag = frag[il.find(marker) + len(marker):].strip()
                    break
            # now split frag by ' and ' and '&' and '/'
            parts = re.split(r'\band\b|&|/', frag)
            for p in parts:
                p = p.strip()
                if not p:
                    continue
                # remove leading words until a word starts with uppercase (title case) or contains '&'
                words = p.split()
                i = 0
                while i < len(words) and not re.match(r'[A-Z0-9]', words[i][0]):
                    i += 1
                candidate = ' '.join(words[i:]) if i < len(words) else p
                candidate = candidate.strip(" '\"")
                # filter out if empty, contains digits, or too long
                if not candidate:
                    continue
                if re.search(r'\d', candidate):
                    continue
                if len(candidate) > 80:
                    continue
                # remove trailing generic phrases
                candidate = re.sub(r'\b(to meet all your.*|making it a.*|perfect for.*|to provide.*)$', '', candidate, flags=re.IGNORECASE).strip()
                if candidate:
                    cats.append(candidate)
    # dedupe preserve order
    seen = set()
    unique = []
    for c in cats:
        if c not in seen:
            seen.add(c)
            unique.append(c)
    rows.append({'business_id': bid, 'categories': unique})

# Build dataframe

df = pd.DataFrame(rows)
if df.empty:
    result = {"category": None, "business_count": 0, "average_rating": None}
else:
    df_ex = df.explode('categories')
    if 'categories' not in df_ex.columns or df_ex['categories'].dropna().empty:
        result = {"category": None, "business_count": 0, "average_rating": None}
    else:
        df_ex = df_ex[df_ex['categories'].notna()]
        df_ex['categories'] = df_ex['categories'].str.strip()
        cat_counts = df_ex.groupby('categories')['business_id'].nunique().reset_index()
        cat_counts = cat_counts.rename(columns={'categories':'category','business_id':'business_count'})
        cat_counts = cat_counts.sort_values(by=['business_count','category'], ascending=[False, True])
        top = cat_counts.iloc[0]
        top_category = top['category']
        top_count = int(top['business_count'])
        biz_ids = set(df_ex[df_ex['categories']==top_category]['business_id'].unique())

        # process reviews
        df_r = pd.DataFrame(reviews)
        if 'rating' in df_r.columns:
            df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
        else:
            df_r['rating'] = pd.Series(dtype='float')
        if 'business_ref' in df_r.columns:
            df_r['business_id'] = df_r['business_ref'].apply(lambda x: x.replace('businessref_','businessid_') if isinstance(x, str) else None)
        else:
            df_r['business_id'] = None
        df_r_cat = df_r[df_r['business_id'].isin(biz_ids)]
        if df_r_cat.empty:
            avg = None
        else:
            avg = round(float(df_r_cat['rating'].mean()), 2)
        result = {"category": top_category, "business_count": top_count, "average_rating": (None if avg is None else avg)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_NeumhbNtYh7RIqIMjxGLdY3e': ['checkin', 'business'], 'var_call_yJeK0J3aYKtbIkDeETPJZWaP': ['review', 'tip', 'user'], 'var_call_5kJVrgXIvN0Edazsc7HFYBgI': 'file_storage/call_5kJVrgXIvN0Edazsc7HFYBgI.json', 'var_call_QYZaFbgIPmrqZ0Z5w0n7PI7g': 'file_storage/call_QYZaFbgIPmrqZ0Z5w0n7PI7g.json', 'var_call_YjJC0VopQuMgq5f2rYcJ7a7n': {'category': None, 'business_count': 0, 'average_rating': None}, 'var_call_5lJRX3ne1c6ql1kvUOPQTGXF': [], 'var_call_A9JencJUo1qHNPTfBWZ42ph7': 'file_storage/call_A9JencJUo1qHNPTfBWZ42ph7.json', 'var_call_uxwhrrGVHMrvMk4un5Qes1Eh': {'category': None, 'business_count': 0, 'average_rating': None}, 'var_call_sBXu0Rr5Ol9prv15c3X1Thb1': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'business_id': 'businessid_64', 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'business_id': 'businessid_52', 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.'}, {'business_id': 'businessid_29', 'description': 'Located at 41 Haddon Ave in Collingswood, NJ, this versatile establishment offers a range of services including Wedding Planning, Flowers & Gifts, Event Planning & Services, Financial Services, Shopping, and Florists.'}, {'business_id': 'businessid_10', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}, {'business_id': 'businessid_61', 'description': 'Located at 1218 Millennium Pkwy in Brandon, FL, this facility provides essential services in the categories of Medical Centers, Health & Medical.'}, {'business_id': 'businessid_54', 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'business_id': 'businessid_8', 'description': 'This Philadelphia, PA location offers a range of services including Hotels & Travel, Taxis, Transportation, Local Services, and Automotive to meet all your travel and transportation needs.'}, {'business_id': 'businessid_59', 'description': 'Located at 4403 Chestnut St in Philadelphia, PA, this vibrant spot offers a delightful mix of Food, Bubble Tea, Restaurants, Sandwiches, Vietnamese, Cafes, perfect for a casual meal or a refreshing drink.'}, {'business_id': 'businessid_91', 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}, {'business_id': 'businessid_83', 'description': 'Located at 13002 Seminole Blvd, Ste 10-11 in Largo, FL, this business specializes in Optometrists, Health & Medical, Eyewear & Opticians, Ophthalmologists, Doctors, Shopping, offering a range of eye care services and products.'}, {'business_id': 'businessid_93', 'description': 'Located at 914 Edwardsville Rd in Troy, IL, this vibrant spot offers a diverse menu featuring American (New) cuisine, along with a lively atmosphere perfect for nightlife, bars, restaurants, and sports bars.'}, {'business_id': 'businessid_1', 'description': 'Located in Pennsauken, NJ, this business specializes in Home Services, Pool & Hot Tub Service, providing expert care for all your residential maintenance needs.'}, {'business_id': 'businessid_24', 'description': 'Located at 4663 Maryland Ave in Saint Louis, MO, this delightful spot offers a tempting selection of treats in the categories of Food, Ice Cream & Frozen Yogurt.'}], 'var_call_d3hmgMApt5bTFgZrW2N6NizF': {'category': None, 'business_count': 0, 'average_rating': None}}

exec(code, env_args)
