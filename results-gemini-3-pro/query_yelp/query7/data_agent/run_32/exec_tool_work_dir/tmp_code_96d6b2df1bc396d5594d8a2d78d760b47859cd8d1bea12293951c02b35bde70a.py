code = """import json
import re

# Load reviews
reviews = locals()['var_function-call-11067263071687489332']
# Load businesses (could be list or file path)
b_data = locals()['var_function-call-12682879445057223057']
if isinstance(b_data, str) and not isinstance(b_data, list):
    # It's a file path
    with open(b_data, 'r') as f:
        businesses = json.load(f)
else:
    businesses = b_data

business_counts = {}

def get_year(date_str):
    match = re.search(r'\d{4}', date_str)
    if match:
        return int(match.group(0))
    return 0

for r in reviews:
    y = get_year(r['date'])
    if y >= 2016:
        b_ref = r['business_ref']
        b_id = b_ref.replace('businessref_', 'businessid_')
        business_counts[b_id] = business_counts.get(b_id, 0) + 1

category_counts = {}

def extract_categories(desc):
    text = desc
    
    # Pattern 1: category of 'A, B'
    match = re.search(r"category of '([^']+)'", text)
    if match:
        content = match.group(1)
        return [c.strip() for c in content.split(',')]
    
    # Pattern 2: keywords
    keywords = ["services in", "including", "categories of", "destination for", "seeking", "ranging from"]
    start_idx = -1
    used_kw = ""
    for kw in keywords:
        idx = text.find(kw)
        if idx != -1:
            start_idx = idx + len(kw)
            used_kw = kw
            break
    
    if start_idx != -1:
        sub = text[start_idx:]
        # Remove trailing period
        sub = sub.strip().rstrip('.')
        
        # Split by comma
        parts = sub.split(',')
        
        cleaned_parts = []
        for i, part in enumerate(parts):
            part = part.strip()
            # Remove "and "
            if part.startswith('and '):
                part = part[4:]
            
            # Special handling for "ranging from ... to X"
            if used_kw == "ranging from" and part.startswith("to "):
                part = part[3:]
            
            # Clean up potential suffix in the last part
            if i == len(parts) - 1:
                # "making it...", "to meet...", "for all..."
                # Heuristic: split by words, stop at lowercase (unless & or known)
                tokens = part.split(' ')
                cat_tokens = []
                for t in tokens:
                    if not t: continue
                    # Clean punctuation attached to word?
                    # t might be "needs." (already stripped period at end of string, but maybe internal?)
                    # "making it..." -> "making" starts with lowercase.
                    if t[0].isupper() or t in ['&', 'and', 'of', 'in', '/'] or t[0].isdigit(): 
                        cat_tokens.append(t)
                    else:
                        break
                part = ' '.join(cat_tokens)
            
            if part:
                cleaned_parts.append(part)
        return cleaned_parts
    
    return []

b_map = {b['business_id']: b['description'] for b in businesses}

for b_id, count in business_counts.items():
    if b_id in b_map:
        cats = extract_categories(b_map[b_id])
        for c in cats:
            c = c.strip()
            if c:
                category_counts[c] = category_counts.get(c, 0) + count

sorted_cats = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)

print("__RESULT__:")
print(json.dumps(sorted_cats[:10]))"""

