code = """import json, re
with open(var_call_c8DwRj64MtSJYZW92sSCp2Oh, 'r') as f:
    businesses = json.load(f)
with open(var_call_n0S2syUfDJf7pjVSheCo8pDc, 'r') as f:
    reviews = json.load(f)

# try robust state extraction
state_pattern = re.compile(r',\s*([A-Z]{2})(?=[,\.\s]|$)')
ref_to_state = {}
state_reviewcount = {}

for b in businesses:
    bid = b.get('business_id')
    desc = b.get('description') or ''
    rc_raw = b.get('review_count')
    try:
        rc = int(rc_raw)
    except:
        try:
            rc = int(float(rc_raw))
        except:
            rc = 0
    if not bid:
        continue
    parts = bid.split('_',1)
    if len(parts) != 2:
        continue
    bref = 'businessref_' + parts[1]
    m = state_pattern.search(desc)
    state = m.group(1) if m else None
    if state:
        ref_to_state[bref] = state
        state_reviewcount[state] = state_reviewcount.get(state, 0) + rc

if not state_reviewcount:
    result = {"state": None, "total_reviews": 0, "average_rating": None}
else:
    # choose state with highest total reviews
    state_max = max(state_reviewcount.items(), key=lambda x: x[1])[0]
    total_reviews = state_reviewcount[state_max]
    # compute average rating from reviews for businesses in that state
    ratings = []
    for r in reviews:
        bref = r.get('business_ref')
        if bref in ref_to_state and ref_to_state[bref] == state_max:
            try:
                ratings.append(float(r.get('rating')))
            except:
                pass
    avg = round(sum(ratings)/len(ratings), 3) if ratings else None
    result = {"state": state_max, "total_reviews": total_reviews, "average_rating": avg}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_DyWkhUZrWhEw6LixAvfowfDs': ['business', 'checkin'], 'var_call_ZcivhTR0krr3WaNsPaY0wwdP': ['review', 'tip', 'user'], 'var_call_c8DwRj64MtSJYZW92sSCp2Oh': 'file_storage/call_c8DwRj64MtSJYZW92sSCp2Oh.json', 'var_call_n0S2syUfDJf7pjVSheCo8pDc': 'file_storage/call_n0S2syUfDJf7pjVSheCo8pDc.json', 'var_call_9oeTCPeOCg4UFqZcFJE93muh': {'state': None, 'total_reviews': 0, 'average_rating': None}, 'var_call_1laMVn0AMpbLxhZPrd1MMgLu': 'file_storage/call_1laMVn0AMpbLxhZPrd1MMgLu.json', 'var_call_PIvy8zBP7dGQZSYICadzOpOw': {'state': None, 'total_reviews': 0, 'average_rating': None}, 'var_call_7ADW41m5U9ZxsbGIPjXgxYYP': {'total_businesses': 100, 'with_description': 100, 'matched_state_count': 0, 'samples': []}, 'var_call_TrcBjt5ZiGUgH1EiSrQdh4tO': [{'business_id': 'businessid_49', 'description_repr': "'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local "}, {'business_id': 'businessid_47', 'description_repr': "'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Arti"}, {'business_id': 'businessid_88', 'description_repr': "'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'"}, {'business_id': 'businessid_41', 'description_repr': "'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'"}, {'business_id': 'businessid_33', 'description_repr': "'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'"}, {'business_id': 'businessid_74', 'description_repr': "'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food"}, {'business_id': 'businessid_92', 'description_repr': "'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whiten"}, {'business_id': 'businessid_64', 'description_repr': "'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'"}, {'business_id': 'businessid_52', 'description_repr': "'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative n"}, {'business_id': 'businessid_29', 'description_repr': "'Located at 41 Haddon Ave in Collingswood, NJ, this versatile establishment offers a range of services including Wedding Planning, Flowers & Gifts, Event Planning & Services, Financial Services, Shopp"}, {'business_id': 'businessid_10', 'description_repr': '"Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of \'Restaurants, Chinese\'."'}, {'business_id': 'businessid_61', 'description_repr': "'Located at 1218 Millennium Pkwy in Brandon, FL, this facility provides essential services in the categories of Medical Centers, Health & Medical.'"}, {'business_id': 'businessid_54', 'description_repr': "'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience St"}, {'business_id': 'businessid_8', 'description_repr': "'This Philadelphia, PA location offers a range of services including Hotels & Travel, Taxis, Transportation, Local Services, and Automotive to meet all your travel and transportation needs.'"}, {'business_id': 'businessid_59', 'description_repr': "'Located at 4403 Chestnut St in Philadelphia, PA, this vibrant spot offers a delightful mix of Food, Bubble Tea, Restaurants, Sandwiches, Vietnamese, Cafes, perfect for a casual meal or a refreshing d"}, {'business_id': 'businessid_91', 'description_repr': "'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning,"}, {'business_id': 'businessid_83', 'description_repr': "'Located at 13002 Seminole Blvd, Ste 10-11 in Largo, FL, this business specializes in Optometrists, Health & Medical, Eyewear & Opticians, Ophthalmologists, Doctors, Shopping, offering a range of eye "}, {'business_id': 'businessid_93', 'description_repr': "'Located at 914 Edwardsville Rd in Troy, IL, this vibrant spot offers a diverse menu featuring American (New) cuisine, along with a lively atmosphere perfect for nightlife, bars, restaurants, and spor"}, {'business_id': 'businessid_1', 'description_repr': "'Located in Pennsauken, NJ, this business specializes in Home Services, Pool & Hot Tub Service, providing expert care for all your residential maintenance needs.'"}, {'business_id': 'businessid_24', 'description_repr': "'Located at 4663 Maryland Ave in Saint Louis, MO, this delightful spot offers a tempting selection of treats in the categories of Food, Ice Cream & Frozen Yogurt.'"}, {'business_id': 'businessid_95', 'description_repr': "'Located at 201 Veterans Memorial Blvd in Metairie, LA, this establishment offers a diverse menu featuring Restaurants, Sandwiches, Specialty Food, Food, Fruits & Veggies, and Fast Food options for ev"}, {'business_id': 'businessid_50', 'description_repr': "'Located at 7670 E 96th St in Fishers, IN, this vibrant eatery offers a diverse menu featuring Burgers, Fast Food, Sandwiches, Restaurants, perfect for a quick and satisfying meal.'"}, {'business_id': 'businessid_26', 'description_repr': "'Located at 7003 Seminole Blvd in Seminole, FL, this establishment specializes in a variety of offerings, including Fast Food, Restaurants, Coffee & Tea, Food, and Burgers, making it a convenient stop"}, {'business_id': 'businessid_84', 'description_repr': "'Located at 5816 Crawfordsville Rd in Indianapolis, IN, this store offers a diverse selection of products in categories such as Books, Mags, Music & Video, Video Game Stores, Videos & Video Game Renta"}, {'business_id': 'businessid_89', 'description_repr': "'Located at 540 Shoemaker Rd in King of Prussia, PA, this establishment offers a range of services including Dry Cleaning & Laundry, Laundromat, Local Services, and Laundry Services.'"}, {'business_id': 'businessid_32', 'description_repr': "'Located at 1715 Jefferson Hwy in New Orleans, LA, this lively establishment offers a great atmosphere for enjoying Bars, Dive Bars, Burgers, Nightlife, and Restaurants.'"}, {'business_id': 'businessid_70', 'description_repr': "'Located at 4500 Shores Dr, Ste 2 in Metairie, LA, this business specializes in a range of offerings within the Home Services, Plumbing categories.'"}, {'business_id': 'businessid_42', 'description_repr': "'Located at 1180 Collinsville Crossing in Collinsville, IL, this establishment offers a range of services including Tires, Automotive, Auto Repair, and Oil Change Stations to meet all your vehicle nee"}, {'business_id': 'businessid_71', 'description_repr': "'Located at 8853 West Fairview Ave in Boise, ID, this business specializes in Automotive, Auto Repair, Car Dealers, and Auto Parts & Supplies.'"}, {'business_id': 'businessid_97', 'description_repr': "'Located at 560 Cottman Ave in Cheltenham, PA, this establishment specializes in Body Shops, Automotive services to meet all your vehicle repair needs.'"}]}

exec(code, env_args)
