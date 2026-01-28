code = """import json

# Paper data from physical activity & 2016 search
papers_2016_pa = [
    {"title": "A Trip to the Moon: Personalized Animated Movies for Self-reflection", "domains": ["physical activity", "mental", "sleep"]},
    {"title": "A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App", "domains": ["physical activity", "mental", "food", "location"]}
]

# Citation data from database (already loaded as list)
citations = locals()['var_functions.query_db:20']

# Group citations by title
citation_totals = {}
for citation in citations:
    title = citation['title']
    count = int(citation['citation_count'])
    
    if title not in citation_totals:
        citation_totals[title] = 0
    citation_totals[title] += count

# Create final results with title and total citation count
result = []
for paper in papers_2016_pa:
    title = paper['title']
    total_citations = citation_totals.get(title, 0)
    result.append({
        'title': title,
        'total_citation_count': total_citations
    })

output = json.dumps(result, indent=2)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:18': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}], 'var_functions.query_db:20': [{'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '48', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '49', 'citation_year': '2021'}, {'id': '49', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '11', 'citation_year': '2022'}, {'id': '50', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '71', 'citation_year': '2023'}, {'id': '51', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '38', 'citation_year': '2024'}, {'id': '52', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '81', 'citation_year': '2025'}, {'id': '147', 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': '65', 'citation_year': '2019'}, {'id': '148', 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': '98', 'citation_year': '2020'}, {'id': '149', 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': '23', 'citation_year': '2021'}, {'id': '150', 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': '65', 'citation_year': '2022'}, {'id': '151', 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': '14', 'citation_year': '2023'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'domains': ['physical activity', 'mental', 'sleep']}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'domains': ['physical activity', 'mental', 'food', 'location']}]}

exec(code, env_args)
