code = """import json
import pandas as pd

biz_path = var_call_5kJVrgXIvN0Edazsc7HFYBgI
rev_path = var_call_QYZaFbgIPmrqZ0Z5w0n7PI7g

with open(biz_path, 'r') as f:
    businesses = json.load(f)
with open(rev_path, 'r') as f:
    reviews = json.load(f)

rows = []
for b in businesses:
    bid = b.get('business_id')
    desc = b.get('description') or ''
    desc = desc.strip()
    cats = set()
    if desc:
        # take last sentence
        parts = [p.strip() for p in desc.split('.') if p.strip()]
        last = parts[-1] if parts else desc
        # split by comma into segments
        segs = [s.strip() for s in last.split(',') if s.strip()]
        for s in segs:
            ls = s.lower()
            if ls.startswith('located') or ls.startswith('this') or ls.startswith('offers') or ls.startswith('provides'):
                # try to find 'including' and take after
                if 'including' in ls:
                    idx = ls.find('including')
                    cand = s[idx + len('including'):].strip() if idx != -1 else ''
                    if cand:
                        s = cand
                    else:
                        continue
                else:
                    continue
            if any(ch.isdigit() for ch in s):
                continue
            if len(s) > 80:
                continue
            # must contain at least one word starting with uppercase letter
            words = [w for w in s.split() if w]
            has_title = any(w[0].isalpha() and w[0].upper() == w[0] for w in words)
            if not has_title:
                continue
            # remove leading articles
            if s.lower().startswith('the '):
                s = s[4:]
            if s.lower().startswith('a '):
                s = s[2:]
            s = s.strip("' \"")
            if s:
                cats.add(s)
    rows.append({'business_id': bid, 'categories': list(cats)})

# build dataframe
DF = pd.DataFrame(rows)
result = {'category': None, 'business_count': 0, 'average_rating': None}
if not DF.empty:
    DF_ex = DF.explode('categories')
    if 'categories' in DF_ex.columns and not DF_ex['categories'].dropna().empty:
        DF_ex = DF_ex[DF_ex['categories'].notna()].copy()
        DF_ex['categories'] = DF_ex['categories'].str.strip()
        counts = DF_ex.groupby('categories')['business_id'].nunique().reset_index()
        counts = counts.rename(columns={'categories': 'category', 'business_id': 'business_count'})
        counts = counts.sort_values(by=['business_count', 'category'], ascending=[False, True])
        top = counts.iloc[0]
        top_cat = top['category']
        top_count = int(top['business_count'])
        biz_ids = set(DF_ex[DF_ex['categories'] == top_cat]['business_id'].unique())

        # reviews
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
        if not df_r_cat.empty:
            avg = round(float(df_r_cat['rating'].mean()), 2)
        else:
            avg = None
        result = {'category': top_cat, 'business_count': top_count, 'average_rating': (None if avg is None else avg)}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_NeumhbNtYh7RIqIMjxGLdY3e': ['checkin', 'business'], 'var_call_yJeK0J3aYKtbIkDeETPJZWaP': ['review', 'tip', 'user'], 'var_call_5kJVrgXIvN0Edazsc7HFYBgI': 'file_storage/call_5kJVrgXIvN0Edazsc7HFYBgI.json', 'var_call_QYZaFbgIPmrqZ0Z5w0n7PI7g': 'file_storage/call_QYZaFbgIPmrqZ0Z5w0n7PI7g.json', 'var_call_YjJC0VopQuMgq5f2rYcJ7a7n': {'category': None, 'business_count': 0, 'average_rating': None}, 'var_call_5lJRX3ne1c6ql1kvUOPQTGXF': [], 'var_call_A9JencJUo1qHNPTfBWZ42ph7': 'file_storage/call_A9JencJUo1qHNPTfBWZ42ph7.json', 'var_call_uxwhrrGVHMrvMk4un5Qes1Eh': {'category': None, 'business_count': 0, 'average_rating': None}, 'var_call_sBXu0Rr5Ol9prv15c3X1Thb1': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'business_id': 'businessid_64', 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'business_id': 'businessid_52', 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.'}, {'business_id': 'businessid_29', 'description': 'Located at 41 Haddon Ave in Collingswood, NJ, this versatile establishment offers a range of services including Wedding Planning, Flowers & Gifts, Event Planning & Services, Financial Services, Shopping, and Florists.'}, {'business_id': 'businessid_10', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}, {'business_id': 'businessid_61', 'description': 'Located at 1218 Millennium Pkwy in Brandon, FL, this facility provides essential services in the categories of Medical Centers, Health & Medical.'}, {'business_id': 'businessid_54', 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'business_id': 'businessid_8', 'description': 'This Philadelphia, PA location offers a range of services including Hotels & Travel, Taxis, Transportation, Local Services, and Automotive to meet all your travel and transportation needs.'}, {'business_id': 'businessid_59', 'description': 'Located at 4403 Chestnut St in Philadelphia, PA, this vibrant spot offers a delightful mix of Food, Bubble Tea, Restaurants, Sandwiches, Vietnamese, Cafes, perfect for a casual meal or a refreshing drink.'}, {'business_id': 'businessid_91', 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}, {'business_id': 'businessid_83', 'description': 'Located at 13002 Seminole Blvd, Ste 10-11 in Largo, FL, this business specializes in Optometrists, Health & Medical, Eyewear & Opticians, Ophthalmologists, Doctors, Shopping, offering a range of eye care services and products.'}, {'business_id': 'businessid_93', 'description': 'Located at 914 Edwardsville Rd in Troy, IL, this vibrant spot offers a diverse menu featuring American (New) cuisine, along with a lively atmosphere perfect for nightlife, bars, restaurants, and sports bars.'}, {'business_id': 'businessid_1', 'description': 'Located in Pennsauken, NJ, this business specializes in Home Services, Pool & Hot Tub Service, providing expert care for all your residential maintenance needs.'}, {'business_id': 'businessid_24', 'description': 'Located at 4663 Maryland Ave in Saint Louis, MO, this delightful spot offers a tempting selection of treats in the categories of Food, Ice Cream & Frozen Yogurt.'}], 'var_call_d3hmgMApt5bTFgZrW2N6NizF': {'category': None, 'business_count': 0, 'average_rating': None}}

exec(code, env_args)
