code = """import json
import re

# Load all papers from MongoDB
paper_data_path = locals()['var_functions.query_db:22']
with open(paper_data_path, 'r') as f:
    all_papers = json.load(f)

print('Total papers loaded:', len(all_papers))

# Process papers to extract key information
papers_2016_physical_activity = []

for paper in all_papers:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    
    # Extract title
    title = filename.replace('.txt', '') if filename else ''
    
    # Check if paper is from 2016
    year_match = re.search(r'2016', paper.get('text', ''))
    if not year_match:
        continue
    
    # Check if in physical activity domain
    has_physical_activity = 'physical activity' in text
    
    # Extract other domains if any
    domains = []
    if has_physical_activity:
        domains.append('physical activity')
    if 'mental' in text:
        domains.append('mental')
    if 'sleep' in text:
        domains.append('sleep')
    if 'food' in text:
        domains.append('food')
    if 'finances' in text:
        domains.append('finances')
    if 'location' in text:
        domains.append('location')
    
    if has_physical_activity:
        papers_2016_physical_activity.append({
            'title': title,
            'domains': domains
        })

print('Papers from 2016 in physical activity domain:', len(papers_2016_physical_activity))

for paper in papers_2016_physical_activity:
    print(f"- Title: {paper['title']}")
    print(f"  Domains: {paper['domains']}")

result = json.dumps(papers_2016_physical_activity)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:18': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}], 'var_functions.query_db:20': [{'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '48', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '49', 'citation_year': '2021'}, {'id': '49', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '11', 'citation_year': '2022'}, {'id': '50', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '71', 'citation_year': '2023'}, {'id': '51', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '38', 'citation_year': '2024'}, {'id': '52', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '81', 'citation_year': '2025'}, {'id': '147', 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': '65', 'citation_year': '2019'}, {'id': '148', 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': '98', 'citation_year': '2020'}, {'id': '149', 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': '23', 'citation_year': '2021'}, {'id': '150', 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': '65', 'citation_year': '2022'}, {'id': '151', 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': '14', 'citation_year': '2023'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
