code = """import json

# Load citations from the earlier query
citations_path = locals()['var_functions.query_db:10']
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Load food papers from the latest query
food_papers_path = locals()['var_functions.query_db:36']
with open(food_papers_path, 'r') as f:
    food_papers = json.load(f)

print(f'Loaded {len(citations)} citation records')
print(f'Loaded {len(food_papers)} food papers')

# Build citation dictionary (sum across all years)
citation_dict = {}
for cite in citations:
    title = cite.get('title', '').strip().lower()
    count = int(cite.get('citation_count', 0))
    if title:
        citation_dict[title] = citation_dict.get(title, 0) + count

print(f'Unique papers with citations: {len(citation_dict)}')

# Sum citations for food papers
total_citations = 0
matched_papers = []

for paper in food_papers:
    filename = paper.get('filename', '').replace('.txt', '')
    title_lower = filename.lower()
    
    if title_lower in citation_dict:
        count = citation_dict[title_lower]
        total_citations += count
        matched_papers.append((filename, count))

# Sort by citation count
matched_papers.sort(key=lambda x: x[1], reverse=True)

print(f'Food papers with citations: {len(matched_papers)}')
print(f'Total citation count: {total_citations}')

result = {
    'total_food_papers': len(food_papers),
    'food_papers_with_citations': len(matched_papers),
    'total_citation_count': total_citations,
    'paper_details': [{'title': t, 'citations': c} for t, c in matched_papers]
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}], 'var_functions.list_db:14': ['paper_docs'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'total_food_papers': 4, 'papers_with_citations': 4, 'total_citation_count': 1328, 'top_papers': [['ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 452], ['A Lived Informatics Model of Personal Informatics', 390], ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 266], ['A Stage-based Model of Personal Informatics Systems', 220]]}, 'var_functions.execute_python:22': {'total_food_domain_papers_identified': 0, 'papers_with_citation_data': 0, 'total_citation_count': 0, 'papers': []}, 'var_functions.execute_python:26': {'total_food_papers': 0, 'papers_with_data': 0, 'total_citations': 0, 'papers': []}, 'var_functions.execute_python:30': {'status': 'debug_complete'}, 'var_functions.execute_python:34': {'count': 0, 'total_citations': 0}, 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
