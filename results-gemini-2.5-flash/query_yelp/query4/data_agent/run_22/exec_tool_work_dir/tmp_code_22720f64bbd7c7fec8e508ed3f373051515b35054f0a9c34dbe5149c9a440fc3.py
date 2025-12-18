code = """import json
import pandas as pd

business_data_path = locals()['var_function-call-3370925917841059415']
with open(business_data_path, 'r') as f:
    business_records = json.load(f)

credit_card_businesses = []
for record in business_records:
    attributes = record.get('attributes')
    if attributes and isinstance(attributes, dict) and attributes.get('BusinessAcceptsCreditCards') == 'True':
        business_id = record['business_id']
        description = record.get('description', '')
        categories_str = ''
        if ' in the fields of ' in description:
            categories_str = description.split(' in the fields of ')[1].strip('.')
        elif ' in the category of ' in description:
            categories_str = description.split(' in the category of ')[1].strip('.')
        elif ' offers a range of services in ' in description:
            categories_str = description.split(' offers a range of services in ')[1].strip('.')
        elif ' offers a wide range of services, including ' in description:
            categories_str = description.split(' offers a wide range of services, including ')[1].strip('.')
        elif ' offers a range of services including ' in description:
            categories_str = description.split(' offers a range of services including ')[1].strip('.')
        elif ' offers a diverse range of services and products in the fields of ' in description:
            categories_str = description.split(' offers a diverse range of services and products in the fields of ')[1].strip('.')
        elif ' offers a variety of services including ' in description:
            categories_str = description.split(' offers a variety of services including ')[1].strip('.')
        elif ' specializes in ' in description:
            categories_str = description.split(' specializes in ')[1].strip('.')
        elif ' offers a delightful array of options ranging from ' in description:
            categories_str = description.split(' offers a delightful array of options ranging from ')[1].strip('.')

        categories = [cat.strip() for cat in categories_str.split(',') if cat.strip()]
        for category in categories:
            credit_card_businesses.append({'business_id': business_id, 'category': category})

df_credit_card_businesses = pd.DataFrame(credit_card_businesses)

print('__RESULT__:')
print(df_credit_card_businesses.to_json(orient='records'))"""

env_args = {'var_function-call-3225241360483802484': ['checkin', 'business'], 'var_function-call-3370925917841059415': 'file_storage/function-call-3370925917841059415.json'}

exec(code, env_args)
