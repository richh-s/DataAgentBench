code = """import json

# Load the citations data for 2018
citations_file = locals()['var_functions.query_db:0']
with open(citations_file, 'r') as f:
    citations_2018 = json.load(f)

# Load the paper documents and extract information
papers_file = locals()['var_functions.query_db:16']
with open(papers_file, 'r') as f:
    paper_docs = json.load(f)

# Create a dictionary of papers with their sources
papers_dict = {}
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']
    
    # Determine source/publisher
    source = []
    if 'ACM' in text or 'acm' in text:
        source.append('ACM')
    if 'IEEE' in text or 'ieee' in text:
        source.append('IEEE')
    
    # Check for additional ACM patterns
    acm_patterns = ['Association for Computing Machinery', 'acm.org', 'dx.doi.org']
    for pattern in acm_patterns:
        if pattern in text and 'ACM' not in source:
            source.append('ACM')
    
    papers_dict[title] = source

# Now match citations with papers and filter for ACM papers
acm_citations = []
for citation in citations_2018:
    citation_title = citation['title']
    citation_count = int(citation['citation_count'])
    
    # Check if this paper is in our papers_dict and has ACM as a source
    if citation_title in papers_dict:
        sources = papers_dict[citation_title]
        if 'ACM' in sources:
            acm_citations.append({
                'title': citation_title,
                'citation_count': citation_count,
                'sources': sources
            })

# Calculate average citation count for ACM papers
if acm_citations:
    total_citations = sum(c['citation_count'] for c in acm_citations)
    avg_citations = total_citations / len(acm_citations)
    result = {
        'acm_papers_count': len(acm_citations),
        'total_citations': total_citations,
        'average_citations': round(avg_citations, 2),
        'acm_papers': acm_citations
    }
else:
    result = {
        'acm_papers_count': 0,
        'total_citations': 0,
        'average_citations': 0,
        'acm_papers': []
    }

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:14': {'total_records': 158, 'sample': {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'citations_2018_count': 158, 'paper_docs_count': 5}, 'var_functions.execute_python:20': [{'title': 'A Lived Informatics Model of Personal Informatics', 'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'source': ['ACM']}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'source': ['ACM', 'IEEE']}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'source': ['ACM']}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'source': ['ACM', 'IEEE']}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'source': ['ACM', 'IEEE']}]}

exec(code, env_args)
