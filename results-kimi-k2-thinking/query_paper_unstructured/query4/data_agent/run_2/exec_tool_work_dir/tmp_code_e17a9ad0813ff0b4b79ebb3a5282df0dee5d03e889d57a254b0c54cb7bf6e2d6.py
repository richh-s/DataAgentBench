code = """import json
import pandas as pd
import re

# Process papers data from earlier MongoDB query
paper_docs = locals()['var_functions.query_db:2']

# Read the full paper data
with open(paper_docs, 'r', encoding='utf-8') as f:
    papers_data = json.load(f)

# Load citation data
citations_file = locals()['var_functions.query_db:14']
with open(citations_file, 'r', encoding='utf-8') as f:
    citations_data = json.load(f)

# Make citations dictionary
citations_map = {}
for item in citations_data:
    citations_map[item['title']] = int(item['total_citations'])

# Process papers DataFrame
df_papers = pd.DataFrame(papers_data)
# Title is filename without .txt
df_papers['title'] = df_papers['filename'].str.replace('.txt$', '', regex=True)

# Extract year function
import re

def extract_year(text):
    patterns = [
        r'(\d{4})\s+(?:CHI|Proceedings|Ubicomp|CSCW|Conference|Symposium|Workshop|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)',
        r'(?:CHI|Ubicomp|CSCW|DIS) (\d{4})',
        r'\b(201[0-9]|202[0-9])\b'
    ]
    for pattern in patterns:
        matches = re.findall(pattern, text)
        if matches:
            return int(matches[0])
    return None

df_papers['year'] = df_papers['text'].apply(extract_year)

# Filter 2016
df_2016 = df_papers[df_papers['year'] == 2016]

# Physical activity papers via keyword search
keywords = ['physical activity', 'fitness', 'exercise', 'activity tracking', 'steps', 'step count', 'walking', 'running', 'sports']

def is_physics_activity(text):
    text_lower = text.lower()
    return any(word in text_lower for word in keywords)

pa_papers = df_2016[df_2016['text'].apply(is_physics_activity)]['title'].tolist()

# Get citations
result = []
for title in pa_papers:
    total_citation = citations_map.get(title, 0)
    result.append({'title': title, 'total_citations': total_citation})

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'num_2016_pa_papers': 13, 'titles': ['Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'Designing in the Dark: Eliciting Self-tracking Dimensions for Understanding Enigmatic Disease', 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats', 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'Heed: Exploring the Design of Situated Self-Reporting Devices', 'Personal Tracking of Screen Time on Digital Devices', 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis', 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model', 'TimeAware: Leveraging Framing Effects to Enhance Personal Productivity', 'Understanding Personal Productivity: How Knowledge Workers Define, Evaluate, and Reflect on Their Productivity'], 'all_2016_titles': ['Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'Designing in the Dark: Eliciting Self-tracking Dimensions for Understanding Enigmatic Disease', 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats', 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'Heed: Exploring the Design of Situated Self-Reporting Devices', 'Personal Tracking of Screen Time on Digital Devices', 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis', 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model', 'TimeAware: Leveraging Framing Effects to Enhance Personal Productivity', 'Understanding Personal Productivity: How Knowledge Workers Define, Evaluate, and Reflect on Their Productivity']}, 'var_functions.query_db:10': [], 'var_functions.query_db:12': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
