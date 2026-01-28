code = """import json
import re

# Load data
paper_docs_path = locals()['var_functions.query_db:2']
citations_path = locals()['var_functions.query_db:24']

with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

with open(citations_path, 'r') as f:
    citation_totals = json.load(f)

# Build citation lookup
citation_lookup = {rec['title']: int(rec['total_citations']) for rec in citation_totals}

# Process papers with better year extraction
results = []

for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    if not text or not title:
        continue
    
    # Extract year with multiple patterns
    year = None
    
    # Pattern 1: Four digit year 2017-2029 anywhere in text
    year_match = re.search(r"\b(201[7-9]|202[0-9])\b", text)
    if year_match:
        year = int(year_match.group(1))
    
    # Pattern 2: Venue format: CHI '17, Ubicomp '18, etc.
    if year is None:
        match = re.search(r"\b(CHI|UBICOMP|CSCW|DIS)\s*'\s*(1[7-9]|2[0-9])\b", text, re.IGNORECASE)
        if match:
            year_suffix = match.group(2)
            if year_suffix.startswith('1'):
                year = int(f"201{year_suffix[1:]}")
            elif year_suffix.startswith('2'):
                year = int(f"202{year_suffix[1:]}")
    
    # Skip if no year found or year <= 2016
    if year is None or year <= 2016:
        continue
    
    # Check for empirical contribution
    text_lower = text.lower()
    
    # Empirical indicators - simpler patterns
    is_empirical = False
    if 'empirical' in text_lower:
        is_empirical = True
    elif 'user study' in text_lower:
        is_empirical = True
    elif 'we surveyed' in text_lower or 'survey' in text_lower:
        is_empirical = True
    elif 'we conducted' in text_lower and ('interview' in text_lower or 'study' in text_lower):
        is_empirical = True
    elif 'participants' in text_lower and ('study' in text_lower or 'survey' in text_lower or 'interview' in text_lower):
        is_empirical = True
    elif 'data collection' in text_lower or 'field study' in text_lower:
        is_empirical = True
    
    # If empirical, add to results
    if is_empirical:
        total_citations = citation_lookup.get(title, 0)
        
        results.append({
            "title": title,
            "year": year,
            "total_citation_count": total_citations
        })

# Sort by citation count descending
results = sorted(results, key=lambda x: x["total_citation_count"], reverse=True)

print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': {'paper_docs_path': 'file_storage/functions.query_db:2.json', 'citations_path': 'file_storage/functions.query_db:5.json'}, 'var_functions.execute_python:14': [], 'var_functions.execute_python:16': {'first_filename': 'A Lived Informatics Model of Personal Informatics.txt', 'total_papers': 5, 'total_citations': 1405, 'citation_sample': {'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}}, 'var_functions.execute_python:18': {'papers_parsed': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'contribution': 'theoretical', 'text_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'contribution': 'survey', 'text_snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'contribution': 'empirical', 'text_snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'contribution': 'empirical', 'text_snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'contribution': 'artifact', 'text_snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C'}], 'citation_totals_sample': {'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing': 99, 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies': 188, 'Sundroid: Solar Radiation Awareness with Smartphones': 287, 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity': 368, 'Why We Use and Abandon Smart Devices': 463}}, 'var_functions.execute_python:20': {'empirical_papers_2017_plus': 0, 'citation_totals_size': 259, 'results': []}, 'var_functions.execute_python:22': {'total_papers': 5, 'citation_totals_size': 259, 'papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'is_empirical': True, 'contrib_patterns': ['theoretical', 'survey'], 'text_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.wash"}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'is_empirical': True, 'contrib_patterns': ['survey'], 'text_snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowled'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'is_empirical': True, 'contrib_patterns': ['empirical', 'survey'], 'text_snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard Unive'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'is_empirical': True, 'contrib_patterns': ['empirical', 'theoretical', 'survey'], 'text_snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  conditi'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'is_empirical': True, 'contrib_patterns': ['artifact'], 'text_snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent Crocher1,3, Frank Vetere1, Suranga Nanayakkara1,4 \n1Microsoft Research Centre for SocialNUI, The Univ'}]}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': []}

exec(code, env_args)
