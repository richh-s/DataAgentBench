code = """import json, re, pandas as pd

with open(var_call_f7fdarCrZpeM5z65nIxcoNCC, 'r') as f:
    business_data = json.load(f)
with open(var_call_CG3ZySBTjUiAP0WUxrLqqKzy, 'r') as f:
    review_data = json.load(f)

bdf = pd.DataFrame(business_data)
rdf = pd.DataFrame(review_data)

# Extract state abbreviation from description using pattern ' City, ST,' or ' in City, ST,' etc.
state_pattern = re.compile(r'\b([A-Z][a-zA-Z]+),\s*([A-Z]{2})\b')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = state_pattern.search(desc)
    if m:
        return m.group(2)
    # Fallback: look for ', ST' directly
    m2 = re.search(r',\s*([A-Z]{2})\b', desc)
    if m2:
        return m2.group(1)
    return None

bdf['state'] = bdf['description'].apply(extract_state)

b_state = bdf[['business_id', 'state']].dropna()

b_state['key'] = b_state['business_id'].str.replace('businessid_', '', regex=False)
rdf['key'] = rdf['business_ref'].str.replace('businessref_', '', regex=False)

merged = rdf.merge(b_state[['key', 'state']], on='key', how='inner')

if merged.empty:
    result = {'error': 'No reviews could be matched to businesses with identifiable states.'}
else:
    merged['rating'] = pd.to_numeric(merged['rating'])
    agg = merged.groupby('state').agg(review_count=('rating', 'size'), avg_rating=('rating', 'mean')).reset_index()
    agg = agg.sort_values('review_count', ascending=False)
    row = agg.iloc[0]
    result = {
        'state': row['state'],
        'review_count': int(row['review_count']),
        'average_rating': round(float(row['avg_rating']), 3)
    }

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_f7fdarCrZpeM5z65nIxcoNCC': 'file_storage/call_f7fdarCrZpeM5z65nIxcoNCC.json', 'var_call_CG3ZySBTjUiAP0WUxrLqqKzy': 'file_storage/call_CG3ZySBTjUiAP0WUxrLqqKzy.json', 'var_call_y1OLMe9EKGsyzMwgOswAkD2O': {'sample_descriptions': ['Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.', 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.', 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.', 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.', 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.', 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.', 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.', 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.', 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.', 'Located at 41 Haddon Ave in Collingswood, NJ, this versatile establishment offers a range of services including Wedding Planning, Flowers & Gifts, Event Planning & Services, Financial Services, Shopping, and Florists.', "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'.", 'Located at 1218 Millennium Pkwy in Brandon, FL, this facility provides essential services in the categories of Medical Centers, Health & Medical.', 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.', 'This Philadelphia, PA location offers a range of services including Hotels & Travel, Taxis, Transportation, Local Services, and Automotive to meet all your travel and transportation needs.', 'Located at 4403 Chestnut St in Philadelphia, PA, this vibrant spot offers a delightful mix of Food, Bubble Tea, Restaurants, Sandwiches, Vietnamese, Cafes, perfect for a casual meal or a refreshing drink.', 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.', 'Located at 13002 Seminole Blvd, Ste 10-11 in Largo, FL, this business specializes in Optometrists, Health & Medical, Eyewear & Opticians, Ophthalmologists, Doctors, Shopping, offering a range of eye care services and products.', 'Located at 914 Edwardsville Rd in Troy, IL, this vibrant spot offers a diverse menu featuring American (New) cuisine, along with a lively atmosphere perfect for nightlife, bars, restaurants, and sports bars.', 'Located in Pennsauken, NJ, this business specializes in Home Services, Pool & Hot Tub Service, providing expert care for all your residential maintenance needs.', 'Located at 4663 Maryland Ave in Saint Louis, MO, this delightful spot offers a tempting selection of treats in the categories of Food, Ice Cream & Frozen Yogurt.']}}

exec(code, env_args)
