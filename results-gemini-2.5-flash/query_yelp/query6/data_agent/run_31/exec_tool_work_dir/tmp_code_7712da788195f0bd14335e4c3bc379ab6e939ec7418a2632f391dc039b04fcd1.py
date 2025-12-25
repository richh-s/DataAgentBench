code = """import json

business_info = locals()['var_function-call-11000740935444237545'][0]
business_name = business_info['name']
description = business_info['description']

# Extract category from the description
# Example description: '...menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes,...'
# We want to extract 'Restaurants, Breakfast & Brunch, American (New), Cafes'

start_phrase = 'menu featuring '
end_phrase = ', perfect for a cozy meal'

start_index = description.find(start_phrase)
end_index = description.find(end_phrase)

category = description[start_index + len(start_phrase) : end_index] if start_index != -1 and end_index != -1 else 'N/A'

final_answer = f"The business that received the highest average rating is {business_name}, and it belongs to the category: {category}."

print('__RESULT__:')
print(json.dumps(final_answer))"""

env_args = {'var_function-call-1804990784370553280': [{'business_ref': 'businessref_9', 'average_rating': '4.0', 'review_count': '5'}], 'var_function-call-7056402424478715136': 'businessid_9', 'var_function-call-11000740935444237545': [{'name': 'Coffee House Too Cafe', 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
