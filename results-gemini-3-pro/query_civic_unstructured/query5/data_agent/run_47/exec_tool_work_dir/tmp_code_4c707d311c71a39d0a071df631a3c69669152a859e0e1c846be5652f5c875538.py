code = """import pandas as pd
import json
import re

# Load Funding Data
# The previous query_db result for funding is in 'var_function-call-17465459041874363350'
with open(locals()['var_function-call-17465459041874363350'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Load Civic Docs Data
# The previous query_db result for civic_docs is in 'var_function-call-17465459041874365577'
with open(locals()['var_function-call-17465459041874365577'], 'r') as f:
    civic_docs = json.load(f)

# Helper function to classify project type
def is_disaster_project(name, text_block):
    name_lower = name.lower()
    text_lower = text_block.lower()
    keywords = ['fema', 'caloes', 'caljpia', 'disaster', 'woolsey fire', 'emergency', 'recovery']
    
    if any(k in name_lower for k in keywords):
        return True
    if any(k in text_lower for k in keywords):
        return True
    return False

# Helper function to find start date
def started_in_2022(text_block):
    # Look for "Begin Construction: <Date>"
    # Or "Start Date: <Date>"
    # Or "Construction began <Date>"
    patterns = [
        r"Begin Construction[:\s]+(.*?)(?:\n|$)",
        r"Start Date[:\s]+(.*?)(?:\n|$)",
        r"Construction began[:\s]+(.*?)(?:\n|$)",
        r"Construction Start[:\s]+(.*?)(?:\n|$)",
        r"Advertise[:\s]+(.*?)(?:\n|$)" # Advertise might be start?
    ]
    
    for pat in patterns:
        match = re.search(pat, text_block, re.IGNORECASE)
        if match:
            date_str = match.group(1)
            if "2022" in date_str:
                return True
    
    # Also check "Construction was completed ... 2022" - uncertain if started in 2022
    # But if "Updates: Construction was completed November 2022", it might have started in 2022.
    # However, to be safe, let's look for explicit starts first. 
    # If a project has "Status: Design" and "Complete Design: 2022", did it start in 2022? Probably earlier or 2022.
    
    # Let's try searching for just "2022" in dates associated with "Begin" or "Start".
    # Done above.
    
    return False

# Mapping Project Name to Text Block
# Since parsing the whole text is hard without specific delimiters, 
# I will search for each Funding Project Name in the texts.
# To avoid extracting the same project multiple times (from multiple agendas), 
# I should probably use the "latest" status or look for any confirmation of 2022 start.
# If ANY document says it started in 2022, I count it.

matched_projects = set()
total_funding = 0
debug_info = []

# Pre-process funding names to help matching
# e.g. "Clover Heights Storm Drain (FEMA Project)" -> "Clover Heights Storm Drain"
# But need to keep track of the original name for Funding lookup.
project_lookup = []
for idx, row in funding_df.iterrows():
    full_name = row['Project_Name']
    # Create a cleaner name for searching in text (remove parens)
    clean_name = re.sub(r'\s*\(.*?\)', '', full_name).strip()
    project_lookup.append({
        'full_name': full_name,
        'clean_name': clean_name,
        'amount': row['Amount']
    })

# We'll use a set to track which full_names we have already counted to avoid double counting
counted_projects = set()

for doc in civic_docs:
    text = doc['text']
    
    for proj in project_lookup:
        full_name = proj['full_name']
        if full_name in counted_projects:
            continue
            
        clean_name = proj['clean_name']
        
        # Search for clean_name in text
        # We want to match it as a header or distinct line ideally
        if clean_name in text:
            # Extract a chunk of text starting from the name
            start_idx = text.find(clean_name)
            # Take next 1000 chars or until next project name (heuristic)
            # Better: find the start of the next project? 
            # Or just take a chunk.
            chunk = text[start_idx:start_idx+2000]
            
            # Check type
            if is_disaster_project(full_name, chunk):
                # Check start date
                if started_in_2022(chunk):
                    total_funding += proj['amount']
                    counted_projects.add(full_name)
                    debug_info.append(f"Matched: {full_name}, Amount: {proj['amount']}")

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": list(counted_projects), "debug": debug_info}))"""

env_args = {'var_function-call-17465459041874363350': 'file_storage/function-call-17465459041874363350.json', 'var_function-call-17465459041874365577': 'file_storage/function-call-17465459041874365577.json'}

exec(code, env_args)
