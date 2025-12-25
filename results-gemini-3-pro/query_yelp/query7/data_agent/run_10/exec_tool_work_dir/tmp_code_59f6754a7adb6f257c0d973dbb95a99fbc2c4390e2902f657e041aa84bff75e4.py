code = """import json
import re

reviews = locals()['var_function-call-13670594900718658966']
businesses_path = locals()['var_function-call-3179065193301312969']

if isinstance(businesses_path, str) and not isinstance(businesses_path, list):
    with open(businesses_path, 'r') as f:
        businesses = json.load(f)
else:
    businesses = businesses_path

biz_review_map = {}
for r in reviews:
    bid = r['business_ref'].replace('businessref_', 'businessid_')
    count = int(r['review_count'])
    biz_review_map[bid] = count

category_counts = {}

keywords = [
    "including ", 
    "services in ", 
    "destination for ", 
    "seeking ", 
    "specializes in ", 
    "category of ", 
    "mix of ", 
    "featuring ", 
    "realm of ", 
    "categories of ",
    "range of options ranging from "
]

# Stop phrases that appear after the list
stop_phrases = [
    ", making it ", 
    " to meet ", 
    ", perfect for ", 
    ", offering ",
    " catering to "
]

for b in businesses:
    bid = b['business_id']
    desc = b.get('description', '')
    if not desc:
        continue
    
    cat_part = None
    
    # Try to find the start of the list
    for kw in keywords:
        if kw in desc:
            # Handle "category of '...'"
            if kw == "category of ":
                match = re.search(r"category of '([^']+)'", desc)
                if match:
                    cat_part = match.group(1)
                else:
                    cat_part = desc.split(kw)[-1]
            else:
                cat_part = desc.split(kw)[-1]
            break
            
    if not cat_part:
        # Fallback: look for "offers ... [list]" where list is capitalized words?
        # Maybe the list is just at the end?
        # Let's skip for now and see coverage.
        continue

    # Truncate at stop phrases
    for stop in stop_phrases:
        if stop in cat_part:
            cat_part = cat_part.split(stop)[0]

    # Clean up
    cat_part = cat_part.strip().rstrip('.')
    
    # Remove quotes if present
    cat_part = cat_part.replace("'", "")
    
    # Split
    # Replace " and " with ", "
    # Replace " ranges from " ?? "ranging from " was in keyword.
    
    cat_part = cat_part.replace(" and ", ", ")
    
    cats = [c.strip() for c in cat_part.split(',')]
    
    count = biz_review_map.get(bid, 0)
    
    for c in cats:
        if not c: continue
        # Filter out junk?
        if len(c) > 50: continue # Likely failed parsing
        category_counts[c] = category_counts.get(c, 0) + count

# Sort
sorted_cats = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)

print("__RESULT__:")
print(json.dumps(sorted_cats[:10]))"""

