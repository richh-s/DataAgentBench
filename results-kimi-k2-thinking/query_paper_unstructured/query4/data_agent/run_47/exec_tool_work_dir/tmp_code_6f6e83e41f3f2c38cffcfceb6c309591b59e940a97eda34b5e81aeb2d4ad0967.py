code = """import json
import re
from collections import defaultdict

# Get the file paths from storage
mongo_result_path = locals()['var_functions.query_db:2']
citations_result_path = locals()['var_functions.query_db:12']

# Load the MongoDB results
with open(mongo_result_path, 'r') as f:
    mongo_papers = json.load(f)

# Load the citations data
with open(citations_result_path, 'r') as f:
    citations_data = json.load(f)

# Create a dictionary for citation lookups
citation_dict = {item['title']: int(item['total_citations']) for item in citations_data}

# Find papers from 2016 in physical activity domain
papers_2016_physical_activity = []

for paper in mongo_papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Convert to lowercase for searching
    text_lower = text.lower()
    
    # Check if paper is in physical activity domain (contains "physical activity")
    if 'physical activity' in text_lower:
        # Try to extract the publication year looking for common patterns
        year = None
        
        # Pattern 1: Look for venue year patterns like "CHI 2016", "Ubicomp 2016", etc.
        venue_pattern = r'(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UIST|SUI|ISS|MobileHCI)\s+2016'
        match = re.search(venue_pattern, text, re.IGNORECASE)
        if match:
            year = 2016
        
        # Pattern 2: Look for copyright notices with 2016
        if not year:
            copyright_pattern = r'Copyright.*\b2016\b'
            if re.search(copyright_pattern, text):
                year = 2016
        
        # Pattern 3: Look for "2016" in context of publication
        if not year:
            # Count occurrences of 2016 in the text and see if it's likely a publication year
            year_2016_matches = re.findall(r'\b2016\b', text)
            if len(year_2016_matches) > 0:
                # Check if this looks like a 2016 paper by looking at the first page content
                # Typically first 2000 characters contain header info
                header_text = text[:2000]
                if '2016' in header_text:
                    year = 2016
        
        if year == 2016:
            # Get total citations if available
            total_citations = citation_dict.get(title, 0)
            
            papers_2016_physical_activity.append({
                'title': title,
                'total_citations': total_citations
            })

# Sort by citation count (descending)
papers_2016_physical_activity.sort(key=lambda x: x['total_citations'], reverse=True)

print('__RESULT__:')
print(json.dumps(papers_2016_physical_activity, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'papers_found': 5, 'papers': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', '_id': '694f5530284b10b11dc0a86b'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', '_id': '694f5530284b10b11dc0a86c'}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt', '_id': '694f5530284b10b11dc0a870'}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'filename': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt", '_id': '694f5530284b10b11dc0a871'}, {'title': 'Charting Design Preferences on Wellness Wearables', 'filename': 'Charting Design Preferences on Wellness Wearables.txt', '_id': '694f5530284b10b11dc0a873'}]}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
