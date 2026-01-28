code = """import json
import re

# Load citations
with open(locals()['var_function-call-15899723909047088907'], 'r') as f:
    citations_data = json.load(f)

# Load paper docs
with open(locals()['var_function-call-3855934582646754385'], 'r') as f:
    paper_docs = json.load(f)

# Create a lookup for citation counts for 2020
# citations_data is a list of dicts: {'title': ..., 'citation_count': ...}
citation_map = {}
for item in citations_data:
    citation_map[item['title']] = int(item['citation_count'])

total_citations = 0
chi_papers = []

for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    
    # Check for CHI venue
    # Look for "CHI" as a whole word in the first 2000 characters
    # Common headers: "CHI '15", "CHI 2015", "Proceedings of CHI", "CHI Conference"
    # Also checking if it is NOT "OzCHI" or others if they share the substring (handled by \b)
    # Using re.IGNORECASE might be risky if "chi" is a word, but CHI is usually caps in headers.
    # However, sometimes it's "Chi". Let's stick to case sensitive "CHI" or "Conference on Human Factors in Computing Systems"
    
    # Heuristic: Check first 2000 chars
    header_text = text[:3000]
    
    # Regex for CHI venue
    # We want to match "CHI" but not "OzCHI", "ARCHI", etc.
    # Also we want to ensure it's likely the venue, not just a mention in text.
    # Usually appears near dates or "Proceedings of".
    # But for this task, presence of "CHI" in the first part is the best proxy.
    
    if re.search(r'\bCHI\b', header_text) or re.search(r'Conference on Human Factors in Computing Systems', header_text, re.IGNORECASE):
        # Additional check: exclude "OzCHI" if it was matched by generic means? 
        # \bCHI\b excludes OzCHI.
        
        # Check if it is really CHI. 
        # Sometimes "CHI" is mentioned in "Permission to make digital... CHI...".
        # Which is standard for ACM CHI papers.
        
        # Extract title
        title = filename.replace('.txt', '')
        
        if title in citation_map:
            total_citations += citation_map[title]
            chi_papers.append(title)

print("__RESULT__:")
print(total_citations)"""

env_args = {'var_function-call-15899723909047088907': 'file_storage/function-call-15899723909047088907.json', 'var_function-call-3855934582646754385': 'file_storage/function-call-3855934582646754385.json'}

exec(code, env_args)
