code = """import json
import pandas as pd
import dateutil.parser
import re

# Load the data from the previous tool call
file_path = locals()['var_function-call-10653943689121975464']
with open(file_path, 'r') as f:
    data = json.load(f)

# Helper to parse natural language dates
def parse_date(date_str):
    try:
        # Clean up strings like "dated ", "on ", "of", "the"
        clean_str = re.sub(r'(dated|on|of|the|rd|th|st|nd)', '', date_str, flags=re.IGNORECASE)
        # Handle "2019, November 27" -> "2019 November 27"
        clean_str = clean_str.replace(',', ' ').strip()
        dt = dateutil.parser.parse(clean_str, fuzzy=True)
        return dt
    except:
        return None

# Filter and process
filtered_records = []
for entry in data:
    g_date_str = entry.get('grant_date', '')
    g_date = parse_date(g_date_str)
    
    # Check if grant date is in H2 2019
    if g_date and (pd.Timestamp('2019-07-01') <= g_date <= pd.Timestamp('2019-12-31')):
        f_date_str = entry.get('filing_date', '')
        f_date = parse_date(f_date_str)
        if f_date:
            filing_year = f_date.year
            
            # Extract CPC codes (Level 4 = first 3 chars)
            cpc_json = entry.get('cpc', '[]')
            try:
                cpc_list = json.loads(cpc_json)
                # Get unique level 4 codes for this patent
                codes = set()
                for c in cpc_list:
                    code_str = c.get('code', '')
                    if len(code_str) >= 3:
                        codes.add(code_str[:3])
                
                for code in codes:
                    filtered_records.append({'cpc': code, 'filing_year': filing_year})
            except:
                pass

df = pd.DataFrame(filtered_records)

# Check if dataframe is empty
if df.empty:
    print('__RESULT__:')
    print(json.dumps([]))
else:
    # Count filings per CPC per year
    counts = df.groupby(['cpc', 'filing_year']).size().reset_index(name='count')
    
    results = []
    # For each CPC, calculate EMA
    for cpc_code, group in counts.groupby('cpc'):
        # Create full range of years for this CPC (from min to max in the data? or min to max of this group?)
        # Usually, EMA requires a continuous time series.
        # Let's use the min and max filing years present in the specific group.
        min_year = group['filing_year'].min()
        max_year = group['filing_year'].max()
        all_years = pd.DataFrame({'filing_year': range(min_year, max_year + 1)})
        
        merged = pd.merge(all_years, group, on='filing_year', how='left').fillna(0)
        
        # Calculate EMA
        # Smoothing factor 0.1
        merged['ema'] = merged['count'].ewm(alpha=0.1, adjust=False).mean()
        
        # Find best year (max EMA)
        best_idx = merged['ema'].idxmax()
        best_year = merged.loc[best_idx, 'filing_year']
        max_ema = merged.loc[best_idx, 'ema']
        
        results.append({
            'cpc_code': cpc_code,
            'best_year': int(best_year),
            'max_ema': float(max_ema)
        })

    # Sort by max_ema descending
    results.sort(key=lambda x: x['max_ema'], reverse=True)
    
    print('__RESULT__:')
    print(json.dumps(results))"""

env_args = {'var_function-call-14791997855874567430': 'file_storage/function-call-14791997855874567430.json', 'var_function-call-1357772695752790823': [{'count(*)': '171'}], 'var_function-call-1357772695752791016': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-10653943689121975751': [{'symbol': 'A', 'level': '2.0', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'A01', 'level': '4.0', 'titleFull': 'AGRICULTURE; FORESTRY; ANIMAL HUSBANDRY; HUNTING; TRAPPING; FISHING'}, {'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'A01B1/00', 'level': '7.0', 'titleFull': 'Hand tools'}], 'var_function-call-10653943689121975464': 'file_storage/function-call-10653943689121975464.json'}

exec(code, env_args)
