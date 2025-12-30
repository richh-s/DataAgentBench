code = """import json
import pandas as pd

try:
    with open(locals()['var_function-call-7295023987179093116'], 'r') as f:
        funding_data = json.load(f)

    with open(locals()['var_function-call-10283202643711845823'], 'r') as f:
        civic_docs = json.load(f)

    projects = []
    
    # Process only the document that seems to be the status report
    # The preview showed text starting with "Public Works Commission... Status Report"
    # We can process all, filtering duplicates later.
    
    for doc in civic_docs:
        text = doc.get('text', '')
        lines = text.split('\n')
        
        mode = 'scan' # scan, capture_design
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            if 'Capital Improvement Projects (Design)' in line:
                mode = 'capture_design'
                i += 1
                continue
            
            # Stop capturing if we hit another section
            if 'Capital Improvement Projects (' in line and 'Design' not in line:
                mode = 'scan'
            if 'Disaster Recovery Projects' in line:
                mode = 'scan'
            
            if mode == 'capture_design':
                # Check if valid project line
                if not line: 
                    i += 1
                    continue
                if line.startswith('Page') or line.startswith('Agenda'): 
                    i += 1
                    continue
                
                # Check next line for 'Updates' or marker
                is_proj = False
                for k in range(1, 5):
                    if i + k < len(lines):
                        nxt = lines[i+k].strip()
                        if 'Updates:' in nxt or 'Project Description:' in nxt:
                            is_proj = True
                            break
                        if nxt and not nxt.startswith('('): # If next line is text, maybe this line isn't a header? 
                            # But headers can be multi-line? 
                            # In preview, headers are single line.
                            pass
                
                if is_proj:
                    projects.append(line)
            
            i += 1

    # Filter funding
    funding_df = pd.DataFrame(funding_data)
    funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])
    # Amount > 50000
    funding_filtered = funding_df[funding_df['Amount'] > 50000]
    
    # Match
    # Clean project names (remove potential artifacts)
    extracted_clean = [p.strip() for p in projects]
    extracted_df = pd.DataFrame({'Project_Name': extracted_clean})
    
    # Inner join
    result_df = pd.merge(extracted_df, funding_filtered, on='Project_Name', how='inner')
    
    final_projects = result_df['Project_Name'].unique().tolist()
    
    print("__RESULT__:")
    print(json.dumps(final_projects))

except Exception as e:
    print("__RESULT__:")
    print(json.dumps({"error": str(e)}))"""

env_args = {'var_function-call-7295023987179093116': 'file_storage/function-call-7295023987179093116.json', 'var_function-call-10283202643711845823': 'file_storage/function-call-10283202643711845823.json'}

exec(code, env_args)
