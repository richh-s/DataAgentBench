code = """import json
import re
import pandas as pd

# Load data
file_path = locals()['var_function-call-13020009233019568097']
with open(file_path, 'r') as f:
    data = json.load(f)

# H2 2019 months
h2_months = ['july', 'august', 'september', 'october', 'november', 'december', 
             'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

# Helper to check H2 2019
def is_h2_2019(date_str):
    date_str = date_str.lower()
    if '2019' not in date_str:
        return False
    # Check if any H2 month is present
    for m in h2_months:
        if m in date_str:
            return True
    return False

# Helper to check Germany
def is_germany(info_str):
    # Check for DE country code in typical positions
    # "from DE", "application ... DE-", "publication ... DE-"
    # "assigned to ... Germany"
    if 'DE-' in info_str:
        return True
    if re.search(r'\bfrom DE\b', info_str):
        return True
    if re.search(r'\bGermany\b', info_str, re.IGNORECASE):
        return True
    return False

# Helper to extract filing year
def get_filing_year(date_str):
    # Find 4 digits
    match = re.search(r'\d{4}', date_str)
    if match:
        return int(match.group(0))
    return None

# Process
filtered_cpc_years = []

for row in data:
    if not is_h2_2019(row['grant_date']):
        continue
    if not is_germany(row['Patents_info']):
        continue
    
    f_year = get_filing_year(row['filing_date'])
    if f_year is None:
        continue
    
    # Extract CPC
    try:
        cpcs = json.loads(row['cpc'])
        # Get unique Level 4 codes for this patent
        codes = set()
        for c in cpcs:
            code = c.get('code', '')
            if len(code) >= 3:
                l4 = code[:3]
                codes.add(l4)
        
        for code in codes:
            filtered_cpc_years.append({'cpc': code, 'year': f_year})
            
    except:
        continue

# Create DataFrame
df = pd.DataFrame(filtered_cpc_years)

if df.empty:
    print("__RESULT__:")
    print(json.dumps({"error": "No data found"}))
else:
    # Count per CPC per Year
    counts = df.groupby(['cpc', 'year']).size().reset_index(name='count')
    
    # Calculate EMA
    # Sort by year
    results = []
    unique_cpcs = counts['cpc'].unique()
    
    for cpc in unique_cpcs:
        cpc_data = counts[counts['cpc'] == cpc].sort_values('year')
        
        # Fill missing years?
        # EMA usually requires continuous time series.
        # But here we only have filings for the *granted set*.
        # If we want EMA of *filings*, we should consider that the filings of the granted patents are just a subset.
        # However, "exponential moving average of patent filings each year" implies we treat the count of filings (of these eventually granted patents) as the time series.
        # We should fill missing years with 0 if we assume a continuous timeline from min to max year.
        min_year = cpc_data['year'].min()
        max_year = cpc_data['year'].max()
        all_years = range(min_year, max_year + 1)
        cpc_data = cpc_data.set_index('year').reindex(all_years, fill_value=0).reset_index()
        cpc_data = cpc_data.rename(columns={'index': 'year'})
        
        # Calculate EMA
        # alpha = 0.1
        cpc_data['ema'] = cpc_data['count'].ewm(alpha=0.1, adjust=False).mean()
        
        # Find max EMA
        best_row = cpc_data.loc[cpc_data['ema'].idxmax()]
        
        results.append({
            'cpc': cpc,
            'best_year': int(best_row['year']),
            'max_ema': float(best_row['ema'])
        })
    
    # Sort by max_ema descending
    results.sort(key=lambda x: x['max_ema'], reverse=True)
    
    # Top 20
    top_results = results[:20]
    
    print("__RESULT__:")
    print(json.dumps(top_results))"""

env_args = {'var_function-call-10046613690508653826': 'file_storage/function-call-10046613690508653826.json', 'var_function-call-10046613690508653035': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}], 'var_function-call-5063788461440302350': [{'symbol': 'A', 'level': '2.0', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'A01', 'level': '4.0', 'titleFull': 'AGRICULTURE; FORESTRY; ANIMAL HUSBANDRY; HUNTING; TRAPPING; FISHING'}, {'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'A01B1/00', 'level': '7.0', 'titleFull': 'Hand tools'}], 'var_function-call-5063788461440299145': [{'Patents_info': 'In AT, the patent filing (application no. AT-52022-U) is assigned to ST Extruded Products Germany GmbH and has publication no. AT-17758-U1.'}, {'Patents_info': 'Application (no. AU-2006246481-A) from AU, belonging to KAO GERMANY GMBH, with pub. number AU-2006246481-B2.'}, {'Patents_info': 'TRELLEBORG AUTOMOTIVE GERMANY holds the PL patent application (number PL-07728345-T), with publication no. PL-2010798-T3.'}, {'Patents_info': 'The DE application (number DE-102008034343-A) is assigned to CONTINENTAL MECH COMPONENTS GERMANY GMBH and has pub. number DE-102008034343-B4.'}, {'Patents_info': 'In EP, the application (ID EP-18829350-A) is belonging to MEYER BURGER GERMANY GMBH and has pub. number EP-3729486-C0.'}], 'var_function-call-4315669850520866024': [{'symbol': 'B21'}, {'symbol': 'B25'}, {'symbol': 'B99'}, {'symbol': 'B29'}, {'symbol': 'B33'}, {'symbol': 'C22'}, {'symbol': 'D99'}, {'symbol': 'F28'}, {'symbol': 'A45'}, {'symbol': 'A24'}], 'var_function-call-13020009233019568097': 'file_storage/function-call-13020009233019568097.json'}

exec(code, env_args)
