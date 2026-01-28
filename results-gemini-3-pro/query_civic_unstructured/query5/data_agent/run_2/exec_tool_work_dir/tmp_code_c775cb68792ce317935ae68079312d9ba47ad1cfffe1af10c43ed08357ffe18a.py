code = """import json
import re

civic_path = locals()['var_function-call-9021704853761821384']
funding_path = locals()['var_function-call-17294341897624108968']

with open(civic_path, 'r') as f:
    civic = json.load(f)
with open(funding_path, 'r') as f:
    funding = json.load(f)

# Funding map
funding_map = {}
for row in funding:
    nm = row['Project_Name'].strip()
    amt = int(row['Amount'])
    if nm in funding_map:
        funding_map[nm] += amt
    else:
        funding_map[nm] = amt

found_projects = set()
debug_list = []

for doc in civic:
    lines = doc['text'].splitlines()
    for i, line in enumerate(lines):
        # Check for start date patterns with 2022
        if '2022' in line:
            is_start = False
            l_lower = line.lower()
            if 'begin construction' in l_lower: is_start = True
            if 'start construction' in l_lower: is_start = True
            if 'beginning in' in l_lower: is_start = True
            if 'started' in l_lower and 'completed' not in l_lower: is_start = True # "started and is anticipated..."
            
            if is_start:
                # Find project name
                p_name = None
                # Look back
                for k in range(i, max(-1, i-50), -1):
                    l = lines[k].strip()
                    if not l: continue
                    
                    # Check if this line is a project name
                    # Heuristic: Followed by (cid:190) or Updates:
                    if k+1 < len(lines):
                        nx = lines[k+1].strip()
                        if '(cid:190)' in nx or nx.startswith('Updates:') or nx.startswith('Project Description:'):
                            # Exclude headers
                            if 'Capital Improvement Projects' not in l and 'Agenda Item' not in l:
                                p_name = l
                                break
                    
                    # Also check if line is exactly in funding_map
                    if l in funding_map:
                        p_name = l
                        break
                
                if p_name:
                    # Check Disaster
                    # Look at block around
                    context = " ".join(lines[max(0, i-20):min(len(lines), i+20)])
                    
                    is_disaster = False
                    d_kws = ['FEMA', 'CalOES', 'Woolsey', 'Disaster', 'Emergency']
                    if any(kw in p_name for kw in d_kws) or any(kw in context for kw in d_kws):
                        is_disaster = True
                    
                    if is_disaster:
                        found_projects.add(p_name)
                        debug_list.append({'name': p_name, 'date_line': line.strip()})

# Calculate total funding
total = 0
matched_names = []

for p in found_projects:
    # Get funding
    # 1. Exact match
    amt = funding_map.get(p, 0)
    
    # 2. If 0, try fuzzy match or suffix match
    if amt == 0:
        # Maybe p_name in text is "X" but Funding has "X (FEMA Project)"
        # Since we identified it as Disaster, we should look for the FEMA/Disaster version in Funding?
        # Or look for any match starting with p_name?
        for k, v in funding_map.items():
            if k.startswith(p):
                # Check if suffix implies disaster?
                # or just take it if p matches
                amt += v
    else:
        # If exact match found, should we ALSO look for suffixes?
        # e.g. p="X". Funding has "X" and "X (FEMA Project)".
        # If p is disaster, maybe we sum all?
        # Let's sum all variations that start with p_name
         for k, v in funding_map.items():
            if k != p and k.startswith(p) and ('FEMA' in k or 'CalOES' in k):
                amt += v
    
    # If still 0, maybe p_name has extra chars?
    if amt == 0:
         # Try reverse: p_name might contain the Funding name
         for k, v in funding_map.items():
             if k in p:
                 amt += v
                 # And suffixes of k
                 # This is getting messy.
                 # Let's trust exact match or prefix match.
                 pass

    if amt > 0:
        total += amt
        matched_names.append({'name': p, 'amount': amt})

print('__RESULT__:')
print(json.dumps({'total_funding': total, 'projects': matched_names, 'debug': debug_list}))"""

