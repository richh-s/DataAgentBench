code = """import json

# Load data
citations_path = locals()['var_functions.query_db:6']
papers_path = locals()['var_functions.query_db:7']

with open(citations_path, 'r') as f:
    citations = json.load(f)

with open(papers_path, 'r') as f:
    papers = json.load(f)

# Get all 2018 citations
citations_2018 = [c for c in citations if str(c.get('citation_year', '')) == '2018']
print('Total 2018 citations:', len(citations_2018))

# Create paper map with titles
paper_map = {}
for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    paper_map[title.lower()] = {
        'text': paper.get('text', ''),
        'full_title': title
    }

# Check for matches and ACM publication
acm_citation_counts = []
matched_papers = []

for cit in citations_2018:
    cit_title = cit.get('title', '')
    cit_title_lower = cit_title.lower()
    
    # Find matching paper
    if cit_title_lower in paper_map:
        paper_info = paper_map[cit_title_lower]
        text = paper_info['text']
        
        # Multiple checks for ACM publication
        checks = {
            'acm_copyright': 'ACM' in text and 'Copyright' in text,
            'acm_isbn': 'ACM' in text and 'ISBN' in text,
            'acm_doi': 'acm.org' in text.lower() or 'doi.acm' in text.lower(),
            'acm_permission': 'Permission to make digital or hard copies' in text and 'ACM' in text
        }
        
        # Common ACM venues
        acm_venues = ['CHI', 'CSCW', 'DIS', 'IUI', 'TEI', 'Ubicomp', 'UbiComp']
        text_upper = text.upper()
        venue_check = any(venue.upper() in text_upper and ('ACM' in text or checks['acm_copyright']) for venue in acm_venues)
        
        # If any ACM indicator is present
        if any(checks.values()) or venue_check:
            acm_citation_counts.append(int(cit.get('citation_count', 0)))
            matched_papers.append({
                'title': cit_title,
                'citations': int(cit.get('citation_count', 0))
            })

# Calculate final result
if acm_citation_counts:
    avg = sum(acm_citation_counts) / len(acm_citation_counts)
    result = {
        'average_citation_count': round(avg, 2),
        'total_acm_papers': len(acm_citation_counts),
        'papers': matched_papers
    }
else:
    result = {'average_citation_count': 0, 'total_acm_papers': 0, 'papers': []}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '14', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '28', 'citation_year': '2018'}, {'id': '25', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '58', 'citation_year': '2018'}, {'id': '34', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '20', 'citation_year': '2018'}, {'id': '40', 'title': 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set', 'citation_count': '13', 'citation_year': '2018'}], 'var_functions.list_db:1': ['paper_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'average': 68.5, 'count': 2}, 'var_functions.execute_python:20': {'average_citation_count': 68.5, 'papers_analyzed': 2, 'total_citations': 137}, 'var_functions.execute_python:22': {'average_citation_count': 68.5, 'papers_count': 2, 'sample_titles': ['A Lived Informatics Model of Personal Informatics', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}}

exec(code, env_args)
