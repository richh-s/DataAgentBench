code = """import json
import pandas as pd
# Load variables from previous tool calls
biz = var_call_RSaYuNmtr5bkU3AYna1eZasG
ratings = var_call_53LHBbcyEXBDBkk09WwSVVH3
# Create DataFrames
df_biz = pd.DataFrame(biz)
df_r = pd.DataFrame(ratings)
# Convert numeric fields
if not df_r.empty:
    df_r['avg_rating'] = pd.to_numeric(df_r['avg_rating'])
    df_r['review_count'] = pd.to_numeric(df_r['review_count'])
# Merge
df_merged = pd.merge(df_r, df_biz, on='gmap_id', how='left')
# Prepare output list
output = []
for _, row in df_merged.iterrows():
    entry = {
        'gmap_id': row['gmap_id'],
        'name': row.get('name') if pd.notna(row.get('name')) else None,
        'avg_rating': round(float(row['avg_rating']), 2) if pd.notna(row['avg_rating']) else None,
        'review_count': int(row['review_count']) if pd.notna(row['review_count']) else None
    }
    output.append(entry)
# Sort by avg_rating desc
output = sorted(output, key=lambda x: (-x['avg_rating'] if x['avg_rating'] is not None else 0, -x['review_count'] if x['review_count'] is not None else 0))
result = json.dumps(output)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_GTidhfNxi79THKO3p2PS6sus': [], 'var_call_RSaYuNmtr5bkU3AYna1eZasG': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}], 'var_call_53LHBbcyEXBDBkk09WwSVVH3': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'review_count': '56'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'review_count': '6'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'review_count': '1'}]}

exec(code, env_args)
