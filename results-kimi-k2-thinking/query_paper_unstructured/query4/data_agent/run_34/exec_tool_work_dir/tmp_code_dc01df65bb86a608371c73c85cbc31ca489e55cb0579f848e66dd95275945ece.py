code = """import json
import re

# Read all papers
with open(locals()['var_functions.query_db:28'], 'r') as f:
    all_papers = json.load(f)

print('Total papers in database:', len(all_papers))

# Function to extract year from text
def extract_year(text):
    # Look for patterns like YYYY, 'YY, or YYYY in headers
    year_patterns = [
        r'\b(20\d{2})\b',  # 20xx
        r"'\b(\d{2})\b",   # 'xx
    ]
    
    # Look in the first 2000 characters (usually header)
    header = text[:2000]
    
    for pattern in year_patterns:
        matches = re.findall(pattern, header)
        for match in matches:
            # Convert 'xx to 20xx
            if len(match) == 2:
                year = int('20' + match)
            else:
                year = int(match)
            # Filter reasonable years for HCI papers (2000-2025)
            if 2000 <= year <= 2025:
                return year
    return None

# Find papers that mention physical activity AND have year 2016
physical_activity_2016 = []
for paper in all_papers:
    text = paper.get('text', '').lower()
    if 'physical activity' in text:
        year = extract_year(paper.get('text', ''))
        if year == 2016:
            title = paper['filename'].replace('.txt', '')
            physical_activity_2016.append({
                'title': title,
                'id': paper['_id'],
                'year': year
            })

print('__RESULT__:')
print(json.dumps({
    'total_papers': len(all_papers),
    'physical_activity_2016_papers': physical_activity_2016,
    'count': len(physical_activity_2016)
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'count': 5}, 'var_functions.query_db:8': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.execute_python:10': {'titles': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'Charting Design Preferences on Wellness Wearables'], 'count': 5}, 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'physical_activity_papers_count': 5, 'papers_2016_count': 2, 'papers_2016': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'id': '694f5530284b10b11dc0a86b'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'id': '694f5530284b10b11dc0a86c'}]}, 'var_functions.query_db:20': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': '265', 'citation_years': '5'}], 'var_functions.execute_python:22': 'file_storage/functions.execute_python:22.json', 'var_functions.query_db:24': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': '265', 'citation_years': '5'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': '266', 'citation_years': '6'}], 'var_functions.execute_python:26': {'total_pa_papers': 5, 'papers_2016': []}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.list_db:30': ['paper_docs']}

exec(code, env_args)
