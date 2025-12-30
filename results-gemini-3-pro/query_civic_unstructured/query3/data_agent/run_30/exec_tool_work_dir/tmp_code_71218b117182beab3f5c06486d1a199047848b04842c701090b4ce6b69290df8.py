code = """import json
import re

with open(locals()['var_function-call-8110328958345281458'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-13323334654076855934'], 'r') as f:
    civic_docs = json.load(f)

doc_text = " ".join([d['text'] for d in civic_docs])
# Normalize text to avoid newline issues in regex
doc_text = doc_text.replace('\n', ' ')

def clean_name(name):
    name = name.split('(')[0].strip()
    return name

results = []
for rec in funding_data:
    fname = rec['Project_Name']
    fsource = rec['Funding_Source']
    amount = rec['Amount']
    
    # Check funding relevance
    is_f_rel = 'fema' in fname.lower() or 'emergency' in fname.lower() or 'fema' in fsource.lower()
    
    # Search in doc
    c_name = clean_name(fname)
    # Escape regex special chars in name
    # We use basic string find instead of regex to avoid issues, or simple regex
    # But names might have symbols. re.escape is safe.
    pattern = re.escape(c_name)
    
    status = "Unknown"
    is_d_rel = False
    
    # Find all occurrences
    matches = [m.start() for m in re.finditer(pattern, doc_text, re.IGNORECASE)]
    
    if matches:
        # Check the context of the first match (or all?)
        # Let's check the first one for status/relevance
        idx = matches[0]
        # Look around
        start_ctx = max(0, idx - 1000)
        end_ctx = min(len(doc_text), idx + 1000)
        context = doc_text[start_ctx:end_ctx].lower()
        
        # Determine Status from context (looking for headers or nearby status words)
        # Note: Headers like "Capital Improvement Projects (Design)" might be far back.
        # But we normalized newlines to spaces, so regex search for headers works.
        # We search backwards from idx for the last header.
        
        pre_text = doc_text[start_ctx:idx] # Text before name
        # Find last header
        header_pat = r'capital improvement projects \((design|construction|not started)\)'
        headers = list(re.finditer(header_pat, pre_text, re.IGNORECASE))
        if headers:
            last_header = headers[-1].group(1).lower()
            if last_header == 'design':
                status = "Design"
            elif last_header == 'construction':
                status = "Construction" # User hint says: design, completed, not started. I will map construction to "Design" or keep as Construction. I'll keep "Construction" as it's more specific, or "Design" if I must strictly follow hints? Hints say "Projects have three statuses...". Maybe "Construction" falls under "Design" or "Completed"? No. Usually Construction is the phase after Design.
                # But wait, hint says "Projects have three statuses: 'design', 'completed', and 'not started'".
                # It doesn't list 'construction'.
                # But the doc has "Capital Improvement Projects (Construction)".
                # This is a contradiction. I will output "Construction" because it's in the text.
                # Wait, if I must follow hints... "Projects have three statuses...".
                # Maybe Construction projects are 'active'?
                # I'll stick to what the document says: "Construction".
            elif last_header == 'not started':
                status = "Not Started"
        
        # Check for completion in context
        if "construction was completed" in context or "notice of completion" in context:
            status = "Completed"
            
        # Check relevance in context
        if 'fema' in context or 'emergency' in context or 'caloes' in context:
            is_d_rel = True
            
    if is_f_rel or is_d_rel:
        results.append({
            "Project_Name": fname,
            "Funding_Source": fsource,
            "Amount": amount,
            "Status": status
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-8110328958345281458': 'file_storage/function-call-8110328958345281458.json', 'var_function-call-13323334654076855934': 'file_storage/function-call-13323334654076855934.json'}

exec(code, env_args)
