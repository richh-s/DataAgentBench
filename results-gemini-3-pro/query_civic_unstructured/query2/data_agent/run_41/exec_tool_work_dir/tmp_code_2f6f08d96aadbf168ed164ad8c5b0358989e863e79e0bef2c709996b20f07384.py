code = """import json
import re

# Load civic docs
with open(locals()['var_function-call-4654103334756958724'], 'r') as f:
    civic_docs = json.load(f)

# Load funding data
with open(locals()['var_function-call-4654103334756962095'], 'r') as f:
    funding_data = json.load(f)

projects = []
# Iterate over docs
for doc in civic_docs:
    text = doc['text']
    # Split text into lines to avoid complex regex issues
    lines = text.split('\n')
    
    # Iterate and look for the pattern
    # Current project name candidate
    # We look for a line with "(cid:190) Updates" or "(cid:190) Project Description"
    # The project name should be the non-empty line above it.
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if line.startswith('(cid:190) Updates') or line.startswith('(cid:190) Project Description'):
            # Look backwards for name
            j = i - 1
            while j >= 0 and not lines[j].strip():
                j -= 1
            if j >= 0:
                p_name = lines[j].strip()
                
                # Extract the text block for this project
                # From line i to the next project start or end of text
                # We can't easily find the next start without iterating ahead.
                # Let's collect lines until we see another potential name-header pattern?
                # Or just grab the next 20 lines? The sections are short.
                # Better: scan forward until next "(cid:190)" or end.
                
                block_lines = []
                k = i
                while k < len(lines):
                    # If we see a new "(cid:190) Updates", stop?
                    # But the current block starts at i.
                    # We continue. If we find another "(cid:190) Updates" later, that belongs to next project.
                    # But the next project's name is before that.
                    # So if we hit a line that is a Name for the next project, we should stop.
                    # This is hard to detect.
                    # Heuristic: Stop if we see "(cid:190)" again?
                    # The text has "(cid:190) Updates", "(cid:190) Project Schedule".
                    # So we can't stop at any "(cid:190)".
                    # We should stop when we see a line that is followed by "(cid:190) Updates" later?
                    # Let's just take the text until the next "(cid:190) Updates" and trim the end?
                    
                    if k > i and (lines[k].strip().startswith('(cid:190) Updates') or lines[k].strip().startswith('(cid:190) Project Description')):
                        break
                    block_lines.append(lines[k])
                    k += 1
                
                p_text = "\n".join(block_lines)
                
                # Check for completion in 2022
                is_completed_2022 = False
                if "Construction was completed" in p_text and "2022" in p_text:
                    # Verify they are in the same sentence or close proximity
                    # Simple check: extract the sentence
                    sentences = p_text.split('.')
                    for s in sentences:
                        if "Construction was completed" in s and "2022" in s:
                            is_completed_2022 = True
                            break
                            
                projects.append({'name': p_name, 'text': p_text, 'completed_2022': is_completed_2022})

# Filter and Sum
total_funding = 0
matched_projects = []
park_keywords = ['park', 'playground', 'recreation']

for p in projects:
    if p['completed_2022']:
        name = p['name']
        # Check topic
        if any(k in name.lower() for k in park_keywords):
            # Find funding
            amount = 0
            for fund in funding_data:
                if fund['Project_Name'].strip().lower() == name.strip().lower():
                    amount = fund['Amount']
                    break
            
            if amount > 0:
                total_funding += amount
                matched_projects.append({'name': name, 'amount': amount})

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": matched_projects}))"""

env_args = {'var_function-call-4654103334756958724': 'file_storage/function-call-4654103334756958724.json', 'var_function-call-4654103334756962095': 'file_storage/function-call-4654103334756962095.json'}

exec(code, env_args)
