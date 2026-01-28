code = """import json

# Load citations data
citations_path = locals()['var_functions.query_db:6']
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Load papers data
papers_path = locals()['var_functions.query_db:7']
with open(papers_path, 'r') as f:
    papers = json.load(f)

# Filter 2018 citations
citations_2018 = [c for c in citations if str(c.get('citation_year', '')) == '2018']

# Create paper map
paper_map = {}
for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    paper_map[title.lower()] = paper

# Find ACM papers with citations in 2018
acm_matches = []
for cit in citations_2018:
    cit_title = cit.get('title', '').lower()
    if cit_title in paper_map:
        paper = paper_map[cit_title]
        text = paper.get('text', '')
        
        # Check for ACM publication indicators
        if ('ACM' in text and ('ISBN' in text or 'Copyright' in text)) or \
           ('acm.org' in text) or \
           ('Permission to make digital or hard copies' in text and 'ACM' in text):
            acm_matches.append({
                'title': cit.get('title'),
                'citations': int(cit.get('citation_count', 0))
            })

# Calculate average
if acm_matches:
    avg = sum(item['citations'] for item in acm_matches) / len(acm_matches)
    result = {'average': round(avg, 2), 'count': len(acm_matches)}
else:
    result = {'average': 0, 'count': 0}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '14', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '28', 'citation_year': '2018'}, {'id': '25', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '58', 'citation_year': '2018'}, {'id': '34', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '20', 'citation_year': '2018'}, {'id': '40', 'title': 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set', 'citation_count': '13', 'citation_year': '2018'}], 'var_functions.list_db:1': ['paper_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
