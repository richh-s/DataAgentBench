code = """import json

citations_path = locals()['var_functions.query_db:16']
with open(citations_path, 'r') as f:
    citations = json.load(f)

print('Total citations:', len(citations))

physical_papers = []
for cit in citations:
    title = cit.get('title', '').lower()
    count = int(cit.get('citation_count', 0))
    orig_title = cit.get('title', '')
    
    has_keyword = any(keyword in title for keyword in ['physical activity', 'fitness', 'exercise', 'activity tracking', 'wearable'])
    
    if has_keyword or ('activity' in title and 'track' in title):
        physical_papers.append({'title': orig_title, 'citation_count': count})

print('Found physical activity papers:', len(physical_papers))

# Sort by citation count
def get_count(p):
    return p['citation_count']

physical_papers.sort(key=get_count, reverse=True)

for paper in physical_papers[:10]:
    print(paper['title'], paper['citation_count'])

output = physical_papers
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'paper_count': 5, 'sample_keys': ['_id', 'filename', 'text'], 'sample_filename': 'A Lived Informatics Model of Personal Informatics.txt'}, 'var_functions.execute_python:14': {'all_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': 2015, 'domain': ['physical activity', 'food', 'finances'], 'venue': ['CHI', 'Ubicomp', 'CSCW'], 'source': ['ACM'], 'contribution': ['empirical', 'artifact', 'theoretical']}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'domain': ['physical activity', 'food', 'sleep', 'finances'], 'venue': ['CHI', 'Ubicomp'], 'source': ['ACM', 'IEEE'], 'contribution': ['empirical', 'artifact', 'theoretical']}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2016, 'domain': ['physical activity', 'sleep', 'mental'], 'venue': ['CHI'], 'source': ['ACM'], 'contribution': ['empirical', 'artifact', 'theoretical']}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2016, 'domain': ['physical activity', 'food', 'mental'], 'venue': ['CHI'], 'source': ['ACM', 'IEEE'], 'contribution': ['empirical', 'artifact', 'theoretical']}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': 2016, 'domain': ['food', 'sleep'], 'venue': ['CHI'], 'source': ['ACM', 'IEEE'], 'contribution': ['empirical', 'artifact', 'theoretical']}], 'papers_2016_physical_activity': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2016, 'domain': ['physical activity', 'sleep', 'mental'], 'venue': ['CHI'], 'source': ['ACM'], 'contribution': ['empirical', 'artifact', 'theoretical']}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2016, 'domain': ['physical activity', 'food', 'mental'], 'venue': ['CHI'], 'source': ['ACM', 'IEEE'], 'contribution': ['empirical', 'artifact', 'theoretical']}]}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': []}

exec(code, env_args)
