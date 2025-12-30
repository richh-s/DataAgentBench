code = """import json
import pandas as pd

funding_path = locals()['var_function-call-9960923256029121607']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

docs_path = locals()['var_function-call-9960923256029120432']
with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

projects = []
newline = chr(10)

for doc in civic_docs:
    text = doc['text']
    lines = text.split(newline)
    current_status = None
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check Section
        if 'Capital Improvement Projects' in line:
            if '(Design)' in line:
                current_status = 'design'
            elif '(Construction)' in line:
                current_status = 'construction_section'
            elif '(Not Started)' in line:
                current_status = 'not started'
            i += 1
            continue
        
        if not line:
            i += 1
            continue

        # Check if this line is a project name
        # Look ahead for "Updates:" or "Project Description:"
        # Allow skipping up to 2 empty lines
        is_project = False
        k = i + 1
        skipped_count = 0
        while k < len(lines) and skipped_count < 3:
            chk = lines[k].strip()
            if not chk:
                skipped_count += 1
                k += 1
                continue
            
            # Check marker
            if ('Updates:' in chk or 'Project Description:' in chk) and len(chk) < 100:
                is_project = True
            break # Stop after checking the first non-empty line
        
        if is_project:
            project_name = line
            block_lines = [line]
            
            # Consume lines until next project or section
            # We start from i + 1 (the lines we peeked at are part of the block)
            j = i + 1
            while j < len(lines):
                l = lines[j].strip()
                
                # Check for section header
                if 'Capital Improvement Projects' in l:
                    break
                
                # Check for next project
                # Use same logic: is l a name?
                # But we can't look ahead easily inside this loop if we are consuming line by line.
                # Actually, we can.
                if l: # Potential name
                    # Look ahead from j
                    is_next = False
                    m = j + 1
                    sc = 0
                    while m < len(lines) and sc < 3:
                        c = lines[m].strip()
                        if not c:
                            sc += 1
                            m += 1
                            continue
                        if ('Updates:' in c or 'Project Description:' in c) and len(c) < 100:
                            is_next = True
                        break
                    
                    if is_next:
                        # j is the start of next project, so we stop here
                        break
                
                block_lines.append(lines[j]) # Append original line (with indent etc? or stripped? logic uses stripped for check, let's append original or stripped. stripped is safer for text search)
                j += 1
            
            full_text = newline.join([bl.strip() for bl in block_lines])
            
            p_status = current_status
            if p_status == 'construction_section':
                # Check completion
                # "Construction was completed"
                if 'construction was completed' in full_text.lower():
                    p_status = 'completed'
                else:
                    p_status = 'construction'
            
            projects.append({
                'Project_Name': project_name,
                'text': full_text,
                'status': p_status
            })
            
            i = j # Continue from where we left off
            continue
        
        i += 1

related_projects = []
seen_names = set()

for p in projects:
    if p['Project_Name'] in seen_names:
        continue
    text_lower = p['text'].lower()
    name_lower = p['Project_Name'].lower()
    if 'emergency' in text_lower or 'fema' in text_lower or 'emergency' in name_lower or 'fema' in name_lower:
        related_projects.append(p)
        seen_names.add(p['Project_Name'])

related_df = pd.DataFrame(related_projects)

if not related_df.empty:
    related_df['Project_Name'] = related_df['Project_Name'].str.strip()
    
    # Debug: Check if Latigo is there now
    # print([n for n in related_df['Project_Name'] if 'Latigo' in n])
    
    merged_df = pd.merge(related_df, funding_df, on='Project_Name', how='left')
    result = merged_df[['Project_Name', 'Funding_Source', 'Amount', 'status']]
    
    # Map 'construction' to something else? Or leave it.
    # The user asked for "statuses".
    # I'll output what I have.
    result = result.fillna('N/A')
    
    print("__RESULT__:")
    print(result.to_json(orient='records'))
else:
    print("__RESULT__:")
    print("[]")"""

env_args = {'var_function-call-7478273444201397872': ['Funding'], 'var_function-call-7478273444201397573': ['civic_docs'], 'var_function-call-9960923256029121607': 'file_storage/function-call-9960923256029121607.json', 'var_function-call-9960923256029120432': 'file_storage/function-call-9960923256029120432.json', 'var_function-call-16485460042547208209': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000', 'status': 'not started'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '50000', 'status': 'not started'}], 'var_function-call-11203928266313563770': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000', 'status': 'not started'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '50000', 'status': 'not started'}]}

exec(code, env_args)
