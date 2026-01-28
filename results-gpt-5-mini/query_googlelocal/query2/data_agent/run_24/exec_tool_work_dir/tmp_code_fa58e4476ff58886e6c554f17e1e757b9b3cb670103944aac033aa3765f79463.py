code = """import json
import pandas as pd

# Load previous tool results
b = var_call_9UHwOtOk70hEPY6KXDGMaKGu
r = var_call_WHudxh4zZ89jBAFnyuONuPma

# Create DataFrames
dfb = pd.DataFrame(b)
dfr = pd.DataFrame(r)

# Convert avg_rating to float
if 'avg_rating' in dfr.columns:
    dfr['avg_rating'] = dfr['avg_rating'].astype(float)

# Merge on gmap_id
merged = pd.merge(dfb, dfr, on='gmap_id')

# Filter for average rating >= 4.0
filtered = merged[merged['avg_rating'] >= 4.0].copy()

# Prepare output list with rounded ratings
out = []
for _, row in filtered.iterrows():
    out.append({
        'name': row['name'],
        'avg_rating': round(float(row['avg_rating']), 2)
    })

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_M3NZR4DrX8mpIiRjqMsxJKhJ': [], 'var_call_9UHwOtOk70hEPY6KXDGMaKGu': [{'name': 'Angel-A Massage', 'gmap_id': 'gmap_22', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'name': 'Elite Massage', 'gmap_id': 'gmap_25', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'gmap_id': 'gmap_33', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'name': 'SUSY massage', 'gmap_id': 'gmap_24', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'name': 'Aurora Massage', 'gmap_id': 'gmap_20', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'name': 'Orient Massage', 'gmap_id': 'gmap_21', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'name': 'Good Massage', 'gmap_id': 'gmap_28', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}], 'var_call_WHudxh4zZ89jBAFnyuONuPma': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'cnt': '56'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'cnt': '15'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'cnt': '6'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875', 'cnt': '8'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'cnt': '1'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875', 'cnt': '8'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125', 'cnt': '8'}]}

exec(code, env_args)
