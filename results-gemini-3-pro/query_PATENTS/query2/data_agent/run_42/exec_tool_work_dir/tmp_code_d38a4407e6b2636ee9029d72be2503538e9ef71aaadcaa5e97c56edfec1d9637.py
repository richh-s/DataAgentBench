code = """import json
import pandas as pd
from datetime import datetime

# Load data
# The result is stored in 'var_function-call-8210490788658783622' which is a file path
file_path = locals()['var_function-call-8210490788658783622']
with open(file_path, 'r') as f:
    records = json.load(f)

# Helper to parse date
def parse_date(date_str):
    if not date_str:
        return None
    # Remove 'dated ', 'on ', 'of ' to clean up
    clean = date_str.replace('dated ', '').replace('on ', '').replace('of ', '').replace(',', '').strip()
    # clean might be "5th March 2019", "2013 June 17th", "July 21st 2014"
    # Handling ordinal suffixes st, nd, rd, th
    # Regex might be better, or just removing them
    for suffix in ['st', 'nd', 'rd', 'th']:
        clean = clean.replace(suffix, '')
    
    # Try formats
    formats = [
        "%d %B %Y", "%B %d %Y", "%Y %B %d", 
        "%d %b %Y", "%b %d %Y", "%Y %b %d"
    ]
    for fmt in formats:
        try:
            return datetime.strptime(clean, fmt)
        except ValueError:
            continue
    return None

# Filter and Extract
filtered_data = []
for r in records:
    # Grant Date
    g_date = parse_date(r['grant_date'])
    if not g_date:
        continue
    # Filter H2 2019
    if not (g_date.year == 2019 and g_date.month >= 7):
        continue
    
    # Filing Date -> Year
    f_date = parse_date(r['filing_date'])
    if not f_date:
        continue
    year = f_date.year
    
    # CPC Codes
    try:
        cpc_list = json.loads(r['cpc'])
    except:
        continue
        
    # Extract unique Class codes (3 chars)
    codes = set()
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 3:
            codes.add(code[:3]) # Level 4 is Class (3 chars e.g. A01)
            
    for c in codes:
        filtered_data.append({'year': year, 'cpc': c})

# Create DataFrame
df = pd.DataFrame(filtered_data)

if df.empty:
    print('__RESULT__:')
    print(json.dumps([]))
else:
    # Aggregation: Count filings per year per CPC
    counts = df.groupby(['cpc', 'year']).size().reset_index(name='count')
    
    # Fill missing years?
    # EMA needs continuous time series usually? Or just over the years present?
    # "EMA of patent filings each year". Implicitly assumes a time series.
    # If a year is missing, count is 0.
    # Range of years: min to max in data
    min_year = counts['year'].min()
    max_year = counts['year'].max()
    all_years = range(min_year, max_year + 1)
    
    # Reindex for each CPC
    full_df_list = []
    unique_cpcs = counts['cpc'].unique()
    
    for cpc in unique_cpcs:
        cpc_df = counts[counts['cpc'] == cpc].set_index('year')
        cpc_df = cpc_df.reindex(all_years, fill_value=0).reset_index().rename(columns={'index': 'year'})
        cpc_df['cpc'] = cpc
        
        # Calculate EMA
        # alpha = 0.1
        # pandas ewm: alpha=0.1, adjust=False (EMA_t = alpha*x_t + (1-alpha)*EMA_{t-1})
        cpc_df['ema'] = cpc_df['count'].ewm(alpha=0.1, adjust=False).mean()
        full_df_list.append(cpc_df)
        
    full_df = pd.concat(full_df_list, ignore_index=True)
    
    # "Find the CPC technology areas ... with the highest ... each year"
    # For each year, find CPC with max EMA
    top_per_year = full_df.loc[full_df.groupby('year')['ema'].idxmax()]
    
    # We need "Include the full title, CPC group code, and the best year for each CPC group"
    # The groups are the ones identified in `top_per_year`.
    unique_top_cpcs = top_per_year['cpc'].unique()
    
    # For each unique top CPC, find its best year (max EMA)
    results = []
    for cpc in unique_top_cpcs:
        cpc_rows = full_df[full_df['cpc'] == cpc]
        best_row = cpc_rows.loc[cpc_rows['ema'].idxmax()]
        results.append({
            'cpc_group': cpc,
            'best_year': int(best_row['year']),
            'max_ema': float(best_row['ema'])
        })
        
    print('__RESULT__:')
    print(json.dumps(results))"""

env_args = {'var_function-call-9349135532436099927': 'file_storage/function-call-9349135532436099927.json', 'var_function-call-7996704792418014537': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-135606811111269997': [{'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'A01B59/00', 'level': '7.0', 'titleFull': 'Devices specially adapted for connection between animals or tractors and agricultural machines or implements'}, {'symbol': 'A01B19/00', 'level': '7.0', 'titleFull': 'Harrows with non-rotating tools'}, {'symbol': 'A01B35/00', 'level': '7.0', 'titleFull': 'Other machines for working soil not specially adapted for working soil on which crops are growing'}, {'symbol': 'A01B13/00', 'level': '7.0', 'titleFull': 'Ploughs or like machines for special purposes ; Ditch diggers, trench ploughs, forestry ploughs, ploughs for land or marsh reclamation'}], 'var_function-call-14112593806741946107': [{'symbol': 'A01B1/00', 'level': '7.0'}, {'symbol': 'A', 'level': '2.0'}, {'symbol': 'A01', 'level': '4.0'}, {'symbol': 'A01B', 'level': '5.0'}], 'var_function-call-18427524461417541909': [{'Patents_info': 'In AT, the patent filing (application no. AT-52022-U) is assigned to ST Extruded Products Germany GmbH and has publication no. AT-17758-U1.'}, {'Patents_info': 'Application (no. AU-2006246481-A) from AU, belonging to KAO GERMANY GMBH, with pub. number AU-2006246481-B2.'}, {'Patents_info': 'TRELLEBORG AUTOMOTIVE GERMANY holds the PL patent application (number PL-07728345-T), with publication no. PL-2010798-T3.'}, {'Patents_info': 'The DE application (number DE-102008034343-A) is assigned to CONTINENTAL MECH COMPONENTS GERMANY GMBH and has pub. number DE-102008034343-B4.'}, {'Patents_info': 'In EP, the application (ID EP-18829350-A) is belonging to MEYER BURGER GERMANY GMBH and has pub. number EP-3729486-C0.'}], 'var_function-call-8210490788658783622': 'file_storage/function-call-8210490788658783622.json'}

exec(code, env_args)
