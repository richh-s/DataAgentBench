code = """import json
from collections import defaultdict

# Load the 2018 citations data
citations_file = locals()['var_functions.query_db:0']
citations_2018 = []
with open(citations_file, 'r') as f:
    citations_2018 = json.load(f)

# Load ACM papers list
acm_papers = locals()['var_functions.execute_python:12']['acm_papers']

# Create a dictionary of ACM paper titles for lookup
acm_titles = {paper['title'].lower().strip(): paper for paper in acm_papers}

# Match citations with ACM papers
total_citations = 0
matched_count = 0
matched_papers = []

for citation in citations_2018:
    citation_title = citation['title'].lower().strip()
    if citation_title in acm_titles:
        citation_count = int(citation['citation_count'])
        total_citations += citation_count
        matched_count += 1
        matched_papers.append({
            'title': citation['title'],
            'citation_count': citation_count
        })

# Calculate average
average_citations = total_citations / matched_count if matched_count > 0 else 0

result = {
    'average_citation_count': round(average_citations, 2),
    'total_acm_papers_cited': matched_count,
    'total_citations': total_citations,
    'matched_papers': matched_papers
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.execute_python:10': {'citations_2018_count': 158, 'paper_docs_count': 5}, 'var_functions.execute_python:12': {'acm_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'publisher': 'ACM', 'year': 2015, 'venue': '2015', 'id': '694f5530284b10b11dc0a869'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'publisher': 'ACM', 'year': 2009, 'venue': '1521', 'id': '694f5530284b10b11dc0a86a'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'publisher': 'ACM', 'year': None, 'venue': 'CHI', 'id': '694f5530284b10b11dc0a86b'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'publisher': 'ACM', 'year': 2014, 'venue': '2019', 'id': '694f5530284b10b11dc0a86c'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'publisher': 'ACM', 'year': 2011, 'venue': 'DIS', 'id': '694f5530284b10b11dc0a86d'}], 'acm_count': 5}}

exec(code, env_args)
