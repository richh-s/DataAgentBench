code = """import json
import pandas as pd

# Get the data from storage
citations_data = locals()['var_functions.query_db:4']
paper_docs_data = locals()['var_functions.query_db:5']

# Check if they're file paths (strings) or actual data
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

# Find papers in the 'food' domain by searching the text
food_papers = []
for idx, paper in df_papers.iterrows():
    text = paper['text'].lower()
    # Look for food domain indicators
    if 'food' in text:
        food_papers.append(paper['title'])

# Get unique food paper titles
food_paper_titles = list(set(food_papers))

# Filter citations for food papers (case-insensitive matching)
food_citations = df_citations[df_citations['title'].str.lower().isin([t.lower() for t in food_paper_titles])]

# Convert citation_count to numeric
food_citations['citation_count'] = pd.to_numeric(food_citations['citation_count'])

# Calculate total citation count
total_citations = food_citations['citation_count'].sum()

# Also count unique food papers for context
unique_food_papers_count = len(food_paper_titles)

result = {
    'total_citation_count': int(total_citations),
    'food_papers_count': unique_food_papers_count,
    'citation_records_count': len(food_citations)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:1': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
