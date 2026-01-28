code = """import json

# Get the ratings data
ratings_data = locals()['var_functions.query_db:12']

# Calculate average rating
ratings = [int(item['rating']) for item in ratings_data]
average_rating = sum(ratings) / len(ratings)

result = {
    'average_rating': round(average_rating, 2),
    'total_reviews': len(ratings),
    'total_businesses': 3
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['business', 'checkin'], 'var_functions.query_db:2': [], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:10': {'business_ids': ['businessid_52', 'businessid_84', 'businessid_76'], 'business_refs': ['businessref_52', 'businessref_84', 'businessref_76'], 'count': 3}, 'var_functions.query_db:12': [{'business_ref': 'businessref_84', 'rating': '5'}, {'business_ref': 'businessref_84', 'rating': '5'}, {'business_ref': 'businessref_52', 'rating': '4'}, {'business_ref': 'businessref_52', 'rating': '5'}, {'business_ref': 'businessref_76', 'rating': '4'}, {'business_ref': 'businessref_76', 'rating': '3'}, {'business_ref': 'businessref_52', 'rating': '2'}, {'business_ref': 'businessref_52', 'rating': '5'}, {'business_ref': 'businessref_76', 'rating': '3'}, {'business_ref': 'businessref_84', 'rating': '5'}, {'business_ref': 'businessref_76', 'rating': '1'}, {'business_ref': 'businessref_52', 'rating': '4'}, {'business_ref': 'businessref_76', 'rating': '4'}, {'business_ref': 'businessref_76', 'rating': '4'}, {'business_ref': 'businessref_52', 'rating': '5'}, {'business_ref': 'businessref_76', 'rating': '4'}, {'business_ref': 'businessref_84', 'rating': '5'}, {'business_ref': 'businessref_76', 'rating': '4'}, {'business_ref': 'businessref_76', 'rating': '5'}], 'var_functions.query_db:14': [{'average_rating': '4.052631578947368'}]}

exec(code, env_args)
