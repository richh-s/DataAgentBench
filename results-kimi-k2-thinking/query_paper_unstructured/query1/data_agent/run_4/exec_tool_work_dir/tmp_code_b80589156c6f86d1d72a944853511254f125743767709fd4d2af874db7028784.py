code = """import json
import re

# Load the full citation data
citations_path = locals()['var_functions.query_db:26']
with open(citations_path, 'r') as f:
    all_citations = json.load(f)

# Look for food-related papers by checking titles for food keywords
food_keywords = [r'\bfood\b', r'\bdiet\b', r'\bdietary\b', r'\beat\b', r'\beating\b', r'\bmeal\b']

food_papers = []

for citation in all_citations:
    title = citation['title']
    total_citations = int(citation['total_citations'])
    
    # Check if title contains food-related terms
    title_lower = title.lower()
    if any(keyword.strip('\\b') in title_lower for keyword in food_keywords):
        paper_info = {
            'title': title,
            'total_citations': total_citations
        }
        food_papers.append(paper_info)

# Calculate total citations
print('Number of food domain papers: ' + str(len(food_papers)))
print('\nFood domain papers found:')
for paper in food_papers:
    print('- ' + paper['title'] + ' (' + str(paper['total_citations']) + ' citations)')

total_citation_count = sum([paper['total_citations'] for paper in food_papers])
print('\nTotal citation count for food domain papers: ' + str(total_citation_count))

print('__RESULT__:')
print(json.dumps({'total_citations': total_citation_count, 'paper_count': len(food_papers)}))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:18': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'], 'var_functions.query_db:20': [{'title': 'A Lived Informatics Model of Personal Informatics', 'total_citations': '390'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'total_citations': '220'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': '266'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': [], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation'], 'var_functions.query_db:32': [{'title': 'A Lived Informatics Model of Personal Informatics', 'total_citations': '390'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'total_citations': '220'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': '265'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': '266'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'total_citations': '452'}]}

exec(code, env_args)
