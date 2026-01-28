code = """import json
import re

# Load the data files
citation_file = locals()['var_functions.query_db:2']
papers_file = locals()['var_functions.query_db:5']

with open(citation_file, 'r') as f:
    citations_2018 = json.load(f)

with open(papers_file, 'r') as f:
    paper_docs = json.load(f)

# Create citation lookup dictionary
citation_lookup = {}
for cite in citations_2018:
    citation_lookup[cite['title']] = int(cite['citation_count'])

# Find ACM papers that were cited in 2018
acm_citations_data = []

for doc in paper_docs:
    # Get title from filename
    filename = doc.get('filename', '')
    if not filename:
        continue
    
    title = filename[:-4] if filename.endswith('.txt') else filename
    
    # Check if this paper has citations in 2018
    if title not in citation_lookup:
        continue
    
    # Check if it's an ACM paper
    text = doc.get('text', '')
    text_lower = text.lower()
    
    # ACM detection criteria
    is_acm = False
    
    # 1. Direct ACM mentions
    if 'acm' in text_lower or 'association for computing machinery' in text_lower:
        is_acm = True
    
    # 2. ACM copyright/permission statement
    if 'permission to make digital or hard copies' in text_lower:
        is_acm = True
    
    # 3. Check for ACM venues with explicit ACM reference
    if not is_acm:
        # Look for common ACM conference patterns
        acm_patterns = [
            r'proceedings of the acm',
            r'acm conference',
            r'acm sig',
            r'acm transactions',
            r'acm 978-\d',
            r'acm digital library'
        ]
        
        for pattern in acm_patterns:
            if re.search(pattern, text_lower):
                is_acm = True
                break
    
    # 4. Check for known ACM venues combined with publisher info
    if not is_acm:
        # Common ACM venues
        acm_venues = ['chi', 'ubicomp', 'ubi comp', 'cscw', 'dis', 'tei', 'iui', 'www']
        
        # Look for venue mention combined with ACM-like patterns
        for venue in acm_venues:
            # Check if venue appears with year
            venue_pattern = rf'\b{venue}\b.*?(20\d{{2}}|\'\d{{2}})'
            if re.search(venue_pattern, text_lower):
                # Also check if ACM appears anywhere in the document
                if 'acm' in text_lower:
                    is_acm = True
                    break
    
    if is_acm:
        acm_citations_data.append({
            'title': title,
            'citation_count': citation_lookup[title]
        })

# Calculate average
if acm_citations_data:
    total_papers = len(acm_citations_data)
    total_citations = sum(p['citation_count'] for p in acm_citations_data)
    average_citations = total_citations / total_papers
    
    # Sort by citation count to show top papers
    sorted_papers = sorted(acm_citations_data, key=lambda x: x['citation_count'], reverse=True)
    
    result = {
        'average_citation_count': round(average_citations, 2),
        'total_acm_papers': total_papers,
        'total_citations': total_citations,
        'top_papers': sorted_papers[:5]
    }
else:
    result = {
        'average_citation_count': 0,
        'total_acm_papers': 0,
        'total_citations': 0,
        'top_papers': []
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'average_citation_count': 68.5, 'total_acm_papers': 2, 'total_citations': 137}, 'var_functions.execute_python:14': {'avg': 68.5, 'count': 2, 'total': 137}}

exec(code, env_args)
