code = """import json
import pandas as pd

filtered_papers = locals()['var_function-call-8118617072640170263']

file_path_citations = locals()['var_function-call-9960317872571995896']
with open(file_path_citations, 'r') as f:
    citations_data = json.load(f)

df_papers = pd.DataFrame(filtered_papers)
df_citations = pd.DataFrame(citations_data)

df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'], errors='coerce')

merged_df = pd.merge(df_papers, df_citations, on='title', how='inner')

total_citations = merged_df.groupby('title')['citation_count'].sum().reset_index()

result = total_citations.to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-1330267927777135001': ['paper_docs'], 'var_function-call-8451556604040005886': 'file_storage/function-call-8451556604040005886.json', 'var_function-call-4293209901039072546': [], 'var_function-call-8118617072640170263': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_function-call-9960317872571995896': 'file_storage/function-call-9960317872571995896.json'}

exec(code, env_args)
