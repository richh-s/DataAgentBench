code = """import json
import re

# Load data
# Re-load sql_data because previous local context might be fresh or not.
sql_data = locals()['var_function-call-700104084572947078'] 
mongo_data = locals()['var_function-call-7035236905111544362'] # This has 31 items

counts_map = {}
for row in sql_data:
    bid = row['business_ref'].replace('businessref_', 'businessid_')
    counts_map[bid] = int(row['count'])

category_counts = {}

def extract_categories(desc):
    patterns = [
        r"services in the categories of (.*)", # "categories of" might be preceded by "in the"
        r"services in the category of (.*)",
        r"services in (.*)",
        r"services including (.*)",
        r"seeking (.*)",
        r"specializes in (.*)", # "specializes in a variety of offerings, including"
        r"options, including (.*)", # "options, including"
        r"encompassing (.*)", # "encompassing Food, ..."
        r"featuring (.*)", # "featuring American (New)..."
        r"mix of (.*)" # "mix of Restaurants..."
    ]
    
    # The previous patterns were a bit simple. Let's refine based on examples.
    # Examples:
    # "... services in Internal Medicine, Doctors, Health & Medical." -> "Internal Medicine..."
    # "... services including Nail Salons..." -> "Nail Salons..."
    # "... seeking Candy Stores..." -> "Candy Stores..."
    # "... category of 'Restaurants, Chinese'." -> "'Restaurants, Chinese'"
    # "... including Fast Food..." -> "Fast Food..."
    # "... specializes in Body Shops, Automotive services..." -> "Body Shops, Automotive services" (remove "services" at end? No, "Automotive services" might be category)
    # Wait, "Automotive services" in example 8: "Body Shops, Automotive services to meet all your..."
    # My regex will capture "Body Shops, Automotive services to meet all your vehicle repair needs."
    # I need to stop at " to meet" or similar?
    # Or just assume the list ends at the end of the sentence?
    # In example 8: "specializes in Body Shops, Automotive services to meet all your vehicle repair needs."
    # The categories are likely "Body Shops", "Automotive". "services" might be part of "Automotive services" or text.
    # Actually, in Yelp, "Automotive" is a category. "Body Shops" is a category.
    # The text says "... to meet all your vehicle repair needs."
    # I should cut off at certain keywords like " to ", " making it", " ensuring", " perfect for".
    
    # Let's try to extract the whole sentence part after the keyword, then truncate at " to ", " making ", " ensuring ", " perfect ".
    
    # Revised patterns order matters. longer matches first?
    
    text_part = None
    
    # Normalize text to simplify regex
    desc_norm = desc
    
    # Specific patterns
    match_patterns = [
        r"services in the categories of (.*)",
        r"services in the category of (.*)",
        r"services in (.*)",
        r"services including (.*)",
        r"seeking (.*)",
        r"offerings, including (.*)",
        r"options, including (.*)",
        r"encompassing (.*)",
        r"featuring (.*)",
        r"mix of (.*)",
        r"specializes in (.*)"
    ]
    
    for pat in match_patterns:
        match = re.search(pat, desc_norm)
        if match:
            text_part = match.group(1)
            # If "specializes in", we might match "a variety of offerings, including..."
            # So if text_part starts with "a variety...", we recurse or ignore?
            if "including" in text_part and "specializes in" in pat:
                # Let the "including" pattern catch it later or handle it here?
                # Actually, if we matched "specializes in", we get "a variety of offerings, including X, Y...".
                # We should look for "including" inside text_part.
                m2 = re.search(r"including (.*)", text_part)
                if m2:
                    text_part = m2.group(1)
            break
            
    if not text_part:
        return []

    # Truncate at common non-category phrases
    stop_phrases = [" to meet", " making it", " ensuring", " perfect for", " providing", " with options"]
    for phrase in stop_phrases:
        if phrase in text_part:
            text_part = text_part.split(phrase)[0]
    
    # Remove trailing dot
    if text_part.endswith('.'):
        text_part = text_part[:-1]
    
    # Remove quotes
    text_part = text_part.replace("'", "")
    
    # Split
    cats = [c.strip() for c in text_part.split(',')]
    
    # Clean "and "
    cleaned_cats = []
    for c in cats:
        if c.startswith('and '):
            c = c[4:]
        # Remove "services" if it's strictly "services" or at the end of "Automotive services"?
        # Actually "Automotive" is the category. "Automotive services" might be "Automotive" + word "services".
        # But if the text is "Automotive services", maybe I should keep it?
        # Let's keep it as is, usually Yelp categories are clean words.
        # But wait, in "Body Shops, Automotive services", "Automotive services" -> "Automotive"?
        # In example 1: "Internal Medicine, Doctors, Health & Medical". Clean.
        # Example 8: "Body Shops, Automotive services".
        # If I keep "Automotive services", it might not match "Automotive".
        # But I don't have a canonical list.
        # Let's try to strip " services" from the end of category if it exists?
        # Only if "Automotive services" is not a category.
        # Let's assume the text is mostly correct.
        
        # Another cleanup: "in the fields of "
        if "in the fields of " in c:
            c = c.replace("in the fields of ", "")
            
        cleaned_cats.append(c.strip())
        
    return cleaned_cats

# Process
matched_count = 0
for bus in mongo_data:
    bid = bus.get('business_id')
    desc = bus.get('description', '')
    
    if bid in counts_map:
        matched_count += 1
        count = counts_map[bid]
        cats = extract_categories(desc)
        for cat in cats:
            if not cat: continue
            category_counts[cat] = category_counts.get(cat, 0) + count

# Sort
sorted_cats = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)
top_5 = sorted_cats[:5]

print("__RESULT__:")
print(json.dumps({
    "top_5": top_5,
    "matched_businesses": matched_count
}))"""

