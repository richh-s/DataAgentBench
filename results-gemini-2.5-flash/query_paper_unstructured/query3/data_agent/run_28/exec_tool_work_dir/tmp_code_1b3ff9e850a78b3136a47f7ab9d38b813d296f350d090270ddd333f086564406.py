code = """import pandas as pd
import json

filtered_papers = json.loads(locals()['var_function-call-7805726745655903324'])
citations_data = json.loads(open(locals()['var_function-call-11639470653427147503'], 'r').read())

df_filtered_papers = pd.DataFrame(filtered_papers)
df_citations = pd.DataFrame(citations_data)

df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])

merged_df = pd.merge(df_filtered_papers, df_citations, on='title', how='inner')

total_citations = merged_df.groupby('title')['citation_count'].sum().reset_index()

result = total_citations.to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_function-call-1149772925907859432': ['paper_docs'], 'var_function-call-5976115717685306466': 'file_storage/function-call-5976115717685306466.json', 'var_function-call-7805726745655903324': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2020, 'contribution': ['empirical', 'survey']}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2020, 'contribution': ['empirical', 'survey']}], 'var_function-call-11639470653427147503': 'file_storage/function-call-11639470653427147503.json'}

exec(code, env_args)
