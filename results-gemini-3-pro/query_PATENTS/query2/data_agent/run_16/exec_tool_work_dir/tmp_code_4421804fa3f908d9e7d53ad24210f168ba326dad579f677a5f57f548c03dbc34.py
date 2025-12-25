code = """import json
import re
from collections import defaultdict

# Paths provided in storage
patents_file = locals()['var_function-call-4468695718563702582']
definitions_file = locals()['var_function-call-4933460451412689560']

# Load Definitions
with open(definitions_file, 'r') as f:
    definitions_data = json.load(f)

# Map Level 4 symbol to Title
cpc_titles = {item['symbol']: item['titleFull'] for item in definitions_data}

# Load Patents
with open(patents_file, 'r') as f:
    patents_data = json.load(f)

# Helper to parse dates
# Formats: "3rd August 2021", "dated 6th October 2020", "21st of September, 2021", "August the 29th, 2019"
# "14th Mar 2019", "2013, June 17th", "on December 15th, 2015"
months = {
    'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,
    'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12,
    'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'jun': 6, 'jul': 7, 'aug': 8, 'sep': 9, 'sept': 9, 'oct': 10, 'nov': 11, 'dec': 12
}

def parse_date_get_year_month(d_str):
    try:
        # Normalize
        s = d_str.lower().replace(',', ' ').replace('dated', '').replace('on', '').replace('of', '').replace('the', '')
        # Remove ordinals st, nd, rd, th
        s = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', s)
        parts = s.split()
        
        day = None
        month = None
        year = None
        
        for p in parts:
            if p.isdigit():
                val = int(p)
                if val > 1900:
                    year = val
                elif val <= 31:
                    day = val
            elif p in months:
                month = months[p]
        
        if year and month:
            return year, month
        return None
    except:
        return None

def parse_year(d_str):
    ym = parse_date_get_year_month(d_str)
    if ym:
        return ym[0]
    return None

# Aggregation
cpc_filing_counts = defaultdict(lambda: defaultdict(int)) # cpc -> year -> count
all_years = set()

for row in patents_data:
    g_date = row.get('grant_date', '')
    ym = parse_date_get_year_month(g_date)
    
    # Filter Grant Date: H2 2019 (Year 2019, Month >= 7)
    if ym and ym[0] == 2019 and ym[1] >= 7:
        # Valid patent
        f_date = row.get('filing_date', '')
        f_year = parse_year(f_date)
        
        if f_year:
            # Extract CPC
            try:
                cpc_list = json.loads(row.get('cpc', '[]'))
                # Get unique Level 4 codes
                l4_codes = set()
                for item in cpc_list:
                    code = item.get('code', '')
                    if len(code) >= 3:
                        l4 = code[:3]
                        # Verify if it is a valid Level 4 key (optional, but good)
                        if l4 in cpc_titles:
                            l4_codes.add(l4)
                
                # Count
                for code in l4_codes:
                    cpc_filing_counts[code][f_year] += 1
                    all_years.add(f_year)
            except:
                pass

if not all_years:
    print("__RESULT__:")
    print("[]")
    exit()

min_year = min(all_years)
max_year = max(all_years)
years_range = list(range(min_year, max_year + 1))

results = []

for cpc, counts in cpc_filing_counts.items():
    # Calculate EMA
    ema_series = []
    
    # Initialize
    # Value for min_year
    val_0 = counts.get(years_range[0], 0)
    ema_series.append(val_0)
    
    max_ema = val_0
    best_year = years_range[0]
    
    for i in range(1, len(years_range)):
        y = years_range[i]
        count = counts.get(y, 0)
        # EMA_t = 0.1 * Count + 0.9 * EMA_{t-1}
        prev_ema = ema_series[-1]
        new_ema = 0.1 * count + 0.9 * prev_ema
        ema_series.append(new_ema)
        
        if new_ema > max_ema:
            max_ema = new_ema
            best_year = y
            
    # Also check if the first year was the max (already set)
    
    title = cpc_titles.get(cpc, "Unknown")
    
    results.append({
        "full title": title,
        "CPC group code": cpc,
        "best year": best_year,
        "max_ema": max_ema # For sorting/checking
    })

# The query phrasing "Find the CPC technology areas ... with the highest exponential moving average ... each year"
# is ambiguous. I will sort by max_ema descending to show the "highest" areas first.
results.sort(key=lambda x: x['max_ema'], reverse=True)

# Format for output (exclude max_ema if not requested, but I'll keep it clean)
final_output = []
for r in results:
    final_output.append({
        "full title": r['full title'],
        "CPC group code": r['CPC group code'],
        "best year": r['best year']
    })

print("__RESULT__:")
print(json.dumps(final_output))"""

