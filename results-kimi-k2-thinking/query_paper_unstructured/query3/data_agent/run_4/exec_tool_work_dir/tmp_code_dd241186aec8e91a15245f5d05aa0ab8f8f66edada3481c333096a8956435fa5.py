code = """import json
import re

# Get MongoDB file path
mongo_file = globals()['var_functions.query_db:5']
with open(mongo_file, 'r') as f:
    papers = json.load(f)

# Extract paper information
def extract_info(paper):
    filename = paper['filename']
    text = paper['text']
    
    title = filename.replace('.txt', '')
    
    # Find year - look for venue abbreviations with years
    year = None
    patterns = ['UbiComp', 'CHI', 'DIS', 'CSCW', 'PervasiveHealth', 'WWW', 'IUI', 'OzCHI', 'TEI', 'AH']
    for pattern in patterns:
        match = re.search(pattern + r"\s*['"]\s*(\d{2})", text[:2000])
        if match:
            yr = match.group(1)
            year = 2000 + int(yr) if int(yr) < 50 else 1900 + int(yr)
            break
    
    # Fall back to looking for 20xx year pattern
    if not year:
        match = re.search(r'20\d{2}', text[:2000])
        if match:
            year = int(match.group())
    
    # Is empirical?
    is_empirical = 'empirical' in text.lower()
    
    return {'title': title, 'year': year, 'is_empirical': is_empirical}

# Process all papers
paper_data = [extract_info(p) for p in papers]

# Filter empirical papers after 2016
empirical_after_2016 = [p for p in paper_data if p['is_empirical'] and p['year'] and p['year'] > 2016]

output = {
    'total_papers': len(paper_data),
    'empirical_papers': len([p for p in paper_data if p['is_empirical']]),
    'empirical_after_2016': len(empirical_after_2016),
    'sample_titles': [p['title'] for p in empirical_after_2016[:5]]
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:14': {'total_papers': 5, 'sample_keys': ['_id', 'filename', 'text'], 'sample_filename': 'A Lived Informatics Model of Personal Informatics.txt', 'sample_text_preview': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, 'var_functions.query_db:16': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}]}

exec(code, env_args)
