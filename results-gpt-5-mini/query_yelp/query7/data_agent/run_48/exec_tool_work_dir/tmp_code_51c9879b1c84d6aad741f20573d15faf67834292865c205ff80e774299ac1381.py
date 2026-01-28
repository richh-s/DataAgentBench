code = """import json
import pandas as pd

# Load the large business query result from the file path stored in var_call_mojMXPNcJJOoHbKqwZvUYHfD
with open(var_call_mojMXPNcJJOoHbKqwZvUYHfD, 'r') as f:
    businesses = json.load(f)

reviews = var_call_3HAijxGIjCygkeM1WoD4KwOH

# Create DataFrames
df_bus = pd.DataFrame(businesses)
# ensure business_id and description present
if 'business_id' not in df_bus.columns:
    df_bus['business_id'] = df_bus.get('business_id', None)
if 'description' not in df_bus.columns:
    df_bus['description'] = df_bus.get('description', '')

# Map review business_ref to business_id by replacing prefix
for r in reviews:
    if 'business_ref' in r and isinstance(r['business_ref'], str):
        r['business_id'] = r['business_ref'].replace('businessref_', 'businessid_')
    else:
        r['business_id'] = None

# Merge reviews with businesses on business_id
df_rev = pd.DataFrame(reviews)
merged = df_rev.merge(df_bus[['business_id','description']], on='business_id', how='left')

# Function to extract categories from description
import re

def extract_categories(desc):
    if not isinstance(desc, str) or not desc:
        return []
    desc = desc.strip()
    # Try to find a keyword indicating start of category list
    keywords = ['offers a range of services in', 'offers a range of services including', 'offers a variety of services including',
                'offers a variety of services', 'offers a range of services', 'offers a diverse range of services including',
                'offers', 'specializes in', 'specializes in the fields of', 'this business offers', 'this establishment offers',
                'this facility offers', 'this location offers', 'offers a delightful selection of', 'this charming establishment offers',
                'this establishment offers a diverse selection of', 'this business specializes in']
    lowered = desc.lower()
    start = None
    for kw in keywords:
        i = lowered.find(kw)
        if i != -1:
            start = i + len(kw)
            break
    if start is not None:
        rest = desc[start:]
    else:
        # fallback: try to remove leading location/address by cutting after the first comma
        parts = desc.split(',', 1)
        rest = parts[1] if len(parts) > 1 else desc
    # Now split rest by commas
    parts = [p.strip() for p in re.split(r',|/|;| and | including | & ', rest) if p.strip()]
    # Clean parts: remove phrases that look like addresses or contain digits or 'located' or 'in '
    cats = []
    for p in parts:
        p_clean = re.sub(r'\b(in|at|located|located at)\b', '', p, flags=re.I).strip()
        # remove trailing words like 'services' or 'offers'
        p_clean = re.sub(r'\b(services|facility|establishment|business|offers|offering)\b', '', p_clean, flags=re.I).strip()
        # remove excessive whitespace and punctuation
        p_clean = re.sub(r'[^A-Za-z\s&\-\/]','', p_clean).strip()
        # Exclude short or numeric
        if len(p_clean) >= 2 and not re.search(r'\d', p_clean):
            # Title case the category
            cats.append(' '.join([w.capitalize() for w in p_clean.split()]))
    # Deduplicate while preserving order
    seen = set(); res = []
    for c in cats:
        if c and c.lower() not in seen:
            seen.add(c.lower()); res.append(c)
    return res

# Apply extraction
merged['categories'] = merged['description'].apply(extract_categories)

# For each review, count one for each category
from collections import Counter
counter = Counter()
for idx, row in merged.iterrows():
    cats = row['categories']
    if not cats:
        continue
    for c in cats:
        counter[c] += 1

# Get top 5 categories
top5 = counter.most_common(5)
output = [{'category': c, 'reviews': n} for c,n in top5]

# If no categories found (edge case), return empty list
import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_8YpWJtUUgj6SvNQW5X94CYMF': ['checkin', 'business'], 'var_call_ihRZ7c0EV85dyWpmIRVNXZ85': ['review', 'tip', 'user'], 'var_call_R4yjFntyd376N25DbC36AbGX': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64', 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52', 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.'}, {'_id': '6859a000fe8b31cd7362e2b4', 'business_id': 'businessid_29', 'description': 'Located at 41 Haddon Ave in Collingswood, NJ, this versatile establishment offers a range of services including Wedding Planning, Flowers & Gifts, Event Planning & Services, Financial Services, Shopping, and Florists.'}], 'var_call_khwGGxCHW3Og5hpAR99FsfqF': [{'user_id': 'userid_746'}, {'user_id': 'userid_1109'}, {'user_id': 'userid_1950'}, {'user_id': 'userid_1316'}, {'user_id': 'userid_1182'}, {'user_id': 'userid_151'}, {'user_id': 'userid_1158'}, {'user_id': 'userid_508'}, {'user_id': 'userid_435'}, {'user_id': 'userid_958'}, {'user_id': 'userid_1879'}, {'user_id': 'userid_308'}, {'user_id': 'userid_1179'}, {'user_id': 'userid_324'}, {'user_id': 'userid_863'}, {'user_id': 'userid_100'}, {'user_id': 'userid_1333'}, {'user_id': 'userid_1636'}, {'user_id': 'userid_1850'}, {'user_id': 'userid_711'}, {'user_id': 'userid_729'}, {'user_id': 'userid_1505'}, {'user_id': 'userid_1315'}, {'user_id': 'userid_1708'}, {'user_id': 'userid_1661'}, {'user_id': 'userid_850'}, {'user_id': 'userid_1675'}, {'user_id': 'userid_227'}, {'user_id': 'userid_577'}, {'user_id': 'userid_257'}, {'user_id': 'userid_598'}, {'user_id': 'userid_847'}, {'user_id': 'userid_673'}, {'user_id': 'userid_1856'}, {'user_id': 'userid_384'}, {'user_id': 'userid_935'}, {'user_id': 'userid_210'}, {'user_id': 'userid_1101'}, {'user_id': 'userid_945'}, {'user_id': 'userid_842'}, {'user_id': 'userid_1351'}, {'user_id': 'userid_230'}, {'user_id': 'userid_593'}, {'user_id': 'userid_1431'}, {'user_id': 'userid_686'}, {'user_id': 'userid_527'}, {'user_id': 'userid_244'}, {'user_id': 'userid_393'}, {'user_id': 'userid_1178'}, {'user_id': 'userid_526'}, {'user_id': 'userid_90'}, {'user_id': 'userid_238'}, {'user_id': 'userid_1105'}], 'var_call_mojMXPNcJJOoHbKqwZvUYHfD': 'file_storage/call_mojMXPNcJJOoHbKqwZvUYHfD.json', 'var_call_3HAijxGIjCygkeM1WoD4KwOH': [{'business_ref': 'businessref_74', 'date': '2021-07-16 17:24:00'}, {'business_ref': 'businessref_57', 'date': 'September 04, 2017 at 08:57 PM'}, {'business_ref': 'businessref_96', 'date': 'August 06, 2016 at 02:19 AM'}, {'business_ref': 'businessref_45', 'date': 'August 10, 2016 at 04:36 AM'}, {'business_ref': 'businessref_74', 'date': 'April 17, 2016 at 12:00 AM'}, {'business_ref': 'businessref_53', 'date': '25 Nov 2016, 20:04'}, {'business_ref': 'businessref_41', 'date': 'December 12, 2017 at 02:27 AM'}, {'business_ref': 'businessref_96', 'date': '2017-01-06 11:15:06'}, {'business_ref': 'businessref_10', 'date': '2021-11-28 23:56:00'}, {'business_ref': 'businessref_66', 'date': 'November 10, 2021 at 06:40 AM'}, {'business_ref': 'businessref_31', 'date': '24 Jan 2017, 19:28'}, {'business_ref': 'businessref_92', 'date': '2019-11-14 17:06:00'}, {'business_ref': 'businessref_26', 'date': '2018-07-23 06:45:43'}, {'business_ref': 'businessref_98', 'date': '2017-11-17 16:06:00'}, {'business_ref': 'businessref_45', 'date': 'February 06, 2018 at 07:29 PM'}, {'business_ref': 'businessref_45', 'date': 'October 28, 2016 at 03:54 PM'}, {'business_ref': 'businessref_36', 'date': '2018-05-21 17:51:00'}, {'business_ref': 'businessref_14', 'date': 'May 04, 2017 at 11:25 PM'}, {'business_ref': 'businessref_86', 'date': '2019-04-14 23:08:41'}, {'business_ref': 'businessref_57', 'date': 'October 30, 2018 at 01:06 PM'}, {'business_ref': 'businessref_13', 'date': 'August 22, 2021 at 12:11 AM'}, {'business_ref': 'businessref_68', 'date': 'October 14, 2018 at 04:06 PM'}, {'business_ref': 'businessref_36', 'date': '2016-12-02 00:06:00'}, {'business_ref': 'businessref_60', 'date': '2017-03-24 23:59:00'}, {'business_ref': 'businessref_20', 'date': '27 May 2017, 00:50'}, {'business_ref': 'businessref_15', 'date': 'June 20, 2018 at 02:12 PM'}, {'business_ref': 'businessref_62', 'date': '2018-04-01 10:52:37'}, {'business_ref': 'businessref_33', 'date': 'August 18, 2016 at 11:57 AM'}, {'business_ref': 'businessref_37', 'date': '2016-07-24 20:27:00'}, {'business_ref': 'businessref_92', 'date': '30 Dec 2018, 18:49'}, {'business_ref': 'businessref_66', 'date': 'June 21, 2020 at 07:59 PM'}, {'business_ref': 'businessref_33', 'date': 'August 30, 2019 at 06:15 PM'}, {'business_ref': 'businessref_6', 'date': '30 Jun 2017, 04:44'}, {'business_ref': 'businessref_12', 'date': 'October 26, 2017 at 11:10 PM'}, {'business_ref': 'businessref_79', 'date': '30 Oct 2017, 01:27'}, {'business_ref': 'businessref_60', 'date': '2019-05-29 19:46:00'}]}

exec(code, env_args)
