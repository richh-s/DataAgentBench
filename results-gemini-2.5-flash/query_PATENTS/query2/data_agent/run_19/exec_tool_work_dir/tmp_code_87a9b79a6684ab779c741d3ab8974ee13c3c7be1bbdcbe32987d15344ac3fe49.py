code = """import json
import pandas as pd
from datetime import datetime

with open(locals()['var_function-call-2218518486593243679'], 'r') as f:
    publication_data = json.load(f)

# Function to parse natural language date
def parse_date(date_str):
    if not isinstance(date_str, str):
        return None
    date_str = date_str.lower().replace("dated ", "").replace("the ", "").replace(",", "")
    
    # Common month names and their numerical representation
    month_map = {
        "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
        "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12
    }

    # Extract year, month, day
    try:
        parts = date_str.split()
        year = int(parts[-1])
        month_name = None
        day = 1 # Default day if not found
        for part in parts:
            if part in month_map:
                month_name = part
            elif part.isdigit() or (len(part) > 0 and part[:-2].isdigit() and part.endswith(("st", "nd", "rd", "th"))):
                try:
                    day = int(part.replace("st", "").replace("nd", "").replace("rd", "").replace("th", ""))
                except ValueError:
                    pass
        
        if month_name and year:
            month = month_map[month_name]
            # Basic validation for day
            if not (1 <= day <= 31):
                day = 1 # Reset to 1 if invalid
            return datetime(year, month, day)
    except Exception:
        return None
    return None

# Function to extract country code from Patents_info
def extract_country_code(patents_info):
    if not isinstance(patents_info, str):
        return None
    if "publication no. US-" in patents_info:
        return "US"
    if "publication no. DE-" in patents_info:
        return "DE"
    if "(ID US-" in patents_info:
        return "US"
    if "(ID DE-" in patents_info:
        return "DE"
    
    # Fallback to look for country codes after "ID" or "publication no." or similar patterns
    import re
    match = re.search(r'(?:ID|publication no\.)\s*([A-Z]{2})-', patents_info)
    if match:
        return match.group(1)
    
    return None


filtered_patents = []
for record in publication_data:
    grant_date_str = record.get('grant_date')
    filing_date_str = record.get('filing_date')
    patents_info = record.get('Patents_info')
    cpc_json = record.get('cpc')

    grant_date = parse_date(grant_date_str)
    filing_date = parse_date(filing_date_str)
    country_code = extract_country_code(patents_info)

    if grant_date and filing_date and country_code == 'DE' and \
       datetime(2019, 7, 1) <= grant_date <= datetime(2019, 12, 31):
        
        try:
            cpc_list = json.loads(cpc_json)
            for cpc_entry in cpc_list:
                cpc_code = cpc_entry.get('code')
                if cpc_code:
                    filtered_patents.append({
                        'cpc_code': cpc_code,
                        'filing_year': filing_date.year
                    })
        except json.JSONDecodeError:
            continue

df_patents = pd.DataFrame(filtered_patents)

# Extract CPC group at level 4. Assuming level 4 means a code like A01B 1/00, where it has 4 parts
# A01B 1/00 -> 3 parts if split by space and slash.
# CPC codes are like A01B1/00, A01B1/02
# To get level 4, we usually truncate to the 4th segment of the hierarchical classification.
# For example, A01B 1/00 would be A01B, and A01B 1/00C would be A01B 1/00C.
# The definition of level 4 is crucial here. Let's assume level 4 means the first 4 characters for now
# or the segment before the last '/'. I need to verify what level 4 CPC means.
# Based on the CPC format (e.g., C01B33/00), a level 4 group would likely be something like C01B or C01B33.
# Let's consider `A01B 1/00` to be a level 4 group (Section-Class-Subclass-Main Group).
# So, for 'C01B33/00', if we want level 4, we would need to know the hierarchy.
# If C01B is section/class, then C01B33 is subclass/main group.
# Let's assume level 4 means the part before the final '/', if any, or the full code if no '/'.
# For codes like 'H01M10/0565', 'H01M10/056' could be level 4.
# The database CPCDefinition_database has a 'level' field. I should use that for accurate level filtering later.
# For now, let's just store the full CPC code and later filter by level 4.

# Let's group by cpc_code and filing_year to count patents
patent_counts = df_patents.groupby(['cpc_code', 'filing_year']).size().reset_index(name='count')

# Calculate EMA
smoothing_factor = 0.1
# Sort by cpc_code and filing_year for correct EMA calculation
patent_counts = patent_counts.sort_values(by=['cpc_code', 'filing_year'])

ema_results = []
for cpc_code in patent_counts['cpc_code'].unique():
    cpc_data = patent_counts[patent_counts['cpc_code'] == cpc_code].copy()
    cpc_data['ema'] = cpc_data['count'].ewm(alpha=smoothing_factor, adjust=False).mean()
    ema_results.append(cpc_data)

df_ema = pd.concat(ema_results)

# Find the best year for each CPC code
best_years = df_ema.loc[df_ema.groupby('cpc_code')['ema'].idxmax()]

# Select relevant columns and sort
result = best_years[['cpc_code', 'filing_year', 'ema']].rename(columns={'filing_year': 'best_year'}).to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-2218518486593243679': 'file_storage/function-call-2218518486593243679.json'}

exec(code, env_args)
