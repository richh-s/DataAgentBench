code = """import json
import re
import pandas as pd

# Load the data from the file
with open(locals()['var_function-call-8534322476324174148'], 'r') as f:
    data = json.load(f)

parsed_data = []
for record in data:
    cpc_raw = record.get('cpc')
    filing_date_raw = record.get('filing_date')

    # Extract year from filing_date
    filing_year = None
    if filing_date_raw:
        # Regex to find a four-digit number that looks like a year
        match = re.search(r'\b(19|20)\d{2}\b', filing_date_raw)
        if match:
            filing_year = int(match.group(0))

    if cpc_raw and filing_year:
        try:
            cpc_list = json.loads(cpc_raw)
            for cpc_item in cpc_list:
                code = cpc_item.get('code')
                if code:
                    # Check if it's a level 5 CPC code (e.g., A01B1/00, B60R1/0002)
                    # Level 5 CPC codes usually have a format like 'SECTION_CLASS_SUBCLASS/GROUP_SUBGROUP'
                    # and the group is typically 3 digits, subgroup 2 digits.
                    # A more robust way is to check the length and structure, but for simplicity,
                    # we can look for codes that have a 5-character main symbol and then 1-4 digits, a '/', and then at least 2 digits.
                    # Or more simply, if it is not broken down by / and has 5 alpha numeric and then 1 or more numeric characters.
                    # Let's consider a simpler heuristic for level 5: 
                    # a section (1 char), a class (2 chars), a subclass (1 char), a group (3 digits), a subgroup (2 digits)
                    # example: G01N33/00
                    # For level 5, it means it should have a '/'
                    if '/' in code:
                        parts = code.split('/')
                        if len(parts) == 2: # Should have group and subgroup after the /
                            main_symbol = parts[0]
                            group_subgroup = parts[1]
                            
                            # Further refine to ensure it's a level 5 group code, 
                            # which means the last two digits of the subgroup are '00' 
                            # and the code before the '/' has at least 4 alphanumeric characters.
                            # Example: A01B1/00 -> level 5 group code
                            # Example: A01B1/006 -> level 6 subgroup code
                            # Based on CPC hierarchy, a 5-level group code usually ends with "/00" for the subgroup part,
                            # but the query is asking for CPC group codes at level 5.
                            # A level 5 CPC group code is typically a symbol like A01B1/00, where '00' indicates a group level.
                            # A level 6 CPC subgroup code is like A01B1/006.
                            # The query asks for CPC group codes at level 5. So, it should end with /00
                            if len(group_subgroup) == 2 and group_subgroup.endswith('00'):
                                parsed_data.append({'cpc_code': code, 'filing_year': filing_year})
        except json.JSONDecodeError:
            # Handle cases where cpc is not a valid JSON string
            pass

df = pd.DataFrame(parsed_data)

if not df.empty:
    # Group by cpc_code and filing_year and count filings
    filings_by_year = df.groupby(['cpc_code', 'filing_year']).size().reset_index(name='filings_count')

    # Calculate EMA for each CPC code
    smoothing_factor = 0.2
    
    # Sort by year to ensure correct EMA calculation
    filings_by_year = filings_by_year.sort_values(by=['cpc_code', 'filing_year'])

    # Function to calculate EMA for a single CPC code
    def calculate_ema(series, alpha):
        return series.ewm(alpha=alpha, adjust=False).mean()

    # Apply EMA calculation for each CPC code
    ema_results = filings_by_year.groupby('cpc_code')['filings_count'].transform(lambda x: calculate_ema(x, smoothing_factor))
    filings_by_year['ema'] = ema_results

    # Find the year with the highest EMA for each CPC code
    idx_max_ema = filings_by_year.loc[filings_by_year.groupby('cpc_code')['ema'].idxmax()]

    # Filter for best year 2022
    cpc_best_year_2022 = idx_max_ema[idx_max_ema['filing_year'] == 2022]['cpc_code'].tolist()
else:
    cpc_best_year_2022 = []

print('__RESULT__:')
print(json.dumps(cpc_best_year_2022))"""

env_args = {'var_function-call-8534322476324174148': 'file_storage/function-call-8534322476324174148.json'}

exec(code, env_args)
