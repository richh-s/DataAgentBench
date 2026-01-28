code = """import json
import re

# Load the papers data
papers_raw = locals().get('var_functions.query_db:18')
if not papers_raw:
    print("Error: papers data not found")
    exit(1)

# Parse papers data
papers_data = []
if isinstance(papers_raw, str):
    try:
        # First try loading as JSON
        papers_data = json.loads(papers_raw)
    except:
        # If fails, read as file path
        with open(papers_raw, 'r') as f:
            papers_data = json.load(f)
else:
    papers_data = papers_raw

print(f"Processing {len(papers_data)} papers")

# Function to extract paper info
def extract_paper_info(paper):
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    title = filename.replace('.txt', '').strip()
    
    # Extract year
    year = None
    years = []
    
    # Find 4-digit years
    for ym in re.findall(r'\b(19\d{2}|20\d{2})\b', text):
        y = int(ym)
        if 1900 <= y <= 2100:
            years.append(y)
    
    # Find short years like '15, '16
    for sm in re.findall(r"'(\d{2})", text):
        y = 2000 + int(sm) if int(sm) < 50 else 1900 + int(sm)
        if 1900 <= y <= 2100:
            years.append(y)
    
    if years:
        year = max(years)
    
    # Check for empirical contribution
    has_empirical = False
    text_lower = text.lower()
    
    # Check direct empirical mention
    if 'empirical' in text_lower:
        has_empirical = True
    
    # Check other empirical indicators
    if not has_empirical:
        indicators = [
            'user stud', 'field stud', 'interview', 'survey ',
            'questionnaire', 'evaluation studied', 'evaluation of',
            'experiment', 'participant', 'case stud', 'qualitative',
            'longitudinal stud', 'follow-up stud', 'focus group',
            'user centered', 'human centered', 'usability test'
        ]
        for indicator in indicators:
            if indicator in text_lower:
                has_empirical = True
                break
    
    return {
        'title': title,
        'year': year,
        'has_empirical': has_empirical
    }

# Process papers
papers_info = []
for paper in papers_data:
    info = extract_paper_info(paper)
    if info['title'] and info['year']:
        papers_info.append(info)

# Filter for empirical papers after 2016
empirical_papers = [p for p in papers_info if p['year'] > 2016 and p['has_empirical']]

print(f"Found {len(empirical_papers)} empirical papers after 2016")

result = {
    'total_papers': len(papers_info),
    'empirical_papers_after_2016': len(empirical_papers),
    'papers': [{'title': p['title'], 'year': p['year']} for p in empirical_papers]
}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_functions.query_db:0': [{'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86e', 'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}, {'_id': '694f5530284b10b11dc0a873', 'filename': 'Charting Design Preferences on Wellness Wearables.txt'}, {'_id': '694f5530284b10b11dc0a875', 'filename': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt"}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.execute_python:16': {'total_processed': 99, 'empirical_after_2016': 0, 'sample_empirical': []}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
