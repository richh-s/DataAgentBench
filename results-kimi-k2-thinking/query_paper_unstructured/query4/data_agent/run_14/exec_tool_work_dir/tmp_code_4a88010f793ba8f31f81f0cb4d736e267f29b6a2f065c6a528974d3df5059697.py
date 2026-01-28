code = """import json

mongo_result_path = locals()['var_functions.query_db:2']
with open(mongo_result_path, 'r') as f:
    mongo_papers = json.load(f)

sqlite_result_path = locals()['var_functions.query_db:16']
with open(sqlite_result_path, 'r') as f:
    citations = json.load(f)

print('Total MongoDB papers:', len(mongo_papers))
print('Total citations:', len(citations))

papers_2016_physical = []
for paper in mongo_papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    text_lower = paper.get('text', '').lower()
    text_upper = paper.get('text', '').upper()
    
    year = 2016 if '2016' in text_upper else None
    
    if year == 2016 and 'physical activity' in text_lower:
        papers_2016_physical.append(title)

print('2016 physical activity papers from MongoDB:', len(papers_2016_physical))
for t in papers_2016_physical:
    print('  Title:', t)

matches = []
for citation in citations:
    cit_title = citation.get('title', '')
    cit_count = int(citation.get('citation_count', 0))
    
    for paper_title in papers_2016_physical:
        if cit_title == paper_title:
            matches.append({'title': paper_title, 'count': cit_count})

print('Direct matches found:', len(matches))
for m in matches:
    print('  Title:', m['title'], 'Count:', m['count'])

result = matches
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'paper_count': 5, 'sample_keys': ['_id', 'filename', 'text'], 'sample_filename': 'A Lived Informatics Model of Personal Informatics.txt'}, 'var_functions.execute_python:14': {'all_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': 2015, 'domain': ['physical activity', 'food', 'finances'], 'venue': ['CHI', 'Ubicomp', 'CSCW'], 'source': ['ACM'], 'contribution': ['empirical', 'artifact', 'theoretical']}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'domain': ['physical activity', 'food', 'sleep', 'finances'], 'venue': ['CHI', 'Ubicomp'], 'source': ['ACM', 'IEEE'], 'contribution': ['empirical', 'artifact', 'theoretical']}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2016, 'domain': ['physical activity', 'sleep', 'mental'], 'venue': ['CHI'], 'source': ['ACM'], 'contribution': ['empirical', 'artifact', 'theoretical']}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2016, 'domain': ['physical activity', 'food', 'mental'], 'venue': ['CHI'], 'source': ['ACM', 'IEEE'], 'contribution': ['empirical', 'artifact', 'theoretical']}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': 2016, 'domain': ['food', 'sleep'], 'venue': ['CHI'], 'source': ['ACM', 'IEEE'], 'contribution': ['empirical', 'artifact', 'theoretical']}], 'papers_2016_physical_activity': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2016, 'domain': ['physical activity', 'sleep', 'mental'], 'venue': ['CHI'], 'source': ['ACM'], 'contribution': ['empirical', 'artifact', 'theoretical']}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2016, 'domain': ['physical activity', 'food', 'mental'], 'venue': ['CHI'], 'source': ['ACM', 'IEEE'], 'contribution': ['empirical', 'artifact', 'theoretical']}]}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