env_args = {'var_function-call-12603055113156843865': ['review', 'tip', 'user'], 'var_function-call-700104084572947078': [{'business_ref': 'businessref_13', 'count': '1'}, {'business_ref': 'businessref_79', 'count': '1'}, {'business_ref': 'businessref_6', 'count': '2'}, {'business_ref': 'businessref_74', 'count': '2'}, {'business_ref': 'businessref_66', 'count': '2'}, {'business_ref': 'businessref_9', 'count': '1'}, {'business_ref': 'businessref_33', 'count': '3'}, {'business_ref': 'businessref_15', 'count': '1'}, {'business_ref': 'businessref_36', 'count': '2'}, {'business_ref': 'businessref_60', 'count': '2'}, {'business_ref': 'businessref_12', 'count': '1'}, {'business_ref': 'businessref_31', 'count': '1'}, {'business_ref': 'businessref_53', 'count': '1'}, {'business_ref': 'businessref_51', 'count': '2'}, {'business_ref': 'businessref_8', 'count': '1'}, {'business_ref': 'businessref_57', 'count': '2'}, {'business_ref': 'businessref_86', 'count': '1'}, {'business_ref': 'businessref_97', 'count': '1'}, {'business_ref': 'businessref_62', 'count': '1'}, {'business_ref': 'businessref_72', 'count': '1'}, {'business_ref': 'businessref_37', 'count': '1'}, {'business_ref': 'businessref_92', 'count': '2'}, {'business_ref': 'businessref_26', 'count': '1'}, {'business_ref': 'businessref_68', 'count': '1'}, {'business_ref': 'businessref_41', 'count': '1'}, {'business_ref': 'businessref_10', 'count': '1'}, {'business_ref': 'businessref_96', 'count': '2'}, {'business_ref': 'businessref_98', 'count': '1'}, {'business_ref': 'businessref_14', 'count': '1'}, {'business_ref': 'businessref_20', 'count': '1'}, {'business_ref': 'businessref_45', 'count': '3'}], 'var_function-call-15859765085273258938': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-15860727362228958578': {'business_id': {'$in': ['businessid_13', 'businessid_79', 'businessid_6', 'businessid_74', 'businessid_66', 'businessid_9', 'businessid_33', 'businessid_15', 'businessid_36', 'businessid_60', 'businessid_12', 'businessid_31', 'businessid_53', 'businessid_51', 'businessid_8', 'businessid_57', 'businessid_86', 'businessid_97', 'businessid_62', 'businessid_72', 'businessid_37', 'businessid_92', 'businessid_26', 'businessid_68', 'businessid_41', 'businessid_10', 'businessid_96', 'businessid_98', 'businessid_14', 'businessid_20', 'businessid_45']}}, 'var_function-call-18445929683046463822': [{'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}], 'var_function-call-9733503455671904259': {'top_5': [['Nail Salons', 3], ['Hair Removal', 3], ['Beauty & Spas', 3], ['Waxing', 3], ['Candy Stores', 2]], 'total_sql_businesses': 31, 'total_mongo_businesses': 5, 'matched_businesses': 5}, 'var_function-call-7035236905111544362': [{'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}, {'_id': '6859a000fe8b31cd7362e2b8', 'business_id': 'businessid_8', 'description': 'This Philadelphia, PA location offers a range of services including Hotels & Travel, Taxis, Transportation, Local Services, and Automotive to meet all your travel and transportation needs.'}, {'_id': '6859a000fe8b31cd7362e2c1', 'business_id': 'businessid_26', 'description': 'Located at 7003 Seminole Blvd in Seminole, FL, this establishment specializes in a variety of offerings, including Fast Food, Restaurants, Coffee & Tea, Food, and Burgers, making it a convenient stop for a quick meal or a refreshing beverage.'}, {'_id': '6859a000fe8b31cd7362e2c8', 'business_id': 'businessid_97', 'description': 'Located at 560 Cottman Ave in Cheltenham, PA, this establishment specializes in Body Shops, Automotive services to meet all your vehicle repair needs.'}, {'_id': '6859a000fe8b31cd7362e2c9', 'business_id': 'businessid_14', 'description': "Located at 7055 Marketplace Dr in Goleta, CA, this store offers a diverse selection of products across various categories, including Women's Clothing, Fashion, Department Stores, Home Decor, Home & Garden, Shopping, Men's Clothing, and Discount Store."}, {'_id': '6859a000fe8b31cd7362e2cd', 'business_id': 'businessid_57', 'description': 'Located at 13605 W Hillsborough Ave in Tampa, FL, this versatile establishment offers a range of services and dining options, including Movers, American (New), Landscape Architects, Food, Home Services, Self Storage, Local Services, Restaurants.'}, {'_id': '6859a000fe8b31cd7362e2d6', 'business_id': 'businessid_51', 'description': 'Situated at 3109 N Ola Ave in Tampa, FL, this establishment offers a range of services in the hospitality sector, including Hotels & Travel, Hostels, Bed & Breakfast, Hotels, and Event Planning & Services.'}, {'_id': '6859a000fe8b31cd7362e2db', 'business_id': 'businessid_45', 'description': 'Located at 2900 4th St N in St. Petersburg, FL, this establishment offers a diverse range of products and services in the categories of Food, Grocery, Shopping.'}, {'_id': '6859a000fe8b31cd7362e2dc', 'business_id': 'businessid_68', 'description': 'Located at 593 Brandon Town Ctr in Brandon, FL, this establishment offers a range of services in the categories of Beauty & Spas, Hair Removal, and Eyebrow Services.'}, {'_id': '6859a000fe8b31cd7362e2dd', 'business_id': 'businessid_6', 'description': 'Located at 246 W 1st St in Reno, NV, this vibrant destination offers a delightful mix of Restaurants, Breakfast & Brunch, Bars, Wine Bars, Coffee & Tea, Food, Cafes, Sandwiches, and Nightlife, making it an ideal spot for any meal or occasion.'}, {'_id': '6859a000fe8b31cd7362e2e0', 'business_id': 'businessid_79', 'description': 'Located at 838-842 Christian St in Philadelphia, PA, this establishment offers a wide range of services including Pet Groomers, Pet Stores, Pet Training, Dog Walkers, Pet Services, Pets, and Pet Sitting.'}, {'_id': '6859a000fe8b31cd7362e2e1', 'business_id': 'businessid_66', 'description': 'Located at 3849 State St. Space I-58 in Santa Barbara, CA, this establishment offers a variety of quick and delicious options in the categories of Fast Food, Chinese, Restaurants.'}, {'_id': '6859a000fe8b31cd7362e2e5', 'business_id': 'businessid_15', 'description': 'Located at 3803 Gen Degaulle Dr in New Orleans, LA, this establishment specializes in Automotive, Oil Change Stations, providing efficient service for all your vehicle maintenance needs.'}, {'_id': '6859a000fe8b31cd7362e2e6', 'business_id': 'businessid_96', 'description': 'Located at 3257 Ivanhoe Ave in Saint Louis, MO, this establishment offers a vibrant atmosphere perfect for enjoying a diverse selection of experiences, including Wine Bars, American (New), Cocktail Bars, Restaurants, American (Traditional), Nightlife, and Bars.'}, {'_id': '6859a000fe8b31cd7362e2ed', 'business_id': 'businessid_86', 'description': 'Located at 705 East Passyunk Ave in Philadelphia, PA, this vibrant eatery offers a diverse menu featuring American (New), Restaurants, American (Traditional), Asian Fusion, Noodles, Dim Sum, Fast Food, Chinese, catering to a variety of tastes and preferences.'}, {'_id': '6859a000fe8b31cd7362e2ee', 'business_id': 'businessid_53', 'description': 'Located at 1040 N American St, Ste 1101 in Philadelphia, PA, this eatery offers a diverse menu featuring Salad, Sandwiches, Restaurants, and Burgers.'}, {'_id': '6859a000fe8b31cd7362e2f2', 'business_id': 'businessid_72', 'description': 'Located at 1913 Foggy Ridge Pkwy in Lutz, FL, this establishment specializes in Auto Repair, Car Dealers, Automotive services, providing comprehensive solutions for all your vehicle needs.'}, {'_id': '6859a000fe8b31cd7362e2f3', 'business_id': 'businessid_9', 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}, {'_id': '6859a000fe8b31cd7362e2f4', 'business_id': 'businessid_20', 'description': 'Located at 9040 State Road 54 in Trinity, FL, this establishment offers a diverse array of options, including Restaurants, American (New), Caterers, Fast Food, Chicken Shop, Event Planning & Services, and American (Traditional).'}, {'_id': '6859a000fe8b31cd7362e2f5', 'business_id': 'businessid_37', 'description': 'Located at 13122 N Dale Mabry Hwy in Tampa, FL, this facility offers a comprehensive range of services in Fitness & Instruction, Gyms, Boot Camps, Trainers, Active Life, and Interval Training Gyms.'}, {'_id': '6859a000fe8b31cd7362e2f7', 'business_id': 'businessid_62', 'description': 'Located at 8424 Sheldon Rd in Tampa, FL, this establishment offers a diverse range of products and services, including Photography Stores & Services, Shopping, Grocery, and Food.'}, {'_id': '6859a000fe8b31cd7362e2fb', 'business_id': 'businessid_31', 'description': 'Located at 1234 Pasadena Ave S in South Pasadena, FL, this business specializes in Automotive services, offering a comprehensive Car Wash and professional Auto Detailing to keep your vehicle looking its best.'}, {'_id': '6859a000fe8b31cd7362e300', 'business_id': 'businessid_12', 'description': 'Located at 7704 Calgary Trail S in Edmonton, AB, this vibrant spot offers a diverse experience with options for Pubs, Restaurants, Nightlife, Burgers, Seafood, and Bars.'}, {'_id': '6859a000fe8b31cd7362e302', 'business_id': 'businessid_60', 'description': 'Located at 8101 W Judge Perez Dr in Chalmette, LA, this versatile establishment offers a wide range of options for customers, including Food, Shopping, Fashion, Discount Store, Grocery, Electronics, Drugstores, Department Stores, ensuring that visitors can find everything they need in one convenient location.'}, {'_id': '6859a000fe8b31cd7362e304', 'business_id': 'businessid_98', 'description': 'Situated at 600 Red Lion Rd in Philadelphia, PA, this establishment offers a range of services in Real Estate, Apartments, and Home Services.'}, {'_id': '6859a000fe8b31cd7362e308', 'business_id': 'businessid_36', 'description': "Located at 47 Easton Rd in Willow Grove, PA, this inviting establishment offers a delightful menu featuring authentic flavors in the categories of 'Restaurants, Vietnamese'."}, {'_id': '6859a000fe8b31cd7362e30d', 'business_id': 'businessid_13', 'description': 'Located at 3545 Almaville Rd in Smyrna, TN, this establishment offers a delightful experience encompassing Food, Arts & Entertainment, Wineries, and a Wine Tasting Room.'}]}

exec(code, env_args)
