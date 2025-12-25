code = """import pandas as pd
import json

businesses_with_credit_cards_raw = locals()['var_function-call-5749206060255450980']['query_db_response']['results'][0]
businesses_with_credit_cards = json.loads(businesses_with_credit_cards_raw)

df_businesses = pd.DataFrame(businesses_with_credit_cards)

def parse_categories(attributes):
    if isinstance(attributes, dict) and 'Categories' in attributes:
        return [cat.strip() for cat in attributes['Categories'].split(',')] if attributes['Categories'] else []
    return []

df_businesses['categories'] = df_businesses['attributes'].apply(parse_categories)
df_exploded = df_businesses.explode('categories')

category_counts = df_exploded.groupby('categories').size().reset_index(name='business_count')

most_common_category = category_counts.loc[category_counts['business_count'].idxmax()]


business_ids_in_most_common_category = df_exploded[df_exploded['categories'] == most_common_category['categories']]['business_id'].tolist()

print('__RESULT__:')
print(json.dumps({
    'most_common_category': most_common_category.to_dict(),
    'business_ids_in_most_common_category': business_ids_in_most_common_category
}))"""

env_args = {'var_function-call-5749206060255450980': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True'}}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'BusinessAcceptsCreditCards': 'True'}}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'attributes': {'BusinessAcceptsCreditCards': 'True'}}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'attributes': {'BusinessAcceptsCreditCards': 'True'}}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'attributes': {'BusinessAcceptsCreditCards': 'True'}}]}

exec(code, env_args)
