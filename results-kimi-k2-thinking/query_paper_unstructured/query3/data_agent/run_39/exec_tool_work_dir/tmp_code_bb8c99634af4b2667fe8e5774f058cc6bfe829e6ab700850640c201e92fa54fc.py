code = """import json
import re

# Read the paper documents from the file
with open('/tmp/tmpo1k6c4x7.json', 'r') as f:
    paper_docs = json.load(f)

# Process paper documents to extract title, year, and contribution
def extract_paper_info(doc):
    filename = doc['filename']
    text = doc['text']
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '')
    
    # Extract year from text - look for patterns like '2017', '2018', etc.
    # Common patterns: UbiComp '17, CHI 2018, 2019, etc.
    year = None
    
    # Look for 4-digit year patterns
    year_matches = re.findall(r"(?:\b|')((?:19|20)\d{2})\b", text)
    if year_matches:
        # Convert to integers and filter reasonable years for academic papers
        years = [int(y) for y in year_matches if 1900 <= int(y) <= 2030]
        if years:
            # Take the most recent year as publication year
            year = max(years)
    
    # Extract contribution type - look for keywords
    contribution = []
    text_lower = text.lower()
    
    # Define contribution keywords
    contribution_keywords = {
        'empirical': ['empirical', 'empirically', 'study', 'studies', 'survey', 'experiment', 'experiments', 'evaluation', 'evaluated', 'user study', 'field study', 'case study'],
        'artifact': ['artifact', 'system', 'tool', 'prototype', 'implementation', 'design', 'architecture'],
        'theoretical': ['theory', 'theoretical', 'framework', 'model', 'conceptual', 'taxonomy'],
        'survey': ['survey', 'literature review', 'systematic review', 'meta-analysis'],
        'methodological': ['method', 'methodology', 'methodological', 'approach', 'technique']
    }
    
    # Check for each contribution type
    for contrib_type, keywords in contribution_keywords.items():
        if any(keyword in text_lower for keyword in keywords):
            contribution.append(contrib_type)
    
    # Remove duplicates and join
    contribution = list(set(contribution))
    
    return {
        'title': title,
        'year': year,
        'contribution': contribution,
        'filename': filename
    }

# Process all papers
processed_papers = [extract_paper_info(doc) for doc in paper_docs]

# Filter papers with year > 2016 and that have 'empirical' in contribution
empirical_papers_2017_plus = [
    paper for paper in processed_papers 
    if paper['year'] is not None and paper['year'] > 2016 and 'empirical' in paper['contribution']
]

print('__RESULT__:')
print(json.dumps(empirical_papers_2017_plus))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
