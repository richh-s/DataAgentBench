code = """import json
import os
import re

# Check the value stored in var_functions.query_db:2
result_path = var_functions.query_db:2
print("Result path type:", type(result_path))
print("Result path value:", result_path)

# List files to see what's available
print("\nJSON files in current directory:")
for f in os.listdir('.'):
    if '.json' in f:
        print(" ", f)

# Try to read the file
if os.path.exists(result_path):
    with open(result_path, 'r') as f:
        paper_docs = json.load(f)
    
    print(f"\nLoaded {len(paper_docs)} documents")
    
    # Extract paper information: title, year, domain
    papers_info = []
    
    for i, doc in enumerate(paper_docs[:20]):  # Process first 20 for testing
        filename = doc.get('filename', '')
        text = doc.get('text', '')
        
        # Extract title from filename (remove .txt extension)
        title = filename.replace('.txt', '') if filename else ''
        
        # Extract year from text
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
        
        # Check for physical activity domain
        is_physical_activity = 'physical activity' in text.lower()
        
        if title:
            papers_info.append({
                'title': title,
                'year': year,
                'is_physical_activity': is_physical_activity
            })
            print(f"Paper {i+1}: {title[:50]}... - Year: {year} - PA: {is_physical_activity}")
    
    # Filter for 2016 physical activity papers
    papers_2016_pa = [p for p in papers_info if p['year'] == 2016 and p['is_physical_activity']]
    
    print(f"\nFiltered {len(papers_2016_pa)} papers from 2016 in physical activity domain")
    
    # Now process all documents
    papers_info_all = []
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
            papers_info_all.append({
                'title': title,
                'year': year,
                'is_physical_activity': is_physical_activity
            })
    
    papers_2016_pa = [p for p in papers_info_all if p['year'] == 2016 and p['is_physical_activity']]
    filtered_titles = [p['title'] for p in papers_2016_pa]
    
    print(f"Final count: {len(papers_2016_pa)} papers")
    print('__RESULT__:')
    print(json.dumps(filtered_titles))
else:
    print("File does not exist")
    print('__RESULT__:')
    print(json.dumps([]))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
