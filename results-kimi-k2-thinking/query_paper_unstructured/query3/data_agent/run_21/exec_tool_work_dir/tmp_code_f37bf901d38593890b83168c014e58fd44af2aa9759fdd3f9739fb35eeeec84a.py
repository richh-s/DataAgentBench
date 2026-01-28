code = """import json
import re
import pandas as pd

# Load MongoDB paper documents
mongo_file = var_functions.query_db:14
with open(mongo_file, 'r') as f:
    paper_docs = json.load(f)

# Load citation data
citation_file = var_functions.query_db:12
with open(citation_file, 'r') as f:
    citations_data = json.load(f)

# Extract paper information from MongoDB documents
papers = []
for doc in paper_docs:
    try:
        filename = doc.get('filename', '')
        if not filename or '.txt' not in filename:
            continue
            
        # Extract title from filename
        title = filename.replace('.txt', '').strip()
        
        text = doc.get('text', '')
        
        # Extract year - look for 4-digit year patterns (2017-2029)
        year_match = re.search(r'20(1[7-9]|[2-9][0-9])', text)
        year = int(year_match.group()) if year_match else None
        
        # Check for empirical contribution
        is_empirical = bool(re.search(r'\bempirical\b', text, re.IGNORECASE))
        
        if title and year and is_empirical:
            papers.append({
                'title': title,
                'year': year
            })
    except:
        continue

# Create DataFrame for citations
citations_df = pd.DataFrame(citations_data)
if not citations_df.empty:
    # Convert citation_count to numeric
    citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'], errors='coerce')
    # Group by title and sum citation counts
    total_citations = citations_df.groupby('title')['citation_count'].sum().reset_index()
else:
    total_citations = pd.DataFrame(columns=['title', 'citation_count'])

# Create DataFrame for empirical papers
papers_df = pd.DataFrame(papers)

# Remove duplicates (same title may appear multiple times)
papers_df = papers_df.drop_duplicates(subset=['title'])

# Join papers with their total citations
result_df = pd.merge(papers_df, total_citations, on='title', how='left')

# Handle papers with no citations
result_df['citation_count'] = result_df['citation_count'].fillna(0).astype(int)

# Sort by title for consistent ordering
result_df = result_df.sort_values('title')

# Prepare final result as list of dictionaries
final_result = result_df.to_dict('records')

# Print result in required format
print('__RESULT__:')
print(json.dumps(final_result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
