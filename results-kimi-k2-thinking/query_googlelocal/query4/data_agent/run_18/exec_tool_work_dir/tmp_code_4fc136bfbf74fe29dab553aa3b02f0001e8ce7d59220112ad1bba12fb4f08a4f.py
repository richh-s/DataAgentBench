code = """import json

# Access the stored results
business_data = var_functions.query_db:6
review_data = var_functions.query_db:5

# Create the final answer by matching gmap_id to business name
answer = []
for review in review_data:
    gmap_id = review['gmap_id']
    count = review['high_rating_count']
    # Find the business name
    for business in business_data:
        if business['gmap_id'] == gmap_id:
            answer.append(f"{business['name']}: {count} high-rating reviews")
            break

final_answer = "\\n".join(answer)
print("__RESULT__:")
print(final_answer)"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:5': [{'gmap_id': 'gmap_20', 'high_rating_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_count': '6'}], 'var_functions.query_db:6': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}], 'var_functions.query_db:8': [{'gmap_id': 'gmap_20', 'high_rating_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_count': '6'}, {'gmap_id': 'gmap_35', 'high_rating_count': '6'}, {'gmap_id': 'gmap_72', 'high_rating_count': '5'}, {'gmap_id': 'gmap_62', 'high_rating_count': '5'}, {'gmap_id': 'gmap_46', 'high_rating_count': '5'}, {'gmap_id': 'gmap_17', 'high_rating_count': '4'}, {'gmap_id': 'gmap_69', 'high_rating_count': '3'}, {'gmap_id': 'gmap_56', 'high_rating_count': '3'}], 'var_functions.query_db:10': [{'gmap_id': 'gmap_20', 'high_rating_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_count': '6'}], 'var_functions.query_db:12': [{'rating': '1', 'count': '12'}, {'rating': '2', 'count': '2'}, {'rating': '3', 'count': '2'}, {'rating': '4', 'count': '7'}, {'rating': '5', 'count': '84'}]}

exec(code, env_args)
