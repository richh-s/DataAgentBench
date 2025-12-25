code = """import json
import pandas as pd

review_counts = locals()['var_function-call-717367244536023637']
business_names = locals()['var_function-call-7802571701628065614']

df_review_counts = pd.DataFrame(review_counts)
df_business_names = pd.DataFrame(business_names)

merged_df = pd.merge(df_review_counts, df_business_names, on='gmap_id')

result_list = merged_df.to_dict(orient='records')

final_answer = []
for item in result_list:
    final_answer.append(f"{item['name']} received {item['high_rating_review_count']} high-rating reviews.")

print("__RESULT__:")
print(json.dumps("\n".join(final_answer)))"""

env_args = {'var_function-call-717367244536023637': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-5632580562048122738': "gmap_20', 'gmap_53', 'gmap_40", 'var_function-call-7802571701628065614': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
