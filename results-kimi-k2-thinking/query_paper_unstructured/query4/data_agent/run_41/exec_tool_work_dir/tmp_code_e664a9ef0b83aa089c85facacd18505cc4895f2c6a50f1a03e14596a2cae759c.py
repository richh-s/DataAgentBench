code = """import json
import re

# Load all physical activity papers
papers_path = locals()['var_functions.query_db:14']
with open(papers_path, 'r') as f:
    physical_activity_papers = json.load(f)

# Load citations data
citations_path = locals()['var_functions.query_db:2']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

# Create citations dictionary
citations_dict = {item['title']: int(item['total_citations']) for item in citations_data}

# Find papers from 2016 in the physical activity domain
results = []

for paper in physical_activity_papers:
    filename = paper['filename']
    text = paper['text']
    
    # Extract title
    title = filename.replace('.txt', '')
    
    # Check if paper is from 2016 (look for explicit 2016 in text)
    # Pattern to match publication years like: CHI 2016, Ubicomp 2016, etc.
    year_2016_patterns = [
        r'\b2016\b.*?(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)',
        r'(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH).*?\b2016\b',
        r"\b2016\b.*?(Proceedings|Conference|ACM|IEEE)",
        r"Copyright\s+[^\d]*\b2016\b",
        r"CHI\s+'?16",  # CHI '16 or CHI 16
        r"Ubicomp\s+'?16",
        r"CSCW\s+'?16"
    ]
    
    is_2016 = False
    for pattern in year_2016_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            is_2016 = True
            break
    
    # Additional check for explicit 2016
    if not is_2016 and re.search(r'\b2016\b', text):
        # Make sure it's not just a reference year
        # Check if 2016 appears near venue/publisher names
        context = re.findall(r'.{0,50}2016.{0,50}', text)
        for ctx in context:
            if any(keyword in ctx.lower() for keyword in ['proceedings', 'conference', 'chi', 'ubicomp', 'cscw', 'dis', 'acm', 'ieee']):
                is_2016 = True
                break
    
    # If from 2016 and has citations
    if is_2016 and title in citations_dict:
        results.append({
            'title': title,
            'total_citations': citations_dict[title]
        })

# Remove duplicates and sort by citations
unique_results = {}
for r in results:
    if r['title'] not in unique_results:
        unique_results[r['title']] = r

sorted_results = sorted(unique_results.values(), key=lambda x: x['total_citations'], reverse=True)

result_str = json.dumps(sorted_results, indent=2)
print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:4': [{'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'total_citations': 636}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'total_citations': 271}, {'title': 'Charting Design Preferences on Wellness Wearables', 'total_citations': 269}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': 266}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': 265}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': [{'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'total_citations': 452}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': 266}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': 265}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
