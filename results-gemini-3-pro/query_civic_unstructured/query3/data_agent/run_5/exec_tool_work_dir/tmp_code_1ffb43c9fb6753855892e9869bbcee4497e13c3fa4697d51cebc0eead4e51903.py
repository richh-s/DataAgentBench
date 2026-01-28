code = """import json
import re

# Load data
with open('var_function-call-3666629617059837292.json', 'r') as f:
    funding_data = json.load(f)

with open('var_function-call-5922907063922145685.json', 'r') as f:
    civic_docs = json.load(f)

funding_map = {}
for item in funding_data:
    funding_map[item['Project_Name']] = {
        'Funding_Source': item['Funding_Source'],
        'Amount': item['Amount']
    }

all_project_names = list(funding_map.keys())
all_project_names.sort(key=len, reverse=True)

results = []
keywords = ['emergency', 'fema', 'disaster', 'fire', 'warning']

for doc in civic_docs:
    text = doc['text']
    # Split lines
    lines = text.split('\n')
    
    clean_lines = [l.strip() for l in lines if l.strip()]
    
    headers = [
        "Capital Improvement Projects (Design)",
        "Capital Improvement Projects (Construction)",
        "Capital Improvement Projects (Not Started)",
        "Disaster Recovery Projects"
    ]
    
    current_status = "unknown"
    
    i = 0
    while i < len(clean_lines):
        line = clean_lines[i]
        
        # Check header
        is_header = False
        for h in headers:
            if h.lower() in line.lower():
                if "design" in h.lower():
                    current_status = "design"
                elif "construction" in h.lower():
                    current_status = "construction"
                elif "not started" in h.lower():
                    current_status = "not started"
                is_header = True
                break
        
        if is_header:
            i += 1
            continue
            
        # Check project
        matched_proj = None
        # Simple match: line starts with project name or equals it (ignoring punctuation)
        # We need to escape regex pattern string properly: r'[^\\w\\s]'
        line_clean = re.sub(r'[^\\w\\s]', '', line).strip()
        
        for proj in all_project_names:
            proj_clean = re.sub(r'[^\\w\\s]', '', proj).strip()
            if proj_clean and line_clean and (proj_clean == line_clean or line_clean.startswith(proj_clean)):
                 matched_proj = proj
                 break
        
        if matched_proj:
            # Capture text
            project_text_lines = []
            j = i + 1
            while j < len(clean_lines):
                next_line = clean_lines[j]
                
                # Check next header
                is_next_header = False
                for h in headers:
                    if h.lower() in next_line.lower():
                        is_next_header = True
                        break
                if is_next_header:
                    break
                
                # Check next project
                is_next_proj = False
                nl_clean = re.sub(r'[^\\w\\s]', '', next_line).strip()
                for proj in all_project_names:
                    p_clean = re.sub(r'[^\\w\\s]', '', proj).strip()
                    if p_clean and nl_clean and (p_clean == nl_clean or nl_clean.startswith(p_clean)):
                        is_next_proj = True
                        break
                if is_next_proj:
                    break
                
                project_text_lines.append(next_line)
                j += 1
            
            full_proj_text = " ".join(project_text_lines)
            
            # Refine status
            final_status = current_status
            if final_status == "construction":
                if "completed" in full_proj_text.lower() or "notice of completion" in full_proj_text.lower():
                    final_status = "completed"
            
            # Check relevance
            is_relevant = False
            for kw in keywords:
                if kw.lower() in matched_proj.lower() or kw.lower() in full_proj_text.lower():
                    is_relevant = True
                    break
            
            if is_relevant:
                f_info = funding_map.get(matched_proj, {})
                results.append({
                    "Project_Name": matched_proj,
                    "Funding_Source": f_info.get('Funding_Source'),
                    "Amount": f_info.get('Amount'),
                    "Status": final_status
                })
            
            i = j
        else:
            i += 1

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-8927615700191605796': ['Funding'], 'var_function-call-8927615700191608741': ['civic_docs'], 'var_function-call-3666629617059836093': 'file_storage/function-call-3666629617059836093.json', 'var_function-call-3666629617059837292': 'file_storage/function-call-3666629617059837292.json', 'var_function-call-5922907063922145685': 'file_storage/function-call-5922907063922145685.json'}

exec(code, env_args)
