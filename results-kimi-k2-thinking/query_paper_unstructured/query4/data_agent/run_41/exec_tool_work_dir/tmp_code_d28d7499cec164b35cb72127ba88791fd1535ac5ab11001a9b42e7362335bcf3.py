code = """import json
import re

papers_path = locals()['var_functions.query_db:14']
with open(papers_path, 'r') as f:
    physical_activity_papers = json.load(f)

citations_path = locals()['var_functions.query_db:2']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

citations_dict = {}
for item in citations_data:
    citations_dict[item['title']] = int(item['total_citations'])

results = []

for paper in physical_activity_papers:
    filename = paper['filename']
    text = paper['text']
    title = filename.replace('.txt', '')
    
    if title not in citations_dict:
        continue
    
    is_2016 = False
    if re.search(r'\b2016\b.*?(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|Proceedings|Conference)', text, re.IGNORECASE):
        is_2016 = True
    elif re.search(r'(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|Proceedings|Conference).*?\b2016\b', text, re.IGNORECASE):
        is_2016 = True
    elif re.search(r'Copyright[^\n]*\b2016\b', text, re.IGNORECASE):
        is_2016 = True
    elif re.search(r'(CHI|Ubicomp|CSCW|DIS)\s*[\'\u2019]\s*16\b', text, re.IGNORECASE):
        is_2016 = True
    
    if is_2016:
        results.append({
            'title': title,
            'total_citations': citations_dict[title]
        })

sorted_results = sorted(results, key=lambda x: x['total_citations'], reverse=True)
result_str = json.dumps(sorted_results, indent=2)
print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:4': [{'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'total_citations': 636}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'total_citations': 271}, {'title': 'Charting Design Preferences on Wellness Wearables', 'total_citations': 269}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': 266}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': 265}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': [{'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'total_citations': 452}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': 266}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': 265}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': []}

exec(code, env_args)
