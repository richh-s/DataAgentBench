code = """import re
import json

file_path = locals()['var_function-call-9118460724126248135']

with open(file_path, 'r') as f:
    data = json.load(f)

disaster_projects_2022 = set()

for doc in data:
    text = doc['text']

    # Normalize text: replace special characters that interfere with regex and improve readability
    text = text.replace('(cid:190)', '-- ').replace('(cid:131)', '- ')

    # This pattern attempts to capture project name and its subsequent details
    # It looks for a line starting with a capital letter, followed by common project-related words,
    # then captures all lines until it encounters another potential project name or a section header.
    project_pattern = re.compile(
        r'([A-Z][A-Za-z0-9\s&,-_./\\(\\)]+?(?:Project|Improvements|Plan|Study|Repairs|Facility|Park|Lane|System|Signals|Structure|Greens|Quality))\n'  # Project Name (escaped parentheses)
        r'(.*?)'  # Non-greedy capture of all details
        r'(?=\n[A-Z][A-Za-z0-9\s&,-_./\\(\\)]+?(?:Project|Improvements|Plan|Study|Repairs|Facility|Park|Lane|System|Signals|Structure|Greens|Quality)|Capital Improvement Projects|Disaster Recovery Projects|\Z)' # Lookahead for next project, section header, or end of text
        , re.DOTALL
    )

    # Also, identify the current project category (Capital or Disaster) based on section headers
    # This is a bit tricky with re.split, so we'll iterate through matches and check context
    
    # Split the text into segments based on Capital/Disaster headers to establish context
    segments = re.split(r'(Capital Improvement Projects(?: \\(Design\\)| \\(Construction\\)| \\(Not Started\\))?|Disaster Recovery Projects)', text, flags=re.IGNORECASE)
    
    current_context = ""
    for i in range(len(segments)):
        segment_text = segments[i]
        if "disaster recovery projects" in segment_text.lower():
            current_context = "disaster"
        elif "capital improvement projects" in segment_text.lower():
            current_context = "capital"
            
        # Now apply the project pattern within this segment and the next if available
        # This helps ensure projects are associated with the correct category
        content_to_parse = segment_text
        if i + 1 < len(segments): # Include the content after the header itself
            content_to_parse += segments[i+1]

        if current_context == "disaster":
            for match in project_pattern.finditer(content_to_parse):
                project_name = match.group(1).strip()
                details = match.group(2)

                # Check for 2022 in the schedule details
                if re.search(r'(?:Begin Construction|Advertise|Final Design|Complete Design|Project Schedule|Estimated Schedule):.*?2022', details, re.IGNORECASE):
                    disaster_projects_2022.add(project_name)

print('__RESULT__:')
print(json.dumps(list(disaster_projects_2022)))"""

env_args = {'var_function-call-9118460724126248135': 'file_storage/function-call-9118460724126248135.json'}

exec(code, env_args)
