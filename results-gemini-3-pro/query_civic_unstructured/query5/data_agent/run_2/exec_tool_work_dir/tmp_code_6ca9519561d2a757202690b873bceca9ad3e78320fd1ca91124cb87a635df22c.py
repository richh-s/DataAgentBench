code = """import json
import re

# Load the data
civic_docs_path = locals()['var_function-call-9021704853761821384']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

funding_path = locals()['var_function-call-17294341897624108968']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Helper to normalize strings for matching
def normalize(s):
    return s.strip().lower()

extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_projects = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        
        # Check for potential project name
        # A project name is usually followed by a line starting with (cid:190) (which is a bullet point)
        # We look ahead
        is_project = False
        j = i + 1
        while j < len(lines):
            peek = lines[j].strip()
            if peek:
                if peek.startswith("(cid:190)") or peek.startswith("Updates:") or peek.startswith("Project Description:"):
                    is_project = True
                break
            j += 1
        
        if is_project:
            p_name = line
            # Extract block
            block_lines = []
            k = i + 1
            while k < len(lines):
                nav_line = lines[k].strip()
                # Stop if we hit a likely new project or section header
                # Heuristic: New project if line is followed by (cid:190) and line doesn't start with (cid:190)
                # But headers also fit this pattern.
                # Headers usually contain "Capital Improvement Projects" or "Commission" etc.
                
                if "Capital Improvement Projects" in nav_line and ("(Design)" in nav_line or "(Construction)" in nav_line or "(Not Started)" in nav_line):
                     break
                
                # Check for next project start
                # Look ahead from k
                m = k + 1
                is_next = False
                while m < len(lines):
                    peek_next = lines[m].strip()
                    if peek_next:
                        if peek_next.startswith("(cid:190)") and not nav_line.startswith("(cid:190)"):
                            # likely new project
                            is_next = True
                        break
                    m += 1
                
                if is_next:
                    break
                
                block_lines.append(lines[k])
                k += 1
            
            block_text = "\n".join(block_lines)
            
            # Extract Start Date
            start_date = None
            # Patterns: "Begin Construction: ...", "Start Date: ..."
            # Also "Construction was completed ..."
            
            date_match = re.search(r"Begin [Cc]onstruction[:\s]+(.*?)(?:\n|$)", block_text)
            if not date_match:
                 date_match = re.search(r"Start [Dd]ate[:\s]+(.*?)(?:\n|$)", block_text)
            
            if date_match:
                start_date = date_match.group(1).strip()
            
            # Determine if disaster related
            # Keywords in text
            is_disaster = False
            keywords = ["FEMA", "CalOES", "Woolsey", "Disaster", "Emergency"]
            if any(kw in block_text for kw in keywords) or any(kw in p_name for kw in keywords):
                is_disaster = True
                
            current_projects.append({
                "name": p_name,
                "start_date": start_date,
                "is_disaster": is_disaster,
                "block_preview": block_text[:200]
            })
            
            i = k
        else:
            i += 1
            
    extracted_projects.extend(current_projects)

print("__RESULT__:")
print(json.dumps(extracted_projects))"""

env_args = {'var_function-call-4835809069730370506': ['Funding'], 'var_function-call-4835809069730370969': ['civic_docs'], 'var_function-call-17294341897624108968': 'file_storage/function-call-17294341897624108968.json', 'var_function-call-17294341897624106339': 'file_storage/function-call-17294341897624106339.json', 'var_function-call-9021704853761821384': 'file_storage/function-call-9021704853761821384.json'}

exec(code, env_args)
