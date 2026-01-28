code = """import json

# Reload all the data to verify our findings
citations_file = locals()['var_functions.query_db:0']
if isinstance(citations_file, str):
    with open(citations_file, 'r') as f:
        citations_data = json.load(f)
else:
    citations_data = citations_file

papers_file = locals()['var_functions.query_db:5']
if isinstance(papers_file, str):
    with open(papers_file, 'r') as f:
        papers_data = json.load(f)
else:
    papers_data = papers_file

print('Total 2018 citations:', len(citations_data))
print('Total papers in collection:', len(papers_data))

# Let's look at the ACM papers we found
acm_papers_info = []
for i, paper in enumerate(papers_data):
    text = paper.get('text', '')
    if 'acm' in text.lower():
        filename = paper.get('filename', '')
        title = filename.replace('.txt', '')
        acm_papers_info.append({
            'index': i,
            'filename': filename,
            'title': title
        })

print('ACM papers found in collection:')
for info in acm_papers_info:
    print('  ', info)

# Map all papers by filename
papers_by_filename = {p.get('filename', '').replace('.txt', '').strip().lower(): p for p in papers_data}

# Check which citations correspond to our ACM papers
matched_citations = []
for citation in citations_data:
    citation_title = citation['title'].strip().lower()
    
    # Check if this citation matches any of our ACM papers
    for info in acm_papers_info:
        paper_title = info['title'].strip().lower()
        if paper_title == citation_title or citation_title in paper_title or paper_title in citation_title:
            matched_citations.append({
                'title': citation['title'],
                'count': int(citation['citation_count'])
            })
            break

print('Matched ACM citations:')
for mc in matched_citations:
    print('  ', mc)

# Calculate the average
if matched_citations:
    total_count = sum(mc['count'] for mc in matched_citations)
    average = total_count / len(matched_citations)
    print('Total ACM papers matched:', len(matched_citations))
    print('Average citation count:', average)
else:
    average = 0
    print('No ACM papers matched with citations')

result = {
    'acm_papers_identified': len(acm_papers_info),
    'acm_citations_matched': len(matched_citations),
    'average_citation_count': average,
    'matched_papers_details': matched_citations
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:18': {'acm_papers_count': 2, 'total_2018_citations': 158, 'missing_papers': 156, 'average_citations': 68.5, 'total_citations_for_acm_papers': 137}, 'var_functions.execute_python:24': {'total_citations': 158, 'total_papers': 5, 'papers_dict_size': 5, 'sample_citation_title': 'expense control: a gamified, semi-automated, crowd-based approach for receipt capturing', 'sample_match_found': False}, 'var_functions.execute_python:30': {'acm_papers_with_citations': 2, 'average_citation_count': 68.5, 'total_acm_citations': 137, 'total_2018_citations': 158}}

exec(code, env_args)
