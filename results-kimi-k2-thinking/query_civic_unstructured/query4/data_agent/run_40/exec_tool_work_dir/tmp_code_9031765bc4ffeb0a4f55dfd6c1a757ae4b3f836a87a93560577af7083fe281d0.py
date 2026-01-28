code = """import os, json, re

# Find data files on system
files = []
for root, dirs, filenames in os.walk('/'):
    for f in filenames:
        if 'query_db' in f and f.endswith('.json'):
            files.append(os.path.join(root, f))

print('Found files:')
for f in files[:5]:
    print(f)

if len(files) >= 2:
    # Load the files
    with open(files[0], 'r') as f:
        data1 = json.load(f)
    with open(files[1], 'r') as f:
        data2 = json.load(f)
    
    # Determine which is which
    if len(data1) > 0 and 'Funding_ID' in str(data1[0]):
        funding = data1
        civic = data2
    else:
        funding = data2
        civic = data1
    
    print('\nFunding records:', len(funding))
    print('Civic docs:', len(civic))
    
    # Extract Spring 2022 projects from civic docs
    spring_projects = []
    for doc in civic:
        txt = doc['text']
        if 'Spring 2022' in txt or '2022-Spring' in txt:
            lines = txt.split('\n')
            for i in range(len(lines)):
                if lines[i].strip() and ('Spring 2022' in lines[i] or '2022-Spring' in lines[i]):
                    # Look back up to 5 lines
                    start = max(0, i-5)
                    for j in range(i-1, start-1, -1):
                        candidate = lines[j].strip()
                        if candidate and len(candidate) > 10 and not candidate.startswith('('):
                            spring_projects.append(candidate)
                            break
                    break
    
    print('Spring 2022 candidates:', len(spring_projects))
    
    # Match with funding
    matched_names = set()
    total = 0
    for fund in funding:
        fname = fund['Project_Name']
        amount = int(fund['Amount'])
        for proj in spring_projects:
            # Check if either string contains the other
            if fname in proj or proj in fname or any(part in fname for part in proj.split() if len(part) > 5):
                if fname not in matched_names:
                    matched_names.add(fname)
                    total += amount
                    break
    
    result = json.dumps({'project_count': len(matched_names), 'total_funding': total})
    print('__RESULT__:')
    print(result)
else:
    print('Failed to find data files')"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
