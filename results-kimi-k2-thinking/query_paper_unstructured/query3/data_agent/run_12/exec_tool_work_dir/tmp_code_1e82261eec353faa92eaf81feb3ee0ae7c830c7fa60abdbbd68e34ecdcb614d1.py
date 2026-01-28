code = """import json
import re

# Read the full MongoDB query result from the file
file_path = locals()['var_functions.query_db:2']
with open(file_path, 'r') as f:
    papers = json.load(f)

# Let's extract year more systematically by looking for common conference patterns
year_pattern = r"(?:UBICOMP|CHI|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*'?(\d{2})\b|(?:UBICOMP|CHI|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s+(\d{4})\b|\b(20\d{2})\b"

papers_with_years = []
for i, paper in enumerate(papers):
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year using multiple patterns
    year = None
    
    # Pattern 1: Conference abbreviations with year (e.g., UBICOMP '15, CHI 2016)
    conf_patterns = [
        r"UBICOMP\s*'?(\d{2})\b",
        r"CHI\s*'?(\d{2})\b", 
        r"CSCW\s*'?(\d{2})\b",
        r"DIS\s*'?(\d{2})\b",
        r"PervasiveHealth\s*'?(\d{2})\b",
        r"WWW\s*'?(\d{2})\b",
        r"IUI\s*'?(\d{2})\b",
        r"OzCHI\s*'?(\d{2})\b",
        r"TEI\s*'?(\d{2})\b",
        r"AH\s*'?(\d{2})\b",
        r"UBICOMP\s+(\d{4})\b",
        r"CHI\s+(\d{4})\b",
        r"CSCW\s+(\d{4})\b",
        r"DIS\s+(\d{4})\b",
        r"PervasiveHealth\s+(\d{4})\b",
        r"WWW\s+(\d{4})\b",
        r"IUI\s+(\d{4})\b",
        r"OzCHI\s+(\d{4})\b",
        r"TEI\s+(\d{4})\b",
        r"AH\s+(\d{4})\b"
    ]
    
    for pattern in conf_patterns:
        match = re.search(pattern, text)
        if match:
            year_str = match.group(1)
            if len(year_str) == 2:
                # Convert 2-digit year to 4-digit
                year = 2000 + int(year_str)
            else:
                year = int(year_str)
            break
    
    # Pattern 2: Explicit copyright years
    if not year:
        copyright_match = re.search(r"Copyright\s+\d{4}\\s+(?:\(c\)\s+)?(\d{4})", text)
        if copyright_match:
            year = int(copyright_match.group(1))
    
    # Pattern 3: Any 4-digit year in 2010-2030 range in first 500 chars
    if not year:
        intro_text = text[:500]
        year_matches = re.findall(r"\b(20\d{2})\b", intro_text)
        if year_matches:
            year = int(year_matches[0])
    
    has_empirical = 'empirical' in text.lower()
    
    if has_empirical and year:
        papers_with_years.append({
            'title': title,
            'year': year,
            'has_empirical': has_empirical
        })

# Filter for post-2016
post_2016_empirical = [p for p in papers_with_years if p['year'] > 2016]

result = {
    'all_empirical_with_years': papers_with_years,
    'post_2016_empirical': post_2016_empirical
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': [], 'var_functions.list_db:10': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:12': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing'}, {'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity'}], 'var_functions.execute_python:14': [{'index': 0, 'title': 'A Lived Informatics Model of Personal Informatics', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'index': 1, 'title': 'A Stage-based Model of Personal Informatics Systems', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'index': 2, 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'index': 3, 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'index': 4, 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_functions.execute_python:16': [], 'var_functions.execute_python:18': [{'index': 0, 'title': 'A Lived Informatics Model of Personal Informatics', 'text_preview': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, {'index': 1, 'title': 'A Stage-based Model of Personal Informatics Systems', 'text_preview': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152'}, {'index': 2, 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'text_preview': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali'}, {'index': 3, 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'text_preview': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E'}, {'index': 4, 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'text_preview': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C'}], 'var_functions.execute_python:20': [], 'var_functions.execute_python:24': {'total_empirical_papers': 2, 'empirical_papers': [{'index': 2, 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None}, {'index': 3, 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None}]}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
