code = """import pandas as pd
import json

reviews_output_str = locals()['var_function-call-2713994913755726959']['results'][0]
business_output_str = locals()['var_function-call-1432176497897247560']['results'][0]

def extract_json_from_output(output_string):
    start_index = output_string.find('[')
    end_index = output_string.rfind(']') + 1
    if start_index != -1 and end_index != -1:
        return output_string[start_index:end_index]
    return None

reviews_json_str = extract_json_from_output(reviews_output_str)
business_json_str = extract_json_from_output(business_output_str)

reviews_data = json.loads(reviews_json_str)
business_data = json.loads(business_json_str)

reviews_df = pd.DataFrame(reviews_data)
business_df = pd.DataFrame(business_data)

merged_df = pd.merge(reviews_df, business_df, on='gmap_id')

result = merged_df[['name', 'high_rating_review_count']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-2713994913755726959': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-1432176497897247560': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
