code = """import json

desc = var_call_DRyllglFGfhV6Dl5Y7Feon7O[0]['description']
name = var_call_DRyllglFGfhV6Dl5Y7Feon7O[0]['name']
business_id = var_call_DRyllglFGfhV6Dl5Y7Feon7O[0]['business_id']

def extract_categories(description:str):
    lower = description.lower()
    for token in ['menu featuring', 'offers a delightful array of dishes in the category of', 'offers a delightful array of options ranging from']:
        idx = lower.find(token)
        if idx != -1:
            tail = description[idx+len(token):].strip()
            return tail.strip().strip('."')
    return None

category = extract_categories(desc)

top = var_call_sdh69YxrbaaM84BtrkwE0Ni0[0]

out = {
    'business_name': name,
    'business_id': business_id,
    'category': category,
    'avg_rating': float(top['avg_rating']),
    'review_count_in_period': int(top['review_cnt']),
    'period': '2016-01-01 to 2016-06-30'
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_sdh69YxrbaaM84BtrkwE0Ni0': [{'business_ref': 'businessref_9', 'avg_rating': '4.0', 'review_cnt': '5'}], 'var_call_dNlUtevC2kf7HJPbwTDoPFH8': 'file_storage/call_dNlUtevC2kf7HJPbwTDoPFH8.json', 'var_call_DSMfMx7DUWwe2k7tnXFK3W8E': 'file_storage/call_DSMfMx7DUWwe2k7tnXFK3W8E.json', 'var_call_9z6vdTKpk250byvcwnDcBLxl': {'business_id': 'businessid_9', 'business_name': 'Coffee House Too Cafe', 'category': None, 'avg_rating': 4.0, 'review_count_in_period': 5}, 'var_call_DRyllglFGfhV6Dl5Y7Feon7O': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