env_args = {'var_function-call-12301865050448712506': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-3591072977364923219': [{'yelping_since': '15 Jan 2009, 16:40'}, {'yelping_since': '13 Jul 2010, 15:42'}, {'yelping_since': '2010-09-07 23:24:36'}], 'var_function-call-13670594900718658966': [{'business_ref': 'businessref_9', 'review_count': '3'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_25', 'review_count': '1'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_29', 'review_count': '1'}, {'business_ref': 'businessref_39', 'review_count': '1'}, {'business_ref': 'businessref_36', 'review_count': '3'}, {'business_ref': 'businessref_12', 'review_count': '4'}, {'business_ref': 'businessref_60', 'review_count': '4'}, {'business_ref': 'businessref_89', 'review_count': '3'}, {'business_ref': 'businessref_17', 'review_count': '1'}, {'business_ref': 'businessref_43', 'review_count': '3'}, {'business_ref': 'businessref_67', 'review_count': '5'}, {'business_ref': 'businessref_15', 'review_count': '3'}, {'business_ref': 'businessref_33', 'review_count': '5'}, {'business_ref': 'businessref_81', 'review_count': '1'}, {'business_ref': 'businessref_31', 'review_count': '1'}, {'business_ref': 'businessref_99', 'review_count': '1'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_51', 'review_count': '3'}, {'business_ref': 'businessref_37', 'review_count': '6'}, {'business_ref': 'businessref_57', 'review_count': '7'}, {'business_ref': 'businessref_8', 'review_count': '4'}, {'business_ref': 'businessref_56', 'review_count': '1'}, {'business_ref': 'businessref_62', 'review_count': '2'}, {'business_ref': 'businessref_86', 'review_count': '4'}, {'business_ref': 'businessref_97', 'review_count': '1'}, {'business_ref': 'businessref_72', 'review_count': '1'}, {'business_ref': 'businessref_85', 'review_count': '1'}, {'business_ref': 'businessref_42', 'review_count': '1'}, {'business_ref': 'businessref_40', 'review_count': '3'}, {'business_ref': 'businessref_7', 'review_count': '2'}, {'business_ref': 'businessref_92', 'review_count': '2'}, {'business_ref': 'businessref_61', 'review_count': '1'}, {'business_ref': 'businessref_88', 'review_count': '4'}, {'business_ref': 'businessref_21', 'review_count': '4'}, {'business_ref': 'businessref_26', 'review_count': '4'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_4', 'review_count': '1'}, {'business_ref': 'businessref_23', 'review_count': '1'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}, {'business_ref': 'businessref_45', 'review_count': '5'}, {'business_ref': 'businessref_82', 'review_count': '2'}, {'business_ref': 'businessref_76', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '3'}, {'business_ref': 'businessref_3', 'review_count': '2'}, {'business_ref': 'businessref_96', 'review_count': '4'}, {'business_ref': 'businessref_98', 'review_count': '3'}, {'business_ref': 'businessref_22', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}, {'business_ref': 'businessref_79', 'review_count': '8'}, {'business_ref': 'businessref_44', 'review_count': '4'}, {'business_ref': 'businessref_13', 'review_count': '3'}, {'business_ref': 'businessref_6', 'review_count': '4'}, {'business_ref': 'businessref_71', 'review_count': '1'}, {'business_ref': 'businessref_91', 'review_count': '2'}, {'business_ref': 'businessref_46', 'review_count': '1'}, {'business_ref': 'businessref_1', 'review_count': '1'}, {'business_ref': 'businessref_47', 'review_count': '1'}, {'business_ref': 'businessref_16', 'review_count': '1'}, {'business_ref': 'businessref_55', 'review_count': '1'}], 'var_function-call-1086051703367138226': {'collection': 'business', 'filter': {'business_id': {'$in': ['businessid_9', 'businessid_74', 'businessid_25', 'businessid_66', 'businessid_29', 'businessid_39', 'businessid_36', 'businessid_12', 'businessid_60', 'businessid_89', 'businessid_17', 'businessid_43', 'businessid_67', 'businessid_15', 'businessid_33', 'businessid_81', 'businessid_31', 'businessid_99', 'businessid_53', 'businessid_51', 'businessid_37', 'businessid_57', 'businessid_8', 'businessid_56', 'businessid_62', 'businessid_86', 'businessid_97', 'businessid_72', 'businessid_85', 'businessid_42', 'businessid_40', 'businessid_7', 'businessid_92', 'businessid_61', 'businessid_88', 'businessid_21', 'businessid_26', 'businessid_68', 'businessid_4', 'businessid_23', 'businessid_41', 'businessid_10', 'businessid_45', 'businessid_82', 'businessid_76', 'businessid_14', 'businessid_3', 'businessid_96', 'businessid_98', 'businessid_22', 'businessid_20', 'businessid_79', 'businessid_44', 'businessid_13', 'businessid_6', 'businessid_71', 'businessid_91', 'businessid_46', 'businessid_1', 'businessid_47', 'businessid_16', 'businessid_55']}}, 'projection': {'business_id': 1, 'description': 1}}, 'var_function-call-5384906104719140954': [{'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}], 'var_function-call-943300224109302492': [['Beauty & Spas', 6], ['Nail Salons', 5], ['Hair Removal', 5], ['Waxing', 5], ['Gun/Rifle Ranges', 4], ['Active Life', 4], ['Candy Stores', 2], ['Specialty Food', 2], ['Food', 2], ['Hair Salons', 1]], 'var_function-call-15484196696998214768': 'Done', 'var_function-call-16053908929684018946': {'total_reviews_records': 62, 'total_businesses_fetched': 5, 'parsed_count': 5, 'failed_count': 0, 'sample_failed': []}, 'var_function-call-12587517818132191152': [{'_id': '6859a000fe8b31cd7362e2f3', 'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'review_count': '53', 'is_open': '0', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'hours': {'Monday': '7:0-15:0', 'Tuesday': '7:0-15:0', 'Wednesday': '7:0-15:0', 'Thursday': '7:0-15:0', 'Friday': '7:0-15:0', 'Saturday': '8:30-15:0', 'Sunday': '8:30-15:0'}, 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}], 'var_function-call-3179065193301312969': 'file_storage/function-call-3179065193301312969.json'}

exec(code, env_args)
