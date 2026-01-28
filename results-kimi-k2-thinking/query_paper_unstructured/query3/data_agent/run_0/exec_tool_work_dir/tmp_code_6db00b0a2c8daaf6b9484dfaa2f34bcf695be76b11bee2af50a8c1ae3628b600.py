code = """import json
import re

# Load data
paper_docs_path = locals()['var_functions.query_db:2']
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

# Debug all papers in detail
paper_details = []
for i, doc in enumerate(paper_docs):
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Look for ANY year patterns
    year_patterns = re.findall(r'\b(20\d{2})\b', text)
    
    # Look for venue patterns
    venue_patterns = re.findall(r"(?i)(CHI|UBICOMP|CSCW|DIS|PervasiveHealth|WWW|IUI)\s+'?(\d{2})\b", text)
    
    # Look for copyright
    copyright = re.search(r'(?i)Copyright[^\n]*(20\d{2})', text)
    
    # Check for empirical keywords
    text_lower = text.lower()
    empirical_keywords = ['empirical', 'survey', 'interview', 'study', 'participants', 'experiment', 'evaluation', 'data collection']
    found_keywords = [kw for kw in empirical_keywords if kw in text_lower]
    
    paper_details.append({
        'index': i,
        'title': title,
        'filename': filename,
        'year_patterns': year_patterns,
        'venue_patterns': venue_patterns,
        'copyright_year': copyright.group(1) if copyright else None,
        'empirical_keywords': found_keywords,
        'text_preview': text[:500]
    })

print('__RESULT__:')
print(json.dumps(paper_details, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': {'paper_docs_path': 'file_storage/functions.query_db:2.json', 'citations_path': 'file_storage/functions.query_db:5.json'}, 'var_functions.execute_python:14': [], 'var_functions.execute_python:16': {'first_filename': 'A Lived Informatics Model of Personal Informatics.txt', 'total_papers': 5, 'total_citations': 1405, 'citation_sample': {'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}}, 'var_functions.execute_python:18': {'papers_parsed': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'contribution': 'theoretical', 'text_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'contribution': 'survey', 'text_snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'contribution': 'empirical', 'text_snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'contribution': 'empirical', 'text_snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'contribution': 'artifact', 'text_snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C'}], 'citation_totals_sample': {'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing': 99, 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies': 188, 'Sundroid: Solar Radiation Awareness with Smartphones': 287, 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity': 368, 'Why We Use and Abandon Smart Devices': 463}}, 'var_functions.execute_python:20': {'empirical_papers_2017_plus': 0, 'citation_totals_size': 259, 'results': []}, 'var_functions.execute_python:22': {'total_papers': 5, 'citation_totals_size': 259, 'papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'is_empirical': True, 'contrib_patterns': ['theoretical', 'survey'], 'text_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.wash"}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'is_empirical': True, 'contrib_patterns': ['survey'], 'text_snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowled'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'is_empirical': True, 'contrib_patterns': ['empirical', 'survey'], 'text_snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard Unive'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'is_empirical': True, 'contrib_patterns': ['empirical', 'theoretical', 'survey'], 'text_snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  conditi'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'is_empirical': True, 'contrib_patterns': ['artifact'], 'text_snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent Crocher1,3, Frank Vetere1, Suranga Nanayakkara1,4 \n1Microsoft Research Centre for SocialNUI, The Univ'}]}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': [], 'var_functions.execute_python:30': []}

exec(code, env_args)
