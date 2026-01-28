code = """import json

# Load the data we have so far
businesses_cached = locals()['var_functions.query_db:14']
print(f"Businesses already cached: {len(businesses_cached)}")

# Load business IDs we need to check
all_business_ids = locals()['var_functions.execute_python:16']
print(f"Total business IDs to check: {len(all_business_ids)}")

# Find which IDs we haven't queried yet
cached_ids = {b['business_id'] for b in businesses_cached}
remaining_ids = [bid for bid in all_business_ids if bid not in cached_ids]
print(f"Remaining IDs to query: {len(remaining_ids)}")

# Load 2018 reviews data
reviews_file_path = locals()['var_functions.query_db:5']
with open(reviews_file_path, 'r') as f:
    reviews_2018 = json.load(f)

# Count how many reviews each business got in 2018
business_ref_review_count = {}
for review in reviews_2018:
    if review['business_ref']:
        bref = review['business_ref']
        business_ref_review_count[bref] = business_ref_review_count.get(bref, 0) + 1

print(f"Total 2018 reviews: {len(reviews_2018)}")
print(f"Total unique businesses reviewed: {len(business_ref_review_count)}")

# Check parking attributes in businesses we already have info for
businesses_with_parking = set()
parking_details = []

for business in businesses_cached:
    attributes = business.get('attributes')
    if not attributes:
        continue
    
    business_ref = business['business_id'].replace('businessid_', 'businessref_', 1)
    review_count = business_ref_review_count.get(business_ref, 0)
    
    has_bike_parking = False
    has_business_parking = False
    
    # Check BikeParking
    if isinstance(attributes, dict) and 'BikeParking' in attributes:
        bike_value = attributes['BikeParking']
        if str(bike_value).lower() == 'true' or str(bike_value).strip() == 'True':
            has_bike_parking = True
    
    # Check BusinessParking
    if isinstance(attributes, dict) and 'BusinessParking' in attributes:
        parking_value = attributes['BusinessParking']
        parking_str = str(parking_value)
        if 'True' in parking_str and 'False' not in parking_str.replace('True', ''):
            has_business_parking = True
        elif isinstance(parking_value, dict):
            for p_type, p_avail in parking_value.items():
                if str(p_avail).lower() == 'true':
                    has_business_parking = True
                    break
    
    if has_bike_parking or has_business_parking:
        businesses_with_parking.add(business['business_id'])
        parking_details.append({
            'business_id': business['business_id'],
            'business_ref': business_ref,
            'review_count': review_count,
            'has_bike_parking': has_bike_parking,
            'has_business_parking': has_business_parking
        })

print(f"Businesses with parking attributes (from cached): {len(businesses_with_parking)}")

result = {
    "total_business_ids": len(all_business_ids),
    "cached_count": len(businesses_cached),
    "remaining_count": len(remaining_ids),
    "businesses_with_parking_cached": len(businesses_with_parking),
    "parking_details_sample": parking_details[:3]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['checkin', 'business'], 'var_functions.query_db:2': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'total_reviews_2018': 65, 'unique_business_refs_2018': 36, 'unique_business_ids_to_search': 36}, 'var_functions.execute_python:10': {'business_ids_count': 36, 'businees_ids_list': ['businessid_27', 'businessid_26', 'businessid_37', 'businessid_24', 'businessid_8', 'businessid_47', 'businessid_17', 'businessid_22', 'businessid_28', 'businessid_35', 'businessid_66', 'businessid_20', 'businessid_80', 'businessid_25', 'businessid_67', 'businessid_57', 'businessid_43', 'businessid_73', 'businessid_13', 'businessid_86', 'businessid_15', 'businessid_99', 'businessid_40', 'businessid_59', 'businessid_36', 'businessid_62', 'businessid_79', 'businessid_45', 'businessid_68', 'businessid_4', 'businessid_46', 'businessid_82', 'businessid_14', 'businessid_91', 'businessid_83', 'businessid_77']}, 'var_functions.query_db:14': [{'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2b8', 'business_id': 'businessid_8', 'name': 'Uber', 'review_count': '218', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '0:0-0:0', 'Wednesday': '0:0-0:0', 'Thursday': '0:0-0:0', 'Friday': '0:0-0:0'}, 'description': 'This Philadelphia, PA location offers a range of services including Hotels & Travel, Taxis, Transportation, Local Services, and Automotive to meet all your travel and transportation needs.'}, {'_id': '6859a000fe8b31cd7362e2b9', 'business_id': 'businessid_59', 'name': 'Chestnut St. Cafe', 'review_count': '34', 'is_open': '0', 'attributes': {'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsTakeOut': 'None', 'RestaurantsDelivery': 'None', 'HasTV': 'True', 'Ambience': "{'touristy': False, 'hipster': None, 'romantic': None, 'divey': None, 'intimate': None, 'trendy': None, 'upscale': False, 'classy': None, 'casual': True}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}"}, 'hours': {'Monday': '11:0-19:0', 'Tuesday': '11:0-19:0', 'Wednesday': '11:0-19:0', 'Thursday': '11:0-19:0', 'Friday': '11:0-19:0', 'Saturday': '11:0-16:0'}, 'description': 'Located at 4403 Chestnut St in Philadelphia, PA, this vibrant spot offers a delightful mix of Food, Bubble Tea, Restaurants, Sandwiches, Vietnamese, Cafes, perfect for a casual meal or a refreshing drink.'}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91', 'name': 'Cafe Porche and snowbar', 'review_count': '172', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'WiFi': "u'free'", 'WheelchairAccessible': 'True', 'Caters': 'True', 'HasTV': 'True', 'HappyHour': 'False', 'Ambience': "{'touristy': None, 'hipster': None, 'romantic': None, 'divey': None, 'intimate': True, 'trendy': None, 'upscale': None, 'classy': True, 'casual': True}", 'RestaurantsDelivery': 'True', 'RestaurantsPriceRange2': '2', 'GoodForKids': 'True', 'RestaurantsAttire': "u'casual'", 'BikeParking': 'True', 'OutdoorSeating': 'True', 'NoiseLevel': "u'quiet'", 'RestaurantsGoodForGroups': 'True', 'RestaurantsTakeOut': 'True', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsReservations': 'False', 'GoodForMeal': "{'dessert': None, 'latenight': None, 'lunch': True, 'dinner': None, 'brunch': True, 'breakfast': True}", 'Alcohol': "u'beer_and_wine'", 'RestaurantsTableService': 'True', 'Corkage': 'False', 'BYOB': 'True'}, 'hours': {'Monday': '0:0-0:0', 'Friday': '8:30-14:30', 'Saturday': '8:30-14:30', 'Sunday': '9:0-14:30'}, 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}, {'_id': '6859a000fe8b31cd7362e2bb', 'business_id': 'businessid_83', 'name': 'Eyeglass World', 'review_count': '6', 'is_open': '1', 'attributes': {'RestaurantsPriceRange2': '2', 'AcceptsInsurance': 'True', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': 'None', 'ByAppointmentOnly': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '9:0-18:0', 'Wednesday': '9:0-15:0', 'Thursday': '9:0-19:0', 'Friday': '9:0-19:0', 'Saturday': '9:0-18:0', 'Sunday': '9:0-15:0'}, 'description': 'Located at 13002 Seminole Blvd, Ste 10-11 in Largo, FL, this business specializes in Optometrists, Health & Medical, Eyewear & Opticians, Ophthalmologists, Doctors, Shopping, offering a range of eye care services and products.'}], 'var_functions.execute_python:16': ['businessid_27', 'businessid_26', 'businessid_37', 'businessid_24', 'businessid_8', 'businessid_47', 'businessid_17', 'businessid_22', 'businessid_28', 'businessid_35', 'businessid_66', 'businessid_20', 'businessid_80', 'businessid_25', 'businessid_67', 'businessid_57', 'businessid_43', 'businessid_73', 'businessid_13', 'businessid_86', 'businessid_15', 'businessid_99', 'businessid_40', 'businessid_59', 'businessid_36', 'businessid_62', 'businessid_79', 'businessid_45', 'businessid_68', 'businessid_4', 'businessid_46', 'businessid_82', 'businessid_14', 'businessid_91', 'businessid_83', 'businessid_77'], 'var_functions.execute_python:18': ['businessid_47', 'businessid_8', 'businessid_59', 'businessid_91', 'businessid_83'], 'var_functions.query_db:20': [{'_id': '6859a000fe8b31cd7362e2be', 'business_id': 'businessid_24', 'name': 'FroYo Frozen Yogurt', 'review_count': '43', 'is_open': '0', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '1', 'WiFi': "u'no'", 'BikeParking': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsTakeOut': 'True'}, 'hours': {'Monday': '13:0-21:0', 'Tuesday': '13:0-21:0', 'Wednesday': '13:0-21:0', 'Thursday': '13:0-21:0', 'Friday': '12:0-22:0', 'Saturday': '12:0-22:0', 'Sunday': '13:0-21:0'}, 'description': 'Located at 4663 Maryland Ave in Saint Louis, MO, this delightful spot offers a tempting selection of treats in the categories of Food, Ice Cream & Frozen Yogurt.'}, {'_id': '6859a000fe8b31cd7362e2c1', 'business_id': 'businessid_26', 'name': "McDonald's", 'review_count': '28', 'is_open': '1', 'attributes': {'WiFi': "u'free'", 'RestaurantsReservations': 'False', 'GoodForKids': 'True', 'Caters': 'False', 'RestaurantsPriceRange2': '1', 'OutdoorSeating': 'False', 'RestaurantsAttire': "u'casual'", 'HasTV': 'True', 'Alcohol': "u'none'", 'RestaurantsTakeOut': 'True', 'RestaurantsTableService': 'False', 'DriveThru': 'True', 'RestaurantsGoodForGroups': 'False', 'BusinessAcceptsCreditCards': 'True', 'BikeParking': 'True', 'RestaurantsDelivery': 'True', 'NoiseLevel': "u'average'", 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'Ambience': "{'romantic': False, 'intimate': False, 'touristy': False, 'hipster': False, 'divey': False, 'classy': False, 'trendy': False, 'upscale': False, 'casual': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}"}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '0:0-0:0', 'Wednesday': '0:0-0:0', 'Thursday': '0:0-0:0', 'Friday': '0:0-0:0', 'Saturday': '0:0-0:0', 'Sunday': '0:0-0:0'}, 'description': 'Located at 7003 Seminole Blvd in Seminole, FL, this establishment specializes in a variety of offerings, including Fast Food, Restaurants, Coffee & Tea, Food, and Burgers, making it a convenient stop for a quick meal or a refreshing beverage.'}, {'_id': '6859a000fe8b31cd7362e2cb', 'business_id': 'businessid_35', 'name': 'Bywood Seafood Market', 'review_count': '9', 'is_open': '1', 'attributes': {'NoiseLevel': "u'quiet'", 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsAttire': "u'casual'", 'RestaurantsPriceRange2': '2', 'RestaurantsTakeOut': 'True'}, 'hours': {'Monday': '8:30-18:0', 'Tuesday': '8:30-18:0', 'Wednesday': '8:30-18:0', 'Thursday': '8:30-18:0', 'Friday': '8:30-18:0', 'Saturday': '9:0-17:0'}, 'description': 'Located at 827 Conestoga Rd in Bryn Mawr, PA, this establishment offers a delightful selection of fresh catches and culinary delights, making it a go-to destination for Seafood, Food, Seafood Markets, Specialty Food, Restaurants enthusiasts.'}, {'_id': '6859a000fe8b31cd7362e2cc', 'business_id': 'businessid_28', 'name': 'Battleground Hospital For Animals', 'review_count': '19', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-18:0', 'Saturday': '7:30-13:0'}, 'description': 'Located at 225 S Royal Oaks Blvd in Franklin, TN, this establishment offers a range of services for animal lovers, including Veterinarians, Pets, Pet Groomers, Pet Services, Pet Boarding, and Pet Sitting.'}, {'_id': '6859a000fe8b31cd7362e2ce', 'business_id': 'businessid_27', 'name': 'Egg Roll King Two', 'review_count': '37', 'is_open': '1', 'attributes': {'RestaurantsAttire': "u'casual'", 'Alcohol': "u'none'", 'OutdoorSeating': 'False', 'RestaurantsGoodForGroups': 'True', 'WiFi': "u'no'", 'RestaurantsTakeOut': 'True', 'RestaurantsPriceRange2': '1', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsDelivery': 'False', 'BikeParking': 'True', 'NoiseLevel': "u'average'", 'GoodForKids': 'True', 'Caters': 'True', 'RestaurantsReservations': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': None, 'lunch': True, 'dinner': None, 'brunch': None, 'breakfast': None}", 'HasTV': 'True', 'Ambience': "{'touristy': False, 'hipster': False, 'romantic': False, 'divey': None, 'intimate': False, 'trendy': False, 'upscale': False, 'classy': False, 'casual': None}"}, 'hours': 'None', 'description': 'Located at 2253 Oddie Blvd in Sparks, NV, this establishment offers a delightful dining experience featuring a diverse menu in the category of Restaurants, Chinese.'}]}

exec(code, env_args)
