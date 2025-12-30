code = """import json
import re

# Load citations
with open(locals()['var_function-call-16389443028975404888'], 'r') as f:
    citations = json.load(f)

# Load papers
with open(locals()['var_function-call-7093843895895526717'], 'r') as f:
    papers = json.load(f)

# Create a dictionary for quick lookup of papers by filename
paper_dict = {p['filename']: p['text'] for p in papers}

acm_citations = []
missing_papers = []

for c in citations:
    title = c['title']
    filename = title + ".txt"
    if filename in paper_dict:
        text = paper_dict[filename]
        # Check for ACM in the first 5000 characters (header/copyright usually there)
        # Using a simple check. "ACM" usually appears in copyright or header.
        # "IEEE" usually appears similarly.
        # Check specific patterns to be more robust?
        # "Copyright ... ACM" or "Permission ... ACM"
        head_text = text[:5000]
        
        is_acm = False
        if "ACM" in head_text:
            is_acm = True
        elif "Association for Computing Machinery" in head_text:
            is_acm = True
            
        # Verify if IEEE is there to avoid confusion (though a paper is usually one or the other)
        if "IEEE" in head_text and not is_acm:
            # likely IEEE
            pass
        elif "IEEE" in head_text and is_acm:
            # Both? Usually ACM conferences might mention IEEE in references or joint.
            # But the prompt implies distinct sources.
            # Let's assume if it has ACM copyright it is ACM.
            pass
            
        if is_acm:
            acm_citations.append(int(c['citation_count']))
    else:
        missing_papers.append(title)

# Calculate average
if acm_citations:
    avg_citations = sum(acm_citations) / len(acm_citations)
else:
    avg_citations = 0

print(f"DEBUG: Found {len(acm_citations)} ACM papers out of {len(citations)} citations.")
print(f"DEBUG: Missing papers: {len(missing_papers)}")

print("__RESULT__:")
print(json.dumps(avg_citations))"""

env_args = {'var_function-call-16389443028975404888': 'file_storage/function-call-16389443028975404888.json', 'var_function-call-10458991170078353782': 'file_storage/function-call-10458991170078353782.json', 'var_function-call-7093843895895526717': 'file_storage/function-call-7093843895895526717.json'}

exec(code, env_args)
