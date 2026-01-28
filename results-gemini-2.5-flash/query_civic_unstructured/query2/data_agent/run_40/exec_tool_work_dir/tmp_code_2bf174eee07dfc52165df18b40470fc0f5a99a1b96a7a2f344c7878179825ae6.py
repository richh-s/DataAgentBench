code = """import json
import re

funding_data = json.load(open(locals()['var_function-call-11819915285845147095'], 'r'))
civic_docs = json.load(open(locals()['var_function-call-13092724548813218485'], 'r'))

project_info = []

# Regex patterns to extract project details
project_name_pattern = re.compile(r'\\n([A-Z][a-zA-Z0-9&\\s,-]+?)(?:\\n\\\(cid:190\\\)|$)', re.MULTILINE)
topic_pattern = re.compile(r'topic: (.*?)\\n')
status_pattern = re.compile(r'status: (.*?)\\n')
et_pattern = re.compile(r'Complete (?:Construction|Design|Project|Work):\\s*(.*?)(?:\\n|$)') # Capture end time/date

for doc in civic_docs:
    text = doc['text']
    
    # Extract project names
    # This pattern is more robust to capture project names, considering they are typically followed by (cid:190) Updates or similar.
    project_blocks = re.split(r'\\n(?=[A-Z][a-zA-Z0-9&\\s,-]+?(?:\\n\\\(cid:190\\\)|$))', text)
    
    for block in project_blocks:
        name_match = re.search(r'([A-Z][a-zA-Z0-9&\\s,-]+?)\\n', block)
        if name_match:
            project_name = name_match.group(1).strip()
            
            # Check for "park" in the name or surrounding text to approximate topic
            is_park_related = "park" in project_name.lower() or "park" in block.lower()

            # Check status
            status_match = re.search(r'Updates:(?:.*?)Construction was completed, (.*?)(?:\\n|.)', block, re.DOTALL)
            status = 'unknown'
            if status_match:
                status = 'completed'
                end_date_str = status_match.group(1).strip()
            else:
                status_keywords = ["completed", "complete construction", "notice of completion filed"]
                if any(keyword in block.lower() for keyword in status_keywords):
                    status = 'completed'
                
                # Try to get end date even if not explicitly "Construction was completed"
                end_date_match = re.search(r'Complete (?:Construction|Design|Project|Work|Completion):\\s*(.*?)(?:\\n|$)', block)
                if end_date_match:
                    end_date_str = end_date_match.group(1).strip()
                else:
                    end_date_str = ''


            if is_park_related and status == 'completed' and '2022' in end_date_str:
                project_info.append({
                    'Project_Name': project_name,
                    'End_Date': end_date_str # Store the raw end date string for verification
                })


# Filter funding data for relevant projects
park_projects_2022 = {proj['Project_Name'] for proj in project_info}
total_funding = 0

for item in funding_data:
    if item['Project_Name'] in park_projects_2022:
        try:
            total_funding += int(item['Amount'])
        except ValueError:
            # Handle cases where 'Amount' might not be a valid integer
            pass

print("__RESULT__:")
print(json.dumps(total_funding))"""

env_args = {'var_function-call-11819915285845147095': 'file_storage/function-call-11819915285845147095.json', 'var_function-call-13092724548813218485': 'file_storage/function-call-13092724548813218485.json'}

exec(code, env_args)
