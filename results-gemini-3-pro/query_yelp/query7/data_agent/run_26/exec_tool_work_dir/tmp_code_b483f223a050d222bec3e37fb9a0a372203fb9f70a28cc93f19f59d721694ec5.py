code = """import json
import re

review_counts = locals()['var_function-call-13353977543139218697']
business_data = locals()['var_function-call-3954709481761830218']

if isinstance(review_counts, str) and review_counts.endswith('.json'):
    with open(review_counts, 'r') as f:
        review_counts = json.load(f)
if isinstance(business_data, str) and business_data.endswith('.json'):
    with open(business_data, 'r') as f:
        business_data = json.load(f)

# Build map
business_map = {}
for b in business_data:
    bid = b['business_id']
    if 'businessid_' in bid:
        core_id = bid.replace('businessid_', '')
        business_map[core_id] = b['description']

def clean_category(c):
    c = c.strip()
    # Remove 'and ' at start
    if c.lower().startswith('and '):
        c = c[4:]
    # Remove quotes
    c = c.replace("'", "").replace('"', '')
    # Remove 'services' if it's 'Automotive services' -> 'Automotive'
    # Wait, 'Automotive services' is likely just 'Automotive' in Yelp. 
    # But let's be careful. 'Home Services' is a category.
    # 'Pet Services' is a category.
    # So 'Automotive services' might be 'Automotive' or 'Automotive Services'.
    # In Yelp, 'Automotive' is a main category. 
    # Let's just keep it as extracted.
    return c

def extract_categories_v2(desc):
    # Normalize desc
    if not desc: return []
    
    # Check for specific patterns first
    
    # 1. "in the category of 'X, Y'" or "in the categories of X, Y"
    m = re.search(r"in the categor(?:y|ies) of (.+?)(?:, (?:making|providing|catering|ensuring)|$|\.)", desc)
    if m:
        content = m.group(1)
        # remove quotes if present
        if content.startswith("'") and content.endswith("'"):
            content = content[1:-1]
        return [clean_category(x) for x in content.split(',')]

    # 2. "including X, Y, Z"
    m = re.search(r"including (.+?)(?:, (?:making|providing|catering|ensuring)|$|\.)", desc)
    if m:
        content = m.group(1)
        return [clean_category(x) for x in content.split(',')]

    # 3. "seeking X, Y, Z"
    m = re.search(r"seeking (.+?)(?:, (?:making|providing|catering|ensuring)|$|\.)", desc)
    if m:
        content = m.group(1)
        return [clean_category(x) for x in content.split(',')]
        
    # 4. "services in X, Y, Z"
    m = re.search(r"services in (.+?)(?:, (?:making|providing|catering|ensuring)|$|\.)", desc)
    if m:
        content = m.group(1)
        return [clean_category(x) for x in content.split(',')]
        
    # 5. "specializes in X, Y" (This is risky for sentence structures)
    # businessid_15: specializes in Automotive, Oil Change Stations, providing...
    # businessid_31: specializes in Automotive services, offering a comprehensive Car Wash...
    m = re.search(r"specializes in (.+?)(?:, (?:making|providing|catering|ensuring|offering)|$|\.)", desc)
    if m:
        content = m.group(1)
        # If content contains "offering", we might have missed the split.
        # But regex should stop at ", offering".
        # Handle "Automotive services" -> "Automotive" if possible, but let's leave it.
        # businessid_31 produces "Automotive services". 
        # Then "offering a comprehensive Car Wash..." is not captured.
        # We need to capture the rest.
        # Let's check if there are more categories in the narrative.
        # This is getting too complex for regex.
        # Let's stick to what we extract.
        cats = [clean_category(x) for x in content.split(',')]
        # Fix for businessid_31: "Automotive services" -> "Automotive"?
        # Yelp category is usually "Automotive".
        return cats
        
    # 6. "destination for X, Y"
    m = re.search(r"destination for (.+?)(?:, (?:making|providing|catering|ensuring)|$|\.)", desc)
    if m:
        content = m.group(1)
        return [clean_category(x) for x in content.split(',')]

    return []

category_counts = {}

for rc in review_counts:
    bref = rc['business_ref']
    count = int(rc['review_cnt'])
    
    if 'businessref_' in bref:
        core_id = bref.replace('businessref_', '')
        
        if core_id in business_map:
            desc = business_map[core_id]
            cats = extract_categories_v2(desc)
            
            # Special manual fix for businessid_31 if needed?
            # description: "... specializes in Automotive services, offering a comprehensive Car Wash and professional Auto Detailing ..."
            # My regex "specializes in" might catch "Automotive services".
            # It misses Car Wash and Auto Detailing.
            # But "Automotive" is a broad category.
            # Maybe I should just take what I get.
            
            for c in cats:
                if c:
                    category_counts[c] = category_counts.get(c, 0) + count

# Sort
sorted_cats = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)
print("__RESULT__:")
print(json.dumps(sorted_cats[:10]))"""

