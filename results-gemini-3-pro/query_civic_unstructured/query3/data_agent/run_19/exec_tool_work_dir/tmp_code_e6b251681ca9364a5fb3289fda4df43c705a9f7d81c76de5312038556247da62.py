code = """import json
import sqlite3
import re
import pandas as pd

# Load Funding Data
with open(locals()['var_function-call-7198597239587007982'], 'r') as f:
    funding_data = json.load(f)

# Load Civic Docs
with open(locals()['var_function-call-13273956969477554140'], 'r') as f:
    civic_docs = json.load(f)

# Prepare Funding DataFrame
df_funding = pd.DataFrame(funding_data)

# Extract Text from Civic Docs
# Combine text from all docs? Or prioritize latest?
# Let's verify if there are multiple docs.
print(f"Number of civic docs: {len(civic_docs)}")
# Sort by filename date just in case
def extract_date(filename):
    # malibucity_agenda_03222023-2060.txt
    match = re.search(r'(\d{8})', filename)
    if match:
        return match.group(1)
    return "00000000"

civic_docs.sort(key=lambda x: extract_date(x.get('filename', '')), reverse=True)
# Use the text from the latest document? Or all?
# Different projects might be in different documents.
# I'll concatenate all text, but maybe mark boundaries.
# Or better: search in all docs, if found in multiple, take the one from the latest doc.

project_status_map = {} # {ProjectName: {status, topic, extracted_name}}

keywords = ["park", "road", "FEMA", "fire", "emergency", "drainage", "storm drain", "highway", "bridge", "playground", "water treatment", "guardrail", "sirens", "warning", "disaster", "culvert", "slide", "slope"]

def get_status_from_header(text, pos):
    # Search backwards for header
    # Headers: "Capital Improvement Projects (Design)", "Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)"
    # Also "Disaster Recovery Projects"
    
    # Slice text up to pos
    preceding_text = text[:pos]
    # Find last occurrence of headers
    headers = [
        ("Capital Improvement Projects (Design)", "design"),
        ("Capital Improvement Projects (Construction)", "Construction"),
        ("Capital Improvement Projects (Not Started)", "not started"),
        ("Disaster Recovery Projects", "disaster recovery"), # Maybe status? Or Type?
        ("Capital Improvement Projects", "unknown") # Fallback
    ]
    
    last_header = None
    max_idx = -1
    for h_str, status in headers:
        idx = preceding_text.rfind(h_str)
        if idx > max_idx:
            max_idx = idx
            last_header = status
            
    return last_header if last_header else "unknown"

def clean_name(name):
    # Remove suffixes like (FEMA Project), (CalOES Project)
    # Regex to remove parenthesized content at end
    return re.sub(r'\s*\(.*?\)\s*$', '', name)

# Iterate over funding projects
results = []

for index, row in df_funding.iterrows():
    p_name = row['Project_Name']
    f_source = row['Funding_Source']
    amount = row['Amount']
    
    # Determine if project is related to FEMA/Emergency by Name
    name_related = False
    if re.search(r'(emergency|FEMA)', p_name, re.IGNORECASE):
        name_related = True
        
    # Search in docs
    found_info = None
    
    # Try Exact Match First
    for doc in civic_docs:
        text = doc['text']
        # Escape for regex
        pattern = re.escape(p_name)
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            start_idx = match.start()
            end_idx = match.end()
            
            # Extract text block: from end_idx to next double newline or next known project?
            # Simple heuristic: next 500 chars or until next header/bullet
            # Look for "(cid:190)" bullets or newlines
            # Better: Text usually has structure.
            # I'll take a chunk.
            chunk = text[end_idx:end_idx+2000]
            
            # Extract Status from Header (look backwards from start_idx)
            status = get_status_from_header(text, start_idx)
            
            # Check for completion in chunk
            if "Construction was completed" in chunk or "Notice of completion" in chunk:
                status = "completed"
                
            # Extract topics
            found_keywords = []
            for k in keywords:
                if re.search(r'\b' + re.escape(k) + r'\b', chunk, re.IGNORECASE) or re.search(r'\b' + re.escape(k) + r'\b', p_name, re.IGNORECASE):
                    found_keywords.append(k)
            
            found_info = {
                "status": status,
                "topics": found_keywords,
                "text_snippet": chunk
            }
            break # Found in latest doc (since we sorted)
    
    # If not found, try Base Name match
    if not found_info:
        base_name = clean_name(p_name)
        if base_name != p_name and len(base_name) > 5:
            for doc in civic_docs:
                text = doc['text']
                pattern = re.escape(base_name)
                match = re.search(pattern, text, re.IGNORECASE)
                if match:
                    start_idx = match.start()
                    end_idx = match.end()
                    chunk = text[end_idx:end_idx+2000]
                    status = get_status_from_header(text, start_idx)
                    if "Construction was completed" in chunk or "Notice of completion" in chunk:
                        status = "completed"
                    found_keywords = []
                    for k in keywords:
                        if re.search(r'\b' + re.escape(k) + r'\b', chunk, re.IGNORECASE) or re.search(r'\b' + re.escape(k) + r'\b', p_name, re.IGNORECASE):
                            found_keywords.append(k)
                    found_info = {
                        "status": status,
                        "topics": found_keywords,
                        "text_snippet": chunk
                    }
                    break
    
    if found_info:
        # Check if related to FEMA/Emergency
        # Criteria: Name has keywords OR Topics has keywords
        is_related = name_related
        if not is_related:
            for t in found_info['topics']:
                if t.lower() in ['fema', 'emergency']:
                    is_related = True
                    break
        # Also check text snippet for 'FEMA' or 'Emergency'
        if not is_related:
            if re.search(r'(emergency|FEMA)', found_info['text_snippet'], re.IGNORECASE):
                is_related = True

        if is_related:
            results.append({
                "Project Name": p_name,
                "Funding Source": f_source,
                "Amount": amount,
                "Status": found_info['status']
            })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-7198597239587007982': 'file_storage/function-call-7198597239587007982.json', 'var_function-call-7198597239587008259': 'file_storage/function-call-7198597239587008259.json', 'var_function-call-13273956969477554140': 'file_storage/function-call-13273956969477554140.json'}

exec(code, env_args)
