code = """import json
import pandas as pd
import re

# Load data
with open(var_call_gbwHwSqbysbBryWZr9Ne041T, 'r') as f:
    businesses = json.load(f)
with open(var_call_jLB6pH4qk33x9BnnCCX5Ho4f, 'r') as f:
    reviews = json.load(f)

bdf = pd.DataFrame(businesses)
rdf = pd.DataFrame(reviews)

# Normalize
bdf['attributes'] = bdf.get('attributes', None)
bdf['description'] = bdf.get('description', '')

# Extract wifi
def parse_wifi(attr):
    if attr is None or attr == 'None':
        return None
    if isinstance(attr, dict):
        val = attr.get('WiFi') or attr.get('wifi')
        if val is None:
            return None
        s = str(val)
    else:
        s = str(attr)
    s_low = s.lower()
    for token in ['free','paid','no','none','yes']:
        if token in s_low:
            return token
    # try to find word after WiFi
    m = re.search(r"wifi[^\w]*(?:[:=\']*)\s*([a-zA-Z]+)", s, re.I)
    if m:
        return m.group(1).lower()
    return None

bdf['wifi_raw'] = bdf['attributes'].apply(parse_wifi)

# Determine offers wifi
bdf['offers_wifi'] = bdf['wifi_raw'].apply(lambda v: False if v is None or v in ['no','none'] else True)

# Extract state: find first two-letter uppercase token anywhere
def extract_state(desc):
    if not isinstance(desc, str):
        return None
    # find all 2-letter uppercase tokens
    found = re.findall(r"\b([A-Z]{2})\b", desc)
    if found:
        # verify it's a US state by length 2; we'll accept first
        return found[-1]  # choose last occurrence (state often near end)
    return None

bdf['state'] = bdf['description'].apply(extract_state)

# Filter wifi businesses with state
wifi_biz = bdf[(bdf['offers_wifi']) & (bdf['state'].notnull())].copy()

# Map business_id to business_ref
wifi_biz['business_ref'] = wifi_biz['business_id'].astype(str).str.replace('businessid_', 'businessref_')

# Prepare reviews df
if 'business_ref' in rdf.columns and 'rating' in rdf.columns:
    rdf2 = rdf[['business_ref','rating']].copy()
    rdf2['rating'] = pd.to_numeric(rdf2['rating'], errors='coerce')
else:
    rdf2 = pd.DataFrame(columns=['business_ref','rating'])

# Merge reviews for wifi businesses
merged = pd.merge(rdf2, wifi_biz[['business_ref','state']], on='business_ref', how='inner')

# Compute per-state distinct wifi business count and average rating across reviews
state_counts = wifi_biz.groupby('state')['business_id'].nunique().rename('wifi_business_count')
state_avg = merged.groupby('state')['rating'].mean().rename('average_rating')

summary = pd.concat([state_counts, state_avg], axis=1).reset_index()
summary['average_rating'] = summary['average_rating'].apply(lambda x: None if pd.isna(x) else float(round(float(x),3)))
summary['wifi_business_count'] = summary['wifi_business_count'].astype(int)

# Determine top state
if summary.empty:
    result = {'state': None, 'wifi_business_count': 0, 'average_rating': None}
else:
    maxc = summary['wifi_business_count'].max()
    cand = summary[summary['wifi_business_count']==maxc].copy()
    cand['avg_sort'] = cand['average_rating'].apply(lambda x: x if x is not None else -999)
    cand = cand.sort_values(by=['avg_sort','state'], ascending=[False, True])
    top = cand.iloc[0]
    result = {'state': top['state'], 'wifi_business_count': int(top['wifi_business_count']), 'average_rating': top['average_rating']}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_o67tVfb3ILfk4WUAiMTMgalH': ['checkin', 'business'], 'var_call_8mPFtwEhbfv4OhNqKH5qEJnN': ['review', 'tip', 'user'], 'var_call_gbwHwSqbysbBryWZr9Ne041T': 'file_storage/call_gbwHwSqbysbBryWZr9Ne041T.json', 'var_call_jLB6pH4qk33x9BnnCCX5Ho4f': 'file_storage/call_jLB6pH4qk33x9BnnCCX5Ho4f.json', 'var_call_A07fBOARjLBcYKJ7Nik9b73r': {'state': None, 'wifi_business_count': 0, 'average_rating': None}, 'var_call_VX3hHmjijjX4rZoOLHenNa7n': 'file_storage/call_VX3hHmjijjX4rZoOLHenNa7n.json', 'var_call_pisaPQu3vdeaij7m33wvnMam': {'total_businesses': 100, 'wifi_businesses': 22, 'businesses_with_state': 0, 'wifi_businesses_with_state': 0, 'state_counts_all_sample': {}, 'state_counts_wifi_sample': {}, 'examples_wifi': [{'business_id': 'businessid_64', 'wifi_raw': 'free', 'state': None, 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'business_id': 'businessid_54', 'wifi_raw': 'free', 'state': None, 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'business_id': 'businessid_91', 'wifi_raw': 'free', 'state': None, 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}, {'business_id': 'businessid_93', 'wifi_raw': 'free', 'state': None, 'description': 'Located at 914 Edwardsville Rd in Troy, IL, this vibrant spot offers a diverse menu featuring American (New) cuisine, along with a lively atmosphere perfect for nightlife, bars, restaurants, and sports bars.'}, {'business_id': 'businessid_26', 'wifi_raw': 'free', 'state': None, 'description': 'Located at 7003 Seminole Blvd in Seminole, FL, this establishment specializes in a variety of offerings, including Fast Food, Restaurants, Coffee & Tea, Food, and Burgers, making it a convenient stop for a quick meal or a refreshing beverage.'}, {'business_id': 'businessid_89', 'wifi_raw': 'free', 'state': None, 'description': 'Located at 540 Shoemaker Rd in King of Prussia, PA, this establishment offers a range of services including Dry Cleaning & Laundry, Laundromat, Local Services, and Laundry Services.'}, {'business_id': 'businessid_97', 'wifi_raw': 'free', 'state': None, 'description': 'Located at 560 Cottman Ave in Cheltenham, PA, this establishment specializes in Body Shops, Automotive services to meet all your vehicle repair needs.'}, {'business_id': 'businessid_67', 'wifi_raw': 'free', 'state': None, 'description': 'Located at 1501 W Chester Pike in Havertown, PA, this eatery specializes in Vietnamese, Soup, Restaurants, Noodles, offering a delightful array of flavorful dishes.'}, {'business_id': 'businessid_51', 'wifi_raw': 'free', 'state': None, 'description': 'Situated at 3109 N Ola Ave in Tampa, FL, this establishment offers a range of services in the hospitality sector, including Hotels & Travel, Hostels, Bed & Breakfast, Hotels, and Event Planning & Services.'}, {'business_id': 'businessid_6', 'wifi_raw': 'free', 'state': None, 'description': 'Located at 246 W 1st St in Reno, NV, this vibrant destination offers a delightful mix of Restaurants, Breakfast & Brunch, Bars, Wine Bars, Coffee & Tea, Food, Cafes, Sandwiches, and Nightlife, making it an ideal spot for any meal or occasion.'}, {'business_id': 'businessid_55', 'wifi_raw': 'free', 'state': None, 'description': 'Located at 1003 4th St N in St. Petersburg, FL, this delightful spot offers a variety of treats including Ice Cream & Frozen Yogurt, Shaved Ice, Food, and Desserts.'}, {'business_id': 'businessid_77', 'wifi_raw': 'free', 'state': None, 'description': 'Located at 900 Packer Ave in Philadelphia, PA, this establishment offers a range of services in Hotels & Travel, Venues & Event Spaces, Hotels, and Event Planning & Services, making it an ideal choice for travelers and event organizers alike.'}, {'business_id': 'businessid_86', 'wifi_raw': 'free', 'state': None, 'description': 'Located at 705 East Passyunk Ave in Philadelphia, PA, this vibrant eatery offers a diverse menu featuring American (New), Restaurants, American (Traditional), Asian Fusion, Noodles, Dim Sum, Fast Food, Chinese, catering to a variety of tastes and preferences.'}, {'business_id': 'businessid_40', 'wifi_raw': 'free', 'state': None, 'description': 'Located at 4457 Main St in Philadelphia, PA, this establishment specializes in Venues & Event Spaces, Event Planning & Services, making it an ideal choice for hosting memorable gatherings and celebrations.'}, {'business_id': 'businessid_44', 'wifi_raw': 'free', 'state': None, 'description': 'Located at 2424 E York St in Philadelphia, PA, this vibrant establishment offers a delightful array of options, including Restaurants, Diners, Breakfast & Brunch, American (New), American (Traditional), Burgers, making it a perfect spot for any meal of the day.'}, {'business_id': 'businessid_43', 'wifi_raw': 'free', 'state': None, 'description': 'Located at 11425 Allisonville Road in Fishers, IN, this vibrant eatery offers a delightful menu featuring Tex-Mex, Tacos, Restaurants, Breakfast & Brunch, Sandwiches, Mexican, Fast Food, perfect for satisfying any craving at any time of day.'}, {'business_id': 'businessid_20', 'wifi_raw': 'free', 'state': None, 'description': 'Located at 9040 State Road 54 in Trinity, FL, this establishment offers a diverse array of options, including Restaurants, American (New), Caterers, Fast Food, Chicken Shop, Event Planning & Services, and American (Traditional).'}, {'business_id': 'businessid_25', 'wifi_raw': 'free', 'state': None, 'description': 'Located at 5608 W Fairview Ave in Boise, ID, this charming establishment offers a delightful array of options in the categories of Food, Restaurants, Sandwiches, Breakfast & Brunch, and Bakeries.'}, {'business_id': 'businessid_82', 'wifi_raw': 'free', 'state': None, 'description': 'Located at 1620 South St in Philadelphia, PA, this vibrant establishment offers a delightful array of options, perfect for any occasion, including Restaurants, Coffee & Tea, Food, Breakfast & Brunch, Event Planning & Services, American (Traditional), and Caterers.'}, {'business_id': 'businessid_12', 'wifi_raw': 'paid', 'state': None, 'description': 'Located at 7704 Calgary Trail S in Edmonton, AB, this vibrant spot offers a diverse experience with options for Pubs, Restaurants, Nightlife, Burgers, Seafood, and Bars.'}]}, 'var_call_xlPCzB9nlgGQ2tm2l77u3Ltq': 'file_storage/call_xlPCzB9nlgGQ2tm2l77u3Ltq.json'}

exec(code, env_args)
