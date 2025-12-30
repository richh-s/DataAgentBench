code = """import pandas as pd
import json

citations_file = locals()['var_function-call-7410212991170922061']
paper_docs_file = locals()['var_function-call-1872680180026608863']

with open(citations_file, 'r') as f:
    citations_data = json.load(f)

with open(paper_docs_file, 'r') as f:
    paper_docs_data = json.load(f)

df_citations = pd.DataFrame(citations_data)
df_paper_docs = pd.DataFrame(paper_docs_data)

df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])
df_paper_docs['title'] = df_paper_docs['filename'].str.replace('.txt', '', regex=False)

def extract_venue(text):
    if "CHI" in text:
        return "CHI"
    return None

df_paper_docs['venue'] = df_paper_docs['text'].apply(extract_venue)
df_chi_papers = df_paper_docs[df_paper_docs['venue'] == 'CHI']

merged_df = pd.merge(df_citations, df_chi_papers, on='title', how='inner')

total_citations = merged_df['citation_count'].sum()

print('__RESULT__:')
print(json.dumps(total_citations))"""

env_args = {'var_function-call-7410212991170922061': 'file_storage/function-call-7410212991170922061.json', 'var_function-call-1872680180026608863': 'file_storage/function-call-1872680180026608863.json'}

exec(code, env_args)
