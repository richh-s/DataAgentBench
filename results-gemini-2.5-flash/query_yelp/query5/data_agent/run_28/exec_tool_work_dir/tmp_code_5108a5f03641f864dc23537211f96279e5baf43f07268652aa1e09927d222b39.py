code = """import pandas as pd
import json

business_wifi_data = locals()['var_function-call-6077624179990755452']
review_ratings_data = locals()['var_function-call-15607614723740326743']

df_wifi = pd.DataFrame(business_wifi_data)
df_ratings = pd.DataFrame(review_ratings_data)

df_merged = pd.merge(df_wifi, df_ratings, left_on='business_id', right_on='business_ref', how='inner')

# Convert avg_rating to numeric
df_merged['avg_rating'] = pd.to_numeric(df_merged['avg_rating'])

# Group by state and count businesses and average ratings
state_summary = df_merged.groupby('state').agg(
    num_businesses=('business_id', 'count'),
    total_rating=('avg_rating', 'sum')
).reset_index()

# Find the state with the highest number of businesses
highest_businesses_state = state_summary.loc[state_summary['num_businesses'].idxmax()]

# Calculate the average rating for that state
average_rating_for_highest_state = highest_businesses_state['total_rating'] / highest_businesses_state['num_businesses']

result_dict = {
    "state": highest_businesses_state['state'],
    "num_businesses": int(highest_businesses_state['num_businesses']),
    "average_rating": round(float(average_rating_for_highest_state), 2)
}

print('__RESULT__:')
print(json.dumps(result_dict))"""

env_args = {'var_function-call-17528142431518494084': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'WiFi': "u'no'"}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'attributes': {'WiFi': "u'no'"}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'_id': '6859a000fe8b31cd7362e2b7', 'business_id': 'businessid_54', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}], 'var_function-call-6077624179990755452': [{'business_id': 'businessref_64', 'state': 'MO'}, {'business_id': 'businessref_54', 'state': 'FL'}, {'business_id': 'businessref_91', 'state': 'LA'}], 'var_function-call-15607614723740326743': [{'business_ref': 'businessref_91', 'avg_rating': '4.911111111111111'}, {'business_ref': 'businessref_54', 'avg_rating': '3.5'}, {'business_ref': 'businessref_64', 'avg_rating': '3.7142857142857144'}]}

exec(code, env_args)
