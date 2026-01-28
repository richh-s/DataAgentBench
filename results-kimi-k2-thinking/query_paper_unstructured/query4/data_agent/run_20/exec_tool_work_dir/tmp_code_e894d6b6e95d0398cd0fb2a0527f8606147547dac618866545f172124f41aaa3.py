code = """import json
import re

# Load the physical activity papers data
file_path = locals()['var_functions.query_db:20']

with open(file_path, 'r') as f:
    pa_papers = json.load(f)

print(f"Total physical activity papers retrieved: {len(pa_papers)}")

# Look for 2016 publication year patterns
# Common patterns: "2016", "'16", "CHI 2016", "UbiComp 2016", etc.
year_patterns = [
    re.compile(r'\b2016\b'),
    re.compile(r"16\b"),
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
]

papers_2016 = []

for paper in pa_papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Check if any year pattern matches
    has_2016 = any(pattern.search(text) for pattern in year_patterns)
    
    if has_2016:
        title = filename.replace('.txt', '') if filename else ''
        papers_2016.append({
            'title': title,
            'filename': filename
        })

print(f"Physical activity papers from 2016: {len(papers_2016)}")
for p in papers_2016:
    print(f"- {p['title']}")

# Output the list
result = papers_2016
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.execute_python:10': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:18': [{'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'Why We Use and Abandon Smart Devices'}, {'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App'}, {'title': 'Reviewing Reflection: On the Use of Reflection in Interactive System Design'}, {'title': 'Beyond Self-Tracking and Reminders: Designing Smartphone Apps That Support Habit Formation'}, {'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection'}, {'title': 'Barriers to Engagement with a Personal Informatics Productivity Tool'}, {'title': 'How to Drive a London Bus: Measuring Performance in a Mobile and Remote Workplace'}, {'title': 'Sitting in the Same Boat: A Case Study of a Combined Awareness System and Behaviour Change Technology'}, {'title': 'A Lived Informatics Model of Personal Informatics'}, {'title': 'Sensor Requirements for Activity Recognition on Smart Watches'}, {'title': 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture'}, {'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling'}, {'title': 'Social Fabric Fitness: The Design and Evaluation of Wearable E-textile Displays to Support Group Running'}, {'title': 'Live Interest Meter: Learning from Quantified Feedback in Mass Lectures'}, {'title': 'MoodLight: Exploring Personal and Social Implications of Ambient Display of Biosensor Data'}, {'title': 'The Power of Mobile Notifications to Increase Wellbeing Logging Behavior'}, {'title': 'Pass the Ball: Enforced Turn-Taking in Activity Tracking'}, {'title': 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
