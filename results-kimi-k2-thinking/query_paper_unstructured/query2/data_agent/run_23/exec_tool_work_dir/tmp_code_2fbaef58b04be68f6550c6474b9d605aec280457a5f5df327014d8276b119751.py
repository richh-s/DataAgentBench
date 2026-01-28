code = """import json

# Load data
citations_path = locals()['var_functions.query_db:6']
papers_path = locals()['var_functions.query_db:7']

with open(citations_path, 'r') as f:
    citations = json.load(f)

with open(papers_path, 'r') as f:
    papers = json.load(f)

# Filter 2018 citations
citations_2018 = [c for c in citations if str(c.get('citation_year', '')) == '2018']
citation_titles = {c.get('title', '').lower(): c for c in citations_2018}

# Common ACM venues from the hints
acm_venues = ['CHI', 'Ubicomp', 'UbiComp', 'CSCW', 'DIS', 'PervasiveHealth', 'WWW', 'IUI', 'OzCHI', 'TEI', 'AH']

acm_citations = []
found_titles = []

for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    title_lower = title.lower()
    text = paper.get('text', '')
    
    # Check if this paper has citations in 2018
    if title_lower in citation_titles:
        # Check if published by ACM
        text_upper = text.upper()
        text_lower_check = text.lower()
        
        # Multiple ways to identify ACM papers
        is_acm = False
        
        # 1. Copyright notice with ACM
        if 'ACM' in text and ('ISBN' in text or 'COPYRIGHT' in text):
            is_acm = True
        
        # 2. ACM in header/venue
        if not is_acm:
            for venue in acm_venues:
                if venue in text_upper and ('ACM' in text or '.ACM.' in text_upper or venue in ['CHI', 'CSCW', 'DIS', 'IUI', 'TEI']):
                    is_acm = True
                    break
        
        # 3. Explicit ACM DOI or URL
        if not is_acm:
            if 'DOI.ACM.ORG' in text_upper or 'DL.ACM.ORG' in text_upper:
                is_acm = True
        
        # 4. ACM permission statement
        if not is_acm:
            if 'Permission to make digital or hard copies' in text and 'ACM' in text:
                is_acm = True
        
        if is_acm:
            cit = citation_titles[title_lower]
            acm_citations.append(int(cit.get('citation_count', 0)))
            found_titles.append(cit.get('title'))

# Calculate final result
if acm_citations:
    avg = sum(acm_citations) / len(acm_citations)
    result = {
        'average_citation_count': round(avg, 2),
        'papers_count': len(acm_citations),
        'sample_titles': found_titles[:5]  # First 5 titles
    }
else:
    result = {'average_citation_count': 0, 'papers_count': 0, 'sample_titles': []}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '14', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '28', 'citation_year': '2018'}, {'id': '25', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '58', 'citation_year': '2018'}, {'id': '34', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '20', 'citation_year': '2018'}, {'id': '40', 'title': 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set', 'citation_count': '13', 'citation_year': '2018'}], 'var_functions.list_db:1': ['paper_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'average': 68.5, 'count': 2}, 'var_functions.execute_python:20': {'average_citation_count': 68.5, 'papers_analyzed': 2, 'total_citations': 137}}

exec(code, env_args)
