code = """import json
import pandas as pd

df_bus = pd.DataFrame(var_call_XEYKcrKcQFPU99OHKDxEHP3Q)
df_rev = pd.DataFrame(var_call_6ZI8JqKF1otCQVd2zGCeqxVF)

# ensure numeric
df_rev['avg_rating'] = df_rev['avg_rating'].astype(float)

# merge
df = pd.merge(df_bus, df_rev, on='gmap_id', how='inner')

# filter >= 4.0
df_filtered = df[df['avg_rating'] >= 4.0].copy()

# prepare output: list of dicts with name and average_rating rounded to 2 decimals, sorted desc
output = (
    df_filtered[['name', 'avg_rating']]
    .assign(avg_rating=lambda x: x['avg_rating'].round(2))
    .sort_values('avg_rating', ascending=False)
    .to_dict(orient='records')
)

# convert to JSON string
result_json = json.dumps(output)

print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_TNvuNGUOAWKbYo2GylloVGl7': [], 'var_call_XEYKcrKcQFPU99OHKDxEHP3Q': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}], 'var_call_6ZI8JqKF1otCQVd2zGCeqxVF': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'num_reviews': '56'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'num_reviews': '15'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'num_reviews': '6'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875', 'num_reviews': '8'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'num_reviews': '1'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875', 'num_reviews': '8'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125', 'num_reviews': '8'}]}

exec(code, env_args)
