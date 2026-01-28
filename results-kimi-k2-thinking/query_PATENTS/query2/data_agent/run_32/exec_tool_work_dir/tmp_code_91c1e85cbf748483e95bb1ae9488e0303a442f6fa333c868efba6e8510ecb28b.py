code = """import json, re
from collections import defaultdict

# Load the German patents data file
patents_file = 'var_functions.query_db:148'
with open(patents_file, 'r') as f:
    patents = json.load(f)

print('Loaded ' + str(len(patents)) + ' patent records from 2019')

# Initialize data structures for analysis
cpc_monthly_counts = defaultdict(lambda: defaultdict(int))
month_names = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
second_half_months = ['jul', 'aug', 'sep', 'oct', 'nov', 'dec']
processed_count = 0

# Helper function to extract month number from date string
def extract_month(date_str):
    date_str_lower = str(date_str).lower()
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    for i, month in enumerate(months, 1):
        if month in date_str_lower:
            return i
    return None

# Filter for second half of 2019 and extract CPC level 4 codes
for patent in patents:
    grant_date = patent.get('grant_date', '')
    cpc_data = patent.get('cpc', '[]')
    
    # Check if grant date is in second half of 2019
    date_str = str(grant_date).lower()
    if '2019' not in date_str:
        continue
    
    has_second_half_month = any(m in date_str for m in second_half_months)
    if not has_second_half_month:
        continue
    
    # Extract month number
    month_num = extract_month(grant_date)
    if not month_num or month_num < 7:  # Only July-December (months 7-12)
        continue
    
    try:
        # Parse CPC codes
        if isinstance(cpc_data, str):
            cpc_list = json.loads(cpc_data)
        else:
            cpc_list = cpc_data
        
        # Count each CPC code (extract level 4)
        for cpc_item in cpc_list:
            cpc_full_code = cpc_item.get('code', '')
            if cpc_full_code and '/' in cpc_full_code:
                # Extract level 4 code (main group before slash)
                level_4 = cpc_full_code.split('/')[0]
                # Clean the code
                level_4 = re.sub(r'[^A-Z0-9]$', '', level_4)
                if len(level_4) >= 3:
                    cpc_monthly_counts[level_4][month_num] += 1
                    processed_count += 1
    except:
        continue

print('Filtered to second half 2019: ' + str(len([p for p in patents if any(m in str(p.get('grant_date','')).lower() for m in second_half_months) and '2019' in str(p.get('grant_date','')).lower()])) + ' patents')
print('Total CPC entries analyzed: ' + str(processed_count))
print('Unique CPC Level 4 codes found: ' + str(len(cpc_monthly_counts)))

# Calculate Exponential Moving Average (EMA) with smoothing factor 0.1
alpha = 0.1
cpc_ema_results = []

for cpc_code, monthly_counts in cpc_monthly_counts.items():
    ema = None
    max_ema = 0
    best_month = None
    total_filings = 0
    
    # Calculate EMA for months 7-12 (July to December 2019)
    for month in range(7, 13):
        count = monthly_counts.get(month, 0)
        total_filings += count
        
        if ema is None:
            ema = count
        else:
            ema = alpha * count + (1 - alpha) * ema
        
        # Track highest EMA and the month it occurred
        if ema > max_ema:
            max_ema = ema
            best_month = month
    
    # Store results for this CPC code
    cpc_ema_results.append({
        'cpc_level_4_code': cpc_code,
        'max_ema': round(max_ema, 2),
        'best_month_num': best_month,
        'best_month_name': month_names[best_month] if best_month else '',
        'best_year': 2019,
        'total_filings': total_filings
    })

# Sort by max EMA value
cpc_ema_results.sort(key=lambda x: x['max_ema'], reverse=True)

print('\nTop 10 CPC Level 4 codes by EMA:')
for i, result in enumerate(cpc_ema_results[:10], 1):
    print(str(i) + '. ' + result['cpc_level_4_code'] + ' | ' +
          'EMA: ' + str(result['max_ema']) + ' | ' +
          'Best: ' + result['best_month_name'] + ' ' + str(result['best_year']) + ' | ' +
          'Total: ' + str(result['total_filings']))

# Prepare top codes for title lookup
top_cpc_codes = [r['cpc_level_4_code'] for r in cpc_ema_results[:10]]

result_summary = {
    'analysis_complete': True,
    'total_cpc_codes_analyzed': len(cpc_ema_results),
    'top_cpc_codes': top_cpc_codes,
    'detailed_results': cpc_ema_results[:10]
}

print('__RESULT__:')
print(json.dumps(result_summary))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': 'Date parsing and CPC level 4 extraction functions ready', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:16': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': [{'total_records': '11735'}], 'var_functions.query_db:38': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DE application (number DE-102009046500-A) is owned by LEAR CORP and has publication number DE-102009046500-B4.', 'grant_date': 'Mar 21st, 2019', 'cpc': '[\n  {\n    "code": "G01R31/389",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01R31/389",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'grant_date': '5th of December, 2019', 'cpc': '[\n  {\n    "code": "F02D41/3005",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M65/005",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'grant_date': '22nd of August, 2019', 'cpc': '[\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In DE, the patent filing (application number DE-102015221196-A) is owned by SCHOTT AG and has pub. number DE-102015221196-B4.', 'grant_date': 'September the 19th, 2019', 'cpc': '[\n  {\n    "code": "G01D11/24",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B23K1/0016",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'DIEFFENBACHER GMBH MASCHINEN holds the DE patent application (number DE-102016119956-A), with publication number DE-102016119956-B4.', 'grant_date': 'on March 14th, 2019', 'cpc': '[\n  {\n    "code": "B27N3/24",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B30B15/0094",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B30B5/06",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DE patent filing (application number DE-102018102700-A) is assigned to DIOGO CARLOS ALBERTO RAMOS and has pub. number DE-102018102700-B3.', 'grant_date': '28th Feb 2019', 'cpc': '[\n  {\n    "code": "A23N12/10",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A23B7/0053",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F26B17/18",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F26B3/24",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A23N17/004",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A23N12/083",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A23L3/18",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DE application (number DE-102014111322-A) is owned by LEMKE SEBASTIAN and has publication no. DE-102014111322-B4.', 'grant_date': '17th of October, 2019', 'cpc': '[\n  {\n    "code": "B63B21/50",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In DE, the patent application (no. DE-102014209298-A) is held by DENSO CORP and has publication number DE-102014209298-B4.', 'grant_date': 'on March 21st, 2019', 'cpc': '[\n  {\n    "code": "F02M65/003",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02D41/2467",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M63/0026",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02D2200/0602",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02M2200/247",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02D41/403",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02D41/402",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M65/005",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02D2041/2055",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02M57/005",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/405",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M65/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02T10/40",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:48': [{'symbol': 'B99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}, {'symbol': 'B29', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL'}, {'symbol': 'B33', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY'}], 'var_functions.execute_python:56': ['C04B2235', 'B01D2255', 'B01J29', 'H01R4', 'H04W52', 'C04B35', 'H04L1', 'H01J49', 'B01J23', 'F02D41'], 'var_functions.query_db:66': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DE application (number DE-102009046500-A) is owned by LEAR CORP and has publication number DE-102009046500-B4.', 'grant_date': 'Mar 21st, 2019', 'cpc': '[\n  {\n    "code": "G01R31/389",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01R31/389",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'grant_date': '5th of December, 2019', 'cpc': '[\n  {\n    "code": "F02D41/3005",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M65/005",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'grant_date': '22nd of August, 2019', 'cpc': '[\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:70': [{'symbol': 'G06F', 'titleFull': 'ELECTRIC DIGITAL DATA PROCESSING'}, {'symbol': 'G06F2117/00', 'titleFull': 'Details relating to the type or aim of the circuit design'}, {'symbol': 'G06F2216/00', 'titleFull': 'Indexing scheme relating to additional aspects of information retrieval not explicitly covered by G06F16/00 and subgroups'}, {'symbol': 'G06F2218/00', 'titleFull': 'Aspects of pattern recognition specially adapted for signal processing'}, {'symbol': 'G06F2200/00', 'titleFull': 'Indexing scheme relating to G06F1/04 - G06F1/32'}, {'symbol': 'G06F2115/00', 'titleFull': 'Details relating to the type of the circuit'}, {'symbol': 'G06F2209/00', 'titleFull': 'Indexing scheme relating to G06F9/00'}, {'symbol': 'G06F2111/00', 'titleFull': 'Details relating to CAD techniques'}, {'symbol': 'G06F2206/00', 'titleFull': 'Indexing scheme related to dedicated interfaces for computers'}, {'symbol': 'G06F1/00', 'titleFull': 'Details not covered by groups G06F3/00 - G06F13/00 and G06F21/00'}], 'var_functions.query_db:76': 'file_storage/functions.query_db:76.json', 'var_functions.query_db:78': 'file_storage/functions.query_db:78.json', 'var_functions.query_db:80': 'file_storage/functions.query_db:80.json', 'var_functions.query_db:82': 'file_storage/functions.query_db:82.json', 'var_functions.query_db:88': 'file_storage/functions.query_db:88.json', 'var_functions.query_db:92': [], 'var_functions.query_db:94': [{'total': '11735'}], 'var_functions.query_db:96': 'file_storage/functions.query_db:96.json', 'var_functions.query_db:98': [{'count': '73'}], 'var_functions.query_db:100': 'file_storage/functions.query_db:100.json', 'var_functions.query_db:102': 'file_storage/functions.query_db:102.json', 'var_functions.query_db:104': 'file_storage/functions.query_db:104.json', 'var_functions.query_db:106': 'file_storage/functions.query_db:106.json', 'var_functions.query_db:108': 'file_storage/functions.query_db:108.json', 'var_functions.query_db:110': 'file_storage/functions.query_db:110.json', 'var_functions.query_db:112': 'file_storage/functions.query_db:112.json', 'var_functions.query_db:116': 'file_storage/functions.query_db:116.json', 'var_functions.query_db:120': 'file_storage/functions.query_db:120.json', 'var_functions.query_db:126': [{'count': '87'}], 'var_functions.query_db:128': 'file_storage/functions.query_db:128.json', 'var_functions.query_db:130': 'file_storage/functions.query_db:130.json', 'var_functions.query_db:132': [{'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': 'on October 31st, 2019', 'cpc': '[\n  {\n    "code": "A61M2230/30",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61M2230/30",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3693",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3496",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3496",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3693",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'grant_date': 'on November 5th, 2019', 'cpc': '[\n  {\n    "code": "F04C15/06",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F04C11/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F04C2/1071",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F04C13/008",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F04C11/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F04C13/008",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F04C2/1071",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F01C1/101",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F01C1/101",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F04C15/06",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F01C1/101",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E21B43/129",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F04C15/06",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F04C13/008",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F04C11/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F04C2/1071",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F04C11/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F04C2/107",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F01C1/10",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E21B43/129",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E21B43/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E21B43/129",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E21B43/129",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': 'dated 21st November 2019', 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': 'Mar 21st, 2019', 'cpc': '[\n  {\n    "code": "G01R31/389",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01R31/389",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:134': 'file_storage/functions.query_db:134.json', 'var_functions.query_db:136': 'file_storage/functions.query_db:136.json', 'var_functions.query_db:138': [{'count': '92'}], 'var_functions.query_db:140': 'file_storage/functions.query_db:140.json', 'var_functions.query_db:148': 'file_storage/functions.query_db:148.json', 'var_functions.query_db:150': 'file_storage/functions.query_db:150.json'}

exec(code, env_args)