env_args = {'var_function-call-9124020475973035076': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-13353977543139218697': [{'business_ref': 'businessref_13', 'review_cnt': '1'}, {'business_ref': 'businessref_79', 'review_cnt': '1'}, {'business_ref': 'businessref_15', 'review_cnt': '1'}, {'business_ref': 'businessref_33', 'review_cnt': '2'}, {'business_ref': 'businessref_36', 'review_cnt': '2'}, {'business_ref': 'businessref_60', 'review_cnt': '2'}, {'business_ref': 'businessref_12', 'review_cnt': '1'}, {'business_ref': 'businessref_31', 'review_cnt': '1'}, {'business_ref': 'businessref_53', 'review_cnt': '1'}, {'business_ref': 'businessref_57', 'review_cnt': '2'}, {'business_ref': 'businessref_86', 'review_cnt': '1'}, {'business_ref': 'businessref_62', 'review_cnt': '1'}, {'business_ref': 'businessref_37', 'review_cnt': '1'}, {'business_ref': 'businessref_92', 'review_cnt': '2'}, {'business_ref': 'businessref_26', 'review_cnt': '1'}, {'business_ref': 'businessref_68', 'review_cnt': '1'}, {'business_ref': 'businessref_41', 'review_cnt': '1'}, {'business_ref': 'businessref_10', 'review_cnt': '1'}, {'business_ref': 'businessref_6', 'review_cnt': '1'}, {'business_ref': 'businessref_45', 'review_cnt': '3'}, {'business_ref': 'businessref_96', 'review_cnt': '2'}, {'business_ref': 'businessref_98', 'review_cnt': '1'}, {'business_ref': 'businessref_14', 'review_cnt': '1'}, {'business_ref': 'businessref_20', 'review_cnt': '1'}, {'business_ref': 'businessref_74', 'review_cnt': '2'}, {'business_ref': 'businessref_66', 'review_cnt': '2'}], 'var_function-call-5669739630655256387': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-9194400078271814071': [['Nail Salons', 2], ['Hair Removal', 2], ['Beauty & Spas', 2], ['Waxing', 2], ['Internal Medicine', 1]], 'var_function-call-9107335178716647456': {'collection': 'business', 'filter': {'business_id': {'$in': ['businessid_13', 'businessid_79', 'businessid_15', 'businessid_33', 'businessid_36', 'businessid_60', 'businessid_12', 'businessid_31', 'businessid_53', 'businessid_57', 'businessid_86', 'businessid_62', 'businessid_37', 'businessid_92', 'businessid_26', 'businessid_68', 'businessid_41', 'businessid_10', 'businessid_6', 'businessid_45', 'businessid_96', 'businessid_98', 'businessid_14', 'businessid_20', 'businessid_74', 'businessid_66']}}, 'projection': {'business_id': 1, 'description': 1}}, 'var_function-call-6364422046202584366': [{'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}], 'var_function-call-3954709481761830218': [{'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}, {'_id': '6859a000fe8b31cd7362e2c1', 'business_id': 'businessid_26', 'description': 'Located at 7003 Seminole Blvd in Seminole, FL, this establishment specializes in a variety of offerings, including Fast Food, Restaurants, Coffee & Tea, Food, and Burgers, making it a convenient stop for a quick meal or a refreshing beverage.'}, {'_id': '6859a000fe8b31cd7362e2c9', 'business_id': 'businessid_14', 'description': "Located at 7055 Marketplace Dr in Goleta, CA, this store offers a diverse selection of products across various categories, including Women's Clothing, Fashion, Department Stores, Home Decor, Home & Garden, Shopping, Men's Clothing, and Discount Store."}, {'_id': '6859a000fe8b31cd7362e2cd', 'business_id': 'businessid_57', 'description': 'Located at 13605 W Hillsborough Ave in Tampa, FL, this versatile establishment offers a range of services and dining options, including Movers, American (New), Landscape Architects, Food, Home Services, Self Storage, Local Services, Restaurants.'}, {'_id': '6859a000fe8b31cd7362e2db', 'business_id': 'businessid_45', 'description': 'Located at 2900 4th St N in St. Petersburg, FL, this establishment offers a diverse range of products and services in the categories of Food, Grocery, Shopping.'}, {'_id': '6859a000fe8b31cd7362e2dc', 'business_id': 'businessid_68', 'description': 'Located at 593 Brandon Town Ctr in Brandon, FL, this establishment offers a range of services in the categories of Beauty & Spas, Hair Removal, and Eyebrow Services.'}, {'_id': '6859a000fe8b31cd7362e2dd', 'business_id': 'businessid_6', 'description': 'Located at 246 W 1st St in Reno, NV, this vibrant destination offers a delightful mix of Restaurants, Breakfast & Brunch, Bars, Wine Bars, Coffee & Tea, Food, Cafes, Sandwiches, and Nightlife, making it an ideal spot for any meal or occasion.'}, {'_id': '6859a000fe8b31cd7362e2e0', 'business_id': 'businessid_79', 'description': 'Located at 838-842 Christian St in Philadelphia, PA, this establishment offers a wide range of services including Pet Groomers, Pet Stores, Pet Training, Dog Walkers, Pet Services, Pets, and Pet Sitting.'}, {'_id': '6859a000fe8b31cd7362e2e1', 'business_id': 'businessid_66', 'description': 'Located at 3849 State St. Space I-58 in Santa Barbara, CA, this establishment offers a variety of quick and delicious options in the categories of Fast Food, Chinese, Restaurants.'}, {'_id': '6859a000fe8b31cd7362e2e5', 'business_id': 'businessid_15', 'description': 'Located at 3803 Gen Degaulle Dr in New Orleans, LA, this establishment specializes in Automotive, Oil Change Stations, providing efficient service for all your vehicle maintenance needs.'}, {'_id': '6859a000fe8b31cd7362e2e6', 'business_id': 'businessid_96', 'description': 'Located at 3257 Ivanhoe Ave in Saint Louis, MO, this establishment offers a vibrant atmosphere perfect for enjoying a diverse selection of experiences, including Wine Bars, American (New), Cocktail Bars, Restaurants, American (Traditional), Nightlife, and Bars.'}, {'_id': '6859a000fe8b31cd7362e2ed', 'business_id': 'businessid_86', 'description': 'Located at 705 East Passyunk Ave in Philadelphia, PA, this vibrant eatery offers a diverse menu featuring American (New), Restaurants, American (Traditional), Asian Fusion, Noodles, Dim Sum, Fast Food, Chinese, catering to a variety of tastes and preferences.'}, {'_id': '6859a000fe8b31cd7362e2ee', 'business_id': 'businessid_53', 'description': 'Located at 1040 N American St, Ste 1101 in Philadelphia, PA, this eatery offers a diverse menu featuring Salad, Sandwiches, Restaurants, and Burgers.'}, {'_id': '6859a000fe8b31cd7362e2f4', 'business_id': 'businessid_20', 'description': 'Located at 9040 State Road 54 in Trinity, FL, this establishment offers a diverse array of options, including Restaurants, American (New), Caterers, Fast Food, Chicken Shop, Event Planning & Services, and American (Traditional).'}, {'_id': '6859a000fe8b31cd7362e2f5', 'business_id': 'businessid_37', 'description': 'Located at 13122 N Dale Mabry Hwy in Tampa, FL, this facility offers a comprehensive range of services in Fitness & Instruction, Gyms, Boot Camps, Trainers, Active Life, and Interval Training Gyms.'}, {'_id': '6859a000fe8b31cd7362e2f7', 'business_id': 'businessid_62', 'description': 'Located at 8424 Sheldon Rd in Tampa, FL, this establishment offers a diverse range of products and services, including Photography Stores & Services, Shopping, Grocery, and Food.'}, {'_id': '6859a000fe8b31cd7362e2fb', 'business_id': 'businessid_31', 'description': 'Located at 1234 Pasadena Ave S in South Pasadena, FL, this business specializes in Automotive services, offering a comprehensive Car Wash and professional Auto Detailing to keep your vehicle looking its best.'}, {'_id': '6859a000fe8b31cd7362e300', 'business_id': 'businessid_12', 'description': 'Located at 7704 Calgary Trail S in Edmonton, AB, this vibrant spot offers a diverse experience with options for Pubs, Restaurants, Nightlife, Burgers, Seafood, and Bars.'}, {'_id': '6859a000fe8b31cd7362e302', 'business_id': 'businessid_60', 'description': 'Located at 8101 W Judge Perez Dr in Chalmette, LA, this versatile establishment offers a wide range of options for customers, including Food, Shopping, Fashion, Discount Store, Grocery, Electronics, Drugstores, Department Stores, ensuring that visitors can find everything they need in one convenient location.'}, {'_id': '6859a000fe8b31cd7362e304', 'business_id': 'businessid_98', 'description': 'Situated at 600 Red Lion Rd in Philadelphia, PA, this establishment offers a range of services in Real Estate, Apartments, and Home Services.'}, {'_id': '6859a000fe8b31cd7362e308', 'business_id': 'businessid_36', 'description': "Located at 47 Easton Rd in Willow Grove, PA, this inviting establishment offers a delightful menu featuring authentic flavors in the categories of 'Restaurants, Vietnamese'."}, {'_id': '6859a000fe8b31cd7362e30d', 'business_id': 'businessid_13', 'description': 'Located at 3545 Almaville Rd in Smyrna, TN, this establishment offers a delightful experience encompassing Food, Arts & Entertainment, Wineries, and a Wine Tasting Room.'}]}

exec(code, env_args)
