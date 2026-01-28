code = """import json
import pandas as pd

# Load the patent data
patent_file = locals()['var_functions.query_db:4']
with open(patent_file, 'r') as f:
    patent_data = json.load(f)

# Load the CPC level 5 data
cpc_file = locals()['var_functions.query_db:11']
with open(cpc_file, 'r') as f:
    cpc_level5 = json.load(f)

# Create set of valid level 5 CPC codes for fast lookup
level5_codes = {item['symbol'] for item in cpc_level5}

# Debug: print some sample CPC codes from patents and level5 codes
sample_patents = patent_data[:5]
sample_cpc_codes = []
for patent in sample_patents:
    cpc_str = patent.get('cpc', '')
    if cpc_str:
        try:
            cpc_list = json.loads(cpc_str)
            for cpc_item in cpc_list:
                sample_cpc_codes.append(cpc_item.get('code', ''))
        except:
            pass

# Function to parse publication date
month_map = {
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
    'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
}

def parse_date(date_str):
    if not date_str or date_str == '':
        return None
    try:
        # Format: "Aug 3rd, 2021" or "Oct 6th, 2020"
        parts = date_str.split()
        if len(parts) >= 3:
            month = parts[0]
            year = parts[-1]
            if month in month_map and year.isdigit():
                return int(year)
    except:
        pass
    return None

# Extract subclass-level CPC codes and years from patents
patent_records = []
for patent in patent_data:
    pub_date = patent.get('publication_date', '')
    year = parse_date(pub_date)
    if not year:
        continue
    
    cpc_str = patent.get('cpc', '')
    if not cpc_str or cpc_str == '':
        continue
    
    try:
        cpc_list = json.loads(cpc_str)
        for cpc_item in cpc_list:
            code = cpc_item.get('code', '')
            if code:
                # Extract subclass part (letters + first set of digits)
                # For "C01B33/00", extract "C01B"
                # For "H01M10/0565", extract "H01M"
                import re
                match = re.search(r'^([A-Z]\d{2}[A-Z])', code)
                if not match:
                    match = re.search(r'^([A-Z]\d{2}[A-Z]\d{2})', code)
                
                if match:
                    subclass = match.group(1)
                    # Check if it's a level 5 code
                    if subclass in level5_codes:
                        patent_records.append({
                            'cpc_subclass': subclass,
                            'year': year,
                            'full_code': code
                        })
    except:
        continue

print('__RESULT__:')
print(json.dumps({
    'sample_cpc_from_patents': sample_cpc_codes[:20],
    'sample_level5_codes': list(level5_codes)[:20],
    'total_patents_processed': len(patent_data),
    'valid_records': len(patent_records),
    'sample_records': patent_records[:10]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:12': {'total_patents_processed': 277813, 'valid_records': 0, 'sample_records': []}}

exec(code, env_args)
