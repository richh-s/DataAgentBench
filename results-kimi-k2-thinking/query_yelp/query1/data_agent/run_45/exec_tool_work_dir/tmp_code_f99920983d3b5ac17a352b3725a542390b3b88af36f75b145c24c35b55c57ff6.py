code = """import json

# Get the reviews data
reviews = [
    {"business_ref": "businessref_65", "rating": "3"}, 
    {"business_ref": "businessref_84", "rating": "5"}, 
    {"business_ref": "businessref_65", "rating": "5"}, 
    {"business_ref": "businessref_87", "rating": "5"}, 
    {"business_ref": "businessref_65", "rating": "4"}, 
    {"business_ref": "businessref_87", "rating": "4"}, 
    {"business_ref": "businessref_84", "rating": "5"}, 
    {"business_ref": "businessref_65", "rating": "4"}, 
    {"business_ref": "businessref_65", "rating": "4"}, 
    {"business_ref": "businessref_52", "rating": "4"}, 
    {"business_ref": "businessref_65", "rating": "3"}, 
    {"business_ref": "businessref_65", "rating": "5"}, 
    {"business_ref": "businessref_52", "rating": "5"}, 
    {"business_ref": "businessref_76", "rating": "4"}, 
    {"business_ref": "businessref_76", "rating": "3"}, 
    {"business_ref": "businessref_52", "rating": "2"}, 
    {"business_ref": "businessref_65", "rating": "4"}, 
    {"business_ref": "businessref_52", "rating": "5"}, 
    {"business_ref": "businessref_76", "rating": "3"}, 
    {"business_ref": "businessref_65", "rating": "3"}, 
    {"business_ref": "businessref_84", "rating": "5"}, 
    {"business_ref": "businessref_76", "rating": "1"}, 
    {"business_ref": "businessref_65", "rating": "3"}, 
    {"business_ref": "businessref_87", "rating": "1"}, 
    {"business_ref": "businessref_65", "rating": "4"}, 
    {"business_ref": "businessref_65", "rating": "3"}, 
    {"business_ref": "businessref_87", "rating": "4"}, 
    {"business_ref": "businessref_65", "rating": "4"}, 
    {"business_ref": "businessref_87", "rating": "1"}, 
    {"business_ref": "businessref_52", "rating": "4"}, 
    {"business_ref": "businessref_65", "rating": "5"}, 
    {"business_ref": "businessref_76", "rating": "4"}, 
    {"business_ref": "businessref_65", "rating": "4"}, 
    {"business_ref": "businessref_65", "rating": "3"}, 
    {"business_ref": "businessref_76", "rating": "4"}, 
    {"business_ref": "businessref_65", "rating": "4"}, 
    {"business_ref": "businessref_87", "rating": "5"}, 
    {"business_ref": "businessref_52", "rating": "5"}, 
    {"business_ref": "businessref_76", "rating": "4"}, 
    {"business_ref": "businessref_84", "rating": "5"}, 
    {"business_ref": "businessref_65", "rating": "4"}, 
    {"business_ref": "businessref_76", "rating": "4"}, 
    {"business_ref": "businessref_76", "rating": "5"}
]

# Extract ratings and calculate average
ratings = [int(review['rating']) for review in reviews]
average_rating = sum(ratings) / len(ratings)

print('__RESULT__:')
print(json.dumps({"average_rating": round(average_rating, 2), "total_reviews": len(ratings)}))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}], 'var_functions.query_db:4': [{'business_ref': 'businessref_65', 'rating': '3'}, {'business_ref': 'businessref_84', 'rating': '5'}, {'business_ref': 'businessref_65', 'rating': '5'}, {'business_ref': 'businessref_87', 'rating': '5'}, {'business_ref': 'businessref_65', 'rating': '4'}, {'business_ref': 'businessref_87', 'rating': '4'}, {'business_ref': 'businessref_84', 'rating': '5'}, {'business_ref': 'businessref_65', 'rating': '4'}, {'business_ref': 'businessref_65', 'rating': '4'}, {'business_ref': 'businessref_52', 'rating': '4'}, {'business_ref': 'businessref_65', 'rating': '3'}, {'business_ref': 'businessref_65', 'rating': '5'}, {'business_ref': 'businessref_52', 'rating': '5'}, {'business_ref': 'businessref_76', 'rating': '4'}, {'business_ref': 'businessref_76', 'rating': '3'}, {'business_ref': 'businessref_52', 'rating': '2'}, {'business_ref': 'businessref_65', 'rating': '4'}, {'business_ref': 'businessref_52', 'rating': '5'}, {'business_ref': 'businessref_76', 'rating': '3'}, {'business_ref': 'businessref_65', 'rating': '3'}, {'business_ref': 'businessref_84', 'rating': '5'}, {'business_ref': 'businessref_76', 'rating': '1'}, {'business_ref': 'businessref_65', 'rating': '3'}, {'business_ref': 'businessref_87', 'rating': '1'}, {'business_ref': 'businessref_65', 'rating': '4'}, {'business_ref': 'businessref_65', 'rating': '3'}, {'business_ref': 'businessref_87', 'rating': '4'}, {'business_ref': 'businessref_65', 'rating': '4'}, {'business_ref': 'businessref_87', 'rating': '1'}, {'business_ref': 'businessref_52', 'rating': '4'}, {'business_ref': 'businessref_65', 'rating': '5'}, {'business_ref': 'businessref_76', 'rating': '4'}, {'business_ref': 'businessref_65', 'rating': '4'}, {'business_ref': 'businessref_65', 'rating': '3'}, {'business_ref': 'businessref_76', 'rating': '4'}, {'business_ref': 'businessref_65', 'rating': '4'}, {'business_ref': 'businessref_87', 'rating': '5'}, {'business_ref': 'businessref_52', 'rating': '5'}, {'business_ref': 'businessref_76', 'rating': '4'}, {'business_ref': 'businessref_84', 'rating': '5'}, {'business_ref': 'businessref_65', 'rating': '4'}, {'business_ref': 'businessref_76', 'rating': '4'}, {'business_ref': 'businessref_76', 'rating': '5'}]}

exec(code, env_args)
