code = """import pandas as pd
import json
# Data from previous tool calls
df_bus = pd.DataFrame(var_call_rQZo2XZZK3c6dDZCWF09MsWv)
df_rev = pd.DataFrame(var_call_RwPjGxcgShBfn6Z5tonvoU4J)
# Convert avg_rating to float
df_rev['avg_rating'] = df_rev['avg_rating'].astype(float)
# Merge
df_merged = pd.merge(df_bus, df_rev[['gmap_id','avg_rating','num_reviews']], on='gmap_id', how='inner')
# Filter for avg_rating >= 4.0
df_filtered = df_merged[df_merged['avg_rating'] >= 4.0].copy()
# Round ratings for presentation
df_filtered['avg_rating'] = df_filtered['avg_rating'].round(3)
# Prepare result list
result = df_filtered[['name','avg_rating']].sort_values('avg_rating', ascending=False).to_dict(orient='records')
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_MTzkmAiVqSlARm4TbuyHCUaT': [], 'var_call_rQZo2XZZK3c6dDZCWF09MsWv': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}], 'var_call_RwPjGxcgShBfn6Z5tonvoU4J': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'num_reviews': '56'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'num_reviews': '15'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'num_reviews': '6'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875', 'num_reviews': '8'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'num_reviews': '1'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875', 'num_reviews': '8'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125', 'num_reviews': '8'}]}

exec(code, env_args)
