code = """import json
import pandas as pd

filtered_papers = locals()['var_function-call-7497874506724323776']
df_papers = pd.DataFrame(filtered_papers)

citations_file_path = locals()['var_function-call-10447827911067689876']
with open(citations_file_path, 'r') as f:
    citations_data = json.load(f)
df_citations = pd.DataFrame(citations_data)
df_citations['total_citation_count'] = df_citations['total_citation_count'].astype(int)

merged_df = pd.merge(df_papers, df_citations, on='title', how='inner')

result = merged_df[['title', 'total_citation_count']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-14474643791060089691': ['paper_docs'], 'var_function-call-6604890257152561261': 'file_storage/function-call-6604890257152561261.json', 'var_function-call-3273880440063485916': [], 'var_function-call-16964130583038944759': ['Citations', 'sqlite_sequence'], 'var_function-call-11401142599698079820': [], 'var_function-call-7497874506724323776': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018, 'contribution': ['empirical', 'survey']}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019, 'contribution': ['empirical', 'survey']}], 'var_function-call-10447827911067689876': 'file_storage/function-call-10447827911067689876.json'}

exec(code, env_args)
