code = """import json
import re
# Read the full papers data
full_papers_path = var_functions.query_db:5
with open(full_papers_path, 'r') as f:
    papers_data = json.load(f)
    
def extract_paper_info(text, filename):
    # Get title from filename
    title = filename.replace('.txt', '')
    
    # Search for year patterns
    year_matches = re.findall(r'\s\'?(1[9-9][0-9]{2}|20[0-9]{2})\'?', text)
    year = None
    if year_matches:
        years = [int(y) for y in year_matches if 1900 <= int(y) <= 2100]
        if years:
            year = max(years)
    
    # Check for empirical contribution
    has_empirical = bool(re.search(r'empirical', text, re.IGNORECASE))
    
    if not has_empirical:
        empirical_indicators = [
            r'user study', r'participant', r'survey of', r'interview', 
            r'experiment', r'evaluation', r'field study', r'case study',
            r'empirical evaluation', r'empirical study'
        ]
        has_empirical = bool(re.search('|'.join(empirical_indicators), text, re.IGNORECASE))
    
    return {
        'title': title,
        'year': year,
        'has_empirical': has_empirical
    }

processed_papers = []
for paper in papers_data:
    info = extract_paper_info(paper.get('text', ''), paper.get('filename', ''))
    if info['title'] and info['year'] and info['has_empirical']:
        processed_papers.append(info)

papers_after_2016 = [p for p in processed_papers if p['year'] > 2016]

print('__RESULT__:')
print(json.dumps({
    'total_papers': len(processed_papers),
    'papers_after_2016': len(papers_after_2016),
    'sample_papers': papers_after_2016[:10]
}))"""

env_args = {'var_functions.query_db:0': [{'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86e', 'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}, {'_id': '694f5530284b10b11dc0a873', 'filename': 'Charting Design Preferences on Wellness Wearables.txt'}, {'_id': '694f5530284b10b11dc0a875', 'filename': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt"}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}]}

exec(code, env_args)
