code = """import json
import re

with open(locals()['var_function-call-2466750499459274811'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-3057395287432783199'], 'r') as f:
    civic_docs = json.load(f)

project_names = [r['Project_Name'] for r in funding_data]
project_names.sort(key=len, reverse=True)

# Filter for likely park projects
park_keywords = ['park', 'playground', 'recreation', 'skate']
park_projects = [p for p in project_names if any(k in p.lower() for k in park_keywords)]

completion_patterns = [
    r"construction\s+was\s+completed,?\s+([a-zA-Z]+)?\s?2022",
    r"complete\s+construction:?\s+([a-zA-Z]+)?\s?2022",
    r"construction\s+completed\s+([a-zA-Z]+)?\s?2022",
    r"completed\s+in\s+2022"
]

results = {}

for doc in civic_docs:
    text = doc['text']
    for pname in park_projects:
        pname_esc = re.escape(pname)
        # Find match
        match = re.search(pname_esc, text, re.IGNORECASE)
        if match:
            start = match.end()
            # Get next 500 chars
            context = text[start:start+500]
            # Clean newlines for display
            context_clean = context.replace('\n', ' ')
            
            # Check for completion in 2022
            is_completed_2022 = False
            for pat in completion_patterns:
                if re.search(pat, context, re.IGNORECASE):
                    is_completed_2022 = True
                    break
            
            if is_completed_2022:
                results[pname] = {"status": "Completed 2022", "context_snippet": context_clean[:200]}
            else:
                # Store it just to see what the status is (maybe completed in 2023 or design)
                if pname not in results:
                    results[pname] = {"status": "Found", "context_snippet": context_clean[:200]}

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-2466750499459274811': 'file_storage/function-call-2466750499459274811.json', 'var_function-call-2466750499459274820': 'file_storage/function-call-2466750499459274820.json', 'var_function-call-3057395287432783199': 'file_storage/function-call-3057395287432783199.json', 'var_function-call-1088644896488091841': {'total_funding': 163000, 'projects': ['Storm Drain Trash Screens Phase Two', 'Bluffs Park Shade Structure', 'PCH Signal Synchronization System Improvements Project', 'Storm Drain Trash Screens', 'Malibu Road Slope Repairs', 'Encinal Canyon Road Repairs']}}

exec(code, env_args)
