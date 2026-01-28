code = """import json

# Load the 2018 citations data
citations_file = locals()['var_functions.query_db:0']
if isinstance(citations_file, str):
    with open(citations_file, 'r') as f:
        citations_data = json.load(f)
else:
    citations_data = citations_file

# Load the paper documents
papers_file = locals()['var_functions.query_db:5']
if isinstance(papers_file, str):
    with open(papers_file, 'r') as f:
        papers_data = json.load(f)
else:
    papers_data = papers_file

# Create a list of available paper titles from filenames
paper_titles = []
for paper in papers_data:
    filename = paper.get('filename', '')
    if filename:
        title = filename.replace('.txt', '').strip().lower()
        paper_titles.append(title)

print('Total citations in 2018:', len(citations_data))
print('Total papers available:', len(papers_data))
print('Paper titles from files:', paper_titles)

# Check which papers have ACM in their text
acm_paper_indices = []
for i, paper in enumerate(papers_data):
    text = paper.get('text', '').lower()
    if 'acm' in text:
        acm_paper_indices.append(i)

print('Papers with ACM found:', acm_paper_indices)

# Build title to citation count mapping
citation_map = {}
for c in citations_data:
    title = c['title'].strip().lower()
    count = int(c['citation_count'])
    citation_map[title] = count

print('Sample citation titles:', list(citation_map.keys())[:3])

# Try to match ACM papers with citations by comparing titles
acm_citation_counts = []
for idx in acm_paper_indices:
    paper_title = paper_titles[idx]
    print('Checking ACM paper:', paper_title)
    
    # Look for exact or partial matches in citation titles
    for citation_title, count in citation_map.items():
        if paper_title == citation_title or paper_title in citation_title or citation_title in paper_title:
            acm_citation_counts.append(count)
            print('  Matched with:', citation_title, 'count:', count)
            break

print('ACM papers matched with 2018 citations:', len(acm_citation_counts))

if acm_citation_counts:
    average = sum(acm_citation_counts) / len(acm_citation_counts)
    total = sum(acm_citation_counts)
else:
    average = 0
    total = 0

result = {
    'acm_papers_with_citations': len(acm_citation_counts),
    'average_citation_count': average,
    'total_acm_citations': total,
    'total_2018_citations': len(citations_data)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:18': {'acm_papers_count': 2, 'total_2018_citations': 158, 'missing_papers': 156, 'average_citations': 68.5, 'total_citations_for_acm_papers': 137}, 'var_functions.execute_python:24': {'total_citations': 158, 'total_papers': 5, 'papers_dict_size': 5, 'sample_citation_title': 'expense control: a gamified, semi-automated, crowd-based approach for receipt capturing', 'sample_match_found': False}}

exec(code, env_args)
