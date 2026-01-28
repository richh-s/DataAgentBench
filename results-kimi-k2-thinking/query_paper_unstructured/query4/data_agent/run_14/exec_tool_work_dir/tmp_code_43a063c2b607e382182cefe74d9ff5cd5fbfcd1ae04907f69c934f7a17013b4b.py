code = """import json

# Load MongoDB paper data
mongo_result_path = locals()['var_functions.query_db:2']
with open(mongo_result_path, 'r') as f:
    mongo_papers = json.load(f)

# Load citations data
sqlite_result_path = locals()['var_functions.query_db:16']
with open(sqlite_result_path, 'r') as f:
    citations = json.load(f)

print('Total papers in MongoDB:', len(mongo_papers))
print('Total citations in database:', len(citations))

# Extract metadata from MongoDB papers (year and domain)
papers_2016_physical_activity = []

for paper in mongo_papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = paper.get('text', '').lower()
    
    # Extract year from text
    year = None
    text_upper = paper.get('text', '').upper()
    if '2016' in text_upper:
        year = 2016
    elif '2015' in text_upper:
        year = 2015
    elif '2014' in text_upper:
        year = 2014
    elif '2017' in text_upper:
        year = 2017
    
    # Check if it's from 2016 and contains 'physical activity' domain
    if year == 2016 and 'physical activity' in text:
        papers_2016_physical_activity.append(title)

print('Papers from 2016 with physical activity domain in MongoDB:', len(papers_2016_physical_activity))
for title in papers_2016_physical_activity:
    print('  - "' + title + '"')

# Find matching citations for these papers
matching_citations = []
for citation in citations:
    citation_title = citation.get('title', '')
    citation_count = int(citation.get('citation_count', 0))
    
    # Check if this citation matches any of our 2016 physical activity papers
    for paper_title in papers_2016_physical_activity:
        if citation_title == paper_title:
            matching_citations.append({
                'title': paper_title,
                'citation_count': citation_count
            })

print('\nMatching citations found:', len(matching_citations))
for mc in matching_citations:
    print('  - "' + mc['title'] + '": ' + str(mc['citation_count']) + ' citations')

# Also check if there are other physical activity papers in 2016 citations
# that might not be in the MongoDB papers list
print('\nLooking for physical activity papers in 2016 citations...')
physical_activity_keywords = ['physical activity', 'fitness', 'exercise', 'activity tracking', 'wearable']
additional_matches = []

for citation in citations:
    citation_title = citation.get('title', '').lower()
    citation_original_title = citation.get('title', '')
    citation_count = int(citation.get('citation_count', 0))
    
    # Check if title mentions physical activity
    contains_physical_activity = False
    for keyword in physical_activity_keywords:
        if keyword in citation_title:
            contains_physical_activity = True
            break
    
    # Also check for very specific activity tracking terms
    if 'activity' in citation_title and any(word in citation_title for word in ['track', 'monitor', 'sense', 'wear']):
        contains_physical_activity = True
    
    if contains_physical_activity:
        additional_matches.append({
            'title': citation_original_title,
            'citation_count': citation_count
        })

print('Physical activity related papers in 2016 citations:', len(additional_matches))
for am in additional_matches:
    print('  - "' + am['title'] + '": ' + str(am['citation_count']) + ' citations')

# Combine results
all_results = matching_citations + additional_matches

print('\n__RESULT__:')
print(json.dumps(all_results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'paper_count': 5, 'sample_keys': ['_id', 'filename', 'text'], 'sample_filename': 'A Lived Informatics Model of Personal Informatics.txt'}, 'var_functions.execute_python:14': {'all_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': 2015, 'domain': ['physical activity', 'food', 'finances'], 'venue': ['CHI', 'Ubicomp', 'CSCW'], 'source': ['ACM'], 'contribution': ['empirical', 'artifact', 'theoretical']}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'domain': ['physical activity', 'food', 'sleep', 'finances'], 'venue': ['CHI', 'Ubicomp'], 'source': ['ACM', 'IEEE'], 'contribution': ['empirical', 'artifact', 'theoretical']}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2016, 'domain': ['physical activity', 'sleep', 'mental'], 'venue': ['CHI'], 'source': ['ACM'], 'contribution': ['empirical', 'artifact', 'theoretical']}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2016, 'domain': ['physical activity', 'food', 'mental'], 'venue': ['CHI'], 'source': ['ACM', 'IEEE'], 'contribution': ['empirical', 'artifact', 'theoretical']}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': 2016, 'domain': ['food', 'sleep'], 'venue': ['CHI'], 'source': ['ACM', 'IEEE'], 'contribution': ['empirical', 'artifact', 'theoretical']}], 'papers_2016_physical_activity': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2016, 'domain': ['physical activity', 'sleep', 'mental'], 'venue': ['CHI'], 'source': ['ACM'], 'contribution': ['empirical', 'artifact', 'theoretical']}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2016, 'domain': ['physical activity', 'food', 'mental'], 'venue': ['CHI'], 'source': ['ACM', 'IEEE'], 'contribution': ['empirical', 'artifact', 'theoretical']}]}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