env_args = {'var_function-call-4835809069730370506': ['Funding'], 'var_function-call-4835809069730370969': ['civic_docs'], 'var_function-call-17294341897624108968': 'file_storage/function-call-17294341897624108968.json', 'var_function-call-17294341897624106339': 'file_storage/function-call-17294341897624106339.json', 'var_function-call-9021704853761821384': 'file_storage/function-call-9021704853761821384.json', 'var_function-call-16225886592360458391': 'file_storage/function-call-16225886592360458391.json', 'var_function-call-7448979053420828400': {'total_funding': 0, 'projects': []}, 'var_function-call-6835986635429651258': ['2022 Morning View Resurfacing & Storm Drain Improvements', 'project and will submit to the County for review.', 'PCH Median Improvements Project', 'or phasing out the project', 'Westward Beach Road Repair Project', '(cid:131) City working with consultant on the design of the shoulder repairs', 'Westward Beach Road Drainage Improvements Project', 'cleared the project.', 'Clover Heights Storm Drainage Improvements', 'to finalize plans and specifications', 'Latigo Canyon Road Retaining Wall Repair Project', '(cid:131) Awaiting final FEMA/CalOES approval for scope modification', 'Storm Drain Master Plan', 'Trancas Canyon Park Upper and Lower Slopes Repair', '(cid:131) Plans and specifications are being finalized by consultant', 'Civic Center Water Treatment Facility Phase 2', '(cid:131) Staff has submitted a request for Federal funding', 'Permanent Skate Park', 'project', 'PCH at Trancas Canyon Road Right Turn Lane', 'the Spring 2023.', 'Outdoor Warning Signs', 'Malibu Bluffs Park South Walkway Repairs', '(cid:131) City to request proposal from consultant for design services', 'Trancas Canyon Park Playground', '(cid:131) Staff is currently working on the final design plans', 'Malibu Canyon Road Traffic Study', 'feasible traffic safety improvements can be constructed at this location.', '(cid:131) Funding agreement is schedule for city council on March 27, 2023', 'Malibu Road Slope Repairs', '(cid:190) Updates: Project is currently under construction', 'Encinal Canyon Road Repairs', '(cid:190) Updates: Project is currently under construction', 'PCH Signal Synchronization System Improvements Project', 'Engineering, Inc.', 'Storm Drain Trash Screens Phase Two', '(cid:131) Project is currently out to bid. Bids are due on March 23, 2023.', 'Bluffs Park Shade Structure', 'Marie Canyon Green Streets', 'Broad Beach Road Water Quality Repair', 'Point Dume Walkway Repairs', 'PCH Median Improvements at Paradise Cove and Zuma Beach', 'of Zuma Beach, specifically where the yellow paddles are installed.', 'PCH Crosswalk Improvements at Big Rock Drive and 20326 PCH', 'Kanan Dume Biofilter', 'City Traffic Signals Backup Power', 'Canyon Road, and Winter Canyon Road', '(cid:190) Updates: Project is in the preliminary design phase', 'Marie Canyon Green Streets', 'advertised for construction bids shortly after this date.'], 'var_function-call-14109362879668950822': [], 'var_function-call-15824116889137722751': ['Fiscal Year 2022-2023 Capital Improvement Program:', '2022 Morning View Resurfacing & Storm Drain Improvements', '(cid:131) On September 22, 2022, the City received four (4) construction bids', '(cid:190) Updates: Construction was completed November 2022. Notice of completion', '(cid:131) Construction was completed, November 2022', '(cid:131) Construction was completed, November 2022'], 'var_function-call-16774841394030744416': [{'file': 'malibucity_agenda__01262022-1835.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'file': 'malibucity_agenda__01262022-1835.txt', 'line': '(cid:131) Begin Construction: Spring/Summer 2022'}, {'file': 'malibucity_agenda__01262022-1835.txt', 'line': '(cid:131) Award Contract and Begin Construction: Spring/Summer 2022'}, {'file': 'malibucity_agenda__01262022-1835.txt', 'line': '(cid:131) Begin Construction: Summer/Winter 2022'}, {'file': 'malibucity_agenda__01262022-1835.txt', 'line': '(cid:131) Begin Construction: Fall 2022'}, {'file': 'malibucity_agenda__01262022-1835.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'file': 'malibucity_agenda__01262022-1835.txt', 'line': '(cid:131) Begin Design: Spring 2022'}, {'file': 'malibucity_agenda__01262022-1835.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'file': 'malibucity_agenda__01262022-1835.txt', 'line': '(cid:131) Begin Construction: April 2022'}, {'file': 'malibucity_agenda__01262022-1835.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'file': 'malibucity_agenda__01262022-1835.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'file': 'malibucity_agenda__01262022-1835.txt', 'line': 'beginning in April 2022.'}, {'file': 'malibucity_agenda__01262022-1835.txt', 'line': '(cid:131) Begin Construction: April 2022'}, {'file': 'malibucity_agenda__01262022-1835.txt', 'line': 'started and is anticipated to be completed by the Spring of 2022.'}, {'file': 'malibucity_agenda__01262022-1835.txt', 'line': '(cid:131) Begin Construction: Fall 2022'}, {'file': 'malibucity_agenda__01262022-1835.txt', 'line': 'beginning in Fall 2022.'}, {'file': 'malibucity_agenda__01262022-1835.txt', 'line': '(cid:131) Begin Construction: Fall 2022'}, {'file': 'malibucity_agenda__01272021-1626.txt', 'line': '(cid:131) Begin Construction: March 2022'}, {'file': 'malibucity_agenda__01272021-1626.txt', 'line': '(cid:131) Begin Construction: Summer 2022'}, {'file': 'malibucity_agenda__01272021-1626.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'file': 'malibucity_agenda__01272021-1626.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'file': 'malibucity_agenda__03022021-1648.txt', 'line': '(cid:131) Begin Construction: March 2022'}, {'file': 'malibucity_agenda__03022021-1648.txt', 'line': '(cid:131) Begin Construction: Summer 2022'}, {'file': 'malibucity_agenda__03022021-1648.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'file': 'malibucity_agenda__03022021-1648.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'file': 'malibucity_agenda__03232022-1869.txt', 'line': '(cid:131) Begin Construction: Summer 2022'}, {'file': 'malibucity_agenda__03232022-1869.txt', 'line': '(cid:131) Begin Construction: Summer 2022'}, {'file': 'malibucity_agenda__03232022-1869.txt', 'line': '(cid:131) Award Contract and Begin Construction: Summer 2022'}, {'file': 'malibucity_agenda__03232022-1869.txt', 'line': '(cid:131) Begin Construction: Fall/Winter 2022'}, {'file': 'malibucity_agenda__03232022-1869.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'file': 'malibucity_agenda__03232022-1869.txt', 'line': '(cid:131) Begin Design: Late Spring 2022'}, {'file': 'malibucity_agenda__03232022-1869.txt', 'line': '(cid:131) Begin Construction: Summer 2022'}, {'file': 'malibucity_agenda__03232022-1869.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'file': 'malibucity_agenda__03232022-1869.txt', 'line': '(cid:131) Begin Construction: Summer 2022'}, {'file': 'malibucity_agenda__03232022-1869.txt', 'line': '(cid:131) Begin Construction: Summer 2022'}, {'file': 'malibucity_agenda__03232022-1869.txt', 'line': 'beginning in Spring 2022.'}, {'file': 'malibucity_agenda__03232022-1869.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'file': 'malibucity_agenda__03232022-1869.txt', 'line': '(cid:131) Begin Construction: Fall 2022'}, {'file': 'malibucity_agenda__03232022-1869.txt', 'line': 'beginning in Fall 2022.'}, {'file': 'malibucity_agenda__03232022-1869.txt', 'line': '(cid:131) Begin Construction: Fall 2022'}]}

exec(code, env_args)
