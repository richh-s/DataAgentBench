code = """import json

# Load review counts
counts_data = locals()['var_function-call-12637187437118360065']
if isinstance(counts_data, str):
    counts_data = json.loads(counts_data)
review_counts = counts_data['counts']

# Load business descriptions
desc_data = locals()['var_function-call-3965566035212561558']
if isinstance(desc_data, str):
    if desc_data.endswith('.json'):
        with open(desc_data, 'r') as f:
            businesses = json.load(f)
    else:
        businesses = json.loads(desc_data)
else:
    businesses = desc_data

category_totals = {}

def extract_categories_robust(desc):
    text = desc.strip()
    
    # delimiters to find the start of the list
    delimiters = [
        "services in the fields of ",
        "services in ", 
        "services including ", 
        "seeking ", 
        "category of ",
        "categories of ",
        "featuring ",
        "including ",
        "options for "
    ]
    
    # Find the last delimiter that appears in the text
    # (Using last to avoid earlier "including" if any, though usually only one)
    # Actually, usually the relevant one is the last significant phrase.
    
    start_index = -1
    used_delimiter = ""
    
    for d in delimiters:
        idx = text.rfind(d)
        if idx != -1:
            # We want the rightmost delimiter
            if idx > start_index:
                start_index = idx
                used_delimiter = d
                
    if start_index == -1:
        return []

    # Content after delimiter
    content = text[start_index + len(used_delimiter):]
    
    # Remove single quotes if it looks like 'Category, Category'
    if content.startswith("'") and (content.endswith("'") or content.endswith("'.")):
        # Find ending quote
        end_quote = content.rfind("'")
        if end_quote > 0:
            content = content[1:end_quote]
            
    # Remove trailing period
    if content.endswith('.'):
        content = content[:-1]
        
    # Split by comma
    parts = [p.strip() for p in content.split(',')]
    
    cats = []
    for p in parts:
        # Check if p contains "and "
        # "and Waxing"
        # "and Department Stores"
        # "and Department Stores ensuring..."
        
        # Split by "and " if present
        subparts = p.split(' and ')
        for sp in subparts:
            sp = sp.strip()
            if not sp:
                continue
            
            # Heuristic: Categories are usually capitalized or '&'
            # If a part starts with lowercase and it's not a known connector, maybe we hit the end description?
            # E.g. "ensuring that visitors..."
            if sp[0].islower() and sp not in ['of', 'the']:
                # likely not a category, or end of list reached
                # but "ensuring" came after a comma.
                # If we are in the middle of a list, "and" usually connects the last item.
                # If we found "ensuring" it implies the list ended before.
                continue
            
            # Clean up potential trailing sentence
            # "Department Stores ensuring that..."
            # This is hard. "Department Stores" is a category. "ensuring..." is text.
            # Usually there is a comma before ensuring? "Department Stores, ensuring..."
            # If so, "ensuring that..." would be a separate part in `parts`.
            # And `sp` would be "ensuring that...".
            # So `sp[0].islower()` check handles it.
            
            cats.append(sp)
            
    return cats

for b in businesses:
    bid = b['business_id']
    desc = b.get('description', '')
    
    if bid in review_counts:
        count = review_counts[bid]
        categories = extract_categories_robust(desc)
        
        # print(f"Business: {bid}, Count: {count}, Cats: {categories}")
        
        for cat in categories:
            if cat:
                category_totals[cat] = category_totals.get(cat, 0) + count

sorted_cats = sorted(category_totals.items(), key=lambda x: x[1], reverse=True)

print("__RESULT__:")
print(json.dumps(sorted_cats))"""

