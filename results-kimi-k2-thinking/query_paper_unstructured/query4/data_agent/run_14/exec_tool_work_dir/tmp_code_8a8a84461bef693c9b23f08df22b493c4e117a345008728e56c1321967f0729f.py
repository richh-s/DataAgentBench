code = """import json

# Load the citations data
citations_path = locals()['var_functions.query_db:16']
with open(citations_path, 'r') as f:
    citations = json.load(f)

print('Total citations for 2016:', len(citations))
print('First few citation titles:')
for i, cit in enumerate(citations[:5]):
    print(f"  {i+1}. {cit.get('title')}")

# Search for physical activity related papers in the citations
physical_activity_papers = []
keywords = ['physical activity', 'fitness', 'exercise', 'activity tracking', 'wearable', 'motion', 'movement']

for citation in citations:
    title = citation.get('title', '').lower()
    citation_count = int(citation.get('citation_count', 0))
    original_title = citation.get('title', '')
    
    # Check if any keyword is in the title
    is_physical_activity = any(keyword in title for keyword in keywords)
    
    # Also check for combinations like "activity" with "track/monitor/sense"
    if 'activity' in title and any(word in title for word in ['track', 'monitor', 'sense', 'capture', 'recognition', 'wearable']):
        is_physical_activity = True
    
    if is_physical_activity:
        physical_activity_papers.append({
            'title': original_title,
            'citation_count': citation_count
        })

print('\nPhysical activity related papers in 2016 citations:', len(physical_activity_papers))
for paper in physical_activity_papers:
    print(f"  - {paper['title']}: {paper['citation_count']} citations")

# Also, let's check if any of the papers have year information that might be 2016
print('\nLooking at citation IDs and titles more carefully...')

result = physical_activity_papers
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'paper_count': 5, 'sample_keys': ['_id', 'filename', 'text'], 'sample_filename': 'A Lived Informatics Model of Personal Informatics.txt'}, 'var_functions.execute_python:14': {'all_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': 2015, 'domain': ['physical activity', 'food', 'finances'], 'venue': ['CHI', 'Ubicomp', 'CSCW'], 'source': ['ACM'], 'contribution': ['empirical', 'artifact', 'theoretical']}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'domain': ['physical activity', 'food', 'sleep', 'finances'], 'venue': ['CHI', 'Ubicomp'], 'source': ['ACM', 'IEEE'], 'contribution': ['empirical', 'artifact', 'theoretical']}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2016, 'domain': ['physical activity', 'sleep', 'mental'], 'venue': ['CHI'], 'source': ['ACM'], 'contribution': ['empirical', 'artifact', 'theoretical']}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2016, 'domain': ['physical activity', 'food', 'mental'], 'venue': ['CHI'], 'source': ['ACM', 'IEEE'], 'contribution': ['empirical', 'artifact', 'theoretical']}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': 2016, 'domain': ['food', 'sleep'], 'venue': ['CHI'], 'source': ['ACM', 'IEEE'], 'contribution': ['empirical', 'artifact', 'theoretical']}], 'papers_2016_physical_activity': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2016, 'domain': ['physical activity', 'sleep', 'mental'], 'venue': ['CHI'], 'source': ['ACM'], 'contribution': ['empirical', 'artifact', 'theoretical']}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2016, 'domain': ['physical activity', 'food', 'mental'], 'venue': ['CHI'], 'source': ['ACM', 'IEEE'], 'contribution': ['empirical', 'artifact', 'theoretical']}]}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': []}

exec(code, env_args)
