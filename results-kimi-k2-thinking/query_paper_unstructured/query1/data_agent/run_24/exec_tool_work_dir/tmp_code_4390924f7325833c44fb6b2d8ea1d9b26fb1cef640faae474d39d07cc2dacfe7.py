code = """import json
import pandas as pd

# Read the Citations data from file
citations_file = '/tmp/tmp7v0g7n1f.json'  # This is var_functions.query_db:4
citations_data = []
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Read the paper_docs data from file  
paper_docs_file = '/tmp/tmp9v6s1q6r.json'  # This is var_functions.query_db:5
paper_docs_data = []
with open(paper_docs_file, 'r') as f:
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
