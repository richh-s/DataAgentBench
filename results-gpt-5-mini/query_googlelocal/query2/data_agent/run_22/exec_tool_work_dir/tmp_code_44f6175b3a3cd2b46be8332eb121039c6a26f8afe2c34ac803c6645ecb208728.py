code = """import pandas as pd
import json
# Load results from previous queries
df_business = pd.DataFrame(var_call_w2CRWUzp508dLVJW2NOhD514)
df_avg = pd.DataFrame(var_call_AzM1qH8V9xMc1y3AjPjLLbEr)
# Ensure types
if not df_avg.empty:
    df_avg['avg_rating'] = df_avg['avg_rating'].astype(float)
# Merge
df_merged = pd.merge(df_business, df_avg, on='gmap_id', how='inner')
# Filter for avg_rating >= 4.0
df_filtered = df_merged[df_merged['avg_rating'] >= 4.0].copy()
# Round ratings to 3 decimals for presentation
if not df_filtered.empty:
    df_filtered['avg_rating'] = df_filtered['avg_rating'].round(3)
# Sort by avg_rating descending
df_filtered = df_filtered.sort_values(by='avg_rating', ascending=False)
# Build result list
result = []
for _, row in df_filtered.iterrows():
    result.append({
        'gmap_id': row['gmap_id'],
        'name': row['name'],
        'avg_rating': float(row['avg_rating']) if not pd.isna(row['avg_rating']) else None
    })
# Print according to required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_jGRN9pPcAiQpxficpGQOfAxg': [], 'var_call_w2CRWUzp508dLVJW2NOhD514': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}], 'var_call_AzM1qH8V9xMc1y3AjPjLLbEr': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}]}

exec(code, env_args)
