code = """import json
import re

# Read the MongoDB documents
mongo_file_path = var_functions.query_db:2
with open(mongo_file_path, 'r') as f:
    paper_docs = json.load(f)

print(f"Total papers in MongoDB: {len(paper_docs)}")

# Extract relevant information from each paper document
papers_info = []
for doc in paper_docs:
    try:
        # Extract title from filename (remove .txt extension)
        filename = doc.get('filename', '')
        title = filename.replace('.txt', '') if filename else ''
        text = doc.get('text', '')
        
        # Extract year from text - look for common patterns like "2015" or "'15"
        # Look for venue years like "UbiComp '15" or "2015"
        year = None
        
        # Pattern 1: Look for year in venue format (e.g., "UbiComp '15", "CHI '16")
        venue_year_match = re.search(r"[A-Za-z]+\s+'(\d{2})", text)
        if venue_year_match:
            year_str = venue_year_match.group(1)
            if year_str.startswith('1'):
                year = 1900 + int(year_str)
            else:
                year = 2000 + int(year_str)
        
        # Pattern 2: Look for four-digit year in parentheses
        if not year:
            year_match = re.search(r"\b(20\d{2})\b", text)
            if year_match:
                year = int(year_match.group(1))
        
        # Extract domain - look for "physical activity" mention
        # Convert to lowercase for case-insensitive matching
        text_lower = text.lower()
        domain_mentions = []
        
        # Common domains to check
        domains = ['physical activity', 'sleep', 'food', 'mental', 'finances', 
                  'productivity', 'screen time', 'social interactions', 'location',
                  'chronic', 'diabetes', 'health_behavior', 'health', 'fitness']
        
        # Use word boundaries to avoid partial matches
        for dom in domains:
            if re.search(r'\b' + re.escape(dom) + r'\b', text_lower):
                domain_mentions.append(dom)
        
        # Also check for "physical activity" specifically (case variations)
        if 'physical activity' in text_lower:
            domain_mentions.append('physical activity')
        
        # Combine domains into a comma-separated string, or None if empty
        domain_str = ', '.join(domain_mentions) if domain_mentions else None
        
        papers_info.append({
            'title': title,
            'year': year,
            'domain': domain_str,
            'filename': filename
        })
    except Exception as e:
        print(f"Error processing document: {e}")
        continue

# Filter for papers from 2016 in physical activity domain
filtered_papers = []
for paper in papers_info:
    if paper['year'] == 2016 and paper['domain'] and 'physical activity' in paper['domain'].lower():
        filtered_papers.append(paper)

print(f"Papers from 2016 in 'physical activity' domain: {len(filtered_papers)}")
for p in filtered_papers:
    print(f"  - {p['title']} (Year: {p['year']}, Domain: {p['domain']})")

# Convert to JSON-serializable format
result = json.dumps({
    'all_papers_count': len(papers_info),
    'filtered_papers': filtered_papers
})

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}]}

exec(code, env_args)
