code = """import json, os, re

# Check what variables are available
available_vars = [var for var in locals().keys() if 'query_db' in var]
print("Available variables:", available_vars)

# Access the storage variable using locals()
if 'var_functions.query_db:2' in locals():
    result_path = locals()['var_functions.query_db:2']
    print("Found file path:", result_path)
    
    # Check if file exists
    if os.path.exists(result_path):
        print("File exists, loading...")
        with open(result_path, 'r') as f:
            paper_docs = json.load(f)
        
        print(f"Loaded {len(paper_docs)} documents")
        
        # Extract paper information from all documents
        papers_info = []
        for doc in paper_docs:
            filename = doc.get('filename', '')
            text = doc.get('text', '')
            title = filename.replace('.txt', '') if filename else ''
            
            year = None
            year_patterns = [r"(\b20\d{2}\b)"]
            header_text = text[:500]
            for pattern in year_patterns:
                matches = re.findall(pattern, header_text)
                if matches:
                    for match in matches:
                        if len(match) == 4:
                            year_val = int(match)
                            if 2010 <= year_val <= 2020:
                                year = year_val
                                break
                    if year:
                        break
            
            is_physical_activity = 'physical activity' in text.lower()
            
            if title:
                papers_info.append({
                    'title': title,
                    'year': year,
                    'is_physical_activity': is_physical_activity
                })
        
        # Filter for 2016 physical activity papers
        papers_2016_pa = [p for p in papers_info if p['year'] == 2016 and p['is_physical_activity']]
        filtered_titles = [p['title'] for p in papers_2016_pa]
        
        print(f"Found {len(papers_2016_pa)} papers from 2016 in physical activity domain")
        
        print('__RESULT__:')
        print(json.dumps(filtered_titles))
    else:
        print("File does not exist")
        print('__RESULT__:')
        print(json.dumps([]))
else:
    print("Variable not found in locals")
    print('__RESULT__:')
    print(json.dumps([]))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
