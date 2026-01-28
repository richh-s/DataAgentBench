code = """import json

path_funding = locals()['var_function-call-8803859908455603463']
path_docs = locals()['var_function-call-8587075472335102739']

with open(path_funding, 'r') as f:
    funding_data = json.load(f)

with open(path_docs, 'r') as f:
    docs = json.load(f)

valid_names = set(x['Project_Name'] for x in funding_data)
# Create a mapping for prefix matching
# e.g. "Birdview Avenue Improvements" -> ["Birdview Avenue Improvements", "Birdview Avenue Improvements (CalOES Project)", ...]
name_map = {}
for vn in valid_names:
    # Normalize: remove suffixes like (FEMA Project) for matching base name
    base = vn.split('(')[0].strip()
    if base not in name_map:
        name_map[base] = []
    name_map[base].append(vn)

identified = []
marker = 'cid:190'

for doc in docs:
    lines = doc['text'].splitlines()
    curr_name = None
    buf = []
    
    for line in lines:
        s = line.strip()
        if not s: continue
        
        if marker in s:
            # Try to identify name from buf
            # Check last few lines
            candidates = buf[-3:] if len(buf)>=3 else buf
            found_vn = None
            
            # Iterate backwards through candidates
            for cand in reversed(candidates):
                if not cand: continue
                # Check exact match
                if cand in valid_names:
                    found_vn = cand
                    break
                # Check base match
                if cand in name_map:
                    # Found a base name. Which variant?
                    # We don't know yet. But we can store the base name and decide later?
                    # Or just pick the first one?
                    # The prompt asks for total funding.
                    # If "Birdview Avenue Improvements" starts in Spring 2022, 
                    # do we include funding for "Birdview Avenue Improvements (CalOES Project)"?
                    # Yes, likely.
                    # So we should track the project *base* name or all variants.
                    # Let's store the base name `cand` if it matches.
                    found_vn = cand
                    break
                
                # Check if cand is a prefix of some valid name
                # e.g. cand="Latigo Canyon Road Retaining Wall Repair Project" (full match)
                # cand="Latigo Canyon Road" (partial?)
                
                # Let's rely on exact or base match found in `name_map`.
            
            curr_name = found_vn
            buf = []
        else:
            buf.append(s)
            if curr_name:
                low = s.lower()
                match = False
                if 'spring 2022' in low: match = True
                if 'march 2022' in low: match = True
                if 'april 2022' in low: match = True
                if 'may 2022' in low: match = True
                
                if match:
                    if 'begin' in low or 'start' in low or 'commence' in low:
                        # Add all variants of this project to identified?
                        # Or just the detected name?
                        # If I detected "Birdview Avenue Improvements", and it's a key in name_map
                        # I should add all values in name_map[curr_name] to the list?
                        if curr_name in name_map:
                            for v in name_map[curr_name]:
                                identified.append(v)
                        elif curr_name in valid_names:
                            # It's a full name
                            identified.append(curr_name)
                            # Also check if it is a base for others?
                            base = curr_name.split('(')[0].strip()
                            if base in name_map and base != curr_name:
                                for v in name_map[base]:
                                    identified.append(v)

final_projects = list(set(identified))
print('__RESULT__:')
print(json.dumps(final_projects))"""

env_args = {'var_function-call-6062983773300407174': ['civic_docs'], 'var_function-call-8587075472335102739': 'file_storage/function-call-8587075472335102739.json', 'var_function-call-4603789047444994898': ['Funding'], 'var_function-call-8803859908455603463': 'file_storage/function-call-8803859908455603463.json', 'var_function-call-4031632959131545213': ['scheduled for the April 11, 2022 Council meeting.', 'sending this project out to bid during the Spring of 2022.', 'damaged by the Woolsey Fire.', 'beginning in April 2022.', 'March 2022', 'beginning in Spring 2022.', '(cid:131) The project consultant has started the design of this project.', 'assessment district will be created.', 'advertised for construction bids shortly after this date.', 'timber with non-combustible materials.', 'Fire.', '(cid:131) Next public community meeting is scheduled for March 25th.', 'is finalizing the bid documents.', 'that was damaged by the Woolsey Fire.', 'Metro.']}

exec(code, env_args)