env_args = {'var_function-call-15696234175843027394': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-9418626010781047011': [{'business_ref': 'businessref_13', 'review_count': '1'}, {'business_ref': 'businessref_79', 'review_count': '1'}, {'business_ref': 'businessref_6', 'review_count': '2'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_9', 'review_count': '1'}, {'business_ref': 'businessref_33', 'review_count': '3'}, {'business_ref': 'businessref_15', 'review_count': '1'}, {'business_ref': 'businessref_36', 'review_count': '2'}, {'business_ref': 'businessref_60', 'review_count': '2'}, {'business_ref': 'businessref_12', 'review_count': '1'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_51', 'review_count': '2'}, {'business_ref': 'businessref_8', 'review_count': '1'}, {'business_ref': 'businessref_57', 'review_count': '2'}, {'business_ref': 'businessref_86', 'review_count': '1'}, {'business_ref': 'businessref_97', 'review_count': '1'}, {'business_ref': 'businessref_62', 'review_count': '1'}, {'business_ref': 'businessref_72', 'review_count': '1'}, {'business_ref': 'businessref_37', 'review_count': '1'}, {'business_ref': 'businessref_31', 'review_count': '1'}, {'business_ref': 'businessref_26', 'review_count': '1'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}, {'business_ref': 'businessref_45', 'review_count': '3'}, {'business_ref': 'businessref_96', 'review_count': '2'}, {'business_ref': 'businessref_98', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}, {'business_ref': 'businessref_92', 'review_count': '2'}], 'var_function-call-12637187437118360065': {'ids': ['businessid_13', 'businessid_79', 'businessid_6', 'businessid_74', 'businessid_66', 'businessid_9', 'businessid_33', 'businessid_15', 'businessid_36', 'businessid_60', 'businessid_12', 'businessid_53', 'businessid_51', 'businessid_8', 'businessid_57', 'businessid_86', 'businessid_97', 'businessid_62', 'businessid_72', 'businessid_37', 'businessid_31', 'businessid_26', 'businessid_68', 'businessid_41', 'businessid_10', 'businessid_45', 'businessid_96', 'businessid_98', 'businessid_14', 'businessid_20', 'businessid_92'], 'counts': {'businessid_13': 1, 'businessid_79': 1, 'businessid_6': 2, 'businessid_74': 2, 'businessid_66': 2, 'businessid_9': 1, 'businessid_33': 3, 'businessid_15': 1, 'businessid_36': 2, 'businessid_60': 2, 'businessid_12': 1, 'businessid_53': 1, 'businessid_51': 2, 'businessid_8': 1, 'businessid_57': 2, 'businessid_86': 1, 'businessid_97': 1, 'businessid_62': 1, 'businessid_72': 1, 'businessid_37': 1, 'businessid_31': 1, 'businessid_26': 1, 'businessid_68': 1, 'businessid_41': 1, 'businessid_10': 1, 'businessid_45': 3, 'businessid_96': 2, 'businessid_98': 1, 'businessid_14': 1, 'businessid_20': 1, 'businessid_92': 2}}, 'var_function-call-596267005130533481': [{'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}], 'var_function-call-7828907003675331541': [['Nail Salons', 3], ['Hair Removal', 3], ['Beauty & Spas', 3], ['and Waxing', 3], ['Candy Stores', 2]], 'var_function-call-16164348200264985742': [['Nail Salons', 3], ['Hair Removal', 3], ['Beauty & Spas', 3], ['Waxing', 3], ['Candy Stores', 2], ['Specialty Food', 2], ['Food', 2], ['Internal Medicine', 1], ['Doctors', 1], ['Health & Medical', 1]], 'var_function-call-9362242597606982045': {'missing': ['businessid_12', 'businessid_14', 'businessid_79', 'businessid_13', 'businessid_60', 'businessid_45', 'businessid_57', 'businessid_37', 'businessid_98', 'businessid_51', 'businessid_36', 'businessid_62', 'businessid_31', 'businessid_66', 'businessid_97', 'businessid_96', 'businessid_72', 'businessid_20', 'businessid_6', 'businessid_86', 'businessid_9', 'businessid_53', 'businessid_8', 'businessid_68', 'businessid_26', 'businessid_15'], 'b45_desc': 'Not Found'}, 'var_function-call-870437619574113581': [{'_id': '6859a000fe8b31cd7362e2db', 'business_id': 'businessid_45', 'name': 'The Fresh Market', 'review_count': '113', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}", 'RestaurantsPriceRange2': '2', 'BikeParking': 'True', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsTakeOut': 'True', 'DogsAllowed': 'False', 'Caters': 'True', 'NoiseLevel': "u'quiet'", 'GoodForKids': 'True', 'RestaurantsDelivery': 'True'}, 'hours': {'Monday': '8:0-21:0', 'Tuesday': '7:0-22:0', 'Wednesday': '7:0-22:0', 'Thursday': '7:0-16:0', 'Friday': '8:0-21:0', 'Saturday': '8:0-21:0', 'Sunday': '8:0-16:0'}, 'description': 'Located at 2900 4th St N in St. Petersburg, FL, this establishment offers a diverse range of products and services in the categories of Food, Grocery, Shopping.'}], 'var_function-call-3965566035212561558': [{'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}, {'_id': '6859a000fe8b31cd7362e2b8', 'business_id': 'businessid_8', 'description': 'This Philadelphia, PA location offers a range of services including Hotels & Travel, Taxis, Transportation, Local Services, and Automotive to meet all your travel and transportation needs.'}, {'_id': '6859a000fe8b31cd7362e2c1', 'business_id': 'businessid_26', 'description': 'Located at 7003 Seminole Blvd in Seminole, FL, this establishment specializes in a variety of offerings, including Fast Food, Restaurants, Coffee & Tea, Food, and Burgers, making it a convenient stop for a quick meal or a refreshing beverage.'}, {'_id': '6859a000fe8b31cd7362e2c8', 'business_id': 'businessid_97', 'description': 'Located at 560 Cottman Ave in Cheltenham, PA, this establishment specializes in Body Shops, Automotive services to meet all your vehicle repair needs.'}, {'_id': '6859a000fe8b31cd7362e2c9', 'business_id': 'businessid_14', 'description': "Located at 7055 Marketplace Dr in Goleta, CA, this store offers a diverse selection of products across various categories, including Women's Clothing, Fashion, Department Stores, Home Decor, Home & Garden, Shopping, Men's Clothing, and Discount Store."}, {'_id': '6859a000fe8b31cd7362e2cd', 'business_id': 'businessid_57', 'description': 'Located at 13605 W Hillsborough Ave in Tampa, FL, this versatile establishment offers a range of services and dining options, including Movers, American (New), Landscape Architects, Food, Home Services, Self Storage, Local Services, Restaurants.'}, {'_id': '6859a000fe8b31cd7362e2d6', 'business_id': 'businessid_51', 'description': 'Situated at 3109 N Ola Ave in Tampa, FL, this establishment offers a range of services in the hospitality sector, including Hotels & Travel, Hostels, Bed & Breakfast, Hotels, and Event Planning & Services.'}, {'_id': '6859a000fe8b31cd7362e2db', 'business_id': 'businessid_45', 'description': 'Located at 2900 4th St N in St. Petersburg, FL, this establishment offers a diverse range of products and services in the categories of Food, Grocery, Shopping.'}, {'_id': '6859a000fe8b31cd7362e2dc', 'business_id': 'businessid_68', 'description': 'Located at 593 Brandon Town Ctr in Brandon, FL, this establishment offers a range of services in the categories of Beauty & Spas, Hair Removal, and Eyebrow Services.'}, {'_id': '6859a000fe8b31cd7362e2dd', 'business_id': 'businessid_6', 'description': 'Located at 246 W 1st St in Reno, NV, this vibrant destination offers a delightful mix of Restaurants, Breakfast & Brunch, Bars, Wine Bars, Coffee & Tea, Food, Cafes, Sandwiches, and Nightlife, making it an ideal spot for any meal or occasion.'}, {'_id': '6859a000fe8b31cd7362e2e0', 'business_id': 'businessid_79', 'description': 'Located at 838-842 Christian St in Philadelphia, PA, this establishment offers a wide range of services including Pet Groomers, Pet Stores, Pet Training, Dog Walkers, Pet Services, Pets, and Pet Sitting.'}, {'_id': '6859a000fe8b31cd7362e2e1', 'business_id': 'businessid_66', 'description': 'Located at 3849 State St. Space I-58 in Santa Barbara, CA, this establishment offers a variety of quick and delicious options in the categories of Fast Food, Chinese, Restaurants.'}, {'_id': '6859a000fe8b31cd7362e2e5', 'business_id': 'businessid_15', 'description': 'Located at 3803 Gen Degaulle Dr in New Orleans, LA, this establishment specializes in Automotive, Oil Change Stations, providing efficient service for all your vehicle maintenance needs.'}, {'_id': '6859a000fe8b31cd7362e2e6', 'business_id': 'businessid_96', 'description': 'Located at 3257 Ivanhoe Ave in Saint Louis, MO, this establishment offers a vibrant atmosphere perfect for enjoying a diverse selection of experiences, including Wine Bars, American (New), Cocktail Bars, Restaurants, American (Traditional), Nightlife, and Bars.'}, {'_id': '6859a000fe8b31cd7362e2ed', 'business_id': 'businessid_86', 'description': 'Located at 705 East Passyunk Ave in Philadelphia, PA, this vibrant eatery offers a diverse menu featuring American (New), Restaurants, American (Traditional), Asian Fusion, Noodles, Dim Sum, Fast Food, Chinese, catering to a variety of tastes and preferences.'}, {'_id': '6859a000fe8b31cd7362e2ee', 'business_id': 'businessid_53', 'description': 'Located at 1040 N American St, Ste 1101 in Philadelphia, PA, this eatery offers a diverse menu featuring Salad, Sandwiches, Restaurants, and Burgers.'}, {'_id': '6859a000fe8b31cd7362e2f2', 'business_id': 'businessid_72', 'description': 'Located at 1913 Foggy Ridge Pkwy in Lutz, FL, this establishment specializes in Auto Repair, Car Dealers, Automotive services, providing comprehensive solutions for all your vehicle needs.'}, {'_id': '6859a000fe8b31cd7362e2f3', 'business_id': 'businessid_9', 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}, {'_id': '6859a000fe8b31cd7362e2f4', 'business_id': 'businessid_20', 'description': 'Located at 9040 State Road 54 in Trinity, FL, this establishment offers a diverse array of options, including Restaurants, American (New), Caterers, Fast Food, Chicken Shop, Event Planning & Services, and American (Traditional).'}, {'_id': '6859a000fe8b31cd7362e2f5', 'business_id': 'businessid_37', 'description': 'Located at 13122 N Dale Mabry Hwy in Tampa, FL, this facility offers a comprehensive range of services in Fitness & Instruction, Gyms, Boot Camps, Trainers, Active Life, and Interval Training Gyms.'}, {'_id': '6859a000fe8b31cd7362e2f7', 'business_id': 'businessid_62', 'description': 'Located at 8424 Sheldon Rd in Tampa, FL, this establishment offers a diverse range of products and services, including Photography Stores & Services, Shopping, Grocery, and Food.'}, {'_id': '6859a000fe8b31cd7362e2fb', 'business_id': 'businessid_31', 'description': 'Located at 1234 Pasadena Ave S in South Pasadena, FL, this business specializes in Automotive services, offering a comprehensive Car Wash and professional Auto Detailing to keep your vehicle looking its best.'}, {'_id': '6859a000fe8b31cd7362e300', 'business_id': 'businessid_12', 'description': 'Located at 7704 Calgary Trail S in Edmonton, AB, this vibrant spot offers a diverse experience with options for Pubs, Restaurants, Nightlife, Burgers, Seafood, and Bars.'}, {'_id': '6859a000fe8b31cd7362e302', 'business_id': 'businessid_60', 'description': 'Located at 8101 W Judge Perez Dr in Chalmette, LA, this versatile establishment offers a wide range of options for customers, including Food, Shopping, Fashion, Discount Store, Grocery, Electronics, Drugstores, Department Stores, ensuring that visitors can find everything they need in one convenient location.'}, {'_id': '6859a000fe8b31cd7362e304', 'business_id': 'businessid_98', 'description': 'Situated at 600 Red Lion Rd in Philadelphia, PA, this establishment offers a range of services in Real Estate, Apartments, and Home Services.'}, {'_id': '6859a000fe8b31cd7362e308', 'business_id': 'businessid_36', 'description': "Located at 47 Easton Rd in Willow Grove, PA, this inviting establishment offers a delightful menu featuring authentic flavors in the categories of 'Restaurants, Vietnamese'."}, {'_id': '6859a000fe8b31cd7362e30d', 'business_id': 'businessid_13', 'description': 'Located at 3545 Almaville Rd in Smyrna, TN, this establishment offers a delightful experience encompassing Food, Arts & Entertainment, Wineries, and a Wine Tasting Room.'}]}

exec(code, env_args)
