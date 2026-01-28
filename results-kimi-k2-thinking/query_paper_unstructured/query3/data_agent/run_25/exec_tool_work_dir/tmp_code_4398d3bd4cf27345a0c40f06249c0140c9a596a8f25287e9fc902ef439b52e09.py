code = """import json
import re

# Get the file paths
citation_file_path = locals()['var_functions.query_db:0']
mongodb_file_path = locals()['var_functions.query_db:2']

# Load citation data
with open(citation_file_path, 'r') as f:
    citations = json.load(f)

# Load MongoDB paper data
with open(mongodb_file_path, 'r') as f:
    papers = json.load(f)

# Extract paper details
paper_info = []
for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = paper.get('text', '')
    
    # Extract year (look for 2017, 2018, 2019, etc.)
    year_match = re.search(r'\b(201[7-9]|202[0-9])\b', text)
    year = int(year_match.group(1)) if year_match else None
    
    # Find if paper has empirical contribution
    has_empirical = 'empirical' in text.lower()
    
    # Extract venue if present
    venue_match = re.search(r'(CHI|Ubicomp|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UIST)\s*(\'\d{2}|\d{4})?', text)
    venue = venue_match.group(1) if venue_match else None
    
    # Extract source if present
    source_match = re.search(r'(ACM|IEEE|PubMed)', text)
    source = source_match.group(1) if source_match else None
    
    if title and year and has_empirical:
        paper_info.append({
            'title': title,
            'year': year,
            'has_empirical': has_empirical,
            'venue': venue,
            'source': source
        })

# Create dictionary for easy lookup by title
paper_dict = {p['title']: p for p in paper_info}

# Join with citations data
citations_dict = {c['title']: int(c['total_citations']) for c in citations}

# Get results for empirical papers published after 2016 (2017+)
results = []
for title, paper in paper_dict.items():
    total_citations = citations_dict.get(title, 0)
    if total_citations > 0:
        results.append({
            'title': title,
            'year': paper['year'],
            'total_citations': total_citations,
            'venue': paper['venue'],
            'source': paper['source']
        })

# Sort by citations
results.sort(key=lambda x: x['total_citations'], reverse=True)

print("__RESULT__:")
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
