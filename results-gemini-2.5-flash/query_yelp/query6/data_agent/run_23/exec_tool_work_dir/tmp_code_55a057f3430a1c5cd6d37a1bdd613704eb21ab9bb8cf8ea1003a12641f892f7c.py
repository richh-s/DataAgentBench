code = """import json

description = locals()['var_function-call-12191468098706126251']['results'][0][0]['description']
category_start_index = description.find("featuring ") + len("featuring ")
category_end_index = description.find(", perfect for")
category = description[category_start_index:category_end_index].strip()

business_ref_result = locals()['var_function-call-6033096644027190616']['results'][0][0]
business_ref = business_ref_result['business_ref']
average_rating = business_ref_result['average_rating']

answer = f"The business with the highest average rating is {business_ref.replace('businessref_', 'Business ')} with an average rating of {average_rating}. It belongs to the category: {category}."

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_function-call-6033096644027190616': [{'business_ref': 'businessref_9', 'average_rating': '4.0', 'review_count': '5'}], 'var_function-call-12191468098706126251': [{'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
