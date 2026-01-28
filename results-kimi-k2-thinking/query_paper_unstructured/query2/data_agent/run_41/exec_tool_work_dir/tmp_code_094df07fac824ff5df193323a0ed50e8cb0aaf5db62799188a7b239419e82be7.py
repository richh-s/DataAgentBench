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

# Process papers to identify ACM papers with 2018 citations
acm_citations_list = []
acm_count = 0

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
    text_lower = text.lower()
    
    # Check for ACM indicators
    is_acm = False
    
    # Look for explicit ACM references
    if 'acm' in text_lower or 'association for computing machinery' in text_lower:
        is_acm = True
    
    # Look for ACM copyright/permission statements
    if 'permission to make digital or hard copies' in text_lower:
        is_acm = True
    
    # Look for ACM ISBN pattern
    if 'acm 978-' in text_lower:
        is_acm = True
    
    # Check for known ACM venues if we find venue indicators
    if not is_acm:
        # Common ACM conference patterns
        acm_indicators = [
            'proceedings of the acm',
            'acm conference',
            'acm sigchi',
            'acm transactions'
        ]
        
        for indicator in acm_indicators:
            if indicator in text_lower:
                is_acm = True
                break
    
    if is_acm:
        citation_count = citation_dict[title]
        acm_citations_list.append({
            'title': title,
            'citation_count': citation_count
        })
        acm_count += 1

print(f"Found {acm_count} ACM papers with citations in 2018")

# Calculate statistics
if acm_citations_list:
    total_citations = sum(p['citation_count'] for p in acm_citations_list)
    avg_citations = total_citations / len(acm_citations_list)
    
    result = {
        'average_citation_count': round(avg_citations, 2),
        'total_acm_papers': len(acm_citations_list),
        'total_citations': total_citations
    }
    
    print(f"Average citations: {avg_citations:.2f}")
    print(f"Total ACM papers: {len(acm_citations_list)}")
    print(f"Total citations: {total_citations}")
    
    # Show top papers
    print("\nTop ACM papers by citation count:")
    sorted_papers = sorted(acm_citations_list, key=lambda x: x['citation_count'], reverse=True)
    for i, paper in enumerate(sorted_papers[:10]):
        print(f"  {i+1}. {paper['title'][:60]}... - {paper['citation_count']} citations")
else:
    result = {
        'average_citation_count': 0,
        'total_acm_papers': 0,
        'total_citations': 0
    }
    print("No ACM papers found with citations in 2018")

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'average_citation_count': 68.5, 'total_acm_papers': 2, 'total_citations': 137}}

exec(code, env_args)
