code = """import pandas as pd
businesses_with_credit_cards = locals()['var_function-call-5749206060255450980']['results'][0]
df_businesses = pd.DataFrame(businesses_with_credit_cards)

def parse_categories(attributes):
    if isinstance(attributes, dict) and 'Categories' in attributes:
        return [cat.strip() for cat in attributes['Categories'].split(',')] if attributes['Categories'] else []
    return []

df_businesses['categories'] = df_businesses['attributes'].apply(parse_categories)
df_exploded = df_businesses.explode('categories')

category_counts = df_exploded.groupby('categories').size().reset_index(name='business_count')

print('__RESULT__:')
print(category_counts.to_json(orient='records'))"""

env_args = {'var_function-call-5749206060255450980': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True'}}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'BusinessAcceptsCreditCards': 'True'}}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'attributes': {'BusinessAcceptsCreditCards': 'True'}}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'attributes': {'BusinessAcceptsCreditCards': 'True'}}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'attributes': {'BusinessAcceptsCreditCards': 'True'}}]}

exec(code, env_args)
