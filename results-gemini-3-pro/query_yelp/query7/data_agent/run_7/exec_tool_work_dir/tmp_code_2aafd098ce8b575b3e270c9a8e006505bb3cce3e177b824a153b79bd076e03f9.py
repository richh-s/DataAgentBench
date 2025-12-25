code = """import json
import os

sql_results = locals()['var_function-call-14509043132087738444']
mongo_file = locals()['var_function-call-3683741755750727028']

if isinstance(mongo_file, str) and os.path.exists(mongo_file):
    with open(mongo_file, 'r') as f:
        mongo_results = json.load(f)
else:
    mongo_results = mongo_file

count_map = {}
for item in sql_results:
    bid = item['business_ref'].replace('businessref_', 'businessid_')
    count_map[bid] = int(item['count'])

category_counts = {}

def parse_cats(desc):
    markers = [
        "categories, including ",
        "offerings, including ",
        "options, including ",
        "categories of ",
        "category of '",
        "category of ",
        "mix of ",
        "fields of ",
        "services in ", 
        "including ", 
        "destination for ", 
        "seeking ",
        "specializes in ",
        "menu featuring ",
        "options for ",
        "encompassing "
    ]
    
    text = ""
    for m in markers:
        if m in desc:
            parts = desc.split(m)
            text = parts[-1]
            break
            
    if not text:
        return ""
        
    suffixes = [
        ", making it",
        " making it",
        ", providing",
        " providing",
        ", catering",
        " catering",
        ", ensuring",
        " ensuring"
    ]
    for s in suffixes:
        if s in text:
            text = text.split(s)[0]
    
    return text

def clean_cats(text):
    if not text:
        return []
    text = text.strip()
    if text.endswith('.'):
        text = text[:-1]
    if text.endswith("'"):
        text = text[:-1]
    text = text.replace(" and ", ", ")
    parts = text.split(',')
    cats = [p.strip() for p in parts if p.strip()]
    return cats

debug_list = []

for biz in mongo_results:
    bid = biz['business_id']
    if bid in count_map:
        count = count_map[bid]
        desc = biz.get('description', '')
        cat_text = parse_cats(desc)
        cats = clean_cats(cat_text)
        
        debug_list.append(str(bid) + ": " + str(cats))
        
        for c in cats:
            c = c.replace("'", "").replace('"', "")
            category_counts[c] = category_counts.get(c, 0) + count

sorted_cats = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)
top_5 = sorted_cats[:5]

print("__RESULT__:")
print(json.dumps({"top_5": top_5}))"""

