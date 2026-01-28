code = """import json
import re

# Load the citation data for 2018
with open('var_functions.query_db:2.json', 'r') as f:
    citations_2018 = json.load(f)

# Load the paper documents
with open('var_functions.query_db:5.json', 'r') as f:
    paper_docs = json.load(f)

print(f"Number of citations in 2018: {len(citations_2018)}")
print(f"Number of paper documents: {len(paper_docs)}")

# Preview the data structure
print("\nFirst few citations:")
for i, cite in enumerate(citations_2018[:3]):
    print(f"  {i+1}. {cite['title']} - {cite['citation_count']} citations")

print("\nFirst few paper documents:")
for i, doc in enumerate(paper_docs[:3]):
    print(f"  {i+1}. {doc['filename']}")

# Convert citation data to a dict for easier lookup
citation_dict = {cite['title']: int(cite['citation_count']) for cite in citations_2018}

print(f"\nCreated citation dictionary with {len(citation_dict)} entries")
print(f"Sample entries: {list(citation_dict.items())[:3]}")

# Process paper documents to extract title, source, and other info
papers_with_sources = []

for doc in paper_docs:
    # Extract title from filename
    filename = doc['filename']
    if filename.endswith('.txt'):
        title = filename[:-4]  # Remove .txt extension
    else:
        title = filename
    
    # Extract text content
    text = doc.get('text', '')
    
    # Initialize source as empty
    source = ''
    
    # Look for ACM mentions in the text (common patterns)
    # Look for ACM copyright, ACM references, ACM Digital Library, etc.
    if re.search(r'ACM', text, re.IGNORECASE):
        source = 'ACM'
    elif re.search(r'Association for Computing Machinery', text, re.IGNORECASE):
        source = 'ACM'
    
    # Also check for venue information which might indicate ACM
    # Common ACM venues: CHI, Ubicomp, CSCW, DIS, TEI, IUI, etc.
    acm_venues = ['CHI', 'Ubicomp', 'CSCW', 'DIS', 'TEI', 'IUI', 'WWW', 'ISS']
    for venue in acm_venues:
        if re.search(r'\b' + venue + r'\b', text):
            # Check if it's an ACM conference by looking for ACM in the text
            if re.search(r'ACM', text, re.IGNORECASE):
                source = 'ACM'
                break
    
    papers_with_sources.append({
        'title': title,
        'source': source,
        'text_snippet': text[:500]  # First 500 chars for debugging
    })

print(f"\nProcessed {len(papers_with_sources)} papers")
print("\nSample papers with sources:")
for i, paper in enumerate(papers_with_sources[:5]):
    print(f"  {i+1}. {paper['title']}")
    print(f"     Source: {paper['source']}")
    print(f"     Snippet: {paper['text_snippet'][:100]}...")

# Now match papers with citations and filter for ACM papers
acm_citations = []

for paper in papers_with_sources:
    title = paper['title']
    source = paper['source']
    
    # Check if this paper has citations in 2018 and is from ACM
    if title in citation_dict and source == 'ACM':
        acm_citations.append({
            'title': title,
            'citation_count': citation_dict[title],
            'source': source
        })

print(f"\nFound {len(acm_citations)} ACM papers with citations in 2018")

# Calculate average citation count
if acm_citations:
    total_citations = sum(paper['citation_count'] for paper in acm_citations)
    avg_citations = total_citations / len(acm_citations)
    
    print(f"\nTotal citations for ACM papers: {total_citations}")
    print(f"Number of ACM papers: {len(acm_citations)}")
    print(f"Average citation count: {avg_citations:.2f}")
    
    # Show some examples
    print("\nTop 5 ACM papers by citation count:")
    acm_citations_sorted = sorted(acm_citations, key=lambda x: x['citation_count'], reverse=True)
    for i, paper in enumerate(acm_citations_sorted[:5]):
        print(f"  {i+1}. {paper['title']} - {paper['citation_count']} citations")
else:
    print("No ACM papers found with citations in 2018")
    avg_citations = 0

result = {
    'average_citation_count': round(avg_citations, 2),
    'total_acm_papers': len(acm_citations),
    'total_citations': sum(paper['citation_count'] for paper in acm_citations) if acm_citations else 0
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