env_args = {'var_function-call-6833142422007582779': 'file_storage/function-call-6833142422007582779.json', 'var_function-call-6833142422007583338': [{'symbol': 'A01K2227/108', 'level': '9.0', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'level': '9.0', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'level': '9.0', 'titleFull': 'Bovine'}], 'var_function-call-17534221550273436220': [{'COUNT(*)': '277813'}], 'var_function-call-14511499758726772371': [{'Patents_info': 'The US patent application (no. US-201916389545-A) is assigned to MODERNATX INC and has pub. number US-10695419-B2.'}, {'Patents_info': 'Application (ID US-201916412740-A) from US, assigned to LEGACY RES AND DEVELOPMENT GROUP LLC, with publication no. US-10898606-B2.'}, {'Patents_info': 'TANDEM DIABETES CARE INC holds the US patent filing (app. number US-201916444452-A), with publication number US-10918785-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916560126-A) is belonging to DENSO CORP and has pub. number US-10897184-B2.'}, {'Patents_info': 'The US patent filing (app. number US-201916584394-A) is owned by DEPUY SYNTHES PRODUCTS INC and has publication no. US-11911287-B2.'}], 'var_function-call-6146513652087149824': [{'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.'}, {'Patents_info': 'Patent application (no. DE-102015114819-A) from DE, held by ROCKWELL COLLINS DEUTSCHLAND GMBH, with pub. number DE-102015114819-B3.'}, {'Patents_info': 'Application (no. DE-10127786-A) from DE, belonging to KRAHFORST JUERGEN, with pub. number DE-10127786-B4.'}, {'Patents_info': 'Patent filing (application no. DE-10200192-A) from DE, held by COPERION GMBH, with publication no. DE-10200192-B4.'}, {'Patents_info': 'Patent filing (application no. DE-10201217-A) from DE, assigned to NEUBAUER KURT MASCHF, with publication no. DE-10201217-B4.'}], 'var_function-call-17543357168241398586': [{'symbol': 'C01B33/00', 'level': '7.0', 'titleFull': 'Silicon; Compounds thereof'}], 'var_function-call-8922638722301088516': [{'parents': '[\n  "C01B",\n  "C01",\n  "C"\n]'}], 'var_function-call-4642165689100570418': [{'symbol': 'C01B', 'level': '5.0'}], 'var_function-call-17553871321314445393': [{'symbol': 'C', 'level': '2.0'}, {'symbol': 'C01', 'level': '4.0'}], 'var_function-call-2162445816587743607': [{'symbol': 'B04'}, {'symbol': 'B23'}, {'symbol': 'B30'}, {'symbol': 'B21'}, {'symbol': 'B25'}, {'symbol': 'B99'}, {'symbol': 'B29'}, {'symbol': 'B33'}, {'symbol': 'C22'}, {'symbol': 'D99'}], 'var_function-call-44325647844237237': [], 'var_function-call-4468695718563702582': 'file_storage/function-call-4468695718563702582.json', 'var_function-call-4933460451412689560': 'file_storage/function-call-4933460451412689560.json'}

exec(code, env_args)
