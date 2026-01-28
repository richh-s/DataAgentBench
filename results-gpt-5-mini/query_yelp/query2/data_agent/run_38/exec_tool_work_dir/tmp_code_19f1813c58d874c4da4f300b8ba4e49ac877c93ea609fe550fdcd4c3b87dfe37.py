code = """import json
import re
import pandas as pd

# Load data from storage-provided file paths
with open(var_call_hnbS2r0B157HVxPIyR2iaOso, 'r') as f:
    businesses = json.load(f)
with open(var_call_PRVB85tOGkVHNnREEVIIlOSY, 'r') as f:
    reviews = json.load(f)

# Create DataFrames
df_b = pd.DataFrame(businesses)
df_r = pd.DataFrame(reviews)

# Extract state from description
state_re = re.compile(r',\s*([A-Z]{2})(?:[,\.\s]|$)')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = state_re.search(desc)
    if m:
        return m.group(1)
    # fallback: any two-letter uppercase token
    m2 = re.search(r"\b([A-Z]{2})\b", desc)
    if m2:
        return m2.group(1)
    return None

# Apply extraction
if 'description' in df_b.columns:
    df_b['state'] = df_b['description'].apply(extract_state)
else:
    df_b['state'] = None

# Map businessid_X -> businessref_X
def to_businessref(bid):
    if not isinstance(bid, str):
        return None
    parts = bid.split('_', 1)
    if len(parts) == 2:
        return 'businessref_' + parts[1]
    return 'businessref_' + bid

if 'business_id' in df_b.columns:
    df_b['business_ref'] = df_b['business_id'].apply(to_businessref)
else:
    df_b['business_ref'] = None

mapping = dict(zip(df_b['business_ref'], df_b['state']))

# Map states onto reviews
if 'business_ref' in df_r.columns:
    df_r['state'] = df_r['business_ref'].map(mapping)
else:
    df_r['state'] = None

# Ensure rating numeric
if 'rating' in df_r.columns:
    df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
else:
    df_r['rating'] = None

# Drop reviews without state or rating
df_r2 = df_r.dropna(subset=['state', 'rating'])

# Group by state
grp = df_r2.groupby('state').agg(review_count=('rating', 'size'), average_rating=('rating', 'mean')).reset_index()

if grp.empty:
    result = {"state": None, "review_count": 0, "average_rating": None}
else:
    top = grp.loc[grp['review_count'].idxmax()]
    result = {"state": str(top['state']), "review_count": int(top['review_count']), "average_rating": float(top['average_rating'])}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_yxoka8JgQv9OVal98LwLfu4o': ['business', 'checkin'], 'var_call_QOxPKLOpS49F6CI8JjFushn6': ['review', 'tip', 'user'], 'var_call_FzaEeHzXOkAwyc0FbONSMUl7': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'name': 'Candy Barrel', 'review_count': '7', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'name': 'Luminosity', 'review_count': '39', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64', 'name': 'Nail Care Salon', 'review_count': '6', 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52', 'name': 'Architectural Antiques of Indianapolis', 'review_count': '6', 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.'}, {'_id': '6859a000fe8b31cd7362e2b4', 'business_id': 'businessid_29', 'name': "Aster's Floral Shop", 'review_count': '25', 'description': 'Located at 41 Haddon Ave in Collingswood, NJ, this versatile establishment offers a range of services including Wedding Planning, Flowers & Gifts, Event Planning & Services, Financial Services, Shopping, and Florists.'}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10', 'name': 'China Wok', 'review_count': '20', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}, {'_id': '6859a000fe8b31cd7362e2b6', 'business_id': 'businessid_61', 'name': 'Brandon Family Medical Care', 'review_count': '17', 'description': 'Located at 1218 Millennium Pkwy in Brandon, FL, this facility provides essential services in the categories of Medical Centers, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2b7', 'business_id': 'businessid_54', 'name': '7-Eleven', 'review_count': '10', 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'_id': '6859a000fe8b31cd7362e2b8', 'business_id': 'businessid_8', 'name': 'Uber', 'review_count': '218', 'description': 'This Philadelphia, PA location offers a range of services including Hotels & Travel, Taxis, Transportation, Local Services, and Automotive to meet all your travel and transportation needs.'}, {'_id': '6859a000fe8b31cd7362e2b9', 'business_id': 'businessid_59', 'name': 'Chestnut St. Cafe', 'review_count': '34', 'description': 'Located at 4403 Chestnut St in Philadelphia, PA, this vibrant spot offers a delightful mix of Food, Bubble Tea, Restaurants, Sandwiches, Vietnamese, Cafes, perfect for a casual meal or a refreshing drink.'}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91', 'name': 'Cafe Porche and snowbar', 'review_count': '172', 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}, {'_id': '6859a000fe8b31cd7362e2bb', 'business_id': 'businessid_83', 'name': 'Eyeglass World', 'review_count': '6', 'description': 'Located at 13002 Seminole Blvd, Ste 10-11 in Largo, FL, this business specializes in Optometrists, Health & Medical, Eyewear & Opticians, Ophthalmologists, Doctors, Shopping, offering a range of eye care services and products.'}, {'_id': '6859a000fe8b31cd7362e2bc', 'business_id': 'businessid_93', 'name': "Callahan's Corner", 'review_count': '10', 'description': 'Located at 914 Edwardsville Rd in Troy, IL, this vibrant spot offers a diverse menu featuring American (New) cuisine, along with a lively atmosphere perfect for nightlife, bars, restaurants, and sports bars.'}, {'_id': '6859a000fe8b31cd7362e2bd', 'business_id': 'businessid_1', 'name': 'Spa Guy Dave', 'review_count': '6', 'description': 'Located in Pennsauken, NJ, this business specializes in Home Services, Pool & Hot Tub Service, providing expert care for all your residential maintenance needs.'}, {'_id': '6859a000fe8b31cd7362e2be', 'business_id': 'businessid_24', 'name': 'FroYo Frozen Yogurt', 'review_count': '43', 'description': 'Located at 4663 Maryland Ave in Saint Louis, MO, this delightful spot offers a tempting selection of treats in the categories of Food, Ice Cream & Frozen Yogurt.'}], 'var_call_hnbS2r0B157HVxPIyR2iaOso': 'file_storage/call_hnbS2r0B157HVxPIyR2iaOso.json', 'var_call_PRVB85tOGkVHNnREEVIIlOSY': 'file_storage/call_PRVB85tOGkVHNnREEVIIlOSY.json'}

exec(code, env_args)
