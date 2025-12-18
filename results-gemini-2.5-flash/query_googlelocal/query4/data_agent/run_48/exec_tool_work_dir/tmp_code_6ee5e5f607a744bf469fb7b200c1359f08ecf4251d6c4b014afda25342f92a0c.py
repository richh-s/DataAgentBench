code = """import pandas as pd

review_data = locals()['var_function-call-12415697655197522120']['results'][0]
business_data = locals()['var_function-call-9814418456039598483']['results'][0]

df_reviews = pd.DataFrame(review_data)
df_businesses = pd.DataFrame(business_data)

merged_df = pd.merge(df_reviews, df_businesses, on='gmap_id')

result_list = []
for index, row in merged_df.iterrows():
    result_list.append(f"{row['name']} received {row['high_rating_review_count']} high-rating reviews.")

final_answer = "\n".join(result_list)

print('__RESULT__:')
print(final_answer)"""

env_args = {'var_function-call-12415697655197522120': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-9814418456039598483': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
