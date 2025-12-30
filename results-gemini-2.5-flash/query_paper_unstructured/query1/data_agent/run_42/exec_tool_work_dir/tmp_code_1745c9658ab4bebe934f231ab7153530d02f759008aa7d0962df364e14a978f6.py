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
    # Simple keyword search for 'food' domain, as per hint "When matching domains or contributions, use substring/contains matching"
    if 'food' in text.lower():
        domain = 'food'
    paper_info.append({'title': title, 'domain': domain})

paper_info_df = pd.DataFrame(paper_info)

# Filter for papers in the 'food' domain
food_papers_df = paper_info_df[paper_info_df['domain'] == 'food']

# Merge with citations data
merged_df = pd.merge(food_papers_df, citations_data, on='title', how='inner')

# Calculate total citation count
merged_df['citation_count'] = pd.to_numeric(merged_df['citation_count'])
total_citations = merged_df['citation_count'].sum()

print('__RESULT__:')
print(json.dumps(total_citations))"""

env_args = {'var_function-call-15463748877077547584': 'file_storage/function-call-15463748877077547584.json', 'var_function-call-664171284714214306': 'file_storage/function-call-664171284714214306.json'}

exec(code, env_args)
