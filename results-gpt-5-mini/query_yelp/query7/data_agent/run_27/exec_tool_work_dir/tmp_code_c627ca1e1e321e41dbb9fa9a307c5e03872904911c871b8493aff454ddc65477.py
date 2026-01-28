code = """import json
# var_call_wb4PTjyUx7Se1kVBOZd7U2aZ is path to the large JSON file
path = var_call_wb4PTjyUx7Se1kVBOZd7U2aZ
with open(path, 'r') as f:
    businesses = json.load(f)
# Load the earlier aggregated review counts
agg = var_call_1tLnaUWBiPOGR6WZQU5uzdOF
# build map from businessid to review_count
agg_map = { 'businessid_'+r['business_ref'].split('_',1)[1]: int(r['review_count']) for r in agg }
# For each business in businesses, extract categories from description
# The description contains comma-separated category strings at the end; we'll attempt to extract capitalized categories after 'offers' or 'offers a range'
import re
results = []
for b in businesses:
    bid = b.get('business_id')
    if bid in agg_map:
        desc = b.get('description','')
        # Try to extract categories by finding the segment after 'offers' or 'offers a range of services in' or 'this establishment offers'
        m = re.search(r'offers(?: a range of services in| a range of services| a range of options ranging from| a diverse range of services and products| a delightful array of options ranging from)? (.+)\.?$', desc, re.IGNORECASE)
        cats = []
        if m:
            cat_str = m.group(1)
            # split by commas and 'and'
            parts = re.split(r',| and | & ', cat_str)
            # clean
            parts = [p.strip().strip('.') for p in parts if p.strip()]
            cats = parts
        else:
            # fallback: take last 5 comma-separated tokens
            parts = [p.strip() for p in desc.split(',')]
            cats = parts[-5:]
        results.append({'business_id': bid, 'name': b.get('name'), 'categories': cats, 'review_count': agg_map[bid]})
# Now aggregate review counts per category
from collections import defaultdict
cat_counts = defaultdict(int)
for r in results:
    for c in r['categories']:
        cat_counts[c] += r['review_count']
# convert to list and sort
cat_list = [{'category': k, 'review_count': v} for k,v in cat_counts.items()]
cat_list.sort(key=lambda x: x['review_count'], reverse=True)
# take top 5
top5 = cat_list[:5]
print('__RESULT__:')
print(json.dumps(top5))"""

env_args = {'var_call_g1tst1j7lstkCjXybb4BIhAA': ['business', 'checkin'], 'var_call_06DWp10e5tWQ2vU2967SEB8u': ['review', 'tip', 'user'], 'var_call_mH8Mx4R4v8eK4eV6UOSnckYT': [{'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'attributes': 'None', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'business_id': 'businessid_74', 'name': 'Candy Barrel', 'review_count': '7', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '4', 'BikeParking': 'False'}, 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'business_id': 'businessid_92', 'name': 'Luminosity', 'review_count': '39', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'True', 'NoiseLevel': "u'quiet'", 'WiFi': "u'no'"}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'business_id': 'businessid_64', 'name': 'Nail Care Salon', 'review_count': '6', 'attributes': {'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': True, 'valet': False}", 'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'True', 'WiFi': "u'free'"}, 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'business_id': 'businessid_52', 'name': 'Architectural Antiques of Indianapolis', 'review_count': '6', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'BikeParking': 'True'}, 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.'}, {'business_id': 'businessid_29', 'name': "Aster's Floral Shop", 'review_count': '25', 'attributes': {'BikeParking': 'True', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '2', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsDelivery': 'None'}, 'description': 'Located at 41 Haddon Ave in Collingswood, NJ, this versatile establishment offers a range of services including Wedding Planning, Flowers & Gifts, Event Planning & Services, Financial Services, Shopping, and Florists.'}], 'var_call_1tLnaUWBiPOGR6WZQU5uzdOF': [{'business_ref': 'businessref_45', 'review_count': '3'}, {'business_ref': 'businessref_96', 'review_count': '2'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_33', 'review_count': '2'}, {'business_ref': 'businessref_36', 'review_count': '2'}, {'business_ref': 'businessref_60', 'review_count': '2'}, {'business_ref': 'businessref_57', 'review_count': '2'}, {'business_ref': 'businessref_92', 'review_count': '2'}, {'business_ref': 'businessref_13', 'review_count': '1'}, {'business_ref': 'businessref_6', 'review_count': '1'}, {'business_ref': 'businessref_15', 'review_count': '1'}, {'business_ref': 'businessref_12', 'review_count': '1'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_86', 'review_count': '1'}, {'business_ref': 'businessref_62', 'review_count': '1'}, {'business_ref': 'businessref_37', 'review_count': '1'}, {'business_ref': 'businessref_79', 'review_count': '1'}, {'business_ref': 'businessref_31', 'review_count': '1'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}, {'business_ref': 'businessref_98', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}, {'business_ref': 'businessref_26', 'review_count': '1'}, {'business_ref': 'businessref_68', 'review_count': '1'}], 'var_call_mYuIO5sQ3g8xJ1JKkWtpKqZb': ['businessid_45', 'businessid_96', 'businessid_74', 'businessid_66', 'businessid_33', 'businessid_36', 'businessid_60', 'businessid_57', 'businessid_92', 'businessid_13', 'businessid_6', 'businessid_15', 'businessid_12', 'businessid_53', 'businessid_86', 'businessid_62', 'businessid_37', 'businessid_79', 'businessid_31', 'businessid_41', 'businessid_10', 'businessid_98', 'businessid_14', 'businessid_20', 'businessid_26', 'businessid_68'], 'var_call_wb4PTjyUx7Se1kVBOZd7U2aZ': 'file_storage/call_wb4PTjyUx7Se1kVBOZd7U2aZ.json'}

exec(code, env_args)
