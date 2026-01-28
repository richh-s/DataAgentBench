code = """import json
import pandas as pd
import re

# Read the MongoDB data from the file
storage_key = 'var_functions.query_db:2'
file_path = locals()[storage_key]

with open(file_path, 'r') as f:
    mongo_data = json.load(f)

# Process all documents to extract title, year, and check for empirical contribution
papers_info = []

for doc in mongo_data:
    # Get title from filename
    filename = doc.get('filename', '')
    if not filename:
        continue
        
    title = filename.replace('.txt', '')
    text = doc.get('text', '')
    
    if not text:
        continue
    
    # Try to extract year from text
    year = None
    
    # Pattern 1: Look for year in format 20XX (2017-2025)
    year_match = re.search(r'\b(20(1[7-9]|[2-9]\d))\b', text[:2000])
    if year_match:
        year = int(year_match.group(1))
    
    # Pattern 2: Look for conference year formats like '17, '18
    if not year:
        conf_match = re.search(r"(?:CHI|UbiComp|UBICOMP|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*'?(\d{2})\b", text[:2000], re.IGNORECASE)
        if conf_match:
            year_num = int(conf_match.group(1))
            if year_num >= 17:  # 2017 onwards
                year = 2000 + year_num
    
    # Pattern 3: Look for full year with venue names
    if not year:
        full_year_match = re.search(r"(CHI|UbiComp|UBICOMP|CSCW|DIS|PervasiveHealth|WWW|IUI)\s+(20(1[7-9]|[2-9]\d))\b", text[:2000], re.IGNORECASE)
        if full_year_match:
            year = int(full_year_match.group(2))
    
    # Check if paper has empirical contribution based on content
    text_lower = text.lower()
    
    # Empirical indicators - multiple approaches
    empirical_keywords = ['empirical', 'study', 'experiment', 'user study', 'field study', 'evaluation', 'participants', 'survey', 'interview', 'data collection', 'quantitative', 'qualitative', 'evaluation study']
    
    # Count keyword occurrences, excluding false positives
    keyword_score = 0
    for keyword in empirical_keywords:
        if keyword in text_lower:
            # Skip false positives
            if keyword == 'study' and ('case study' in text_lower or 'further study' in text_lower):
                continue
            keyword_score += 1
    
    # Additional check - look for methodology sections
    has_methodology = 'method' in text_lower or 'methodology' in text_lower or 'procedure' in text_lower or 'data analysis' in text_lower
    
    # Determine if empirical
    is_empirical = False
    if keyword_score >= 3 or (keyword_score >= 2 and has_methodology):
        is_empirical = True
    
    # Only keep papers after 2016 that are empirical
    if year and year > 2016 and is_empirical:
        papers_info.append({
            'title': title,
            'year': year,
            'is_empirical': True
        })

# Create DataFrame
if papers_info:
    empirical_df = pd.DataFrame(papers_info)
    
    print('__RESULT__:')
    print(json.dumps({
        'empirical_papers_after_2016': len(papers_info),
        'papers': papers_info[:20],  # First 20 as sample
        'year_distribution': empirical_df['year'].value_counts().sort_index().to_dict()
    }))
else:
    print('__RESULT__:')
    print(json.dumps({
        'empirical_papers_after_2016': 0,
        'papers': [],
        'message': 'No empirical papers found after 2016 in this dataset'
    }))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'message': 'No empirical papers found after 2016', 'empirical_papers': []}, 'var_functions.execute_python:12': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'title': 'A Lived Informatics Model of Personal Informatics', 'year_matches': [], 'text_preview': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'title': 'A Stage-based Model of Personal Informatics Systems', 'year_matches': [], 'text_preview': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year_matches': [], 'text_preview': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year_matches': [], 'text_preview': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year_matches': [], 'text_preview': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C'}], 'var_functions.execute_python:14': {'papers_after_2016': 0, 'empirical_papers_after_2016': 0, 'message': 'No papers found after 2016'}, 'var_functions.execute_python:16': {'total_papers': 5, 'sample_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}, 'var_functions.list_db:18': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
