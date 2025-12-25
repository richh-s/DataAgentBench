code = """import json
import re

# SQL result data from before (I need to reconstruct reviews_map)
sql_data = locals()['var_function-call-4854865074449366240']
reviews_map = {}
for row in sql_data:
    bid = row['business_ref'].replace('businessref_', 'businessid_')
    cnt = int(row['review_count'])
    reviews_map[bid] = cnt

# Mongo result data
mongo_data = locals()['var_function-call-2958204850641891544']
if isinstance(mongo_data, str) and mongo_data.endswith('.json'):
    with open(mongo_data, 'r') as f:
        mongo_records = json.load(f)
else:
    mongo_records = mongo_data

# Parsing logic
category_counts = {}

anchors = [
    "services in", "services, including", "services including", "including",
    "category of", "seeking", "featuring", "specializes in", "options for",
    "categories of", "mix of", "fields of", "array of", "selection of"
]

# Regex to find the last occurrence of any anchor?
# Actually, the structure usually puts the list at the end.
# I will look for the LAST matching anchor in the text? Or the first?
# "offers a range of services in X..." -> "services in" is good.
# "specializes in a variety of offerings, including X..." -> "including" is better than "specializes in"?
# "menu featuring X..."
# Let's try to match one of the specific phrases that precedes the list.

# "services in "
# "services including "
# "including " -> very common
# "category of "
# "seeking "
# "featuring "
# "specializes in " (if "including" follows, "including" handles it. If "specializes in X, Y", then "specializes in" handles it)
# "mix of "
# "fields of "

regex_pattern = r"(?:services in|services, including|services including|including|category of|seeking|featuring|specializes in|options for|categories of|mix of|fields of) (.*?)(?:\.$|$)"

for b in mongo_records:
    bid = b['business_id']
    desc = b.get('description', '')
    count = reviews_map.get(bid, 0)
    
    # We want to find the part of the description that lists categories.
    # It usually ends the string.
    # Let's find the last match of the pattern, or just search.
    # Most descriptions seem to have only one such phrase near the end.
    
    # Let's normalize spaces
    desc = ' '.join(desc.split())
    
    # Try to find the list part
    # We search for the pattern. If multiple, maybe the last one?
    # Actually, "including" might appear earlier? No, usually "range of services including..."
    
    matches = list(re.finditer(regex_pattern, desc, re.IGNORECASE))
    if matches:
        # Take the last match as it's likely closest to the list at the end
        match = matches[-1]
        cats_str = match.group(1)
        
        # Clean up quotes
        cats_str = cats_str.replace("'", "").replace('"', "")
        
        # Split by comma
        parts = cats_str.split(',')
        cleaned_cats = []
        for i, part in enumerate(parts):
            p = part.strip()
            # Handle "and X"
            if ' and ' in p:
                # "Home & Garden" -> keep
                # "X, Y, and Z" -> The last part is "and Z".
                # But "Bed & Breakfast" uses "&".
                # "and" usually separates the last item.
                # If it starts with "and ", remove it.
                if p.lower().startswith('and '):
                    p = p[4:].strip()
                # What if "X and Y"? "Movers and Packers"?
                # Usually Yelp categories are distinct.
                # If "and" is in the middle, it might be a category name like "Bed & Breakfast" (usually &).
                # If it says "Fast Food and Burgers", it's two categories?
                # The text says "Fast Food, Restaurants, Coffee & Tea, Food, and Burgers".
                # So "and Burgers" is the last item.
                pass
            
            # Remove "the categories of" or similar if captured?
            # The regex consumes the anchor.
            
            if p:
                cleaned_cats.append(p)
        
        for cat in cleaned_cats:
            # Normalize category name? (Capitalize?)
            # Yelp categories are usually Camel Case.
            # Let's keep as is but strip.
            if cat.lower() == "the": continue # glitch
            category_counts[cat] = category_counts.get(cat, 0) + count
    else:
        # Fallback or log?
        # Maybe "destination for X"?
        match = re.search(r"destination for (.*?)(?:\.$|$)", desc, re.IGNORECASE)
        if match:
             cats_str = match.group(1).replace("'", "")
             parts = cats_str.split(',')
             for p in parts:
                 p = p.strip()
                 if p.lower().startswith('and '): p = p[4:].strip()
                 if p: category_counts[p] = category_counts.get(p, 0) + count

sorted_cats = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)
print("__RESULT__:")
print(json.dumps(sorted_cats))"""

