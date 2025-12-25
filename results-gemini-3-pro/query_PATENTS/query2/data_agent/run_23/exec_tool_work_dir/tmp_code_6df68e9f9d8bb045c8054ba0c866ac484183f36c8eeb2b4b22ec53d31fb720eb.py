code = """import json
import pandas as pd
import re

# Load data
file_path = locals()['var_function-call-13601185424003768990']
with open(file_path, 'r') as f:
    data = json.load(f)

# Helper to parse date
def parse_date_str(date_str):
    if not date_str:
        return None
    # Remove common prefixes
    clean_str = date_str.lower().replace('dated', '').replace('on', '').replace('the', '').replace(',', '').strip()
    # Try pandas
    try:
        return pd.to_datetime(clean_str)
    except:
        # Fallback regex for Year
        match = re.search(r'\d{4}', clean_str)
        if match:
            return pd.to_datetime(match.group(0), format='%Y')
        return None

# Filter and process
counts = {} # {code: {year: count}}

start_date = pd.Timestamp('2019-07-01')
end_date = pd.Timestamp('2019-12-31')

for row in data:
    # Check grant date
    g_date = parse_date_str(row.get('grant_date'))
    if g_date is None or pd.isna(g_date):
        continue
    
    if start_date <= g_date <= end_date:
        # Check filing date
        f_date = parse_date_str(row.get('filing_date'))
        if f_date is None or pd.isna(f_date):
            continue
        
        f_year = f_date.year
        
        # Parse CPC
        cpc_json = row.get('cpc')
        if not cpc_json:
            continue
        try:
            cpc_list = json.loads(cpc_json)
        except:
            continue
            
        # Extract Level 4 codes (Class: first 3 chars)
        codes = set()
        for item in cpc_list:
            code = item.get('code', '')
            if len(code) >= 3:
                # Class is usually first 3 chars (e.g. H01)
                # Verify if it's alphanumeric? Usually yes.
                lvl4 = code[:3]
                codes.add(lvl4)
        
        for code in codes:
            if code not in counts:
                counts[code] = {}
            counts[code][f_year] = counts[code].get(f_year, 0) + 1

# Calculate EMA
results = []
smoothing = 0.1

for code, year_counts in counts.items():
    if not year_counts:
        continue
    
    years = sorted(year_counts.keys())
    min_year = years[0]
    max_year = years[-1]
    
    # Build full series
    full_years = range(min_year, max_year + 1)
    series = [year_counts.get(y, 0) for y in full_years]
    
    # Calculate EMA
    # Pandas ewm
    # adjust=False => y_t = alpha*x_t + (1-alpha)*y_{t-1}
    # span implies alpha=2/(span+1). We have alpha=0.1 explicitly.
    # So we use com or alpha directly.
    
    df_series = pd.Series(series, index=full_years)
    ema_series = df_series.ewm(alpha=smoothing, adjust=False).mean()
    
    max_ema = ema_series.max()
    best_year = ema_series.idxmax()
    
    results.append({
        "code": code,
        "max_ema": max_ema,
        "best_year": int(best_year)
    })

# Sort by max_ema desc
results.sort(key=lambda x: x['max_ema'], reverse=True)

# Keep top results (maybe top 20 or so to verify, or all if feasible)
# The user wants "Find the CPC technology areas ...". 
# I'll return the top 50 codes to get titles for.
top_results = results[:50]

print("__RESULT__:")
print(json.dumps(top_results))"""

env_args = {'var_function-call-16016236543642685128': 'file_storage/function-call-16016236543642685128.json', 'var_function-call-16016236543642684803': [{'symbol': 'A01K2227/108', 'level': '9.0', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'level': '9.0', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'level': '9.0', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'level': '9.0', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'level': '9.0', 'titleFull': 'Ovine'}], 'var_function-call-13561635954094791069': [{'cpc': '[\n  {\n    "code": "Y10S439/909",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y10S439/909",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01R13/631",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01R13/5224",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01R13/5224",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01R13/631",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'dated 7th October 2004', 'filing_date': 'dated 9th April 2003', 'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.'}], 'var_function-call-13561635954094789046': [{'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'A01B13/00', 'level': '7.0', 'titleFull': 'Ploughs or like machines for special purposes ; Ditch diggers, trench ploughs, forestry ploughs, ploughs for land or marsh reclamation'}, {'symbol': 'A01B35/00', 'level': '7.0', 'titleFull': 'Other machines for working soil not specially adapted for working soil on which crops are growing'}, {'symbol': 'A01B59/00', 'level': '7.0', 'titleFull': 'Devices specially adapted for connection between animals or tractors and agricultural machines or implements'}, {'symbol': 'A01B67/00', 'level': '7.0', 'titleFull': 'Devices for controlling the tractor motor by resistance of tools'}], 'var_function-call-317795769849267931': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-16573650118009255803': [{'symbol': 'H', 'level': '2.0'}, {'symbol': 'H01', 'level': '4.0'}, {'symbol': 'H01R', 'level': '5.0'}, {'symbol': 'H01R13/631', 'level': '10.0'}], 'var_function-call-13601185424003768990': 'file_storage/function-call-13601185424003768990.json'}

exec(code, env_args)
