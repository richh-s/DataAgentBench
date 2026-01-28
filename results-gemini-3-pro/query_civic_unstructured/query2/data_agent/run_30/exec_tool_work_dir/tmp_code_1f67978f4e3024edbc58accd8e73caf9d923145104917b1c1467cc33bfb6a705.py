code = """import json
import re

# Load data
with open(locals()['var_function-call-3018582044476684640'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-3018582044476683837'], 'r') as f:
    civic_docs = json.load(f)

def is_park_project(name, text_block):
    content = (name + " " + text_block).lower()
    return "park" in content

def is_completed_in_2022(text_block):
    text_lower = text_block.lower()
    # Check for 2022 and completed status
    if "2022" in text_lower:
        if "completed" in text_lower or "completion" in text_lower:
            # Check proximity or specific phrases
            # "Construction was completed November 2022"
            # "completed, November 2022"
            if re.search(r"completed.{0,50}2022", text_lower) or re.search(r"completion.{0,50}2022", text_lower):
                return True
            # Also "November 2022" followed by "Notice of completion filed" might be a completed project
            if "notice of completion" in text_lower and "2022" in text_lower:
                 if re.search(r"completed.{0,50}2022", text_lower):
                     return True
    return False

extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    # Split text into lines to process line by line
    lines = text.split('\n')
    
    # Iterate lines to find potential headers
    # A header is a line that is followed shortly by "Updates:" or "Project Description:"
    # We can detect the bullet char by context if needed, or just skip it.
    
    for i, line in enumerate(lines):
        line_clean = line.strip()
        if not line_clean:
            continue
            
        # Check if this line triggers a section
        # Look ahead a few lines
        is_header = False
        # look ahead 1 or 2 non-empty lines
        look_ahead_count = 0
        for k in range(i + 1, min(i + 5, len(lines))):
            next_line = lines[k].strip()
            if not next_line:
                continue
            look_ahead_count += 1
            # Check for keywords indicating start of content
            if "Updates:" in next_line or "Project Description:" in next_line or "Project Schedule:" in next_line:
                is_header = True
                break
            if look_ahead_count > 1: # Only allow 1 intervening line (e.g. the bullet line)
                break
        
        if is_header:
            # This 'line' is likely the project name
            p_name = line_clean
            
            # Extract the block until the next likely header
            # For simplicity, let's just grab until the end or next clear header
            # But finding the next header is circular.
            # Let's just grab the next 20 lines or until a known stop word?
            # Or use regex on the full text with the known name.
            
            # Let's find where this name is in the full text and slice
            # Be careful with duplicates.
            
            # Alternative: Collect all text from this line index until the next detected header line index.
            # This requires a first pass to identify all header indices.
            pass

# Pass 1: Identify header indices
doc_headers = []
for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    headers = []
    
    for i, line in enumerate(lines):
        line_clean = line.strip()
        if not line_clean: continue
        if len(line_clean) > 100: continue # Likely not a header
        if "Page" in line_clean or "Item" in line_clean: continue
        
        # Check lookahead
        look_ahead_count = 0
        found_marker = False
        for k in range(i + 1, min(i + 6, len(lines))):
            nl = lines[k].strip()
            if not nl: continue
            look_ahead_count += 1
            # Markers often have the bullet char, we can match "Updates" etc
            if "Updates:" in nl or "Project Description:" in nl or "Project Schedule:" in nl:
                found_marker = True
                break
            if look_ahead_count > 2: 
                break
        
        if found_marker:
            headers.append(i)
            
    # Pass 2: Extract blocks
    for idx, start_line_idx in enumerate(headers):
        end_line_idx = headers[idx+1] if idx + 1 < len(headers) else len(lines)
        
        # The header line itself is the name
        p_name = lines[start_line_idx].strip()
        
        # The block is everything from start to end
        block_lines = lines[start_line_idx+1 : end_line_idx]
        block_text = "\n".join(block_lines)
        
        extracted_projects.append({"name": p_name, "text": block_text})

# Filter
relevant_names = set()
for p in extracted_projects:
    if is_park_project(p['name'], p['text']):
        if is_completed_in_2022(p['text']):
            relevant_names.add(p['name'])

# Sum funding
final_sum = 0
found_projects = []

for record in funding_data:
    # Normalize names for comparison? 
    # The prompt says names match.
    if record['Project_Name'] in relevant_names:
        final_sum += int(record['Amount'])
        found_projects.append(record['Project_Name'])

print("__RESULT__:")
print(json.dumps({"total_funding": final_sum, "projects": list(set(found_projects))}))"""

env_args = {'var_function-call-3018582044476684640': 'file_storage/function-call-3018582044476684640.json', 'var_function-call-3018582044476683837': 'file_storage/function-call-3018582044476683837.json'}

exec(code, env_args)
