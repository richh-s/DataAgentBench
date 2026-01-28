code = """import json

# Get the data from storage
citations_data = locals()['var_functions.query_db:2']
print('Type of citations_data:', type(citations_data))

# If it's a file path, load the JSON
if isinstance(citations_data, str):
    with open(citations_data, 'r') as f:
        citations = json.load(f)
    print('Loaded citations from file')
else:
    citations = citations_data
    print('Used citations directly')

print('Number of citations:', len(citations))
if citations and len(citations) > 0:
    print('First citation keys:', list(citations[0].keys()))
    print('First citation:', citations[0])

# Get paper documents
paper_docs_data = locals()['var_functions.query_db:22']
print('\nType of paper_docs_data:', type(paper_docs_data))

if isinstance(paper_docs_data, str):
    with open(paper_docs_data, 'r') as f:
        paper_docs = json.load(f)
    print('Loaded paper_docs from file')
else:
    paper_docs = paper_docs_data
    print('Used paper_docs directly')

print('Number of papers:', len(paper_docs))
if paper_docs and len(paper_docs) > 0:
    print('First paper keys:', list(paper_docs[0].keys()))
    print('First paper filename:', paper_docs[0].get('filename'))

# Now process the data
total_citations = 0
food_paper_count = 0

# Build a dictionary of citations by title for faster lookup
citation_dict = {}
for cit in citations:
    title = cit.get('title', '')
    count = int(cit.get('citation_count', 0))
    if title in citation_dict:
        citation_dict[title] += count
    else:
        citation_dict[title] = count

print('\nNumber of unique citation titles:', len(citation_dict))

# Check each paper to see if it's about food
for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    text = doc.get('text', '').lower()
    
    # Check if this is a food paper
    if 'food' in text or 'eating' in text or 'diet' in text:
        food_paper_count += 1
        # Check if we have citations for this paper
        if title in citation_dict:
            paper_citations = citation_dict[title]
            total_citations += paper_citations
            print(f"Found food paper: {title[:50]}... - Citations: {paper_citations}")

print('\nTotal food papers found:', food_paper_count)
print('Total citations from matched food papers:', total_citations)

# Also check for fuzzy matches if we didn't find exact matches
if total_citations == 0:
    from difflib import get_close_matches
    paper_titles = [title.replace('.txt', '') for title in [doc.get('filename', '') for doc in paper_docs]]
    
    food_papers = []
    for i, doc in enumerate(paper_docs):
        text = doc.get('text', '').lower()
        if 'food' in text or 'eating' in text or 'diet' in text:
            food_papers.append(paper_titles[i])
    
    citation_titles = list(citation_dict.keys())
    
    for food_title in food_papers:
        matches = get_close_matches(food_title, citation_titles, n=1, cutoff=0.8)
        if matches:
            total_citations += citation_dict[matches[0]]
            food_paper_count += 1
    
    print('\nAfter fuzzy matching:')
    print('Total citations:', total_citations)

result = {"total_citation_count": total_citations}
print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:28': {'total_citation_count': 0, 'matched_papers': 0}}

exec(code, env_args)
