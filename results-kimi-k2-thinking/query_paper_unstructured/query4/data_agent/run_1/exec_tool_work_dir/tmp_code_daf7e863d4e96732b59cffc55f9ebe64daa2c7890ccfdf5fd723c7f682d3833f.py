code = """import json
import os
import re

# Load the MongoDB results (physical activity and 2016)
result_key = 'var_functions.query_db:6'
mongo_results = locals().get(result_key, [])

# If it's a file path (string), read the file
if isinstance(mongo_results, str) and os.path.exists(mongo_results):
    with open(mongo_results, 'r') as f:
        mongo_results = json.load(f)

print(f"Total documents found: {len(mongo_results)}")

# Process documents to extract title and check for 2016 and physical activity domain
papers_2016_physical_activity = []

for doc in mongo_results:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename (remove .txt)
    title = filename.replace('.txt', '') if filename else ''
    
    # Check if text contains 2016 and physical activity (case-insensitive)
    has_2016 = bool(re.search(r'\b2016\b', text))
    has_physical_activity = bool(re.search(r'physical activity', text, re.IGNORECASE))
    
    # Also check if it's explicitly about physical activity domain
    # Look for domain indicators
    domain_indicators = [
        'physical activity', 'exercise', 'fitness', 'active', 'step count', 
        'walking', 'running', 'sedentary'
    ]
    
    domain_score = sum(1 for indicator in domain_indicators if indicator.lower() in text.lower())
    is_physical_activity_domain = has_physical_activity or domain_score >= 2
    
    papers_2016_physical_activity.append({
        'title': title,
        'filename': filename,
        'has_2016': has_2016,
        'has_physical_activity': has_physical_activity,
        'domain_score': domain_score,
        'is_physical_activity_domain': is_physical_activity_domain
    })

# Filter papers that have both 2016 and are physical activity domain
filtered_papers = [p for p in papers_2016_physical_activity if p['has_2016'] and p['is_physical_activity_domain']]

print(f"Papers with 2016 and physical activity domain: {len(filtered_papers)}")
for paper in filtered_papers[:5]:
    print(f"- {paper['title']}")

# Save the filtered titles for next step
titles_to_check = [p['title'] for p in filtered_papers]

__RESULT__:
print(json.dumps({
    "total_docs": len(mongo_results),
    "filtered_papers_count": len(filtered_papers),
    "titles": titles_to_check
}, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
