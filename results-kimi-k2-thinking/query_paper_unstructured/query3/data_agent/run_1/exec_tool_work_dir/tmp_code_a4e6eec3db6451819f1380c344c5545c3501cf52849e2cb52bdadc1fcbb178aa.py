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
    
    # Process paper documents
    processed_papers = []
    
    for i, doc in enumerate(docs):
        if i % 100 == 0:
            print(f'Processing paper {i}/{len(docs)}')
            
        filename = doc.get('filename', '')
        text = doc.get('text', '')
        
        # Extract title (filename without .txt)
        title = filename.replace('.txt', '') if filename else ''
        if not title:
            continue
            
        # Extract year
        year = None
        year_patterns = [
            r'CHI\s+(\d{4})',
            r'Ubicomp\s+(\d{4})',
            r'CSCW\s+(\d{4})',
            r'DIS\s+(\d{4})',
            r'WWW\s+(\d{4})',
            r'IUI\s+(\d{4})',
            r'OzCHI\s+(\d{4})',
            r'TEI\s+(\d{4})',
            r'AH\s+(\d{4})',
            r'PervasiveHealth\s+(\d{4})',
            r'Proceedings\s+of\s+[^\d]*(\d{4})',
            r'Copyright[^\d]*(\d{4})',
            r'\\b(20(1[7-9]|2[0-9]))\\b'  # 2017-2029
        ]
        
        for pattern in year_patterns:
            match = re.search(pattern, text)
            if match:
                candidate_year = int(match.group(1))
                if 2010 <= candidate_year <= 2025:  # Reasonable range
                    year = candidate_year
                    break
        
        # Skip if no year found
        if not year:
            continue
            
        # Extract contribution type
        contribution = []
        contribution_text = text.lower()
        
        # Check for empirical contribution
        if any(keyword in contribution_text for keyword in [
            'empirical study', 'empirical research', 'empirical investigation', 
            'empirical evaluation', 'empirical analysis', 'empirical work',
            'we conducted', 'we performed', 'we carried out', 'we report',
            'study', 'experiment', 'evaluation', 'field study', 'user study'
        ]) and not any(keyword in contribution_text for keyword in [
            'this paper', 'we propose', 'we present', 'we introduce',
            'design', 'system', 'prototype', 'framework', 'model'
        ]):
            # Additional check: see if it's in the context of contribution
            if re.search(r'contribution.*empirical|empirical.*contribution', text, re.IGNORECASE):
                contribution.append('empirical')
            elif re.search(r'we.*(conduct|perform|carry out|report).*(study|experiment|evaluation|investigation)', text, re.IGNORECASE):
                contribution.append('empirical')
        
        # Also check for explicit contribution statements
        if re.search(r'this.*contribution.*empirical', text, re.IGNORECASE):
            contribution.append('empirical')
            
        # Remove duplicates
        contribution = list(set(contribution))
        
        # Only keep papers after 2016 with empirical contribution
        if year > 2016 and 'empirical' in contribution:
            processed_papers.append({
                'title': title,
                'year': year,
                'contribution': contribution
            })
    
    print(f'Found {len(processed_papers)} empirical papers after 2016')
    
    # Process citations
    citations_by_title = {}
    for citation in citations:
        title = citation.get('title', '')
        count = int(citation.get('citation_count', 0))
        
        if title not in citations_by_title:
            citations_by_title[title] = 0
        citations_by_title[title] += count
    
    print(f'Summed citations for {len(citations_by_title)} unique paper titles')
    
    # Merge paper data with citations
    final_results = []
    
    for paper in processed_papers:
        title = paper['title']
        total_citations = citations_by_title.get(title, 0)
        
        final_results.append({
            'title': title,
            'year': paper['year'],
            'total_citation_count': total_citations
        })
    
    # Sort by citation count (descending)
    final_results.sort(key=lambda x: x['total_citation_count'], reverse=True)
    
    print(f'Final results: {len(final_results)} papers')
    
    # Show top 10
    print("\nTop 10 papers by citation count:")
    for i, paper in enumerate(final_results[:10]):
        print(f"{i+1}. {paper['title']} ({paper['year']}) - {paper['total_citation_count']} citations")
    
    result = final_results

print('__RESULT__:')
print(json.dumps(result, default=str))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.execute_python:8': [{'title': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'filename': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System.txt", 'year': 2018, 'venue': 'CHI', 'source': 'ACM', 'contribution': ['empirical'], 'domains': ['productivity', 'social interactions', 'chronic', 'health_behavior', 'physical activity', 'screen time', 'food', 'mental', 'location', 'diabetes']}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': [{'title': 'Communicating Uncertainty in Fertility Prognosis', 'filename': 'Communicating Uncertainty in Fertility Prognosis.txt', 'year': 2019, 'venue': 'CHI', 'source': 'ACM', 'contribution': ['artifact', 'empirical', 'methodological'], 'domains': ['location', 'screen time', 'mental', 'physical activity', 'productivity', 'sleep', 'social interactions', 'chronic', 'health_behavior']}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
