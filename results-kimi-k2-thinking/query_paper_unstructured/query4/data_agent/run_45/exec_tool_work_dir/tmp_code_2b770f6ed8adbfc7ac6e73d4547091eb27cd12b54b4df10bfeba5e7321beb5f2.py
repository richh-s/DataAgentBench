code = """import json
import re

# Access the stored results from locals()
paper_docs = locals()['var_functions.query_db:12']
citations_data = locals()['var_functions.query_db:1']

# Create a set of paper titles from the documents  
paper_titles = set()
for doc in paper_docs:
    filename = doc.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]  # Remove .txt extension
        paper_titles.add(title)

# Process papers to find physical activity domain and year 2016
physical_activity_papers = {}
for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Check if it's in physical activity domain (case insensitive)
    has_physical_activity = 'physical activity' in text.lower()
    
    # Extract year from text - look for patterns like 2016
    year = None
    year_match = re.search(r'\b(2016)\b', text)
    if year_match:
        year = int(year_match.group(1))
    
    if has_physical_activity and year == 2016:
        title = filename[:-4] if filename.endswith('.txt') else filename
        physical_activity_papers[title] = {
            'title': title,
            'year': year,
            'domain': 'physical activity'
        }

# Sum up citations for these papers
citation_totals = {}
for citation in citations_data:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    
    if title in physical_activity_papers:
        citation_totals[title] = citation_totals.get(title, 0) + count

# Prepare results
results = []
for title, total_citations in citation_totals.items():
    results.append({
        'title': title,
        'total_citations': total_citations
    })

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
