code = """import json
import os

# Load the 2020 citations
citations_key = 'var_functions.query_db:0'
citations_data = locals()[citations_key]
if isinstance(citations_data, str) and os.path.exists(citations_data):
    with open(citations_data, 'r') as f:
        citations_2020 = json.load(f)
else:
    citations_2020 = citations_data

# Check if specific CHI paper from sample is in citations
target_title = "A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App"

found = False
citation_count = 0
for citation in citations_2020:
    if citation.get('title', '') == target_title:
        found = True
        citation_count = int(citation.get('citation_count', 0))
        break

print('Paper found:', found)
print('Citation count:', citation_count)

# Let's check some other sample citations from the preview
sample_titles = [
    "A Lived Informatics Model of Personal Informatics",
    "A Trip to the Moon: Personalized Animated Movies for Self-reflection",
    "ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation"
]

results = {}
for title in sample_titles:
    for citation in citations_2020:
        if citation.get('title', '') == title:
            results[title] = int(citation.get('citation_count', 0))
            break

print('Sample matches:', results)

result = {
    'target_paper_found': found,
    'target_paper_citations': citation_count,
    'sample_matches': results
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 188, 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': 'Data loaded successfully', 'var_functions.execute_python:14': {'chi_papers_total': 5, 'chi_papers_cited': 4, 'total_citations_2020': 243, 'sample_matched_titles': ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'A Lived Informatics Model of Personal Informatics', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}, 'var_functions.execute_python:18': {'chi_papers_total': 0, 'chi_papers_cited_2020': 0, 'total_citations_2020': 0}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': {'chi_papers': 0, 'chi_cited_2020': 0, 'total_citations': 0}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:34': {'chi_papers_identified': 0, 'chi_papers_cited_in_2020': 0, 'total_citation_count_2020': 0}}

exec(code, env_args)
