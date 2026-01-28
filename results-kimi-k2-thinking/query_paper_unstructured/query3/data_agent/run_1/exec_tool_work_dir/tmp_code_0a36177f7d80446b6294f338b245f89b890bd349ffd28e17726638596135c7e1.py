code = """import json, re, os

# Get the file path from storage
file_path_key = 'var_functions.query_db:10'
file_path = locals().get(file_path_key)

if not file_path or not isinstance(file_path, str):
    print('File path not found or not a string')
    result = {'error': 'File path not accessible'}
else:
    print('Reading from file:', file_path)
    # Read the JSON data
    with open(file_path, 'r', encoding='utf-8') as f:
        docs = json.load(f)
    
    print('Number of docs loaded:', len(docs))
    
    # Process each document to extract metadata
    processed_docs = []
    
    for i, doc in enumerate(docs):
        if i % 100 == 0:
            print(f'Processing doc {i}/{len(docs)}')
            
        filename = doc.get('filename', '')
        text = doc.get('text', '')
        
        # Extract title (filename without .txt)
        title = filename.replace('.txt', '') if filename else ''
        
        # Extract year from text looking for patterns like "2017", "CHI 2018", "2019," etc.
        year = None
        year_patterns = [
            r'CHI\s+(\d{4})',
            r'Ubicomp\s+(\d{4})',
            r'CSCW\s+(\d{4})',
            r'(\d{4})\s+(Paper|Conference|Proceedings)',
            r'Proceedings\s+of\s+[^\d]*(\d{4})',
            r'Copyright[^\d]*(\d{4})',
            r'\\b(20(1[7-9]|2[0-9]))\\b'  # 2017-2029
        ]
        
        for pattern in year_patterns:
            match = re.search(pattern, text)
            if match:
                candidate_year = int(match.group(1))
                if 2017 <= candidate_year <= 2025:  # Reasonable range
                    year = candidate_year
                    break
        
        # Extract venue
        venue = None
        venue_patterns = [
            (r'CHI', 'CHI'),
            (r'Ubicomp|UbiComp|Ubi comp', 'Ubicomp'),
            (r'CSCW', 'CSCW'),
            (r'DIS', 'DIS'),
            (r'PervasiveHealth', 'PervasiveHealth'),
            (r'WWW', 'WWW'),
            (r'IUI', 'IUI'),
            (r'OzCHI', 'OzCHI'),
            (r'TEI', 'TEI'),
            (r'AH', 'AH')
        ]
        
        for pattern, venue_name in venue_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                venue = venue_name
                break
        
        # Extract source
        source = None
        if 'ACM' in text:
            source = 'ACM'
        elif 'IEEE' in text:
            source = 'IEEE'
        elif 'PubMed' in text or 'PMID' in text:
            source = 'PubMed'
        
        # Extract contribution type
        contribution = []
        # Look for contribution indicators
        if re.search(r'contribution.*empirical|empirical.*contribution|empirical study|empirical research|empirical investigation', text, re.IGNORECASE):
            contribution.append('empirical')
        if re.search(r'contribution.*artifact|artifact.*contribution|system.*design|design.*system|prototype', text, re.IGNORECASE):
            contribution.append('artifact')
        if re.search(r'contribution.*theoretical|theoretical.*contribution|theoretical framework|theoretical model', text, re.IGNORECASE):
            contribution.append('theoretical')
        if re.search(r'contribution.*survey|survey.*contribution|literature review|systematic review', text, re.IGNORECASE):
            contribution.append('survey')
        if re.search(r'contribution.*methodological|methodological.*contribution|methodology|methods', text, re.IGNORECASE):
            contribution.append('methodological')
        
        # Extract domains
        domains = []
        domain_patterns = [
            (r'food|diet|nutrition|eating', 'food'),
            (r'physical activity|exercise|fitness|sedentary|sedentary behavior|standing|moving|steps', 'physical activity'),
            (r'sleep|sleeping|insomnia|circadian', 'sleep'),
            (r'mental health|depression|anxiety|stress|wellbeing|well-being', 'mental'),
            (r'finances|financial|money|budget|spending', 'finances'),
            (r'productivity|work|workplace|job', 'productivity'),
            (r'screen time|phone use|mobile|smartphone|device use|technology use', 'screen time'),
            (r'social interactions|social|communication|relationship', 'social interactions'),
            (r'location|gps|place|spatial', 'location'),
            (r'chronic|chronic disease|illness|health condition', 'chronic'),
            (r'diabetes|diabetic|blood glucose|glycemic', 'diabetes'),
            (r'health behavior|behavior change|lifestyle|habit', 'health_behavior')
        ]
        
        for pattern, domain_name in domain_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                domains.append(domain_name)
        
        # Only keep papers with year > 2016
        if year and year > 2016:
            processed_docs.append({
                'title': title,
                'filename': filename,
                'year': year,
                'venue': venue,
                'source': source,
                'contribution': list(set(contribution)),
                'domains': list(set(domains))
            })
    
    print('Total processed docs after 2016:', len(processed_docs))
    
    # Filter for empirical papers
    empirical_papers = [
        paper for paper in processed_docs 
        if 'empirical' in paper.get('contribution', [])
    ]
    
    print('Empirical papers after 2016:', len(empirical_papers))
    
    # Show samples
    for paper in empirical_papers[:5]:
        print('Sample empirical paper:', paper['title'], 'Year:', paper['year'])
    
    # Save to JSON file for reference
    result = empirical_papers

print('__RESULT__:')
print(json.dumps(result, default=str))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.execute_python:8': [{'title': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'filename': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System.txt", 'year': 2018, 'venue': 'CHI', 'source': 'ACM', 'contribution': ['empirical'], 'domains': ['productivity', 'social interactions', 'chronic', 'health_behavior', 'physical activity', 'screen time', 'food', 'mental', 'location', 'diabetes']}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
