code = """import json

# Get both datasets - they should be available in the local scope
# Use the actual variable pattern shown in the system messages
papers = var_functions_query_db_12
citations_path = var_functions_query_db_13

# Load citations from file path
with open(citations_path, 'r') as f:
    citations = json.load(f)

print('Papers loaded:', len(papers))
print('Citations loaded:', len(citations))

# Process papers to extract metadata
paper_metadata = []
for paper in papers:
    filename = paper['filename']
    title = filename.replace('.txt', '')
    text = paper['text']
    
    # Extract year from text (look for patterns like '2017', '2015', etc.)
    year_match = re.search(r'(19|20)\d{2}', text)
    year = int(year_match.group()) if year_match else None
    
    # Check if contribution type is empirical
    is_empirical = 'empirical' in text.lower()
    
    # Extract venue (look for common venues)
    venue_match = re.search(r'(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|HCI|UIST)', text, re.IGNORECASE)
    venue = venue_match.group() if venue_match else None
    
    paper_metadata.append({
        'title': title,
        'year': year,
        'venue': venue,
        'is_empirical': is_empirical,
        'filename': filename
    })

print('Processed paper metadata, sample:', paper_metadata[0])
print('Found empirical papers:', sum(1 for p in paper_metadata if p['is_empirical']))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json'}

exec(code, env_args)
