code = """import json, re, pandas as pd

def load_tool_result(var):
    if isinstance(var, str):
        with open(var, 'r') as f:
            return json.load(f)
    return var

biz = load_tool_result(var_call_nM334UVtoNFxYyzh0CYyTTDV)
rev = load_tool_result(var_call_RIoSDHu7GDyB3qSNOy3DhfNp)

biz_df = pd.DataFrame(biz)
rev_df = pd.DataFrame(rev)

state_pat = re.compile(r",\s*([A-Z]{2})\b")

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = state_pat.search(desc)
    return m.group(1) if m else None

biz_df['state'] = biz_df['description'].apply(extract_state)

biz_df['key'] = biz_df['business_id'].astype(str).str.replace('businessid_', '', regex=False)
biz_df['review_count'] = pd.to_numeric(biz_df['review_count'], errors='coerce')

state_review_totals = biz_df.dropna(subset=['state','review_count']).groupby('state')['review_count'].sum().sort_values(ascending=False)

if state_review_totals.empty:
    out = {'error':'Could not parse any state codes from business.description.'}
else:
    max_state = state_review_totals.index[0]

    rev_df['key'] = rev_df['business_ref'].astype(str).str.replace('businessref_', '', regex=False)
    rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')
    rev_state = rev_df.merge(biz_df[['key','state']], on='key', how='inner').dropna(subset=['rating'])
    biz_avg = rev_state.groupby(['state','key'])['rating'].mean().reset_index(name='biz_avg_rating')
    state_biz_avg = biz_avg[biz_avg['state']==max_state]['biz_avg_rating'].mean()

    out = {
        'state_with_highest_total_reviews': max_state,
        'total_reviews_in_state': int(state_review_totals.iloc[0]),
        'average_business_rating_in_state': None if pd.isna(state_biz_avg) else float(state_biz_avg)
    }

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_nM334UVtoNFxYyzh0CYyTTDV': 'file_storage/call_nM334UVtoNFxYyzh0CYyTTDV.json', 'var_call_RIoSDHu7GDyB3qSNOy3DhfNp': 'file_storage/call_RIoSDHu7GDyB3qSNOy3DhfNp.json', 'var_call_8cxpozZA91uAji1pvybuGpzM': {'error': 'No reviews could be matched to a parsed state from business descriptions.'}, 'var_call_QWGNztc6DPY1HAd0Wkxdw1BE': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'name': 'Candy Barrel', 'review_count': '7', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'name': 'Luminosity', 'review_count': '39', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64', 'name': 'Nail Care Salon', 'review_count': '6', 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52', 'name': 'Architectural Antiques of Indianapolis', 'review_count': '6', 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.'}, {'_id': '6859a000fe8b31cd7362e2b4', 'business_id': 'businessid_29', 'name': "Aster's Floral Shop", 'review_count': '25', 'description': 'Located at 41 Haddon Ave in Collingswood, NJ, this versatile establishment offers a range of services including Wedding Planning, Flowers & Gifts, Event Planning & Services, Financial Services, Shopping, and Florists.'}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10', 'name': 'China Wok', 'review_count': '20', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}, {'_id': '6859a000fe8b31cd7362e2b6', 'business_id': 'businessid_61', 'name': 'Brandon Family Medical Care', 'review_count': '17', 'description': 'Located at 1218 Millennium Pkwy in Brandon, FL, this facility provides essential services in the categories of Medical Centers, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2b7', 'business_id': 'businessid_54', 'name': '7-Eleven', 'review_count': '10', 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'_id': '6859a000fe8b31cd7362e2b8', 'business_id': 'businessid_8', 'name': 'Uber', 'review_count': '218', 'description': 'This Philadelphia, PA location offers a range of services including Hotels & Travel, Taxis, Transportation, Local Services, and Automotive to meet all your travel and transportation needs.'}, {'_id': '6859a000fe8b31cd7362e2b9', 'business_id': 'businessid_59', 'name': 'Chestnut St. Cafe', 'review_count': '34', 'description': 'Located at 4403 Chestnut St in Philadelphia, PA, this vibrant spot offers a delightful mix of Food, Bubble Tea, Restaurants, Sandwiches, Vietnamese, Cafes, perfect for a casual meal or a refreshing drink.'}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91', 'name': 'Cafe Porche and snowbar', 'review_count': '172', 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}, {'_id': '6859a000fe8b31cd7362e2bb', 'business_id': 'businessid_83', 'name': 'Eyeglass World', 'review_count': '6', 'description': 'Located at 13002 Seminole Blvd, Ste 10-11 in Largo, FL, this business specializes in Optometrists, Health & Medical, Eyewear & Opticians, Ophthalmologists, Doctors, Shopping, offering a range of eye care services and products.'}, {'_id': '6859a000fe8b31cd7362e2bc', 'business_id': 'businessid_93', 'name': "Callahan's Corner", 'review_count': '10', 'description': 'Located at 914 Edwardsville Rd in Troy, IL, this vibrant spot offers a diverse menu featuring American (New) cuisine, along with a lively atmosphere perfect for nightlife, bars, restaurants, and sports bars.'}, {'_id': '6859a000fe8b31cd7362e2bd', 'business_id': 'businessid_1', 'name': 'Spa Guy Dave', 'review_count': '6', 'description': 'Located in Pennsauken, NJ, this business specializes in Home Services, Pool & Hot Tub Service, providing expert care for all your residential maintenance needs.'}, {'_id': '6859a000fe8b31cd7362e2be', 'business_id': 'businessid_24', 'name': 'FroYo Frozen Yogurt', 'review_count': '43', 'description': 'Located at 4663 Maryland Ave in Saint Louis, MO, this delightful spot offers a tempting selection of treats in the categories of Food, Ice Cream & Frozen Yogurt.'}]}

exec(code, env_args)
