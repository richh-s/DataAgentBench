code = """import json

# Load the citations data
file_path = locals()['var_functions.query_db:2']
print(f'Loading citations from: {file_path}')

with open(file_path, 'r') as f:
    citations = json.load(f)

print(f'Total citation records: {len(citations)}')

# Access the food paper titles from previous result
food_result = locals()['var_functions.execute_python:14']
food_paper_titles = food_result['food_paper_titles']

print(f'Food paper titles to search for: {len(food_paper_titles)}')
for title in food_paper_titles:
    print(f'  - {title}')

# Find citations for food papers
food_citations = []
for citation in citations:
    if citation['title'] in food_paper_titles:
        food_citations.append(citation)

print(f'Found {len(food_citations)} citation records for food papers')

# Calculate total citation count
total_citations = 0
if food_citations:
    for citation in food_citations:
        count = int(citation['citation_count'])
        total_citations += count
        print(f"  {citation['title']}: {count} citations (year {citation['citation_year']})")

result = {
    'food_citations': food_citations,
    'total_citation_count': total_citations,
    'food_paper_count': len(food_paper_titles),
    'citation_record_count': len(food_citations)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:10': {'food_paper_titles': [], 'count': 0}, 'var_functions.execute_python:12': {'food_paper_titles': [], 'count': 0}, 'var_functions.execute_python:14': {'food_paper_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation'], 'count': 5, 'food_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'keyword': 'food'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'keyword': 'food'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'keyword': 'eating'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'keyword': 'food'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'keyword': 'eating'}]}}

exec(code, env_args)
