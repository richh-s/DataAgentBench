code = """import json
import os
import re

# Get the file path from storage
file_path = locals()['var_functions.query_db:26']
print(f"File path: {file_path}")

# Read the JSON file
with open(file_path, 'r') as f:
    papers_data = json.load(f)

print(f"Total papers in database: {len(papers_data)}")

# Check what years appear in the papers
years_found = {}
for paper in papers_data:
    text = paper.get('text', '')
    # Find all 4-digit numbers that could be years
    year_matches = re.findall(r'\b(201[0-9]|202[0-9])\b', text)
    for year in year_matches:
        years_found[year] = years_found.get(year, 0) + 1

print("Years found in papers:")
for year, count in sorted(years_found.items()):
    print(f"  {year}: {count} papers")

# Now find papers from 2016 in physical activity domain
physical_activity_2016 = []
for paper in papers_data:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    
    # Check if 2016 is in the text AND it's a publication year (look for patterns)
    has_2016 = False
    
    # Common patterns for publication years
    patterns = [
        r'2016\s*\n',  # 2016 followed by newline
        r'2016\s*[:.,]',  # 2016 followed by punctuation
        r'CHI\s*2016',  # CHI 2016
        r'Ubicomp\s*2016',  # Ubicomp 2016
        r'CSCW\s*2016',  # CSCW 2016
    ]
    
    for pattern in patterns:
        if re.search(pattern, text, re.IGNORECASE):
            has_2016 = True
            break
    
    # Also check if 2016 appears in the first few lines (header)
    first_lines = '\n'.join(text.split('\n')[:20])
    if '2016' in first_lines:
        has_2016 = True
    
    # Check for physical activity
    has_physical_activity = 'physical activity' in text
    
    if has_2016 and has_physical_activity:
        title = filename.replace('.txt', '')
        physical_activity_2016.append({
            'title': title,
            '_id': paper.get('_id'),
            'filename': filename
        })

print(f"\nFound {len(physical_activity_2016)} papers from 2016 in physical activity domain:")
for p in physical_activity_2016:
    print(f"- {p['title']}")

print('__RESULT__:')
print(json.dumps(physical_activity_2016))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': 'test', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': [], 'var_functions.query_db:22': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity'}, {'title': 'Why We Use and Abandon Smart Devices'}, {'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App'}, {'title': 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set'}, {'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application"}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization"}, {'title': 'Reviewing Reflection: On the Use of Reflection in Interactive System Design'}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching"}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers'}, {'title': 'No Forests Without Trees: Particulars and Patterns in Visualizing Personal Communication'}, {'title': 'Beyond Self-Tracking and Reminders: Designing Smartphone Apps That Support Habit Formation'}, {'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection'}, {'title': 'Barriers to Engagement with a Personal Informatics Productivity Tool'}, {'title': 'Modeling Interdependent and Periodic Real-World Action Sequences'}, {'title': 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video'}, {'title': 'How to Drive a London Bus: Measuring Performance in a Mobile and Remote Workplace'}], 'var_functions.query_db:24': [{'total_records': '1405'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
