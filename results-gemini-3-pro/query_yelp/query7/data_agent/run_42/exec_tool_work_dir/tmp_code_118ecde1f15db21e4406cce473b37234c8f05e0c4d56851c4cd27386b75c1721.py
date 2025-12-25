code = """import json

# Load SQL result
sql_result = locals()['var_function-call-3569218054206668481']
# Load Mongo result
mongo_file = locals()['var_function-call-12816037468976728331']
with open(mongo_file, 'r') as f:
    businesses = json.load(f)

# Create a map of business_id -> count
business_counts = {}
for row in sql_result:
    ref = row['business_ref']
    bid = ref.replace('businessref_', 'businessid_')
    count = int(row['cnt'])
    business_counts[bid] = count

category_counts = {}

def extract_categories(description):
    # Normalize text
    text = description
    
    # Phrases to look for. Order matters (longer phrases first if they overlap)
    phrases = [
        "products across various categories, including ",
        "categories of ",
        "category of ",
        "services in ",
        "including ",
        "seeking ",
        "fields of ",
        "mix of "
    ]
    
    cats_str = ""
    # Find the last occurrence of any phrase? Or the first?
    # Usually the description ends with the categories.
    
    found = False
    for phrase in phrases:
        if phrase in text:
            # Get text after phrase
            # If multiple phrases exist, we might have issues.
            # Usually only one relevant phrase introduces the list.
            # Let's take the part after the phrase.
            temp = text.split(phrase)[-1]
            # Strip trailing period
            if temp.endswith('.'):
                temp = temp[:-1]
            cats_str = temp
            found = True
            break
            
    if not found:
        return []
    
    # Process the string
    # Remove quotes
    cats_str = cats_str.replace("'", "")
    cats_str = cats_str.replace('"', "")
    
    # Split by comma
    items = [x.strip() for x in cats_str.split(',')]
    
    final_cats = []
    for item in items:
        # Check for "and " at the start
        if item.startswith('and '):
            item = item[4:]
        
        item = item.strip()
        if item:
            final_cats.append(item)
            
    return final_cats

debug_info = []

for biz in businesses:
    bid = biz['business_id']
    desc = biz.get('description', '')
    
    cats = extract_categories(desc)
    
    # Get review count for this business
    count = business_counts.get(bid, 0)
    
    debug_info.append({'bid': bid, 'cats': cats, 'count': count})
    
    for cat in cats:
        category_counts[cat] = category_counts.get(cat, 0) + count

# Sort categories by count desc
sorted_cats = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)
top_5 = sorted_cats[:5]

print("__RESULT__:")
print(json.dumps({"top_5": top_5, "debug": debug_info[:5]})) # Show first 5 debug entries"""

