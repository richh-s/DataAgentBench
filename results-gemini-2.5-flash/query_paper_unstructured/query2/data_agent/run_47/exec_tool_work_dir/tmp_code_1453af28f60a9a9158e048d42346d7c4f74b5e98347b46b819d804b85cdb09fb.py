code = """import json
import pandas as pd
import re

with open(locals()['var_function-call-11924547492432796297'], 'r') as f:
    citations_data = json.load(f)
citations_df = pd.DataFrame(citations_data)
citations_df['title'] = citations_df['title'].str.replace('.txt', '', regex=False)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

with open(locals()['var_function-call-10455918958747168031'], 'r') as f:
    paper_docs_data = json.load(f)

paper_info = []
for doc in paper_docs_data:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']
    
    source = None
    source_match = re.search(r'ACM Classification Keywords|Copyright \d{4} \u00a9 ACM|Published by ACM', text, re.IGNORECASE)
    if source_match:
        source = 'ACM'

    paper_info.append({'title': title, 'source': source})

paper_info_df = pd.DataFrame(paper_info)

merged_df = pd.merge(citations_df, paper_info_df, on='title', how='inner')
acm_papers_2018 = merged_df[merged_df['source'] == 'ACM']

if not acm_papers_2018.empty:
    average_citation_count = acm_papers_2018['citation_count'].mean()
    result = {'average_citation_count': average_citation_count}
else:
    result = {'average_citation_count': 0}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-11924547492432796297': 'file_storage/function-call-11924547492432796297.json', 'var_function-call-938173056724871066': 'file_storage/function-call-938173056724871066.json', 'var_function-call-10455918958747168031': 'file_storage/function-call-10455918958747168031.json'}

exec(code, env_args)
