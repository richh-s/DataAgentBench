code = """import json
import re

# Read the full MongoDB results from the file
mongo_file_path = var_functions.query_db:2
with open(mongo_file_path, 'r') as f:
    all_papers = json.load(f)

print(f"Total papers retrieved: {len(all_papers)}")

# Function to extract paper information from the text
paper_info = []

for paper in all_papers:
    filename = paper['filename']
    text = paper['text']
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '')
    
    # Extract year from text - look for patterns like "20XX" near venue information
    # Common patterns: CHI '17, Ubicomp '15, etc.
    year_match = re.search(r"'(\d{2})\b", text)
    year = None
    if year_match:
        year_str = year_match.group(1)
        # Convert to full year (assuming 2000s)
        year = 2000 + int(year_str)
    
    # Extract contribution - look for patterns that indicate contribution type
    # The hints mention contributions like: "empirical", "artifact", "theoretical", "survey", "methodological"
    contribution = []
    
    # Look for contribution-related keywords in the text
    text_lower = text.lower()
    
    if 'empirical' in text_lower:
        contribution.append('empirical')
    if 'artifact' in text_lower:
        contribution.append('artifact')
    if 'theoretical' in text_lower:
        contribution.append('theoretical')
    if 'survey' in text_lower:
        contribution.append('survey')
    if 'methodological' in text_lower or 'methodology' in text_lower:
        contribution.append('methodological')
    
    paper_info.append({
        'title': title,
        'year': year,
        'contribution': contribution,
        'filename': filename
    })

# Filter papers with 'empirical' contribution and published after 2016
empirical_papers_after_2016 = [
    paper for paper in paper_info 
    if 'empirical' in paper['contribution'] and paper['year'] and paper['year'] > 2016
]

print(f"Papers with empirical contribution after 2016: {len(empirical_papers_after_2016)}")

# For debugging, show a few examples
for i, paper in enumerate(empirical_papers_after_2016[:5]):
    print(f"{i+1}. {paper['title']} - Year: {paper['year']}")

# Save the filtered papers
filtered_papers = empirical_papers_after_2016

print('__RESULT__:')
print(json.dumps(filtered_papers))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
