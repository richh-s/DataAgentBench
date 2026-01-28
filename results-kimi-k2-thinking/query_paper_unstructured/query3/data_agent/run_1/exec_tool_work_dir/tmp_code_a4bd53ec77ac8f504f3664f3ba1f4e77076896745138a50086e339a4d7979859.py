code = """import json, re, os

# Get the file path from storage
file_path_key = 'var_functions.query_db:14'
file_path = locals().get(file_path_key)

citations_file_key = 'var_functions.query_db:16'
citations_file_path = locals().get(citations_file_key)

if not file_path or not isinstance(file_path, str):
    print('Paper docs file path not found or not a string')
    result = {'error': 'Paper docs file path not accessible'}
elif not citations_file_path or not isinstance(citations_file_path, str):
    print('Citations file path not found or not a string')
    result = {'error': 'Citations file path not accessible'}
else:
    print('Reading paper docs from file:', file_path)
    print('Reading citations from file:', citations_file_path)
    
    # Read paper documents
    with open(file_path, 'r', encoding='utf-8') as f:
        docs = json.load(f)
    
    # Read citations
    with open(citations_file_path, 'r', encoding='utf-8') as f:
        citations = json.load(f)
    
    print(f'Loaded {len(docs)} paper documents')
    print(f'Loaded {len(citations)} citation records')
    
    # Process citations first - sum by title
    citations_by_title = {}
    for citation in citations:
        title = citation.get('title', '')
        count = int(citation.get('citation_count', 0))
        
        if title not in citations_by_title:
            citations_by_title[title] = 0
        citations_by_title[title] += count
    
    print(f'Total citation records for {len(citations_by_title)} unique papers')
    
    # Process paper documents and match with citations
    empirical_papers = []
    
    for i, doc in enumerate(docs):
        if i % 50 == 0:
            print(f'Processing paper {i}/{len(docs)}')
            
        filename = doc.get('filename', '')
        text = doc.get('text', '')
        
        # Extract title (filename without .txt)
        title = filename.replace('.txt', '') if filename else ''
        if not title:
            continue
            
        # Extract year from text
        year = None
        year_match = None
        
        # Look for venue with year (e.g., CHI 2018)
        venue_year_patterns = [
            r'CHI\s+(\d{4})',
            r'Ubicomp\s+(\d{4})',
            r'CSCW\s+(\d{4})',
            r'DIS\s+(\d{4})',
            r'WWW\s+(\d{4})',
            r'IUI\s+(\d{4})',
            r'OzCHI\s+(\d{4})',
            r'TEI\s+(\d{4})',
            r'AH\s+(\d{4})',
            r'PervasiveHealth\s+(\d{4})'
        ]
        
        for pattern in venue_year_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                year = int(match.group(1))
                break
        
        # If not found, look for copyright year
        if not year:
            copyright_match = re.search(r'Copyright[^\d]*(\d{4})', text)
            if copyright_match:
                year = int(copyright_match.group(1))
        
        # If not found, look for any 4-digit year in reasonable range
        if not year:
            year_match = re.search(r'\b(20(1[7-9]|2[0-9]))\b', text)
            if year_match:
                year = int(year_match.group(1))
        
        # Skip if no year found or year <= 2016
        if not year or year <= 2016:
            continue
            
        # Check for empirical contribution
        is_empirical = False
        text_lower = text.lower()
        
        # Check for explicit empirical contribution statements
        if re.search(r'empirical.*contribution|contribution.*empirical', text, re.IGNORECASE):
            is_empirical = True
        # Check for empirical study indicators
        elif re.search(r'we.conducted.*study|we.report.*study|empirical.study|user.study|field.study', text_lower):
            is_empirical = True
        # Check for methodology describing data collection
        elif re.search(r'participants|subjects|data.collection|experiment|evaluation|survey|interview', text_lower):
            # Make sure it's not just a proposal
            if not re.search(r'we.propose|we.present|future.work', text_lower):
                is_empirical = True
        
        if is_empirical:
            # Check if we have citations for this paper
            total_citations = citations_by_title.get(title, 0)
            
            empirical_papers.append({
                'title': title,
                'year': year,
                'total_citation_count': total_citations
            })
    
    print(f'Found {len(empirical_papers)} empirical papers after 2016')
    
    # Sort by citation count
    empirical_papers.sort(key=lambda x: x['total_citation_count'], reverse=True)
    
    # Show results
    print('\nResults:')
    for i, paper in enumerate(empirical_papers):
        print(f"{i+1}. {paper['title']} ({paper['year']}) - {paper['total_citation_count']} citations")
    
    result = empirical_papers

print('__RESULT__:')
print(json.dumps(result, default=str))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.execute_python:8': [{'title': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'filename': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System.txt", 'year': 2018, 'venue': 'CHI', 'source': 'ACM', 'contribution': ['empirical'], 'domains': ['productivity', 'social interactions', 'chronic', 'health_behavior', 'physical activity', 'screen time', 'food', 'mental', 'location', 'diabetes']}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': [{'title': 'Communicating Uncertainty in Fertility Prognosis', 'filename': 'Communicating Uncertainty in Fertility Prognosis.txt', 'year': 2019, 'venue': 'CHI', 'source': 'ACM', 'contribution': ['artifact', 'empirical', 'methodological'], 'domains': ['location', 'screen time', 'mental', 'physical activity', 'productivity', 'sleep', 'social interactions', 'chronic', 'health_behavior']}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