env_args = {'var_function-call-11207273361998681301': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-5799923388676594119': [{'user_id': 'userid_286', 'name': 'Todd', 'review_count': '376', 'yelping_since': '15 Jan 2009, 16:40', 'useful': '1373', 'funny': '723', 'cool': '639', 'elite': '2010,2011,2012,2013,2014'}], 'var_function-call-12004838686829524238': [{'review_id': 'reviewid_135', 'user_id': 'userid_548', 'business_ref': 'businessref_34', 'rating': '2', 'useful': '0', 'funny': '0', 'cool': '0', 'text': "Sure, it's cheap, but there isn't much to see. I think you'd have to have a big interest in the topic to find it exciting, and kids would be bored. I think it only lasted maybe 10-15 minutes. Our tour person was somewhat knowledgeable and seemed into it, but he didn't give us much time to read the information on each level. I had to take photos of the plaques to read later, and half of them need replacing, as they are so sun-bleached they're virtually unreadable (tour guide said they're being replaced soon and that the other half were already replaced). I really thought it needed to be higher up to give a good view. The Lewis and Clark State Historic Site just down the road was more interesting and free. If you live around here like I do and have nothing better to do, you might want to give it a go if the topic interests you, but if you're a tourist, this is not something you should waste your time on.", 'date': 'August 01, 2016 at 03:44 AM'}], 'var_function-call-2076200190323499580': [{'count_star()': '66'}], 'var_function-call-11067263071687489332': [{'business_ref': 'businessref_79', 'date': '17 Jul 2020, 20:30'}, {'business_ref': 'businessref_67', 'date': '2018-01-02 21:35:31'}, {'business_ref': 'businessref_37', 'date': '28 Sep 2016, 17:19'}, {'business_ref': 'businessref_9', 'date': '14 Nov 2016, 15:01'}, {'business_ref': 'businessref_57', 'date': 'June 03, 2016 at 09:43 PM'}, {'business_ref': 'businessref_8', 'date': '2016-03-12 14:19:00'}, {'business_ref': 'businessref_21', 'date': 'May 07, 2016 at 03:17 PM'}, {'business_ref': 'businessref_14', 'date': 'October 16, 2016 at 09:09 PM'}, {'business_ref': 'businessref_6', 'date': '07 Jul 2018, 17:56'}, {'business_ref': 'businessref_15', 'date': '29 Jul 2016, 13:48'}, {'business_ref': 'businessref_3', 'date': 'May 20, 2017 at 06:28 PM'}, {'business_ref': 'businessref_40', 'date': '2018-11-25 23:09:00'}, {'business_ref': 'businessref_96', 'date': '2016-02-25 04:58:04'}, {'business_ref': 'businessref_62', 'date': '2018-01-09 15:08:10'}, {'business_ref': 'businessref_71', 'date': 'June 02, 2020 at 01:31 PM'}, {'business_ref': 'businessref_21', 'date': '2019-09-05 19:50:40'}, {'business_ref': 'businessref_79', 'date': 'August 27, 2020 at 10:09 PM'}, {'business_ref': 'businessref_25', 'date': 'December 12, 2016 at 05:23 PM'}, {'business_ref': 'businessref_37', 'date': 'February 15, 2016 at 01:48 PM'}, {'business_ref': 'businessref_96', 'date': 'September 26, 2016 at 07:47 PM'}, {'business_ref': 'businessref_12', 'date': '2016-09-19 19:54:00'}, {'business_ref': 'businessref_91', 'date': '2019-10-20 14:16:18'}, {'business_ref': 'businessref_79', 'date': '2019-04-18 00:17:00'}, {'business_ref': 'businessref_29', 'date': 'September 23, 2021 at 09:12 PM'}, {'business_ref': 'businessref_60', 'date': 'December 22, 2020 at 08:14 PM'}, {'business_ref': 'businessref_14', 'date': '2016-05-06 16:02:13'}, {'business_ref': 'businessref_61', 'date': '2016-08-30 14:10:16'}, {'business_ref': 'businessref_51', 'date': 'May 17, 2016 at 06:50 PM'}, {'business_ref': 'businessref_21', 'date': '2016-05-10 20:15:12'}, {'business_ref': 'businessref_86', 'date': '12 Oct 2017, 23:50'}, {'business_ref': 'businessref_82', 'date': '2017-04-27 13:57:02'}, {'business_ref': 'businessref_4', 'date': '2016-12-14 03:32:00'}, {'business_ref': 'businessref_39', 'date': '02 Mar 2016, 01:50'}, {'business_ref': 'businessref_79', 'date': '31 Aug 2016, 22:07'}, {'business_ref': 'businessref_3', 'date': '20 Apr 2017, 08:10'}, {'business_ref': 'businessref_21', 'date': '28 Sep 2016, 21:28'}, {'business_ref': 'businessref_13', 'date': 'April 03, 2021 at 01:23 AM'}, {'business_ref': 'businessref_45', 'date': 'April 21, 2017 at 12:49 PM'}, {'business_ref': 'businessref_40', 'date': '2018-11-28 02:47:00'}, {'business_ref': 'businessref_44', 'date': '2019-10-30 00:07:28'}, {'business_ref': 'businessref_6', 'date': '26 Jan 2017, 00:30'}, {'business_ref': 'businessref_9', 'date': 'April 22, 2017 at 05:50 PM'}, {'business_ref': 'businessref_60', 'date': '03 Mar 2021, 10:51'}, {'business_ref': 'businessref_85', 'date': '2019-05-26 02:42:15'}, {'business_ref': 'businessref_16', 'date': '13 Jun 2016, 00:09'}, {'business_ref': 'businessref_82', 'date': 'September 29, 2016 at 10:16 PM'}, {'business_ref': 'businessref_88', 'date': 'January 10, 2016 at 02:47 AM'}, {'business_ref': 'businessref_13', 'date': 'December 02, 2017 at 10:06 PM'}, {'business_ref': 'businessref_44', 'date': 'December 17, 2016 at 04:33 PM'}, {'business_ref': 'businessref_15', 'date': 'November 09, 2017 at 09:40 PM'}, {'business_ref': 'businessref_26', 'date': 'February 22, 2019 at 06:40 PM'}, {'business_ref': 'businessref_44', 'date': '02 Jan 2016, 22:14'}, {'business_ref': 'businessref_76', 'date': 'May 23, 2018 at 04:04 PM'}, {'business_ref': 'businessref_67', 'date': '2020-01-03 13:54:00'}, {'business_ref': 'businessref_42', 'date': 'October 05, 2019 at 09:47 PM'}, {'business_ref': 'businessref_88', 'date': '2016-09-27 15:07:00'}, {'business_ref': 'businessref_57', 'date': 'August 28, 2017 at 11:10 PM'}, {'business_ref': 'businessref_67', 'date': '30 Dec 2018, 21:55'}, {'business_ref': 'businessref_55', 'date': '2020-02-26 14:27:00'}, {'business_ref': 'businessref_40', 'date': 'April 09, 2016 at 09:51 PM'}], 'var_function-call-13826952471968783520': [{'count_star()': '60'}], 'var_function-call-6966303239727768892': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-6063302655149728285': 'file_storage/function-call-6063302655149728285.json', 'var_function-call-9031899379296763324': [['Restaurants', 12], ['Food', 11], ['American (New)', 8], ['Shopping', 8], ['American (Traditional)', 7], ['Automotive', 6], ['Breakfast & Brunch', 6], ['Active Life', 5], ['Local Services', 5], ['Auto Repair', 5]], 'var_function-call-11064541541903352327': ['businessid_13', 'businessid_4', 'businessid_86', 'businessid_76', 'businessid_15', 'businessid_26', 'businessid_44', 'businessid_88', 'businessid_8', 'businessid_6', 'businessid_61', 'businessid_51', 'businessid_42', 'businessid_16', 'businessid_85', 'businessid_71', 'businessid_37', 'businessid_21', 'businessid_60', 'businessid_39', 'businessid_67', 'businessid_62', 'businessid_40', 'businessid_9', 'businessid_57', 'businessid_14', 'businessid_3', 'businessid_96', 'businessid_91', 'businessid_82', 'businessid_29', 'businessid_79', 'businessid_45', 'businessid_55', 'businessid_12', 'businessid_25'], 'var_function-call-12682879445057223057': [{'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2b4', 'business_id': 'businessid_29', 'name': "Aster's Floral Shop", 'review_count': '25', 'is_open': '1', 'attributes': {'BikeParking': 'True', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '2', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsDelivery': 'None'}, 'hours': {'Monday': '9:0-18:0', 'Tuesday': '9:0-18:0', 'Wednesday': '9:0-18:0', 'Thursday': '9:0-18:0', 'Friday': '9:0-18:0', 'Saturday': '9:0-18:0'}, 'description': 'Located at 41 Haddon Ave in Collingswood, NJ, this versatile establishment offers a range of services including Wedding Planning, Flowers & Gifts, Event Planning & Services, Financial Services, Shopping, and Florists.'}, {'_id': '6859a000fe8b31cd7362e2b6', 'business_id': 'businessid_61', 'name': 'Brandon Family Medical Care', 'review_count': '17', 'is_open': '1', 'attributes': {'ByAppointmentOnly': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'hours': {'Monday': '8:0-17:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '12:0-20:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1218 Millennium Pkwy in Brandon, FL, this facility provides essential services in the categories of Medical Centers, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2b8', 'business_id': 'businessid_8', 'name': 'Uber', 'review_count': '218', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '0:0-0:0', 'Wednesday': '0:0-0:0', 'Thursday': '0:0-0:0', 'Friday': '0:0-0:0'}, 'description': 'This Philadelphia, PA location offers a range of services including Hotels & Travel, Taxis, Transportation, Local Services, and Automotive to meet all your travel and transportation needs.'}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91', 'name': 'Cafe Porche and snowbar', 'review_count': '172', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'WiFi': "u'free'", 'WheelchairAccessible': 'True', 'Caters': 'True', 'HasTV': 'True', 'HappyHour': 'False', 'Ambience': "{'touristy': None, 'hipster': None, 'romantic': None, 'divey': None, 'intimate': True, 'trendy': None, 'upscale': None, 'classy': True, 'casual': True}", 'RestaurantsDelivery': 'True', 'RestaurantsPriceRange2': '2', 'GoodForKids': 'True', 'RestaurantsAttire': "u'casual'", 'BikeParking': 'True', 'OutdoorSeating': 'True', 'NoiseLevel': "u'quiet'", 'RestaurantsGoodForGroups': 'True', 'RestaurantsTakeOut': 'True', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsReservations': 'False', 'GoodForMeal': "{'dessert': None, 'latenight': None, 'lunch': True, 'dinner': None, 'brunch': True, 'breakfast': True}", 'Alcohol': "u'beer_and_wine'", 'RestaurantsTableService': 'True', 'Corkage': 'False', 'BYOB': 'True'}, 'hours': {'Monday': '0:0-0:0', 'Friday': '8:30-14:30', 'Saturday': '8:30-14:30', 'Sunday': '9:0-14:30'}, 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}]}

exec(code, env_args)
