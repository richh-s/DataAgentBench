code = """import json
import re

# Load citation data
citations_result = var_functions.query_db:2
if isinstance(citations_result, str):
    with open(citations_result, 'r') as f:
        citations_list = json.load(f)
else:
    citations_list = citations_result

# Load paper documents
papers_result = var_functions.query_db:5
if isinstance(papers_result, str):
    with open(papers_result, 'r') as f:
        papers_list = json.load(f)
else:
    papers_list = papers_result

# Convert citation counts to integers
for citation in citations_list:
    citation['citation_count'] = int(citation['citation_count'])

# Create mapping from title to citation count
citations_map = {}
for citation in citations_list:
    citations_map[citation['title']] = citation['citation_count']

# Function to extract venue from paper text
def extract_venue_from_text(text):
    text_sample = text[:3000]
    
    if 'CHI' in text_sample or 'Proceedings of the ACM Conference on Human Factors' in text_sample:
        return 'CHI'
    elif 'UbiComp' in text_sample or 'Ubiquitous Computing' in text_sample:
        return 'Ubicomp'
    elif 'CSCW' in text_sample:
        return 'CSCW'
    elif 'DIS' in text_sample or 'Designing Interactive Systems' in text_sample:
        return 'DIS'
    elif 'WWW' in text_sample:
        return 'WWW'
    elif 'IUI' in text_sample:
        return 'IUI'
    elif 'PervasiveHealth' in text_sample:
        return 'PervasiveHealth'
    elif 'TEI' in text_sample:
        return 'TEI'
    elif 'OzCHI' in text_sample:
        return 'OzCHI'
    
    return None

# Create mapping from paper title to venue
venue_map = {}
for paper in papers_list:
    title = paper['filename'].replace('.txt', '')
    venue = extract_venue_from_text(paper.get('text', ''))
    if venue:
        venue_map[title] = venue

# Find CHI papers and sum their 2020 citations
chi_citations_total = 0
chi_papers_matched = 0
results = []

for title, citation_count in citations_map.items():
    if title in venue_map and venue_map[title] == 'CHI':
        chi_citations_total += citation_count
        chi_papers_matched += 1
        results.append({'title': title, 'citations': citation_count})

# Sort results by citation count (descending)
results.sort(key=lambda x: x['citations'], reverse=True)

# Prepare output
output_result = {
    'total_chi_citations': chi_citations_total,
    'number_of_chi_papers': chi_papers_matched,
    'top_chi_papers': results[:10]
}

print('__RESULT__:')
print(json.dumps(output_result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
