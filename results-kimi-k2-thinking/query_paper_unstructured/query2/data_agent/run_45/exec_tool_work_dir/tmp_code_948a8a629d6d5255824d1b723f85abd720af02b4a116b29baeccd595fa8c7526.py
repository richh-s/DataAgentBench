code = """import json
import re

# Load both datasets
citations_file = locals()['var_functions.query_db:0']
papers_file = locals()['var_functions.query_db:16']

with open(citations_file, 'r') as f:
    citations_2018 = json.load(f)

with open(papers_file, 'r') as f:
    paper_docs = json.load(f)

# Create citation map
citation_titles = {item['title'] for item in citations_2018}
citation_map = {item['title']: int(item['citation_count']) for item in citations_2018}

# Count papers and their sources
paper_count = len(paper_docs)
acm_papers = []
all_papers_info = []

for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    title = filename.replace('.txt', '')
    
    # Check if this paper has citations in 2018
    if title in citation_titles:
        text_lower = text.lower()
        source = None
        
        if 'acm' in text_lower:
            source = 'ACM'
        elif 'ieee' in text_lower:
            source = 'IEEE'
        elif 'pubmed' in text_lower:
            source = 'PubMed'
        
        # Extract venue
        venue = None
        venue_patterns = [r'CHI', r'Ubicomp', r'UbiComp', r'CSCW', r'DIS', r'PervasiveHealth', r'WWW', r'IUI', r'OzCHI', r'TEI', r'AH']
        for pattern in venue_patterns:
            match = re.search(pattern, text)
            if match:
                venue = match.group()
                break
        
        # Extract year
        year = None
        year_match = re.search(r'Copyright\s+(?:\xa9\s+)?(19|20)\d{2}', text)
        if not year_match:
            year_match = re.search(r'(19|20)\d{2}', text)
        if year_match:
            try:
                year = int(year_match.group(0))
            except:
                year = None
        
        all_papers_info.append({
            'title': title,
            'source': source,
            'venue': venue,
            'year': year,
            'has_citations': title in citation_map,
            'citation_count': citation_map.get(title, 0)
        })
        
        if source == 'ACM':
            acm_papers.append(title)

# Calculate statistics
acm_papers_cited = [p for p in all_papers_info if p['has_citations'] and p['source'] == 'ACM']
summary = {
    'total_paper_docs': paper_count,
    'papers_in_citations': len([p for p in all_papers_info if p['has_citations']]),
    'acm_papers': len(acm_papers),
    'acm_papers_in_citations': len(acm_papers_cited),
    'citation_stats': {
        'total_citations': sum(p['citation_count'] for p in acm_papers_cited),
        'average_citations': sum(p['citation_count'] for p in acm_papers_cited) / len(acm_papers_cited) if acm_papers_cited else 0
    },
    'acm_papers_details': acm_papers_cited
}

print('__RESULT__:')
print(json.dumps(summary, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.execute_python:10': {'record_count': 158, 'sample': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '28'}, {'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '58'}]}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'record_count': 158, 'sample': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': 95}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': 28}, {'title': 'Why We Use and Abandon Smart Devices', 'citation_count': 58}], 'total_citations': 7949}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'acm_papers_count': 2, 'total_citations': 137, 'average_citations': 68.5, 'sample_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': 50, 'year': 2015, 'venue': 'CHI'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citation_count': 87, 'year': 2016, 'venue': 'CHI'}]}, 'var_functions.execute_python:20': {'acm_papers_count': 2, 'total_citations': 137, 'average_citations': 68.5, 'all_acm_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': 50, 'year': 2015, 'venue': 'CHI'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citation_count': 87, 'year': 2016, 'venue': 'CHI'}]}}

exec(code, env_args)
