code = """import json
import re

with open(locals()['var_function-call-9955597028425929881'], 'r') as f:
    civic_docs = json.load(f)

projects_spring_2022 = set()

for doc in civic_docs:
    text = doc['text']
    # Corrected regex: hyphen in character class escaped as \-
    # Also, ensure no triple quotes are unescaped within this string literal.
    # The tool uses """ to wrap the code, so no ''' escaping needed for this.
    match_pattern = r'([A-Z][a-zA-Z0-9\s&,\-_]+Project(?:\\s\\(.+?)\\))?(?:.|\n)*?(?:Begin(?:s)? Construction|Advertise|st|et|Start time/date):\\s*(?:Spring|March|April|May)\\s*2022'
    
    matches = re.finditer(match_pattern, text, re.IGNORECASE)

    for match in matches:
        project_name = match.group(1).strip()
        if not re.search(r'^(Capital Improvement|Disaster Recovery) Projects(?:\\s\\(.+?)\\))?$', project_name, re.IGNORECASE):
            projects_spring_2022.add(project_name)

projects_spring_2022_list = list(projects_spring_2022)

print("__RESULT__:")
print(json.dumps(projects_spring_2022_list))"""

env_args = {'var_function-call-9955597028425929881': 'file_storage/function-call-9955597028425929881.json'}

exec(code, env_args)
