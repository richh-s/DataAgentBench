code = """import json
import re

# Load Funding Data
with open('var_function-call-17324143026383402211.json', 'r') as f:
    funding_data = json.load(f)

# Load Civic Docs
with open('var_function-call-17324143026383404966.json', 'r') as f:
    civic_docs = json.load(f)

# 1. Identify Park Projects from Funding Table
# Keywords: 'park', 'playground'
park_projects = []
for record in funding_data:
    name = record['Project_Name']
    if 'park' in name.lower() or 'playground' in name.lower():
        park_projects.append(name)

print(f"Park Projects found in Funding: {park_projects}")

# 2. Check Status and Date in Civic Docs
# We need to find these projects in the text and check for completion in 2022.
# Pattern: Project Name -> ... -> "completed" ... "2022"
# Note: Text structure is loose.
# We will look for the Project Name, then look at the text following it (up to a limit or next project).

# Let's clean the text a bit (replace the weird cid char if needed, though regex can handle it)
# We'll concatenate all texts or process them one by one. Processing one by one allows finding the 'update' context.

completed_2022_projects = set()

# Normalize text for easier searching
def normalize(text):
    return text.replace('\n', ' ').replace('  ', ' ')

for doc in civic_docs:
    text = doc['text']
    # Split text into lines to maybe help with structure? 
    # Or just search for Project Name index.
    
    # Text is often: "Project Name\n\n(cid:190) Updates:..."
    
    for proj in park_projects:
        # Simple search for Project Name
        # We need to be careful about substring matches, but Project Names are usually distinct enough.
        # Let's find all occurrences of the project name
        
        # We use re.escape to handle parentheses in project names like "(FEMA Project)"
        matches = [m.start() for m in re.finditer(re.escape(proj), text, re.IGNORECASE)]
        
        for start_idx in matches:
            # Look ahead, say 1000 chars
            context = text[start_idx:start_idx+2000]
            
            # Check for completion
            # Patterns: 
            # "Construction was completed.*2022"
            # "Complete Construction:.*2022"
            # "Status:.*Completed" ... "2022"
            
            # We want to match "completed" and "2022" in close proximity and specifically referring to construction/project.
            # AND exclude "Complete Design: 2022"
            
            # Let's look for "Construction" or "Project" completion.
            
            normalized_context = normalize(context).lower()
            
            # Case 1: "Construction was completed [Month] 2022"
            if re.search(r'construction was completed.*?2022', normalized_context):
                completed_2022_projects.add(proj)
                continue
                
            # Case 2: "Complete Construction:.*2022" (and not 2023, 2024 etc in the same phrase)
            # Example: "Complete Construction: Summer 2022"
            # Be careful of "Complete Construction: Summer 2023"
            
            # Regex to find the completion date line
            # Look for "complete construction" followed by date
            match = re.search(r'complete construction[:\s]+(\w+\s+20\d{2})', normalized_context)
            if match:
                date_str = match.group(1)
                if '2022' in date_str:
                    completed_2022_projects.add(proj)
                    continue

            # Case 3: "Notice of completion filed.*2022" implies completion in 2022 or late 2021. 
            # But the prompt specifically asks for "completed in 2022".
            # If "Notice of completion filed January 2023", usually construction was completed in late 2022.
            # In the preview: "Construction was completed November 2022. Notice of completion filed January 2023"
            # So searching for "Construction was completed ... 2022" covers this.
            
            # Case 4: Just "Status: Completed" and date. (Less likely in this specific doc format)

print(f"Projects completed in 2022: {list(completed_2022_projects)}")

# 3. Sum Funding
total_funding = 0
for record in funding_data:
    if record['Project_Name'] in completed_2022_projects:
        total_funding += int(record['Amount'])

print('__RESULT__:')
print(json.dumps(total_funding))"""

env_args = {'var_function-call-5219184128043879497': ['Funding'], 'var_function-call-5219184128043880064': ['civic_docs'], 'var_function-call-17324143026383402211': 'file_storage/function-call-17324143026383402211.json', 'var_function-call-17324143026383404966': 'file_storage/function-call-17324143026383404966.json'}

exec(code, env_args)
