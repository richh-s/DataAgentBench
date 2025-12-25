code = """import json
import re
import pandas as pd

# Load data
file_path = locals()['var_function-call-6422516106666611400']
with open(file_path, 'r') as f:
    data = json.load(f)

# Process data
records = []
year_pattern = re.compile(r'\b(19|20)\d{2}\b')

for row in data:
    f_date = row.get('filing_date')
    cpc_json = row.get('cpc')
    
    if not f_date or not cpc_json:
        continue
        
    # Extract Year
    # The date formats are "dated 5th March 2019", "March the 18th, 2019".
    # Finding a 4-digit number starting with 19 or 20 is a good heuristic.
    match = year_pattern.search(f_date)
    if not match:
        continue
    year = int(match.group(0))
    
    # Extract CPC codes
    try:
        cpc_list = json.loads(cpc_json)
    except:
        continue
        
    if not isinstance(cpc_list, list):
        continue
        
    subclasses = set()
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 4:
            subclasses.add(code[:4])
            
    for sc in subclasses:
        records.append({'subclass': sc, 'year': year})

# Create DataFrame
df = pd.DataFrame(records)

# Aggregate counts
# Fill missing years with 0? 
# Usually EMA is calculated over a time series. If a year has 0 filings, the EMA should decay.
# So we need a continuous year range for each subclass or globally.
# Let's find global min and max year to be safe, or per subclass.
# Per subclass is probably sufficient, but 0-filling gaps is crucial.

if df.empty:
    print("__RESULT__:")
    print("[]")
else:
    # Group by subclass and year to get counts
    counts = df.groupby(['subclass', 'year']).size().reset_index(name='count')
    
    # Create full range of years for each subclass
    min_year = counts['year'].min()
    max_year = counts['year'].max()
    all_years = range(min_year, max_year + 1)
    
    results = []
    
    # Pivot to get matrix (Years x Subclasses) filled with 0
    # This handles all years for all subclasses in one go
    pivot_df = counts.pivot(index='year', columns='subclass', values='count').fillna(0).reindex(all_years, fill_value=0)
    
    # Calculate EMA
    # Pandas ewm: alpha=0.2, adjust=False (matches the formula: y_t = alpha*x_t + (1-alpha)*y_{t-1})
    # If adjust=True (default), it uses weights.
    # The recursive formula corresponds to adjust=False.
    # Initial value: ewm usually starts with the first observation.
    ema_df = pivot_df.ewm(alpha=0.2, adjust=False).mean()
    
    # Find best year for each subclass
    best_years = ema_df.idxmax()
    
    # Filter for Best Year == 2022
    target_subclasses = best_years[best_years == 2022].index.tolist()
    
    print("__RESULT__:")
    print(json.dumps(target_subclasses))"""

env_args = {'var_function-call-6487159229108555457': 'file_storage/function-call-6487159229108555457.json', 'var_function-call-6487159229108553280': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}], 'var_function-call-4451239759330927851': [{'symbol': 'A01B1/00', 'level': '7.0'}, {'symbol': 'A', 'level': '2.0'}, {'symbol': 'A01', 'level': '4.0'}, {'symbol': 'A01B', 'level': '5.0'}], 'var_function-call-3552584556167493191': [{'count(*)': '277813'}], 'var_function-call-16984543996015765041': [], 'var_function-call-6422516106666611400': 'file_storage/function-call-6422516106666611400.json'}

exec(code, env_args)
