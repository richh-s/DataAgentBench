code = """description = locals()['var_function-call-5211452387769093178'][0]['description']
start_index = description.find("featuring ") + len("featuring ")
end_index = description.find(", perfect for a cozy meal")
categories_str = description[start_index:end_index]
categories = categories_str.replace(" and", ",").split(", ")
highest_rated_business_ref = locals()['var_function-call-9765275397514501736'][0]['business_ref']
highest_average_rating = locals()['var_function-call-9765275397514501736'][0]['average_rating']

print("__RESULT__:")
print(f"The business with the highest average rating is {highest_rated_business_ref.replace("businessref_", "")}, with an average rating of {highest_average_rating}. It belongs to the categories: {", ".join(categories)}.")"""

env_args = {'var_function-call-9765275397514501736': [{'business_ref': 'businessref_9', 'average_rating': '4.0', 'review_count': '5'}], 'var_function-call-5211452387769093178': [{'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
