code = """import json
import re
import pandas as pd
from datetime import datetime

# Load the patent data for German patents in second half 2019
file_path = "file_storage/functions.query_db:50.json"
with open(file_path, 'r') as f:
    patents_data = json.load(f)

print(f"Total German patents in second half 2019: {len(patents_data)}")

# Extract CPC codes at level 4 and create year-wise data
cpc_data = []  # List to store records
year_pattern = re.compile(r'2019')  # All should be 2019

for patent in patents_data:
    cpc_field = patent.get('cpc', '')
    grant_date = patent.get('grant_date', '')
    
    if not cpc_field:
        continue
        
    try:
        cpc_codes = json.loads(cpc_field)
    except:
        continue
    
    # Confirm it's 2019 (should be based on our query)
    if '2019' not in grant_date:
        continue
    
    year = 2019
    
    for code_entry in cpc_codes:
        code = code_entry.get('code', '')
        if not code or '/' not in code:
            continue
            
        # Extract level 4 CPC code (Section/Subclass + main group)
        # Format: G06F9/45533 becomes G06F9/455
        parts = code.split('/')
        section_subclass = parts[0]  # e.g., G06F9
        group = parts[1]  # e.g., 45533
        
        # Level 4: main group (first 3 digits if available)
        if len(group) >= 3:
            main_group = group[:3]
            level4_code = f"{section_subclass}/{main_group}"
            
            cpc_data.append({
                'cpc_code': level4_code,
                'year': year,
                'count': 1
            })

# Create DataFrame
df = pd.DataFrame(cpc_data)
print(f"Total CPC code instances: {len(df)}")

# Group by CPC code and year to get counts
grouped = df.groupby(['cpc_code', 'year']).size().reset_index(name='filings')
print(f"Unique CPC-year combinations: {len(grouped)}")

# Pivot to get years as columns
df_pivot = grouped.pivot(index='cpc_code', columns='year', values='filings').fillna(0)

# Ensure 2019 column exists and add missing years for EMA calculation
years = [2019, 2020, 2021, 2022]
for year in years:
    if year not in df_pivot.columns:
        df_pivot[year] = 0

# Calculate EMA for each CPC code
smoothing_factor = 0.1

def calculate_ema(row):
    values = [row.get(year, 0) for year in sorted(years) if year in row.index]
    
    if not values or sum(values) == 0:
        return 0
    
    # Calculate EMA sequentially
    ema = values[0]  # Initialize with first value
    for i in range(1, len(values)):
        ema = (smoothing_factor * values[i]) + ((1 - smoothing_factor) * ema)
    
    return ema

def get_best_year(row):
    values = {year: row.get(year, 0) for year in years if year in row.index}
    if not values:
        return None
    return max(values, key=values.get)

def get_best_year_count(row):
    best_year = get_best_year(row)
    return row.get(best_year, 0)

# Apply calculations
df_pivot['ema'] = df_pivot.apply(calculate_ema, axis=1)
df_pivot['best_year'] = df_pivot.apply(get_best_year, axis=1)
df_pivot['best_year_count'] = df_pivot.apply(get_best_year_count, axis=1)
df_pivot['total_filings'] = df_pivot[[2019, 2020, 2021, 2022]].sum(axis=1)

# Filter CPC codes with at least 1 filing in 2019
active_cpc = df_pivot[df_pivot[2019] > 0].copy()

# Sort by EMA
top_cpc = active_cpc.sort_values('ema', ascending=False).head(15)

print(f"Top CPC codes by EMA: {len(top_cpc)}")
print(top_cpc.head())

# Prepare results for title lookup
results_for_titles = top_cpc.reset_index()[['cpc_code', 'full_title', 'best_year', 'best_year_count', 'ema']].to_dict('records')

output = {
    'total_patents_analyzed': len(patents_data),
    'top_cpc_codes': results_for_titles
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['cpc_definition'], 'var_functions.list_db:2': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:24': {'available_vars': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9'], 'patent_count': 3838, 'file_path': 'file_storage/functions.query_db:9.json'}, 'var_functions.execute_python:28': {'total_german_patents': 20, 'total_cpc_codes': 93, 'top_cpc_emas': [{'cpc_code': 'E21B43/129', 'filing_count': 4, 'exponential_moving_average': 4.0}, {'cpc_code': 'F04C11/001', 'filing_count': 3, 'exponential_moving_average': 3.0}, {'cpc_code': 'F04C2/1071', 'filing_count': 3, 'exponential_moving_average': 3.0}, {'cpc_code': 'F04C13/008', 'filing_count': 3, 'exponential_moving_average': 3.0}, {'cpc_code': 'F01C1/101', 'filing_count': 3, 'exponential_moving_average': 3.0}, {'cpc_code': 'H04W52/0261', 'filing_count': 3, 'exponential_moving_average': 3.0}, {'cpc_code': 'H04W52/0216', 'filing_count': 3, 'exponential_moving_average': 3.0}, {'cpc_code': 'H04W52/0229', 'filing_count': 3, 'exponential_moving_average': 3.0}, {'cpc_code': 'H04W72/0446', 'filing_count': 3, 'exponential_moving_average': 3.0}, {'cpc_code': 'H04W52/0251', 'filing_count': 3, 'exponential_moving_average': 3.0}, {'cpc_code': 'F24B5/023', 'filing_count': 3, 'exponential_moving_average': 3.0}, {'cpc_code': 'F02M59/102', 'filing_count': 2, 'exponential_moving_average': 2.0}, {'cpc_code': 'F04B53/001', 'filing_count': 2, 'exponential_moving_average': 2.0}, {'cpc_code': 'F02M59/368', 'filing_count': 2, 'exponential_moving_average': 2.0}, {'cpc_code': 'H04L5/0037', 'filing_count': 2, 'exponential_moving_average': 2.0}, {'cpc_code': 'H04L1/1614', 'filing_count': 2, 'exponential_moving_average': 2.0}, {'cpc_code': 'H04L1/1822', 'filing_count': 2, 'exponential_moving_average': 2.0}, {'cpc_code': 'H04L1/1861', 'filing_count': 2, 'exponential_moving_average': 2.0}, {'cpc_code': 'H04L5/0007', 'filing_count': 2, 'exponential_moving_average': 2.0}, {'cpc_code': 'H04L1/1864', 'filing_count': 2, 'exponential_moving_average': 2.0}]}, 'var_functions.query_db:32': [{'symbol': 'H04W52/0261', 'titleFull': 'Power saving arrangements in terminal devices managing power supply demand, e.g. depending on battery level'}, {'symbol': 'H04W52/0251', 'titleFull': 'Power saving arrangements in terminal devices using monitoring of local events, e.g. events related to user activity'}, {'symbol': 'F04C2/1071', 'titleFull': 'Rotary-piston machines or pumps of intermeshing-engagement type, i.e. with engagement of co-operating members similar to that of toothed gearing of internal-axis type with the outer member having more teeth or tooth-equivalents, e.g. rollers, than the inner member with helical teeth the inner and outer member having a different number of threads and one of the two being made of elastic materials, e.g. Moineau type'}, {'symbol': 'F04C11/001', 'titleFull': 'Combinations of two or more machines or pumps, each being of rotary-piston or oscillating-piston type; Pumping installations of similar working principle'}, {'symbol': 'F04C13/008', 'titleFull': 'Pumps for submersible use, i.e. down-hole pumping'}, {'symbol': 'E21B43/129', 'titleFull': 'Adaptations of down-hole pump systems powered by fluid supplied from outside the borehole'}, {'symbol': 'H04W52/0216', 'titleFull': 'Power saving arrangements in terminal devices managed by the network, e.g. network or access point is master and terminal is slave using a pre-established activity schedule, e.g. traffic indication frame'}, {'symbol': 'H04W52/0229', 'titleFull': 'Power saving arrangements in terminal devices using monitoring of external events, e.g. the presence of a signal where the received signal is a wanted signal'}, {'symbol': 'F01C1/101', 'titleFull': 'Moineau-type'}, {'symbol': 'H04W72/0446', 'titleFull': 'Resources in time domain, e.g. slots or frames'}], 'var_functions.query_db:34': [{'symbol': 'F24B5/023', 'titleFull': 'Supply of primary air for combustion'}, {'symbol': 'H04W72/0446', 'titleFull': 'Resources in time domain, e.g. slots or frames'}, {'symbol': 'H04W52/0261', 'titleFull': 'Power saving arrangements in terminal devices managing power supply demand, e.g. depending on battery level'}, {'symbol': 'H04W52/0251', 'titleFull': 'Power saving arrangements in terminal devices using monitoring of local events, e.g. events related to user activity'}, {'symbol': 'H04L1/1822', 'titleFull': 'Automatic repetition systems, e.g. Van Duuren systems involving configuration of automatic repeat request [ARQ] with parallel processes'}, {'symbol': 'F04C2/1071', 'titleFull': 'Rotary-piston machines or pumps of intermeshing-engagement type, i.e. with engagement of co-operating members similar to that of toothed gearing of internal-axis type with the outer member having more teeth or tooth-equivalents, e.g. rollers, than the inner member with helical teeth the inner and outer member having a different number of threads and one of the two being made of elastic materials, e.g. Moineau type'}, {'symbol': 'H04L1/1864', 'titleFull': 'ARQ related signaling'}, {'symbol': 'F04B53/001', 'titleFull': 'Noise damping'}, {'symbol': 'F04C11/001', 'titleFull': 'Combinations of two or more machines or pumps, each being of rotary-piston or oscillating-piston type; Pumping installations of similar working principle'}, {'symbol': 'F04C13/008', 'titleFull': 'Pumps for submersible use, i.e. down-hole pumping'}, {'symbol': 'F02M59/102', 'titleFull': 'Mechanical drive, e.g. tappets or cams'}, {'symbol': 'E21B43/129', 'titleFull': 'Adaptations of down-hole pump systems powered by fluid supplied from outside the borehole'}, {'symbol': 'F02M59/368', 'titleFull': 'Pump inlet valves being closed when actuated'}, {'symbol': 'H04L1/1614', 'titleFull': 'Details of the supervisory signal using bitmaps'}, {'symbol': 'H04L1/1861', 'titleFull': 'Physical mapping arrangements'}, {'symbol': 'F01C1/101', 'titleFull': 'Moineau-type'}, {'symbol': 'H04L5/0007', 'titleFull': 'Time-frequency the frequencies being orthogonal, e.g. OFDM(A), DMT'}, {'symbol': 'H04W52/0216', 'titleFull': 'Power saving arrangements in terminal devices managed by the network, e.g. network or access point is master and terminal is slave using a pre-established activity schedule, e.g. traffic indication frame'}, {'symbol': 'H04W52/0229', 'titleFull': 'Power saving arrangements in terminal devices using monitoring of external events, e.g. the presence of a signal where the received signal is a wanted signal'}, {'symbol': 'H04L5/0037', 'titleFull': 'Inter-user or inter-terminal allocation'}], 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:42': {'total_patents': 31, 'top_cpc_count': 20, 'top_cpc_codes': ['B01D2255/207', 'F04C2/107', 'E21B43/129', 'H04L1/186', 'C04B2235/656', 'C04B2235/322', 'C04B35/645', 'H01R43/048', 'H01R4/188', 'H01R4/184', 'F04C11/001', 'F04C13/008', 'F01C1/101', 'H04W52/026', 'H04W52/021', 'H04W52/022', 'H04W72/044', 'H04W52/025', 'F24B5/023', 'B29C2049/589'], 'ema_summary': [{'cpc_code': 'B01D2255/207', 'ema': 7.29, 'best_year': 2019, 'best_year_count': 10, 'total_2019': 10}, {'cpc_code': 'F04C2/107', 'ema': 2.92, 'best_year': 2019, 'best_year_count': 4, 'total_2019': 4}, {'cpc_code': 'E21B43/129', 'ema': 2.92, 'best_year': 2019, 'best_year_count': 4, 'total_2019': 4}, {'cpc_code': 'H04L1/186', 'ema': 2.92, 'best_year': 2019, 'best_year_count': 4, 'total_2019': 4}, {'cpc_code': 'C04B2235/656', 'ema': 2.92, 'best_year': 2019, 'best_year_count': 4, 'total_2019': 4}, {'cpc_code': 'C04B2235/322', 'ema': 2.92, 'best_year': 2019, 'best_year_count': 4, 'total_2019': 4}, {'cpc_code': 'C04B35/645', 'ema': 2.92, 'best_year': 2019, 'best_year_count': 4, 'total_2019': 4}, {'cpc_code': 'H01R43/048', 'ema': 2.92, 'best_year': 2019, 'best_year_count': 4, 'total_2019': 4}, {'cpc_code': 'H01R4/188', 'ema': 2.92, 'best_year': 2019, 'best_year_count': 4, 'total_2019': 4}, {'cpc_code': 'H01R4/184', 'ema': 2.92, 'best_year': 2019, 'best_year_count': 4, 'total_2019': 4}, {'cpc_code': 'F04C11/001', 'ema': 2.19, 'best_year': 2019, 'best_year_count': 3, 'total_2019': 3}, {'cpc_code': 'F04C13/008', 'ema': 2.19, 'best_year': 2019, 'best_year_count': 3, 'total_2019': 3}, {'cpc_code': 'F01C1/101', 'ema': 2.19, 'best_year': 2019, 'best_year_count': 3, 'total_2019': 3}, {'cpc_code': 'H04W52/026', 'ema': 2.19, 'best_year': 2019, 'best_year_count': 3, 'total_2019': 3}, {'cpc_code': 'H04W52/021', 'ema': 2.19, 'best_year': 2019, 'best_year_count': 3, 'total_2019': 3}, {'cpc_code': 'H04W52/022', 'ema': 2.19, 'best_year': 2019, 'best_year_count': 3, 'total_2019': 3}, {'cpc_code': 'H04W72/044', 'ema': 2.19, 'best_year': 2019, 'best_year_count': 3, 'total_2019': 3}, {'cpc_code': 'H04W52/025', 'ema': 2.19, 'best_year': 2019, 'best_year_count': 3, 'total_2019': 3}, {'cpc_code': 'F24B5/023', 'ema': 2.19, 'best_year': 2019, 'best_year_count': 3, 'total_2019': 3}, {'cpc_code': 'B29C2049/589', 'ema': 2.19, 'best_year': 2019, 'best_year_count': 3, 'total_2019': 3}]}, 'var_functions.query_db:44': [{'symbol': 'B01D2255/207', 'titleFull': 'Transition metals'}, {'symbol': 'C04B2235/656', 'titleFull': 'Aspects relating to heat treatments of ceramic bodies such as green ceramics or pre-sintered ceramics, e.g. burning, sintering or melting processes characterised by specific heating conditions during heat treatment'}, {'symbol': 'E21B43/129', 'titleFull': 'Adaptations of down-hole pump systems powered by fluid supplied from outside the borehole'}, {'symbol': 'H01R4/184', 'titleFull': 'Electrically-conductive connections between two or more conductive members in direct contact, i.e. touching one another; Means for effecting or maintaining such contact; Electrically-conductive connections having two or more spaced connecting locations for conductors and using contact members penetrating insulation effected solely by twisting, wrapping, bending, crimping, or other permanent deformation by crimping for cylindrical elongated bodies, e.g. cables having circular cross-section comprising a U-shaped wire-receiving portion'}, {'symbol': 'C04B2235/322', 'titleFull': 'Transition aluminas, e.g. delta or gamma aluminas'}, {'symbol': 'H04W72/044', 'titleFull': 'Wireless resource allocation based on the type of the allocated resource'}, {'symbol': 'C04B35/645', 'titleFull': 'Pressure sintering'}, {'symbol': 'F24B5/023', 'titleFull': 'Supply of primary air for combustion'}, {'symbol': 'F04C11/001', 'titleFull': 'Combinations of two or more machines or pumps, each being of rotary-piston or oscillating-piston type; Pumping installations of similar working principle'}, {'symbol': 'F04C13/008', 'titleFull': 'Pumps for submersible use, i.e. down-hole pumping'}, {'symbol': 'F01C1/101', 'titleFull': 'Moineau-type'}, {'symbol': 'F04C2/107', 'titleFull': 'Rotary-piston machines or pumps of intermeshing-engagement type, i.e. with engagement of co-operating members similar to that of toothed gearing of internal-axis type with the outer member having more teeth or tooth-equivalents, e.g. rollers, than the inner member with helical teeth'}, {'symbol': 'H01R4/188', 'titleFull': 'Electrically-conductive connections between two or more conductive members in direct contact, i.e. touching one another; Means for effecting or maintaining such contact; Electrically-conductive connections having two or more spaced connecting locations for conductors and using contact members penetrating insulation effected solely by twisting, wrapping, bending, crimping, or other permanent deformation by crimping having an uneven wire-receiving surface to improve the contact'}, {'symbol': 'H01R43/048', 'titleFull': 'Crimping apparatus or processes'}], 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json'}

exec(code, env_args)
