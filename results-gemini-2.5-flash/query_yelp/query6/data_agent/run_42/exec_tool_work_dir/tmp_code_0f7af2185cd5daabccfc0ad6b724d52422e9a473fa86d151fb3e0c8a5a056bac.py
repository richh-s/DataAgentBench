code = """business_info = locals()['var_function-call-2731257416781942543'][0]
business_ref = business_info['business_ref']
average_rating = business_info['average_rating']

description_data = locals()['var_function-call-4477193261604217513'][0]
description = description_data['description']

category_start = description.find("featuring ") + len("featuring ")
category_end = description.find(", perfect")
category = description[category_start:category_end]

result = f"The business {business_ref.replace('businessref_', '')} received the highest average rating of {average_rating} and belongs to the category: {category}."

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-2731257416781942543': [{'business_ref': 'businessref_9', 'average_rating': '4.0', 'review_count': '5'}], 'var_function-call-4477193261604217513': [{'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
