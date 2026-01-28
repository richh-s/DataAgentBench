code = """import json
# Load the review counts from storage variable
reviews = var_call_KEwW77S90IhnCwKqNjtv1J83
# Load business documents; var_call_YoJ4xeGCUy5yInItC68HIK70 may be a file path
bdata = var_call_YoJ4xeGCUy5yInItC68HIK70
if isinstance(bdata, str):
    with open(bdata, 'r') as f:
        businesses = json.load(f)
else:
    businesses = bdata
# Build mapping from business_id to categories (as list)
import re
biz_categories = {}
for b in businesses:
    bid = b.get('business_id')
    cats = []
    # prefer explicit 'categories' field
    if 'categories' in b and b.get('categories'):
        c = b.get('categories')
        if isinstance(c, list):
            cats = [str(x).strip() for x in c if x]
        else:
            cats = [x.strip() for x in str(c).split(',') if x.strip()]
    else:
        desc = b.get('description') or ''
        desc = desc.strip()
        # Try to extract after certain phrases
        markers = ['in the categories of', 'in the category of', 'offers a range of services in', 'offers a diverse range of services in', 'offers a range of services, including', 'including', 'specializes in', 'this establishment offers a wide range of services including', 'this establishment offers a wide range of services, including', 'offers a wide range of services, including', 'offers a wide range of services', 'offers a diverse selection of', 'offers a diverse range of', 'this business offers a diverse range of services and products in the fields of', 'this business offers a diverse range of services and products in the fields of']
        lower = desc.lower()
        start = None
        for m in markers:
            idx = lower.find(m)
            if idx!=-1:
                start = idx + len(m)
                break
        if start is None:
            # try after the first occurrence of 'this' after the address
            m = re.search(r"this\b", lower)
            if m:
                start = m.end()
        if start is None:
            # fallback: after the first comma following the first 'in '
            m = re.search(r"in [A-Za-z ]+,", desc)
            if m:
                start = m.end()
        if start is None:
            # use whole description
            candidate = desc
        else:
            candidate = desc[start:]
        # split candidate by commas and ' and '
        parts = re.split(r",| and |;|/", candidate)
        cleaned = []
        for p in parts:
            p = p.strip()
            # remove leading words like 'this', 'offers', 'including'
            p = re.sub(r'^(this|offers|offering|offering a|offering an|provides|providing|a range of|a diverse range of|a diverse selection of)\b', '', p, flags=re.I).strip()
            # remove location words (addresses often contain numbers, street, rd, ave, in CITY)
            if re.search(r'\d', p):
                continue
            if len(p) < 2:
                continue
            # remove trailing phrases like 'making it a must-visit for anyone seeking X'
            p = re.sub(r'making it.*$', '', p, flags=re.I).strip()
            # Filter out generic words
            if p.lower().startswith('located') or p.lower().startswith('located at'):
                continue
            cleaned.append(p)
        # further split items that contain ' in ' or ':'
        final = []
        for item in cleaned:
            # often items contain words like 'Restaurants' or 'Restaurants, Chinese'
            # split on ',', keep fragments
            frags = [f.strip() for f in re.split(r",", item) if f.strip()]
            for f in frags:
                # ignore fragments that look like sentences
                if len(f.split())>10:
                    continue
                final.append(f)
        # if nothing found, leave empty
        cats = final
    # normalize categories (strip, title case)
    cats_norm = []
    for c in cats:
        c2 = c.strip()
        # remove trailing 'and' or '&'
        c2 = re.sub(r'^(and |& )| (and|&)$', '', c2)
        if c2:
            # remove duplicated spaces
            c2 = re.sub(r'\s+', ' ', c2)
            cats_norm.append(c2)
    biz_categories[bid] = cats_norm
# Aggregate review counts per category
from collections import defaultdict
cat_counts = defaultdict(int)
for rec in reviews:
    bref = rec.get('business_ref')
    cnt = int(rec.get('review_count') or 0)
    # transform businessref_X -> businessid_X
    if bref.startswith('businessref_'):
        bid = 'businessid_' + bref.split('_',1)[1]
    else:
        bid = bref
    cats = biz_categories.get(bid, [])
    if not cats:
        # as fallback, try to find business by id numeric match ignoring prefix
        keynum = bid.split('_')[-1]
        found = False
        for k,v in biz_categories.items():
            if k and k.endswith('_'+keynum):
                for c in v:
                    cat_counts[c] += cnt
                found = True
                break
        if not found:
            # count under Unknown
            cat_counts['Unknown'] += cnt
    else:
        for c in cats:
            cat_counts[c] += cnt
# Prepare sorted top 5
items = sorted(cat_counts.items(), key=lambda x: x[1], reverse=True)
top5 = [{'category': k, 'total_reviews': v} for k,v in items[:5]]
# Print according to required format
print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_lV0PmYPXdCw4IVmeGAHX3mBh': ['business', 'checkin'], 'var_call_VpVIwRz3jJlZIPyzHn66lDgR': ['review', 'tip', 'user'], 'var_call_fQRtz3pYtJn4xBIe586AGNeV': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'attributes': 'None', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'name': 'Candy Barrel', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '4', 'BikeParking': 'False'}, 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'name': 'Luminosity', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'True', 'NoiseLevel': "u'quiet'", 'WiFi': "u'no'"}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64', 'name': 'Nail Care Salon', 'attributes': {'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': True, 'valet': False}", 'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'True', 'WiFi': "u'free'"}, 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52', 'name': 'Architectural Antiques of Indianapolis', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'BikeParking': 'True'}, 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.'}, {'_id': '6859a000fe8b31cd7362e2b4', 'business_id': 'businessid_29', 'name': "Aster's Floral Shop", 'attributes': {'BikeParking': 'True', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '2', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsDelivery': 'None'}, 'description': 'Located at 41 Haddon Ave in Collingswood, NJ, this versatile establishment offers a range of services including Wedding Planning, Flowers & Gifts, Event Planning & Services, Financial Services, Shopping, and Florists.'}], 'var_call_s53ZCSpupaX8vpBau4zR5snH': [{'user_id': 'userid_286', 'yelping_since': '15 Jan 2009, 16:40'}, {'user_id': 'userid_1331', 'yelping_since': '13 Jul 2010, 15:42'}, {'user_id': 'userid_1880', 'yelping_since': '2010-09-07 23:24:36'}, {'user_id': 'userid_271', 'yelping_since': 'October 23, 2011 at 07:47 PM'}, {'user_id': 'userid_534', 'yelping_since': '2011-08-30 13:46:26'}, {'user_id': 'userid_1997', 'yelping_since': '2009-12-02 18:54:31'}, {'user_id': 'userid_1386', 'yelping_since': '2009-04-15 12:46:06'}, {'user_id': 'userid_237', 'yelping_since': 'October 04, 2009 at 05:59 PM'}, {'user_id': 'userid_596', 'yelping_since': '20 Apr 2008, 16:55'}, {'user_id': 'userid_948', 'yelping_since': '2007-07-28 22:22:09'}, {'user_id': 'userid_42', 'yelping_since': 'January 14, 2009 at 06:31 PM'}, {'user_id': 'userid_604', 'yelping_since': 'October 10, 2009 at 01:37 AM'}, {'user_id': 'userid_1291', 'yelping_since': '17 Nov 2008, 02:26'}, {'user_id': 'userid_995', 'yelping_since': '2010-04-29 14:32:53'}, {'user_id': 'userid_1630', 'yelping_since': '26 Sep 2009, 02:31'}, {'user_id': 'userid_1857', 'yelping_since': 'May 03, 2009 at 08:19 PM'}, {'user_id': 'userid_1936', 'yelping_since': 'July 21, 2008 at 06:04 PM'}, {'user_id': 'userid_288', 'yelping_since': 'August 13, 2009 at 01:09 PM'}, {'user_id': 'userid_1956', 'yelping_since': '2011-08-19 18:09:41'}, {'user_id': 'userid_529', 'yelping_since': '2009-12-14 01:40:43'}, {'user_id': 'userid_1469', 'yelping_since': '2009-11-15 20:31:44'}, {'user_id': 'userid_1802', 'yelping_since': '2010-04-22 06:45:06'}, {'user_id': 'userid_809', 'yelping_since': 'May 18, 2010 at 01:22 AM'}, {'user_id': 'userid_1157', 'yelping_since': 'May 21, 2011 at 03:22 PM'}, {'user_id': 'userid_1619', 'yelping_since': 'September 02, 2009 at 07:31 PM'}, {'user_id': 'userid_177', 'yelping_since': '2009-06-19 17:41:48'}, {'user_id': 'userid_474', 'yelping_since': '2009-02-17 04:12:33'}, {'user_id': 'userid_970', 'yelping_since': '31 Oct 2006, 20:51'}, {'user_id': 'userid_1306', 'yelping_since': '2011-12-14 23:17:41'}, {'user_id': 'userid_606', 'yelping_since': 'September 19, 2009 at 02:55 AM'}, {'user_id': 'userid_899', 'yelping_since': '2011-02-07 00:26:48'}, {'user_id': 'userid_1465', 'yelping_since': 'June 13, 2008 at 08:02 PM'}, {'user_id': 'userid_1075', 'yelping_since': '2009-04-23 16:18:47'}, {'user_id': 'userid_1805', 'yelping_since': '2008-07-21 23:53:13'}, {'user_id': 'userid_1613', 'yelping_since': 'July 03, 2008 at 03:27 PM'}, {'user_id': 'userid_1052', 'yelping_since': 'July 14, 2011 at 10:03 PM'}, {'user_id': 'userid_82', 'yelping_since': '2006-05-29 16:04:28'}, {'user_id': 'userid_1098', 'yelping_since': '2005-07-18 06:22:37'}, {'user_id': 'userid_95', 'yelping_since': 'October 19, 2007 at 09:22 PM'}, {'user_id': 'userid_1219', 'yelping_since': 'March 05, 2010 at 12:53 AM'}, {'user_id': 'userid_1777', 'yelping_since': '13 Jun 2008, 14:48'}, {'user_id': 'userid_1860', 'yelping_since': '2008-03-06 15:18:14'}, {'user_id': 'userid_139', 'yelping_since': '11 Mar 2011, 16:49'}, {'user_id': 'userid_568', 'yelping_since': '2009-04-30 03:16:12'}, {'user_id': 'userid_714', 'yelping_since': 'August 18, 2008 at 08:13 AM'}, {'user_id': 'userid_1742', 'yelping_since': 'January 14, 2007 at 04:49 PM'}, {'user_id': 'userid_717', 'yelping_since': '2008-11-23 18:11:47'}, {'user_id': 'userid_1250', 'yelping_since': 'August 08, 2010 at 03:05 PM'}, {'user_id': 'userid_1604', 'yelping_since': '03 Jan 2010, 18:29'}, {'user_id': 'userid_1541', 'yelping_since': 'July 30, 2010 at 06:05 PM'}], 'var_call_6uNPHAv0TMILsWxhpXkD2Pdc': 'file_storage/call_6uNPHAv0TMILsWxhpXkD2Pdc.json', 'var_call_KEwW77S90IhnCwKqNjtv1J83': [{'business_ref': 'businessref_79', 'review_count': '8'}, {'business_ref': 'businessref_57', 'review_count': '7'}, {'business_ref': 'businessref_37', 'review_count': '6'}, {'business_ref': 'businessref_45', 'review_count': '5'}, {'business_ref': 'businessref_67', 'review_count': '5'}, {'business_ref': 'businessref_33', 'review_count': '5'}, {'business_ref': 'businessref_88', 'review_count': '4'}, {'business_ref': 'businessref_44', 'review_count': '4'}, {'business_ref': 'businessref_6', 'review_count': '4'}, {'business_ref': 'businessref_12', 'review_count': '4'}, {'business_ref': 'businessref_21', 'review_count': '4'}, {'business_ref': 'businessref_26', 'review_count': '4'}, {'business_ref': 'businessref_8', 'review_count': '4'}, {'business_ref': 'businessref_86', 'review_count': '4'}, {'business_ref': 'businessref_96', 'review_count': '4'}, {'business_ref': 'businessref_60', 'review_count': '4'}, {'business_ref': 'businessref_9', 'review_count': '3'}, {'business_ref': 'businessref_43', 'review_count': '3'}, {'business_ref': 'businessref_15', 'review_count': '3'}, {'business_ref': 'businessref_13', 'review_count': '3'}, {'business_ref': 'businessref_14', 'review_count': '3'}, {'business_ref': 'businessref_40', 'review_count': '3'}, {'business_ref': 'businessref_51', 'review_count': '3'}, {'business_ref': 'businessref_98', 'review_count': '3'}, {'business_ref': 'businessref_36', 'review_count': '3'}, {'business_ref': 'businessref_89', 'review_count': '3'}, {'business_ref': 'businessref_62', 'review_count': '2'}, {'business_ref': 'businessref_7', 'review_count': '2'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_92', 'review_count': '2'}, {'business_ref': 'businessref_3', 'review_count': '2'}, {'business_ref': 'businessref_82', 'review_count': '2'}, {'business_ref': 'businessref_91', 'review_count': '2'}, {'business_ref': 'businessref_17', 'review_count': '1'}, {'business_ref': 'businessref_81', 'review_count': '1'}, {'business_ref': 'businessref_31', 'review_count': '1'}, {'business_ref': 'businessref_99', 'review_count': '1'}, {'business_ref': 'businessref_25', 'review_count': '1'}, {'business_ref': 'businessref_71', 'review_count': '1'}, {'business_ref': 'businessref_61', 'review_count': '1'}, {'business_ref': 'businessref_76', 'review_count': '1'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_29', 'review_count': '1'}, {'business_ref': 'businessref_39', 'review_count': '1'}, {'business_ref': 'businessref_46', 'review_count': '1'}, {'business_ref': 'businessref_1', 'review_count': '1'}, {'business_ref': 'businessref_47', 'review_count': '1'}, {'business_ref': 'businessref_16', 'review_count': '1'}, {'business_ref': 'businessref_55', 'review_count': '1'}, {'business_ref': 'businessref_56', 'review_count': '1'}, {'business_ref': 'businessref_97', 'review_count': '1'}, {'business_ref': 'businessref_72', 'review_count': '1'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_23', 'review_count': '1'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}, {'business_ref': 'businessref_22', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}, {'business_ref': 'businessref_85', 'review_count': '1'}, {'business_ref': 'businessref_42', 'review_count': '1'}, {'business_ref': 'businessref_4', 'review_count': '1'}], 'var_call_YoJ4xeGCUy5yInItC68HIK70': 'file_storage/call_YoJ4xeGCUy5yInItC68HIK70.json'}

exec(code, env_args)
