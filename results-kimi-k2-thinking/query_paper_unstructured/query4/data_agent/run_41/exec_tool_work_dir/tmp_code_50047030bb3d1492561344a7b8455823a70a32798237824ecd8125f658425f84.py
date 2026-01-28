code = """import json

# Load data from files
papers_path = locals()['var_functions.query_db:10']
citations_path = locals()['var_functions.query_db:2']

with open(papers_path, 'r') as f:
    all_papers = json.load(f)

with open(citations_path, 'r') as f:
    citations_data = json.load(f)

# Create dict for easy citation lookup
citations_dict = {}
for item in citations_data:
    citations_dict[item['title']] = int(item['total_citations'])

# Find 2016 physical activity papers
results = []

for paper in all_papers:
    filename = paper['filename']
    text = paper['text']
    title = filename.replace('.txt', '')
    
    # Check for 2016 in text
    has_2016 = ' 2016' in text or ',2016' in text or '.2016' in text or 'Copyright 2016' in text
    
    # Check for physical activity domain terms
    text_lower = text.lower()
    physical_activity_terms = ['physical activity', 'activity tracking', 'fitness tracker', 'exercise tracking', 'activity tracker']
    in_domain = any(term in text_lower for term in physical_activity_terms)
    
    # If both conditions and has citations
    if has_2016 and in_domain and title in citations_dict:
        results.append({
            'title': title,
            'total_citations': citations_dict[title]
        })

# Sort by citations descending
results.sort(key=lambda x: x['total_citations'], reverse=True)

# Generate output
output = json.dumps(results, indent=2)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:4': [{'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'total_citations': 636}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'total_citations': 271}, {'title': 'Charting Design Preferences on Wellness Wearables', 'total_citations': 269}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': 266}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': 265}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': [{'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'total_citations': 452}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': 266}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': 265}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [], 'var_functions.execute_python:22': []}

exec(code, env_args)
