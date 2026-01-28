code = """import json, re
from collections import Counter

business_file = var_call_glKA8W8O9XQpL6skMLeTPrBG
with open(business_file,'r',encoding='utf-8') as f:
    businesses = json.load(f)

descs = [b.get('description','') for b in businesses]

pattern_simple = re.compile(r",\s*([A-Z]{2})\b")
pattern_in = re.compile(r"in\s+([A-Za-z .'-]+),\s*([A-Z]{2})\b")
pattern_any = re.compile(r"\b([A-Z]{2})\b")

matches_simple = []
matches_in = []
matches_any = []
for d in descs:
    ms = pattern_simple.findall(d)
    mi = pattern_in.findall(d)
    ma = pattern_any.findall(d)
    matches_simple.append(ms[0] if ms else None)
    matches_in.append(mi[0][1] if mi else None)
    # prefer simple
    matches_any.append(ma[-1] if ma else None)

cnt_simple = Counter([m for m in matches_simple if m])
cnt_in = Counter([m for m in matches_in if m])
cnt_any = Counter([m for m in matches_any if m])

out = {
    'num_desc': len(descs),
    'simple_nonnull': sum(1 for m in matches_simple if m),
    'in_nonnull': sum(1 for m in matches_in if m),
    'any_nonnull': sum(1 for m in matches_any if m),
    'top_simple': cnt_simple.most_common(5),
    'top_in': cnt_in.most_common(5),
    'top_any': cnt_any.most_common(5),
    'samples': descs[:5]
}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_glKA8W8O9XQpL6skMLeTPrBG': 'file_storage/call_glKA8W8O9XQpL6skMLeTPrBG.json', 'var_call_Yq9r2lFTFDEhJb5LK7Hi8IAf': 'file_storage/call_Yq9r2lFTFDEhJb5LK7Hi8IAf.json', 'var_call_HxpbTYuyfCLvCURVDJsrjBQ2': {'state': None, 'total_reviews': 0, 'avg_rating': None}, 'var_call_jiywuAHkAbL56fKadgid8O8i': {'nonnull_count': 0, 'unique_states': [], 'no_state_samples': ['Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.', 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.', 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.', 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.', 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.', 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.', 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.', 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.', 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.', 'Located at 41 Haddon Ave in Collingswood, NJ, this versatile establishment offers a range of services including Wedding Planning, Flowers & Gifts, Event Planning & Services, Financial Services, Shopping, and Florists.']}}

exec(code, env_args)
