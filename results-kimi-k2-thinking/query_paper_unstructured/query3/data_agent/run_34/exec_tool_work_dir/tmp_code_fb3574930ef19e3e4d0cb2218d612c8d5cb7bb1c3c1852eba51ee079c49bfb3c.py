code = """import json
import pandas as pd
import re

# Read the MongoDB data from the file
storage_key = 'var_functions.query_db:2'
file_path = locals()[storage_key]

with open(file_path, 'r') as f:
    mongo_data = json.load(f)

# Process all documents to extract title and publication year
papers = []

for doc in mongo_data:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '')
    
    year = None
    
    # Method 1: Look for patterns like '2017', '2018' in the first 500 chars
    year_match = re.search(r'\b20(1[7-9]|[2-9]\d)\b', text[:1000])
    if year_match:
        year = int(year_match.group(0))
    
    # Method 2: Look for conference patterns like 'UBICOMP '17', 'CHI 2018'
    if not year:
        conf_match = re.search(r"(?:CHI|UbiComp|UBICOMP|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*'?(\d{2})\b", text[:1000], re.IGNORECASE)
        if conf_match:
            year_str = conf_match.group(1)
            if year_str.startswith('1') or year_str.startswith('2') or year_str.startswith('3'):
                year = int('20' + year_str)
            elif year_str.startswith('9'):
                year = int('19' + year_str)
    
    # Method 3: Look for full year in conference abbreviations
    if not year:
        conf_year_match = re.search(r"(?:CHI|UbiComp|UBICOMP|CSCW|DIS|PervasiveHealth|WWW)\s+(20[12][0-9])\b", text[:1000], re.IGNORECASE)
        if conf_year_match:
            year = int(conf_year_match.group(1))
    
    if year and year > 2016:
        papers.append({
            'title': title,
            'year': year
        })

# Count by year
if papers:
    df = pd.DataFrame(papers)
    year_counts = df['year'].value_counts().sort_index()
    
    # Check for empirical indicators in these papers
    empirical_count = 0
    empirical_titles = []
    
    for doc in mongo_data:
        filename = doc.get('filename', '')
        title = filename.replace('.txt', '') if filename else ''
        
        # Find if paper is in our >2016 list
        if title in [p['title'] for p in papers]:
            text = doc.get('text', '')
            text_lower = text.lower()
            
            # Simple check for empirical indicators
            empirical_terms = ['empirical', 'study', 'experiment', 'evaluation', 'participants', 'user study', 'survey', 'interview', 'data collection']
            domain_indicators = ['participants', 'n=', 'quantitative', 'qualitative', 'statistical', 'results showed', 'finding']
            
            empirical_score = sum(1 for term in empirical_terms if term in text_lower)
            domain_score = sum(1 for term in domain_indicators if term in text_lower)
            
            # If paper has empirical terms and domain-specific language, classify as empirical
            if empirical_score >= 2 or (empirical_score >= 1 and domain_score >= 2):
                empirical_count += 1
                empirical_titles.append(title)
    
    print('__RESULT__:')
    print(json.dumps({
        'papers_after_2016': len(papers),
        'empirical_papers_after_2016': empirical_count,
        'sample_empirical_titles': empirical_titles[:10]
    }))
else:
    print('__RESULT__:')
    print(json.dumps({
        'papers_after_2016': 0,
        'empirical_papers_after_2016': 0,
        'message': 'No papers found after 2016'
    }))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'message': 'No empirical papers found after 2016', 'empirical_papers': []}, 'var_functions.execute_python:12': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'title': 'A Lived Informatics Model of Personal Informatics', 'year_matches': [], 'text_preview': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'title': 'A Stage-based Model of Personal Informatics Systems', 'year_matches': [], 'text_preview': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year_matches': [], 'text_preview': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year_matches': [], 'text_preview': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year_matches': [], 'text_preview': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C'}]}

exec(code, env_args)
