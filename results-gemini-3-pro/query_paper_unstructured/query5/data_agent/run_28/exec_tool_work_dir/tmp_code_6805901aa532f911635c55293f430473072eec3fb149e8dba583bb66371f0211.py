code = """import json
import re

# Load citations
with open(locals()['var_function-call-9700206069512387348'], 'r') as f:
    citations_data = json.load(f)

# Create a lookup for citation counts: title -> count
citation_map = {}
for entry in citations_data:
    # SQL result might have string or int for count. Sample showed "65" (string).
    # Convert to int.
    try:
        count = int(entry['citation_count'])
        citation_map[entry['title']] = count
    except ValueError:
        continue

# Load paper docs
with open(locals()['var_function-call-15345152852245153349'], 'r') as f:
    papers_data = json.load(f)

total_citations = 0
chi_papers_count = 0

for paper in papers_data:
    filename = paper.get('filename', '')
    if not filename.endswith('.txt'):
        continue
    
    title = filename[:-4] # Remove .txt
    
    if title in citation_map:
        text = paper.get('text', '')
        # Check for CHI venue in the first 1000 characters
        # Look for "CHI" as a whole word, often followed by year or 'YY
        # Or "Proceedings of ... CHI"
        # Using a regex that looks for "CHI" in uppercase distinct word
        
        # Taking first 500 chars
        header = text[:500]
        
        # Regex: \bCHI\b matches "CHI" surrounded by word boundaries.
        # This avoids "Chi" in "Chi-squared" if it's mixed case, but we want strict CHI usually.
        # But let's check the sample "UBICOMP '15". It is uppercase.
        
        if re.search(r'\bCHI\b', header):
             # To be safer, maybe check if it looks like a venue string?
             # But "CHI" is quite specific in this context (HCI papers).
             # Let's count it.
             total_citations += citation_map[title]
             chi_papers_count += 1

print(f"Found {chi_papers_count} CHI papers.")
print("__RESULT__:")
print(total_citations)"""

env_args = {'var_function-call-9042960770956765793': ['Citations', 'sqlite_sequence'], 'var_function-call-9042960770956765216': ['paper_docs'], 'var_function-call-9700206069512387348': 'file_storage/function-call-9700206069512387348.json', 'var_function-call-9700206069512385745': 'file_storage/function-call-9700206069512385745.json', 'var_function-call-15345152852245153349': 'file_storage/function-call-15345152852245153349.json'}

exec(code, env_args)
