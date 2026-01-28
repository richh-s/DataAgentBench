code = """import json
import re

# Read paper documents
paper_docs_path = var_functions.query_db:2
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

# Extract paper information from documents
papers_info = []
for doc in paper_docs:
    # Extract title from filename
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else 'Unknown Title'
    
    # Extract text for analysis
    text = doc.get('text', '')
    
    # Extract year
    year = None
    # Look for venue and year markers
    venue_patterns = r'(CHI|Ubicomp|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UBICOMP)\s*[\'"]?\s*(20\d{2})'
    matches = re.findall(venue_patterns, text, re.IGNORECASE)
    
    if matches:
        year = int(matches[0][1])
    else:
        # Look for any four-digit year in the text
        year_match = re.search(r'20\d{2}', text)
        if year_match:
            year = int(year_match.group())
    
    # Determine contribution type - look for empirical in text
    contribution = ''
    text_lower = text.lower()
    
    # Check for empirical contribution
    if 'empirical' in text_lower:
        contribution = 'empirical'
    
    papers_info.append({
        'title': title,
        'year': year,
        'contribution': contribution
    })

# Read citations
citations_path = var_functions.query_db:3
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Create a dictionary to sum citations per paper
citation_sums = {}
for cit in citations:
    title = cit.get('title', '')
    count = int(cit.get('citation_count', 0))
    if title in citation_sums:
        citation_sums[title] += count
    else:
        citation_sums[title] = count

# Filter papers: empirical contribution and published after 2016
results = []
for paper in papers_info:
    if paper['year'] and paper['year'] > 2016 and paper['contribution'] == 'empirical':
        title = paper['title']
        if title in citation_sums:
            results.append({
                'title': title,
                'total_citation_count': citation_sums[title]
            })

# Print result in required format
print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)
