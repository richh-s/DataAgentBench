code = """import json
import re
from collections import defaultdict

# Load German patents data
german_patents_file = 'var_functions.query_db:82'
with open(german_patents_file, 'r') as f:
    german_patents = json.load(f)

print(f'Loaded {len(german_patents)} German patent records')

# Function to check if date is second half 2019
def is_second_half_2019(date_str):
    if not date_str:
        return False
    date_str = str(date_str).lower()
    if '2019' not in date_str:
        return False
    # Check for second half months
    months = ['jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    return any(month in date_str for month in months)

# Function to extract CPC level 4 code
def extract_cpc_level_4(cpc_code):
    if not cpc_code:
        return None
    try:
        # Extract main part before /
        main_part = str(cpc_code).split('/')[0]
        # Clean up - remove trailing non-alphanumeric
        clean_part = re.sub(r'[^A-Z0-9]$', '', main_part)
        return clean_part
    except:
        return None

# Function to extract month number
def extract_month(date_str):
    date_str = str(date_str).lower()
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    for i, month in enumerate(months, 1):
        if month in date_str:
            return i
    return None

# Count CPC Level 4 codes by month for second half 2019
cpc_monthly_counts = defaultdict(lambda: defaultdict(int))
monthly_totals = defaultdict(int)
total_processed = 0

for patent in german_patents:
    grant_date = patent.get('grant_date', '')
    cpc_data = patent.get('cpc', '')
    
    if not is_second_half_2019(grant_date):
        continue
    
    month_num = extract_month(grant_date)
    if not month_num or month_num < 7:  # Must be second half
        continue
    
    try:
        # Parse CPC JSON
        if isinstance(cpc_data, str):
            cpc_list = json.loads(cpc_data)
        else:
            cpc_list = cpc_data
            
        for cpc_item in cpc_list:
            cpc_code = cpc_item.get('code')
            if cpc_code:
                level_4 = extract_cpc_level_4(cpc_code)
                if level_4 and len(level_4) >= 3:
                    cpc_monthly_counts[level_4][month_num] += 1
                    monthly_totals[month_num] += 1
                    total_processed += 1
    except:
        continue

print(f'Processed {total_processed} CPC entries from second half 2019')
print(f'Found {len(cpc_monthly_counts)} unique CPC Level 4 codes')
print(f'Monthly totals: {dict(monthly_totals)}')

# Calculate Exponential Moving Average (EMA) for each CPC Level 4
alpha = 0.1  # Smoothing factor
cpc_ema_results = {}

for cpc_code, monthly_counts in cpc_monthly_counts.items():
    ema = None
    max_ema = 0
    best_month = None
    
    # Calculate EMA from July to December (months 7-12)
    for month in range(7, 13):
        value = monthly_counts.get(month, 0)
        
        if ema is None:
            ema = value  # Initialize with first value
        else:
            ema = alpha * value + (1 - alpha) * ema
        
        # Track maximum EMA
        if ema > max_ema:
            max_ema = ema
            best_month = month
    
    cpc_ema_results[cpc_code] = {
        'max_ema': round(max_ema, 2),
        'best_month': best_month,
        'best_month_name': ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][best_month] if best_month else None,
        'total_filing': sum(monthly_counts.values()),
        'final_ema': round(ema, 2) if ema is not None else 0
    }

# Sort by max EMA value
sorted_cpc = sorted(cpc_ema_results.items(), key=lambda x: x[1]['max_ema'], reverse=True)

print(f'\nTop 15 CPC Level 4 codes by EMA:')
for i, (cpc, data) in enumerate(sorted_cpc[:15], 1):
    print(f"{i:2d}. {cpc:<10} | Max EMA: {data['max_ema']:6.2f} | " + 
          f"Best: {data['best_month_name']} 2019 | Total: {data['total_filing']:3d}")

# Prepare results for title lookup
top_10_cpc = []
for i, (cpc_code, data) in enumerate(sorted_cpc[:10], 1):
    top_10_cpc.append({
        'rank': i,
        'cpc_level_4': cpc_code,
        'max_ema': data['max_ema'],
        'best_month_name': data['best_month_name'],
        'best_month_num': data['best_month'],
        'total_filing': data['total_filing']
    })

result_data = {
    'total_cpc_codes': len(sorted_cpc),
    'total_filings_second_half_2019': total_processed,
    'top_cpc_codes': top_10_cpc
}

print('\nPreparing to fetch titles for top codes...')
print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': 'Date parsing and CPC level 4 extraction functions ready', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:16': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': [{'total_records': '11735'}], 'var_functions.query_db:38': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DE application (number DE-102009046500-A) is owned by LEAR CORP and has publication number DE-102009046500-B4.', 'grant_date': 'Mar 21st, 2019', 'cpc': '[\n  {\n    "code": "G01R31/389",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01R31/389",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'grant_date': '5th of December, 2019', 'cpc': '[\n  {\n    "code": "F02D41/3005",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M65/005",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'grant_date': '22nd of August, 2019', 'cpc': '[\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In DE, the patent filing (application number DE-102015221196-A) is owned by SCHOTT AG and has pub. number DE-102015221196-B4.', 'grant_date': 'September the 19th, 2019', 'cpc': '[\n  {\n    "code": "G01D11/24",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B23K1/0016",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'DIEFFENBACHER GMBH MASCHINEN holds the DE patent application (number DE-102016119956-A), with publication number DE-102016119956-B4.', 'grant_date': 'on March 14th, 2019', 'cpc': '[\n  {\n    "code": "B27N3/24",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B30B15/0094",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B30B5/06",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DE patent filing (application number DE-102018102700-A) is assigned to DIOGO CARLOS ALBERTO RAMOS and has pub. number DE-102018102700-B3.', 'grant_date': '28th Feb 2019', 'cpc': '[\n  {\n    "code": "A23N12/10",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A23B7/0053",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F26B17/18",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F26B3/24",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A23N17/004",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A23N12/083",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A23L3/18",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DE application (number DE-102014111322-A) is owned by LEMKE SEBASTIAN and has publication no. DE-102014111322-B4.', 'grant_date': '17th of October, 2019', 'cpc': '[\n  {\n    "code": "B63B21/50",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In DE, the patent application (no. DE-102014209298-A) is held by DENSO CORP and has publication number DE-102014209298-B4.', 'grant_date': 'on March 21st, 2019', 'cpc': '[\n  {\n    "code": "F02M65/003",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02D41/2467",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M63/0026",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02D2200/0602",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02M2200/247",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02D41/403",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02D41/402",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M65/005",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02D2041/2055",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02M57/005",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/405",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M65/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02T10/40",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:48': [{'symbol': 'B99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}, {'symbol': 'B29', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL'}, {'symbol': 'B33', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY'}], 'var_functions.execute_python:56': ['C04B2235', 'B01D2255', 'B01J29', 'H01R4', 'H04W52', 'C04B35', 'H04L1', 'H01J49', 'B01J23', 'F02D41'], 'var_functions.query_db:66': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DE application (number DE-102009046500-A) is owned by LEAR CORP and has publication number DE-102009046500-B4.', 'grant_date': 'Mar 21st, 2019', 'cpc': '[\n  {\n    "code": "G01R31/389",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01R31/389",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'grant_date': '5th of December, 2019', 'cpc': '[\n  {\n    "code": "F02D41/3005",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M65/005",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'grant_date': '22nd of August, 2019', 'cpc': '[\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:70': [{'symbol': 'G06F', 'titleFull': 'ELECTRIC DIGITAL DATA PROCESSING'}, {'symbol': 'G06F2117/00', 'titleFull': 'Details relating to the type or aim of the circuit design'}, {'symbol': 'G06F2216/00', 'titleFull': 'Indexing scheme relating to additional aspects of information retrieval not explicitly covered by G06F16/00 and subgroups'}, {'symbol': 'G06F2218/00', 'titleFull': 'Aspects of pattern recognition specially adapted for signal processing'}, {'symbol': 'G06F2200/00', 'titleFull': 'Indexing scheme relating to G06F1/04 - G06F1/32'}, {'symbol': 'G06F2115/00', 'titleFull': 'Details relating to the type of the circuit'}, {'symbol': 'G06F2209/00', 'titleFull': 'Indexing scheme relating to G06F9/00'}, {'symbol': 'G06F2111/00', 'titleFull': 'Details relating to CAD techniques'}, {'symbol': 'G06F2206/00', 'titleFull': 'Indexing scheme related to dedicated interfaces for computers'}, {'symbol': 'G06F1/00', 'titleFull': 'Details not covered by groups G06F3/00 - G06F13/00 and G06F21/00'}], 'var_functions.query_db:76': 'file_storage/functions.query_db:76.json', 'var_functions.query_db:78': 'file_storage/functions.query_db:78.json', 'var_functions.query_db:80': 'file_storage/functions.query_db:80.json', 'var_functions.query_db:82': 'file_storage/functions.query_db:82.json'}

exec(code, env_args)
