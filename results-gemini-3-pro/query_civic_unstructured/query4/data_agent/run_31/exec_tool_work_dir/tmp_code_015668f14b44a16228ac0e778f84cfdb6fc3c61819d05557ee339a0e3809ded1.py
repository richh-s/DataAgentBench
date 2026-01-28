code = """import json
import re

# Load civic docs
with open(locals()['var_function-call-8587075472335102739'], 'r') as f:
    docs = json.load(f)

projects = []

def parse_date_season(date_str):
    date_str = date_str.lower().strip()
    if 'spring 2022' in date_str: return True
    if 'march 2022' in date_str or 'mar 2022' in date_str: return True
    if 'april 2022' in date_str or 'apr 2022' in date_str: return True
    if 'may 2022' in date_str: return True
    if re.search(r'(03|04|05)[-/]2022', date_str): return True
    return False

for doc in docs:
    text = doc['text']
    lines = text.split('\n')
    
    potential_title_lines = []
    curr_proj_name = None
    curr_proj_text = ""
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
            
        if "(cid:190)" in stripped:
            if curr_proj_name is None:
                valid_title_lines = [l for l in potential_title_lines if "Agenda" not in l and "Page" not in l and "Capital Improvement" not in l and "Public Works" not in l]
                if valid_title_lines:
                    curr_proj_name = " ".join(valid_title_lines).strip()
                else:
                    curr_proj_name = "Unknown Project"
                curr_proj_text += line + "\n"
                potential_title_lines = []
            else:
                title_candidates = []
                content_candidates = []
                for pt in potential_title_lines:
                    if "(cid:131)" in pt or pt.startswith("Page") or pt.startswith("Agenda"):
                        content_candidates.append(pt)
                    else:
                        title_candidates.append(pt)
                
                real_titles = [t for t in title_candidates if len(t) > 3 and "Agenda" not in t]
                
                if real_titles:
                    projects.append({'name': curr_proj_name, 'text': curr_proj_text})
                    curr_proj_name = " ".join(real_titles).strip()
                    curr_proj_text = line + "\n" 
                    potential_title_lines = []
                else:
                    curr_proj_text += "\n".join(potential_title_lines) + "\n" + line + "\n"
                    potential_title_lines = []
        else:
            potential_title_lines.append(stripped)
            
    if curr_proj_name:
        projects.append({'name': curr_proj_name, 'text': curr_proj_text})

results = []
for p in projects:
    name = p['name']
    text = p['text']
    
    # Check for Start Date matching Spring 2022
    # Patterns:
    # 1. "Begin Construction: Spring 2022"
    # 2. "Start: Spring 2022"
    # 3. "Advertise: Spring 2022" (Maybe? If it's the start phase?)
    # The user asks "projects started in Spring 2022".
    # I will strictly look for "Begin Construction" or "Start" or "Commence" or "Estimated Schedule: \n ... Spring 2022" if it's the first item?
    
    # Let's search for lines with "Spring 2022" (or equivalent) and see what the label is.
    
    lines_in_text = text.split('\n')
    is_target = False
    for l in lines_in_text:
        l_lower = l.lower()
        if parse_date_season(l):
            # Found Spring 2022 in this line. Check context.
            if 'begin construction' in l_lower or 'start' in l_lower or 'commence' in l_lower:
                is_target = True
                break
            # Also check if it's the *only* date or first date in Schedule?
            # E.g. "Advertise: Spring 2022" -> Start of project lifecycle?
            # "projects started" is ambiguous. But usually "Begin Construction" is the main milestone.
            # However, "Design" projects might start design in Spring 2022.
            # "Capital Improvement Projects (Design)" -> "Advertise: Spring 2022" means design done, advertising for construction?
            # If the project is in Design phase, "Started" might mean started design?
            # But the schedule says "Complete Design: Spring 2023".
            # Let's look for any start-like keyword.
            if 'advertise' in l_lower:
                # Advertising is a start of procurement.
                # Let's count it if no better start date exists?
                # Let's stick to "Begin Construction" or "Start" first.
                # Wait, "Latigo Canyon Road Retaining Wall Repair Project" in preview has "Advertise: Spring 2023".
                pass
            
            # If the line contains "Spring 2022" and some activity.
            # Let's accept if it says "Begin" or "Start".
            pass

    if is_target:
        results.append(name)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-6062983773300407174': ['civic_docs'], 'var_function-call-8587075472335102739': 'file_storage/function-call-8587075472335102739.json', 'var_function-call-4603789047444994898': ['Funding'], 'var_function-call-8803859908455603463': 'file_storage/function-call-8803859908455603463.json'}

exec(code, env_args)
