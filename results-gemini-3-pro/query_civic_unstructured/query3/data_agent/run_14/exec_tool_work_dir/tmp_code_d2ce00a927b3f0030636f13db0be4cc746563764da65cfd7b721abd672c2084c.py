code = """import json
import re
import pandas as pd

civic_docs_path = locals()['var_function-call-774567713491960706']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

funding_path = locals()['var_function-call-774567713491960115']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

def parse_civic_doc(text):
    # Cleaning
    text = re.sub(r'Page \d+ of \d+.*Agenda Item # \d+\.[A-Z]\.', '', text)
    text = re.sub(r'\n+', '\n', text)
    
    sections_map = {
        "Capital Improvement Projects (Design)": "Design",
        "Capital Improvement Projects (Construction)": "Construction",
        "Capital Improvement Projects (Not Started)": "Not Started",
        "Capital Improvement Projects (Completed)": "Completed",
        "Disaster Recovery Projects": "Disaster"
    }
    
    # Locate sections
    found_sections = []
    for header, status in sections_map.items():
        # Escape parens for regex
        pattern = re.escape(header)
        for match in re.finditer(pattern, text, re.IGNORECASE):
            found_sections.append({'status': status, 'start': match.start(), 'header': match.group()})
    
    found_sections.sort(key=lambda x: x['start'])
    
    parsed_projects = []
    
    for i in range(len(found_sections)):
        section = found_sections[i]
        start_idx = section['start'] + len(section['header'])
        end_idx = found_sections[i+1]['start'] if i+1 < len(found_sections) else len(text)
        
        section_text = text[start_idx:end_idx]
        
        # Parse projects. Look for Title followed by (cid:190)
        # Regex: Newline, Title Group, Newline, (cid:190)
        # Note: sometimes title might be multiple lines? Assuming single line for now.
        project_matches = list(re.finditer(r'\n([^\n]+)\n+\(cid:190\)', section_text))
        
        for j in range(len(project_matches)):
            p_start = project_matches[j].start(1)
            p_end = project_matches[j+1].start(0) if j+1 < len(project_matches) else len(section_text)
            
            p_title = project_matches[j].group(1).strip()
            p_content = section_text[project_matches[j].end():p_end]
            
            parsed_projects.append({
                'Project_Name': p_title,
                'Status': section['status'],
                'Content': p_content
            })
            
    return parsed_projects

all_projects = []
for doc in civic_docs:
    all_projects.extend(parse_civic_doc(doc['text']))

df_projects = pd.DataFrame(all_projects)
df_funding = pd.DataFrame(funding_data)

# Print a preview
print("__RESULT__:")
print(json.dumps({
    "parsed_count": len(df_projects),
    "sample_projects": df_projects.head(5).to_dict(orient='records') if not df_projects.empty else [],
    "funding_count": len(df_funding)
}))"""

env_args = {'var_function-call-774567713491960115': 'file_storage/function-call-774567713491960115.json', 'var_function-call-774567713491960706': 'file_storage/function-call-774567713491960706.json'}

exec(code, env_args)
