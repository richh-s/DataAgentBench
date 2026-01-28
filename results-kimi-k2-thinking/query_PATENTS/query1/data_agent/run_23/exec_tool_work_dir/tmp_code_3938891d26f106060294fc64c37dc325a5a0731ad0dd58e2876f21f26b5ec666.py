code = """import json, re, collections

fp = globals()['var_functions.query_db:54']
records = json.load(open(fp))

# Diagnostic: check what years we have
pattern = re.compile(r'\b(20\d{2})\b')
year_counts = collections.Counter()
all_codes = set()

for rec in records:
    d = rec.get('publication_date','')
    m = pattern.search(d)
    if m:
        yr = int(m.group(1))
        year_counts[yr] += 1
        
        cpc = rec.get('cpc','[]')
        if cpc:
            try:
                codes = json.loads(cpc)
                for it in codes:
                    cd = it.get('code','')
                    if '/' in cd and not cd.endswith('/00'):
                        all_codes.add(cd)
            except:
                pass

print('Years in data:', sorted(year_counts.keys()))
print('Records per year:')
for yr, cnt in sorted(year_counts.items()):
    print(f'  {yr}: {cnt}')

print('Total level-5 CPC codes:', len(all_codes))

# Check if 2022 exists
has_2022 = 2022 in year_counts
print('Has 2022 data:', has_2022)

# If no 2022, find which years have the most codes
if not has_2022:
    # Count unique codes per year
    year_codes = {}
    for rec in records:
        d = rec.get('publication_date','')
        m = pattern.search(d)
        if m:
            yr = int(m.group(1))
            if yr not in year_codes:
                year_codes[yr] = set()
            
            cpc = rec.get('cpc','[]')
            if cpc:
                try:
                    codes = json.loads(cpc)
                    for it in codes:
                        cd = it.get('code','')
                        if '/' in cd and not cd.endswith('/00'):
                            year_codes[yr].add(cd)
                except:
                    pass
    
    print('\nCode counts by year:')
    for yr, codes in sorted(year_codes.items()):
        print(f'  {yr}: {len(codes)} unique codes')
    
    # Find the most recent year
    if year_counts:
        max_year = max(year_counts.keys())
        print(f'\nMost recent year: {max_year}')
        
        # Calculate for most recent year instead
        year_code_counts = {}
        for rec in records:
            d = rec.get('publication_date','')
            m = pattern.search(d)
            if m and int(m.group(1)) == max_year:
                yr = int(m.group(1))
                cpc = rec.get('cpc','[]')
                if cpc:
                    try:
                        codes = json.loads(cpc)
                        for it in codes:
                            cd = it.get('code','')
                            if '/' in cd and not cd.endswith('/00'):
                                k = (yr, cd)
                                year_code_counts[k] = year_code_counts.get(k, 0) + 1
                    except:
                        pass
        
        all_years = sorted(set(y for y,_ in year_code_counts.keys()))
        all_codes = set(c for _,c in year_code_counts.keys())
        
        s = 0.2
        peaks_target = []
        
        for cd in all_codes:
            ema = None
            max_ema = -1
            peak_yr = None
            for yr in all_years:
                cnt = year_code_counts.get((yr, cd), 0)
                if ema is None:
                    ema = cnt
                else:
                    ema = s * cnt + (1-s) * ema
                if ema > max_ema:
                    max_ema = ema
                    peak_yr = yr
            if peak_yr == max_year:
                peaks_target.append((cd, max_ema))
        
        peaks_target.sort(key=lambda x: x[1], reverse=True)
        result_codes = [c for c,_ in peaks_target]
        
        result = {
            'note': 'No 2022 data found, using most recent year instead',
            'target_year': max_year,
            'cpc_codes': result_codes
        }
else:
    result = {'cpc_codes': []}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B29', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B33', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'C22', 'titleFull': 'METALLURGY; FERROUS OR NON-FERROUS ALLOYS; TREATMENT OF ALLOYS OR NON-FERROUS METALS', 'level': '4.0', 'parents': '[\n  "C"\n]'}, {'symbol': 'D99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0', 'parents': '[\n  "D"\n]'}, {'symbol': 'F28', 'titleFull': 'HEAT EXCHANGE IN GENERAL', 'level': '4.0', 'parents': '[\n  "F"\n]'}, {'symbol': 'B', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING', 'level': '2.0', 'parents': '[]'}, {'symbol': 'H', 'titleFull': 'ELECTRICITY', 'level': '2.0', 'parents': '[]'}, {'symbol': 'Y', 'titleFull': 'GENERAL TAGGING OF NEW TECHNOLOGICAL DEVELOPMENTS; GENERAL TAGGING OF CROSS-SECTIONAL TECHNOLOGIES SPANNING OVER SEVERAL SECTIONS OF THE IPC; TECHNICAL SUBJECTS COVERED BY FORMER USPC CROSS-REFERENCE ART COLLECTIONS [XRACs] AND DIGESTS', 'level': '2.0', 'parents': '[]'}, {'symbol': 'D', 'titleFull': 'TEXTILES; PAPER', 'level': '2.0', 'parents': '[]'}, {'symbol': 'F', 'titleFull': 'MECHANICAL ENGINEERING; LIGHTING; HEATING; WEAPONS; BLASTING', 'level': '2.0', 'parents': '[]'}, {'symbol': 'E', 'titleFull': 'FIXED CONSTRUCTIONS', 'level': '2.0', 'parents': '[]'}, {'symbol': 'C', 'titleFull': 'CHEMISTRY; METALLURGY', 'level': '2.0', 'parents': '[]'}, {'symbol': 'G', 'titleFull': 'PHYSICS', 'level': '2.0', 'parents': '[]'}, {'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES', 'level': '2.0', 'parents': '[]'}], 'var_functions.execute_python:24': {'total_records': 100, 'sample_keys': ['publication_date', 'cpc'], 'sample_pub_dates': ['Aug 3rd, 2021', 'Oct 6th, 2020', 'Sep 21st, 2021', '2020, April 7th', 'Mar 23rd, 2021'], 'sample_cpc_count': 38, 'sample_cpc_codes': ['C01B33/00', 'C01B35/00', 'H01M10/0565']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': [{'total': '277813'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': {'error': 'CPC data file not found'}, 'var_functions.execute_python:40': {'error': 'No CPC records found'}, 'var_functions.execute_python:46': {'analysis_complete': True, 'total_cpc_codes': 0, 'codes_with_peak_2022': 0, 'cpc_codes': []}, 'var_functions.query_db:48': [{'publication_date': 'Aug 3rd, 2021', 'cpc_sample': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"'}, {'publication_date': 'Oct 6th, 2020', 'cpc_sample': '[\n  {\n    "code": "F16H47/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H37/08",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"'}, {'publication_date': 'Sep 21st, 2021', 'cpc_sample': '[\n  {\n    "code": "B29C70/48",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08J5/246",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code":'}, {'publication_date': '2020, April 7th', 'cpc_sample': '[\n  {\n    "code": "A61K48/0066",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C12N2830/32",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "c'}, {'publication_date': 'Mar 23rd, 2021', 'cpc_sample': '[\n  {\n    "code": "H01H9/042",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01H9/223",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code"'}], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.execute_python:62': {'cpc_codes': []}, 'var_functions.query_db:70': [{'total_records': '277813'}], 'var_functions.execute_python:76': {'cpc_codes': []}, 'var_functions.execute_python:84': {'cpc_codes': []}}

exec(code, env_args)
