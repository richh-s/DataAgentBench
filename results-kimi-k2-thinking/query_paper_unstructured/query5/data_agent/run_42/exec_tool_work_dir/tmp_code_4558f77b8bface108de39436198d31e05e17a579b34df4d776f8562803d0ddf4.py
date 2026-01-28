code = """import json
import os

# Load 2020 citations data
citations_key = 'var_functions.query_db:0'
citations_data = locals()[citations_key]
if isinstance(citations_data, str) and os.path.exists(citations_data):
    with open(citations_data, 'r') as f:
        citations_2020 = json.load(f)
else:
    citations_2020 = citations_data

# Sum all citation counts
total_citations = 0
for citation in citations_2020:
    count = int(citation.get('citation_count', 0))
    total_citations += count

result = {
    'total_2020_citations_all_papers': total_citations,
    'number_of_cited_papers': len(citations_2020)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 188, 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': 'Data loaded successfully', 'var_functions.execute_python:14': {'chi_papers_total': 5, 'chi_papers_cited': 4, 'total_citations_2020': 243, 'sample_matched_titles': ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'A Lived Informatics Model of Personal Informatics', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}, 'var_functions.execute_python:18': {'chi_papers_total': 0, 'chi_papers_cited_2020': 0, 'total_citations_2020': 0}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': {'chi_papers': 0, 'chi_cited_2020': 0, 'total_citations': 0}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:34': {'chi_papers_identified': 0, 'chi_papers_cited_in_2020': 0, 'total_citation_count_2020': 0}, 'var_functions.execute_python:36': {'target_paper_found': True, 'target_paper_citations': 16, 'sample_matches': {'A Lived Informatics Model of Personal Informatics': 77, 'A Trip to the Moon: Personalized Animated Movies for Self-reflection': 98, 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation': 52}}, 'var_functions.execute_python:38': {'total_2020_citations': 188, 'total_papers': 5}}

exec(code, env_args)
