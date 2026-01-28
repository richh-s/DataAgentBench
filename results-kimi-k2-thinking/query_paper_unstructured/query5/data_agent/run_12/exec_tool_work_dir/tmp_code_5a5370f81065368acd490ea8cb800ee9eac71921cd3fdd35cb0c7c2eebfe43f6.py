code = """import json
import re

# Load the files
citations_file = locals()['var_functions.query_db:0']
chi_papers_file = locals()['var_functions.query_db:19']

with open(citations_file, 'r') as f:
    citations = json.load(f)

with open(chi_papers_file, 'r') as f:
    chi_papers = json.load(f)

# Extract CHI paper titles
covered_titles = [paper['filename'].replace('.txt', '') for paper in chi_papers]

# Find 2020 citations for CHI papers 
chi_citations_2020 = []
total_citations = 0

for citation in citations:
    citation_title = citation['title']
    if citation_title in covered_titles:
        count = int(citation['citation_count'])
        chi_citations_2020.append({
            'title': citation_title,
            'citation_count': count
        })
        total_citations += count

print('__RESULT__:')
print(json.dumps({
    'total_citations_2020': total_citations,
    'chi_papers_count': len(chi_citations_2020),
    'details': chi_citations_2020
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.execute_python:6': {'citations_count': 188, 'papers_count': 5}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:19': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}]}

exec(code, env_args)
