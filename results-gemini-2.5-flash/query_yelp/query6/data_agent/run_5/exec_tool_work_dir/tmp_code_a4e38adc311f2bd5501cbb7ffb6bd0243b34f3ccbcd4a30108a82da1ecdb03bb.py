code = """import json

result_business_ref_str = locals()['var_function-call-3030456419562296626']['results'][0]
result_business_ref = json.loads(result_business_ref_str)
business_id = result_business_ref['business_ref'].replace("businessref_", "businessid_")
average_rating = result_business_ref['average_rating']

business_description_result_str = locals()['var_function-call-13816901056741780483']['results'][0]
business_description_result = json.loads(business_description_result_str)
description = business_description_result['description']

# Extract categories from the description
categories_start_tag = "featuring "
categories_end_tag = ", perfect for a cozy meal any time of the day."

start_index = description.find(categories_start_tag)
end_index = description.find(categories_end_tag, start_index)

categories_list = []
if start_index != -1 and end_index != -1:
    categories_str = description[start_index + len(categories_start_tag):end_index]
    categories_list = [category.strip() for category in categories_str.split(',')]

# Construct a generic business name since a specific name isn't directly available in the provided data.
business_name = f"Business with ID {business_id}"

result = {
    "business_name": business_name,
    "average_rating": average_rating,
    "categories": categories_list
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-3030456419562296626': [{'business_ref': 'businessref_9', 'average_rating': '4.0', 'review_count': '5'}], 'var_function-call-13816901056741780483': [{'_id': '6859a000fe8b31cd7362e2f3', 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
