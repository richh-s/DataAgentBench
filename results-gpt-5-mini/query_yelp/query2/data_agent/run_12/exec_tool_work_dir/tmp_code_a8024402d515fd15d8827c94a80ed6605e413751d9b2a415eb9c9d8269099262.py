code = """import json, re, pandas as pd
with open(var_call_gmfsuULA5Cj7JYw0AjBra27j, 'r') as f:
    business_data = json.load(f)
with open(var_call_zJ3tUM6dqGmRVBAGwQKmuy8R, 'r') as f:
    review_data = json.load(f)

dfb = pd.DataFrame(business_data)
dfr = pd.DataFrame(review_data)

us_states = set(['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY'])

# function to extract state
def extract_state(desc):
    if not isinstance(desc, str):
        return None
    # try 'in City, ST' pattern
    m = re.search(r'in\s+[^,]+,\s*([A-Z]{2})\b', desc)
    if m and m.group(1) in us_states:
        return m.group(1)
    # try 'Located at ... in City, ST' already covered, try ', ST,' or ', ST.' or ', ST ' near middle
    m2 = re.search(r',\s*([A-Z]{2})\b', desc)
    if m2 and m2.group(1) in us_states:
        return m2.group(1)
    # try 'This City, ST' or 'City, ST' patterns
    m3 = re.search(r'([A-Za-z ]+),\s*([A-Z]{2})\b', desc)
    if m3 and m3.group(2) in us_states:
        return m3.group(2)
    # fallback: find all two-letter uppercase tokens and pick last that is a US state
    tokens = re.findall(r'\b([A-Z]{2})\b', desc)
    for t in reversed(tokens):
        if t in us_states:
            return t
    return None

# Apply
dfb['state'] = dfb['description'].apply(extract_state)
# convert review_count
dfb['review_count'] = pd.to_numeric(dfb['review_count'], errors='coerce').fillna(0).astype(int)
# aggregate
state_reviews = dfb.dropna(subset=['state']).groupby('state')['review_count'].sum().sort_values(ascending=False)

if state_reviews.empty:
    out = {'state': None, 'total_reviews': 0, 'average_rating': None}
else:
    top_state = state_reviews.index[0]
    total_reviews = int(state_reviews.iloc[0])
    # find businesses in top_state
    biz_ids = dfb[dfb['state']==top_state]['business_id'].dropna().unique().tolist()
    biz_refs = [b.replace('businessid_', 'businessref_') for b in biz_ids]
    dfr['rating'] = pd.to_numeric(dfr['rating'], errors='coerce')
    dfr_sub = dfr[dfr['business_ref'].isin(biz_refs)]
    if not dfr_sub.empty:
        avg_rating = round(float(dfr_sub['rating'].mean()), 3)
    else:
        avg_rating = None
    out = {'state': top_state, 'total_reviews': total_reviews, 'average_rating': avg_rating, 'num_businesses_in_state': len(biz_ids), 'num_reviews_found_in_review_table': int(len(dfr_sub))}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_QVob1VqNPAgiofwEAKHrIiTr': ['checkin', 'business'], 'var_call_Pnw1vvitcoZD7CwhfWOMCoaw': ['review', 'tip', 'user'], 'var_call_29NbFVBLxVQw9DZ4jU0BHgZN': 'file_storage/call_29NbFVBLxVQw9DZ4jU0BHgZN.json', 'var_call_zJ3tUM6dqGmRVBAGwQKmuy8R': 'file_storage/call_zJ3tUM6dqGmRVBAGwQKmuy8R.json', 'var_call_usnmfw7OteypT5lIzS9eCHTL': {'state': None, 'total_reviews': 0, 'average_rating': None}, 'var_call_ROE23fzgSZYrYehjJqmb9S4r': {'sample_extraction': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.', 'extracted_state': None}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.', 'extracted_state': None}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.', 'extracted_state': None}, {'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.', 'extracted_state': None}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.', 'extracted_state': None}, {'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.', 'extracted_state': None}, {'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.', 'extracted_state': None}, {'business_id': 'businessid_64', 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.', 'extracted_state': None}, {'business_id': 'businessid_52', 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.', 'extracted_state': None}, {'business_id': 'businessid_29', 'description': 'Located at 41 Haddon Ave in Collingswood, NJ, this versatile establishment offers a range of services including Wedding Planning, Flowers & Gifts, Event Planning & Services, Financial Services, Shopping, and Florists.', 'extracted_state': None}, {'business_id': 'businessid_10', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'.", 'extracted_state': None}, {'business_id': 'businessid_61', 'description': 'Located at 1218 Millennium Pkwy in Brandon, FL, this facility provides essential services in the categories of Medical Centers, Health & Medical.', 'extracted_state': None}, {'business_id': 'businessid_54', 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.', 'extracted_state': None}, {'business_id': 'businessid_8', 'description': 'This Philadelphia, PA location offers a range of services including Hotels & Travel, Taxis, Transportation, Local Services, and Automotive to meet all your travel and transportation needs.', 'extracted_state': None}, {'business_id': 'businessid_59', 'description': 'Located at 4403 Chestnut St in Philadelphia, PA, this vibrant spot offers a delightful mix of Food, Bubble Tea, Restaurants, Sandwiches, Vietnamese, Cafes, perfect for a casual meal or a refreshing drink.', 'extracted_state': None}, {'business_id': 'businessid_91', 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.', 'extracted_state': None}, {'business_id': 'businessid_83', 'description': 'Located at 13002 Seminole Blvd, Ste 10-11 in Largo, FL, this business specializes in Optometrists, Health & Medical, Eyewear & Opticians, Ophthalmologists, Doctors, Shopping, offering a range of eye care services and products.', 'extracted_state': None}, {'business_id': 'businessid_93', 'description': 'Located at 914 Edwardsville Rd in Troy, IL, this vibrant spot offers a diverse menu featuring American (New) cuisine, along with a lively atmosphere perfect for nightlife, bars, restaurants, and sports bars.', 'extracted_state': None}, {'business_id': 'businessid_1', 'description': 'Located in Pennsauken, NJ, this business specializes in Home Services, Pool & Hot Tub Service, providing expert care for all your residential maintenance needs.', 'extracted_state': None}, {'business_id': 'businessid_24', 'description': 'Located at 4663 Maryland Ave in Saint Louis, MO, this delightful spot offers a tempting selection of treats in the categories of Food, Ice Cream & Frozen Yogurt.', 'extracted_state': None}, {'business_id': 'businessid_95', 'description': 'Located at 201 Veterans Memorial Blvd in Metairie, LA, this establishment offers a diverse menu featuring Restaurants, Sandwiches, Specialty Food, Food, Fruits & Veggies, and Fast Food options for every palate.', 'extracted_state': None}, {'business_id': 'businessid_50', 'description': 'Located at 7670 E 96th St in Fishers, IN, this vibrant eatery offers a diverse menu featuring Burgers, Fast Food, Sandwiches, Restaurants, perfect for a quick and satisfying meal.', 'extracted_state': None}, {'business_id': 'businessid_26', 'description': 'Located at 7003 Seminole Blvd in Seminole, FL, this establishment specializes in a variety of offerings, including Fast Food, Restaurants, Coffee & Tea, Food, and Burgers, making it a convenient stop for a quick meal or a refreshing beverage.', 'extracted_state': None}, {'business_id': 'businessid_84', 'description': 'Located at 5816 Crawfordsville Rd in Indianapolis, IN, this store offers a diverse selection of products in categories such as Books, Mags, Music & Video, Video Game Stores, Videos & Video Game Rental, Electronics, Shopping, and Hobby Shops.', 'extracted_state': None}, {'business_id': 'businessid_89', 'description': 'Located at 540 Shoemaker Rd in King of Prussia, PA, this establishment offers a range of services including Dry Cleaning & Laundry, Laundromat, Local Services, and Laundry Services.', 'extracted_state': None}, {'business_id': 'businessid_32', 'description': 'Located at 1715 Jefferson Hwy in New Orleans, LA, this lively establishment offers a great atmosphere for enjoying Bars, Dive Bars, Burgers, Nightlife, and Restaurants.', 'extracted_state': None}, {'business_id': 'businessid_70', 'description': 'Located at 4500 Shores Dr, Ste 2 in Metairie, LA, this business specializes in a range of offerings within the Home Services, Plumbing categories.', 'extracted_state': None}, {'business_id': 'businessid_42', 'description': 'Located at 1180 Collinsville Crossing in Collinsville, IL, this establishment offers a range of services including Tires, Automotive, Auto Repair, and Oil Change Stations to meet all your vehicle needs.', 'extracted_state': None}, {'business_id': 'businessid_71', 'description': 'Located at 8853 West Fairview Ave in Boise, ID, this business specializes in Automotive, Auto Repair, Car Dealers, and Auto Parts & Supplies.', 'extracted_state': None}, {'business_id': 'businessid_97', 'description': 'Located at 560 Cottman Ave in Cheltenham, PA, this establishment specializes in Body Shops, Automotive services to meet all your vehicle repair needs.', 'extracted_state': None}], 'state_counts_top10': [], 'total_states_found': 0}, 'var_call_uTYN3dhrhQCizbt7zspzWkfG': 'file_storage/call_uTYN3dhrhQCizbt7zspzWkfG.json', 'var_call_30zkShwahhgANfyObmhB3CZv': {'state': None, 'total_reviews': 0, 'average_rating': None}, 'var_call_xwaZ5rU6tMFZWTo0mKTS5vI7': {'total_businesses': 100, 'num_extracted_states': 0, 'num_filtered_states': 0, 'top20_raw': [], 'top20_filtered': []}, 'var_call_gmfsuULA5Cj7JYw0AjBra27j': 'file_storage/call_gmfsuULA5Cj7JYw0AjBra27j.json'}

exec(code, env_args)
