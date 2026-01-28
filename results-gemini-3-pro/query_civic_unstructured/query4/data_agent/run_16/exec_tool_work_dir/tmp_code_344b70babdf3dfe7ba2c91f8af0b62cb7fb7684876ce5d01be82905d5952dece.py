code = """import json
import re

# Load the data
with open(locals()['var_function-call-11024242700101333530'], 'r') as f:
    civic_docs = json.load(f)

spring_regex = re.compile(r"(Spring 2022|March 2022|April 2022|May 2022)", re.IGNORECASE)

def extract(text):
    # Find markers: "Updates:" or "Project Description:"
    # We will search for them preceded by the bullet point or just the text
    # The text has "(cid:190)".
    # Let's just look for "Updates:" and "Project Description:"
    
    markers = []
    for m in re.finditer(r"(Updates:|Project Description:)", text):
        markers.append(m.start())
    
    if not markers:
        return []
        
    results = []
    section_headers = ["Capital Improvement Projects", "Agenda Report", "Subject:", "RECOMMENDED ACTION", "Item", "Page"]
    
    for i, start in enumerate(markers):
        # Look backwards for name
        pre = text[:start].rstrip()
        # Remove the bullet point if present (unicode or text)
        # Just take the last non-empty line
        lines = [l.strip() for l in pre.split('\n') if l.strip()]
        
        name = "Unknown"
        # The line immediately before "Updates:" is usually the bullet point line (cid:190)
        # So we want the line before that.
        # Check the last few lines
        if lines:
            # If the last line is just a bullet like "(cid:190)", take the one before
            if "(cid:190)" in lines[-1] or len(lines[-1]) < 3:
                if len(lines) > 1:
                    name = lines[-2]
            else:
                name = lines[-1]
                
        # Simple cleanup of name
        if any(h in name for h in section_headers):
             # Try going back one more line
             if len(lines) > 2:
                 name = lines[-2]
        
        # Look forward
        end = markers[i+1] if i < len(markers)-1 else len(text)
        block = text[start:end]
        
        matches = spring_regex.findall(block)
        for m in matches:
            # Get context
            # Find line with match
            idx = block.find(m)
            line_start = block.rfind('\n', 0, idx) + 1
            line_end = block.find('\n', idx)
            if line_end == -1: line_end = len(block)
            line = block[line_start:line_end].strip()
            
            results.append({"name": name, "date": m, "context": line})
            
    return results

all = []
for doc in civic_docs:
    all.extend(extract(doc['text']))

print("__RESULT__:")
print(json.dumps(all))"""

env_args = {'var_function-call-5331130674983609150': 'file_storage/function-call-5331130674983609150.json', 'var_function-call-5331130674983611055': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-11024242700101333530': 'file_storage/function-call-11024242700101333530.json', 'var_function-call-4323330023283925201': 'file_storage/function-call-4323330023283925201.json'}

exec(code, env_args)
