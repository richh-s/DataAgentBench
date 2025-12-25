code = """import pandas as pd
import json

# Load previous results
reviews = locals()['var_function-call-18282287339917161070']

# Load businesses from file
file_path = locals()['var_function-call-434421136231446142']
with open(file_path, 'r') as f:
    businesses = json.load(f)

# Map business_id -> description
bus_desc = {b['business_id']: b.get('description', '') for b in businesses}

def extract_categories(desc):
    if not desc: return []
    
    keywords = [
        "providing a range of services in ",
        "offers a range of services in ",
        "offers a wide range of services, including ",
        "including ",
        "destination for ",
        "fields of ",
        "category of ",
        "seeking ",
        "selection of "
    ]
    keywords.sort(key=len, reverse=True)
    
    start_idx = -1
    for k in keywords:
        idx = desc.rfind(k)
        if idx != -1:
            start_idx = idx + len(k)
            break
            
    if start_idx == -1:
        return []
        
    text = desc[start_idx:]
    text = text.strip().strip("'").strip('"')
    if text.endswith('.'):
        text = text[:-1]
        
    parts = text.split(',')
    cats = []
    
    for part in parts:
        p = part.strip()
        if not p: continue
        if p.lower().startswith("and "):
            p = p[4:]
            
        words = p.split(' ')
        clean_words = []
        for w in words:
            if not w: continue
            is_connector = w.lower() in ['&', 'and', 'of', 'in', 'the', '-', '/']
            is_cap = w[0].isupper() or not w[0].isalpha()
            
            if is_cap or is_connector:
                clean_words.append(w)
            else:
                break
        
        while clean_words and clean_words[-1].lower() in ['&', 'and', 'of', 'in', 'the', '-', '/', 'for', 'with']:
             clean_words.pop()
             
        cat = " ".join(clean_words)
        if cat.lower().startswith("and "):
            cat = cat[4:]
            
        if cat and len(cat) > 2:
            cats.append(cat)
            
    return cats

category_counts = {}

for r in reviews:
    ref = r['business_ref']
    bid = ref.replace('businessref_', 'businessid_')
    count = int(r['count'])
    
    if bid in bus_desc:
        desc = bus_desc[bid]
        cats = extract_categories(desc)
        for c in cats:
            category_counts[c] = category_counts.get(c, 0) + count

sorted_cats = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)

print("__RESULT__:")
print(json.dumps(sorted_cats[:5]))"""

env_args = {'var_function-call-6938931346648040044': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-18079484843366275396': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}], 'var_function-call-9731683570976762056': [{'user_id': 'userid_286', 'name': 'Todd', 'review_count': '376', 'yelping_since': '15 Jan 2009, 16:40', 'useful': '1373', 'funny': '723', 'cool': '639', 'elite': '2010,2011,2012,2013,2014'}], 'var_function-call-9115192223771584575': [{'review_id': 'reviewid_135', 'user_id': 'userid_548', 'business_ref': 'businessref_34', 'rating': '2', 'useful': '0', 'funny': '0', 'cool': '0', 'text': "Sure, it's cheap, but there isn't much to see. I think you'd have to have a big interest in the topic to find it exciting, and kids would be bored. I think it only lasted maybe 10-15 minutes. Our tour person was somewhat knowledgeable and seemed into it, but he didn't give us much time to read the information on each level. I had to take photos of the plaques to read later, and half of them need replacing, as they are so sun-bleached they're virtually unreadable (tour guide said they're being replaced soon and that the other half were already replaced). I really thought it needed to be higher up to give a good view. The Lewis and Clark State Historic Site just down the road was more interesting and free. If you live around here like I do and have nothing better to do, you might want to give it a go if the topic interests you, but if you're a tourist, this is not something you should waste your time on.", 'date': 'August 01, 2016 at 03:44 AM'}], 'var_function-call-3001861919564569660': [{'date': 'August 01, 2016 at 03:44 AM'}, {'date': 'June 14, 2021 at 11:39 AM'}, {'date': '29 May 2013, 23:01'}, {'date': '21 May 2016, 18:48'}, {'date': 'November 01, 2021 at 05:11 PM'}, {'date': '2013-07-08 21:47:00'}, {'date': 'March 02, 2009 at 09:43 PM'}, {'date': 'March 16, 2014 at 12:40 AM'}, {'date': 'September 18, 2014 at 05:50 PM'}, {'date': '17 Apr 2017, 14:04'}], 'var_function-call-18282287339917161070': [{'business_ref': 'businessref_79', 'count': '4'}, {'business_ref': 'businessref_13', 'count': '2'}, {'business_ref': 'businessref_44', 'count': '3'}, {'business_ref': 'businessref_6', 'count': '2'}, {'business_ref': 'businessref_71', 'count': '1'}, {'business_ref': 'businessref_91', 'count': '1'}, {'business_ref': 'businessref_16', 'count': '1'}, {'business_ref': 'businessref_55', 'count': '1'}, {'business_ref': 'businessref_29', 'count': '1'}, {'business_ref': 'businessref_39', 'count': '1'}, {'business_ref': 'businessref_67', 'count': '3'}, {'business_ref': 'businessref_15', 'count': '2'}, {'business_ref': 'businessref_9', 'count': '2'}, {'business_ref': 'businessref_25', 'count': '1'}, {'business_ref': 'businessref_12', 'count': '1'}, {'business_ref': 'businessref_60', 'count': '2'}, {'business_ref': 'businessref_51', 'count': '1'}, {'business_ref': 'businessref_40', 'count': '3'}, {'business_ref': 'businessref_61', 'count': '1'}, {'business_ref': 'businessref_82', 'count': '2'}, {'business_ref': 'businessref_45', 'count': '1'}, {'business_ref': 'businessref_76', 'count': '1'}, {'business_ref': 'businessref_14', 'count': '2'}, {'business_ref': 'businessref_3', 'count': '2'}, {'business_ref': 'businessref_96', 'count': '2'}, {'business_ref': 'businessref_21', 'count': '4'}, {'business_ref': 'businessref_4', 'count': '1'}, {'business_ref': 'businessref_88', 'count': '2'}, {'business_ref': 'businessref_26', 'count': '1'}, {'business_ref': 'businessref_37', 'count': '2'}, {'business_ref': 'businessref_57', 'count': '2'}, {'business_ref': 'businessref_8', 'count': '1'}, {'business_ref': 'businessref_62', 'count': '1'}, {'business_ref': 'businessref_86', 'count': '1'}, {'business_ref': 'businessref_85', 'count': '1'}, {'business_ref': 'businessref_42', 'count': '1'}], 'var_function-call-737630227541983663': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-434421136231446142': 'file_storage/function-call-434421136231446142.json'}

exec(code, env_args)
