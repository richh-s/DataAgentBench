code = """import json
import re

# Load all papers with physical activity
file_path = locals()['var_functions.query_db:34']

with open(file_path, 'r') as f:
    pa_papers = json.load(f)

print(f"Total physical activity papers: {len(pa_papers)}")

# Define patterns to identify 2016 papers
year_patterns = [
    # Look for publication headers with 2016
    re.compile(r'CHI\s+2016', re.IGNORECASE),
    re.compile(r'UbiComp\s+2016', re.IGNORECASE),
    re.compile(r'Ubicomp\s+2016', re.IGNORECASE),
    re.compile(r'CSCW\s+2016', re.IGNORECASE),
    re.compile(r'DIS\s+2016', re.IGNORECASE),
    re.compile(r'PervasiveHealth\s+2016', re.IGNORECASE),
    re.compile(r'WWW\s+2016', re.IGNORECASE),
    re.compile(r'IUI\s+2016', re.IGNORECASE),
    re.compile(r'OzCHI\s+2016', re.IGNORECASE),
    re.compile(r'TEI\s+2016', re.IGNORECASE),
    re.compile(r'AH\s+2016', re.IGNORECASE),
    # Copyright year 2016
    re.compile(r'Copyright[^\n]*2016', re.IGNORECASE),
    # Published in 2016
    re.compile(r'Published[^\n]*2016', re.IGNORECASE),
]

# Also look for standalone 2016 but be more careful
standalone_2016 = re.compile(r'\b2016\b')

papers_2016 = []

for paper in pa_papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Check if it's likely a 2016 publication
    has_venue_2016 = any(pattern.search(text) for pattern in year_patterns)
    
    if has_venue_2016:
        # Verify it's about physical activity (not just a passing mention)
        # Check if "physical activity" appears near domain-related terms
        pa_matches = [(m.start(), m.end()) for m in re.finditer(r'physical activity', text, re.IGNORECASE)]
        
        if pa_matches:
            title = filename.replace('.txt', '') if filename else ''
            papers_2016.append({
                'title': title,
                'filename': filename
            })

print(f"Found {len(papers_2016)} papers from 2016 in physical activity domain:")
for p in papers_2016:
    print(f"- {p['title']}")

# Output the list
result = papers_2016
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.execute_python:10': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:18': [{'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'Why We Use and Abandon Smart Devices'}, {'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App'}, {'title': 'Reviewing Reflection: On the Use of Reflection in Interactive System Design'}, {'title': 'Beyond Self-Tracking and Reminders: Designing Smartphone Apps That Support Habit Formation'}, {'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection'}, {'title': 'Barriers to Engagement with a Personal Informatics Productivity Tool'}, {'title': 'How to Drive a London Bus: Measuring Performance in a Mobile and Remote Workplace'}, {'title': 'Sitting in the Same Boat: A Case Study of a Combined Awareness System and Behaviour Change Technology'}, {'title': 'A Lived Informatics Model of Personal Informatics'}, {'title': 'Sensor Requirements for Activity Recognition on Smart Watches'}, {'title': 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture'}, {'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling'}, {'title': 'Social Fabric Fitness: The Design and Evaluation of Wearable E-textile Displays to Support Group Running'}, {'title': 'Live Interest Meter: Learning from Quantified Feedback in Mass Lectures'}, {'title': 'MoodLight: Exploring Personal and Social Implications of Ambient Display of Biosensor Data'}, {'title': 'The Power of Mobile Notifications to Increase Wellbeing Logging Behavior'}, {'title': 'Pass the Ball: Enforced Turn-Taking in Activity Tracking'}, {'title': 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': [{'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt'}, {'title': 'Charting Design Preferences on Wellness Wearables', 'filename': 'Charting Design Preferences on Wellness Wearables.txt'}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'filename': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt"}, {'title': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'filename': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness.txt'}, {'title': 'Technologies for Everyday Life Reflection: Illustrating a Design Space', 'filename': 'Technologies for Everyday Life Reflection: Illustrating a Design Space.txt'}, {'title': 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating', 'filename': 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating.txt'}], 'var_functions.query_db:24': [{'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'total_citations': '636'}, {'title': 'Charting Design Preferences on Wellness Wearables', 'total_citations': '269'}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'total_citations': '466'}, {'title': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'total_citations': '153'}, {'title': 'Technologies for Everyday Life Reflection: Illustrating a Design Space', 'total_citations': '358'}, {'title': 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating', 'total_citations': '143'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:30': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'Charting Design Preferences on Wellness Wearables'], 'var_functions.query_db:32': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': '265'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': '266'}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'total_citations': '271'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json'}

exec(code, env_args)
