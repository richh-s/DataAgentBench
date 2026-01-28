code = """import json

papers_all_path = locals()['var_functions.query_db:10']
with open(papers_all_path, 'r') as f:
    all_papers = json.load(f)

citations_path = locals()['var_functions.query_db:2']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

citations_dict = {}
for item in citations_data:
    citations_dict[item['title']] = int(item['total_citations'])

print('Total papers:', len(all_papers))
print('Total papers with citations:', len(citations_dict))

sample_papers = all_papers[:3]
for i, paper in enumerate(sample_papers):
    filename = paper['filename']
    title = filename.replace('.txt', '')
    has_citations = title in citations_dict
    print('\nPaper', i+1)
    print('Title:', title)
    print('Has citations:', has_citations)
    if has_citations:
        print('Citations:', citations_dict[title])

print('__RESULT__:')
print('Debug info printed')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:4': [{'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'total_citations': 636}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'total_citations': 271}, {'title': 'Charting Design Preferences on Wellness Wearables', 'total_citations': 269}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': 266}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': 265}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': [{'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'total_citations': 452}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': 266}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': 265}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [], 'var_functions.execute_python:22': []}

exec(code, env_args)
