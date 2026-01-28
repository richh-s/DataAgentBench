code = """import json
import pandas as pd

# Get the data from storage
citations_data = locals()['var_functions.query_db:4']
paper_docs_data = locals()['var_functions.query_db:5']

# Check if they're file paths
if isinstance(citations_data, str) and citations_data.endswith('.json'):
    with open(citations_data, 'r') as f:
        citations_data = json.load(f)

if isinstance(paper_docs_data, str) and paper_docs_data.endswith('.json'):
    with open(paper_docs_data, 'r') as f:
        paper_docs_data = json.load(f)

# Create DataFrames
df_citations = pd.DataFrame(citations_data)
df_papers = pd.DataFrame(paper_docs_data)

# Extract title from filename for papers
df_papers['title'] = df_papers['filename'].str.replace('.txt$', '', regex=True)

# Find papers in the 'food' domain
food_papers_info = []
for idx, paper in df_papers.iterrows():
    text = paper['text'].lower()
    if 'food' in text:
        # Count how many times 'food' appears to gauge relevance
        food_count = text.count('food')
        food_papers_info.append({
            'title': paper['title'],
            'food_mentions': food_count
        })

# Sort by food mentions to see most relevant papers first
food_papers_info.sort(key=lambda x: x['food_mentions'], reverse=True)

print('__RESULT__:')
print(json.dumps(food_papers_info, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:1': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:11': {'total_citation_count': 876, 'food_papers_count': 3, 'citation_records_count': 17}}

exec(code, env_args)