env_args = {'var_function-call-17842901698263806162': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-17411742535346701157': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-3649926715728267985': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-14509043132087738444': [{'business_ref': 'businessref_45', 'count': '3'}, {'business_ref': 'businessref_74', 'count': '2'}, {'business_ref': 'businessref_66', 'count': '2'}, {'business_ref': 'businessref_33', 'count': '2'}, {'business_ref': 'businessref_36', 'count': '2'}, {'business_ref': 'businessref_60', 'count': '2'}, {'business_ref': 'businessref_57', 'count': '2'}, {'business_ref': 'businessref_92', 'count': '2'}, {'business_ref': 'businessref_96', 'count': '2'}, {'business_ref': 'businessref_13', 'count': '1'}, {'business_ref': 'businessref_79', 'count': '1'}, {'business_ref': 'businessref_15', 'count': '1'}, {'business_ref': 'businessref_12', 'count': '1'}, {'business_ref': 'businessref_31', 'count': '1'}, {'business_ref': 'businessref_53', 'count': '1'}, {'business_ref': 'businessref_86', 'count': '1'}, {'business_ref': 'businessref_62', 'count': '1'}, {'business_ref': 'businessref_37', 'count': '1'}, {'business_ref': 'businessref_26', 'count': '1'}, {'business_ref': 'businessref_68', 'count': '1'}, {'business_ref': 'businessref_98', 'count': '1'}, {'business_ref': 'businessref_14', 'count': '1'}, {'business_ref': 'businessref_20', 'count': '1'}, {'business_ref': 'businessref_6', 'count': '1'}, {'business_ref': 'businessref_41', 'count': '1'}, {'business_ref': 'businessref_10', 'count': '1'}], 'var_function-call-6884879533053385404': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-13515998265298002616': [{'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'name': 'Candy Barrel', 'review_count': '7', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '4', 'BikeParking': 'False'}, 'hours': 'None', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'name': 'Luminosity', 'review_count': '39', 'is_open': '1', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'True', 'NoiseLevel': "u'quiet'", 'WiFi': "u'no'"}, 'hours': {'Monday': '10:0-21:0', 'Tuesday': '10:0-21:0', 'Wednesday': '10:0-21:0', 'Thursday': '10:0-21:0', 'Friday': '10:0-21:0', 'Saturday': '10:0-21:0', 'Sunday': '11:0-18:0'}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10', 'name': 'China Wok', 'review_count': '20', 'is_open': '1', 'attributes': {'RestaurantsGoodForGroups': 'True', 'RestaurantsDelivery': 'False', 'RestaurantsTakeOut': 'True', 'HasTV': 'True', 'BusinessAcceptsCreditCards': 'True', 'Ambience': "{'touristy': False, 'hipster': False, 'romantic': False, 'divey': False, 'intimate': False, 'trendy': False, 'upscale': False, 'classy': False, 'casual': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}", 'BusinessParking': "{u'valet': False, u'garage': False, u'street': False, u'lot': True, u'validated': False}"}, 'hours': 'None', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}], 'var_function-call-2965295578070722115': {'sorted_cats': [['Beauty & Spas', 4], ['Health & Medical', 3], ['Nail Salons', 2], ['Hair Removal', 2], ['Waxing', 2], ['Candy Stores', 2], ['Specialty Food', 2], ['Food', 2], ['Cosmetics & Beauty Supply', 2], ['Cosmetic Dentists', 2], ['Tanning', 2], ['Teeth Whitening', 2], ['Dentists', 2], ['Shopping', 2], ['Blow Dry/Out Services', 2], ['Spray Tanning', 2], ['Hair Salons', 2], ['Internal Medicine', 1], ['Doctors', 1], ['Restaurants', 1], ['Chinese', 1]], 'debug': ["businessid_41: ['Internal Medicine', 'Doctors', 'Health & Medical']", "businessid_33: ['Nail Salons', 'Hair Removal', 'Beauty & Spas', 'Waxing']", "businessid_74: ['Candy Stores', 'Specialty Food', 'Food']", "businessid_92: ['Cosmetics & Beauty Supply', 'Cosmetic Dentists', 'Tanning', 'Teeth Whitening', 'Beauty & Spas', 'Dentists', 'Shopping', 'Blow Dry/Out Services', 'Health & Medical', 'Spray Tanning', 'Hair Salons']", "businessid_10: ['Restaurants', 'Chinese']"]}, 'var_function-call-3683741755750727028': 'file_storage/function-call-3683741755750727028.json', 'var_function-call-18309355307373501171': {'top_5': [['Food', 12], ['Restaurants', 12], ['Shopping', 9], ['Grocery', 6], ['Beauty & Spas', 5]], 'debug': ["businessid_41: ['Internal Medicine', 'Doctors', 'Health & Medical']", "businessid_33: ['Nail Salons', 'Hair Removal', 'Beauty & Spas', 'Waxing']", "businessid_74: ['Candy Stores', 'Specialty Food', 'Food']", "businessid_92: ['Cosmetics & Beauty Supply', 'Cosmetic Dentists', 'Tanning', 'Teeth Whitening', 'Beauty & Spas', 'Dentists', 'Shopping', 'Blow Dry/Out Services', 'Health & Medical', 'Spray Tanning', 'Hair Salons']", "businessid_10: ['Restaurants', 'Chinese']", "businessid_26: ['Fast Food', 'Restaurants', 'Coffee & Tea', 'Food', 'Burgers']", 'businessid_14: ["Women\'s Clothing", \'Fashion\', \'Department Stores\', \'Home Decor\', \'Home & Garden\', \'Shopping\', "Men\'s Clothing", \'Discount Store\']', "businessid_57: ['Movers', 'American (New)', 'Landscape Architects', 'Food', 'Home Services', 'Self Storage', 'Local Services', 'Restaurants']", "businessid_45: ['Food', 'Grocery', 'Shopping']", "businessid_68: ['Beauty & Spas', 'Hair Removal', 'Eyebrow Services']", "businessid_6: ['Restaurants', 'Breakfast & Brunch', 'Bars', 'Wine Bars', 'Coffee & Tea', 'Food', 'Cafes', 'Sandwiches', 'Nightlife']", "businessid_79: ['Pet Groomers', 'Pet Stores', 'Pet Training', 'Dog Walkers', 'Pet Services', 'Pets', 'Pet Sitting']", "businessid_66: ['Fast Food', 'Chinese', 'Restaurants']", 'businessid_15: []', "businessid_96: ['Wine Bars', 'American (New)', 'Cocktail Bars', 'Restaurants', 'American (Traditional)', 'Nightlife', 'Bars']", 'businessid_86: []', 'businessid_53: []', "businessid_20: ['Restaurants', 'American (New)', 'Caterers', 'Fast Food', 'Chicken Shop', 'Event Planning & Services', 'American (Traditional)']", "businessid_37: ['Fitness & Instruction', 'Gyms', 'Boot Camps', 'Trainers', 'Active Life', 'Interval Training Gyms']", "businessid_62: ['Photography Stores & Services', 'Shopping', 'Grocery', 'Food']", 'businessid_31: []', 'businessid_12: []', "businessid_60: ['Food', 'Shopping', 'Fashion', 'Discount Store', 'Grocery', 'Electronics', 'Drugstores', 'Department Stores', 'ensuring that visitors can find everything they need in one convenient location']", "businessid_98: ['Real Estate', 'Apartments', 'Home Services']", 'businessid_36: ["\'Restaurants", \'Vietnamese\']', 'businessid_13: []']}, 'var_function-call-7794356481103465207': {'businessid_15': 'Located at 3803 Gen Degaulle Dr in New Orleans, LA, this establishment specializes in Automotive, Oil Change Stations, providing efficient service for all your vehicle maintenance needs.', 'businessid_86': 'Located at 705 East Passyunk Ave in Philadelphia, PA, this vibrant eatery offers a diverse menu featuring American (New), Restaurants, American (Traditional), Asian Fusion, Noodles, Dim Sum, Fast Food, Chinese, catering to a variety of tastes and preferences.', 'businessid_53': 'Located at 1040 N American St, Ste 1101 in Philadelphia, PA, this eatery offers a diverse menu featuring Salad, Sandwiches, Restaurants, and Burgers.', 'businessid_31': 'Located at 1234 Pasadena Ave S in South Pasadena, FL, this business specializes in Automotive services, offering a comprehensive Car Wash and professional Auto Detailing to keep your vehicle looking its best.', 'businessid_12': 'Located at 7704 Calgary Trail S in Edmonton, AB, this vibrant spot offers a diverse experience with options for Pubs, Restaurants, Nightlife, Burgers, Seafood, and Bars.', 'businessid_13': 'Located at 3545 Almaville Rd in Smyrna, TN, this establishment offers a delightful experience encompassing Food, Arts & Entertainment, Wineries, and a Wine Tasting Room.'}}

exec(code, env_args)
