code = """import json
import re

# Access the stored results
all_vars = locals()

# Get the file paths from the storage variables
citations_file = all_vars.get('var_functions.query_db:2')
papers_file = all_vars.get('var_functions.query_db:5')

# Load the data
with open(citations_file, 'r') as f:
    citations_2018 = json.load(f)

with open(papers_file, 'r') as f:
    paper_docs = json.load(f)

# Convert citation data to a dict for easier lookup
citation_dict = {}
for cite in citations_2018:
    citation_dict[cite['title']] = int(cite['citation_count'])

print(f"Total papers with citations in 2018: {len(citation_dict)}")
print(f"Total paper documents: {len(paper_docs)}")

# More comprehensive approach to identify ACM papers
acm_venues = [
    'CHI', 'Ubicomp', 'UbiComp', 'CSCW', 'DIS', 'TEI', 'IUI', 'WWW',
    'ISS', 'UIST', 'MobileHCI', 'SIGCHI', 'SIGGRAPH'
]

acm_citations_list = []
mismatched_titles = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    
    # Check if this paper has 2018 citations
    if title not in citation_dict:
        continue
    
    text = doc.get('text', '')
    
    # Method 1: Look for explicit ACM references
    has_acm = False
    
    acm_patterns = [
        r'ACM', r'Association for Computing Machinery',
        r'Permission to make digital or hard copies',
        r'ACM 978-', r'ACM Digital Library',
        r'Proceedings of the ACM', r'ACM Conference', r'ACM SIG'
    ]
    
    for pattern in acm_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            has_acm = True
            break
    
    # Method 2: Look for ACM venues in the text
    if not has_acm:
        for venue in acm_venues:
            # Look for venue with year pattern (e.g., CHI '15, Ubicomp 2015)
            venue_patterns = [
                rf'{venue}\s*\'\d{{2}}',  # e.g., CHI '15
                rf'{venue}\s*20\d{{2}}',  # e.g., Ubicomp 2015
                rf'{venue}\s*\d{{4}}',   # e.g., CSCW 2016
            ]
            for pattern in venue_patterns:
                if re.search(pattern, text):
                    # Additional check: if it's a known ACM venue, count it
                    has_acm = True
                    break
            if has_acm:
                break
    
    # Method 3: Check text for "ACM" or "Association for Computing Machinery"
    if not has_acm:
        if 'ACM' in text or 'Association for Computing Machinery' in text:
            has_acm = True
    
    if has_acm:
        citation_count = citation_dict[title]
        acm_citations_list.append({
            'title': title,
            'citation_count': citation_count
        })

# Calculate statistics
if acm_citations_list:
    total_citations = sum(p['citation_count'] for p in acm_citations_list)
    avg_citations = total_citations / len(acm_citations_list)
    
    result = {
        'average_citation_count': round(avg_citations, 2),
        'total_acm_papers': len(acm_citations_list),
        'total_citations': total_citations,
        'sample_papers': acm_citations_list[:5]
    }
else:
    result = {
        'average_citation_count': 0,
        'total_acm_papers': 0,
        'total_citations': 0,
        'sample_papers': []
    }

print(f"Found {len(acm_citations_list)} ACM papers with citations in 2018")
if acm_citations_list:
    print(f"Average citations: {avg_citations:.2f}")
    print("\nTop papers:")
    for paper in sorted(acm_citations_list, key=lambda x: x['citation_count'], reverse=True)[:10]:
        print(f"  {paper['title']}: {paper['citation_count']}")

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'average_citation_count': 68.5, 'total_acm_papers': 2, 'total_citations': 137}}

exec(code, env_args)
