code = """import json
description = locals()['var_function-call-5211452387769093178'][0]['description']
start_index = description.find("featuring ") + len("featuring ")
end_index = description.find(", perfect for a cozy meal")
categories_str = description[start_index:end_index]
categories = [cat.strip() for cat in categories_str.replace(" and", ",").split(",") if cat.strip()]
highest_rated_business_ref = locals()['var_function-call-9765275397514501736'][0]['business_ref']
highest_average_rating = locals()['var_function-call-9765275397514501736'][0]['average_rating']

result = {
    "business_id": highest_rated_business_ref.replace("businessref_", ""),
    "average_rating": highest_average_rating,
    "categories": categories
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-9765275397514501736': [{'business_ref': 'businessref_9', 'average_rating': '4.0', 'review_count': '5'}], 'var_function-call-5211452387769093178': [{'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
