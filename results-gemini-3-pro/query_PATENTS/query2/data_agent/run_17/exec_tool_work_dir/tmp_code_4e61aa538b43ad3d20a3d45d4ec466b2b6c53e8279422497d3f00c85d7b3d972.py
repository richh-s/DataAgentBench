code = """import json
import pandas as pd
import dateutil.parser

# Load data
filename = locals()['var_function-call-2484461217034850947']
with open(filename, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse Dates
def parse_date(d_str):
    if not d_str: return None
    # Clean string
    d_str = d_str.replace('dated ', '').replace('on ', '').replace('of ', '').replace(',', '')
    # Remove ordinal suffixes st, nd, rd, th
    # Simple regex to remove st/nd/rd/th attached to digits
    # But dateutil might handle it? Let's try pd.to_datetime first with fuzzy logic or custom.
    # Manual cleanup of ordinals: "1st", "2nd", "3rd", "4th" ... "31st"
    # Regex replacement for \d+(st|nd|rd|th)
    import re
    d_str = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', d_str)
    try:
        return pd.to_datetime(d_str)
    except:
        return None

df['grant_dt'] = df['grant_date'].apply(parse_date)
df['filing_dt'] = df['filing_date'].apply(parse_date)

# Filter for Granted in H2 2019
start_date = pd.Timestamp('2019-07-01')
end_date = pd.Timestamp('2019-12-31')

filtered = df[(df['grant_dt'] >= start_date) & (df['grant_dt'] <= end_date)].copy()

print(f"DEBUG: Found {len(filtered)} patents granted in H2 2019 in Germany.")

if len(filtered) == 0:
    print("__RESULT__:")
    print(json.dumps([]))
else:
    # Process CPC
    cpc_year_list = []
    
    for _, row in filtered.iterrows():
        f_year = row['filing_dt'].year
        if pd.isna(f_year): continue
        
        cpc_json = row['cpc']
        try:
            cpc_list = json.loads(cpc_json)
            # Extract Level 4 codes (first 3 chars)
            codes = set()
            for item in cpc_list:
                code = item.get('code', '')
                if len(code) >= 3:
                    # Level 4 is usually Class, e.g. A01.
                    # Codes are like "C01B33/00". First 3 chars = "C01"
                    l4 = code[:3]
                    codes.add(l4)
            
            for c in codes:
                cpc_year_list.append({'cpc': c, 'year': f_year})
        except:
            continue

    if not cpc_year_list:
        print("__RESULT__:")
        print(json.dumps([]))
    else:
        df_cpc = pd.DataFrame(cpc_year_list)
        
        # Count filings per year per CPC
        counts = df_cpc.groupby(['cpc', 'year']).size().reset_index(name='count')
        
        # Pivot to have years as index (or process per group)
        # To calculate EMA properly, we should fill missing years?
        # "Moving average ... each year". 
        # Let's pivot: Index=Year, Columns=CPC
        pivot = counts.pivot(index='year', columns='cpc', values='count').fillna(0)
        
        # Reindex to fill gaps in years
        min_year = int(pivot.index.min())
        max_year = int(pivot.index.max())
        all_years = range(min_year, max_year + 1)
        pivot = pivot.reindex(all_years, fill_value=0)
        
        # Calculate EMA
        # smoothing factor 0.1 corresponds to alpha=0.1
        ema = pivot.ewm(alpha=0.1, adjust=False).mean()
        
        # Find best year for each CPC
        # idxmax returns the index (Year) where max value occurs
        best_years = ema.idxmax()
        max_values = ema.max()
        
        results = []
        for cpc_code in best_years.index:
            results.append({
                'cpc': cpc_code,
                'best_year': int(best_years[cpc_code]),
                'max_ema': float(max_values[cpc_code])
            })
            
        # Sort by max_ema descending? Not requested but good.
        results.sort(key=lambda x: x['max_ema'], reverse=True)
        
        print("__RESULT__:")
        print(json.dumps(results))"""

env_args = {'var_function-call-10234011104391041875': 'file_storage/function-call-10234011104391041875.json', 'var_function-call-10234011104391044260': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}], 'var_function-call-2338280954461880606': [{'symbol': 'A', 'level': '2.0', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'A01', 'level': '4.0', 'titleFull': 'AGRICULTURE; FORESTRY; ANIMAL HUSBANDRY; HUNTING; TRAPPING; FISHING'}, {'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'C01B33/00', 'level': '7.0', 'titleFull': 'Silicon; Compounds thereof'}], 'var_function-call-2338280954461884025': [{'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.', 'grant_date': 'dated 7th October 2004'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.', 'grant_date': '2006 on Apr 27th'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.', 'grant_date': 'Nov 29th, 2007'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.', 'grant_date': '2009, January 29th'}, {'Patents_info': 'In DE, the patent filing (application no. DE-102009032362-A) is owned by MARTOR KG and has pub. number DE-102009032362-B3.', 'grant_date': '17th Jun 2010'}], 'var_function-call-2484461217034850947': 'file_storage/function-call-2484461217034850947.json'}

exec(code, env_args)
