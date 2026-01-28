code = """import json
import os
import re

# Load all 2016 papers from MongoDB
result_key = 'var_functions.query_db:14'
mongo_results = locals().get(result_key, [])

# Load from file if it's a file path
if isinstance(mongo_results, str) and os.path.exists(mongo_results):
    with open(mongo_results, 'r') as f:
        mongo_results = json.load(f)

print(f"Total papers with 2016: {len(mongo_results)}")

# Process each document to identify physical activity domain papers
physical_activity_papers = []

for doc in mongo_results:
    filename = doc.get('filename', '')
    text = doc.get('text', '').lower()
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Check for physical activity domain indicators
    domain_indicators = [
        'physical activity', 'physical_activity',
        'exercise', 'fitness', 'walking', 'running',
        'step count', 'sedentary', 'active living'
    ]
    
    # Also check for domain field patterns in text
    has_physical_activity = False
    
    # Check if "physical activity" appears in context that suggests it's a domain
    if 'physical activity' in text:
        # Check if it's part of a domain list or mentioned as a focus
        patterns = [
            r'physical activity[^.]{0,50}(domain|topic|area|focus)',
            r'(domain|topic|area|focus)[^.]{0,50}physical activity',
            r'physical activity[^.,;]{0,30}(sleep|food|mental)',
            r'track[^.,;]{0,30}physical activity'
        ]
        
        for pattern in patterns:
            if re.search(pattern, text, re.IGNORECASE):
                has_physical_activity = True
                break
                
    # Count frequency of activity-related terms
    activity_terms = ['exercise', 'fitness', 'walking', 'running', 'step count', 'steps']
    activity_term_count = sum(text.count(term) for term in activity_terms)
    
    # If physical activity appears multiple times OR activity terms appear frequently,
    # it's likely a physical activity domain paper
    if has_physical_activity or activity_term_count >= 3:
        physical_activity_papers.append({
            'title': title,
            'activity_term_count': activity_term_count
        })

print(f"Physical activity papers from 2016: {len(physical_activity_papers)}")
for paper in physical_activity_papers[:10]:
    print(f"- {paper['title']}")

result = {
    'total_2016_papers': len(mongo_results),
    'physical_activity_papers': physical_activity_papers
}

print("__RESULT__:")
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'total_docs': 5, 'filtered_papers_count': 0, 'titles': []}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [{'title': '"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'total_citations': '53'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'total_citations': '313'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'total_citations': '390'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'total_citations': '368'}, {'title': 'A Situated Exploration of Designing for Personal Health Ecosystems Through Data-enabled Design', 'total_citations': '277'}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'total_citations': '221'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'total_citations': '220'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': '265'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': '266'}, {'title': 'Activity Tracking in Vivo', 'total_citations': '316'}]}

exec(code, env_args)
