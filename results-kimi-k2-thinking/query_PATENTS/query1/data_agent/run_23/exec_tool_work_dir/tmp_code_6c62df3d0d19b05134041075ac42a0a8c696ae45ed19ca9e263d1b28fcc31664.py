code = """import json
import re
import collections

# Load the full dataset
file_path = globals()['var_functions.query_db:54']
records = json.load(open(file_path))

print(f"Processing {len(records)} records")

# Extract year and level-5 CPC codes
year_pattern = re.compile(r'\b(20\d{2})\b')
year_code_counts = collections.Counter()

for rec in records:
    date_str = rec.get('publication_date', '')
    match = year_pattern.search(date_str)
    
    if match:
        year = int(match.group(1))
        cpc_str = rec.get('cpc', '[]')
        
        if cpc_str and cpc_str != '[]':
            try:
                cpc_list = json.loads(cpc_str)
                for item in cpc_list:
                    code = item.get('code', '')
                    # Level 5: has / and subgroup not 00
                    if '/' in code and not code.endswith('/00'):
                        year_code_counts[(year, code)] += 1
            except:
                pass

# Check what years we actually have
all_years = sorted(set(y for y,_ in year_code_counts.keys()))
print(f"Years in dataset: {all_years}")

# Check 2022 specifically
has_2022 = 2022 in all_years
print(f"Has 2022: {has_2022}")

if not has_2022:
    print("No 2022 data found - cannot complete analysis")
    result = []
else:
    # Get all unique level-5 codes
    all_codes = set(c for _,c in year_code_counts.keys())
    print(f"Total unique level-5 codes: {len(all_codes)}")
    
    # Calculate simple trend: compare 2022 to average of previous years
    codes_with_2022_growth = []
    
    for code in all_codes:
        # Get counts for each year for this code
        code_yearly = {year: year_code_counts[(year, code)] 
                      for year in all_years if (year, code) in year_code_counts}
        
        if 2022 not in code_yearly:
            continue
            
        count_2022 = code_yearly[2022]
        
        # Get counts for previous years (2018-2021)
        prev_years = [y for y in [2018, 2019, 2020, 2021] if y in code_yearly]
        
        if not prev_years:
            continue
            
        avg_prev = sum(code_yearly[y] for y in prev_years) / len(prev_years)
        
        if avg_prev > 0 and count_2022 > avg_prev * 1.2:  # 20% growth or more
            growth_ratio = count_2022 / avg_prev
            codes_with_2022_growth.append((code, growth_ratio, count_2022, avg_prev))
    
    # Sort by growth ratio
    codes_with_2022_growth.sort(key=lambda x: x[1], reverse=True)
    
    print(f"Codes with growth in 2022: {len(codes_with_2022_growth)}")
    if codes_with_2022_growth:
        print("Top 10 by growth:")
        for code, ratio, count_2022, avg_prev in codes_with_2022_growth[:10]:
            print(f"  {code}: {count_2022} patents vs {avg_prev:.1f} avg ({ratio:.2f}x)")
    
    # Extract just the codes
    result = [code for code, _, _, _ in codes_with_2022_growth]

# Return the CPC codes
print("\n__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B29', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B33', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'C22', 'titleFull': 'METALLURGY; FERROUS OR NON-FERROUS ALLOYS; TREATMENT OF ALLOYS OR NON-FERROUS METALS', 'level': '4.0', 'parents': '[\n  "C"\n]'}, {'symbol': 'D99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0', 'parents': '[\n  "D"\n]'}, {'symbol': 'F28', 'titleFull': 'HEAT EXCHANGE IN GENERAL', 'level': '4.0', 'parents': '[\n  "F"\n]'}, {'symbol': 'B', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING', 'level': '2.0', 'parents': '[]'}, {'symbol': 'H', 'titleFull': 'ELECTRICITY', 'level': '2.0', 'parents': '[]'}, {'symbol': 'Y', 'titleFull': 'GENERAL TAGGING OF NEW TECHNOLOGICAL DEVELOPMENTS; GENERAL TAGGING OF CROSS-SECTIONAL TECHNOLOGIES SPANNING OVER SEVERAL SECTIONS OF THE IPC; TECHNICAL SUBJECTS COVERED BY FORMER USPC CROSS-REFERENCE ART COLLECTIONS [XRACs] AND DIGESTS', 'level': '2.0', 'parents': '[]'}, {'symbol': 'D', 'titleFull': 'TEXTILES; PAPER', 'level': '2.0', 'parents': '[]'}, {'symbol': 'F', 'titleFull': 'MECHANICAL ENGINEERING; LIGHTING; HEATING; WEAPONS; BLASTING', 'level': '2.0', 'parents': '[]'}, {'symbol': 'E', 'titleFull': 'FIXED CONSTRUCTIONS', 'level': '2.0', 'parents': '[]'}, {'symbol': 'C', 'titleFull': 'CHEMISTRY; METALLURGY', 'level': '2.0', 'parents': '[]'}, {'symbol': 'G', 'titleFull': 'PHYSICS', 'level': '2.0', 'parents': '[]'}, {'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES', 'level': '2.0', 'parents': '[]'}], 'var_functions.execute_python:24': {'total_records': 100, 'sample_keys': ['publication_date', 'cpc'], 'sample_pub_dates': ['Aug 3rd, 2021', 'Oct 6th, 2020', 'Sep 21st, 2021', '2020, April 7th', 'Mar 23rd, 2021'], 'sample_cpc_count': 38, 'sample_cpc_codes': ['C01B33/00', 'C01B35/00', 'H01M10/0565']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': [{'total': '277813'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': {'error': 'CPC data file not found'}, 'var_functions.execute_python:40': {'error': 'No CPC records found'}, 'var_functions.execute_python:46': {'analysis_complete': True, 'total_cpc_codes': 0, 'codes_with_peak_2022': 0, 'cpc_codes': []}, 'var_functions.query_db:48': [{'publication_date': 'Aug 3rd, 2021', 'cpc_sample': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"'}, {'publication_date': 'Oct 6th, 2020', 'cpc_sample': '[\n  {\n    "code": "F16H47/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H37/08",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"'}, {'publication_date': 'Sep 21st, 2021', 'cpc_sample': '[\n  {\n    "code": "B29C70/48",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08J5/246",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code":'}, {'publication_date': '2020, April 7th', 'cpc_sample': '[\n  {\n    "code": "A61K48/0066",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C12N2830/32",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "c'}, {'publication_date': 'Mar 23rd, 2021', 'cpc_sample': '[\n  {\n    "code": "H01H9/042",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01H9/223",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code"'}], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.execute_python:62': {'cpc_codes': []}, 'var_functions.query_db:70': [{'total_records': '277813'}], 'var_functions.execute_python:76': {'cpc_codes': []}, 'var_functions.execute_python:84': {'cpc_codes': []}, 'var_functions.query_db:88': 'file_storage/functions.query_db:88.json', 'var_functions.execute_python:94': {'cpc_codes': []}, 'var_functions.execute_python:98': [], 'var_functions.execute_python:104': []}

exec(code, env_args)
