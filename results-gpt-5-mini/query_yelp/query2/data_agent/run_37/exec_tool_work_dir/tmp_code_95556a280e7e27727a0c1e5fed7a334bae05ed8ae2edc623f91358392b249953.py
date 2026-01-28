code = """import json

# read the previous python result and SQL query result
res1 = var_call_agsU3CbR8QxGppT6M1YR71Gm
res2 = var_call_aTSorv4WRbmkp7Iy9uNLCO1S

# Build final answer
top_state = res1['top_state']
state_total_reviews = res1['total_reviews']
avg_rating = float(res2[0]['avg_rating']) if res2 and res2[0].get('avg_rating') else None

final = {
    'state_with_highest_reviews': top_state,
    'total_reviews_in_state': state_total_reviews,
    'average_rating_of_businesses_in_state': avg_rating
}

import json
print('__RESULT__:')
print(json.dumps(final))"""

env_args = {'var_call_Z1L2Sg4P44zDIAeOtkLCdnkt': ['checkin', 'business'], 'var_call_Ha2U7zlK7vg2YAje53HOygrd': ['review', 'tip', 'user'], 'var_call_9FXhoAkEgUlY3ILP84RrZKxg': 'file_storage/call_9FXhoAkEgUlY3ILP84RrZKxg.json', 'var_call_agsU3CbR8QxGppT6M1YR71Gm': {'top_state': 'MO', 'total_reviews': 2243, 'business_ref_count': 9, 'business_refs': ['businessref_47', 'businessref_64', 'businessref_10', 'businessref_24', 'businessref_30', 'businessref_96', 'businessref_11', 'businessref_4', 'businessref_46']}, 'var_call_aTSorv4WRbmkp7Iy9uNLCO1S': [{'avg_rating': '3.9061032863849765', 'review_count': '213'}]}

exec(code, env_args)
