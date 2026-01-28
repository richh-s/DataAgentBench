code = """import json

# Load data files
mongo_file = var_functions.query_db:14
citation_file = var_functions.query_db:52

with open(mongo_file, 'r') as f:
    papers = json.load(f)

with open(citation_file, 'r') as f:
    citations = json.load(f)

print('Papers loaded:', len(papers))
print('Citation records loaded:', len(citations))

# Find 2016 physical activity papers
papers_2016 = []
for paper in papers:
    text = paper['text']
    filename = paper['filename']
    
    if '2016' in text[:3000] and 'physical activity' in text.lower():
        title = filename.replace('.txt', '')
        papers_2016.append(title)

print('2016 physical activity papers:', len(papers_2016))

# Match with citations
results = []
for title in papers_2016:
    for citation in citations:
        if citation['title'] == title:
            results.append({
                'title': title,
                'total_citations': int(citation['total_citations'])
            })

print('Matched with citations:', len(results))

result_str = json.dumps(results)
print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:10': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.list_db:12': ['paper_docs'], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:22': [], 'var_functions.query_db:26': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing'}, {'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:48': [{'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'total_citations': '221'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'total_citations': '259'}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'total_citations': '349'}, {'title': 'Fine-grained Sharing of Sensed Physical Activity: A Value Sensitive Approach', 'total_citations': '98'}, {'title': 'Low Sampling Rate for Physical Activity Recognition', 'total_citations': '348'}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure", 'total_citations': '542'}, {'title': 'Move into Another World of Happy: Insights for Designing Affect-based Physical Activity Interventions', 'total_citations': '107'}, {'title': 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity', 'total_citations': '12'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'total_citations': '335'}, {'title': 'SweatAtoms: Materializing Physical Activity', 'total_citations': '428'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity', 'total_citations': '180'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', 'total_citations': '278'}, {'title': 'Understanding Physical Activity Through 3D Printed Material Artifacts', 'total_citations': '46'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity', 'total_citations': '358'}], 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json'}

exec(code, env_args)
