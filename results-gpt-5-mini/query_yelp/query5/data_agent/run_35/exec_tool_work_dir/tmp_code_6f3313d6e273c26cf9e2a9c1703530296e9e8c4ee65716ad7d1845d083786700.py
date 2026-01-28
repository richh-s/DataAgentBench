code = """import pandas as pd
import re
import json

biz = pd.DataFrame(var_call_jjxnGGyCQnXjuMrwLXW3kvPZ)
rev = pd.DataFrame(var_call_sW5qqzmvIHnXhSduhNGngkCq)

# create business_ref
biz['business_ref'] = biz['business_id'].str.replace('businessid_', 'businessref_')

# function to extract state
def extract_state(desc):
    if not isinstance(desc, str):
        return None
    # try patterns
    patterns = [r'in [^,]+,\s*([A-Z]{2})', r',\s*([A-Z]{2})\b']
    for p in patterns:
        m = re.search(p, desc)
        if m:
            return m.group(1)
    return None

biz['state'] = biz['description'].apply(extract_state)

# count by state
counts = biz['state'].value_counts(dropna=True)
if counts.empty:
    result = {"error": "No state information found for WiFi businesses"}
else:
    max_count = int(counts.max())
    top_states = counts[counts == max_count].index.tolist()

    # compute average rating for businesses in top_states
    biz_top = biz[biz['state'].isin(top_states)]
    refs = set(biz_top['business_ref'].tolist())
    rev['rating'] = pd.to_numeric(rev['rating'], errors='coerce')
    rev_top = rev[rev['business_ref'].isin(refs)]
    avg_rating = rev_top['rating'].mean()
    avg_rating = round(float(avg_rating), 2) if pd.notna(avg_rating) else None

    if len(top_states) == 1:
        result = {"state": top_states[0], "business_count": max_count, "average_rating": avg_rating}
    else:
        result = {"states": top_states, "business_count": max_count, "average_rating": avg_rating}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_SnzM0B9G4ypBivLR8CSEDjZL': ['checkin', 'business'], 'var_call_n8TFzYQGqCIZIDxQsSy3kEQo': ['review', 'tip', 'user'], 'var_call_fpegks5FN2CfVXGIsAxg6Ib1': 'file_storage/call_fpegks5FN2CfVXGIsAxg6Ib1.json', 'var_call_jjxnGGyCQnXjuMrwLXW3kvPZ': [{'business_id': 'businessid_64', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'business_id': 'businessid_54', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'business_id': 'businessid_91', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}, {'business_id': 'businessid_93', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 914 Edwardsville Rd in Troy, IL, this vibrant spot offers a diverse menu featuring American (New) cuisine, along with a lively atmosphere perfect for nightlife, bars, restaurants, and sports bars.'}, {'business_id': 'businessid_26', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 7003 Seminole Blvd in Seminole, FL, this establishment specializes in a variety of offerings, including Fast Food, Restaurants, Coffee & Tea, Food, and Burgers, making it a convenient stop for a quick meal or a refreshing beverage.'}], 'var_call_sW5qqzmvIHnXhSduhNGngkCq': [{'business_ref': 'businessref_26', 'rating': '1'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_64', 'rating': '5'}, {'business_ref': 'businessref_93', 'rating': '1'}, {'business_ref': 'businessref_26', 'rating': '1'}, {'business_ref': 'businessref_26', 'rating': '1'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_54', 'rating': '4'}, {'business_ref': 'businessref_26', 'rating': '1'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_26', 'rating': '2'}, {'business_ref': 'businessref_26', 'rating': '2'}, {'business_ref': 'businessref_93', 'rating': '4'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_64', 'rating': '3'}, {'business_ref': 'businessref_26', 'rating': '2'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_26', 'rating': '1'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_26', 'rating': '5'}, {'business_ref': 'businessref_93', 'rating': '1'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_26', 'rating': '1'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_54', 'rating': '4'}, {'business_ref': 'businessref_54', 'rating': '4'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_91', 'rating': '4'}, {'business_ref': 'businessref_26', 'rating': '2'}, {'business_ref': 'businessref_26', 'rating': '1'}, {'business_ref': 'businessref_26', 'rating': '5'}, {'business_ref': 'businessref_54', 'rating': '4'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_26', 'rating': '3'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_93', 'rating': '3'}, {'business_ref': 'businessref_93', 'rating': '4'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_26', 'rating': '1'}, {'business_ref': 'businessref_54', 'rating': '3'}, {'business_ref': 'businessref_26', 'rating': '1'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_26', 'rating': '1'}, {'business_ref': 'businessref_54', 'rating': '4'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_64', 'rating': '5'}, {'business_ref': 'businessref_26', 'rating': '1'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_54', 'rating': '5'}, {'business_ref': 'businessref_91', 'rating': '3'}, {'business_ref': 'businessref_64', 'rating': '3'}, {'business_ref': 'businessref_26', 'rating': '1'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_26', 'rating': '1'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_91', 'rating': '4'}, {'business_ref': 'businessref_64', 'rating': '4'}, {'business_ref': 'businessref_54', 'rating': '5'}, {'business_ref': 'businessref_26', 'rating': '4'}, {'business_ref': 'businessref_26', 'rating': '1'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_54', 'rating': '1'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_93', 'rating': '3'}, {'business_ref': 'businessref_93', 'rating': '4'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_64', 'rating': '1'}, {'business_ref': 'businessref_26', 'rating': '1'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_26', 'rating': '1'}, {'business_ref': 'businessref_91', 'rating': '5'}, {'business_ref': 'businessref_64', 'rating': '5'}, {'business_ref': 'businessref_54', 'rating': '1'}], 'var_call_2gpVg64TclBlygWXcEAtwLPW': {'error': 'No businesses with WiFi found or no state information available.'}, 'var_call_nwmFJLrIGo7TPpesXgqqmevB': {'row_count': 5, 'columns': ['business_id', 'attributes', 'description'], 'records': [{'business_id': 'businessid_64', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'business_id': 'businessid_54', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'business_id': 'businessid_91', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}, {'business_id': 'businessid_93', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 914 Edwardsville Rd in Troy, IL, this vibrant spot offers a diverse menu featuring American (New) cuisine, along with a lively atmosphere perfect for nightlife, bars, restaurants, and sports bars.'}, {'business_id': 'businessid_26', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 7003 Seminole Blvd in Seminole, FL, this establishment specializes in a variety of offerings, including Fast Food, Restaurants, Coffee & Tea, Food, and Burgers, making it a convenient stop for a quick meal or a refreshing beverage.'}]}}

exec(code, env_args)
