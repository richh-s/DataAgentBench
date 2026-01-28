code = """import json
import re
import pandas as pd

citations_path = locals()['var_function-call-11680401091389409545']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

paper_docs_path = locals()['var_function-call-7196525365521970479']
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

df_citations = pd.DataFrame(citations_data)
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])

extracted_papers = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    year_match = re.search(r'\b(19|20)\d{2}\b', text)
    year = int(year_match.group(0)) if year_match else None

    contribution_match = re.search(r'Contribution:\s*([^\n]+)', text, re.IGNORECASE)
    contribution_types = []
    if contribution_match:
        contribution_text = contribution_match.group(1).lower()
        if 'empirical' in contribution_text:
            contribution_types.append('empirical')

    if year and 'empirical' in contribution_types:
        extracted_papers.append({
            'title': title,
            'year': year,
            'contribution': contribution_types
        })

df_papers = pd.DataFrame(extracted_papers)

df_filtered_papers = df_papers[(df_papers['year'] > 2016) & (df_papers['contribution'].apply(lambda x: 'empirical' in x))]

merged_df = pd.merge(df_filtered_papers, df_citations, on='title', how='inner')

result = merged_df.groupby('title')['citation_count'].sum().reset_index()
result.rename(columns={'citation_count': 'total_citation_count'}, inplace=True)

print("__RESULT__:")
print(result.to_json(orient='records'))"""

env_args = {'var_function-call-11680401091389409545': 'file_storage/function-call-11680401091389409545.json', 'var_function-call-7196525365521970479': 'file_storage/function-call-7196525365521970479.json'}

exec(code, env_args)
