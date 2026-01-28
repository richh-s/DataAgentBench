code = """import json
import pandas as pd

# Load the citations data for 2018
citations_path = locals()['var_functions.query_db:2']
citations_data = []
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

# Load the paper documents data
papers_path = locals()['var_functions.query_db:5']
papers_data = []
with open(papers_path, 'r') as f:
    papers_data = json.load(f)

# Convert to DataFrames
citations_df = pd.DataFrame(citations_data)
papers_df = pd.DataFrame(papers_data)

# Clean and prepare data
citations_df['citation_count'] = citations_df['citation_count'].astype(int)
citations_df['citation_year'] = citations_df['citation_year'].astype(int)

papers_df['title'] = papers_df['filename'].str.replace('.txt', '')

# Merge on title
merged_df = citations_df.merge(papers_df, on='title', how='inner')

# Filter for papers published by ACM
acm_papers = merged_df[merged_df['source'].str.contains('ACM', na=False)]

# Calculate average citation count
if not acm_papers.empty:
    avg_citations = acm_papers['citation_count'].mean()
    result = f"The average citation count for ACM papers cited in 2018 is {avg_citations:.2f}"
else:
    result = "No ACM papers found in 2018 citations"

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
