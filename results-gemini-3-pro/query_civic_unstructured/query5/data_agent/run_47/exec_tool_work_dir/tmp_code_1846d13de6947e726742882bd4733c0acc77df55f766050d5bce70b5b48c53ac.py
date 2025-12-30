code = """import pandas as pd
import json
import re

with open(locals()['var_function-call-17465459041874363350'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

with open(locals()['var_function-call-17465459041874365577'], 'r') as f:
    civic_docs = json.load(f)

def is_disaster_project(name, text_block):
    name_lower = name.lower()
    text_lower = text_block.lower()
    keywords = ['fema', 'caloes', 'caljpia', 'disaster', 'woolsey fire', 'emergency', 'recovery']
    
    if any(k in name_lower for k in keywords):
        return True
    if any(k in text_lower for k in keywords):
        return True
    return False

def started_in_2022(text_block):
    # Regexes to capture the date part at the end of the line
    # We use simple strings to avoid escape issues. 
    # Python regex '.' does not match newline, so (.*) gets the rest of the line.
    patterns = [
        r"Begin Construction[:\s]+(.*)",
        r"Start Date[:\s]+(.*)",
        r"Construction began[:\s]+(.*)",
        r"Construction Start[:\s]+(.*)",
        r"Advertise[:\s]+(.*)",
        r"Construction was completed[:\s]+(.*)" 
    ]
    
    for pat in patterns:
        # Search in the whole block
        matches = re.findall(pat, text_block, re.IGNORECASE)
        for date_str in matches:
            if "2022" in date_str:
                return True
    return False

matched_projects = set()
total_funding = 0
debug_info = []

project_lookup = []
for idx, row in funding_df.iterrows():
    full_name = row['Project_Name']
    if full_name == "Discussion":
        continue
    # Escape special regex chars in name if any (like parens are already handled by removal, but generally safe)
    clean_name = re.sub(r'\s*\(.*?\)', '', full_name).strip()
    project_lookup.append({
        'full_name': full_name,
        'clean_name': clean_name,
        'amount': row['Amount']
    })

counted_projects = set()

for doc in civic_docs:
    text = doc['text']
    
    for proj in project_lookup:
        full_name = proj['full_name']
        if full_name in counted_projects:
            continue
            
        clean_name = proj['clean_name']
        
        # Simple string find
        if clean_name in text:
            start_idx = text.find(clean_name)
            # Take a chunk
            chunk = text[start_idx:start_idx+3000]
            
            if is_disaster_project(full_name, chunk):
                if started_in_2022(chunk):
                    total_funding += proj['amount']
                    counted_projects.add(full_name)
                    debug_info.append(f"Matched: {full_name}, Amount: {proj['amount']}")

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": list(counted_projects), "debug": debug_info}))"""

env_args = {'var_function-call-17465459041874363350': 'file_storage/function-call-17465459041874363350.json', 'var_function-call-17465459041874365577': 'file_storage/function-call-17465459041874365577.json'}

exec(code, env_args)
