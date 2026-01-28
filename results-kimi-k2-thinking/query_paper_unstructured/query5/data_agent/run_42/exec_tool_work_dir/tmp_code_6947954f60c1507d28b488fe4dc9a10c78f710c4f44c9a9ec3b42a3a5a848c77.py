code = """import json
import os

# Load data
citations_key = 'var_functions.query_db:0'
citations_data = locals()[citations_key]
if isinstance(citations_data, str) and os.path.exists(citations_data):
    with open(citations_data, 'r') as f:
        citations_2020 = json.load(f)
else:
    citations_2020 = citations_data

chi_key = 'var_functions.query_db:26'
chi_data = locals()[chi_key]
if isinstance(chi_data, str) and os.path.exists(chi_data):
    with open(chi_data, 'r') as f:
        chi_docs = json.load(f)
else:
    chi_docs = chi_data

# Extract CHI paper titles
chi_titles = set()

for doc in chi_docs:
    filename = doc.get('filename', '')
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    text = doc.get('text', '')
    text_upper = text.upper()
    
    # Simple check for CHI conference indicators
    if text_upper.find('CHI') >= 0:
        # Look for common conference patterns (first 500 chars)
        header = text_upper[:500]
        if any(x in header for x in ['PROCEEDINGS', 'CONFERENCE', 'ACM']):
            chi_titles.add(title)

# Sum citations for CHI papers
total_citations = 0
matched_papers = 0

for citation in citations_2020:
    citation_title = citation.get('title', '')
    if citation_title in chi_titles:
        count = int(citation.get('citation_count', 0))
        total_citations += count
        matched_papers += 1

result = {
    'chi_papers': len(chi_titles),
    'chi_cited_2020': matched_papers,
    'total_citations': total_citations
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 188, 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': 'Data loaded successfully', 'var_functions.execute_python:14': {'chi_papers_total': 5, 'chi_papers_cited': 4, 'total_citations_2020': 243, 'sample_matched_titles': ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'A Lived Informatics Model of Personal Informatics', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}, 'var_functions.execute_python:18': {'chi_papers_total': 0, 'chi_papers_cited_2020': 0, 'total_citations_2020': 0}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
