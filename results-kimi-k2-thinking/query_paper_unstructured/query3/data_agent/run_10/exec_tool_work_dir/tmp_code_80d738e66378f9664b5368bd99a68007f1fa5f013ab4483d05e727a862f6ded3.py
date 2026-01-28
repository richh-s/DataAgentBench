code = """# First, let's properly load and analyze the paper documents
import json
import re
import os

# Get the file path from storage
paper_data_info = locals()['var_functions.query_db:2']

# Load the paper documents
if isinstance(paper_data_info, str):
    with open(paper_data_info, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = paper_data_info

# Extract paper information from documents
papers_info = []
for i, doc in enumerate(paper_docs):
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '').strip() if filename else ''
    text = doc.get('text', '')
    
    # Extract publication year
    year = None
    # Look for patterns like venue with year: CHI '17, UbiComp '18, etc.
    year_patterns = [
        r"CHI\s+'(\d{2})",
        r"UbiComp\s+'(\d{2})",
        r"CSCW\s+'(\d{2})",
        r"DIS\s+'(\d{2})",
        r"WWW\s+'(\d{2})",
        r"IUI\s+'(\d{2})",
        r"20(\d{2})",  # Last 2 digits of year
        r"20\d{2}"     # Full year
    ]
    
    for pattern in year_patterns:
        matches = re.findall(pattern, text)
        if matches:
            # Convert 2-digit year to 4-digit if needed
            year_str = matches[0]
            if len(year_str) == 2:
                year = int('20' + year_str)
            else:
                year = int(year_str)
            break
    
    # Check for empirical contribution
    contribution = ''
    if 'empirical' in text.lower():
        contribution = 'empirical'
    elif 'empirically' in text.lower():
        contribution = 'empirical'
    
    papers_info.append({
        'title': title,
        'year': year,
        'contribution': contribution,
        'has_empirical': contribution == 'empirical'
    })

# Show the extracted data
for paper in papers_info:
    print(f"Title: {paper['title'][:80]}...")
    print(f"Year: {paper['year']}")
    print(f"Empirical: {paper['has_empirical']}")
    print("---")

print('__RESULT__:')
print(json.dumps(papers_info, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:9': {'total_papers': 5, 'empirical_papers_after_2016_count': 0, 'sample_empirical_papers': []}, 'var_functions.list_db:8': ['Citations', 'sqlite_sequence'], 'var_functions.execute_python:10': {'document_count': 5, 'first_doc_keys': ['_id', 'filename', 'text'], 'sample_filename': 'A Lived Informatics Model of Personal Informatics.txt'}, 'var_functions.query_db:12': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}]}

exec(code, env_args)
