code = """import json
import re

# Load the Mongo query result from the storage file path
with open(var_call_qAIVVBQpLbB6atIJDbCLzuG1, 'r') as f:
    docs = json.load(f)

results = []
seen = set()

for doc in docs:
    text = doc.get('text', '')
    lines = text.splitlines()
    # Normalize lines
    norm_lines = [ln.strip() for ln in lines]
    for idx, ln in enumerate(norm_lines):
        if not ln:
            continue
        if re.search(r'\b(FEMA|emergency)\b', ln, re.I):
            # search back up to 12 lines for a project title containing 'Project' or ending with 'Project'
            proj_name = None
            for j in range(max(0, idx-12), idx+1):
                candidate = norm_lines[j]
                if candidate and re.search(r'Project\b', candidate, re.I):
                    proj_name = candidate
            # if not found, look back for a capitalized line (heuristic)
            if not proj_name:
                for j in range(max(0, idx-12), idx+1):
                    candidate = norm_lines[j]
                    if candidate and len(candidate) < 120 and re.match(r'^[A-Z0-9][A-Za-z0-9\s\-\'"&,()]+$', candidate):
                        proj_name = candidate
                        break
            if not proj_name:
                # fallback: take previous non-empty line
                for j in range(max(0, idx-6), idx+1)[::-1]:
                    if norm_lines[j]:
                        proj_name = norm_lines[j]
                        break
            # clean project name
            if proj_name:
                pn = re.sub(r'\s+', ' ', proj_name).strip()
                # Remove leading numbering or bullets
                pn = re.sub(r'^[\d\)\.\-\s]+', '', pn)
                # Limit length
                pn = pn[:200]
                # Determine status: scan forward up to 12 lines for status-like phrases
                status = None
                for k in range(idx, min(len(norm_lines), idx+13)):
                    s = norm_lines[k]
                    if not s:
                        continue
                    # common status indicators
                    if re.search(r'Project is currently under construction', s, re.I):
                        status = 'under construction'
                        break
                    if re.search(r'Construction was completed|Complete Construction|completed', s, re.I):
                        status = 'completed'
                        break
                    if re.search(r'Project Schedule:|Project Schedule', s, re.I):
                        # look a few lines further for schedule info
                        for m in range(k, min(len(norm_lines), k+6)):
                            t = norm_lines[m]
                            if re.search(r'Complete Design|Final Design|preliminary design|design', t, re.I):
                                status = 'design'
                                break
                        if status:
                            break
                    if re.search(r'awaiting|await|pending|approval', s, re.I):
                        status = s
                        break
                    if re.search(r'Project is in the preliminary design phase|preliminary design', s, re.I):
                        status = 'design'
                        break
                    if re.search(r'Project Updates:|Updates:', s, re.I):
                        # take next non-empty line
                        for m in range(k+1, min(len(norm_lines), k+6)):
                            t = norm_lines[m]
                            if t:
                                status = t
                                break
                        if status:
                            break
                if not status:
                    # try to infer by searching backwards for section headers
                    for b in range(max(0, idx-30), idx)[::-1]:
                        h = norm_lines[b]
                        if re.search(r'Capital Improvement Projects \(Design\)', h, re.I):
                            status = 'design'
                            break
                        if re.search(r'Capital Improvement Projects \(Construction\)', h, re.I):
                            status = 'construction'
                            break
                        if re.search(r'Capital Improvement Projects \(Not Started\)', h, re.I):
                            status = 'not started'
                            break
                if not status:
                    status = 'unknown'

                key = (pn.lower(), status)
                if key not in seen:
                    seen.add(key)
                    results.append({
                        'Project_Name': pn,
                        'Status': status,
                        'Source_File': doc.get('filename')
                    })

# Also include some context: unique project names list
project_names = [r['Project_Name'] for r in results]
output = {'projects': results, 'project_names': project_names}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_qAIVVBQpLbB6atIJDbCLzuG1': 'file_storage/call_qAIVVBQpLbB6atIJDbCLzuG1.json'}

exec(code, env_args)
