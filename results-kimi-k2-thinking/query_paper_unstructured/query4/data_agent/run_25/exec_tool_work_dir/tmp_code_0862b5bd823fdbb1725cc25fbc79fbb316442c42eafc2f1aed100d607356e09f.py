code = """import json

# Read the full citation data from file
citation_file_path = '/tmp/tmp2h3j9g2q.json'
with open(citation_file_path, 'r') as f:
    all_citations = json.load(f)

# Group citations by title and sum the counts
citation_totals = {}
for record in all_citations:
    title = record['title']
    count = int(record['citation_count'])
    citation_totals[title] = citation_totals.get(title, 0) + count

print('Total unique papers in citations:', len(citation_totals))
print('Sample citation totals:')
for i, (title, count) in enumerate(list(citation_totals.items())[:5]):
    print(f'  {title}: {count}')

print('__RESULT__:')
print(json.dumps({'total_papers': len(citation_totals), 'sample': dict(list(citation_totals.items())[:5])}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:14': [{'id': '73', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '90', 'citation_year': '2017'}, {'id': '74', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '88', 'citation_year': '2018'}, {'id': '75', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '83', 'citation_year': '2019'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '77', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '78', 'citation_year': '2021'}, {'id': '194', 'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'citation_count': '57', 'citation_year': '2019'}, {'id': '195', 'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'citation_count': '67', 'citation_year': '2020'}, {'id': '196', 'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'citation_count': '58', 'citation_year': '2021'}, {'id': '197', 'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'citation_count': '16', 'citation_year': '2022'}, {'id': '198', 'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'citation_count': '32', 'citation_year': '2023'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': [{'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt'}, {'filename': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt"}, {'filename': 'Charting Design Preferences on Wellness Wearables.txt'}], 'var_functions.execute_python:32': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'Charting Design Preferences on Wellness Wearables'], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
