code = """import json
import pandas as pd
# load previous results from storage

# var_call_CJZhxJjDQFaRCV7sYW2aJKNO: review counts per business_ref (list of dicts)
# var_call_wr9XDXAIzIsifZE2Y2eYqIkM: path to full business collection result JSON

reviews = var_call_CJZhxJjDQFaRCV7sYW2aJKNO
businesses_path = var_call_wr9XDXAIzIsifZE2Y2eYqIkM

# read full businesses JSON
with open(businesses_path, 'r') as f:
    businesses = json.load(f)

# convert to DataFrame
df_reviews = pd.DataFrame(reviews)
# convert review_count to int
df_reviews['review_count'] = df_reviews['review_count'].astype(int)

# create business_ref to business_id mapping: businessref_X -> businessid_X
# from business ids in businesses
df_businesses = pd.DataFrame(businesses)
# extract numeric id suffix

# create mapping: businessid_# -> categories pulled from description by splitting on commas and detecting categories portion
# We'll try to extract category tokens by splitting description on 'offers' or 'offers a' or 'offers a range of services in' etc.

def extract_categories(desc):
    if not isinstance(desc, str):
        return []
    # common separators
    parts = desc.split('offers')
    if len(parts) > 1:
        cat_part = parts[1]
    else:
        cat_part = desc
    # remove location phrases in parentheses etc
    # split by periods, commas, and 'in' preceding location
    # find last 'in <City,' occurrence and cut before it
    # We'll remove leading 'a', 'a range of services in', 'a diverse range of services' etc
    cat_part = cat_part.lower()
    # remove location starting with 'in ' followed by capitalized word - but lowercased now
    # split at '.'
    cat_part = cat_part.split('.')[0]
    # remove leading phrases
    for prefix in [' a range of services in ', ' a diverse range of services in ', " a diverse menu featuring ", ' a delightful array of options ranging from ', ' a delightful selection of ', ' a range of services including ', ' a variety of services including ', ' a variety of offerings including ', ' a range of services in the categories of ', " a delightful array of dishes in the category of ", ' a range of services in ', ' a range of offerings within the ']:
        if prefix in cat_part:
            cat_part = cat_part.split(prefix)[-1]
    # remove 'the categories of '
    cat_part = cat_part.replace('the categories of ', '')
    # replace '&' with comma
    cat_part = cat_part.replace('&', ',')
    # split by commas
    cats = [c.strip().title() for c in cat_part.split(',') if c.strip()]
    # further split on ' and '
    final = []
    for c in cats:
        for sub in c.split(' And '):
            sub = sub.strip()
            # remove trailing words like 'services', 'offering', 'options'
            for trailing in [' Services', ' Service', ' Options', ' Offerings', ' To Meet All Your Travel And Transportation Needs', ' To Meet All Your Vehicle Needs', ' To Meet All Your Vehicle Repair Needs']:
                if sub.endswith(trailing):
                    sub = sub[:-len(trailing)].strip()
            final.append(sub)
    # filter out location words like states, addresses by removing tokens that contain digits or 'located' or 'in '
    cleaned = [c for c in final if c and not any(ch.isdigit() for ch in c) and 'located' not in c.lower() and len(c) > 1]
    # dedupe
    seen = set()
    out = []
    for c in cleaned:
        if c not in seen:
            seen.add(c)
            out.append(c)
    return out

# build mapping dict businessid -> categories list
mapping = {}
for row in businesses:
    bid = row.get('business_id')
    desc = row.get('description')
    cats = extract_categories(desc)
    mapping[bid] = cats

# map review business_ref to business_id by replacing prefix

def ref_to_id(bref):
    if not isinstance(bref, str):
        return None
    return bref.replace('businessref_', 'businessid_')

# aggregate counts by categories
from collections import defaultdict
cat_counts = defaultdict(int)
for _, r in df_reviews.iterrows():
    bref = r['business_ref']
    cnt = int(r['review_count'])
    bid = ref_to_id(bref)
    cats = mapping.get(bid, [])
    if not cats:
        # if no categories extracted, try to use business id numeric mapping by looking up businesses list for matching id to description maybe empty
        pass
    for c in cats:
        cat_counts[c] += cnt

# convert to sorted list
cat_list = sorted(cat_counts.items(), key=lambda x: x[1], reverse=True)
# take top 5
top5 = cat_list[:5]
result = [{'category': c, 'total_reviews_from_2016_reg_users': v} for c, v in top5]

# print in required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_jIlfMLJBR3WIWOvcXSXCbxxK': ['business', 'checkin'], 'var_call_31voBn5COzGWgEPyflFkMp7n': ['review', 'tip', 'user'], 'var_call_4kwpe2e3tfn60T7RoZEpUNV8': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'business_id': 'businessid_64', 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'business_id': 'businessid_52', 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.'}, {'business_id': 'businessid_29', 'description': 'Located at 41 Haddon Ave in Collingswood, NJ, this versatile establishment offers a range of services including Wedding Planning, Flowers & Gifts, Event Planning & Services, Financial Services, Shopping, and Florists.'}], 'var_call_CJZhxJjDQFaRCV7sYW2aJKNO': [{'business_ref': 'businessref_79', 'review_count': '7'}, {'business_ref': 'businessref_57', 'review_count': '6'}, {'business_ref': 'businessref_37', 'review_count': '6'}, {'business_ref': 'businessref_45', 'review_count': '5'}, {'business_ref': 'businessref_67', 'review_count': '5'}, {'business_ref': 'businessref_21', 'review_count': '4'}, {'business_ref': 'businessref_26', 'review_count': '4'}, {'business_ref': 'businessref_96', 'review_count': '4'}, {'business_ref': 'businessref_88', 'review_count': '4'}, {'business_ref': 'businessref_14', 'review_count': '3'}, {'business_ref': 'businessref_36', 'review_count': '3'}, {'business_ref': 'businessref_13', 'review_count': '3'}, {'business_ref': 'businessref_60', 'review_count': '3'}, {'business_ref': 'businessref_43', 'review_count': '3'}, {'business_ref': 'businessref_44', 'review_count': '3'}, {'business_ref': 'businessref_15', 'review_count': '3'}, {'business_ref': 'businessref_8', 'review_count': '3'}, {'business_ref': 'businessref_98', 'review_count': '3'}, {'business_ref': 'businessref_33', 'review_count': '3'}, {'business_ref': 'businessref_89', 'review_count': '3'}, {'business_ref': 'businessref_12', 'review_count': '3'}, {'business_ref': 'businessref_40', 'review_count': '3'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_92', 'review_count': '2'}, {'business_ref': 'businessref_86', 'review_count': '2'}, {'business_ref': 'businessref_82', 'review_count': '2'}, {'business_ref': 'businessref_62', 'review_count': '2'}, {'business_ref': 'businessref_6', 'review_count': '2'}, {'business_ref': 'businessref_91', 'review_count': '2'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_71', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}, {'business_ref': 'businessref_1', 'review_count': '1'}, {'business_ref': 'businessref_85', 'review_count': '1'}, {'business_ref': 'businessref_25', 'review_count': '1'}, {'business_ref': 'businessref_4', 'review_count': '1'}, {'business_ref': 'businessref_55', 'review_count': '1'}, {'business_ref': 'businessref_7', 'review_count': '1'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_61', 'review_count': '1'}, {'business_ref': 'businessref_76', 'review_count': '1'}, {'business_ref': 'businessref_51', 'review_count': '1'}, {'business_ref': 'businessref_9', 'review_count': '1'}, {'business_ref': 'businessref_3', 'review_count': '1'}, {'business_ref': 'businessref_42', 'review_count': '1'}, {'business_ref': 'businessref_46', 'review_count': '1'}, {'business_ref': 'businessref_17', 'review_count': '1'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_99', 'review_count': '1'}, {'business_ref': 'businessref_81', 'review_count': '1'}, {'business_ref': 'businessref_29', 'review_count': '1'}, {'business_ref': 'businessref_31', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}, {'business_ref': 'businessref_22', 'review_count': '1'}, {'business_ref': 'businessref_23', 'review_count': '1'}, {'business_ref': 'businessref_41', 'review_count': '1'}], 'var_call_w9P0KR07PW5Zub8kitbIWWeA': [{'business_id': 'businessid_49'}, {'business_id': 'businessid_47'}, {'business_id': 'businessid_88'}, {'business_id': 'businessid_41'}, {'business_id': 'businessid_33'}, {'business_id': 'businessid_74'}, {'business_id': 'businessid_92'}, {'business_id': 'businessid_64'}, {'business_id': 'businessid_52'}, {'business_id': 'businessid_29'}, {'business_id': 'businessid_10'}, {'business_id': 'businessid_61'}, {'business_id': 'businessid_54'}, {'business_id': 'businessid_8'}, {'business_id': 'businessid_59'}, {'business_id': 'businessid_91'}, {'business_id': 'businessid_83'}, {'business_id': 'businessid_93'}, {'business_id': 'businessid_1'}, {'business_id': 'businessid_24'}, {'business_id': 'businessid_95'}, {'business_id': 'businessid_50'}, {'business_id': 'businessid_26'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_89'}, {'business_id': 'businessid_32'}, {'business_id': 'businessid_70'}, {'business_id': 'businessid_42'}, {'business_id': 'businessid_71'}, {'business_id': 'businessid_97'}, {'business_id': 'businessid_14'}, {'business_id': 'businessid_3'}, {'business_id': 'businessid_35'}, {'business_id': 'businessid_28'}, {'business_id': 'businessid_57'}, {'business_id': 'businessid_27'}, {'business_id': 'businessid_75'}, {'business_id': 'businessid_34'}, {'business_id': 'businessid_2'}, {'business_id': 'businessid_19'}, {'business_id': 'businessid_48'}, {'business_id': 'businessid_67'}, {'business_id': 'businessid_7'}, {'business_id': 'businessid_51'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_100'}, {'business_id': 'businessid_5'}, {'business_id': 'businessid_63'}, {'business_id': 'businessid_45'}, {'business_id': 'businessid_68'}, {'business_id': 'businessid_6'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_78'}, {'business_id': 'businessid_79'}, {'business_id': 'businessid_66'}, {'business_id': 'businessid_55'}, {'business_id': 'businessid_30'}, {'business_id': 'businessid_80'}, {'business_id': 'businessid_15'}, {'business_id': 'businessid_96'}, {'business_id': 'businessid_11'}, {'business_id': 'businessid_73'}, {'business_id': 'businessid_4'}, {'business_id': 'businessid_77'}, {'business_id': 'businessid_18'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_86'}, {'business_id': 'businessid_53'}, {'business_id': 'businessid_40'}, {'business_id': 'businessid_44'}, {'business_id': 'businessid_43'}, {'business_id': 'businessid_72'}, {'business_id': 'businessid_9'}, {'business_id': 'businessid_20'}, {'business_id': 'businessid_37'}, {'business_id': 'businessid_56'}, {'business_id': 'businessid_62'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_39'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_31'}, {'business_id': 'businessid_85'}, {'business_id': 'businessid_25'}, {'business_id': 'businessid_82'}, {'business_id': 'businessid_58'}, {'business_id': 'businessid_12'}, {'business_id': 'businessid_99'}, {'business_id': 'businessid_60'}, {'business_id': 'businessid_21'}, {'business_id': 'businessid_98'}, {'business_id': 'businessid_16'}, {'business_id': 'businessid_46'}, {'business_id': 'businessid_22'}, {'business_id': 'businessid_36'}, {'business_id': 'businessid_69'}, {'business_id': 'businessid_23'}, {'business_id': 'businessid_38'}, {'business_id': 'businessid_81'}, {'business_id': 'businessid_13'}, {'business_id': 'businessid_17'}], 'var_call_wr9XDXAIzIsifZE2Y2eYqIkM': 'file_storage/call_wr9XDXAIzIsifZE2Y2eYqIkM.json'}

exec(code, env_args)
