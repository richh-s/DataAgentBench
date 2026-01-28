code = """import json
import re
from collections import defaultdict

# Get the variables from storage
citations_result_key = 'var_functions.query_db:5'
if citations_result_key not in locals():
    citations_var = []
else:
    citations_var = locals()[citations_result_key]

paper_docs_result_key = 'var_functions.query_db:6'
if paper_docs_result_key not in locals():
    paper_docs_var = []
else:
    paper_docs_var = locals()[paper_docs_result_key]

# Access citations data
citations_data = None
if isinstance(citations_var, str) and citations_var.endswith('.json'):
    with open(citations_var, 'r') as f:
        citations_data = json.load(f)
elif isinstance(citations_var, list):
    citations_data = citations_var
else:
    citations_data = []

# Access paper documents data  
paper_docs_data = None
if isinstance(paper_docs_var, str) and paper_docs_var.endswith('.json'):
    with open(paper_docs_var, 'r') as f:
        paper_docs_data = json.load(f)
elif isinstance(paper_docs_var, list):
    paper_docs_data = paper_docs_var
else:
    paper_docs_data = []

# Create citation mapping
title_to_citations = defaultdict(int)
for citation in citations_data:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    if title:
        title_to_citations[title] += count

# Find 2016 physical activity papers
papers_2016_physical_activity = []

for doc in paper_docs_data:
    try:
        filename = doc.get('filename', '')
        text = doc.get('text', '')
        
        if not filename or not text:
            continue
            
        # Title from filename
        title = filename.replace('.txt', '').strip()
        
        # Find year in text
        year = None
        text_start = text[:1000]
        
        # Look for full year
        year_match = re.search(r"\b(20\d{2})\b", text_start)
        if year_match:
            year = int(year_match.group(1))
        else:
            # Look for venue year format
            venue_match = re.search(r"[A-Z]+\s*'?(\d{2})\b", text_start)
            if venue_match:
                year_str = venue_match.group(1)
                if int(year_str) >= 10:
                    year = int('20' + year_str)
        
        # Check if 2016 and physical activity
        if year == 2016:
            text_lower = text.lower()
            if 'physical activity' in text_lower or 'exercise' in text_lower:
                total_citations = title_to_citations.get(title, 0)
                papers_2016_physical_activity.append({
                    'title': title,
                    'total_citation_count': total_citations
                })
    except:
        continue

# Sort by citation count
papers_2016_physical_activity.sort(key=lambda x: x['total_citation_count'], reverse=True)

print('__RESULT__:')
print(json.dumps(papers_2016_physical_activity))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
