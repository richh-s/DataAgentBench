code = """import json

papers_path = locals()['var_functions.query_db:14']
with open(papers_path, 'r') as f:
    papers = json.load(f)

citations_path = locals()['var_functions.query_db:2']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

citations_dict = {}
for item in citations_data:
    citations_dict[item['title']] = int(item['total_citations'])

paper_2016_physical_activity = []

for paper in papers:
    filename = paper['filename']
    text = paper['text']
    title = filename.replace('.txt', '')
    
    # Check if paper has citation data
    if title not in citations_dict:
        continue
    
    # Check for 2016 publication year
    has_2016 = False
    text_upper = text.upper()
    
    # Look for various 2016 patterns
    if ' 2016' in text or ',2016' in text or '.2016' in text:
        # Check if near conference/journal names
        context_start = max(0, text_upper.find('2016') - 100)
        context_end = min(len(text_upper), text_upper.find('2016') + 100)
        context = text_upper[context_start:context_end]
        
        venue_indicators = ['CHI', 'UBICOMP', 'CSCW', 'DIS', 'PERVASIVEHEALTH', 'WWW', 'IUI', 'OZCHI', 'TEI', 'AH', 'PROCEEDINGS', 'CONFERENCE', 'ACM', 'IEEE']
        for indicator in venue_indicators:
            if indicator in context:
                has_2016 = True
                break
    
    # Also check for year format like CHI '16
    if not has_2016:
        if "CHI '16" in text or "CHI'16" in text or "CHI 16" in text:
            has_2016 = True
        elif "UBICOMP '16" in text or "UBICOMP'16" in text or "UBICOMP 16" in text:
            has_2016 = True
        elif "CSCW '16" in text or "CSCW'16" in text or "CSCW 16" in text:
            has_2016 = True
    
    if has_2016:
        paper_2016_physical_activity.append({
            'title': title,
            'total_citations': citations_dict[title]
        })

paper_2016_physical_activity.sort(key=lambda x: x['total_citations'], reverse=True)
result_str = json.dumps(paper_2016_physical_activity, indent=2)
print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:4': [{'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'total_citations': 636}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'total_citations': 271}, {'title': 'Charting Design Preferences on Wellness Wearables', 'total_citations': 269}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': 266}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': 265}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': [{'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'total_citations': 452}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': 266}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': 265}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': []}

exec(code, env_args)
