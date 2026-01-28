code = """import json
import re

# Load the civic docs
try:
    with open(locals()['var_function-call-6738799764007294516'], 'r') as f:
        civic_docs = json.load(f)

    # Load the funding data
    with open(locals()['var_function-call-6738799764007295879'], 'r') as f:
        funding_data = json.load(f)

    extracted_projects = []

    for doc in civic_docs:
        text = doc.get('text', '')
        lines = text.split('\n')
        
        current_project = None
        
        for i, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue
                
            # Check if this line is a project title
            is_title = False
            look_ahead_range = 5 
            for j in range(1, look_ahead_range + 1):
                if i + j < len(lines):
                    next_line = lines[i+j].strip()
                    # Check for keywords indicating a project block start
                    if re.search(r'^(Updates:|Project Description:|Project Updates:)', next_line) or re.search(r'^\(cid:190\)\s*(Updates|Project Description)', next_line):
                        is_title = True
                        break
            
            if is_title:
                if current_project:
                    extracted_projects.append(current_project)
                
                current_project = {
                    'name': line,
                    'text_lines': []
                }
            else:
                if current_project:
                    current_project['text_lines'].append(line)
        
        if current_project:
            extracted_projects.append(current_project)

    processed_projects = []
    for proj in extracted_projects:
        full_text = " ".join(proj['text_lines'])
        
        # Extract Start Date
        start_match = re.search(r'Begin [cC]onstruction:?\s*([A-Za-z0-9\s,]+)', full_text)
        if not start_match:
             start_match = re.search(r'Construction start:?\s*([A-Za-z0-9\s,]+)', full_text, re.IGNORECASE)
        
        start_date_str = start_match.group(1).strip() if start_match else None
        
        started_in_2022 = False
        if start_date_str and "2022" in start_date_str:
            started_in_2022 = True
        
        # Check for Disaster related
        is_disaster = False
        disaster_keywords = ["FEMA", "CalOES", "CalJPIA", "Woolsey", "Disaster", "Recovery"]
        
        if any(k.lower() in proj['name'].lower() for k in disaster_keywords):
            is_disaster = True
        
        if any(k in full_text for k in disaster_keywords):
            is_disaster = True
            
        processed_projects.append({
            'name': proj['name'],
            'start_date_raw': start_date_str,
            'started_in_2022': started_in_2022,
            'is_disaster': is_disaster
        })

    print("__RESULT__:")
    print(json.dumps(processed_projects))
except Exception as e:
    print("__RESULT__:")
    print(json.dumps({"error": str(e)}))"""

env_args = {'var_function-call-6738799764007294516': 'file_storage/function-call-6738799764007294516.json', 'var_function-call-6738799764007295879': 'file_storage/function-call-6738799764007295879.json'}

exec(code, env_args)
