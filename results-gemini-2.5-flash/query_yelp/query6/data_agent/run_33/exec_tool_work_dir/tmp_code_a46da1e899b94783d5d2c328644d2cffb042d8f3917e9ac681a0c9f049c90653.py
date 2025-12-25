code = """import json
business_info = locals()['var_function-call-1096217059710138870'][0]
business_name = business_info['name']
description = business_info['description']

# Extract categories from the description
# The categories are usually listed after 'featuring' and before 'perfect for a cozy meal'
start_index = description.find('featuring') + len('featuring')
end_index = description.find(', perfect for a cozy meal')

if start_index != -1 and end_index != -1 and start_index < end_index:
    categories_str = description[start_index:end_index].strip()
    # Assuming categories are comma-separated and we want the primary category or a list of them.
    # For simplicity, let's take the first one or the whole string if it's a single category.
    # Let's extract all of them for a comprehensive answer.
    categories = [cat.strip() for cat in categories_str.split(',') if cat.strip()]
    category_text = ', '.join(categories)
else:
    category_text = "N/A (category not found in description)"

answer = f"The business with the highest average rating is {business_name}, and it belongs to the following categories: {category_text}."

print("__RESULT__:")
print(json.dumps(answer))"""

env_args = {'var_function-call-12719571196467189363': [{'business_ref': 'businessref_16', 'rating': '1'}, {'business_ref': 'businessref_23', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_96', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_37', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '4'}, {'business_ref': 'businessref_43', 'rating': '4'}, {'business_ref': 'businessref_14', 'rating': '3'}, {'business_ref': 'businessref_21', 'rating': '1'}, {'business_ref': 'businessref_16', 'rating': '3'}, {'business_ref': 'businessref_31', 'rating': '1'}, {'business_ref': 'businessref_30', 'rating': '2'}, {'business_ref': 'businessref_81', 'rating': '1'}, {'business_ref': 'businessref_71', 'rating': '5'}, {'business_ref': 'businessref_31', 'rating': '1'}, {'business_ref': 'businessref_46', 'rating': '5'}, {'business_ref': 'businessref_99', 'rating': '5'}, {'business_ref': 'businessref_40', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_68', 'rating': '1'}, {'business_ref': 'businessref_11', 'rating': '5'}, {'business_ref': 'businessref_21', 'rating': '1'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '3'}, {'business_ref': 'businessref_46', 'rating': '5'}, {'business_ref': 'businessref_68', 'rating': '1'}, {'business_ref': 'businessref_88', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '2'}, {'business_ref': 'businessref_71', 'rating': '1'}, {'business_ref': 'businessref_28', 'rating': '5'}, {'business_ref': 'businessref_71', 'rating': '5'}, {'business_ref': 'businessref_37', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '3'}, {'business_ref': 'businessref_17', 'rating': '5'}, {'business_ref': 'businessref_82', 'rating': '4'}], 'var_function-call-5017132378225216979': 'businessid_9', 'var_function-call-11082267816521656977': [], 'var_function-call-1096217059710138870': [{'_id': '6859a000fe8b31cd7362e2f3', 'name': 'Coffee House Too Cafe', 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
