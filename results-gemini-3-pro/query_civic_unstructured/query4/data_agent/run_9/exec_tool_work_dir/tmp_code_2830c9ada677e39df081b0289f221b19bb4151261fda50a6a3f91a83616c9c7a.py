code = """import json
import pandas as pd

# Load Funding
with open(locals()['var_function-call-7108995134629171603'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)
project_names = funding_df['Project_Name'].unique().tolist()

# Load Civic Docs
with open(locals()['var_function-call-11351715847749976099'], 'r') as f:
    civic_docs = json.load(f)

date_substrings = [
    'spring 2022',
    'march 2022', 'april 2022', 'may 2022',
    'mar 2022', 'apr 2022',
    '03/2022', '04/2022', '05/2022',
    '03-2022', '04-2022', '05-2022'
]

start_keywords = ['begin', 'start', 'advertise', 'initiate', 'commence']
end_keywords = ['complete', 'finish', 'end', 'conclusion']

projects_started_spring_2022 = set()

for doc in civic_docs:
    text = doc['text']
    text_lower = text.lower()
    
    # Find all project occurrences
    all_matches = []
    for pname in project_names:
        pname_lower = pname.lower()
        start = 0
        while True:
            idx = text_lower.find(pname_lower, start)
            if idx == -1:
                break
            all_matches.append({
                'start': idx,
                'end': idx + len(pname),
                'name': pname,
                'len': len(pname)
            })
            start = idx + 1
            
    # Sort: Primary by start position (asc), Secondary by length (desc)
    # This ensures that for same start pos, the longest name comes first.
    all_matches.sort(key=lambda x: (x['start'], -x['len']))
    
    # Filter overlaps
    non_overlapping = []
    last_end = 0
    for m in all_matches:
        if m['start'] >= last_end:
            non_overlapping.append(m)
            last_end = m['end']
        else:
            # This is an overlap/substring, skip it.
            # E.g. found "Project A (FEMA)" (len 20) then "Project A" (len 10) at same start.
            # "Project A" skipped.
            pass
            
    # Process segments
    for i in range(len(non_overlapping)):
        m = non_overlapping[i]
        start_idx = m['start'] # actually the text segment starts after the name? 
        # Usually we look at text *after* the header.
        # But wait, my previous code used start_idx of the name.
        # The segment should be the text describing the project. 
        # The project name is the header. The description follows.
        # So segment start should be m['end'].
        
        seg_start = m['end']
        
        if i < len(non_overlapping) - 1:
            limit = non_overlapping[i+1]['start']
        else:
            limit = len(text)
            
        segment = text[seg_start:limit]
        lines = segment.split(chr(10))
        
        for line in lines:
            line_lower = line.lower()
            
            matched = False
            for ds in date_substrings:
                if ds in line_lower:
                    matched = True
                    break
            
            if matched:
                is_start = any(k in line_lower for k in start_keywords)
                is_end = any(k in line_lower for k in end_keywords)
                
                if is_start and not is_end:
                    projects_started_spring_2022.add(m['name'])
                elif is_start and is_end:
                    if 'begin construction' in line_lower or 'start construction' in line_lower or 'advertise' in line_lower:
                        projects_started_spring_2022.add(m['name'])

matching_projects = list(projects_started_spring_2022)
funding_df_matched = funding_df[funding_df['Project_Name'].isin(matching_projects)]
total_funding = funding_df_matched['Amount'].astype(int).sum()

print('__RESULT__:')
print(json.dumps({
    'count': len(matching_projects),
    'total_funding': int(total_funding),
    'projects': matching_projects
}))"""

env_args = {'var_function-call-1427040905961591816': ['civic_docs'], 'var_function-call-1427040905961592135': ['Funding'], 'var_function-call-7108995134629171603': 'file_storage/function-call-7108995134629171603.json', 'var_function-call-7108995134629172052': 'file_storage/function-call-7108995134629172052.json', 'var_function-call-11351715847749976099': 'file_storage/function-call-11351715847749976099.json', 'var_function-call-2260734469536531693': {'count': 11, 'total_funding': 565000, 'projects': ['Trancas Canyon Park Planting and Irrigation Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Latigo Canyon Road Culvert Repairs', 'Encinal Canyon Road Drainage Improvements', 'Trancas Canyon Park Slope Stabilization Project', 'Civic Center Water Treatment Facility Phase 2', 'Bluffs Park Shade Structure', 'PCH at Trancas Canyon Road Right Turn Lane', 'Marie Canyon Green Streets', 'PCH Signal Synchronization System Improvements Project', 'Latigo Canyon Road Roadway/Retaining Wall Improvements']}, 'var_function-call-13457276042356603299': ['approval by March 2022. The project will be advertised for construction', '(cid:131) Complete Final Design: Spring 2022', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: March 2022', '(cid:131) Begin Construction: March 2022', '(cid:131) This project will be presented to the Planning Commission in May 2022.', 'by March 2022. The project will be advertised for construction bids', '(cid:131) Complete Final Design: Spring 2022']}

exec(code, env_args)
