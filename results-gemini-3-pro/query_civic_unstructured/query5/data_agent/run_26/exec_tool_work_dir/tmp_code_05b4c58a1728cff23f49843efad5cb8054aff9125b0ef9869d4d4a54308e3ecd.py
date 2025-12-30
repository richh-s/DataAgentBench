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
funding_names = set(funding_map.keys())

# Regex to find projects: look for lines ending with "Updates:" preceded by a potential title
# The text has special characters like (cid:190) which is a bullet point.
# Pattern: "Name\n\n(cid:190) Updates:"
# Note: In the text preview, it was "(cid:190) Updates:".
# We'll use a regex that captures the line before "\n\n(cid:190) Updates:"

pattern = re.compile(r'([^\n]+)\n\n\(cid:190\) Updates:')
matches = list(pattern.finditer(text))

projects_found = []

def is_disaster(name, header_text):
    # Check name suffixes
    if "(FEMA" in name or "(CalOES" in name or "(CalJPIA" in name:
        return True
    # Check section header
    if "Disaster Recovery Projects" in header_text:
        return True
    return False

for i in range(len(matches)):
    match = matches[i]
    name = match.group(1).strip()
    start_pos = match.start()
    
    # End position is start of next match or end of text
    end_pos = matches[i+1].start() if i < len(matches) - 1 else len(text)
    
    block = text[start_pos:end_pos]
    
    # Find section header by looking backwards from start_pos
    preceding = text[:start_pos]
    # We look for the last occurrence of "Projects" followed by newline or parenthesis
    # Simplification: check if "Disaster Recovery Projects" appears after the last "Capital Improvement Projects"
    
    last_cap = preceding.rfind("Capital Improvement Projects")
    last_dis = preceding.rfind("Disaster Recovery Projects")
    
    section = "capital"
    if last_dis > last_cap:
        section = "disaster"
    
    # Determine type
    dtype = "disaster" if is_disaster(name, section) else "capital"
    
    # Determine start date
    # Look for "Begin Construction: <date>" or "Advertise: <date>"
    # We need to capture the value
    
    st_match = re.search(r'Begin [cC]onstruction:\s*([^\n]+)', block)
    st_date = st_match.group(1).strip() if st_match else ""
    
    # Check if started in 2022
    started_2022 = False
    if "2022" in st_date:
        started_2022 = True
    elif not st_date:
        # Check Advertise date
        adv_match = re.search(r'Advertise:\s*([^\n]+)', block)
        adv_date = adv_match.group(1).strip() if adv_match else ""
        if "2022" in adv_date:
            started_2022 = True
        else:
             # Check for "Construction was completed... 2022" -> Start likely 2022?
             # Or "awarded the contract ... 2022"
             if re.search(r'awarded the contract.*2022', block, re.IGNORECASE):
                 started_2022 = True
             elif re.search(r'Construction was completed.*2022', block, re.IGNORECASE):
                 # Assuming small projects started same year
                 started_2022 = True
             elif re.search(r'Updates:.*2022', block, re.IGNORECASE) and "under construction" in block.lower():
                 # If under construction and updates in 2022, maybe started 2022.
                 # But could have started 2021.
                 # Let's verify specific dates in block if possible.
                 pass

    if dtype == "disaster" and started_2022:
        projects_found.append(name)

# Calculate total funding
total_funding = 0
found_projects_data = []

for name in projects_found:
    # Try exact match first
    amount = 0
    if name in funding_map:
        amount = funding_map[name]
    else:
        # Try finding close match?
        # The prompt says: "The Project_Name ... matches the project names ... in the civic documents"
        # So exact match should ideally work.
        # But maybe there are slight differences (whitespace, casing).
        # Let's try to match case-insensitive or strip.
        found = False
        for fname in funding_names:
            if fname.strip().lower() == name.strip().lower():
                amount = funding_map[fname]
                found = True
                break
        if not found:
             # Maybe the name in text has extra spaces
             pass
    
    if amount:
        try:
            val = int(amount)
            total_funding += val
            found_projects_data.append({"name": name, "amount": val})
        except:
            pass

result = {
    "projects": found_projects_data,
    "total_funding": total_funding
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-5605292304546820245': 'file_storage/function-call-5605292304546820245.json', 'var_function-call-3657045741871633664': 'file_storage/function-call-3657045741871633664.json'}

exec(code, env_args)
