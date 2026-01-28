code = """import json
import re

# Load the files - using string keys to access storage
with open('var_functions.query_db:12', 'r') as f:
    paper_docs = json.load(f)

with open('var_functions.query_db:1', 'r') as f:
    citations_data = json.load(f)

# Create a set of paper titles from the documents  
paper_titles = set()
for doc in paper_docs:
    filename = doc.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]  # Remove .txt extension
        paper_titles.add(title)

# Process papers to find physical activity domain and year 2016
physical_activity_papers = []
for doc in paper_docs:
    text = doc.get('text', '').lower()
    filename = doc.get('filename', '')
    
    # Check if it's in physical activity domain
    has_physical_activity = 'physical activity' in text
    
    # Extract year from text - look for patterns like 2016, '16, etc.
    year = None
    year_match = re.search(r'\b(2016)\b', doc.get('text', ''))
    if year_match:
        year = int(year_match.group(1))
    
    if has_physical_activity and year == 2016:
        title = filename[:-4] if filename.endswith('.txt') else filename
        physical_activity_papers.append(title)

# Sum up citations for these papers
citation_totals = {}
for citation in citations_data:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    
    if title in physical_activity_papers:
        citation_totals[title] = citation_totals.get(title, 0) + count

print('__RESULT__:')
print(json.dumps({
    'physical_activity_papers_2016': physical_activity_papers,
    'citation_totals': citation_totals,
    'total_papers_found': len(physical_activity_papers)
}))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
