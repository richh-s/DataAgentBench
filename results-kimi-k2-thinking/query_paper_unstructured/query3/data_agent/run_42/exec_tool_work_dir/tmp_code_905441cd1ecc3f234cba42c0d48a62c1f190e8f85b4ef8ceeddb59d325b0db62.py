code = """import json
import re

# Get the paper docs data from storage
paper_docs_data = locals()['var_functions.query_db:2']

# Load from file if it's a path string
if isinstance(paper_docs_data, str) and paper_docs_data.endswith('.json'):
    with open(paper_docs_data, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = paper_docs_data

print('Total papers loaded:', len(paper_docs))

# Extract information from all papers
extracted_papers = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename (remove .txt)
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year from text
    year = None
    # Look for year patterns in the text
    patterns = [
        r"(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UBICOMP)\s+'(\d{2})[,'\s]",
        r"(20\d{2})\s*(?:,\s*)?(?:Proceedings|Conference|Journal|International|CHI|UbiComp|CSCW)",
        r"Copyright\s*[\D]*(20\d{2})",
        r"(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}[,-]\s*(20\d{2})",
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            year_str = match.group(1)
            if len(year_str) == 2:
                year = int('20' + year_str)
            else:
                year = int(year_str)
            if 2010 <= year <= 2025:
                break
    
    # Extract contribution type
    contribution = []
    text_lower = text.lower()
    
    # Check for empirical indicators
    empirical_keywords = ['empirical', 'study', 'surveyed', 'interview', 'investigate', 'examine', 'explore', 'understand', 'participants', 'survey']
    if any(keyword in text_lower for keyword in empirical_keywords):
        contribution.append('empirical')
    
    # Check for other contribution types
    if 'artifact' in text_lower or 'system' in text_lower or 'prototype' in text_lower:
        contribution.append('artifact')
    if 'theoretical' in text_lower or 'model' in text_lower or 'framework' in text_lower:
        contribution.append('theoretical')
    if 'survey review' in text_lower or 'literature review' in text_lower:
        contribution.append('survey')
    
    # Remove duplicates
    contribution = list(set(contribution))
    
    if title and year and contribution:  # Only include if we have all info
        extracted_papers.append({
            'title': title,
            'year': year,
            'contribution': contribution
        })

# Filter papers with empirical contribution and year > 2016
empirical_papers_2017_plus = [p for p in extracted_papers if p['year'] > 2016 and 'empirical' in p['contribution']]

print('Total extracted papers with data:', len(extracted_papers))
print('Empirical papers after 2016:', len(empirical_papers_2017_plus))

# Display first few to verify
for i, paper in enumerate(empirical_papers_2017_plus[:5]):
    print(i+1, paper['title'], '- Year:', paper['year'])

# Store results for next step
result_data = empirical_papers_2017_plus

print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}]}

exec(code, env_args)
