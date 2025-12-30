code = """import json
import re

# Load citations
with open(locals()['var_function-call-12437250052302532993'], 'r') as f:
    citations_data = json.load(f)

# Filter citations for 2020
citations_2020 = {}
for item in citations_data:
    if int(item['citation_count']) > 0: # Just to be safe, though 0 citations adds nothing
        citations_2020[item['title']] = int(item['citation_count'])

# Load paper docs
with open(locals()['var_function-call-17247428670658995703'], 'r') as f:
    paper_docs = json.load(f)

total_citations = 0
chi_papers_count = 0
matched_papers = []

for doc in paper_docs:
    filename = doc['filename']
    title = filename.rsplit('.', 1)[0] # remove .txt
    text = doc['text']
    
    # Check if paper is in the 2020 citations list
    if title in citations_2020:
        # Check if venue is CHI
        # Look for "CHI" in the first 2000 characters as a whole word
        # Also include "Conference on Human Factors in Computing Systems"
        header = text[:2000]
        
        # Simple regex for CHI as a whole word
        # We might also see "CHI'19" or "CHI 2019"
        if re.search(r'\bCHI\b', header, re.IGNORECASE) or "Human Factors in Computing Systems" in header:
            # Be careful with "CHI" matching "China" or "Architecture" -> \b handles word boundaries
            # However, "CHI" is usually uppercase in headers.
            # Let's check for "CHI" (uppercase) specifically to avoid false positives like "chi" in "machine" if case insensitive?
            # But regex \bCHI\b matches CHI only.
            
            # Additional check: specific CHI conference patterns
            # e.g. "CHI '15", "CHI 2015", "CHI Conference"
            if re.search(r'CHI\s*[\'’]?\d{2,4}', header) or \
               re.search(r'CHI\s+Conference', header) or \
               "Human Factors in Computing Systems" in header or \
               re.search(r'Proceedings of.*CHI', header, re.IGNORECASE) or \
               re.search(r'\bCHI\b', header): # Fallback to strict word match if others fail?
                
                # Let's be slightly more strict to avoid false positives. 
                # If "CHI" is just mentioned in text, it might be wrong.
                # Usually venue is at the top.
                # Let's trust the \bCHI\b in header for now, maybe check if it looks like a header line.
                
                # Refined check:
                is_chi = False
                if "Human Factors in Computing Systems" in header:
                    is_chi = True
                elif re.search(r'CHI\s*[\'’]?\d{2,4}', header): # CHI '12, CHI 2012
                    is_chi = True
                elif re.search(r'\bCHI\b', header) and ("Conference" in header or "Proceedings" in header or "ACM" in header):
                    is_chi = True
                
                # One more check: The hint says "Common venues include: 'CHI'".
                # It is possible the venue is just "CHI".
                # Let's assume \bCHI\b in the first 500 chars is the venue.
                if not is_chi:
                     if re.search(r'\bCHI\b', text[:500]):
                         is_chi = True

                if is_chi:
                    count = citations_2020[title]
                    total_citations += count
                    chi_papers_count += 1
                    matched_papers.append(title)

print(f"Matched {chi_papers_count} CHI papers cited in 2020.")
print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-12437250052302532993': 'file_storage/function-call-12437250052302532993.json', 'var_function-call-17247428670658995703': 'file_storage/function-call-17247428670658995703.json'}

exec(code, env_args)
