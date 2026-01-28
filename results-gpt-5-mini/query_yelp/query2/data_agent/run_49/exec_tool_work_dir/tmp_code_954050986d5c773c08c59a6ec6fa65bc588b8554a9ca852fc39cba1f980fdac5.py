code = """import json, re

def load_var(v):
    if isinstance(v, str):
        with open(v,'r') as f:
            return json.load(f)
    return v

business_records = load_var(var_call_2zESRXQokhF5Lf5iMBJbnpbn)
review_records = load_var(var_call_iTkaQoBL33XRjP3WrF6keht3)

states = set(['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY'])

bizref_to_state = {}

# patterns to try
patterns = [
    re.compile(r',\s*([A-Z]{2})(?:\b|[,\.])'),
    re.compile(r'in\s+[^,]+,\s*([A-Z]{2})(?:\b|[,\.])', re.IGNORECASE),
    re.compile(r'\b([A-Z]{2})\s+location', re.IGNORECASE),
]

for b in business_records:
    bid = b.get('business_id')
    desc = (b.get('description') or '')
    if not bid:
        continue
    if bid.startswith('businessid_'):
        bref = 'businessref_' + bid.split('businessid_')[-1]
    else:
        bref = bid
    found = None
    for pat in patterns:
        m = pat.search(desc)
        if m:
            g = m.group(1).upper()
            if g in states:
                found = g
                break
    # fallback: search for ' City, ST' anywhere
    if not found:
        m = re.search(r',\s*([A-Za-z]{2})[,\.]', desc)
        if m:
            g = m.group(1).upper()
            if g in states:
                found = g
    if found:
        bizref_to_state[bref] = found

# aggregate reviews
from collections import defaultdict
state_counts = defaultdict(int)
state_rating_sums = defaultdict(float)

for r in review_records:
    bref = r.get('business_ref')
    if not bref:
        continue
    try:
        rating = float(r.get('rating'))
    except:
        continue
    st = bizref_to_state.get(bref)
    if st:
        state_counts[st] += 1
        state_rating_sums[st] += rating

if not state_counts:
    result = {"state": None, "total_reviews": 0, "average_rating": None}
else:
    max_state = max(state_counts.items(), key=lambda x: x[1])[0]
    total = state_counts[max_state]
    avg = state_rating_sums[max_state] / total if total>0 else None
    if avg is not None:
        avg = round(avg, 3)
    result = {"state": max_state, "total_reviews": total, "average_rating": avg}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_5WRzRpXAfI3DswmAJC6LyAJg': ['business', 'checkin'], 'var_call_TswX3NFH0hPFBvda8Rluvpwq': ['review', 'tip', 'user'], 'var_call_2YqDNDO27mXYKnAbO6OxgAPy': 'file_storage/call_2YqDNDO27mXYKnAbO6OxgAPy.json', 'var_call_2zESRXQokhF5Lf5iMBJbnpbn': 'file_storage/call_2zESRXQokhF5Lf5iMBJbnpbn.json', 'var_call_iTkaQoBL33XRjP3WrF6keht3': 'file_storage/call_iTkaQoBL33XRjP3WrF6keht3.json', 'var_call_vQpg8ij8b9x9OXwsuP3Q28Oq': {'state': None, 'total_reviews': 0, 'average_rating': None}, 'var_call_XWg3IBCtyJa56pviinmx3e1c': {'total_business_records': 100, 'mapped_businesses': 0, 'sample_mapped_items': [], 'sample_no_state': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a ra'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, '}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Range'}, {'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Me'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Ha'}, {'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treat'}, {'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in th'}, {'business_id': 'businessid_64', 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & S'}, {'business_id': 'businessid_52', 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home'}, {'business_id': 'businessid_29', 'description': 'Located at 41 Haddon Ave in Collingswood, NJ, this versatile establishment offers a range of services including Wedding '}], 'sample_review_refs': ['businessref_34', 'businessref_89', 'businessref_82', 'businessref_66', 'businessref_95', 'businessref_24', 'businessref_40', 'businessref_47', 'businessref_16', 'businessref_96', 'businessref_46', 'businessref_21', 'businessref_9', 'businessref_26', 'businessref_96', 'businessref_43', 'businessref_68', 'businessref_24', 'businessref_22', 'businessref_57']}, 'var_call_6L5qqLzfNmLphCjFdgyyHKVL': [{'business_id': 'businessid_49', 'desc': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.', 'tokens': []}, {'business_id': 'businessid_47', 'desc': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.', 'tokens': []}, {'business_id': 'businessid_88', 'desc': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.', 'tokens': []}, {'business_id': 'businessid_41', 'desc': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.', 'tokens': []}, {'business_id': 'businessid_33', 'desc': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.', 'tokens': []}, {'business_id': 'businessid_74', 'desc': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.', 'tokens': []}, {'business_id': 'businessid_92', 'desc': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.', 'tokens': []}, {'business_id': 'businessid_64', 'desc': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.', 'tokens': []}, {'business_id': 'businessid_52', 'desc': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.', 'tokens': []}, {'business_id': 'businessid_29', 'desc': 'Located at 41 Haddon Ave in Collingswood, NJ, this versatile establishment offers a range of services including Wedding Planning, Flowers & Gifts, Event Planning & Services, Financial Services, Shopping, and Florists.', 'tokens': []}, {'business_id': 'businessid_10', 'desc': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'.", 'tokens': []}, {'business_id': 'businessid_61', 'desc': 'Located at 1218 Millennium Pkwy in Brandon, FL, this facility provides essential services in the categories of Medical Centers, Health & Medical.', 'tokens': []}, {'business_id': 'businessid_54', 'desc': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.', 'tokens': []}, {'business_id': 'businessid_8', 'desc': 'This Philadelphia, PA location offers a range of services including Hotels & Travel, Taxis, Transportation, Local Services, and Automotive to meet all your travel and transportation needs.', 'tokens': []}, {'business_id': 'businessid_59', 'desc': 'Located at 4403 Chestnut St in Philadelphia, PA, this vibrant spot offers a delightful mix of Food, Bubble Tea, Restaurants, Sandwiches, Vietnamese, Cafes, perfect for a casual meal or a refreshing drink.', 'tokens': []}, {'business_id': 'businessid_91', 'desc': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.', 'tokens': []}, {'business_id': 'businessid_83', 'desc': 'Located at 13002 Seminole Blvd, Ste 10-11 in Largo, FL, this business specializes in Optometrists, Health & Medical, Eyewear & Opticians, Ophthalmologists, Doctors, Shopping, offering a range of eye care services and products.', 'tokens': []}, {'business_id': 'businessid_93', 'desc': 'Located at 914 Edwardsville Rd in Troy, IL, this vibrant spot offers a diverse menu featuring American (New) cuisine, along with a lively atmosphere perfect for nightlife, bars, restaurants, and sports bars.', 'tokens': []}, {'business_id': 'businessid_1', 'desc': 'Located in Pennsauken, NJ, this business specializes in Home Services, Pool & Hot Tub Service, providing expert care for all your residential maintenance needs.', 'tokens': []}, {'business_id': 'businessid_24', 'desc': 'Located at 4663 Maryland Ave in Saint Louis, MO, this delightful spot offers a tempting selection of treats in the categories of Food, Ice Cream & Frozen Yogurt.', 'tokens': []}]}

exec(code, env_args)
