code = """import json
import re

# Read all paper documents
papers_file = globals().get('var_functions.query_db:22')
with open(papers_file, 'r') as f:
    all_papers = json.load(f)

# Read citations for 2020
citations_file = globals().get('var_functions.query_db:2')
with open(citations_file, 'r') as f:
    citations_2020 = json.load(f)

# Create a mapping of titles to citation counts
citation_map = {}
for citation in citations_2020:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    citation_map[title] = count

# Identify CHI papers and sum their citations
total_citations = 0
matched_papers = []
unmatched_chi_papers = []

for paper in all_papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title from filename
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    
    # Check if CHI venue appears in text
    chi_patterns = [
        r'CHI\s*\'\d{2}',
        r'CHI\s*\d{4}',
        r'CHI\s+Conference',
        r'Proceedings of CHI',
        r'CHI\s+\d{2},',
        r'\bCHI\s*\d{2}\b',
        r'\bCHI\b'
    ]
    
    is_chi = False
    for pattern in chi_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            is_chi = True
            break
    
    if is_chi:
        if title in citation_map:
            count = citation_map[title]
            total_citations += count
            matched_papers.append({'title': title, 'citations': count})
        else:
            unmatched_chi_papers.append(title)

print('__RESULT__:')
print(json.dumps({
    'total_chi_citations_2020': total_citations,
    'chi_papers_found': len(all_papers),
    'chi_papers_with_citations': len(matched_papers),
    'chi_papers_without_citations': len(unmatched_chi_papers),
    'matched_papers': matched_papers,
    'unmatched_papers': unmatched_chi_papers
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'type': "<class 'str'>", 'is_string': True, 'is_list': False}, 'var_functions.execute_python:10': {'total_citations_2020': 188, 'sample_titles': ['Sundroid: Solar Radiation Awareness with Smartphones', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'Why We Use and Abandon Smart Devices', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application"]}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_chi_citations_2020': 243, 'chi_papers_count': 5, 'matched_citations_count': 4, 'sample_matched': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': 16}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': 77}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': 98}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citation_count': 52}]}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.list_db:20': ['paper_docs'], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'total_citations_2020': 188, 'total_papers_in_db': 5}}

exec(code, env_args)
