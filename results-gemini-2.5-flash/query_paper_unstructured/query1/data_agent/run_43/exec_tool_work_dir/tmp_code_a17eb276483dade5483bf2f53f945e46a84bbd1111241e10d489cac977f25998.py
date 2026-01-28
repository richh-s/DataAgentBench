code = """import json
import pandas as pd

food_papers_titles = locals()['var_function-call-13128819160068157754']

with open(locals()['var_function-call-1270969914095325749'], 'r') as f:
    citations_data = json.load(f)

citations_df = pd.DataFrame(citations_data)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

food_citations_df = citations_df[citations_df['title'].isin(food_papers_titles)]
total_citations = food_citations_df['citation_count'].sum()

print('__RESULT__:')
print(json.dumps(int(total_citations)))"""

env_args = {'var_function-call-288462182814586690': ['paper_docs'], 'var_function-call-17415221888068049620': 'file_storage/function-call-17415221888068049620.json', 'var_function-call-7078895685832278017': [], 'var_function-call-1270969914095325749': 'file_storage/function-call-1270969914095325749.json', 'var_function-call-7245065674231514512': [], 'var_function-call-13128819160068157754': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App']}

exec(code, env_args)
