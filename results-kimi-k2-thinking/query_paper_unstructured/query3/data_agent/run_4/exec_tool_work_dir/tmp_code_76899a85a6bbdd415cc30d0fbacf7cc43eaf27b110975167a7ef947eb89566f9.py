code = """import json
import re

# Load the full MongoDB results file
with open('/tmp/tmp8b5k6pbd.json', 'r') as f:
    papers = json.load(f)

# Extract paper details
def extract_paper_details(paper):
    filename = paper['filename']
    text = paper['text']
    
    # Extract title (remove .txt extension)
    title = filename.replace('.txt', '')
    
    # Extract year from venue patterns
    year = None
    # Look for common venue abbreviations with year (e.g., CHI '17, UbiComp '15)
    venue_match = re.search(r'(UbiComp|CHI|DIS|CSCW|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*[\'"]\s*(\d{2})', text[:2000])
    if venue_match:
        yr_str = venue_match.group(2)
        if int(yr_str) < 50:
            year = 2000 + int(yr_str)  # 2000-2049
        else:
            year = 1900 + int(yr_str)  # 1950-1999
    else:
        # Look for full year (2015, 2016, etc.)
        year_match = re.search(r'20\d{2}', text[:2000])
        if year_match:
            year = int(year_match.group())
    
    # Check if empirical contribution
    is_empirical = 'empirical' in text.lower()
    
    return {
        'title': title,
        'year': year,
        'is_empirical': is_empirical
    }

# Parse all papers
paper_details = [extract_paper_details(p) for p in papers]

# Filter empirical papers after 2016
empirical_after_2016 = [p for p in paper_details if p['is_empirical'] and p['year'] and p['year'] > 2016]

print('__RESULT__:')
print(json.dumps({
    'total_papers': len(paper_details),
    'empirical_papers': len([p for p in paper_details if p['is_empirical']]),
    'empirical_after_2016': len(empirical_after_2016),
    'sample_titles': [p['title'] for p in empirical_after_2016]
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:14': {'total_papers': 5, 'sample_keys': ['_id', 'filename', 'text'], 'sample_filename': 'A Lived Informatics Model of Personal Informatics.txt', 'sample_text_preview': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, 'var_functions.query_db:16': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.execute_python:26': {'total_papers': 5, 'empirical_papers': 2, 'empirical_after_2016': 1, 'sample_titles': ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App']}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
