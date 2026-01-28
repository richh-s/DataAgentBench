code = """import json
import re

# Get the data from storage
citations_data = locals()['var_functions.query_db:7']
papers_data = locals()['var_functions.query_db:8']

# Load from file paths if they are strings (file paths)
if isinstance(citations_data, str):
    with open(citations_data, 'r') as f:
        citations_data = json.load(f)

if isinstance(papers_data, str):
    with open(papers_data, 'r') as f:
        papers_data = json.load(f)

# Now proceed with the analysis
print('Number of citations records:', len(citations_data))
print('Number of paper documents:', len(papers_data))
print('\nSample citation record:', citations_data[0])
print('\nSample paper document keys:', list(papers_data[0].keys()))
print('\nSample paper document filename:', papers_data[0].get('filename'))

# Parse paper data to extract venue information
# We'll look for CHI in the text and extract publication info
chi_papers = []

for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '').lower()
    
    # Check if this is a CHI paper
    if 'chi' in filename.lower() or 'chi' in text:
        # Extract title from filename
        title_from_filename = filename.replace('.txt', '')
        
        # Look for year in the text
        year_match = re.search(r'(20\d\d)', text)
        year = year_match.group(1) if year_match else None
        
        # Look for venue info
        venue_match = re.search(r'(chi\s*[\'"]?\d{2}|chi\s+\d{4})', text, re.IGNORECASE)
        venue_info = venue_match.group(1) if venue_match else 'CHI'
        
        chi_papers.append({
            'title': title_from_filename,
            'year': year,
            'venue': venue_info,
            'filename': filename
        })

print('\nNumber of potential CHI papers found:', len(chi_papers))
if chi_papers:
    print('Sample CHI paper:', chi_papers[0])"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
