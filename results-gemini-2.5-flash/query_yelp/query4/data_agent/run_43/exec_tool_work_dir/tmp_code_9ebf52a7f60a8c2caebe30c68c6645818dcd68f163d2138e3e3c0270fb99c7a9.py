code = """import pandas as pd
import json
import re

with open(locals()['var_function-call-7753006022657153088'], 'r') as f:
    businesses = json.load(f)

credit_card_businesses_with_categories = []

for business in businesses:
    attributes = business.get('attributes')
    if isinstance(attributes, dict) and attributes.get('BusinessAcceptsCreditCards') == 'True':
        business_id = business['business_id']
        description = business.get('description', '')
        
        categories_found = []
        # Try to find categories using different patterns
        match = re.search(r"in the (?:category|categories|fields) of \'?([a-zA-Z0-9&,\s]+)\'?\.", description)
        if match:
            categories_str = match.group(1).replace("\'", "").strip()
            categories_found.extend([c.strip() for c in re.split(r',| and ', categories_str) if c.strip()])
        
        if not categories_found:
            # Fallback for less structured descriptions, try to extract last part before '.'
            parts = description.split('.')
            if len(parts) > 1:
                last_sentence = parts[-2] # Consider second to last part as last part might be empty
                # Try to extract categories from the end of the sentence
                match_end = re.search(r'(?:in|of|and)\s+([a-zA-Z0-9&,\s]+)$|'''\s*([a-zA-Z0-9&,\s]+)$''', last_sentence)
                if match_end:
                    categories_str_end = (match_end.group(1) or match_end.group(2)).replace("\'", "").strip()
                    categories_found.extend([c.strip() for c in re.split(r',| and ', categories_str_end) if c.strip()])

        for category in categories_found:
            if category:
                credit_card_businesses_with_categories.append({'business_id': business_id, 'category': category})

df_credit_card_businesses = pd.DataFrame(credit_card_businesses_with_categories)

print('__RESULT__:')
print(df_credit_card_businesses.to_json(orient='records'))"""

env_args = {'var_function-call-10589892332600436595': ['checkin', 'business'], 'var_function-call-654616051907714223': [], 'var_function-call-1707409851110908864': [], 'var_function-call-7753006022657153088': 'file_storage/function-call-7753006022657153088.json'}

exec(code, env_args)
