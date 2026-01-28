code = """import json
import re
import pandas as pd

# Load civic docs
civic_docs_path = locals()['var_function-call-774567713491960706']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Load funding data
funding_data = pd.DataFrame(locals()['var_function-call-774567713491960115'])

# Helper function to parse text
def parse_civic_doc(text):
    # Remove page footers/headers
    # Pattern: "Page \d+ of \d+\n\nAgenda Item # 4.B."
    text = re.sub(r'Page \d+ of \d+\s+Agenda Item # \d+\.[A-Z]\.', '', text)
    text = re.sub(r'\n+', '\n', text) # Normalize newlines
    
    projects = []
    
    # Split by major sections
    # Headers found in preview: "Capital Improvement Projects (Design)", "Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)"
    # Also "Disaster Recovery Projects" might exist.
    
    # Let's try to identify sections by lines that look like headers.
    # We can search for the known headers.
    
    sections = [
        ("Design", "Capital Improvement Projects (Design)"),
        ("Construction", "Capital Improvement Projects (Construction)"),
        ("Not Started", "Capital Improvement Projects (Not Started)"),
        ("Completed", "Capital Improvement Projects (Completed)"), # Guessing
        ("Disaster", "Disaster Recovery Projects")
    ]
    
    # We need to split the text.
    # Find indices of headers
    
    found_sections = []
    for status, header in sections:
        # fuzzy match or exact? The preview shows "Capital Improvement Projects (Design)"
        # Note the parens might need escaping in regex
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
        
        # Now parse projects within section text
        # Projects seem to be titles followed by "(cid:190) Updates:" or similar bullets.
        # Let's split by double newlines or identifying the title pattern.
        # A project block starts with a Title line, then fields.
        
        # Regex to find Project Title. 
        # Look for lines that are followed by "(cid:190)" or "Updates:"
        # Or simply split by project blocks.
        
        # We can split by the bullet point that starts a project update block?
        # Actually, the title is above the bullets.
        
        # Let's split by double newlines and check blocks.
        # Or look for the pattern: `\n<Title>\n(cid:190)`
        
        # In the preview:
        # "\n2022 Morning View Resurfacing & Storm Drain Improvements\n\n(cid:190) Updates:"
        
        # So we can search for `\n(?P<title>[^\n]+)\n+(cid:190)` 
        # But `(cid:190)` might be decoded differently depending on encoding.
        # In the JSON string it appears as `(cid:190)`.
        
        # Let's assume the bullet is `(cid:190)` or similar unique char.
        
        # Regex: `\n([^\n]+)\n+\(cid:190\)`
        
        project_matches = list(re.finditer(r'\n([^\n]+)\n+\(cid:190\)', section_text))
        
        for j in range(len(project_matches)):
            p_start = project_matches[j].start(1) # Start of title
            # End of this project is start of next project or end of section
            p_end = project_matches[j+1].start(0) if j+1 < len(project_matches) else len(section_text)
            
            p_title = project_matches[j].group(1).strip()
            p_content = section_text[project_matches[j].end():p_end]
            
            parsed_projects.append({
                'Project_Name': p_title,
                'status': section['status'],
                'content': p_content
            })
            
    return parsed_projects

all_parsed_projects = []
for doc in civic_docs:
    all_parsed_projects.extend(parse_civic_doc(doc['text']))

# Convert to DataFrame
df_parsed = pd.DataFrame(all_parsed_projects)

print("__RESULT__:")
print(df_parsed.head().to_json(orient='records'))
print(f"Total parsed: {len(df_parsed)}")"""

env_args = {'var_function-call-774567713491960115': 'file_storage/function-call-774567713491960115.json', 'var_function-call-774567713491960706': 'file_storage/function-call-774567713491960706.json'}

exec(code, env_args)
