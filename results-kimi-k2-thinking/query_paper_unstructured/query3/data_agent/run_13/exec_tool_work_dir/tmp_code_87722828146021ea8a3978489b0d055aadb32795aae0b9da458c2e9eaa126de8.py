code = """import json
import re

# Load papers data
papers_file = locals()['var_functions.query_db:46']
with open(papers_file, 'r') as f:
    papers = json.load(f)

# Process papers to extract metadata
paper_data = []
for p in papers:
    title = p['filename'].replace('.txt', '')
    text = p['text']
    
    # Extract year
    year = None
    year_matches = re.findall(r"(?:\b|')((?:20)?1[5-9]|20[12]\d)\b", text)
    years = []
    for match in year_matches:
        if match:
            if len(match) == 2:
                y = int('20' + match)
                if 2010 <= y <= 2030:
                    years.append(y)
            elif len(match) == 4:
                y = int(match)
                if 2010 <= y <= 2030:
                    years.append(y)
    if years:
        year = max(years)
    
    # Check for empirical
    empirical = 'empirical' in text.lower()
    
    paper_data.append({'title': title, 'year': year, 'empirical': empirical})

# Filter empirical papers after 2016
filtered_papers = [p for p in paper_data if p['empirical'] and p['year'] and p['year'] > 2016]

print('Total papers processed:', len(paper_data))
print('Empirical papers after 2016:', len(filtered_papers))

# Output titles for citation lookup
titles = [p['title'] for p in filtered_papers]
print('__RESULT__:')
print(json.dumps(titles))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:32': [], 'var_functions.execute_python:42': [], 'var_functions.execute_python:44': {'total_papers': 5, 'sample_filename': 'A Lived Informatics Model of Personal Informatics.txt', 'sample_text_start': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json'}

exec(code, env_args)
