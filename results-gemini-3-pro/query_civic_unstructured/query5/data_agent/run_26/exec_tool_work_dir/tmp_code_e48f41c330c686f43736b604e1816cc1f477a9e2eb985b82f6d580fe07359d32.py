code = """import json
import re

# Load civic docs
with open(locals()['var_function-call-5605292304546820245'], 'r') as f:
    docs = json.load(f)

text = docs[0]['text']

# Load funding data
with open(locals()['var_function-call-3657045741871633664'], 'r') as f:
    funding_data = json.load(f)

funding_map = {item['Project_Name']: item['Amount'] for item in funding_data}

# Split text by the bullet point code to find sections
# The text has (cid:190) which is a bullet.
# Splitting by "(cid:190) Updates:" seems reliable based on preview.
# We'll use string split which is safer than regex for now.

# Normalize text newlines
text = text.replace('\r\n', '\n')

blocks = text.split('(cid:190) Updates:')

projects = []

# The first block is header junk. The last part of a block is the project name for the NEXT block.
# Wait, "Project Name\n\n(cid:190) Updates:"
# So if I split by "(cid:190) Updates:", the END of block i is the Project Name for block i+1.

for i in range(1, len(blocks)):
    current_block = blocks[i] # This contains the updates, schedule etc for the project
    prev_block = blocks[i-1] # The end of this contains the project name
    
    # Extract Project Name from prev_block
    # It should be the last non-empty line(s)
    lines = prev_block.strip().split('\n')
    name = lines[-1].strip()
    
    # Sometimes header info might be there.
    # If name is "Capital Improvement Projects (Design)", then the previous line was the name?
    # No, the structure is: Header -> Project Name -> Updates.
    # If prev_block ends with "Capital Improvement Projects (Design)", then current_block is associated with that? No.
    # The header is usually separated.
    # Let's clean the name.
    
    # Extract info from current_block
    # Search for "Begin Construction: <date>" or "Advertise: <date>"
    
    start_date = ""
    # Simple substring search for start date keywords
    for line in current_block.split('\n'):
        line = line.strip()
        if "Begin Construction:" in line or "Begin construction:" in line:
            start_date = line.split(':', 1)[1].strip()
            break
        if "Advertise:" in line and not start_date:
            start_date = line.split(':', 1)[1].strip()
    
    # Check 2022
    started_2022 = False
    if "2022" in start_date:
        started_2022 = True
    elif "Construction was completed" in current_block and "2022" in current_block:
         # Check if completed in 2022
         if "completed, November 2022" in current_block or "completed November 2022" in current_block:
             started_2022 = True # Assume started in 2022 or late 2021, count it? 
             # Prompt: "started in 2022".
             # Completed in Nov 2022 could start in 2021.
             # But "Broad Beach Road Water Quality Repair" -> completed Nov 2022.
             # "Bluffs Park Shade Structure" -> completed Nov 2022.
             # If I don't have start date, I might miss these.
             # Let's check if the name suggests 2022? "2022 Morning View..."
             pass
    
    # Check for specific "started in 2022" signals
    # "2022 Morning View Resurfacing" -> Name has 2022.
    if "2022" in name:
        started_2022 = True
    
    # Determine Type
    is_disaster = False
    if "(FEMA" in name or "(CalOES" in name or "CalJPIA" in name:
        is_disaster = True
    
    # Also check context for section header
    # We need to see if "Disaster Recovery Projects" was the last header before this name.
    # We can check the whole prev_block for the header.
    # Be careful: prev_block might contain the previous project's data.
    # We need to find the *latest* header in the text up to this point.
    
    # Let's do a global header search
    # Find position of name in full text?
    # Or just scan prev_block. If it has a header, update current_section.
    # But headers are sparse.
    pass

# Refined approach:
# 1. Regex to find all headers and their positions.
# 2. Regex to find all projects and their positions.
# 3. Correlate.

header_pattern = re.compile(r'(Capital Improvement Projects|Disaster Recovery Projects)')
header_matches = list(header_pattern.finditer(text))

project_pattern = re.compile(r'([^\n]+)\n\n\(cid:190\) Updates:')
project_matches = list(project_pattern.finditer(text))

found_list = []

for pm in project_matches:
    p_name = pm.group(1).strip()
    p_start = pm.start()
    p_block_start = pm.end()
    
    # Find next project start to define block end
    p_block_end = len(text)
    for other in project_matches:
        if other.start() > p_start:
            p_block_end = other.start()
            break
            
    p_block = text[p_block_start:p_block_end]
    
    # Determine section
    section = "capital" # default
    last_header_pos = -1
    for hm in header_matches:
        if hm.start() < p_start:
            if hm.start() > last_header_pos:
                last_header_pos = hm.start()
                section = hm.group(1)
    
    # Type check
    dtype = "capital"
    if "Disaster" in section:
        dtype = "disaster"
    if "(FEMA" in p_name or "CalOES" in p_name or "CalJPIA" in p_name:
        dtype = "disaster"
        
    # Start date check
    started_2022 = False
    
    # Check 2022 in name
    if "2022" in p_name:
        started_2022 = True
    
    # Check Schedule
    if "Begin Construction: Fall 2022" in p_block or \
       "Begin Construction: Summer 2022" in p_block or \
       "Begin Construction: Spring 2022" in p_block or \
       "Begin Construction: Winter 2022" in p_block or \
       "Begin construction: Fall 2022" in p_block or \
       "Begin construction: Summer 2022" in p_block or \
       "Begin construction: Spring 2022" in p_block or \
       "Begin construction: Winter 2022" in p_block:
        started_2022 = True
        
    if "Advertise: Fall 2022" in p_block or \
       "Advertise: Summer 2022" in p_block or \
       "Advertise: Spring 2022" in p_block or \
       "Advertise: Winter 2022" in p_block:
        started_2022 = True
        
    # Check numeric months
    if re.search(r'Begin [cC]onstruction:.*2022', p_block):
        started_2022 = True
        
    # Check completed
    if "Construction was completed" in p_block and "2022" in p_block:
         # Heuristic: if completed in 2022, check funding.
         # Actually, better to check if it's listed in funding with a name matching.
         # Let's assume yes for now if we can't find a start date.
         if not re.search(r'Begin [cC]onstruction:.*202[3-9]', p_block):
             started_2022 = True
             
    if dtype == "disaster" and started_2022:
        found_list.append(p_name)

# Sum funding
total = 0
matches_data = []
for name in found_list:
    amt = 0
    # Try exact match
    if name in funding_map:
        amt = funding_map[name]
    else:
        # Try case insensitive
        for k, v in funding_map.items():
            if k.lower().strip() == name.lower().strip():
                amt = v
                break
    
    if amt:
        total += int(amt)
        matches_data.append({"name": name, "amount": amt})

print("__RESULT__:")
print(json.dumps({"matches": matches_data, "total": total}))"""

env_args = {'var_function-call-5605292304546820245': 'file_storage/function-call-5605292304546820245.json', 'var_function-call-3657045741871633664': 'file_storage/function-call-3657045741871633664.json'}

exec(code, env_args)
