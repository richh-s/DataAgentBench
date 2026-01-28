code = """import json
import os

# Load citation data for 2018
citation_file = locals()['var_functions.query_db:0']
citation_data = []
with open(citation_file, 'r') as f:
    content = f.read().strip()
    # Handle JSON array format
    if content.startswith('['):
        citation_data = json.loads(content)
    else:
        # Handle line-delimited JSON
        for line in content.split('\n'):
            line = line.strip()
            if line and line != '' and line != 'null':
                try:
                    citation_data.append(json.loads(line))
                except:
                    continue

# Load paper documents
paper_file = locals()['var_functions.query_db:2']
paper_data = []
with open(paper_file, 'r') as f:
    content = f.read().strip()
    if content.startswith('['):
        paper_data = json.loads(content)
    else:
        for line in content.split('\n'):
            line = line.strip()
            if line and line != '' and line != 'null':
                try:
                    paper_data.append(json.loads(line))
                except:
                    continue

# Find ACM papers
acm_titles = set()
for paper in paper_data:
    text = paper.get('text', '').lower()
    if 'acm' in text or 'association for computing machinery' in text:
        filename = paper.get('filename', '')
        if filename:
            title = filename.replace('.txt', '')
            acm_titles.add(title)

# Match with citations
citation_dict = {item['title']: int(item['citation_count']) for item in citation_data}
matched_citations = [citation_dict[title] for title in acm_titles if title in citation_dict]

# Calculate average
avg_citations = sum(matched_citations) / len(matched_citations) if matched_citations else 0

result = {
    'average_citation_count': avg_citations,
    'acm_papers_matched': len(matched_citations),
    'total_acm_papers': len(acm_titles),
    'total_citations_2018': len(citation_data)
}

print('__RESULT__')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'status': 'files_checked'}}

exec(code, env_args)
