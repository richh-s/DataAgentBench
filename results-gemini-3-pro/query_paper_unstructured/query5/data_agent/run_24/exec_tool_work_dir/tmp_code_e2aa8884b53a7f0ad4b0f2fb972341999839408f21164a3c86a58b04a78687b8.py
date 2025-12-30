code = """import json
import re

# Load citation data
with open(locals()['var_function-call-3271567953918083251'], 'r') as f:
    citations_data = json.load(f)

# Create a dictionary for quick lookup of citations: title -> count
citation_map = {}
for entry in citations_data:
    citation_map[entry['title']] = int(entry['citation_count'])

# Load paper docs
with open(locals()['var_function-call-17597164597794673073'], 'r') as f:
    paper_docs = json.load(f)

chi_citation_sum = 0
chi_papers_count = 0

# Regex for CHI venue
# Matches: "CHI '15", "CHI 2015", "CHI Conference", "Conference on Human Factors in Computing Systems"
# Must be careful to avoid "OzCHI", "CHI Play", etc. so use word boundaries or start of string
venue_regex = re.compile(r"\bCHI\s?'\d{2}|\bCHI\s?20\d{2}|Conference on Human Factors in Computing Systems", re.IGNORECASE)

# Helper to check if text indicates CHI
def is_chi_paper(text):
    # Check first 1000 chars for venue info
    header = text[:1000]
    
    if venue_regex.search(header):
        # Double check it's not OzCHI or something else if possible, but the regex \bCHI should handle it.
        # However, "OzCHI" contains "CHI". \bCHI\b ensures it starts with C.
        # But "CHI '15" might match.
        # Let's verify specific patterns.
        # If "OzCHI" is present, \bCHI might not match if Oz is part of the word. "OzCHI" -> \bOzCHI\b.
        # But "CHI" is separate word usually.
        return True
    return False

for doc in paper_docs:
    filename = doc.get('filename', '')
    if not filename.endswith('.txt'):
        continue
    title = filename[:-4] # Remove .txt
    
    # Check if we have citation info for this paper in 2020
    if title in citation_map:
        text = doc.get('text', '')
        if is_chi_paper(text):
            count = citation_map[title]
            chi_citation_sum += count
            chi_papers_count += 1

print(f"DEBUG: Found {chi_papers_count} CHI papers with citations in 2020.")
print("__RESULT__:")
print(json.dumps(chi_citation_sum))"""

env_args = {'var_function-call-3271567953918083251': 'file_storage/function-call-3271567953918083251.json', 'var_function-call-3271567953918083494': ['paper_docs'], 'var_function-call-17597164597794673073': 'file_storage/function-call-17597164597794673073.json'}

exec(code, env_args)
