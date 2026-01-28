code = """import json
import re

# Read the complete papers data
papers_path = locals()['var_functions.query_db:10']
with open(papers_path, 'r') as f:
    all_papers = json.load(f)

# Read citations data
citations_path = locals()['var_functions.query_db:2']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

# Create citations dictionary
citations_dict = {item['title']: int(item['total_citations']) for item in citations_data}

# Process papers to find 2016 physical activity papers
results = []

for paper in all_papers:
    filename = paper['filename']
    text = paper['text']
    
    # Extract title
    title = filename.replace('.txt', '')
    
    # Look for publication year patterns
    year_patterns = [
        r'\b2016\b.*?(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)',
        r'(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH).*?\b2016\b',
        r"'(\d{2})"  # Pattern like '16
    ]
    
    found_2016 = False
    for pattern in year_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            # Check if it's 16 (which would be 2016)
            for match in matches:
                if match == '16' or '2016' in str(match):
                    found_2016 = True
                    break
        if found_2016:
            break
    
    # Also check for explicit 2016
    if ' 2016' in text or ',2016' in text or '.2016' in text:
        found_2016 = True
    
    # Check for physical activity domain
    physical_activity_terms = [
        'physical activity', 'activity tracking', 'fitness tracker', 'exercise',
        'activity tracker', 'physical fitness', 'workout', 'sedentary behavior'
    ]
    
    in_physical_activity_domain = False
    text_lower = text.lower()
    for term in physical_activity_terms:
        if term in text_lower:
            in_physical_activity_domain = True
            break
    
    # If both conditions met and has citations
    if found_2016 and in_physical_activity_domain and title in citations_dict:
        results.append({
            'title': title,
            'total_citations': citations_dict[title]
        })

# Remove duplicates and sort
unique_results = {r['title']: r for r in results}.values()
sorted_results = sorted(unique_results, key=lambda x: x['total_citations'], reverse=True)

# Print results
result_str = json.dumps(sorted_results, indent=2)
print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:4': [{'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'total_citations': 636}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'total_citations': 271}, {'title': 'Charting Design Preferences on Wellness Wearables', 'total_citations': 269}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': 266}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': 265}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
