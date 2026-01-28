code = """import json
import pandas as pd
import re

citations_data_path = locals()['var_function-call-3602683739999411260']
paper_docs_data_path = locals()['var_function-call-16332062949399673365']

with open(citations_data_path, 'r') as f:
    citations_data = json.load(f)

with open(paper_docs_data_path, 'r') as f:
    paper_docs_data = json.load(f)

citations_df = pd.DataFrame(citations_data)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

paper_info = []
for doc in paper_docs_data:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']
    source_match = re.search(r'Copyright \d{4} \u00a9 (ACM|IEEE|PubMed)', text)
    source = source_match.group(1) if source_match else 'N/A'
    paper_info.append({'title': title, 'source': source})

paper_info_df = pd.DataFrame(paper_info)

merged_df = pd.merge(citations_df, paper_info_df, on='title', how='inner')

acm_papers_df = merged_df[merged_df['source'] == 'ACM']

average_citation_count = acm_papers_df['citation_count'].mean()

print('__RESULT__:')
print(json.dumps(average_citation_count))"""

env_args = {'var_function-call-3602683739999411260': 'file_storage/function-call-3602683739999411260.json', 'var_function-call-16332062949399673365': 'file_storage/function-call-16332062949399673365.json'}

exec(code, env_args)
