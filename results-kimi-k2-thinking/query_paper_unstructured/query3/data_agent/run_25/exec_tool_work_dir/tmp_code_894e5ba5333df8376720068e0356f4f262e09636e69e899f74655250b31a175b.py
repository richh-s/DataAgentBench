code = """import json
import re
from datetime import datetime

# Read the full MongoDB results
citation_file = var_functions.query_db:0
mongodb_file = var_functions.query_db:2

# Load the citation data
with open(citation_file, 'r') as f:
    citations_data = json.load(f)

# Load the MongoDB paper data
with open(mongodb_file, 'r') as f:
    papers_data = json.load(f)

print(f"Loaded {len(citations_data)} citation records and {len(papers_data)} paper documents")

# Extract paper information
papers_info = []

for paper in papers_data:
    # Extract title from filename
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract text
    text = paper.get('text', '')
    
    # Find year in text - look for patterns like YYYY (usually in header)
    year_match = re.search(r'\b(201[0-9]|202[0-9])\b', text)
    year = int(year_match.group(1)) if year_match else None
    
    # Check if paper has empirical contribution by searching for "empirical" in text
    has_empirical = 'empirical' in text.lower()
    
    # Also try to find venue and source patterns
    venue_match = re.search(r'(CHI|Ubicomp|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UIST)\s*(\'\d{2}|\d{4})?', text)
    venue = venue_match.group(1) if venue_match else None
    
    source_match = re.search(r'(ACM|IEEE|PubMed)', text)
    source = source_match.group(1) if source_match else None
    
    papers_info.append({
        'title': title,
        'year': year,
        'has_empirical': has_empirical,
        'venue': venue,
        'source': source
    })

# Filter papers published after 2016 (2017 and later) and with empirical contribution
filtered_papers = [p for p in papers_info if p['year'] and p['year'] > 2016 and p['has_empirical']]

print(f"Found {len(filtered_papers)} empirical papers published after 2016")

# Create a dictionary of title to paper info for easy lookup
paper_dict = {p['title']: p for p in filtered_papers}

# Join with citation data
merged_results = []
for citation in citations_data:
    title = citation.get('title', '')
    if title in paper_dict:
        paper_info = paper_dict[title]
        merged_results.append({
            'title': title,
            'year': paper_info['year'],
            'total_citations': int(citation.get('total_citations', 0)),
            'venue': paper_info['venue'],
            'source': paper_info['source']
        })

# Sort by total citations in descending order
merged_results.sort(key=lambda x: x['total_citations'], reverse=True)

result = {
    'count': len(merged_results),
    'papers': merged_results
}

print("__RESULT__:")
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
