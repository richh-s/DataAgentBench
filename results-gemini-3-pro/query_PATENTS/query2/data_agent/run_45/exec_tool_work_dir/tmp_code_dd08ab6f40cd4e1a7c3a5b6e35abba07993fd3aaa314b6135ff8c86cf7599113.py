code = """import json
import re
import pandas as pd

# Load data
with open(locals()['var_function-call-4625969505607778916'], 'r') as f:
    data = json.load(f)

# Helper for date parsing
def is_h2_2019(date_str):
    if not isinstance(date_str, str): return False
    # Check for 2019
    if '2019' not in date_str: return False
    # Check for H2 months
    h2_months = ['July', 'August', 'September', 'October', 'November', 'December', 
                 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # Simple check: month word in string. 
    # Risk: "January 2019" has no match. "July 2019" has match.
    # Risk: "3rd August 2021" has match 'August' but year is 2021.
    # We already checked '2019' is in string.
    # Case: "Granted in August 2019".
    # Case: "August 3rd, 2019".
    # Case: "14th Mar 2019" -> Mar (not H2).
    # Case: "2019, May 30th" -> May (not H2).
    # Case: "2019 on Nov 14th" -> Nov (H2).
    # But what if "August 2018"? '2019' not in string.
    # What if "August 2019"? '2019' in string and 'August' in string.
    # Edge case: "January 2019, cited August 2018". Unlikely in grant_date field.
    for m in h2_months:
        if m in date_str:
            return True
    return False

def get_filing_year(date_str):
    if not isinstance(date_str, str): return None
    match = re.search(r'\d{4}', date_str)
    if match:
        return int(match.group(0))
    return None

def is_germany(pat_info):
    if not isinstance(pat_info, str): return False
    # Look for DE- patterns or 'from DE' or 'In DE'
    if 'DE-' in pat_info: return True
    if 'from DE' in pat_info: return True
    if 'In DE' in pat_info: return True
    # Explicit check for Germany mentioned as country
    return False

# Filter and Process
rows = []
for entry in data:
    g_date = entry.get('grant_date', '')
    if not is_h2_2019(g_date):
        continue
    
    p_info = entry.get('Patents_info', '')
    if not is_germany(p_info):
        continue
    
    f_date = entry.get('filing_date', '')
    f_year = get_filing_year(f_date)
    if f_year is None:
        continue
        
    cpc_json = entry.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_json)
    except:
        continue
        
    # Extract unique Level 4 codes (first 3 chars)
    codes = set()
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 3:
            # Level 4 is usually Class (e.g., A01)
            l4 = code[:3]
            codes.add(l4)
            
    for c in codes:
        rows.append({'code': c, 'year': f_year})

df = pd.DataFrame(rows)

if df.empty:
    print("__RESULT__:")
    print("[]")
else:
    # Count filings per code per year
    counts = df.groupby(['code', 'year']).size().reset_index(name='count')
    
    # Calculate EMA
    # We need a continuous year range for each code to handle 0s correctly?
    # Or just iterate?
    # EMA formula: ema_t = alpha * count_t + (1-alpha) * ema_t-1
    # For missing years, count_t is 0.
    
    results = []
    
    # Get all unique codes
    unique_codes = counts['code'].unique()
    
    for code in unique_codes:
        code_data = counts[counts['code'] == code].sort_values('year')
        
        # Create full range of years from min to max (or specific range?)
        # Let's use min year in data to max year in data for this code
        min_y = code_data['year'].min()
        max_y = code_data['year'].max()
        all_years = range(min_y, max_y + 1)
        
        # Reindex
        code_data = code_data.set_index('year').reindex(all_years, fill_value=0)
        
        # Calculate EMA
        # Use pandas ewm
        # alpha = 0.1
        # adjust=False corresponds to the recursive formula: y_t = alpha*x_t + (1-alpha)*y_{t-1}
        # with y_0 = x_0 (if we start with the first value)
        code_data['ema'] = code_data['count'].ewm(alpha=0.1, adjust=False).mean()
        
        # Find best year
        best_row = code_data.loc[code_data['ema'].idxmax()]
        best_year = best_row.name
        max_ema = best_row['ema']
        
        results.append({
            'code': code,
            'best_year': int(best_year),
            'max_ema': max_ema
        })
        
    # Sort by max_ema desc? Or just return list?
    # User asks: "Find the CPC technology areas ... with the highest exponential moving average ... each year"
    # Actually, the user might want a list of areas.
    # I'll sort by max_ema descending to show the most prominent ones first.
    results.sort(key=lambda x: x['max_ema'], reverse=True)
    
    print("__RESULT__:")
    print(json.dumps(results))"""

env_args = {'var_function-call-18329779795316075067': 'file_storage/function-call-18329779795316075067.json', 'var_function-call-783895298076463904': [{'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.'}, {'Patents_info': 'In DE, the patent filing (application no. DE-102009032362-A) is owned by MARTOR KG and has pub. number DE-102009032362-B3.'}], 'var_function-call-11071387301097378258': [{'symbol': 'A01K2227/108', 'level': '9.0', 'titleFull': 'Swine', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]'}, {'symbol': 'A01K2227/105', 'level': '9.0', 'titleFull': 'Murine', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]'}, {'symbol': 'A01K2227/101', 'level': '9.0', 'titleFull': 'Bovine', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]'}, {'symbol': 'A01K2227/107', 'level': '9.0', 'titleFull': 'Rabbit', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]'}, {'symbol': 'A01K2227/103', 'level': '9.0', 'titleFull': 'Ovine', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]'}], 'var_function-call-1711144334646262674': [{'symbol': 'C01B', 'level': '5.0'}, {'symbol': 'C01B33/00', 'level': '7.0'}], 'var_function-call-7318353225580530694': [{'symbol': 'A', 'level': '2.0'}, {'symbol': 'A01', 'level': '4.0'}, {'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01B1/00', 'level': '7.0'}], 'var_function-call-13170260157125441038': [{'symbol': 'B04'}, {'symbol': 'B23'}, {'symbol': 'B30'}, {'symbol': 'B21'}, {'symbol': 'B25'}, {'symbol': 'B99'}, {'symbol': 'B29'}, {'symbol': 'B33'}, {'symbol': 'C22'}, {'symbol': 'D99'}], 'var_function-call-13084169619347489539': [{'COUNT(*)': '4833'}], 'var_function-call-4625969505607778916': 'file_storage/function-call-4625969505607778916.json'}

exec(code, env_args)
