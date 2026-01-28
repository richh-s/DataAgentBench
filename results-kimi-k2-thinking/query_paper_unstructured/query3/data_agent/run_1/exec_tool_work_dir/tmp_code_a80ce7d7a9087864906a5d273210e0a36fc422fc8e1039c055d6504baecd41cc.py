code = """import json, re, os

paper_path = locals().get('var_functions.query_db:14')
citations_path = locals().get('var_functions.query_db:16')

if not paper_path or not citations_path:
    papers = []
else:
    with open(paper_path, 'r') as f:
        papers = json.load(f)
    with open(citations_path, 'r') as f:
        citations = json.load(f)
    
    # Sum citations by title
    totals = {}
    for c in citations:
        title = c.get('title', '')
        count = int(c.get('citation_count', 0))
        totals[title] = totals.get(title, 0) + count
    
    # Find empirical papers after 2016
    empirical = []
    
    for p in papers:
        filename = p.get('filename', '')
        text = p.get('text', '')
        title = filename.replace('.txt', '') if filename else ''
        
        if not title:
            continue
        
        # Extract year
        year = None
        for v in ['CHI', 'Ubicomp', 'CSCW', 'DIS', 'WWW', 'IUI', 'OzCHI', 'TEI', 'AH', 'PervasiveHealth']:
            m = re.search(v + r'\s+(\d{4})', text, re.IGNORECASE)
            if m:
                year = int(m.group(1))
                break
        
        if not year:
            m = re.search(r'Copyright[^\d]*(\d{4})', text)
            if m:
                year = int(m.group(1))
        
        if not year:
            m = re.search(r'\b(20(1[7-9]|2[0-9]))\b', text)
            if m:
                year = int(m.group(1))
        
        if not year or year <= 2016:
            continue
        
        # Check for empirical
        txt = text.lower()
        is_empirical = False
        
        if re.search(r'empirical.*contribution', text, re.IGNORECASE):
            is_empirical = True
        elif re.search(r'we.*(conduct|report).*study', txt):
            is_empirical = True
        elif re.search(r'(participants|subjects|data collection|experiment|user study)', txt):
            if re.search(r'(contribution|finding|result)', txt):
                is_empirical = True
        
        if is_empirical:
            empirical.append({
                'title': title,
                'year': year,
                'total_citation_count': totals.get(title, 0)
            })
    
    empirical.sort(key=lambda x: x['total_citation_count'], reverse=True)
    
    output = []
    for paper in empirical:
        output.append(f"{paper['title']}: {paper['total_citation_count']} citations")
    
    result = '\n'.join(output)

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.execute_python:8': [{'title': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'filename': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System.txt", 'year': 2018, 'venue': 'CHI', 'source': 'ACM', 'contribution': ['empirical'], 'domains': ['productivity', 'social interactions', 'chronic', 'health_behavior', 'physical activity', 'screen time', 'food', 'mental', 'location', 'diabetes']}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': [{'title': 'Communicating Uncertainty in Fertility Prognosis', 'filename': 'Communicating Uncertainty in Fertility Prognosis.txt', 'year': 2019, 'venue': 'CHI', 'source': 'ACM', 'contribution': ['artifact', 'empirical', 'methodological'], 'domains': ['location', 'screen time', 'mental', 'physical activity', 'productivity', 'sleep', 'social interactions', 'chronic', 'health_behavior']}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:22': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019, 'total_citation_count': 266}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018, 'total_citation_count': 265}]}

exec(code, env_args)
