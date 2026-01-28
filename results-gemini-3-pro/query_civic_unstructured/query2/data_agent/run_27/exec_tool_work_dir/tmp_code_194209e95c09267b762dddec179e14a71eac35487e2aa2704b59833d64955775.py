code = """import json
import re

# Load the civic docs
with open(locals()['var_function-call-8977914089601309835'], 'r') as f:
    docs = json.load(f)

projects = []

for doc in docs:
    text = doc['text']
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check if this line is a project title
        # Look ahead for a line starting with (cid:190)
        is_project = False
        project_block = []
        
        # Look ahead up to 2 lines
        if i + 1 < len(lines) and lines[i+1].startswith('(cid:190)'):
            is_project = True
        elif i + 2 < len(lines) and lines[i+2].startswith('(cid:190)'):
            # Maybe there is an extra line? Or maybe the title is 2 lines?
            # In the example: "2022 Morning View Resurfacing & Storm Drain Improvements" -> next is (cid:190) Updates:
            pass

        if is_project:
            project_name = line
            # Capture the block until the next project title or end of text
            # A next project title would also follow the rule (next line is (cid:190))
            # So we scan forward
            j = i + 1
            while j < len(lines):
                # Check if lines[j] is a start of a new project
                # i.e., lines[j+1] starts with (cid:190)
                if j + 1 < len(lines) and lines[j+1].startswith('(cid:190)'):
                    break
                project_block.append(lines[j])
                j += 1
            
            # Process the project block
            full_text = " ".join(project_block)
            
            # Check for "park" in name or text (topic extraction)
            # The user asked for "park-related projects". 
            # I should check if "park" is in the project name or explicitly in keywords if extracted?
            # The prompt says: "topic: Keywords describing what the project is about (e.g., "park"...)".
            # "The topic field contains comma-separated keywords." - extracting this from unstructured text is the goal.
            # I will assume if "park" is in the name, it's park-related.
            # Also if the description text mentions it, but name is safer. 
            # Let's search in both Project Name and text for robustness, but primary focus on Name.
            # Wait, the prompt hints say: "Common topics include: 'park'...".
            # Let's look for "park" (case insensitive) in the Project Name. 
            # Example: "Bluffs Park Shade Structure", "Trancas Canyon Park...".
            
            is_park = "park" in project_name.lower()
            
            # Check for completed in 2022
            # Look for "Construction was completed" or "Complete Construction:"
            # And the date.
            
            completion_date = None
            status = "unknown"
            
            # Regex for completion
            # Patterns: 
            # "Construction was completed,? [Month] [Year]"
            # "Complete Construction:? [Month] [Year]"
            # "Notice of completion filed [Month] [Year]" (This implies completed before)
            
            # Let's find sentences containing "completed" or "complete construction"
            
            # Example: "Construction was completed November 2022"
            match = re.search(r'(?:construction was completed|complete construction)[:,\s]+([a-zA-Z]+ \d{4})', full_text, re.IGNORECASE)
            if match:
                date_str = match.group(1)
                status = "completed"
                completion_date = date_str
            
            if is_park and status == "completed" and "2022" in completion_date:
                projects.append({
                    "Project_Name": project_name,
                    "Completion_Date": completion_date
                })
            
            i = j
        else:
            i += 1

print("__RESULT__:")
print(json.dumps(projects))"""

env_args = {'var_function-call-14070122848874409329': ['civic_docs'], 'var_function-call-2375620709415017457': ['Funding'], 'var_function-call-15365523151233485332': 'file_storage/function-call-15365523151233485332.json', 'var_function-call-8977914089601309835': 'file_storage/function-call-8977914089601309835.json'}

exec(code, env_args)