env_args = {'var_function-call-394759627508976658': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-4854865074449366240': [{'business_ref': 'businessref_13', 'review_count': '1'}, {'business_ref': 'businessref_79', 'review_count': '1'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_9', 'review_count': '1'}, {'business_ref': 'businessref_33', 'review_count': '3'}, {'business_ref': 'businessref_15', 'review_count': '1'}, {'business_ref': 'businessref_36', 'review_count': '2'}, {'business_ref': 'businessref_60', 'review_count': '2'}, {'business_ref': 'businessref_12', 'review_count': '1'}, {'business_ref': 'businessref_31', 'review_count': '1'}, {'business_ref': 'businessref_6', 'review_count': '2'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_51', 'review_count': '2'}, {'business_ref': 'businessref_92', 'review_count': '2'}, {'business_ref': 'businessref_26', 'review_count': '1'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_45', 'review_count': '3'}, {'business_ref': 'businessref_96', 'review_count': '2'}, {'business_ref': 'businessref_98', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}, {'business_ref': 'businessref_8', 'review_count': '1'}, {'business_ref': 'businessref_57', 'review_count': '2'}, {'business_ref': 'businessref_86', 'review_count': '1'}, {'business_ref': 'businessref_97', 'review_count': '1'}, {'business_ref': 'businessref_62', 'review_count': '1'}, {'business_ref': 'businessref_72', 'review_count': '1'}, {'business_ref': 'businessref_37', 'review_count': '1'}], 'var_function-call-6691035616520908423': {'business_ids': ['businessid_13', 'businessid_79', 'businessid_74', 'businessid_66', 'businessid_9', 'businessid_33', 'businessid_15', 'businessid_36', 'businessid_60', 'businessid_12', 'businessid_31', 'businessid_6', 'businessid_53', 'businessid_51', 'businessid_92', 'businessid_26', 'businessid_68', 'businessid_45', 'businessid_96', 'businessid_98', 'businessid_14', 'businessid_20', 'businessid_41', 'businessid_10', 'businessid_8', 'businessid_57', 'businessid_86', 'businessid_97', 'businessid_62', 'businessid_72', 'businessid_37'], 'reviews_map': {'businessid_13': '1', 'businessid_79': '1', 'businessid_74': '2', 'businessid_66': '2', 'businessid_9': '1', 'businessid_33': '3', 'businessid_15': '1', 'businessid_36': '2', 'businessid_60': '2', 'businessid_12': '1', 'businessid_31': '1', 'businessid_6': '2', 'businessid_53': '1', 'businessid_51': '2', 'businessid_92': '2', 'businessid_26': '1', 'businessid_68': '1', 'businessid_45': '3', 'businessid_96': '2', 'businessid_98': '1', 'businessid_14': '1', 'businessid_20': '1', 'businessid_41': '1', 'businessid_10': '1', 'businessid_8': '1', 'businessid_57': '2', 'businessid_86': '1', 'businessid_97': '1', 'businessid_62': '1', 'businessid_72': '1', 'businessid_37': '1'}}, 'var_function-call-4986375679061116475': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-3374111026376784924': [['Nail Salons', 3], ['Hair Removal', 3], ['Beauty & Spas', 3], ['Waxing', 3], ['Internal Medicine', 1]], 'var_function-call-10101634130258073621': [{'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}], 'var_function-call-2958204850641891544': [{'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}, {'_id': '6859a000fe8b31cd7362e2b8', 'business_id': 'businessid_8', 'description': 'This Philadelphia, PA location offers a range of services including Hotels & Travel, Taxis, Transportation, Local Services, and Automotive to meet all your travel and transportation needs.'}, {'_id': '6859a000fe8b31cd7362e2c1', 'business_id': 'businessid_26', 'description': 'Located at 7003 Seminole Blvd in Seminole, FL, this establishment specializes in a variety of offerings, including Fast Food, Restaurants, Coffee & Tea, Food, and Burgers, making it a convenient stop for a quick meal or a refreshing beverage.'}, {'_id': '6859a000fe8b31cd7362e2c8', 'business_id': 'businessid_97', 'description': 'Located at 560 Cottman Ave in Cheltenham, PA, this establishment specializes in Body Shops, Automotive services to meet all your vehicle repair needs.'}, {'_id': '6859a000fe8b31cd7362e2c9', 'business_id': 'businessid_14', 'description': "Located at 7055 Marketplace Dr in Goleta, CA, this store offers a diverse selection of products across various categories, including Women's Clothing, Fashion, Department Stores, Home Decor, Home & Garden, Shopping, Men's Clothing, and Discount Store."}, {'_id': '6859a000fe8b31cd7362e2cd', 'business_id': 'businessid_57', 'description': 'Located at 13605 W Hillsborough Ave in Tampa, FL, this versatile establishment offers a range of services and dining options, including Movers, American (New), Landscape Architects, Food, Home Services, Self Storage, Local Services, Restaurants.'}, {'_id': '6859a000fe8b31cd7362e2d6', 'business_id': 'businessid_51', 'description': 'Situated at 3109 N Ola Ave in Tampa, FL, this establishment offers a range of services in the hospitality sector, including Hotels & Travel, Hostels, Bed & Breakfast, Hotels, and Event Planning & Services.'}, {'_id': '6859a000fe8b31cd7362e2db', 'business_id': 'businessid_45', 'description': 'Located at 2900 4th St N in St. Petersburg, FL, this establishment offers a diverse range of products and services in the categories of Food, Grocery, Shopping.'}, {'_id': '6859a000fe8b31cd7362e2dc', 'business_id': 'businessid_68', 'description': 'Located at 593 Brandon Town Ctr in Brandon, FL, this establishment offers a range of services in the categories of Beauty & Spas, Hair Removal, and Eyebrow Services.'}, {'_id': '6859a000fe8b31cd7362e2dd', 'business_id': 'businessid_6', 'description': 'Located at 246 W 1st St in Reno, NV, this vibrant destination offers a delightful mix of Restaurants, Breakfast & Brunch, Bars, Wine Bars, Coffee & Tea, Food, Cafes, Sandwiches, and Nightlife, making it an ideal spot for any meal or occasion.'}, {'_id': '6859a000fe8b31cd7362e2e0', 'business_id': 'businessid_79', 'description': 'Located at 838-842 Christian St in Philadelphia, PA, this establishment offers a wide range of services including Pet Groomers, Pet Stores, Pet Training, Dog Walkers, Pet Services, Pets, and Pet Sitting.'}, {'_id': '6859a000fe8b31cd7362e2e1', 'business_id': 'businessid_66', 'description': 'Located at 3849 State St. Space I-58 in Santa Barbara, CA, this establishment offers a variety of quick and delicious options in the categories of Fast Food, Chinese, Restaurants.'}, {'_id': '6859a000fe8b31cd7362e2e5', 'business_id': 'businessid_15', 'description': 'Located at 3803 Gen Degaulle Dr in New Orleans, LA, this establishment specializes in Automotive, Oil Change Stations, providing efficient service for all your vehicle maintenance needs.'}, {'_id': '6859a000fe8b31cd7362e2e6', 'business_id': 'businessid_96', 'description': 'Located at 3257 Ivanhoe Ave in Saint Louis, MO, this establishment offers a vibrant atmosphere perfect for enjoying a diverse selection of experiences, including Wine Bars, American (New), Cocktail Bars, Restaurants, American (Traditional), Nightlife, and Bars.'}, {'_id': '6859a000fe8b31cd7362e2ed', 'business_id': 'businessid_86', 'description': 'Located at 705 East Passyunk Ave in Philadelphia, PA, this vibrant eatery offers a diverse menu featuring American (New), Restaurants, American (Traditional), Asian Fusion, Noodles, Dim Sum, Fast Food, Chinese, catering to a variety of tastes and preferences.'}, {'_id': '6859a000fe8b31cd7362e2ee', 'business_id': 'businessid_53', 'description': 'Located at 1040 N American St, Ste 1101 in Philadelphia, PA, this eatery offers a diverse menu featuring Salad, Sandwiches, Restaurants, and Burgers.'}, {'_id': '6859a000fe8b31cd7362e2f2', 'business_id': 'businessid_72', 'description': 'Located at 1913 Foggy Ridge Pkwy in Lutz, FL, this establishment specializes in Auto Repair, Car Dealers, Automotive services, providing comprehensive solutions for all your vehicle needs.'}, {'_id': '6859a000fe8b31cd7362e2f3', 'business_id': 'businessid_9', 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}, {'_id': '6859a000fe8b31cd7362e2f4', 'business_id': 'businessid_20', 'description': 'Located at 9040 State Road 54 in Trinity, FL, this establishment offers a diverse array of options, including Restaurants, American (New), Caterers, Fast Food, Chicken Shop, Event Planning & Services, and American (Traditional).'}, {'_id': '6859a000fe8b31cd7362e2f5', 'business_id': 'businessid_37', 'description': 'Located at 13122 N Dale Mabry Hwy in Tampa, FL, this facility offers a comprehensive range of services in Fitness & Instruction, Gyms, Boot Camps, Trainers, Active Life, and Interval Training Gyms.'}, {'_id': '6859a000fe8b31cd7362e2f7', 'business_id': 'businessid_62', 'description': 'Located at 8424 Sheldon Rd in Tampa, FL, this establishment offers a diverse range of products and services, including Photography Stores & Services, Shopping, Grocery, and Food.'}, {'_id': '6859a000fe8b31cd7362e2fb', 'business_id': 'businessid_31', 'description': 'Located at 1234 Pasadena Ave S in South Pasadena, FL, this business specializes in Automotive services, offering a comprehensive Car Wash and professional Auto Detailing to keep your vehicle looking its best.'}, {'_id': '6859a000fe8b31cd7362e300', 'business_id': 'businessid_12', 'description': 'Located at 7704 Calgary Trail S in Edmonton, AB, this vibrant spot offers a diverse experience with options for Pubs, Restaurants, Nightlife, Burgers, Seafood, and Bars.'}, {'_id': '6859a000fe8b31cd7362e302', 'business_id': 'businessid_60', 'description': 'Located at 8101 W Judge Perez Dr in Chalmette, LA, this versatile establishment offers a wide range of options for customers, including Food, Shopping, Fashion, Discount Store, Grocery, Electronics, Drugstores, Department Stores, ensuring that visitors can find everything they need in one convenient location.'}, {'_id': '6859a000fe8b31cd7362e304', 'business_id': 'businessid_98', 'description': 'Situated at 600 Red Lion Rd in Philadelphia, PA, this establishment offers a range of services in Real Estate, Apartments, and Home Services.'}, {'_id': '6859a000fe8b31cd7362e308', 'business_id': 'businessid_36', 'description': "Located at 47 Easton Rd in Willow Grove, PA, this inviting establishment offers a delightful menu featuring authentic flavors in the categories of 'Restaurants, Vietnamese'."}, {'_id': '6859a000fe8b31cd7362e30d', 'business_id': 'businessid_13', 'description': 'Located at 3545 Almaville Rd in Smyrna, TN, this establishment offers a delightful experience encompassing Food, Arts & Entertainment, Wineries, and a Wine Tasting Room.'}]}

exec(code, env_args)
