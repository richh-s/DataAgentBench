code = """import json

# load previous results
res_top = var_call_cQYkfJnqLug7XBt2LBMp9klO
res_avg = var_call_XbxpnAnVpCSBilIzbsWTalQo

output = {
    'state_with_most_reviews': res_top['top_state'],
    'total_reviews_in_state': res_top['total_reviews'],
    'average_rating_of_businesses_in_state': float(res_avg[0]['avg_rating']),
    'num_reviews_used_for_avg': int(res_avg[0]['review_count'])
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_R4VAWuBKEM1yL68n1G0ZL6EA': ['checkin', 'business'], 'var_call_Xd66fok67Dl8Bz52C6ZMt5qS': ['review', 'tip', 'user'], 'var_call_CvKwb8XslONx1lfsFPefIFEa': 'file_storage/call_CvKwb8XslONx1lfsFPefIFEa.json', 'var_call_cQYkfJnqLug7XBt2LBMp9klO': {'top_state': 'MO', 'total_reviews': 2243, 'business_refs': ['businessref_47', 'businessref_64', 'businessref_10', 'businessref_24', 'businessref_30', 'businessref_96', 'businessref_11', 'businessref_4', 'businessref_46']}, 'var_call_XbxpnAnVpCSBilIzbsWTalQo': [{'avg_rating': '3.9061032863849765', 'review_count': '213'}]}

exec(code, env_args)
