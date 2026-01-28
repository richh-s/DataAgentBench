code = """import json, re, pandas as pd

# Load data
with open(var_call_zbZVBzAf6L1maBUDhJpN84JT, 'r') as f:
    business_docs = json.load(f)
with open(var_call_HtUP2QtCM4W2py1nVbQumg46, 'r') as f:
    review_rows = json.load(f)

# DataFrames
df_biz = pd.DataFrame(business_docs)
df_rev = pd.DataFrame(review_rows)

# List of valid US state codes + DC
VALID_STATES = {s for s in ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','DC']}

# Regex patterns to attempt
patterns = [re.compile(r"in\s+[^,]+,\s*([A-Z]{2})\b"),
            re.compile(r",\s*([A-Z]{2})\b"),
            re.compile(r"\b([A-Z]{2})\s*$")]

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    for p in patterns:
        m = p.search(desc)
        if m:
            code = m.group(1)
            if code in VALID_STATES:
                return code
    return None

# Apply extraction
if 'description' in df_biz.columns:
    df_biz['state'] = df_biz['description'].apply(extract_state)
else:
    df_biz['state'] = None

# Build mapping
biz_state_map = {row['business_id']: row['state'] for row in df_biz.to_dict(orient='records')}

# Prepare reviews
if 'rating' in df_rev.columns:
    df_rev['rating'] = pd.to_numeric(df_rev['rating'], errors='coerce')
else:
    df_rev['rating'] = None

# Map business_ref to business_id
if 'business_ref' in df_rev.columns:
    df_rev['business_id'] = df_rev['business_ref'].str.replace('businessref_', 'businessid_', regex=False)
else:
    df_rev['business_id'] = None

# Map to state
df_rev['state'] = df_rev['business_id'].map(biz_state_map)
# Filter reviews with valid state and numeric rating
df_rev_valid = df_rev[df_rev['state'].notna() & df_rev['rating'].notna()].copy()

# Aggregate
if df_rev_valid.empty:
    result = {'state': None, 'review_count': 0, 'average_rating': None}
else:
    agg = df_rev_valid.groupby('state').agg(review_count=('rating','size'), average_rating=('rating','mean'))
    agg = agg.sort_values('review_count', ascending=False)
    top_state = agg.index[0]
    top_count = int(agg.iloc[0]['review_count'])
    avg_rating = round(float(agg.iloc[0]['average_rating']), 3)
    result = {'state': top_state, 'review_count': top_count, 'average_rating': avg_rating}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_zbZVBzAf6L1maBUDhJpN84JT': 'file_storage/call_zbZVBzAf6L1maBUDhJpN84JT.json', 'var_call_HtUP2QtCM4W2py1nVbQumg46': 'file_storage/call_HtUP2QtCM4W2py1nVbQumg46.json', 'var_call_kP6QKdhhBJzhUQVjqQaIP39F': {'state': None, 'review_count': 0, 'average_rating': None}, 'var_call_BDZxjFcyzaArh6TOcHLUE9Np': {'state_counts_sample': {}}, 'var_call_REvNRR0aoycY7B5ol3RsP0h3': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'business_id': 'businessid_64', 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'business_id': 'businessid_52', 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.'}, {'business_id': 'businessid_29', 'description': 'Located at 41 Haddon Ave in Collingswood, NJ, this versatile establishment offers a range of services including Wedding Planning, Flowers & Gifts, Event Planning & Services, Financial Services, Shopping, and Florists.'}, {'business_id': 'businessid_10', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}, {'business_id': 'businessid_61', 'description': 'Located at 1218 Millennium Pkwy in Brandon, FL, this facility provides essential services in the categories of Medical Centers, Health & Medical.'}, {'business_id': 'businessid_54', 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'business_id': 'businessid_8', 'description': 'This Philadelphia, PA location offers a range of services including Hotels & Travel, Taxis, Transportation, Local Services, and Automotive to meet all your travel and transportation needs.'}, {'business_id': 'businessid_59', 'description': 'Located at 4403 Chestnut St in Philadelphia, PA, this vibrant spot offers a delightful mix of Food, Bubble Tea, Restaurants, Sandwiches, Vietnamese, Cafes, perfect for a casual meal or a refreshing drink.'}, {'business_id': 'businessid_91', 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}, {'business_id': 'businessid_83', 'description': 'Located at 13002 Seminole Blvd, Ste 10-11 in Largo, FL, this business specializes in Optometrists, Health & Medical, Eyewear & Opticians, Ophthalmologists, Doctors, Shopping, offering a range of eye care services and products.'}, {'business_id': 'businessid_93', 'description': 'Located at 914 Edwardsville Rd in Troy, IL, this vibrant spot offers a diverse menu featuring American (New) cuisine, along with a lively atmosphere perfect for nightlife, bars, restaurants, and sports bars.'}, {'business_id': 'businessid_1', 'description': 'Located in Pennsauken, NJ, this business specializes in Home Services, Pool & Hot Tub Service, providing expert care for all your residential maintenance needs.'}, {'business_id': 'businessid_24', 'description': 'Located at 4663 Maryland Ave in Saint Louis, MO, this delightful spot offers a tempting selection of treats in the categories of Food, Ice Cream & Frozen Yogurt.'}, {'business_id': 'businessid_95', 'description': 'Located at 201 Veterans Memorial Blvd in Metairie, LA, this establishment offers a diverse menu featuring Restaurants, Sandwiches, Specialty Food, Food, Fruits & Veggies, and Fast Food options for every palate.'}, {'business_id': 'businessid_50', 'description': 'Located at 7670 E 96th St in Fishers, IN, this vibrant eatery offers a diverse menu featuring Burgers, Fast Food, Sandwiches, Restaurants, perfect for a quick and satisfying meal.'}, {'business_id': 'businessid_26', 'description': 'Located at 7003 Seminole Blvd in Seminole, FL, this establishment specializes in a variety of offerings, including Fast Food, Restaurants, Coffee & Tea, Food, and Burgers, making it a convenient stop for a quick meal or a refreshing beverage.'}, {'business_id': 'businessid_84', 'description': 'Located at 5816 Crawfordsville Rd in Indianapolis, IN, this store offers a diverse selection of products in categories such as Books, Mags, Music & Video, Video Game Stores, Videos & Video Game Rental, Electronics, Shopping, and Hobby Shops.'}, {'business_id': 'businessid_89', 'description': 'Located at 540 Shoemaker Rd in King of Prussia, PA, this establishment offers a range of services including Dry Cleaning & Laundry, Laundromat, Local Services, and Laundry Services.'}, {'business_id': 'businessid_32', 'description': 'Located at 1715 Jefferson Hwy in New Orleans, LA, this lively establishment offers a great atmosphere for enjoying Bars, Dive Bars, Burgers, Nightlife, and Restaurants.'}, {'business_id': 'businessid_70', 'description': 'Located at 4500 Shores Dr, Ste 2 in Metairie, LA, this business specializes in a range of offerings within the Home Services, Plumbing categories.'}, {'business_id': 'businessid_42', 'description': 'Located at 1180 Collinsville Crossing in Collinsville, IL, this establishment offers a range of services including Tires, Automotive, Auto Repair, and Oil Change Stations to meet all your vehicle needs.'}, {'business_id': 'businessid_71', 'description': 'Located at 8853 West Fairview Ave in Boise, ID, this business specializes in Automotive, Auto Repair, Car Dealers, and Auto Parts & Supplies.'}, {'business_id': 'businessid_97', 'description': 'Located at 560 Cottman Ave in Cheltenham, PA, this establishment specializes in Body Shops, Automotive services to meet all your vehicle repair needs.'}], 'var_call_W90yCMpMWOyRzLcvE9wteln1': 'file_storage/call_W90yCMpMWOyRzLcvE9wteln1.json', 'var_call_UmkQGBamkI0vgBmfYbHLlFaV': 'file_storage/call_UmkQGBamkI0vgBmfYbHLlFaV.json', 'var_call_K0xdTz38I6Orz9gx2uXAvDy6': {'matched_count': 100, 'unique_states_sample': ['AB', 'AZ', 'CA', 'FL', 'ID', 'IL', 'IN', 'LA', 'MO', 'NJ']}}

exec(code, env_args)
