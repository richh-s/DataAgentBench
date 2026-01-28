code = """import json
import re

# Load 2018 citations data
citations_file = locals()['var_functions.query_db:0']
with open(citations_file, 'r') as f:
    citations_2018 = json.load(f)

# Load paper documents data
papers_file = locals()['var_functions.query_db:16']
with open(papers_file, 'r') as f:
    paper_docs = json.load(f)

# Create a mapping of paper titles to citation counts for 2018
citation_map = {}
for item in citations_2018:
    title = item['title']
    citation_map[title] = int(item['citation_count'])

print('__RESULT__:')
print(f"Total papers in 2018 citations: {len(citation_map)}")
print(f"Sample citation titles: {list(citation_map.keys())[:5]}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.execute_python:10': {'record_count': 158, 'sample': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '28'}, {'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '58'}]}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'record_count': 158, 'sample': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': 95}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': 28}, {'title': 'Why We Use and Abandon Smart Devices', 'citation_count': 58}], 'total_citations': 7949}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'acm_papers_count': 2, 'total_citations': 137, 'average_citations': 68.5, 'sample_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': 50, 'year': 2015, 'venue': 'CHI'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citation_count': 87, 'year': 2016, 'venue': 'CHI'}]}, 'var_functions.execute_python:20': {'acm_papers_count': 2, 'total_citations': 137, 'average_citations': 68.5, 'all_acm_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': 50, 'year': 2015, 'venue': 'CHI'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citation_count': 87, 'year': 2016, 'venue': 'CHI'}]}}

exec(code, env_args)
