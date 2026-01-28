code = """# Check what's stored in the key var_functions.query_db:2
result_key = locals().get('var_functions.query_db:2')
print(f"Value of var_functions.query_db:2: {result_key}")
print(f"Type: {type(result_key)}")

# The result should be a string indicating a file path
if isinstance(result_key, str):
    # Try to read the JSON file
    try:
        with open(result_key, 'r') as f:
            paper_docs = json.load(f)
        print(f"Successfully loaded {len(paper_docs)} documents from file")
        
        # Extract paper information: title, year, domain
        papers_info = []
        
        for doc in paper_docs:
            filename = doc.get('filename', '')
            text = doc.get('text', '')
            
            # Extract title from filename (remove .txt extension)
            title = filename.replace('.txt', '') if filename else ''
            
            # Extract year from text - look for year patterns (e.g., 2016, '16)
            year = None
            # Look for patterns like: year numbers in headers, or specific year mentions
            year_patterns = [
                r"(\b20\d{2}\b)",  # Full year like 2016
            ]
            
            # Search in the first 500 characters where headers usually are
            header_text = text[:500]
            for pattern in year_patterns:
                matches = re.findall(pattern, header_text)
                if matches:
                    for match in matches:
                        if len(match) == 4:  # Full year
                            year_val = int(match)
                            if 2010 <= year_val <= 2020:  # Reasonable range for papers
                                year = year_val
                                break
                    if year:
                        break
            
            # Check if paper is in physical activity domain
            # Look for 'physical activity' in text (case-insensitive)
            is_physical_activity = 'physical activity' in text.lower()
            
            if title:  # Only include papers with titles
                papers_info.append({
                    'title': title,
                    'year': year,
                    'is_physical_activity': is_physical_activity
                })
        
        # Filter papers from 2016 in physical activity domain
        papers_2016_physical_activity = [p for p in papers_info if p['year'] == 2016 and p['is_physical_activity']]
        
        print(f"Found {len(papers_2016_physical_activity)} papers from 2016 in 'physical activity' domain")
        for paper in papers_2016_physical_activity[:10]:  # Show first 10
            print(f"  - {paper['title']} (Year: {paper['year']})")
        
        # Save the filtered paper titles for joining with citations
        filtered_titles = [p['title'] for p in papers_2016_physical_activity]
        
        # Store results for next step
        print('__RESULT__:')
        print(json.dumps(filtered_titles))
        
    except Exception as e:
        print(f"Error reading or processing file: {e}")
else:
    print("Result key is not a file path string")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
