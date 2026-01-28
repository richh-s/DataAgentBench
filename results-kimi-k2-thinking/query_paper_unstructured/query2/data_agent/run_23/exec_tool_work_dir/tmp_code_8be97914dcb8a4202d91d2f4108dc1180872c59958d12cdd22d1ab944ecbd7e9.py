code = """import json

# Load all data
citations_path = locals()['var_functions.query_db:6']
papers_path = locals()['var_functions.query_db:7']

with open(citations_path, 'r') as f:
    citations = json.load(f)

with open(papers_path, 'r') as f:
    papers = json.load(f)

# Get 2018 citations
citations_2018 = [c for c in citations if str(c.get('citation_year', '')) == '2018']

# Create paper map for matching
paper_map = {}
for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    paper_map[title.lower()] = paper

# Find all 2018 citations that have matching papers
matched_acm = []
for cit in citations_2018:
    cit_title = cit.get('title', '')
    cit_title_lower = cit_title.lower()
    
    if cit_title_lower in paper_map:
        paper = paper_map[cit_title_lower]
        text = paper.get('text', '')
        
        # Check for ACM publication with relaxed criteria
        text_check = text.lower()
        if 'acm' in text_check:
            # This is likely an ACM paper
            matched_acm.append({
                'title': cit_title,
                'citation_count': int(cit.get('citation_count', 0))
            })

# Calculate average citation count
if matched_acm:
    avg_citations = sum(p['citation_count'] for p in matched_acm) / len(matched_acm)
    result = {
        'average_citation_count': round(avg_citations, 2),
        'papers_analyzed': len(matched_acm)
    }
else:
    result = {
        'average_citation_count': 0,
        'papers_analyzed': 0
    }

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': [{'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '14', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '28', 'citation_year': '2018'}, {'id': '25', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '58', 'citation_year': '2018'}, {'id': '34', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '20', 'citation_year': '2018'}, {'id': '40', 'title': 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set', 'citation_count': '13', 'citation_year': '2018'}], 'var_functions.list_db:1': ['paper_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'average': 68.5, 'count': 2}, 'var_functions.execute_python:20': {'average_citation_count': 68.5, 'papers_analyzed': 2, 'total_citations': 137}, 'var_functions.execute_python:22': {'average_citation_count': 68.5, 'papers_count': 2, 'sample_titles': ['A Lived Informatics Model of Personal Informatics', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}, 'var_functions.execute_python:24': {'average_citation_count': 68.5, 'total_acm_papers': 2, 'papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'citations': 50}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citations': 87}]}}

exec(code, env_args)
