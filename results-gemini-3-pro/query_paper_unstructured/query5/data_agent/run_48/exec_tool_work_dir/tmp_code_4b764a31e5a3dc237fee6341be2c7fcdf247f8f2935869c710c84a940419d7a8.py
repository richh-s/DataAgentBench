code = """import json
import re

# Load citations
with open(locals()['var_function-call-264858034059979045'], 'r') as f:
    citations = json.load(f)

# Load papers
with open(locals()['var_function-call-8351315325764085192'], 'r') as f:
    papers_list = json.load(f)

# Create a map filename -> text
# filename is title + ".txt"
# Be careful with potential mismatches if any
paper_map = {p['filename']: p['text'] for p in papers_list}

total_citations = 0
chi_papers = []

for cite in citations:
    title = cite['title']
    filename = title + ".txt"
    text = paper_map.get(filename, "")
    
    if not text:
        continue
        
    # Check first 1000 chars for venue
    header = text[:1000]
    
    # Check for CHI patterns
    # Pattern 1: CHI followed by year (e.g. CHI '15, CHI 2015, CHI 2011, CHI’15)
    # Pattern 2: Conference on Human Factors in Computing Systems
    
    is_chi = False
    
    # Regex for CHI year
    # \bCHI\b matches CHI word boundary
    # [\s\W]* matches space or non-word chars (like ' or ’)
    # \d{2,4} matches year
    if re.search(r"\bCHI[\s\W]*\d{2,4}", header, re.IGNORECASE):
        is_chi = True
        
    if "Conference on Human Factors in Computing Systems" in header:
        is_chi = True
        
    # Exclude OzCHI, CHI Play if they are the match
    if re.search(r"\bOzCHI\b", header, re.IGNORECASE):
        is_chi = False
    if re.search(r"\bCHI Play\b", header, re.IGNORECASE):
        is_chi = False
        
    # Double check if other venues are present in the header which might indicate it's not CHI
    # e.g. "UbiComp", "CSCW", "DIS", "IUI", "TEI"
    # But only if "CHI" was found. If "CHI" is found, and "UbiComp" is also found, 
    # it might be "UbiComp... (formerly CHI...)"? Unlikely.
    # More likely "UbiComp '14 ... copyright ... ACM".
    # If "CHI" is found in "ACM CHI Conference", and "UbiComp" is not found -> CHI.
    # What if "CHI" is in "Archived in CHI proceedings"?
    
    # Let's assume the presence of "CHI <Year>" in the first 1000 chars is a strong indicator of CHI venue,
    # unless "OzCHI" or "CHI Play" is explicitly mentioned.
    
    if is_chi:
        # Check for conflicts
        if re.search(r"\bUbiComp\b", header, re.IGNORECASE):
             # check which one comes first or if one is dominant
             # Usually the venue name is at the top.
             # If "UbiComp" is in the header, it's likely UbiComp.
             # Exceptions: "UbiComp" mentioned in text.
             # But we are looking at first 1000 chars.
             # Let's verify with an example. "Sundroid" had "UbiComp'11".
             # If it had "CHI" in the header (e.g. in keywords), it might trigger.
             # Sundroid header: "UbiComp’11...". No "CHI".
             pass
             
        chi_papers.append(title)
        total_citations += int(cite['citation_count'])

print(f"Found {len(chi_papers)} CHI papers.")
print(f"Total citations: {total_citations}")
print(f"Sample CHI papers: {chi_papers[:5]}")

print("__RESULT__:")
print(json.dumps({"total_citations": total_citations, "num_papers": len(chi_papers)}))"""

env_args = {'var_function-call-264858034059979045': 'file_storage/function-call-264858034059979045.json', 'var_function-call-16262197769178367218': {'count': 188, 'sample_title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, 'var_function-call-2494524119581093015': 'file_storage/function-call-2494524119581093015.json', 'var_function-call-3380312142503180972': 'file_storage/function-call-3380312142503180972.json', 'var_function-call-8351315325764085192': 'file_storage/function-call-8351315325764085192.json'}

exec(code, env_args)
