code = """import json
import re

# Load the SQL aggregation result
reviews = var_call_Pjvkr5vqQP0NzVR3RGXEhzen  # list of dicts with business_ref and review_count

# Build mapping from business_ref -> review_count (int)
ref_to_count = {}
for r in reviews:
    ref = r.get('business_ref')
    cnt = int(r.get('review_count'))
    ref_to_count[ref.replace('businessref_', 'businessid_')] = cnt

# List of Mongo query results variables containing business docs
business_vars = [
    var_call_WkUhJeDeYmPgYo7gehrywNQQ,
    var_call_L3lE7BEC3GIqewx2EL6MBLAq,
    var_call_lI0ngjzKJJ7Ik3Q3jXXJ7BPx,
    var_call_6cUZKRtvFkfXNG0jmuI6vRcu,
    var_call_eZak0fxuG6W7OCf5iNM9a7xu,
    var_call_ZSfJDZZJYw8PdzTfLF8qZRla,
    var_call_Ezuu9r5lZfHqOFIabIENLdtI,
    var_call_qpQIypVJhXUvB3r8iS7o087E,
    var_call_hKtkmfJRNiPEuOTHYtQqphCp,
    var_call_AMhLoE4NXLhxqRDhyjVedOlR,
    var_call_0XEyo4lW9YOokJEnQDqbnJ7p,
    var_call_iJ9DHzg1Z0Ofu0OETkvHvHBZ,
    var_call_NPKTUcbCLXJDqaeFLA4KDLYv,
    var_call_avnDK10EEbHcEAjEq0OuIjiC,
    var_call_hYt8VG4EHByJ0Ul4Vjl0vPHq,
    var_call_kR56AAvNswBZeS2oQJ6U9NFC,
    var_call_8llLYyd56yQ7sDCHqpPYoDT4,
    var_call_dVnoAtWpFvK6lAxhyzTWA0lp,
    var_call_eTDWcKHtSSgRnAsgcZgERvPB,
    var_call_YTe3bytoFgCFyZ4CV7kjXprE,
    var_call_8NBFGV8gA5dS40AgulcErmLC,
    var_call_3seNYMyclPbZb0RtHhh71fjS,
    var_call_yRlll9GYvK5lUSDZcdaqXk5v,
    var_call_Kwv8LrBVX9bGK4P3F1G9lrLF,
    var_call_EUzB6cT5x2rNmQjt3MczEOU9,
    var_call_sfWcPgL0e9o1D5pWWUCmkpKK,
]

# Flatten docs
docs = []
for v in business_vars:
    if isinstance(v, list) and len(v) > 0 and isinstance(v[0], dict):
        docs.append(v[0])

# Function to extract categories from description
def extract_categories(desc):
    if not desc or not isinstance(desc, str):
        return []
    # Try several regex patterns to capture the category list
    patterns = [
        r"in the (?:categories|category) of\s*['\"]?(.*?)(?:['\"]?\.|\.|$)",
        r"offers a .* in the (?:categories|category) of\s*['\"]?(.*?)(?:['\"]?\.|\.|$)",
        r"offers a .* range .* in the (?:categories|category) of\s*['\"]?(.*?)(?:['\"]?\.|\.|$)",
    ]
    for pat in patterns:
        m = re.search(pat, desc, flags=re.I)
        if m:
            cats_str = m.group(1)
            # Clean up trailing qualifiers
            cats_str = cats_str.strip()
            # Remove enclosing quotes if any
            if (cats_str.startswith("'") and cats_str.endswith("'")) or (cats_str.startswith('"') and cats_str.endswith('"')):
                cats_str = cats_str[1:-1]
            # Split on commas and ' and '
            parts = re.split(r',|\band\b|&', cats_str)
            cats = [p.strip().strip("'\"") for p in parts if p.strip()]
            return cats
    # Fallback: take last sentence and split by commas
    parts = desc.split('.')
    if len(parts) > 0:
        last = parts[-1]
        parts2 = [p.strip() for p in re.split(r',|\band\b|&', last) if p.strip()]
        return parts2
    return []

# Aggregate review counts by category
from collections import defaultdict
cat_counts = defaultdict(int)

for doc in docs:
    bid = doc.get('business_id')
    desc = doc.get('description', '')
    cats = extract_categories(desc)
    count = ref_to_count.get(bid, 0)
    for c in cats:
        cat_counts[c] += count

# Convert to sorted list
sorted_cats = sorted(cat_counts.items(), key=lambda x: x[1], reverse=True)
top5 = sorted_cats[:5]

# Prepare result as list of dicts
result = [{'category': k, 'total_reviews': v} for k, v in top5]

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_DVsiC0DM6etSW25lY7Aqteqo': ['checkin', 'business'], 'var_call_8BiBSvlT0tqAsSOzvtnACT5S': ['review', 'tip', 'user'], 'var_call_MbQvZP2gCUdBDeNk3dwhxkNF': 'file_storage/call_MbQvZP2gCUdBDeNk3dwhxkNF.json', 'var_call_Pjvkr5vqQP0NzVR3RGXEhzen': [{'business_ref': 'businessref_45', 'review_count': '3'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_33', 'review_count': '2'}, {'business_ref': 'businessref_36', 'review_count': '2'}, {'business_ref': 'businessref_60', 'review_count': '2'}, {'business_ref': 'businessref_57', 'review_count': '2'}, {'business_ref': 'businessref_92', 'review_count': '2'}, {'business_ref': 'businessref_96', 'review_count': '2'}, {'business_ref': 'businessref_13', 'review_count': '1'}, {'business_ref': 'businessref_79', 'review_count': '1'}, {'business_ref': 'businessref_15', 'review_count': '1'}, {'business_ref': 'businessref_12', 'review_count': '1'}, {'business_ref': 'businessref_31', 'review_count': '1'}, {'business_ref': 'businessref_86', 'review_count': '1'}, {'business_ref': 'businessref_6', 'review_count': '1'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_98', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}, {'business_ref': 'businessref_62', 'review_count': '1'}, {'business_ref': 'businessref_37', 'review_count': '1'}, {'business_ref': 'businessref_26', 'review_count': '1'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}], 'var_call_WkUhJeDeYmPgYo7gehrywNQQ': [{'_id': '6859a000fe8b31cd7362e2db', 'business_id': 'businessid_45', 'name': 'The Fresh Market', 'description': 'Located at 2900 4th St N in St. Petersburg, FL, this establishment offers a diverse range of products and services in the categories of Food, Grocery, Shopping.'}], 'var_call_L3lE7BEC3GIqewx2EL6MBLAq': [{'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'name': 'Candy Barrel', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}], 'var_call_lI0ngjzKJJ7Ik3Q3jXXJ7BPx': [{'_id': '6859a000fe8b31cd7362e2e1', 'business_id': 'businessid_66', 'name': 'Panda Express', 'description': 'Located at 3849 State St. Space I-58 in Santa Barbara, CA, this establishment offers a variety of quick and delicious options in the categories of Fast Food, Chinese, Restaurants.'}], 'var_call_6cUZKRtvFkfXNG0jmuI6vRcu': [{'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_eZak0fxuG6W7OCf5iNM9a7xu': [{'_id': '6859a000fe8b31cd7362e308', 'business_id': 'businessid_36', 'name': 'Pho & Beyond', 'description': "Located at 47 Easton Rd in Willow Grove, PA, this inviting establishment offers a delightful menu featuring authentic flavors in the categories of 'Restaurants, Vietnamese'."}], 'var_call_ZSfJDZZJYw8PdzTfLF8qZRla': [{'_id': '6859a000fe8b31cd7362e302', 'business_id': 'businessid_60', 'name': 'Walmart', 'description': 'Located at 8101 W Judge Perez Dr in Chalmette, LA, this versatile establishment offers a wide range of options for customers, including Food, Shopping, Fashion, Discount Store, Grocery, Electronics, Drugstores, Department Stores, ensuring that visitors can find everything they need in one convenient location.'}], 'var_call_Ezuu9r5lZfHqOFIabIENLdtI': [{'_id': '6859a000fe8b31cd7362e2cd', 'business_id': 'businessid_57', 'name': 'Big Boys Moving And Storage', 'description': 'Located at 13605 W Hillsborough Ave in Tampa, FL, this versatile establishment offers a range of services and dining options, including Movers, American (New), Landscape Architects, Food, Home Services, Self Storage, Local Services, Restaurants.'}], 'var_call_qpQIypVJhXUvB3r8iS7o087E': [{'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'name': 'Luminosity', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_call_hKtkmfJRNiPEuOTHYtQqphCp': [{'_id': '6859a000fe8b31cd7362e2e6', 'business_id': 'businessid_96', 'name': 'Farmhaus Restaurant', 'description': 'Located at 3257 Ivanhoe Ave in Saint Louis, MO, this establishment offers a vibrant atmosphere perfect for enjoying a diverse selection of experiences, including Wine Bars, American (New), Cocktail Bars, Restaurants, American (Traditional), Nightlife, and Bars.'}], 'var_call_AMhLoE4NXLhxqRDhyjVedOlR': [{'_id': '6859a000fe8b31cd7362e30d', 'business_id': 'businessid_13', 'name': 'Avian Glen Winery', 'description': 'Located at 3545 Almaville Rd in Smyrna, TN, this establishment offers a delightful experience encompassing Food, Arts & Entertainment, Wineries, and a Wine Tasting Room.'}], 'var_call_0XEyo4lW9YOokJEnQDqbnJ7p': [{'_id': '6859a000fe8b31cd7362e2e0', 'business_id': 'businessid_79', 'name': 'Pit Stop HQ', 'description': 'Located at 838-842 Christian St in Philadelphia, PA, this establishment offers a wide range of services including Pet Groomers, Pet Stores, Pet Training, Dog Walkers, Pet Services, Pets, and Pet Sitting.'}], 'var_call_iJ9DHzg1Z0Ofu0OETkvHvHBZ': [{'_id': '6859a000fe8b31cd7362e2e5', 'business_id': 'businessid_15', 'name': 'Take 5 Oil Change', 'description': 'Located at 3803 Gen Degaulle Dr in New Orleans, LA, this establishment specializes in Automotive, Oil Change Stations, providing efficient service for all your vehicle maintenance needs.'}], 'var_call_NPKTUcbCLXJDqaeFLA4KDLYv': [{'_id': '6859a000fe8b31cd7362e300', 'business_id': 'businessid_12', 'name': 'Atlantic Trap & Gill Pub', 'description': 'Located at 7704 Calgary Trail S in Edmonton, AB, this vibrant spot offers a diverse experience with options for Pubs, Restaurants, Nightlife, Burgers, Seafood, and Bars.'}], 'var_call_avnDK10EEbHcEAjEq0OuIjiC': [{'_id': '6859a000fe8b31cd7362e2fb', 'business_id': 'businessid_31', 'name': 'Island Way Car Wash', 'description': 'Located at 1234 Pasadena Ave S in South Pasadena, FL, this business specializes in Automotive services, offering a comprehensive Car Wash and professional Auto Detailing to keep your vehicle looking its best.'}], 'var_call_hYt8VG4EHByJ0Ul4Vjl0vPHq': [{'_id': '6859a000fe8b31cd7362e2ed', 'business_id': 'businessid_86', 'name': "Humpty's Dumplings", 'description': 'Located at 705 East Passyunk Ave in Philadelphia, PA, this vibrant eatery offers a diverse menu featuring American (New), Restaurants, American (Traditional), Asian Fusion, Noodles, Dim Sum, Fast Food, Chinese, catering to a variety of tastes and preferences.'}], 'var_call_kR56AAvNswBZeS2oQJ6U9NFC': [{'_id': '6859a000fe8b31cd7362e2dd', 'business_id': 'businessid_6', 'name': 'The Jungle', 'description': 'Located at 246 W 1st St in Reno, NV, this vibrant destination offers a delightful mix of Restaurants, Breakfast & Brunch, Bars, Wine Bars, Coffee & Tea, Food, Cafes, Sandwiches, and Nightlife, making it an ideal spot for any meal or occasion.'}], 'var_call_8llLYyd56yQ7sDCHqpPYoDT4': [{'_id': '6859a000fe8b31cd7362e2ee', 'business_id': 'businessid_53', 'name': 'Samwich', 'description': 'Located at 1040 N American St, Ste 1101 in Philadelphia, PA, this eatery offers a diverse menu featuring Salad, Sandwiches, Restaurants, and Burgers.'}], 'var_call_dVnoAtWpFvK6lAxhyzTWA0lp': [{'_id': '6859a000fe8b31cd7362e304', 'business_id': 'businessid_98', 'name': 'Brookmont Apartment Homes', 'description': 'Situated at 600 Red Lion Rd in Philadelphia, PA, this establishment offers a range of services in Real Estate, Apartments, and Home Services.'}], 'var_call_eTDWcKHtSSgRnAsgcZgERvPB': [{'_id': '6859a000fe8b31cd7362e2c9', 'business_id': 'businessid_14', 'name': 'Ross Dress for Less', 'description': "Located at 7055 Marketplace Dr in Goleta, CA, this store offers a diverse selection of products across various categories, including Women's Clothing, Fashion, Department Stores, Home Decor, Home & Garden, Shopping, Men's Clothing, and Discount Store."}], 'var_call_YTe3bytoFgCFyZ4CV7kjXprE': [{'_id': '6859a000fe8b31cd7362e2f4', 'business_id': 'businessid_20', 'name': 'Chick-fil-A', 'description': 'Located at 9040 State Road 54 in Trinity, FL, this establishment offers a diverse array of options, including Restaurants, American (New), Caterers, Fast Food, Chicken Shop, Event Planning & Services, and American (Traditional).'}], 'var_call_8NBFGV8gA5dS40AgulcErmLC': [{'_id': '6859a000fe8b31cd7362e2f7', 'business_id': 'businessid_62', 'name': 'Winn Dixie', 'description': 'Located at 8424 Sheldon Rd in Tampa, FL, this establishment offers a diverse range of products and services, including Photography Stores & Services, Shopping, Grocery, and Food.'}], 'var_call_3seNYMyclPbZb0RtHhh71fjS': [{'_id': '6859a000fe8b31cd7362e2f5', 'business_id': 'businessid_37', 'name': 'Orangetheory Fitness Carrollwood', 'description': 'Located at 13122 N Dale Mabry Hwy in Tampa, FL, this facility offers a comprehensive range of services in Fitness & Instruction, Gyms, Boot Camps, Trainers, Active Life, and Interval Training Gyms.'}], 'var_call_yRlll9GYvK5lUSDZcdaqXk5v': [{'_id': '6859a000fe8b31cd7362e2c1', 'business_id': 'businessid_26', 'name': "McDonald's", 'description': 'Located at 7003 Seminole Blvd in Seminole, FL, this establishment specializes in a variety of offerings, including Fast Food, Restaurants, Coffee & Tea, Food, and Burgers, making it a convenient stop for a quick meal or a refreshing beverage.'}], 'var_call_Kwv8LrBVX9bGK4P3F1G9lrLF': [{'_id': '6859a000fe8b31cd7362e2dc', 'business_id': 'businessid_68', 'name': 'Brow Art', 'description': 'Located at 593 Brandon Town Ctr in Brandon, FL, this establishment offers a range of services in the categories of Beauty & Spas, Hair Removal, and Eyebrow Services.'}], 'var_call_EUzB6cT5x2rNmQjt3MczEOU9': [{'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}], 'var_call_sfWcPgL0e9o1D5pWWUCmkpKK': [{'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10', 'name': 'China Wok', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}]}

exec(code, env_args)
