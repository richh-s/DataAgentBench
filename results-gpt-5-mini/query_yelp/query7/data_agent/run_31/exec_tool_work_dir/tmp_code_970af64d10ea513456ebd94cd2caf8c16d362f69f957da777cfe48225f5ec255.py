code = """import json
from collections import defaultdict

# Load data
reviews = var_call_nkVrYqHXYwIsq4FUYxHtImpv
business_docs = var_call_v8M9Bj1BjWd6wAKbnSvl0C5i

# Map business_ref to counts
ref_counts = {}
for r in reviews:
    ref = r.get("business_ref")
    try:
        count = int(r.get("review_count") or 0)
    except:
        count = 0
    ref_counts[ref] = count

# Simple category extraction without backslashes
def extract_categories(desc):
    if not desc:
        return []
    txt = desc
    lowered = txt.lower()
    markers = [
        "including", "includes", "in the fields of", "in the category of",
        "offers a range of services in", "offers a range of services including",
        "offers a diverse range of services and products in", "this establishment offers a range of services",
        "making it a must-visit for anyone seeking", "in the category of"
    ]
    start = None
    for m in markers:
        idx = lowered.find(m)
        if idx != -1:
            start = idx + len(m)
            break
    if start is None:
        idx = lowered.find("in ")
        if idx != -1:
            candidate = txt[idx+3:]
        else:
            candidate = txt
    else:
        candidate = txt[start:]
    if "." in candidate:
        candidate = candidate.split(".")[0]
    candidate = candidate.replace(" and ", ", ")
    parts = [p.strip() for p in candidate.split(",") if p.strip()]
    out = []
    for p in parts:
        p2 = p.replace("/", ",").replace("&", ",")
        subs = [s.strip() for s in p2.split(",") if s.strip()]
        for s in subs:
            s2 = s
            lowers = s2.lower()
            for pref in ["the fields of", "the category of", "including", "offers a range of services in", "offers a range of services including"]:
                if lowers.startswith(pref):
                    s2 = s2[len(pref):].strip()
                    lowers = s2.lower()
            s2 = " ".join(s2.split())
            if s2:
                out.append(s2)
    seen = set()
    final = []
    for o in out:
        key = o.strip()
        if key and key.lower() not in seen:
            seen.add(key.lower())
            final.append(key)
    return final

# Aggregate counts
cat_counts = defaultdict(int)
for doc in business_docs:
    bid = doc.get("business_id")
    if not bid:
        continue
    parts = bid.split("_",1)
    bref = "businessref_" + parts[1] if len(parts)>1 else "businessref_" + bid
    count = ref_counts.get(bref, 0)
    desc = doc.get("description") or ""
    cats = extract_categories(desc)
    if not cats:
        cats = [doc.get("name")]
    for c in cats:
        cat_counts[c] += count

sorted_cats = sorted(cat_counts.items(), key=lambda x: x[1], reverse=True)
top5 = sorted_cats[:5]
result = [{"category": c, "total_reviews_from_2016_users_since_2016": v} for c, v in top5]

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_nJqvUnQMUi66jxOyU6wa4wOB': ['business', 'checkin'], 'var_call_3p3QfyePBjyxUZKAQ4Fm0yX7': ['review', 'tip', 'user'], 'var_call_nkVrYqHXYwIsq4FUYxHtImpv': [{'business_ref': 'businessref_45', 'review_count': '3'}, {'business_ref': 'businessref_57', 'review_count': '2'}, {'business_ref': 'businessref_92', 'review_count': '2'}, {'business_ref': 'businessref_60', 'review_count': '2'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_36', 'review_count': '2'}, {'business_ref': 'businessref_33', 'review_count': '2'}, {'business_ref': 'businessref_96', 'review_count': '2'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_12', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '1'}, {'business_ref': 'businessref_79', 'review_count': '1'}, {'business_ref': 'businessref_37', 'review_count': '1'}, {'business_ref': 'businessref_98', 'review_count': '1'}, {'business_ref': 'businessref_86', 'review_count': '1'}, {'business_ref': 'businessref_31', 'review_count': '1'}, {'business_ref': 'businessref_62', 'review_count': '1'}, {'business_ref': 'businessref_15', 'review_count': '1'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_6', 'review_count': '1'}, {'business_ref': 'businessref_13', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}, {'business_ref': 'businessref_26', 'review_count': '1'}], 'var_call_ppdldMTOjzk6tL9gzJlBd41o': [{'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'name': 'Candy Barrel'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'name': 'Luminosity'}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10', 'name': 'China Wok'}], 'var_call_8quh6Rjjqn78IeebMqX9AqZo': [{'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}], 'var_call_5NfF9dRE3Pav2XUVP6O9UMS7': [{'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_a91BhPZQo7BHtzY1rk7UIP5U': [{'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'name': 'Candy Barrel', 'review_count': '7', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '4', 'BikeParking': 'False'}, 'hours': 'None', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}], 'var_call_xuaHpFhLdzklbvNYYVYuyjC7': [{'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'name': 'Luminosity', 'review_count': '39', 'is_open': '1', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'True', 'NoiseLevel': "u'quiet'", 'WiFi': "u'no'"}, 'hours': {'Monday': '10:0-21:0', 'Tuesday': '10:0-21:0', 'Wednesday': '10:0-21:0', 'Thursday': '10:0-21:0', 'Friday': '10:0-21:0', 'Saturday': '10:0-21:0', 'Sunday': '11:0-18:0'}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_call_x8ZGL3LeYC1HPA4Y7gBQMkyf': [{'user_id': 'userid_746', 'yelping_since': '2016-06-23 01:59:28'}, {'user_id': 'userid_1109', 'yelping_since': '2016-10-16 18:32:25'}, {'user_id': 'userid_1950', 'yelping_since': '2016-04-16 03:42:28'}, {'user_id': 'userid_1316', 'yelping_since': '2016-12-29 21:32:44'}, {'user_id': 'userid_1182', 'yelping_since': '2016-03-20 18:41:14'}, {'user_id': 'userid_151', 'yelping_since': '2016-11-07 18:40:10'}, {'user_id': 'userid_1158', 'yelping_since': '2016-01-31 16:25:04'}, {'user_id': 'userid_508', 'yelping_since': '2016-07-08 22:37:42'}, {'user_id': 'userid_435', 'yelping_since': '2016-10-31 09:46:54'}, {'user_id': 'userid_958', 'yelping_since': '2016-03-23 20:55:45'}, {'user_id': 'userid_1879', 'yelping_since': '2016-07-08 17:56:11'}, {'user_id': 'userid_308', 'yelping_since': '2016-07-02 23:48:36'}, {'user_id': 'userid_1179', 'yelping_since': '2016-12-18 17:31:52'}, {'user_id': 'userid_324', 'yelping_since': '2016-10-10 22:09:08'}, {'user_id': 'userid_863', 'yelping_since': '2016-01-16 00:45:41'}, {'user_id': 'userid_100', 'yelping_since': '2016-08-18 11:39:42'}, {'user_id': 'userid_1333', 'yelping_since': '2016-12-07 14:57:41'}, {'user_id': 'userid_1636', 'yelping_since': '2016-02-14 23:51:28'}, {'user_id': 'userid_1850', 'yelping_since': '2016-07-22 19:26:01'}, {'user_id': 'userid_711', 'yelping_since': '2016-07-07 22:59:48'}, {'user_id': 'userid_729', 'yelping_since': '2016-02-06 00:41:18'}, {'user_id': 'userid_1505', 'yelping_since': '2016-07-14 00:26:46'}, {'user_id': 'userid_1315', 'yelping_since': '2016-03-07 02:47:32'}, {'user_id': 'userid_1708', 'yelping_since': '2016-03-06 20:06:53'}, {'user_id': 'userid_1661', 'yelping_since': '2016-06-13 00:48:17'}, {'user_id': 'userid_850', 'yelping_since': '2016-04-05 22:20:15'}, {'user_id': 'userid_1675', 'yelping_since': '2016-02-13 20:18:19'}, {'user_id': 'userid_227', 'yelping_since': '2016-01-16 01:12:00'}, {'user_id': 'userid_577', 'yelping_since': '2016-08-05 21:32:23'}, {'user_id': 'userid_257', 'yelping_since': '2016-10-19 21:58:32'}, {'user_id': 'userid_598', 'yelping_since': '2016-07-24 20:27:40'}, {'user_id': 'userid_847', 'yelping_since': '2016-08-04 20:28:55'}, {'user_id': 'userid_673', 'yelping_since': '2016-09-29 14:11:39'}, {'user_id': 'userid_1856', 'yelping_since': '2016-11-19 23:19:11'}, {'user_id': 'userid_384', 'yelping_since': '2016-04-21 20:00:19'}, {'user_id': 'userid_935', 'yelping_since': '2016-03-04 03:53:07'}, {'user_id': 'userid_210', 'yelping_since': '2016-06-24 03:16:47'}, {'user_id': 'userid_1101', 'yelping_since': '2016-06-13 19:58:37'}, {'user_id': 'userid_945', 'yelping_since': '2016-05-08 04:31:48'}, {'user_id': 'userid_842', 'yelping_since': '2016-02-21 19:02:44'}, {'user_id': 'userid_1351', 'yelping_since': '2016-03-30 02:56:55'}, {'user_id': 'userid_230', 'yelping_since': '2016-09-28 21:47:27'}, {'user_id': 'userid_593', 'yelping_since': '2016-11-18 05:33:16'}, {'user_id': 'userid_1431', 'yelping_since': '2016-01-06 23:48:07'}, {'user_id': 'userid_686', 'yelping_since': '2016-02-20 02:24:38'}, {'user_id': 'userid_527', 'yelping_since': '2016-06-26 04:19:08'}, {'user_id': 'userid_244', 'yelping_since': '2016-02-06 05:06:29'}, {'user_id': 'userid_393', 'yelping_since': '2016-08-16 18:42:51'}, {'user_id': 'userid_1178', 'yelping_since': '2016-05-05 18:04:24'}, {'user_id': 'userid_526', 'yelping_since': '2016-12-16 00:17:31'}, {'user_id': 'userid_90', 'yelping_since': '2016-07-14 00:52:49'}, {'user_id': 'userid_238', 'yelping_since': '2016-12-29 01:41:33'}, {'user_id': 'userid_1105', 'yelping_since': '2016-03-15 21:53:34'}], 'var_call_v8M9Bj1BjWd6wAKbnSvl0C5i': [{'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'name': 'Candy Barrel', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'name': 'Luminosity', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10', 'name': 'China Wok', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}]}

exec(code, env_args)
