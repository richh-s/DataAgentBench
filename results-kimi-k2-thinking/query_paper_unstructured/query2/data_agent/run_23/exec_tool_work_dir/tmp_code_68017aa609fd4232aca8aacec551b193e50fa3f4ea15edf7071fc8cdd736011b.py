code = """import json
import re

# Read citations data
citations_file = var_functions.query_db:6
citations = []
with open(citations_file, 'r') as f:
    citations = json.load(f)

# Read paper docs data
papers_file = var_functions.query_db:7
papers = []
with open(papers_file, 'r') as f:
    papers = json.load(f)

# Get citations from 2018
citations_2018 = [c for c in citations if c.get('citation_year') == 2018]

# Create a mapping from paper title (lower) to paper doc for easy lookup
paper_map = {}
for paper in papers:
    # Extract title from filename (remove .txt)
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    paper_map[title.lower()] = {
        'title': title,
        'text': paper.get('text', ''),
        'original_title': title
    }

# Filter papers published by ACM
acm_papers = []
acm_citations = []

for cit in citations_2018:
    cit_title = cit.get('title', '').lower()
    
    # Find matching paper
    if cit_title in paper_map:
        paper = paper_map[cit_title]
        text = paper.get('text', '')
        
        # Look for ACM in the text (common indicators of ACM publication)
        # This could be in copyright notice, conference headers, etc.
        if 'ACM' in text or 'acm' in text or 'Association for Computing Machinery' in text:
            # Verify it's not just a citation but actual publication
            # Common patterns for ACM publication
            acm_indicators = [
                'ACM', 'acm.org', 'Association for Computing Machinery',
                'ISBN:', 'ISBN', 'DOI:', 'doi.acm.org',
                'Permission to make digital or hard copies', 'Copyright','citation_year' in c
            ]
            
            # Check for ACM publishing indicators
            has_acm_publisher = any(indicator in text for indicator in acm_indicators)
            
            if has_acm_publisher:
                acm_papers.append(paper)
                acm_citations.append({
                    'title': cit.get('title'),
                    'citation_count': int(cit.get('citation_count', 0))
                })

# Calculate average citation count
if acm_citations:
    avg_citations = sum(c['citation_count'] for c in acm_citations) / len(acm_citations)
    count = len(acm_citations)
else:
    avg_citations = 0
    count = 0

result = {
    'acm_papers_count': count,
    'average_citation_count': round(avg_citations, 2)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '14', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '28', 'citation_year': '2018'}, {'id': '25', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '58', 'citation_year': '2018'}, {'id': '34', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '20', 'citation_year': '2018'}, {'id': '40', 'title': 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set', 'citation_count': '13', 'citation_year': '2018'}], 'var_functions.list_db:1': ['paper_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
