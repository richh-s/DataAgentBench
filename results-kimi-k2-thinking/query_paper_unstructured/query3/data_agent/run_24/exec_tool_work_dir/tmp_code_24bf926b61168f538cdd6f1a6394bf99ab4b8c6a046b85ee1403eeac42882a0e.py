code = """import json
import re

# Get the file paths from storage
paper_docs_file = var_functions.query_db:2
citations_file = var_functions.query_db:3

# Read paper documents
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Process papers
empirical_papers_after_2016 = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '')
    
    # Find year
    year = None
    venue_year_match = re.search(r'(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH).+?(20\d{2})', text, re.IGNORECASE)
    if venue_year_match:
        year = int(venue_year_match.group(2))
    else:
        year_match = re.search(r'20\d{2}', text[:1000])
        if year_match:
            year = int(year_match.group())
    
    # Check for empirical contribution
    is_empirical = 'empirical' in text.lower()
    
    if year and year > 2016 and is_empirical:
        empirical_papers_after_2016.append(title)

# Read citations
with open(citations_file, 'r') as f:
    citations = json.load(f)

# Sum citations
citation_totals = {}
for cit in citations:
    title = cit.get('title', '')
    if title in empirical_papers_after_2016:
        count = int(cit.get('citation_count', 0))
        citation_totals[title] = citation_totals.get(title, 0) + count

# Format results
results = [{'title': title, 'total_citation_count': count} for title, count in citation_totals.items()]

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)
