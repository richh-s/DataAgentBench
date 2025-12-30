code = """import json
import re

civic_path = locals()['var_function-call-9021704853761821384']
with open(civic_path, 'r') as f:
    civic = json.load(f)

text = civic[0]['text'] # assume 1 doc
lines = text.splitlines()

matches = []

# Iterate lines to find "2022" in start context
for i, line in enumerate(lines):
    # Check for start date patterns with 2022
    if '2022' in line:
        is_start = False
        if 'Begin Construction' in line: is_start = True
        if 'Start Date' in line: is_start = True
        if 'commence' in line: is_start = True
        if 'beginning in' in line: is_start = True
        if 'Construction started' in line: is_start = True
        
        if is_start:
            # Find project name by looking backwards
            # Search for a line that is followed by (cid:190)
            # and is a Project Name (headers are usually distinct)
            
            p_name = None
            # Look back
            for k in range(i, -1, -1):
                l = lines[k].strip()
                if not l: continue
                # Check if this line is a project name
                # It should be followed by a line with (cid:190) or "Updates:"
                # Check line k+1 (which might be < i)
                if k+1 < len(lines):
                    nx = lines[k+1].strip()
                    if '(cid:190)' in nx or nx.startswith('Updates:'):
                        # Candidate.
                        # Exclude headers
                        if 'Capital Improvement Projects' not in l:
                            p_name = l
                            break
            
            if p_name:
                # Check if disaster
                # We need the whole block to check for keywords, or just the name
                # Let's extract a small window around the date line to check context
                context = " ".join(lines[max(0, i-10):min(len(lines), i+10)])
                
                is_disaster = False
                kws = ['FEMA', 'CalOES', 'Woolsey', 'Disaster', 'Emergency']
                if any(kw in p_name for kw in kws) or any(kw in context for kw in kws):
                    is_disaster = True
                
                matches.append({
                    'name': p_name,
                    'line': line.strip(),
                    'is_disaster': is_disaster
                })

print('__RESULT__:')
print(json.dumps(matches))"""

env_args = {'var_function-call-4835809069730370506': ['Funding'], 'var_function-call-4835809069730370969': ['civic_docs'], 'var_function-call-17294341897624108968': 'file_storage/function-call-17294341897624108968.json', 'var_function-call-17294341897624106339': 'file_storage/function-call-17294341897624106339.json', 'var_function-call-9021704853761821384': 'file_storage/function-call-9021704853761821384.json', 'var_function-call-16225886592360458391': 'file_storage/function-call-16225886592360458391.json', 'var_function-call-7448979053420828400': {'total_funding': 0, 'projects': []}, 'var_function-call-6835986635429651258': ['2022 Morning View Resurfacing & Storm Drain Improvements', 'project and will submit to the County for review.', 'PCH Median Improvements Project', 'or phasing out the project', 'Westward Beach Road Repair Project', '(cid:131) City working with consultant on the design of the shoulder repairs', 'Westward Beach Road Drainage Improvements Project', 'cleared the project.', 'Clover Heights Storm Drainage Improvements', 'to finalize plans and specifications', 'Latigo Canyon Road Retaining Wall Repair Project', '(cid:131) Awaiting final FEMA/CalOES approval for scope modification', 'Storm Drain Master Plan', 'Trancas Canyon Park Upper and Lower Slopes Repair', '(cid:131) Plans and specifications are being finalized by consultant', 'Civic Center Water Treatment Facility Phase 2', '(cid:131) Staff has submitted a request for Federal funding', 'Permanent Skate Park', 'project', 'PCH at Trancas Canyon Road Right Turn Lane', 'the Spring 2023.', 'Outdoor Warning Signs', 'Malibu Bluffs Park South Walkway Repairs', '(cid:131) City to request proposal from consultant for design services', 'Trancas Canyon Park Playground', '(cid:131) Staff is currently working on the final design plans', 'Malibu Canyon Road Traffic Study', 'feasible traffic safety improvements can be constructed at this location.', '(cid:131) Funding agreement is schedule for city council on March 27, 2023', 'Malibu Road Slope Repairs', '(cid:190) Updates: Project is currently under construction', 'Encinal Canyon Road Repairs', '(cid:190) Updates: Project is currently under construction', 'PCH Signal Synchronization System Improvements Project', 'Engineering, Inc.', 'Storm Drain Trash Screens Phase Two', '(cid:131) Project is currently out to bid. Bids are due on March 23, 2023.', 'Bluffs Park Shade Structure', 'Marie Canyon Green Streets', 'Broad Beach Road Water Quality Repair', 'Point Dume Walkway Repairs', 'PCH Median Improvements at Paradise Cove and Zuma Beach', 'of Zuma Beach, specifically where the yellow paddles are installed.', 'PCH Crosswalk Improvements at Big Rock Drive and 20326 PCH', 'Kanan Dume Biofilter', 'City Traffic Signals Backup Power', 'Canyon Road, and Winter Canyon Road', '(cid:190) Updates: Project is in the preliminary design phase', 'Marie Canyon Green Streets', 'advertised for construction bids shortly after this date.']}

exec(code, env_args)
