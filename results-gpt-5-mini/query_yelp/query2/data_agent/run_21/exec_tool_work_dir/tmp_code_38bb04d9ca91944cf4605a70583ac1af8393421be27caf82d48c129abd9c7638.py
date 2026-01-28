code = """import json
import re
from collections import Counter

with open(var_call_K4j5EdaGbvL0F2JZCDZlMfb4, 'r') as f:
    businesses = json.load(f)
with open(var_call_MC5PA2iXmKvLohsxZOLzSr5l, 'r') as f:
    reviews = json.load(f)

states = set(['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','DC'])

def extract_state_tokens(desc):
    if not isinstance(desc, str):
        return None
    toks = re.findall(r"\b[A-Za-z]{2}\b", desc)
    # uppercase tokens only
    toks2 = [t.upper() for t in toks]
    for t in reversed(toks2):
        if t in states:
            return t
    return None

# Try alternative: find pattern ', XX' anywhere
pat = re.compile(r',\s*([A-Za-z]{2})\b')
def extract_state_pat(desc):
    if not isinstance(desc, str):
        return None
    m = pat.findall(desc)
    for t in reversed(m):
        if t.upper() in states:
            return t.upper()
    return None

# Collect states using multiple methods
counts = Counter()
counts_pat = Counter()
no_state = []
for b in businesses:
    desc = b.get('description','')
    s1 = extract_state_tokens(desc)
    s2 = extract_state_pat(desc)
    state = s1 or s2
    if state:
        counts[state] += 1
    else:
        no_state.append(b.get('business_id'))
    if s2:
        counts_pat[s2] += 1

# Sum review_count per state (using state from s1 or s2)
state_review_counts = Counter()
for b in businesses:
    desc = b.get('description','')
    state = extract_state_tokens(desc) or extract_state_pat(desc)
    try:
        rc = int(b.get('review_count',0))
    except:
        try:
            rc = int(float(b.get('review_count',0)))
        except:
            rc = 0
    if state:
        state_review_counts[state] += rc

# Find top state by total review_count
if state_review_counts:
    top_state, top_total = state_review_counts.most_common(1)[0]
else:
    top_state, top_total = None, 0

# Compute average rating for businesses in top_state
if top_state:
    # map business_ref -> business_id
    biz_state = {}
    for b in businesses:
        bid = b.get('business_id')
        desc = b.get('description','')
        state = extract_state_tokens(desc) or extract_state_pat(desc)
        if state:
            biz_state[bid] = state
    ratings = []
    for r in reviews:
        bref = r.get('business_ref')
        if not bref:
            continue
        bid = str(bref).replace('businessref_','businessid_')
        state = biz_state.get(bid)
        if state == top_state:
            try:
                ratings.append(float(r.get('rating')))
            except:
                pass
    avg = round(sum(ratings)/len(ratings),2) if ratings else None
else:
    avg = None

out = {
    'num_businesses_with_state': sum(counts.values()),
    'num_businesses_total': len(businesses),
    'top_state': top_state,
    'top_state_total_reviews': top_total,
    'average_rating_top_state': avg,
    'state_counts_sample': counts.most_common(10),
    'state_counts_pat_sample': counts_pat.most_common(10),
    'no_state_sample_10': no_state[:10]
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_G8hOykkC4hAZtPhL6yZt1uZ4': ['checkin', 'business'], 'var_call_G7tiMa5ecVnpHmEVAStpmLgn': ['review', 'tip', 'user'], 'var_call_K4j5EdaGbvL0F2JZCDZlMfb4': 'file_storage/call_K4j5EdaGbvL0F2JZCDZlMfb4.json', 'var_call_MC5PA2iXmKvLohsxZOLzSr5l': 'file_storage/call_MC5PA2iXmKvLohsxZOLzSr5l.json', 'var_call_AFjWY94ENbetQ3HDcnvZ5AGH': {'state': None, 'total_reviews': 0, 'average_rating': None}, 'var_call_bGOAEWagOaMhgtQBKmBYp7ip': 'file_storage/call_bGOAEWagOaMhgtQBKmBYp7ip.json', 'var_call_jiUXn8Zg5LAPvkQNweIWwwAX': {'state': None, 'total_reviews': 0, 'average_rating': None}, 'var_call_Z5NHfhUm6sXSEe1HjXkxpy4T': [{'business_id': 'businessid_49', 'desc_repr': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local S', 'toks1': [], 'toks2': ['CA']}, {'business_id': 'businessid_47', 'desc_repr': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artis', 'toks1': [], 'toks2': ['MO']}, {'business_id': 'businessid_88', 'desc_repr': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.', 'toks1': [], 'toks2': ['ID']}, {'business_id': 'businessid_41', 'desc_repr': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.', 'toks1': [], 'toks2': ['FL']}, {'business_id': 'businessid_33', 'desc_repr': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.', 'toks1': [], 'toks2': ['IN']}, {'business_id': 'businessid_74', 'desc_repr': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.', 'toks1': [], 'toks2': ['FL']}, {'business_id': 'businessid_92', 'desc_repr': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whiteni', 'toks1': [], 'toks2': ['PA']}, {'business_id': 'businessid_64', 'desc_repr': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.', 'toks1': [], 'toks2': ['MO']}, {'business_id': 'businessid_52', 'desc_repr': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative ne', 'toks1': [], 'toks2': ['IN']}, {'business_id': 'businessid_29', 'desc_repr': 'Located at 41 Haddon Ave in Collingswood, NJ, this versatile establishment offers a range of services including Wedding Planning, Flowers & Gifts, Event Planning & Services, Financial Services, Shoppi', 'toks1': [], 'toks2': ['NJ']}, {'business_id': 'businessid_10', 'desc_repr': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'.", 'toks1': [], 'toks2': ['MO']}, {'business_id': 'businessid_61', 'desc_repr': 'Located at 1218 Millennium Pkwy in Brandon, FL, this facility provides essential services in the categories of Medical Centers, Health & Medical.', 'toks1': [], 'toks2': ['FL']}, {'business_id': 'businessid_54', 'desc_repr': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Sto', 'toks1': [], 'toks2': ['FL']}, {'business_id': 'businessid_8', 'desc_repr': 'This Philadelphia, PA location offers a range of services including Hotels & Travel, Taxis, Transportation, Local Services, and Automotive to meet all your travel and transportation needs.', 'toks1': [], 'toks2': []}, {'business_id': 'businessid_59', 'desc_repr': 'Located at 4403 Chestnut St in Philadelphia, PA, this vibrant spot offers a delightful mix of Food, Bubble Tea, Restaurants, Sandwiches, Vietnamese, Cafes, perfect for a casual meal or a refreshing dr', 'toks1': [], 'toks2': ['PA']}, {'business_id': 'businessid_91', 'desc_repr': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, ', 'toks1': [], 'toks2': ['LA']}, {'business_id': 'businessid_83', 'desc_repr': 'Located at 13002 Seminole Blvd, Ste 10-11 in Largo, FL, this business specializes in Optometrists, Health & Medical, Eyewear & Opticians, Ophthalmologists, Doctors, Shopping, offering a range of eye c', 'toks1': [], 'toks2': ['FL']}, {'business_id': 'businessid_93', 'desc_repr': 'Located at 914 Edwardsville Rd in Troy, IL, this vibrant spot offers a diverse menu featuring American (New) cuisine, along with a lively atmosphere perfect for nightlife, bars, restaurants, and sport', 'toks1': [], 'toks2': ['IL']}, {'business_id': 'businessid_1', 'desc_repr': 'Located in Pennsauken, NJ, this business specializes in Home Services, Pool & Hot Tub Service, providing expert care for all your residential maintenance needs.', 'toks1': [], 'toks2': ['NJ']}, {'business_id': 'businessid_24', 'desc_repr': 'Located at 4663 Maryland Ave in Saint Louis, MO, this delightful spot offers a tempting selection of treats in the categories of Food, Ice Cream & Frozen Yogurt.', 'toks1': [], 'toks2': ['MO']}, {'business_id': 'businessid_95', 'desc_repr': 'Located at 201 Veterans Memorial Blvd in Metairie, LA, this establishment offers a diverse menu featuring Restaurants, Sandwiches, Specialty Food, Food, Fruits & Veggies, and Fast Food options for eve', 'toks1': [], 'toks2': ['LA']}, {'business_id': 'businessid_50', 'desc_repr': 'Located at 7670 E 96th St in Fishers, IN, this vibrant eatery offers a diverse menu featuring Burgers, Fast Food, Sandwiches, Restaurants, perfect for a quick and satisfying meal.', 'toks1': [], 'toks2': ['IN']}, {'business_id': 'businessid_26', 'desc_repr': 'Located at 7003 Seminole Blvd in Seminole, FL, this establishment specializes in a variety of offerings, including Fast Food, Restaurants, Coffee & Tea, Food, and Burgers, making it a convenient stop ', 'toks1': [], 'toks2': ['FL']}, {'business_id': 'businessid_84', 'desc_repr': 'Located at 5816 Crawfordsville Rd in Indianapolis, IN, this store offers a diverse selection of products in categories such as Books, Mags, Music & Video, Video Game Stores, Videos & Video Game Rental', 'toks1': [], 'toks2': ['IN']}, {'business_id': 'businessid_89', 'desc_repr': 'Located at 540 Shoemaker Rd in King of Prussia, PA, this establishment offers a range of services including Dry Cleaning & Laundry, Laundromat, Local Services, and Laundry Services.', 'toks1': [], 'toks2': ['PA']}, {'business_id': 'businessid_32', 'desc_repr': 'Located at 1715 Jefferson Hwy in New Orleans, LA, this lively establishment offers a great atmosphere for enjoying Bars, Dive Bars, Burgers, Nightlife, and Restaurants.', 'toks1': [], 'toks2': ['LA']}, {'business_id': 'businessid_70', 'desc_repr': 'Located at 4500 Shores Dr, Ste 2 in Metairie, LA, this business specializes in a range of offerings within the Home Services, Plumbing categories.', 'toks1': [], 'toks2': ['LA']}, {'business_id': 'businessid_42', 'desc_repr': 'Located at 1180 Collinsville Crossing in Collinsville, IL, this establishment offers a range of services including Tires, Automotive, Auto Repair, and Oil Change Stations to meet all your vehicle need', 'toks1': [], 'toks2': ['IL']}, {'business_id': 'businessid_71', 'desc_repr': 'Located at 8853 West Fairview Ave in Boise, ID, this business specializes in Automotive, Auto Repair, Car Dealers, and Auto Parts & Supplies.', 'toks1': [], 'toks2': ['ID']}, {'business_id': 'businessid_97', 'desc_repr': 'Located at 560 Cottman Ave in Cheltenham, PA, this establishment specializes in Body Shops, Automotive services to meet all your vehicle repair needs.', 'toks1': [], 'toks2': ['PA']}], 'var_call_6SdHbWuB3QTnrS2J3Pc0AVwA': {'state': None, 'total_reviews': 0, 'average_rating': None}}

exec(code, env_args)
