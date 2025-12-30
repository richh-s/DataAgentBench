code = """import json
import pandas as pd
import re

with open(locals()['var_function-call-11909799912303783270'], 'r') as f:
    paper_docs = json.load(f)


def extract_info(text):
    source = None
    match_source = re.search(r'(ACM|IEEE|PubMed)', text)
    if match_source:
        source = match_source.group(1)
    return source


paper_info = []
for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    source = extract_info(doc['text'])
    paper_info.append({'title': title, 'source': source})

df_papers = pd.DataFrame(paper_info)
df_acm_papers = df_papers[df_papers['source'] == 'ACM']

with open(locals()['var_function-call-3190855524824393528'], 'r') as f:
    citations_2018 = json.load(f)
df_citations = pd.DataFrame(citations_2018)
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])

merged_df = pd.merge(df_acm_papers, df_citations, on='title', how='inner')

if not merged_df.empty:
    average_citation_count = merged_df['citation_count'].mean()
else:
    average_citation_count = 0

print('__RESULT__:')
print(json.dumps(average_citation_count))"""

env_args = {'var_function-call-3190855524824393528': 'file_storage/function-call-3190855524824393528.json', 'var_function-call-11574367242754567115': 'file_storage/function-call-11574367242754567115.json', 'var_function-call-11909799912303783270': 'file_storage/function-call-11909799912303783270.json'}

exec(code, env_args)
