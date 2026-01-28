code = """import json
import pandas as pd

# Read citations data
citations_file = 'var_functions.query_db:5'
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Read paper documents data  
paper_docs_file = 'var_functions.query_db:6'
with open(paper_docs_file, 'r') as f:
    paper_docs_data = json.load(f)

# Create DataFrames
citations_df = pd.DataFrame(citations_data)
paper_docs_df = pd.DataFrame(paper_docs_data)

# Extract title from filename
paper_docs_df['title'] = paper_docs_df['filename'].str.replace('.txt', '', regex=False)

# Identify CHI papers by searching for CHI in text
paper_docs_df['is_chi'] = paper_docs_df['text'].str.contains('CHI', case=False, na=False)
chi_papers_df = paper_docs_df[paper_docs_df['is_chi']].copy()

# Normalize titles for matching
citations_df['title_norm'] = citations_df['title'].str.lower().str.strip()
chi_papers_df['title_norm'] = chi_papers_df['title'].str.lower().str.strip()

# Merge on normalized titles
merged_df = pd.merge(chi_papers_df, citations_df, on='title_norm', how='inner')

# Calculate total citations
total_citations = merged_df['citation_count'].astype(int).sum()
num_papers = len(merged_df)

# Prepare result
result = {
    'total_citations': int(total_citations),
    'num_papers': int(num_papers),
    'papers': merged_df[['title_x', 'citation_count']].rename(columns={'title_x': 'title'}).to_dict('records')
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
