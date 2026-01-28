code = """import json
import re

# Get the paper documents data from storage - try reading directly
file_path = 'var_functions.query_db:8'

# Read and process the data
paper_docs = []
try:
    with open(file_path, 'r') as f:
        paper_docs = json.load(f)
except:
    # Try alternative approach if file reading fails
    file_path = globals().get('var_functions.query_db:8')
    if file_path and isinstance(file_path, str):
        with open(file_path, 'r') as f:
            paper_docs = json.load(f)

if not paper_docs:
    print("Could not load paper documents")
else:
    print(f"Total paper documents: {len(paper_docs)}")
    
    # Process papers to find 2016 physical activity papers
    papers_2016_pa = []
    papers_2016_all = []
    
    for doc in paper_docs:
        text = doc.get('text', '')
        filename = doc.get('filename', '')
        title = filename.replace('.txt', '')
        
        # Extract year from text
        year_str = None
        copyright_match = re.search(r'Copyright\s*[@©]?\s*(20\d{2})', text)
        if copyright_match:
            year_str = copyright_match.group(1)
        else:
            year_match = re.search(r'\b(20\d{2})\b', text)
            if year_match:
                year_str = year_match.group(1)
        
        # Check if year is 2016
        if year_str == '2016':
            papers_2016_all.append(title)
            
            # Check if domain includes physical activity
            text_lower = text.lower()
            pa_keywords = ['physical activity', 'physical activities', 'fitness', 'exercise', 'workout', 'step count', 'walking', 'running']
            
            if any(keyword in text_lower for keyword in pa_keywords):
                papers_2016_pa.append(title)
    
    print(f"Papers from 2016 (all domains): {len(papers_2016_all)}")
    print(f"Papers from 2016 in physical activity domain: {len(papers_2016_pa)}")
    
    if papers_2016_pa:
        print("Physical activity papers from 2016:")
        for title in papers_2016_pa[:10]:  # Show first 10
            print("  - " + title)
    
    # Prepare results
    result = {
        'papers_2016_pa_count': len(papers_2016_pa),
        'papers_2016_all_count': len(papers_2016_all),
        'paper_titles_pa': papers_2016_pa
    }
    
    print('__RESULT__:')
    print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'paper_titles': [], 'papers': []}, 'var_functions.query_db:12': [{'citation_year': '2011'}, {'citation_year': '2012'}, {'citation_year': '2013'}, {'citation_year': '2014'}, {'citation_year': '2015'}, {'citation_year': '2016'}, {'citation_year': '2017'}, {'citation_year': '2018'}, {'citation_year': '2019'}, {'citation_year': '2020'}, {'citation_year': '2021'}, {'citation_year': '2022'}, {'citation_year': '2023'}, {'citation_year': '2024'}, {'citation_year': '2025'}]}

exec(code, env_args)
