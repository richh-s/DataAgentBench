code = """import json
import re
import os

# Load citations
with open(locals()['var_function-call-14258248544266261240'], 'r') as f:
    citations_data = json.load(f)

# Create a lookup for citation counts by title
citation_map = {}
for entry in citations_data:
    citation_map[entry['title']] = entry['citation_count']

# Load paper documents
# The result might be a list of documents.
with open(locals()['var_function-call-18048887829581669547'], 'r') as f:
    papers_data = json.load(f)

total_citations = 0
chi_papers_count = 0
found_titles = []

for paper in papers_data:
    filename = paper.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    
    # Check if this paper was cited in 2020 (i.e., is in our citation map)
    if title in citation_map:
        text = paper.get('text', '')
        # Check for CHI venue in the first 500 characters
        # Look for "CHI" followed by year or in a header context
        # Sample header: "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN"
        # Potential CHI header: "CHI '20, April 25-30, 2020, Honolulu, HI, USA" or "CHI 2016"
        
        header = text[:500]
        # Regex to match CHI followed by year like CHI '15, CHI 2015
        # Or just CHI in the first line if it stands alone
        
        # We also need to be careful not to match "CHI" in "Architecting..." if it's not a venue.
        # But in the header, "CHI" is usually distinct.
        
        if re.search(r"\bCHI\b", header):
            # To be safer, checking for CHI followed by a year or 'YY
            if re.search(r"CHI\s*['’]?\d{2,4}", header) or "CHI Conference" in header or "Conference on Human Factors in Computing Systems" in header:
                 total_citations += citation_map[title]
                 chi_papers_count += 1
                 found_titles.append(title)
            else:
                 # Fallback: if header contains CHI and a date/location pattern, count it.
                 # For now, let's assume CHI + year is sufficient.
                 # Let's log if we see CHI but not year, to be sure.
                 pass

print(f"DEBUG: Found {chi_papers_count} CHI papers cited in 2020.")
print(f"DEBUG: Total citations: {total_citations}")

print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-14258248544266261240': 'file_storage/function-call-14258248544266261240.json', 'var_function-call-14258248544266263107': 'file_storage/function-call-14258248544266263107.json', 'var_function-call-18048887829581669547': 'file_storage/function-call-18048887829581669547.json'}

exec(code, env_args)
