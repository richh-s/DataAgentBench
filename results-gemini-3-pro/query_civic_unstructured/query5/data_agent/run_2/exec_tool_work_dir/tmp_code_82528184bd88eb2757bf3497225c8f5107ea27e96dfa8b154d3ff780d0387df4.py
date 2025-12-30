code = """import json
import re

civic_path = locals()['var_function-call-9021704853761821384']
funding_path = locals()['var_function-call-17294341897624108968']

with open(civic_path, 'r') as f:
    civic = json.load(f)
with open(funding_path, 'r') as f:
    funding = json.load(f)

# Create a lookup for funding
# Project_Name -> Amount
funding_map = {}
for row in funding:
    nm = row['Project_Name'].strip()
    amt = row['Amount']
    if nm in funding_map:
        funding_map[nm] += int(amt)
    else:
        funding_map[nm] = int(amt)

extracted = []

for doc in civic:
    lines = doc['text'].splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i+=1
            continue
            
        # Detect Project Name
        # Condition: Next non-empty line starts with (cid:190) or "Updates:" or "Project Description:"
        # OR line is in funding_map (exact match)
        
        is_p = False
        if line in funding_map:
            is_p = True
        else:
            j = i + 1
            while j < len(lines):
                peek = lines[j].strip()
                if peek:
                    if '(cid:190)' in peek or peek.startswith('Updates:') or peek.startswith('Project Description:'):
                        is_p = True
                    break
                j += 1
        
        if is_p:
            p_name = line
            # Collect block
            block = []
            k = i + 1
            while k < len(lines):
                nav = lines[k].strip()
                # Stop if header
                if 'Capital Improvement Projects' in nav and ('(Design)' in nav or '(Construction)' in nav or '(Not Started)' in nav):
                    break
                # Stop if new project
                # If nav is in funding_map and not same as p_name -> new project
                if nav in funding_map and nav != p_name:
                    break
                
                # Or check lookahead marker
                m = k + 1
                is_next = False
                while m < len(lines):
                    pk = lines[m].strip()
                    if pk:
                        if '(cid:190)' in pk and not '(cid:190)' in nav:
                             is_next = True
                        break
                    m += 1
                if is_next:
                    # But wait, if nav is just a line in the block, we shouldn't stop.
                    # This heuristic is tricky.
                    # If nav is a known project name, stop.
                    # If nav looks like a project name (followed by marker), stop.
                    # The `is_next` logic checks if `nav` is followed by marker.
                    break
                
                block.append(lines[k])
                k += 1
            
            blk_txt = '\n'.join(block)
            
            # Extract Date
            # "Begin Construction: <Date>"
            # "commence during <Date>"
            # "beginning in <Date>"
            # "scheduled to begin <Date>"
            
            start_year = None
            
            # Regexes
            # We look for "2022" in the context of start keywords
            
            # Simple check: if "Begin Construction" and "2022" in same line?
            # Or "Begin Construction" ... "2022" nearby.
            
            s_date_str = ""
            date_patterns = [
                r"Begin [Cc]onstruction[:\s]+([^\n]*)",
                r"Start [Dd]ate[:\s]+([^\n]*)",
                r"commence during ([^\n]*)",
                r"beginning in ([^\n]*)",
                r"scheduled to begin ([^\n]*)"
            ]
            
            for pat in date_patterns:
                match = re.search(pat, blk_txt)
                if match:
                    s_date_str = match.group(1)
                    if '2022' in s_date_str:
                        start_year = 2022
                        break
            
            # Also check "Construction was completed" - does NOT imply start in 2022 necessarily.
            # But if text says "Construction started ... 2022", catch it.
            
            if not start_year:
                if "started" in blk_txt and "2022" in blk_txt:
                    # Check proximity
                    # e.g. "Construction started in January 2022"
                    if re.search(r"started (in|on)?\s*[\w\s]*2022", blk_txt):
                        start_year = 2022
            
            # Detect Disaster
            is_disaster = False
            d_kws = ['FEMA', 'CalOES', 'Woolsey', 'Disaster', 'Emergency']
            if any(kw in p_name for kw in d_kws) or any(kw in blk_txt for kw in d_kws):
                is_disaster = True
            
            # Also check if Funding has suffix version?
            # If p_name is "X", and "X (FEMA Project)" exists, maybe it is disaster.
            # But here we rely on text content.
            
            extracted.append({
                'name': p_name,
                'start_year': start_year,
                'is_disaster': is_disaster,
                'funding_found': p_name in funding_map
            })
            
            i = k
        else:
            i += 1

# Filter and Sum
total_funding = 0
matched_projects = []

for p in extracted:
    if p['is_disaster'] and p['start_year'] == 2022:
        # Get funding
        # Exact match
        amt = funding_map.get(p['name'], 0)
        
        # If amt is 0, maybe name mismatch?
        # Try finding name in funding keys
        if amt == 0:
             # Try to find a match
             # e.g. "Name in text" might differ slightly
             pass
        
        if amt > 0:
            total_funding += amt
            matched_projects.append(p['name'])

print('__RESULT__:')
print(json.dumps({'total_funding': total_funding, 'projects': matched_projects, 'all_extracted': extracted}))"""

env_args = {'var_function-call-4835809069730370506': ['Funding'], 'var_function-call-4835809069730370969': ['civic_docs'], 'var_function-call-17294341897624108968': 'file_storage/function-call-17294341897624108968.json', 'var_function-call-17294341897624106339': 'file_storage/function-call-17294341897624106339.json', 'var_function-call-9021704853761821384': 'file_storage/function-call-9021704853761821384.json', 'var_function-call-16225886592360458391': 'file_storage/function-call-16225886592360458391.json'}

exec(code, env_args)
