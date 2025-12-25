code = """import pandas as pd
import json

with open(locals()['var_function-call-7753006022657153088'], 'r') as f:
    businesses = json.load(f)

credit_card_businesses = []
for business in businesses:
    attributes = business.get('attributes')
    if isinstance(attributes, dict) and attributes.get('BusinessAcceptsCreditCards') == 'True':
        business_id = business['business_id']
        description = business.get('description', '')
        # Extract categories from description (example: '...in the category of 'Restaurants, Chinese'.')
        categories_str = description.split('in the categories of ')[-1].split('in the category of ')[-1].split('.')[0].replace(''', '')
        categories = [c.strip() for c in categories_str.split(',') if c.strip()]
        
        # If no specific categories are found, try splitting the last part of description directly
        if not categories:
            last_part = description.split(' in the fields of ')[-1].split('.')[-2] if ' in the fields of ' in description else description.split(',')[-1].split('.')[0]
            categories = [c.strip() for c in last_part.split(' and ') if c.strip()]
            if not categories:
                categories = [c.strip() for c in description.split('offers a diverse range of services and products in the fields of ')[-1].split('.')[0].split(',') if c.strip()]
        
        for category in categories:
            credit_card_businesses.append({'business_id': business_id, 'category': category})

df_credit_card_businesses = pd.DataFrame(credit_card_businesses)

print('__RESULT__:')
print(df_credit_card_businesses.to_json(orient='records'))"""

env_args = {'var_function-call-10589892332600436595': ['checkin', 'business'], 'var_function-call-654616051907714223': [], 'var_function-call-1707409851110908864': [], 'var_function-call-7753006022657153088': 'file_storage/function-call-7753006022657153088.json'}

exec(code, env_args)
