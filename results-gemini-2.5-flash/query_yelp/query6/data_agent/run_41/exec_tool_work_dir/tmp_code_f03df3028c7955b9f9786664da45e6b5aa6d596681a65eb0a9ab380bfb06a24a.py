code = """import json

business_info = locals()['var_function-call-10431651234061519868'][0]
business_name = business_info['name']
description = business_info['description']

# Extracting category from the description. The category information is present after 'featuring' and before 'perfect for'
start_index = description.find('featuring') + len('featuring')
end_index = description.find('perfect for')
category = description[start_index:end_index].strip()

final_answer = f"The business that received the highest average rating is {business_name} with an average rating of 4.0. It belongs to the category: {category}"

print('__RESULT__:')
print(json.dumps(final_answer))"""

env_args = {'var_function-call-18296553822686851081': [{'business_ref': 'businessref_9', 'average_rating': '4.0', 'review_count': '5'}], 'var_function-call-8939159942922486649': 'businessid_9', 'var_function-call-10431651234061519868': [{'name': 'Coffee House Too Cafe', 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
