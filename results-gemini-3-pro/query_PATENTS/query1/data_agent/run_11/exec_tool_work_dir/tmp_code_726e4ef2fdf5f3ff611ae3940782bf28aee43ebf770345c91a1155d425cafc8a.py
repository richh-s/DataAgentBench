code = """import json
import re
import collections

# Load the large result file
file_path = locals()['var_function-call-17338179346736761681']
with open(file_path, 'r') as f:
    data = json.load(f)

# Structure to hold counts: counts[subclass][year] = count
counts = collections.defaultdict(lambda: collections.defaultdict(int))
all_years = set()

year_pattern = re.compile(r'\b(19|20)\d{2}\b')

for row in data:
    f_date = row.get('filing_date', '')
    cpc_str = row.get('cpc', '')
    
    if not f_date or not cpc_str:
        continue
    
    # Extract Year
    match = year_pattern.search(f_date)
    if match:
        year = int(match.group(0))
    else:
        continue
        
    all_years.add(year)
    
    # Extract CPC codes
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    # Get unique subclasses for this patent
    subclasses = set()
    for item in cpc_list:
        code = item.get('code', '')
        # Level 5 is Subclass (4 chars), e.g., C01B
        if len(code) >= 4:
            subclass = code[:4]
            subclasses.add(subclass)
            
    # Increment counts
    for sc in subclasses:
        counts[sc][year] += 1

# Define range of years
if not all_years:
    print("__RESULT__:")
    print("[]")
    exit()

min_year = min(all_years)
max_year = max(all_years)
# We can just iterate from min_year to max_year

results = []
alpha = 0.2

for sc, year_counts in counts.items():
    # Calculate EMA
    ema = 0
    # We need to decide start year. 
    # Option 1: Start from global min_year.
    # Option 2: Start from first year of this subclass.
    # "Identify the CPC technology areas with the highest exponential moving average of patent filings each year"
    # Usually implies a continuous series. I'll start from the global min_year to handle 0s correctly if the technology existed but had no filings?
    # Actually, if a technology didn't exist, its count is 0. EMA will decay or stay 0.
    # However, if we start at the first appearance, the first EMA is the count. 
    # If we start at global min, and count is 0, EMA is 0.
    # Let's use global min_year for consistency across technologies.
    
    # But wait, if min_year is 1900 and a tech starts in 2000, 100 years of 0s.
    # The prompt says "Identify the CPC technology areas with the highest exponential moving average ... each year".
    # And "whose best year is 2022".
    # This implies we compare the EMA values of a single tech across years.
    
    ema_series = {}
    current_ema = None
    
    # Let's sort years for this subclass to find the start?
    # Or use global range. Global range is safer for "each year" comparison if we were comparing techs against each other.
    # Here we just need the max year for THIS tech.
    # If I start late, the first value has high weight (1.0).
    # If I start early with 0s, the first value has 0.2 weight eventually.
    # Standard EMA usually assumes a stream.
    # I will iterate from the MIN YEAR IN THE DATASET up to MAX YEAR (should be at least 2022).
    
    # Let's check max year in data.
    if max_year < 2022:
        # If no 2022 data, then no result can be 2022.
        pass
    
    max_ema_val = -1
    best_year = -1
    
    # Initialize EMA with the first year's value (even if 0, if we treat it as time series)
    # Or initialize with first non-zero?
    # Pandas ewm ignores NaNs or treats start.
    # Simple formula: EMA_t = alpha * x_t + (1-alpha) * EMA_{t-1}
    # Initial: EMA_0 = x_0.
    
    # I will use the global min_year as start.
    # First year:
    first_val = year_counts.get(min_year, 0)
    current_ema = first_val
    
    if min_year == 2022: # Edge case
         if first_val > 0: # Or just comparison
             pass

    if current_ema > max_ema_val:
        max_ema_val = current_ema
        best_year = min_year
        
    for y in range(min_year + 1, max_year + 1):
        val = year_counts.get(y, 0)
        current_ema = (val * alpha) + (current_ema * (1 - alpha))
        
        if current_ema > max_ema_val:
            max_ema_val = current_ema
            best_year = y
            
    if best_year == 2022:
        results.append(sc)

# Sort results to be deterministic?
results.sort()

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-18328823556170727936': 'file_storage/function-call-18328823556170727936.json', 'var_function-call-1448611933655007552': [{'symbol': 'H01M10/0565', 'level': '11.0', 'titleFull': 'Polymeric materials, e.g. gel-type or solid-type'}, {'symbol': 'C01B33/00', 'level': '7.0', 'titleFull': 'Silicon; Compounds thereof'}], 'var_function-call-12333554857187488258': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}], 'var_function-call-520411694824460309': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-8582293101607143888': [{'len': '4', 'count': '677'}], 'var_function-call-17338179346736761681': 'file_storage/function-call-17338179346736761681.json'}

exec(code, env_args)
