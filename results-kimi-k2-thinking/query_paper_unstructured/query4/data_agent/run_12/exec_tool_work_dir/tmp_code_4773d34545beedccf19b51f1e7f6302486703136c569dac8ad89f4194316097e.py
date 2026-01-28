code = """import json
import re

# Load full papers data
mongo_key = 'var_functions.query_db:32'
papers_data = locals().get(mongo_key)

if isinstance(papers_data, str) and papers_data.endswith('.json'):
    with open(papers_data, 'r') as f:
        papers = json.load(f)
else:
    papers = papers_data

# Load full citations data  
citations_key = 'var_functions.query_db:14'
citations_data = locals().get(citations_key)

if isinstance(citations_data, str) and citations_data.endswith('.json'):
    with open(citations_data, 'r') as f:
        citations = json.load(f)
else:
    citations = citations_data

# Parse paper information
paper_info = []
for paper in papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year with multiple patterns
    year = None
    patterns = [
        r'UBICOMP\s*[\'′]?(\d{2})',  # UBICOMP '15
        r'CHI\s*[\'′]?(\d{2})',      # CHI '16
        r'\b(20\d{2})\b',           # 2015, 2016
        r'\b(19\d{2})\b',           # 1990s
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            year_str = match.group(1)
            if len(year_str) == 4:
                year = int(year_str)
            elif len(year_str) == 2:
                # Convert 15 to 2015, 16 to 2016, etc.
                year = 2000 + int(year_str)
            break
    
    # Domain detection - check if in 'physical activity' domain
    text_lower = text.lower()
    domain_keywords = ['physical activity', 'physical activities', 'fitness', 'exercise', 
                       'activity tracking', 'fitness tracking', 'workout']
    is_physical_activity = any(keyword in text_lower for keyword in domain_keywords)
    
    paper_info.append({
        'title': title,
        'year': year,
        'is_physical_activity': is_physical_activity,
        'original_title': title  # Keep for matching with citations
    })

# Filter papers from 2016 in physical activity domain
papers_2016_pa = [p for p in paper_info if p['year'] == 2016 and p['is_physical_activity']]

# Create a dictionary for citation lookup by title
citation_dict = {}
for cit in citations:
    cit_title = cit.get('title', '')
    cit_count = int(cit.get('citation_count', 0))
    cit_year = int(cit.get('citation_year', 0))
    
    if cit_title not in citation_dict:
        citation_dict[cit_title] = []
    citation_dict[cit_title].append({
        'citation_count': cit_count,
        'citation_year': cit_year
    })

# Find papers and their citations
results = []
for paper in papers_2016_pa:
    paper_title = paper['title']
    total_citations = 0
    
    # Find matching citations (exact title match)
    if paper_title in citation_dict:
        for cit_record in citation_dict[paper_title]:
            total_citations += cit_record['citation_count']
    
    results.append({
        'title': paper_title,
        'total_citations': total_citations
    })

# Also check for papers that might have slight variations in title
# This is a fallback in case of minor differences
all_results = []
for paper in papers_2016_pa:
    paper_title = paper['title']
    total_citations = 0
    
    # Direct match first
    if paper_title in citation_dict:
        for cit_record in citation_dict[paper_title]:
            total_citations += cit_record['citation_count']
    else:
        # Try fuzzy matching (case insensitive, strip common words)
        paper_lower = paper_title.lower()
        for cit_title, cit_records in citation_dict.items():
            if paper_lower in cit_title.lower() or cit_title.lower() in paper_lower:
                for cit_record in cit_records:
                    total_citations += cit_record['citation_count']
    
    all_results.append({
        'title': paper_title,
        'total_citations': total_citations
    })

print('__RESULT__:')
print(json.dumps({
    'paper_summary': {
        'total_papers_in_db': len(papers),
        'physical_activity_papers': len([p for p in paper_info if p['is_physical_activity']]),
        'papers_2016': len([p for p in paper_info if p['year'] == 2016]),
        'papers_2016_physical_activity': len(papers_2016_pa)
    },
    'papers_2016_pa_details': papers_2016_pa,
    'citation_results': all_results
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'total_papers': 99, 'first_paper_sample': {'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'text_preview': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'total_papers_loaded': 5}, 'var_functions.execute_python:20': {'total_papers': 5, 'total_citations': 1405, 'papers_2016_pa': [], 'all_papers_info': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'is_physical_activity': True, 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'is_physical_activity': True, 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'is_physical_activity': True, 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'is_physical_activity': True, 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'is_physical_activity': True, 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}]}, 'var_functions.execute_python:22': {'has_sample_paper': True, 'sample_filename': 'A Lived Informatics Model of Personal Informatics.txt', 'year_candidates': [], 'text_preview': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz"}, 'var_functions.execute_python:24': {'all_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'is_physical_activity': True, 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'is_physical_activity': True, 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'is_physical_activity': True, 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'is_physical_activity': True, 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'is_physical_activity': True, 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'papers_2016_pa': [], 'summary': {'total_papers': 5, 'physical_activity_papers': 5, 'papers_2016_pa_count': 0}}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': {'total_papers_loaded': 5, 'total_citations_loaded': 1405}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
