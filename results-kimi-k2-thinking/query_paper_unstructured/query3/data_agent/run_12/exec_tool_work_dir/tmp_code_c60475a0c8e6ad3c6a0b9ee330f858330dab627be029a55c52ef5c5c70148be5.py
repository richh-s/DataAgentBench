code = """import json
import re

# Read the full MongoDB query result from the file
file_path = locals()['var_functions.query_db:2']
with open(file_path, 'r') as f:
    papers = json.load(f)

# Search for papers more systematically
empirical_candidates = []

for i, paper in enumerate(papers):
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    title = filename.replace('.txt', '') if filename else ''
    
    # Look for year patterns in the text
    year_matches = re.findall(r"(?:\b|')((?:19|20)\d{2})\b", text)
    
    # Get the most reasonable year (usually the conference year)
    year = None
    if year_matches:
        # Convert to integers and filter for reasonable conference years
        years = [int(y) for y in year_matches if 1970 <= int(y) <= 2030]
        if years:
            # Take the most recent year that appears (likely the publication year)
            year = max(years)
    
    # Check for empirical in text
    text_lower = text.lower()
    has_empirical = 'empirical' in text_lower
    
    if has_empirical:
        empirical_candidates.append({
            'index': i,
            'title': title,
            'year': year,
            'has_empirical': has_empirical
        })

# Filter for post-2016 papers
post_2016_empirical = [p for p in empirical_candidates if p['year'] and p['year'] > 2016]

print('__RESULT__:')
print(json.dumps(post_2016_empirical[:20], indent=2))  # Show first 20 matches"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': [], 'var_functions.list_db:10': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:12': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing'}, {'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity'}], 'var_functions.execute_python:14': [{'index': 0, 'title': 'A Lived Informatics Model of Personal Informatics', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'index': 1, 'title': 'A Stage-based Model of Personal Informatics Systems', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'index': 2, 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'index': 3, 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'index': 4, 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_functions.execute_python:16': [], 'var_functions.execute_python:18': [{'index': 0, 'title': 'A Lived Informatics Model of Personal Informatics', 'text_preview': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, {'index': 1, 'title': 'A Stage-based Model of Personal Informatics Systems', 'text_preview': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152'}, {'index': 2, 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'text_preview': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali'}, {'index': 3, 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'text_preview': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E'}, {'index': 4, 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'text_preview': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C'}]}

exec(code, env_args)
