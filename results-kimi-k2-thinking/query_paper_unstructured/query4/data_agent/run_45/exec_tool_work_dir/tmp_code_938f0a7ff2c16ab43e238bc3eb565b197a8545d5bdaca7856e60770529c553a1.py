code = """import json
import re

# Get the data from locals() - the keys are the full strings
paper_docs_key = None
citations_data_key = None

for key in locals().keys():
    if 'query_db:12' in key:
        paper_docs_key = key
    elif 'query_db:1' in key:
        citations_data_key = key

paper_docs = locals()[paper_docs_key]
citations_data = locals()[citations_data_key]

# Now both should be lists of dictionaries
physical_activity_papers = {}

for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Check for physical activity domain and year 2016
    has_physical_activity = 'physical activity' in text.lower()
    
    # Extract year
    year = None
    year_match = re.search(r'\b(2016)\b', text)
    if year_match:
        year = int(year_match.group(1))
    
    if has_physical_activity and year == 2016:
        title = filename[:-4] if filename.endswith('.txt') else filename
        physical_activity_papers[title] = title

# Sum citations for these papers
citation_totals = {}
for citation in citations_data:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    
    if title in physical_activity_papers:
        citation_totals[title] = citation_totals.get(title, 0) + count

# Format results
results = []
for title, total in citation_totals.items():
    results.append({
        'title': title,
        'total_citations': total
    })

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
