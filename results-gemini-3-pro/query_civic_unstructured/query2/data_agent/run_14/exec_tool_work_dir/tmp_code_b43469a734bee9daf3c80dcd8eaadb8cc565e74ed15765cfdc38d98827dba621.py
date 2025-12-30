code = """import json
import re

funding_path = locals()['var_function-call-13164751492978107468']
civic_path = locals()['var_function-call-9869211362583101527']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_data = json.load(f)

all_text = ""
for d in civic_data:
    all_text += d.get('text', '') + ' '

total_funding = 0
confirmed_projects = []

for item in funding_data:
    p_name = item['Project_Name']
    amount = int(item['Amount'])
    
    # Check topic: park
    if 'park' not in p_name.lower() and 'playground' not in p_name.lower():
        continue

    base_name = p_name.split('(')[0].strip()
    
    # Find all matches
    matches = [m.start() for m in re.finditer(re.escape(base_name), all_text, re.IGNORECASE)]
    
    is_completed = False
    for start in matches:
        # Take a smaller snippet to avoid overlap if possible, or handle overlap
        # 400 chars should be enough for status
        snippet = all_text[start:start+400].lower()
        
        if '2022' in snippet:
            # Positive indicators
            if ('was completed' in snippet or 
                'construction completed' in snippet or 
                'construction was completed' in snippet or
                'notice of completion' in snippet or
                'project completed' in snippet):
                
                # Check for "scheduled" or "expected" ONLY if they modify "completion"
                # If "scheduled" appears but "was completed" is also there, "was completed" takes precedence?
                # "Construction was completed... Scheduled for Council acceptance..." -> This is COMPLETED.
                
                # So if we find "was completed", we can be fairly sure.
                # Unless it says "Phase 1 was completed... Phase 2..." 
                # But for this granularity, "was completed" is a strong signal.
                
                # Let's check if "not completed" or similar is there? Unlikely.
                
                is_completed = True
                break

    if is_completed:
        total_funding += amount
        confirmed_projects.append(p_name)

print('__RESULT__:')
print(json.dumps({'confirmed_projects': confirmed_projects, 'total_funding': total_funding}))"""

env_args = {'var_function-call-13164751492978107468': 'file_storage/function-call-13164751492978107468.json', 'var_function-call-13164751492978107155': 'file_storage/function-call-13164751492978107155.json', 'var_function-call-9869211362583101527': 'file_storage/function-call-9869211362583101527.json', 'var_function-call-4590254566354638505': {'confirmed_projects': [], 'total_funding': 0}, 'var_function-call-11353638954296130998': 'Done', 'var_function-call-13277355279832923139': {'text_length': 63699, 'funding_count': 500, 'target_found_exact': True, 'matches_count': 5, 'snippets': ['Bluffs Park Shade Structure\n\n(cid:190) Updates: Construction was completed November 2022. Notice of completion\n\nfiled January 2023\n\nPage 4 of 6\n\nAgenda Item # 4.B.\n\n\n\n\n\n\n\n\n\n\n\nMarie Canyon Green Street', 'Bluffs Park Shade Structure\n\n(cid:190) Project Description: This project consists of the installation of four single-post\n\nshade structures at Malibu Bluffs Park.\n\n(cid:190) Updates:\n\n(cid:131) Staff ', 'Bluffs Park Shade Structure\n\n(cid:190) Project Description: This project consists of the installation of four single-\n\npost shade structures at Malibu Bluffs Park\n\n(cid:190) Estimated Schedule:\n\n(cid:', 'Bluffs Park Shade Structure\n\n(cid:190) Project Description: This project consists of the installation of four single-\n\npost shade structures at Malibu Bluffs Park\n\n(cid:190) Estimated Schedule:\n\n(cid:', 'Bluffs Park Shade Structure\n\n(cid:190) Project Description: This project consists of the installation of four single-post\n\nshade structures at Malibu Bluffs Park.\n\n(cid:190) Updates:\n\n(cid:131) Staff ']}}

exec(code, env_args)
