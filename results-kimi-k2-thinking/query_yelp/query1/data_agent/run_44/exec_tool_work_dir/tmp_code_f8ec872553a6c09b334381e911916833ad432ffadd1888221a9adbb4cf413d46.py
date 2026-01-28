code = """import json

# Get the rating results from the previous query
ratings_raw = [{"rating": "3"}, {"rating": "5"}, {"rating": "5"}, {"rating": "5"}, {"rating": "4"}, {"rating": "4"}, {"rating": "5"}, {"rating": "4"}, {"rating": "4"}, {"rating": "4"}, {"rating": "3"}, {"rating": "5"}, {"rating": "5"}, {"rating": "4"}, {"rating": "3"}, {"rating": "2"}, {"rating": "4"}, {"rating": "5"}, {"rating": "3"}, {"rating": "3"}, {"rating": "5"}, {"rating": "1"}, {"rating": "3"}, {"rating": "1"}, {"rating": "4"}, {"rating": "3"}, {"rating": "4"}, {"rating": "4"}, {"rating": "1"}, {"rating": "4"}, {"rating": "5"}, {"rating": "4"}, {"rating": "4"}, {"rating": "3"}, {"rating": "4"}, {"rating": "4"}, {"rating": "5"}, {"rating": "5"}, {"rating": "4"}, {"rating": "5"}, {"rating": "4"}, {"rating": "4"}, {"rating": "5"}]

# Convert string ratings to integers
ratings = [int(item['rating']) for item in ratings_raw]

# Calculate average
average_rating = sum(ratings) / len(ratings)

# Format the result
result = f"{average_rating:.2f}"

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}], 'var_functions.query_db:2': [{'rating': '3'}, {'rating': '5'}, {'rating': '5'}, {'rating': '5'}, {'rating': '4'}, {'rating': '4'}, {'rating': '5'}, {'rating': '4'}, {'rating': '4'}, {'rating': '4'}, {'rating': '3'}, {'rating': '5'}, {'rating': '5'}, {'rating': '4'}, {'rating': '3'}, {'rating': '2'}, {'rating': '4'}, {'rating': '5'}, {'rating': '3'}, {'rating': '3'}, {'rating': '5'}, {'rating': '1'}, {'rating': '3'}, {'rating': '1'}, {'rating': '4'}, {'rating': '3'}, {'rating': '4'}, {'rating': '4'}, {'rating': '1'}, {'rating': '4'}, {'rating': '5'}, {'rating': '4'}, {'rating': '4'}, {'rating': '3'}, {'rating': '4'}, {'rating': '4'}, {'rating': '5'}, {'rating': '5'}, {'rating': '4'}, {'rating': '5'}, {'rating': '4'}, {'rating': '4'}, {'rating': '5'}], 'var_functions.query_db:5': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}], 'var_functions.query_db:6': [{'rating': '3'}, {'rating': '5'}, {'rating': '5'}, {'rating': '5'}, {'rating': '4'}, {'rating': '4'}, {'rating': '5'}, {'rating': '4'}, {'rating': '4'}, {'rating': '4'}, {'rating': '3'}, {'rating': '5'}, {'rating': '5'}, {'rating': '4'}, {'rating': '3'}, {'rating': '2'}, {'rating': '4'}, {'rating': '5'}, {'rating': '3'}, {'rating': '3'}, {'rating': '5'}, {'rating': '1'}, {'rating': '3'}, {'rating': '1'}, {'rating': '4'}, {'rating': '3'}, {'rating': '4'}, {'rating': '4'}, {'rating': '1'}, {'rating': '4'}, {'rating': '5'}, {'rating': '4'}, {'rating': '4'}, {'rating': '3'}, {'rating': '4'}, {'rating': '4'}, {'rating': '5'}, {'rating': '5'}, {'rating': '4'}, {'rating': '5'}, {'rating': '4'}, {'rating': '4'}, {'rating': '5'}], 'var_functions.query_db:8': []}

exec(code, env_args)
