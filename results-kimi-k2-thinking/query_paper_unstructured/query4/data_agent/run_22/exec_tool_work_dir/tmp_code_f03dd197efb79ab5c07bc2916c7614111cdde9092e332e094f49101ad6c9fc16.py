code = """import json
import re

# Read the papers from file
papers_path = "file_storage/functions.query_db:38.json"
with open(papers_path, 'r') as f:
    papers = json.load(f)

print(f"Total papers loaded: {len(papers)}")

# Process papers to extract title, year, and physical activity status
processed_papers = []

for paper in papers:
    filename = paper['filename']
    text = paper['text']
    
    # Extract title
    title = filename.replace('.txt', '')
    
    # Extract year - try multiple patterns
    year = None
    
    # Pattern 1: Look for venue with year like "CHI 2016" or "UBICOMP '16"
    venue_patterns = [
        r'(CHI|Ubi[Ss]?y?\s*Comp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UBICOMP)\s*[\'"′]?(\d{2})\b',
        r'(CHI|Ubi[Ss]?y?\s*Comp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s+(20\d{2})\b',
    ]
    
    for pattern in venue_patterns:
        match = re.search(pattern, text)
        if match:
            yr = match.group(2)
            if yr.startswith('20'):
                year = int(yr)
            else:
                year = int('20' + yr)
            break
    
    # Pattern 2: If no venue pattern, look for any 4-digit year 2010-2025
    if not year:
        year_match = re.search(r'\b(20(?:1[0-9]|2[0-5]))\b', text)
        if year_match:
            year = int(year_match.group(1))
    
    # Check for physical activity domain
    is_physical_activity = 'physical activity' in text.lower()
    
    processed_papers.append({
        'title': title,
        'year': year,
        'is_physical_activity': is_physical_activity
    })

# Filter for 2016 physical activity papers
papers_2016 = [p for p in processed_papers if p['year'] == 2016 and p['is_physical_activity']]

print(f"Papers from 2016 in physical activity domain: {len(papers_2016)}")
for p in papers_2016:
    print(f"  - {p['title']}")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.execute_python:10': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', 'var_functions.list_db:6', '__builtins__', 'json'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:22': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', 'var_functions.list_db:6', 'var_functions.execute_python:10', 'var_functions.query_db:12', 'var_functions.query_db:14', 'var_functions.query_db:16'], 'var_functions.execute_python:28': {'paper_count': 5, 'first_papers': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'text_preview': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu..."}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'text_preview': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152...'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'text_preview': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali...'}]}, 'var_functions.execute_python:30': {'all_physical_activity_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'is_physical_activity': True, 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'is_physical_activity': True, 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'is_physical_activity': True, 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'is_physical_activity': True, 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'title': 'Barriers to Engagement with a Personal Informatics Productivity Tool', 'year': None, 'is_physical_activity': True, 'filename': 'Barriers to Engagement with a Personal Informatics Productivity Tool.txt'}], 'papers_2016': [], 'total_2016_papers': 0}, 'var_functions.query_db:36': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': [{'citation_year': '2011'}, {'citation_year': '2012'}, {'citation_year': '2013'}, {'citation_year': '2014'}, {'citation_year': '2015'}, {'citation_year': '2016'}, {'citation_year': '2017'}, {'citation_year': '2018'}, {'citation_year': '2019'}, {'citation_year': '2020'}, {'citation_year': '2021'}, {'citation_year': '2022'}, {'citation_year': '2023'}, {'citation_year': '2024'}, {'citation_year': '2025'}]}

exec(code, env_args)
