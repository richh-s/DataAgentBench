code = """import json
import pandas as pd
# Load data from storage variables
reviews = var_call_Rv6u7UKTiAb4wfHlF1nvpTiT
businesses = var_call_7lVIqr8BFQbTFrxtzU1QUee9

rev_df = pd.DataFrame(reviews)
rev_df['review_count'] = rev_df['review_count'].astype(int)
rev_df['business_id'] = rev_df['business_ref'].str.replace('businessref_', 'businessid_')

biz_df = pd.DataFrame(businesses)
merged = pd.merge(rev_df, biz_df, on='business_id', how='left')

import re

def extract_categories(desc):
    if not isinstance(desc, str) or not desc:
        return []
    # Try to find portion that lists categories: often after the word 'offers' or after the last 'in '
    desc_lower = desc
    # Try 'offers' pattern
    idx = desc_lower.lower().find('offers')
    if idx != -1:
        sub = desc_lower[idx:]
        # find 'in ' after offers
        in_idx = sub.find(' in ')
        if in_idx != -1:
            tail = sub[in_idx+4:]
        else:
            # take after 'offers' if no 'in '
            tail = sub[6:]
    else:
        # fallback: take substring after last ' in '
        parts = desc.split(' in ')
        tail = parts[-1]
    # cleanup
    tail = tail.strip().strip('.').strip('"').strip("'")
    # cut off at phrases that introduce commentary
    cut_phrases = ['making it', 'perfect for', 'to meet', 'providing', 'offering', 'making this', 'making them', 'making it a', 'making it an']
    for p in cut_phrases:
        li = tail.lower().find(p)
        if li != -1:
            tail = tail[:li]
            break
    # split by comma, slash, semicolon, or pipe
    parts = re.split(r'[,/;|]', tail)
    cats = []
    for p in parts:
        p = p.strip()
        if p:
            cats.append(p)
    return cats

from collections import defaultdict
cat_counts = defaultdict(int)
for _, row in merged.iterrows():
    desc = row.get('description', '')
    cats = extract_categories(desc)
    if not cats:
        name = row.get('name', '')
        if isinstance(name, str) and name:
            cats = [name]
    for c in cats:
        cat_counts[c] += int(row['review_count'])

cat_list = sorted([{'category': k, 'review_count': v} for k, v in cat_counts.items()], key=lambda x: x['review_count'], reverse=True)
top5 = cat_list[:5]

print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_bK1wT73cUxbWQdtnouUxGfhB': ['checkin', 'business'], 'var_call_gFfvBtU7vVDRF2laeOVuOOam': ['review', 'tip', 'user'], 'var_call_UrLl8pmlnmr5bra7UKKOBH6T': 'file_storage/call_UrLl8pmlnmr5bra7UKKOBH6T.json', 'var_call_Rv6u7UKTiAb4wfHlF1nvpTiT': [{'business_ref': 'businessref_45', 'review_count': '3'}, {'business_ref': 'businessref_96', 'review_count': '2'}, {'business_ref': 'businessref_60', 'review_count': '2'}, {'business_ref': 'businessref_92', 'review_count': '2'}, {'business_ref': 'businessref_33', 'review_count': '2'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_36', 'review_count': '2'}, {'business_ref': 'businessref_57', 'review_count': '2'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}, {'business_ref': 'businessref_13', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '1'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_62', 'review_count': '1'}, {'business_ref': 'businessref_79', 'review_count': '1'}, {'business_ref': 'businessref_98', 'review_count': '1'}, {'business_ref': 'businessref_86', 'review_count': '1'}, {'business_ref': 'businessref_31', 'review_count': '1'}, {'business_ref': 'businessref_26', 'review_count': '1'}, {'business_ref': 'businessref_12', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}, {'business_ref': 'businessref_37', 'review_count': '1'}, {'business_ref': 'businessref_6', 'review_count': '1'}, {'business_ref': 'businessref_15', 'review_count': '1'}, {'business_ref': 'businessref_68', 'review_count': '1'}], 'var_call_7lVIqr8BFQbTFrxtzU1QUee9': [{'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'name': 'J&Q Nails', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'business_id': 'businessid_74', 'name': 'Candy Barrel', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'business_id': 'businessid_92', 'name': 'Luminosity', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'business_id': 'businessid_10', 'name': 'China Wok', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}, {'business_id': 'businessid_26', 'name': "McDonald's", 'description': 'Located at 7003 Seminole Blvd in Seminole, FL, this establishment specializes in a variety of offerings, including Fast Food, Restaurants, Coffee & Tea, Food, and Burgers, making it a convenient stop for a quick meal or a refreshing beverage.'}, {'business_id': 'businessid_14', 'name': 'Ross Dress for Less', 'description': "Located at 7055 Marketplace Dr in Goleta, CA, this store offers a diverse selection of products across various categories, including Women's Clothing, Fashion, Department Stores, Home Decor, Home & Garden, Shopping, Men's Clothing, and Discount Store."}, {'business_id': 'businessid_57', 'name': 'Big Boys Moving And Storage', 'description': 'Located at 13605 W Hillsborough Ave in Tampa, FL, this versatile establishment offers a range of services and dining options, including Movers, American (New), Landscape Architects, Food, Home Services, Self Storage, Local Services, Restaurants.'}, {'business_id': 'businessid_45', 'name': 'The Fresh Market', 'description': 'Located at 2900 4th St N in St. Petersburg, FL, this establishment offers a diverse range of products and services in the categories of Food, Grocery, Shopping.'}, {'business_id': 'businessid_68', 'name': 'Brow Art', 'description': 'Located at 593 Brandon Town Ctr in Brandon, FL, this establishment offers a range of services in the categories of Beauty & Spas, Hair Removal, and Eyebrow Services.'}, {'business_id': 'businessid_6', 'name': 'The Jungle', 'description': 'Located at 246 W 1st St in Reno, NV, this vibrant destination offers a delightful mix of Restaurants, Breakfast & Brunch, Bars, Wine Bars, Coffee & Tea, Food, Cafes, Sandwiches, and Nightlife, making it an ideal spot for any meal or occasion.'}, {'business_id': 'businessid_79', 'name': 'Pit Stop HQ', 'description': 'Located at 838-842 Christian St in Philadelphia, PA, this establishment offers a wide range of services including Pet Groomers, Pet Stores, Pet Training, Dog Walkers, Pet Services, Pets, and Pet Sitting.'}, {'business_id': 'businessid_66', 'name': 'Panda Express', 'description': 'Located at 3849 State St. Space I-58 in Santa Barbara, CA, this establishment offers a variety of quick and delicious options in the categories of Fast Food, Chinese, Restaurants.'}, {'business_id': 'businessid_15', 'name': 'Take 5 Oil Change', 'description': 'Located at 3803 Gen Degaulle Dr in New Orleans, LA, this establishment specializes in Automotive, Oil Change Stations, providing efficient service for all your vehicle maintenance needs.'}, {'business_id': 'businessid_96', 'name': 'Farmhaus Restaurant', 'description': 'Located at 3257 Ivanhoe Ave in Saint Louis, MO, this establishment offers a vibrant atmosphere perfect for enjoying a diverse selection of experiences, including Wine Bars, American (New), Cocktail Bars, Restaurants, American (Traditional), Nightlife, and Bars.'}, {'business_id': 'businessid_86', 'name': "Humpty's Dumplings", 'description': 'Located at 705 East Passyunk Ave in Philadelphia, PA, this vibrant eatery offers a diverse menu featuring American (New), Restaurants, American (Traditional), Asian Fusion, Noodles, Dim Sum, Fast Food, Chinese, catering to a variety of tastes and preferences.'}, {'business_id': 'businessid_53', 'name': 'Samwich', 'description': 'Located at 1040 N American St, Ste 1101 in Philadelphia, PA, this eatery offers a diverse menu featuring Salad, Sandwiches, Restaurants, and Burgers.'}, {'business_id': 'businessid_20', 'name': 'Chick-fil-A', 'description': 'Located at 9040 State Road 54 in Trinity, FL, this establishment offers a diverse array of options, including Restaurants, American (New), Caterers, Fast Food, Chicken Shop, Event Planning & Services, and American (Traditional).'}, {'business_id': 'businessid_37', 'name': 'Orangetheory Fitness Carrollwood', 'description': 'Located at 13122 N Dale Mabry Hwy in Tampa, FL, this facility offers a comprehensive range of services in Fitness & Instruction, Gyms, Boot Camps, Trainers, Active Life, and Interval Training Gyms.'}, {'business_id': 'businessid_62', 'name': 'Winn Dixie', 'description': 'Located at 8424 Sheldon Rd in Tampa, FL, this establishment offers a diverse range of products and services, including Photography Stores & Services, Shopping, Grocery, and Food.'}, {'business_id': 'businessid_31', 'name': 'Island Way Car Wash', 'description': 'Located at 1234 Pasadena Ave S in South Pasadena, FL, this business specializes in Automotive services, offering a comprehensive Car Wash and professional Auto Detailing to keep your vehicle looking its best.'}, {'business_id': 'businessid_12', 'name': 'Atlantic Trap & Gill Pub', 'description': 'Located at 7704 Calgary Trail S in Edmonton, AB, this vibrant spot offers a diverse experience with options for Pubs, Restaurants, Nightlife, Burgers, Seafood, and Bars.'}, {'business_id': 'businessid_60', 'name': 'Walmart', 'description': 'Located at 8101 W Judge Perez Dr in Chalmette, LA, this versatile establishment offers a wide range of options for customers, including Food, Shopping, Fashion, Discount Store, Grocery, Electronics, Drugstores, Department Stores, ensuring that visitors can find everything they need in one convenient location.'}, {'business_id': 'businessid_98', 'name': 'Brookmont Apartment Homes', 'description': 'Situated at 600 Red Lion Rd in Philadelphia, PA, this establishment offers a range of services in Real Estate, Apartments, and Home Services.'}, {'business_id': 'businessid_36', 'name': 'Pho & Beyond', 'description': "Located at 47 Easton Rd in Willow Grove, PA, this inviting establishment offers a delightful menu featuring authentic flavors in the categories of 'Restaurants, Vietnamese'."}, {'business_id': 'businessid_13', 'name': 'Avian Glen Winery', 'description': 'Located at 3545 Almaville Rd in Smyrna, TN, this establishment offers a delightful experience encompassing Food, Arts & Entertainment, Wineries, and a Wine Tasting Room.'}]}

exec(code, env_args)
