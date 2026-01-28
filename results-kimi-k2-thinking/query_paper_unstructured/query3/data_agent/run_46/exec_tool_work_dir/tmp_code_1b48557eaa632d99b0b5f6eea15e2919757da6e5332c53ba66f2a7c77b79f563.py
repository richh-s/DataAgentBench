code = """import json
import re

# Load the data
paper_docs_path = locals()['var_functions.query_db:8']
citations_path = locals()['var_functions.query_db:9']

with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

with open(citations_path, 'r') as f:
    citations = json.load(f)

print(f"Loaded {len(paper_docs)} papers and {len(citations)} citation records")

# Process papers to extract metadata
papers = []
for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    
    # Extract title (remove .txt)
    title = filename.replace('.txt', '')
    
    # Extract year from text
    year = None
    
    # Look for 4-digit years starting with 20
    year_match = re.search(r'\b(20\d{2})\b', text[:2000])
    if year_match:
        year = int(year_match.group(1))
    else:
        # Look for pattern like: CHI '17, UIST '16, etc.
        year_match = re.search(r"[A-Z]+\s+'(\d{2})\b", text[:2000])
        if year_match:
            year_num = int(year_match.group(1))
            if year_num < 50:
                year = 2000 + year_num
            else:
                year = 1900 + year_num
    
    # Check if paper has empirical contribution
    lower_text = text.lower()
    is_empirical = 'empirical' in lower_text or \
                   'empiric' in lower_text or \
                   'study' in lower_text or \
                   'evaluation' in lower_text or \
                   'experiment' in lower_text or \
                   'survey' in lower_text or \
                   'interview' in lower_text
    
    # Also look for specific patterns
    empirical_indicators = [
        'empirical study', 'empirical evaluation', 'empirical investigation',
        'field study', 'user study', 'lab study', 'case study',
        'interviews', 'survey', 'experiment', 'experimental'
    ]
    
    has_strong_empirical = any(indicator in lower_text for indicator in empirical_indicators)
    
    papers.append({
        'title': title,
        'year': year,
        'is_empirical': is_empirical,
        'has_strong_empirical': has_strong_empirical,
        'filename': filename
    })

# Filter papers published after 2016 with empirical contribution
empirical_papers_after_2016 = [
    p for p in papers 
    if p['year'] and p['year'] > 2016 and p['is_empirical']
]

print(f"Found {len(empirical_papers_after_2016)} empirical papers after 2016")

# Show filtered papers
for p in empirical_papers_after_2016:
    print(f"- {p['title']} ({p['year']})")

print('__RESULT__:')
print(json.dumps(empirical_papers_after_2016, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:16': 'file_storage/functions.execute_python:16.json', 'var_functions.execute_python:18': [{'title': 'A Lived Informatics Model of Personal Informatics', 'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'year': None, 'text_sample': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu", 'has_empirical': False, 'has_study': True}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'year': None, 'text_sample': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152', 'has_empirical': False, 'has_study': True}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'year': None, 'text_sample': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali', 'has_empirical': True, 'has_study': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'year': None, 'text_sample': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E', 'has_empirical': True, 'has_study': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'year': None, 'text_sample': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C', 'has_empirical': False, 'has_study': True}]}

exec(code, env_args)
