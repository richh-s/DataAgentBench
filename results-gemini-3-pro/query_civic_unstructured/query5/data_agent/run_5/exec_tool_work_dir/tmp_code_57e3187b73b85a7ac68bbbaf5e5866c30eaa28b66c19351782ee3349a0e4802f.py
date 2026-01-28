code = """import json
import pandas as pd
import re

# Access storage
funding_key = 'var_function-call-5948002065454245776'
civic_key = 'var_function-call-16801435053076295994'

file_path_funding = locals()[funding_key]
file_path_civic = locals()[civic_key]

# Load Funding
df_funding = pd.read_json(file_path_funding)

# Load Civic Docs
with open(file_path_civic, 'r') as f:
    civic_docs = json.load(f)

full_text = ""
for doc in civic_docs:
    full_text += doc['text'] + "\n"

# Clean text for easier searching?
# Maybe not, structure matters.
lines = full_text.splitlines()

# 1. Identify Disaster Funding Records
# Suffixes to identifying disaster records in Funding table
disaster_suffixes = [
    '(FEMA Project)', '(CalJPIA Project)', '(CalOES Project)', 
    '(FEMA/CalOES Project)', '(FEMA)', '(CalOES)'
]

def is_disaster_funding(name):
    for suffix in disaster_suffixes:
        if suffix.lower() in name.lower():
            return True
    return False

# 2. Map Projects to Start Dates
# We need to find the Base Name of the project in the text
# Base Name = Name without the suffix
def get_base_name(name):
    base = name
    for suffix in disaster_suffixes:
        base = base.replace(suffix, '').strip()
    return base

# Extract project blocks from text
# Strategy: Find lines that are project names?
# Or search for each base name.

# Get all unique base names from funding
# We will search for each base name in the text and try to extract the start date.
project_info = {} # {base_name: start_date_string}

# We iterate over unique base names
unique_base_names = set([get_base_name(n) for n in df_funding['Project_Name'].unique()])

for base_name in unique_base_names:
    # Search for base_name in text
    # It should be on a line by itself or prominent
    # We'll use regex to find the name, then look ahead for "Begin Construction"
    # Regex: base_name followed by some lines, then "Begin Construction:"
    # We need to be careful not to jump to another project.
    
    # Simple approach: Find the index of the name, look at next 20 lines.
    try:
        # Escape base_name for regex
        pattern = re.escape(base_name)
        # Find all occurrences
        matches = [m.start() for m in re.finditer(pattern, full_text, re.IGNORECASE)]
        
        for match_idx in matches:
            # Look at text after match
            context = full_text[match_idx:match_idx+2000] # 2000 chars should cover the section
            
            # Check if this context belongs to the project (and not the next one)
            # Maybe look for "Begin Construction:"
            date_match = re.search(r'Begin Construction:\s*([^\n]*)', context, re.IGNORECASE)
            if date_match:
                date_str = date_match.group(1).strip()
                # Store it
                # Logic: If multiple occurrences, take the one that looks like a date?
                # Or just overwrite.
                project_info[base_name] = date_str
                break # Found a date, move to next project
    except Exception as e:
        continue

# 3. Sum Funding
total_funding = 0
debug_list = []

for index, row in df_funding.iterrows():
    name = row['Project_Name']
    amount = row['Amount']
    
    # Check if disaster related
    if is_disaster_funding(name):
        base_name = get_base_name(name)
        
        # Check start date
        start_date = project_info.get(base_name)
        
        if start_date:
            # Check if start_date is in 2022
            # Flexible formats: "2022-Spring", "November 2022", "Fall 2022"
            if "2022" in start_date:
                total_funding += amount
                debug_list.append({"name": name, "base": base_name, "date": start_date, "amount": amount})

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": debug_list}))"""

env_args = {'var_function-call-8962819121667412249': ['Funding'], 'var_function-call-8962819121667415660': ['civic_docs'], 'var_function-call-5948002065454245776': 'file_storage/function-call-5948002065454245776.json', 'var_function-call-8815674849536334134': 'file_storage/function-call-8815674849536334134.json', 'var_function-call-16801435053076295994': 'file_storage/function-call-16801435053076295994.json'}

exec(code, env_args)
