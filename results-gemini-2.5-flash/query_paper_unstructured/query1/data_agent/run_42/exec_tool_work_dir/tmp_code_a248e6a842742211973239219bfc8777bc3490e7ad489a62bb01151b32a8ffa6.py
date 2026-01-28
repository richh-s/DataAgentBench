code = """import pandas as pd
import json

citations_data = pd.DataFrame(json.load(open(locals()['var_function-call-15463748877077547584'], 'r')))
paper_docs_data = json.load(open(locals()['var_function-call-664171284714214306'], 'r'))

paper_info = []
for doc in paper_docs_data:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']
    domain = ''
    if 'food' in text.lower():
        domain = 'food'
    paper_info.append({'title': title, 'domain': domain})

paper_info_df = pd.DataFrame(paper_info)

food_papers_df = paper_info_df[paper_info_df['domain'] == 'food']

merged_df = pd.merge(food_papers_df, citations_data, on='title', how='inner')

merged_df['citation_count'] = pd.to_numeric(merged_df['citation_count'])
total_citations = int(merged_df['citation_count'].sum())

print('__RESULT__:')
print(json.dumps(total_citations))"""

env_args = {'var_function-call-15463748877077547584': 'file_storage/function-call-15463748877077547584.json', 'var_function-call-664171284714214306': 'file_storage/function-call-664171284714214306.json'}

exec(code, env_args)
