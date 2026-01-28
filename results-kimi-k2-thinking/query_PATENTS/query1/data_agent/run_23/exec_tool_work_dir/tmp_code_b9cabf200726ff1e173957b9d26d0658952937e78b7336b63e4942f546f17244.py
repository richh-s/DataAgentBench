code = """import json, re, collections

# Get file path for 2022 data
file_path = globals()['var_functions.query_db:88']

# Load records
records = json.load(open(file_path))

# Process 2022 records first to understand what we have
print('2022 records found:', len(records))

# Check level-5 CPC codes in 2022
level5_codes_2022 = set()
for rec in records:
    cpc_str = rec.get('cpc', '[]')
    try:
        codes = json.loads(cpc_str)
        for it in codes:
            cd = it.get('code', '')
            if '/' in cd and not cd.endswith('/00'):
                level5_codes_2022.add(cd)
    except:
        pass

print('Unique level-5 codes in 2022 sample:', len(level5_codes_2022))

# Now get full dataset to calculate EMA
full_file_path = globals()['var_functions.query_db:54']
full_records = json.load(open(full_file_path))

# Process all records to get yearly counts for each level-5 code
pattern = re.compile(r'\b(20\d{2})\b')
year_code_counts = {}

for rec in full_records:
    d = rec.get('publication_date', '')
    m = pattern.search(d)
    if m:
        yr = int(m.group(1))
        cpc = rec.get('cpc', '[]')
        if cpc:
            try:
                codes = json.loads(cpc)
                for it in codes:
                    cd = it.get('code', '')
                    if '/' in cd and not cd.endswith('/00'):
                        k = (yr, cd)
                        year_code_counts[k] = year_code_counts.get(k, 0) + 1
            except:
                pass

# Get all years and codes
all_years = sorted(set(y for y,_ in year_code_counts.keys()))
all_codes = set(c for _,c in year_code_counts.keys())

print('All years:', all_years)
print('All level-5 codes:', len(all_codes))

# Calculate EMA for each code
smoothing = 0.2
codes_peaking_2022 = []

for cd in all_codes:
    ema = None
    max_ema = -1
    peak_year = None
    
    for yr in all_years:
        cnt = year_code_counts.get((yr, cd), 0)
        
        if ema is None:
            ema = cnt
        else:
            ema = smoothing * cnt + (1-smoothing) * ema
        
        if ema > max_ema:
            max_ema = ema
            peak_year = yr
    
    if peak_year == 2022:
        codes_peaking_2022.append((cd, max_ema))

# Sort by EMA value
codes_peaking_2022.sort(key=lambda x: x[1], reverse=True)

print('Codes peaking in 2022:', len(codes_peaking_2022))
if codes_peaking_2022:
    print('Top 20:')
    for cd, ema in codes_peaking_2022[:20]:
        print(f'  {cd}: EMA = {ema:.2f}')

# Extract just the CPC codes
final_codes = [cd for cd, _ in codes_peaking_2022]

result = {'cpc_codes': final_codes}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B29', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B33', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'C22', 'titleFull': 'METALLURGY; FERROUS OR NON-FERROUS ALLOYS; TREATMENT OF ALLOYS OR NON-FERROUS METALS', 'level': '4.0', 'parents': '[\n  "C"\n]'}, {'symbol': 'D99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0', 'parents': '[\n  "D"\n]'}, {'symbol': 'F28', 'titleFull': 'HEAT EXCHANGE IN GENERAL', 'level': '4.0', 'parents': '[\n  "F"\n]'}, {'symbol': 'B', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING', 'level': '2.0', 'parents': '[]'}, {'symbol': 'H', 'titleFull': 'ELECTRICITY', 'level': '2.0', 'parents': '[]'}, {'symbol': 'Y', 'titleFull': 'GENERAL TAGGING OF NEW TECHNOLOGICAL DEVELOPMENTS; GENERAL TAGGING OF CROSS-SECTIONAL TECHNOLOGIES SPANNING OVER SEVERAL SECTIONS OF THE IPC; TECHNICAL SUBJECTS COVERED BY FORMER USPC CROSS-REFERENCE ART COLLECTIONS [XRACs] AND DIGESTS', 'level': '2.0', 'parents': '[]'}, {'symbol': 'D', 'titleFull': 'TEXTILES; PAPER', 'level': '2.0', 'parents': '[]'}, {'symbol': 'F', 'titleFull': 'MECHANICAL ENGINEERING; LIGHTING; HEATING; WEAPONS; BLASTING', 'level': '2.0', 'parents': '[]'}, {'symbol': 'E', 'titleFull': 'FIXED CONSTRUCTIONS', 'level': '2.0', 'parents': '[]'}, {'symbol': 'C', 'titleFull': 'CHEMISTRY; METALLURGY', 'level': '2.0', 'parents': '[]'}, {'symbol': 'G', 'titleFull': 'PHYSICS', 'level': '2.0', 'parents': '[]'}, {'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES', 'level': '2.0', 'parents': '[]'}], 'var_functions.execute_python:24': {'total_records': 100, 'sample_keys': ['publication_date', 'cpc'], 'sample_pub_dates': ['Aug 3rd, 2021', 'Oct 6th, 2020', 'Sep 21st, 2021', '2020, April 7th', 'Mar 23rd, 2021'], 'sample_cpc_count': 38, 'sample_cpc_codes': ['C01B33/00', 'C01B35/00', 'H01M10/0565']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': [{'total': '277813'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': {'error': 'CPC data file not found'}, 'var_functions.execute_python:40': {'error': 'No CPC records found'}, 'var_functions.execute_python:46': {'analysis_complete': True, 'total_cpc_codes': 0, 'codes_with_peak_2022': 0, 'cpc_codes': []}, 'var_functions.query_db:48': [{'publication_date': 'Aug 3rd, 2021', 'cpc_sample': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"'}, {'publication_date': 'Oct 6th, 2020', 'cpc_sample': '[\n  {\n    "code": "F16H47/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H37/08",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"'}, {'publication_date': 'Sep 21st, 2021', 'cpc_sample': '[\n  {\n    "code": "B29C70/48",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08J5/246",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code":'}, {'publication_date': '2020, April 7th', 'cpc_sample': '[\n  {\n    "code": "A61K48/0066",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C12N2830/32",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "c'}, {'publication_date': 'Mar 23rd, 2021', 'cpc_sample': '[\n  {\n    "code": "H01H9/042",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01H9/223",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code"'}], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.execute_python:62': {'cpc_codes': []}, 'var_functions.query_db:70': [{'total_records': '277813'}], 'var_functions.execute_python:76': {'cpc_codes': []}, 'var_functions.execute_python:84': {'cpc_codes': []}, 'var_functions.query_db:88': 'file_storage/functions.query_db:88.json'}

exec(code, env_args)