env_args = {'var_function-call-16297084049708208247': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-3569218054206668481': [{'business_ref': 'businessref_13', 'cnt': '1'}, {'business_ref': 'businessref_79', 'cnt': '1'}, {'business_ref': 'businessref_74', 'cnt': '2'}, {'business_ref': 'businessref_66', 'cnt': '2'}, {'business_ref': 'businessref_15', 'cnt': '1'}, {'business_ref': 'businessref_33', 'cnt': '2'}, {'business_ref': 'businessref_36', 'cnt': '2'}, {'business_ref': 'businessref_60', 'cnt': '2'}, {'business_ref': 'businessref_12', 'cnt': '1'}, {'business_ref': 'businessref_31', 'cnt': '1'}, {'business_ref': 'businessref_53', 'cnt': '1'}, {'business_ref': 'businessref_92', 'cnt': '2'}, {'business_ref': 'businessref_26', 'cnt': '1'}, {'business_ref': 'businessref_68', 'cnt': '1'}, {'business_ref': 'businessref_41', 'cnt': '1'}, {'business_ref': 'businessref_10', 'cnt': '1'}, {'business_ref': 'businessref_45', 'cnt': '3'}, {'business_ref': 'businessref_96', 'cnt': '2'}, {'business_ref': 'businessref_98', 'cnt': '1'}, {'business_ref': 'businessref_14', 'cnt': '1'}, {'business_ref': 'businessref_20', 'cnt': '1'}, {'business_ref': 'businessref_6', 'cnt': '1'}, {'business_ref': 'businessref_57', 'cnt': '2'}, {'business_ref': 'businessref_86', 'cnt': '1'}, {'business_ref': 'businessref_62', 'cnt': '1'}, {'business_ref': 'businessref_37', 'cnt': '1'}], 'var_function-call-13561583767062779772': ['businessid_13', 'businessid_79', 'businessid_74', 'businessid_66', 'businessid_15', 'businessid_33', 'businessid_36', 'businessid_60', 'businessid_12', 'businessid_31', 'businessid_53', 'businessid_92', 'businessid_26', 'businessid_68', 'businessid_41', 'businessid_10', 'businessid_45', 'businessid_96', 'businessid_98', 'businessid_14', 'businessid_20', 'businessid_6', 'businessid_57', 'businessid_86', 'businessid_62', 'businessid_37'], 'var_function-call-1532397386858049905': [{'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'name': 'Candy Barrel', 'review_count': '7', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '4', 'BikeParking': 'False'}, 'hours': 'None', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'name': 'Luminosity', 'review_count': '39', 'is_open': '1', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'True', 'NoiseLevel': "u'quiet'", 'WiFi': "u'no'"}, 'hours': {'Monday': '10:0-21:0', 'Tuesday': '10:0-21:0', 'Wednesday': '10:0-21:0', 'Thursday': '10:0-21:0', 'Friday': '10:0-21:0', 'Saturday': '10:0-21:0', 'Sunday': '11:0-18:0'}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10', 'name': 'China Wok', 'review_count': '20', 'is_open': '1', 'attributes': {'RestaurantsGoodForGroups': 'True', 'RestaurantsDelivery': 'False', 'RestaurantsTakeOut': 'True', 'HasTV': 'True', 'BusinessAcceptsCreditCards': 'True', 'Ambience': "{'touristy': False, 'hipster': False, 'romantic': False, 'divey': False, 'intimate': False, 'trendy': False, 'upscale': False, 'classy': False, 'casual': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}", 'BusinessParking': "{u'valet': False, u'garage': False, u'street': False, u'lot': True, u'validated': False}"}, 'hours': 'None', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}], 'var_function-call-8420091690145602786': {'top_5': [['Beauty & Spas', 4], ['Health & Medical', 3], ['Nail Salons', 2], ['Hair Removal', 2], ['Waxing', 2]], 'debug': [{'bid': 'businessid_41', 'cats': ['Internal Medicine', 'Doctors', 'Health & Medical'], 'count': 1, 'desc': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'bid': 'businessid_33', 'cats': ['Nail Salons', 'Hair Removal', 'Beauty & Spas', 'Waxing'], 'count': 2, 'desc': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'bid': 'businessid_74', 'cats': ['Candy Stores', 'Specialty Food', 'Food'], 'count': 2, 'desc': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'bid': 'businessid_92', 'cats': ['Cosmetics & Beauty Supply', 'Cosmetic Dentists', 'Tanning', 'Teeth Whitening', 'Beauty & Spas', 'Dentists', 'Shopping', 'Blow Dry/Out Services', 'Health & Medical', 'Spray Tanning', 'Hair Salons'], 'count': 2, 'desc': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'bid': 'businessid_10', 'cats': ['Restaurants', 'Chinese'], 'count': 1, 'desc': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}]}, 'var_function-call-17845022333842386003': 5, 'var_function-call-530160267585222203': [{'_id': '6859a000fe8b31cd7362e30d', 'business_id': 'businessid_13', 'name': 'Avian Glen Winery', 'review_count': '12', 'is_open': '1', 'attributes': {'RestaurantsPriceRange2': '2', 'RestaurantsTakeOut': 'True', 'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'False', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '12:0-20:0', 'Tuesday': '12:0-20:0', 'Wednesday': '12:0-20:0', 'Thursday': '12:0-20:0', 'Friday': '12:0-20:0', 'Saturday': '12:0-20:0', 'Sunday': '12:0-20:0'}, 'description': 'Located at 3545 Almaville Rd in Smyrna, TN, this establishment offers a delightful experience encompassing Food, Arts & Entertainment, Wineries, and a Wine Tasting Room.'}], 'var_function-call-12816037468976728331': 'file_storage/function-call-12816037468976728331.json'}

exec(code, env_args)
