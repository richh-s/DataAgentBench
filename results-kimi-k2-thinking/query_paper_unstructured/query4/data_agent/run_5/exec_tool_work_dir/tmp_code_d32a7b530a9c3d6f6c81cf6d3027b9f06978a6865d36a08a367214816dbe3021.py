code = """import json
import re

# Read the paper documents
paper_docs_path = locals()['var_functions.query_db:4']
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

# Extract paper information
papers = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year from the text (look for patterns like '2016', 'CHI 2016', etc.)
    year = None
    year_patterns = [
        r'\b(20\d{2})\b',  # 4-digit year starting with 20
        r"CHI\s+(\d{4})",
        r"UbiComp\s+'(\d{2})",
        r"CSCW\s+(\d{4})",
        r"DIS\s+(\d{4})",
        r"PervasiveHealth\s+(\d{4})",
        r"WWW\s+(\d{4})",
        r"IUI\s+(\d{4})",
        r"OzCHI\s+(\d{4})",
        r"TEI\s+(\d{4})",
        r"AH\s+(\d{4})"
    ]
    
    for pattern in year_patterns:
        match = re.search(pattern, text)
        if match:
            if "UbiComp" in pattern and match.group(1):
                year = int("20" + match.group(1))
            elif match.group(1):
                year = int(match.group(1))
            if year and 2000 <= year <= 2025:
                break
    
    # Extract domain (look for 'physical activity' and other domains)
    domain = []
    domain_patterns = {
        'physical activity': r'physical activity|fitness|exercise',
        'food': r'food|diet|nutrition',
        'sleep': r'sleep',
        'mental': r'mental health|depression|anxiety',
        'finances': r'finance|money|expense',
        'location': r'location|place',
        'social': r'social interaction'
    }
    
    text_lower = text.lower()
    for domain_name, pattern in domain_patterns.items():
        if re.search(pattern, text_lower):
            domain.append(domain_name)
    
    papers.append({
        'title': title,
        'year': year,
        'domain': domain,
        'text': text
    })

# Read citation data
citations = locals()['var_functions.query_db:0']

print('__RESULT__:')
print(json.dumps({
    'papers_count': len(papers),
    'citations_count': len(citations),
    'sample_paper': papers[0] if papers else None,
    'sample_citation': citations[0] if citations else None
}))"""

env_args = {'var_functions.query_db:0': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json'}

exec(code, env_args)
