code = """import json
import re

# Load citations from 2020
citations_file_path = locals()['var_functions.query_db:12']
with open(citations_file_path, 'r') as f:
    citations_data = json.load(f)

print('Total citations in 2020:', len(citations_data))

# Load all papers
papers_file_path = locals()['var_functions.query_db:24']
with open(papers_file_path, 'r') as f:
    papers_data = json.load(f)

print('Total papers in database:', len(papers_data))

# Identify CHI papers from the full dataset
chi_papers = []
chi_pattern = re.compile(r'CHI', re.IGNORECASE)

for paper in papers_data:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    if chi_pattern.search(text):
        title = filename.replace('.txt', '')
        chi_papers.append({'title': title, 'filename': filename})

print('CHI papers found:', len(chi_papers))

# Create a set of CHI paper titles for matching
chi_titles_set = set()
chi_titles_map = {}
for paper in chi_papers:
    title_clean = paper['title'].strip().lower()
    chi_titles_set.add(title_clean)
    chi_titles_map[title_clean] = paper['title']

# Match citations with CHI papers
matched_citations = []
total_citations = 0

for citation in citations_data:
    cit_title = citation.get('title', '').strip()
    cit_count = int(citation.get('citation_count', 0))
    cit_title_clean = cit_title.lower()
    
    if cit_title_clean in chi_titles_set:
        matched_paper_title = chi_titles_map[cit_title_clean]
        matched_citations.append({
            'title': cit_title,
            'matched_paper': matched_paper_title,
            'count': cit_count
        })
        total_citations += cit_count
        print('Match found:', cit_title, '->', cit_count, 'citations')

print('\nTotal matched CHI papers:', len(matched_citations))
print('Total citation count:', total_citations)

# Prepare final result
result = {
    'total_chi_papers_matched': len(matched_citations),
    'total_citation_count': total_citations,
    'chi_papers_found': len(chi_papers)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'status': 'ready_to_query_mongodb', 'citation_count': 188}, 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'status': 'papers_loaded', 'count': 99}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:20': {'matched_citations': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': 16}, {'title': 'A Lived Informatics Model of Personal Informatics', 'count': 77}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'count': 98}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'count': 52}], 'count': 4}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
