code = """import json
import re

# Read the MongoDB result from the file
mongo_file_path = var_functions.query_db:5
with open(mongo_file_path, 'r') as f:
    paper_docs = json.load(f)

# Function to extract paper information from text
extracted_papers = []

for doc in paper_docs:
    try:
        filename = doc['filename']
        # Extract title from filename
        title = filename.replace('.txt', '')
        
        text = doc.get('text', '')
        
        # Extract year - look for patterns like year numbers in 20xx format
        year_match = re.search(r'(?:\b|20)(1[7-9]|20[2-9])\b', text)
        if year_match:
            year_str = year_match.group()
            # Ensure it's a 4-digit year
            if len(year_str) == 2 and year_str.startswith('1'):
                year = int('20' + year_str)
            elif len(year_str) == 4:
                year = int(year_str)
            else:
                year = None
        else:
            year = None
        
        # Extract contribution type - search for keywords
        contribution = None
        contribution_words = ['empirical', 'artifact', 'theoretical', 'survey', 'methodological']
        
        for word in contribution_words:
            if re.search(r'\b' + word + r'\b', text, re.IGNORECASE):
                contribution = word
                break
        
        # Also check for contribution phrases
        if not contribution:
            if re.search(r'empirical\s+(study|research|evaluation|investigation|work)', text, re.IGNORECASE):
                contribution = 'empirical'
            elif re.search(r'theoretical\s+(framework|model|contribution|work)', text, re.IGNORECASE):
                contribution = 'theoretical'
            elif re.search(r'artifact\s+(design|system|contribution|work)', text, re.IGNORECASE):
                contribution = 'artifact'
        
        # Extract venue (conference/journal)
        venue_match = re.search(r'\b(CHI|Ubicomp|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UBICOMP)\b', text, re.IGNORECASE)
        venue = venue_match.group().upper() if venue_match else None
        # Normalize UbiComp/Ubicomp variations
        if venue and 'UBICOMP' in venue.upper():
            venue = 'Ubicomp'
        
        # Extract source (publisher)
        source_match = re.search(r'\b(ACM|IEEE|PubMed)\b', text, re.IGNORECASE)
        source = source_match.group() if source_match else None
        
        # Extract domain
        domain_candidates = ['food', 'physical activity', 'sleep', 'mental', 'finances', 'productivity', 'screen time', 'social interactions', 'location', 'chronic', 'diabetes', 'health_behavior']
        domain = None
        for candidate in domain_candidates:
            if re.search(r'\b' + re.escape(candidate) + r'\b', text, re.IGNORECASE):
                domain = candidate
                break
        
        # Only include papers with valid year and title
        if title and year:
            extracted_papers.append({
                'title': title,
                'year': year,
                'contribution': contribution,
                'venue': venue,
                'source': source,
                'domain': domain
            })
    except Exception as e:
        # Skip documents with errors
        continue

# Filter for papers published after 2016 with 'empirical' contribution
empirical_papers_after_2016 = [
    p for p in extracted_papers 
    if p['year'] > 2016 and p['contribution'] == 'empirical'
]

print('__RESULT__:')
print(json.dumps(empirical_papers_after_2016, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
