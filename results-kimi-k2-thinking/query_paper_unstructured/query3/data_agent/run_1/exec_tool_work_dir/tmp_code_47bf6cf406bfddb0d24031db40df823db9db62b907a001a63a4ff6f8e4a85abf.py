code = """import json, re, os, sys

# Get the file path from storage
file_path_key = 'var_functions.query_db:2'
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
    
    for doc in docs:
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
            r'\b(20(1[7-9]|2[0-9]))\b'  # 2017-2029
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
        if re.search(r'contribution.*empirical|empirical.*contribution', text, re.IGNORECASE):
            contribution.append('empirical')
        if re.search(r'contribution.*artifact|artifact.*contribution', text, re.IGNORECASE):
            contribution.append('artifact')
        if re.search(r'contribution.*theoretical|theoretical.*contribution', text, re.IGNORECASE):
            contribution.append('theoretical')
        if re.search(r'contribution.*survey|survey.*contribution', text, re.IGNORECASE):
            contribution.append('survey')
        if re.search(r'contribution.*methodological|methodological.*contribution', text, re.IGNORECASE):
            contribution.append('methodological')
        
        # Extract domains
        domains = []
        domain_patterns = [
            (r'food|diet|nutrition', 'food'),
            (r'physical activity|exercise|sedentary|sedentary behavior|standing|moving', 'physical activity'),
            (r'sleep|sleeping', 'sleep'),
            (r'mental health|depression|anxiety|stress', 'mental'),
            (r'finances|financial|money', 'finances'),
            (r'productivity|work', 'productivity'),
            (r'screen time|phone use|mobile|smartphone', 'screen time'),
            (r'social interactions|social', 'social interactions'),
            (r'location|gps', 'location'),
            (r'chronic|chronic disease', 'chronic'),
            (r'diabetes|diabetic', 'diabetes'),
            (r'health behavior|behavior change', 'health_behavior')
        ]
        
        for pattern, domain_name in domain_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                domains.append(domain_name)
        
        processed_docs.append({
            'title': title,
            'filename': filename,
            'year': year,
            'venue': venue,
            'source': source,
            'contribution': contribution,
            'domains': list(set(domains))  # Remove duplicates
        })
    
    # Filter for papers with empirical contribution and year > 2016
    empirical_papers_2017_plus = [
        paper for paper in processed_docs 
        if paper.get('year') and paper['year'] > 2016 and 'empirical' in paper.get('contribution', [])
    ]
    
    print('Total processed docs:', len(processed_docs))
    print('Empirical papers after 2016:', len(empirical_papers_2017_plus))
    
    # Show a few samples
    for paper in empirical_papers_2017_plus[:3]:
        print('Sample paper:', paper)
    
    result = empirical_papers_2017_plus

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence']}

exec(code, env_args)
