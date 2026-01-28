code = """import json
import re

# Get the file paths
paper_docs_path = locals()['var_functions.query_db:2']
citations_path = locals()['var_functions.query_db:5']

# Load the data
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

with open(citations_path, 'r') as f:
    citations = json.load(f)

# Parse all papers to see years and contributions
papers_analysis = []

for i, doc in enumerate(paper_docs):
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    if not text:
        papers_analysis.append({'title': title, 'year': None, 'reason': 'empty text'})
        continue
    
    # Extract year - look for 4-digit years
    year_match = re.search(r"\b(201[0-9]|202[0-9])\b", text)
    year = int(year_match.group(1)) if year_match else None
    
    # Check if empirical
    text_lower = text.lower()
    is_empirical = 'empirical' in text_lower or 'user study' in text_lower or 'evaluation' in text_lower or 'survey' in text_lower or 'interview' in text_lower or 'experiment' in text_lower
    
    # Check for common contribution patterns
    contrib_patterns = []
    if 'empirical' in text_lower:
        contrib_patterns.append('empirical')
    if 'artifact' in text_lower:
        contrib_patterns.append('artifact')
    if 'theoretical' in text_lower or 'theory' in text_lower:
        contrib_patterns.append('theoretical')
    if 'survey' in text_lower:
        contrib_patterns.append('survey')
    if 'methodological' in text_lower:
        contrib_patterns.append('methodological')
    
    papers_analysis.append({
        'title': title,
        'year': year,
        'is_empirical': is_empirical,
        'contrib_patterns': contrib_patterns,
        'text_snippet': text[:300] if text else ''
    })

# Build citation aggregate
citation_totals = {}
for citation in citations:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    citation_totals[title] = citation_totals.get(title, 0) + count

print('__RESULT__:')
print(json.dumps({
    'total_papers': len(paper_docs),
    'citation_totals_size': len(citation_totals),
    'papers': papers_analysis
}, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': {'paper_docs_path': 'file_storage/functions.query_db:2.json', 'citations_path': 'file_storage/functions.query_db:5.json'}, 'var_functions.execute_python:14': [], 'var_functions.execute_python:16': {'first_filename': 'A Lived Informatics Model of Personal Informatics.txt', 'total_papers': 5, 'total_citations': 1405, 'citation_sample': {'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}}, 'var_functions.execute_python:18': {'papers_parsed': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'contribution': 'theoretical', 'text_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'contribution': 'survey', 'text_snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'contribution': 'empirical', 'text_snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'contribution': 'empirical', 'text_snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'contribution': 'artifact', 'text_snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C'}], 'citation_totals_sample': {'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing': 99, 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies': 188, 'Sundroid: Solar Radiation Awareness with Smartphones': 287, 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity': 368, 'Why We Use and Abandon Smart Devices': 463}}, 'var_functions.execute_python:20': {'empirical_papers_2017_plus': 0, 'citation_totals_size': 259, 'results': []}}

exec(code, env_args)
