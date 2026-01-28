code = """import json
import re

# Access the stored data
citations_2018_key = 'var_functions.query_db:5'
paper_docs_key = 'var_functions.query_db:2'

citations_2018_data = locals().get(citations_2018_key)
paper_docs_data = locals().get(paper_docs_key)

# Load data from files if they are file paths
if isinstance(citations_2018_data, str) and citations_2018_data.endswith('.json'):
    with open(citations_2018_data, 'r') as f:
        citations_2018 = json.load(f)
else:
    citations_2018 = citations_2018_data

if isinstance(paper_docs_data, str) and paper_docs_data.endswith('.json'):
    with open(paper_docs_data, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = paper_docs_data

# Build a dictionary mapping paper titles to citation counts
citation_dict = {}
for item in citations_2018:
    title = item.get('title', '').strip()
    count = int(item.get('citation_count', 0))
    citation_dict[title] = count

# Find ACM papers with 2018 citations
acm_papers = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '').strip()
    
    # Check if this paper has citations in 2018
    if title in citation_dict:
        text = doc.get('text', '')
        
        # Check for ACM affiliation
        if 'ACM' in text:
            # Look for specific ACM patterns
            acm_patterns = [
                r'ACM\s+\d{4}', r'ACM\s+Copyright', r'Proceedings.*?ACM',
                r'ACM\s+Press', r'ACM\s+Trans', r'ACM\s+SIG',
                r'ISBN.*?ACM', r'DOI.*?10\.1145', r'UbiComp.*?ACM',
                r'CHI.*?ACM', r'CSCW.*?ACM', r'DIS.*?ACM'
            ]
            
            is_acm = any(re.search(pattern, text, re.IGNORECASE) for pattern in acm_patterns)
            
            if is_acm:
                acm_papers.append({
                    'title': title,
                    'citations': citation_dict[title]
                })

# Calculate average citation count
if acm_papers:
    total_citations = sum(p['citations'] for p in acm_papers)
    avg_citations = total_citations / len(acm_papers)
    
    result = {
        'average_citation_count': round(avg_citations, 2),
        'total_acm_papers': len(acm_papers),
        'total_citations': total_citations
    }
else:
    result = {
        'average_citation_count': 0,
        'total_acm_papers': 0,
        'total_citations': 0,
        'message': 'No ACM papers found'
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '14', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '28', 'citation_year': '2018'}, {'id': '25', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '58', 'citation_year': '2018'}, {'id': '34', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '20', 'citation_year': '2018'}, {'id': '40', 'title': 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set', 'citation_count': '13', 'citation_year': '2018'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
