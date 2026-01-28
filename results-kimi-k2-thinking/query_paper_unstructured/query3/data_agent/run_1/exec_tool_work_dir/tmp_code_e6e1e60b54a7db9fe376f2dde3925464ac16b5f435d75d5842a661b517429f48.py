code = """import json, re, os

# Get file paths from storage
paper_path = locals().get('var_functions.query_db:14')
citations_path = locals().get('var_functions.query_db:16')

if not paper_path or not citations_path:
    result = {'error': 'File paths not accessible'}
else:
    # Read data
    with open(paper_path, 'r') as pf:
        papers = json.load(pf)
    with open(citations_path, 'r') as cf:
        citations = json.load(cf)
    
    # Sum citations by title
    citation_totals = {}
    for cit in citations:
        title = cit.get('title', '')
        count = int(cit.get('citation_count', 0))
        citation_totals[title] = citation_totals.get(title, 0) + count
    
    # Find empirical papers after 2016
    empirical_papers = []
    
    for paper in papers:
        filename = paper.get('filename', '')
        text = paper.get('text', '')
        
        # Extract title
        title = filename.replace('.txt', '') if filename else ''
        if not title:
            continue
        
        # Extract year (look for 4-digit year patterns)
        year = None
        
        # Try venue + year pattern first
        venue_patterns = ['CHI', 'Ubicomp', 'CSCW', 'DIS', 'WWW', 'IUI', 'OzCHI', 'TEI', 'AH', 'PervasiveHealth']
        for venue in venue_patterns:
            pattern = venue + r'\s+(\d{4})'
            m = re.search(pattern, text, re.IGNORECASE)
            if m:
                year = int(m.group(1))
                break
        
        # Try copyright year
        if not year:
            m = re.search(r'Copyright[^\d]*(\d{4})', text)
            if m:
                year = int(m.group(1))
        
        # Try any 2017-2025 year
        if not year:
            m = re.search(r'\b(20(1[7-9]|2[0-9]))\b', text)
            if m:
                year = int(m.group(1))
        
        # Skip if not after 2016
        if not year or year <= 2016:
            continue
        
        # Check for empirical contribution
        text_lower = text.lower()
        is_empirical = False
        
        if re.search(r'empirical.*contribution', text, re.IGNORECASE):
            is_empirical = True
        elif re.search(r'we\s+(conducted|report|present|describe).*study', text_lower):
            is_empirical = True
        elif re.search(r'(participants|subjects|data collection|experiment|user study|field study)', text_lower):
            if re.search(r'(contribution|finding|result)', text_lower):
                is_empirical = True
        
        if is_empirical:
            total_cites = citation_totals.get(title, 0)
            empirical_papers.append({
                'title': title,
                'year': year,
                'total_citation_count': total_cites
            })
    
    # Sort by citations
    empirical_papers.sort(key=lambda x: x['total_citation_count'], reverse=True)
    result = empirical_papers

print('__RESULT__:')
print(json.dumps(result, default=str))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.execute_python:8': [{'title': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'filename': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System.txt", 'year': 2018, 'venue': 'CHI', 'source': 'ACM', 'contribution': ['empirical'], 'domains': ['productivity', 'social interactions', 'chronic', 'health_behavior', 'physical activity', 'screen time', 'food', 'mental', 'location', 'diabetes']}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': [{'title': 'Communicating Uncertainty in Fertility Prognosis', 'filename': 'Communicating Uncertainty in Fertility Prognosis.txt', 'year': 2019, 'venue': 'CHI', 'source': 'ACM', 'contribution': ['artifact', 'empirical', 'methodological'], 'domains': ['location', 'screen time', 'mental', 'physical activity', 'productivity', 'sleep', 'social interactions', 'chronic', 'health_behavior']}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
