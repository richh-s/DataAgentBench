code = """import pandas as pd
import json

citations_data_path = locals()['var_function-call-15225904582982455067']
paper_docs_data_path = locals()['var_function-call-17129490907054162555']

with open(citations_data_path, 'r') as f:
    citations_data = json.load(f)

with open(paper_docs_data_path, 'r') as f:
    paper_docs_data = json.load(f)

citations_df = pd.DataFrame(citations_data)
paper_docs_df = pd.DataFrame(paper_docs_data)

# Convert 'citation_count' to numeric
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

# Extract title from filename for joining
paper_docs_df['title'] = paper_docs_df['filename'].str.replace('.txt', '', regex=False)

# Identify ACM papers
acm_papers_titles = []
for index, row in paper_docs_df.iterrows():
    if "ACM" in row['text']:
        acm_papers_titles.append(row['title'])

# Filter citations for ACM papers
acm_citations_df = citations_df[citations_df['title'].isin(acm_papers_titles)]

# Calculate average citation count
average_citation_count = acm_citations_df['citation_count'].mean()

print('__RESULT__:')
print(json.dumps(average_citation_count))"""

env_args = {'var_function-call-15225904582982455067': 'file_storage/function-call-15225904582982455067.json', 'var_function-call-17129490907054162555': 'file_storage/function-call-17129490907054162555.json'}

exec(code, env_args)
