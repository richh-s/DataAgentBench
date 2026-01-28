code = """import json
import pandas as pd

# Load query results from storage variables
bus = pd.DataFrame(var_call_UMYrkNVanhkvoE7FBIdFQpdk)
rev = pd.DataFrame(var_call_gwm0DKKgXTsIXNfuXqr1CJ36)

# Convert types
rev['avg_rating'] = rev['avg_rating'].astype(float)
rev['review_count'] = rev['review_count'].astype(int)

# Merge to get business names
merged = rev.merge(bus, on='gmap_id', how='left')

# Prepare output list
out = []
for _, row in merged.sort_values('avg_rating', ascending=False).iterrows():
    out.append({
        'name': row['name'],
        'gmap_id': row['gmap_id'],
        'avg_rating': round(float(row['avg_rating']), 2),
        'review_count': int(row['review_count'])
    })

result = json.dumps(out)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_v9iHM6tGz1M8NMUpojX49TVd': [], 'var_call_UMYrkNVanhkvoE7FBIdFQpdk': [{'name': 'Angel-A Massage', 'gmap_id': 'gmap_22', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'name': 'Elite Massage', 'gmap_id': 'gmap_25', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'gmap_id': 'gmap_33', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'name': 'SUSY massage', 'gmap_id': 'gmap_24', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'name': 'Aurora Massage', 'gmap_id': 'gmap_20', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'name': 'Orient Massage', 'gmap_id': 'gmap_21', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'name': 'Good Massage', 'gmap_id': 'gmap_28', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}], 'var_call_gwm0DKKgXTsIXNfuXqr1CJ36': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'review_count': '56'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'review_count': '6'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'review_count': '1'}]}

exec(code, env_args)
