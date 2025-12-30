code = """import json
import re

civic_docs_path = locals()['var_function-call-9021704853761821384']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

extracted = []

for doc in civic_docs:
    text = doc['text']
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
            
        # Check project start
        is_p = False
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
            block = []
            k = i + 1
            while k < len(lines):
                nav = lines[k].strip()
                if 'Capital Improvement Projects' in nav and ('(Design)' in nav or '(Construction)' in nav):
                    break
                
                m = k + 1
                nxt = False
                while m < len(lines):
                    pk = lines[m].strip()
                    if pk:
                        if '(cid:190)' in pk and not '(cid:190)' in nav:
                            nxt = True
                        break
                    m += 1
                if nxt:
                    break
                block.append(lines[k])
                k += 1
            
            blk_txt = ' '.join(block)
            
            s_date = None
            # look for Begin Construction
            match = re.search(r'Begin [Cc]onstruction[:\s]+(.*?)(?:$)', blk_txt) # simplified regex, no newline
            if not match:
                # The join used space, so newline is gone. 
                # Wait, "Begin Construction: Fall 2023" might be followed by other text if I join with space.
                # Original lines had newlines.
                # Let's join with newline char
                pass
            
            # Let's use the list of lines for searching
            for b_line in block:
                if 'Begin Construction' in b_line or 'Start Date' in b_line:
                    # extract value
                    parts = b_line.split(':')
                    if len(parts) > 1:
                        s_date = parts[1].strip()
                    break
            
            is_d = False
            kws = ['FEMA', 'CalOES', 'Woolsey', 'Disaster', 'Emergency']
            if any(kw in blk_txt for kw in kws) or any(kw in p_name for kw in kws):
                is_d = True
            
            extracted.append({'name': p_name, 'start': s_date, 'disaster': is_d})
            i = k
        else:
            i += 1

print('__RESULT__:')
print(json.dumps(extracted))"""

env_args = {'var_function-call-4835809069730370506': ['Funding'], 'var_function-call-4835809069730370969': ['civic_docs'], 'var_function-call-17294341897624108968': 'file_storage/function-call-17294341897624108968.json', 'var_function-call-17294341897624106339': 'file_storage/function-call-17294341897624106339.json', 'var_function-call-9021704853761821384': 'file_storage/function-call-9021704853761821384.json'}

exec(code, env_args)
