code = """import json
import os
import re
from datetime import datetime

# Load the German patents data
file_path = "file_storage/functions.query_db:36.json"
with open(file_path, 'r') as f:
    all_german_patents = json.load(f)

print(f"Total German patents: {len(all_german_patents)}")

# Filter for second half of 2019
second_half_months = ['July', 'August', 'September', 'October', 'November', 'December']
german_2019_h2_patents = []

for patent in all_german_patents:
    grant_date = patent.get('grant_date', '')
    
    # Check if second half of 2019
    is_second_half = any(month in grant_date for month in second_half_months) and '2019' in grant_date
    
    if is_second_half:
        german_2019_h2_patents.append(patent)

print(f"German patents in second half 2019: {len(german_2019_h2_patents)}")

# Debug: Show first few patents
for i, p in enumerate(german_2019_h2_patents[:5]):
    print(f"  {i+1}. {p.get('grant_date', 'N/A')} - {p.get('Patents_info', 'N/A')[:100]}...")

# Extract CPC codes at level 4 and count filings
cpc_counts = {}
cpc_yearly_data = {}

for patent in german_2019_h2_patents:
    cpc_field = patent.get('cpc', '')
    grant_date = patent.get('grant_date', '')
    
    if not cpc_field:
        continue
        
    try:
        cpc_codes = json.loads(cpc_field)
    except:
        continue
    
    # Determine year from grant_date (should all be 2019)
    year = 2019
    if str(year) not in grant_date:
        continue
    
    for code_entry in cpc_codes:
        code = code_entry['code']
        if '/' not in code:
            continue
            
        # Extract level 4 CPC
        parts = code.split('/')
        if len(parts) >= 2:
            section = parts[0]
            group = parts[1]
            # Level 4 format: Section/Group (e.g., G06F9/455)
            if len(group) >= 3:
                level4_code = f"{section}/{group}"
                
                # Count per year
                if level4_code not in cpc_yearly_data:
                    cpc_yearly_data[level4_code] = {2019: 0}
                elif 2019 not in cpc_yearly_data[level4_code]:
                    cpc_yearly_data[level4_code][2019] = 0
                    
                cpc_yearly_data[level4_code][2019] += 1
                cpc_counts[level4_code] = cpc_counts.get(level4_code, 0) + 1

print(f"\nCPC codes at level 4: {len(cpc_counts)}")
print("Top 10 by count:")
sorted_cpc = sorted(cpc_counts.items(), key=lambda x: x[1], reverse=True)
for code, count in sorted_cpc[:10]:
    print(f"  {code}: {count}")

# Since we only have 2019 data, EMA is just the count
ema_results = []
for code, yearly_data in cpc_yearly_data.items():
    # For 2019 only, EMA = count
    count = yearly_data.get(2019, 0)
    if count > 0:
        ema_results.append({
            'cpc_code': code,
            'ema': float(count),
            'best_year': 2019,
            'count_2019': count
        })

# Sort by EMA
ema_results.sort(key=lambda x: x['ema'], reverse=True)

output = {
    'total_patents': len(german_2019_h2_patents),
    'total_cpc_codes': len(ema_results),
    'top_ema_cpc': ema_results[:20]  # Top 20
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['cpc_definition'], 'var_functions.list_db:2': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:24': {'available_vars': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9'], 'patent_count': 3838, 'file_path': 'file_storage/functions.query_db:9.json'}, 'var_functions.execute_python:28': {'total_german_patents': 20, 'total_cpc_codes': 93, 'top_cpc_emas': [{'cpc_code': 'E21B43/129', 'filing_count': 4, 'exponential_moving_average': 4.0}, {'cpc_code': 'F04C11/001', 'filing_count': 3, 'exponential_moving_average': 3.0}, {'cpc_code': 'F04C2/1071', 'filing_count': 3, 'exponential_moving_average': 3.0}, {'cpc_code': 'F04C13/008', 'filing_count': 3, 'exponential_moving_average': 3.0}, {'cpc_code': 'F01C1/101', 'filing_count': 3, 'exponential_moving_average': 3.0}, {'cpc_code': 'H04W52/0261', 'filing_count': 3, 'exponential_moving_average': 3.0}, {'cpc_code': 'H04W52/0216', 'filing_count': 3, 'exponential_moving_average': 3.0}, {'cpc_code': 'H04W52/0229', 'filing_count': 3, 'exponential_moving_average': 3.0}, {'cpc_code': 'H04W72/0446', 'filing_count': 3, 'exponential_moving_average': 3.0}, {'cpc_code': 'H04W52/0251', 'filing_count': 3, 'exponential_moving_average': 3.0}, {'cpc_code': 'F24B5/023', 'filing_count': 3, 'exponential_moving_average': 3.0}, {'cpc_code': 'F02M59/102', 'filing_count': 2, 'exponential_moving_average': 2.0}, {'cpc_code': 'F04B53/001', 'filing_count': 2, 'exponential_moving_average': 2.0}, {'cpc_code': 'F02M59/368', 'filing_count': 2, 'exponential_moving_average': 2.0}, {'cpc_code': 'H04L5/0037', 'filing_count': 2, 'exponential_moving_average': 2.0}, {'cpc_code': 'H04L1/1614', 'filing_count': 2, 'exponential_moving_average': 2.0}, {'cpc_code': 'H04L1/1822', 'filing_count': 2, 'exponential_moving_average': 2.0}, {'cpc_code': 'H04L1/1861', 'filing_count': 2, 'exponential_moving_average': 2.0}, {'cpc_code': 'H04L5/0007', 'filing_count': 2, 'exponential_moving_average': 2.0}, {'cpc_code': 'H04L1/1864', 'filing_count': 2, 'exponential_moving_average': 2.0}]}, 'var_functions.query_db:32': [{'symbol': 'H04W52/0261', 'titleFull': 'Power saving arrangements in terminal devices managing power supply demand, e.g. depending on battery level'}, {'symbol': 'H04W52/0251', 'titleFull': 'Power saving arrangements in terminal devices using monitoring of local events, e.g. events related to user activity'}, {'symbol': 'F04C2/1071', 'titleFull': 'Rotary-piston machines or pumps of intermeshing-engagement type, i.e. with engagement of co-operating members similar to that of toothed gearing of internal-axis type with the outer member having more teeth or tooth-equivalents, e.g. rollers, than the inner member with helical teeth the inner and outer member having a different number of threads and one of the two being made of elastic materials, e.g. Moineau type'}, {'symbol': 'F04C11/001', 'titleFull': 'Combinations of two or more machines or pumps, each being of rotary-piston or oscillating-piston type; Pumping installations of similar working principle'}, {'symbol': 'F04C13/008', 'titleFull': 'Pumps for submersible use, i.e. down-hole pumping'}, {'symbol': 'E21B43/129', 'titleFull': 'Adaptations of down-hole pump systems powered by fluid supplied from outside the borehole'}, {'symbol': 'H04W52/0216', 'titleFull': 'Power saving arrangements in terminal devices managed by the network, e.g. network or access point is master and terminal is slave using a pre-established activity schedule, e.g. traffic indication frame'}, {'symbol': 'H04W52/0229', 'titleFull': 'Power saving arrangements in terminal devices using monitoring of external events, e.g. the presence of a signal where the received signal is a wanted signal'}, {'symbol': 'F01C1/101', 'titleFull': 'Moineau-type'}, {'symbol': 'H04W72/0446', 'titleFull': 'Resources in time domain, e.g. slots or frames'}], 'var_functions.query_db:34': [{'symbol': 'F24B5/023', 'titleFull': 'Supply of primary air for combustion'}, {'symbol': 'H04W72/0446', 'titleFull': 'Resources in time domain, e.g. slots or frames'}, {'symbol': 'H04W52/0261', 'titleFull': 'Power saving arrangements in terminal devices managing power supply demand, e.g. depending on battery level'}, {'symbol': 'H04W52/0251', 'titleFull': 'Power saving arrangements in terminal devices using monitoring of local events, e.g. events related to user activity'}, {'symbol': 'H04L1/1822', 'titleFull': 'Automatic repetition systems, e.g. Van Duuren systems involving configuration of automatic repeat request [ARQ] with parallel processes'}, {'symbol': 'F04C2/1071', 'titleFull': 'Rotary-piston machines or pumps of intermeshing-engagement type, i.e. with engagement of co-operating members similar to that of toothed gearing of internal-axis type with the outer member having more teeth or tooth-equivalents, e.g. rollers, than the inner member with helical teeth the inner and outer member having a different number of threads and one of the two being made of elastic materials, e.g. Moineau type'}, {'symbol': 'H04L1/1864', 'titleFull': 'ARQ related signaling'}, {'symbol': 'F04B53/001', 'titleFull': 'Noise damping'}, {'symbol': 'F04C11/001', 'titleFull': 'Combinations of two or more machines or pumps, each being of rotary-piston or oscillating-piston type; Pumping installations of similar working principle'}, {'symbol': 'F04C13/008', 'titleFull': 'Pumps for submersible use, i.e. down-hole pumping'}, {'symbol': 'F02M59/102', 'titleFull': 'Mechanical drive, e.g. tappets or cams'}, {'symbol': 'E21B43/129', 'titleFull': 'Adaptations of down-hole pump systems powered by fluid supplied from outside the borehole'}, {'symbol': 'F02M59/368', 'titleFull': 'Pump inlet valves being closed when actuated'}, {'symbol': 'H04L1/1614', 'titleFull': 'Details of the supervisory signal using bitmaps'}, {'symbol': 'H04L1/1861', 'titleFull': 'Physical mapping arrangements'}, {'symbol': 'F01C1/101', 'titleFull': 'Moineau-type'}, {'symbol': 'H04L5/0007', 'titleFull': 'Time-frequency the frequencies being orthogonal, e.g. OFDM(A), DMT'}, {'symbol': 'H04W52/0216', 'titleFull': 'Power saving arrangements in terminal devices managed by the network, e.g. network or access point is master and terminal is slave using a pre-established activity schedule, e.g. traffic indication frame'}, {'symbol': 'H04W52/0229', 'titleFull': 'Power saving arrangements in terminal devices using monitoring of external events, e.g. the presence of a signal where the received signal is a wanted signal'}, {'symbol': 'H04L5/0037', 'titleFull': 'Inter-user or inter-terminal allocation'}], 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
