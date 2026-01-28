code = """import json
import pandas as pd
with open(var_call_Rp5VVDEy0XKOcKG6atWrw8IL, 'r') as f:
    funding = json.load(f)
relevant_names = var_call_rrriuml9XLKsVYGvFK30M9Od
funding_df = pd.DataFrame(funding)
amount = funding_df[funding_df['Project_Name'].isin(relevant_names)]['Amount'].astype(float).sum()
print('__RESULT__:')
print(json.dumps(int(amount)))"""

env_args = {'var_call_M5WB5deY7REsm7gEQ2IqlM4Q': 'file_storage/call_M5WB5deY7REsm7gEQ2IqlM4Q.json', 'var_call_Rp5VVDEy0XKOcKG6atWrw8IL': 'file_storage/call_Rp5VVDEy0XKOcKG6atWrw8IL.json', 'var_call_vvdJJZTp1wY59mJUiUhblAe7': 0, 'var_call_A7DJ5BY5sUIZZa7tHdqgJt6m': ['Bluffs Park Shade Structure', 'Bluffs Park Workout Station', 'Legacy Park Benches and Arbors Renovation', 'Legacy Park Paver Repair Project', 'Malibu Bluffs Park Roof Replacement Project', 'Malibu Bluffs Park South Walkway', 'Malibu Bluffs Park South Walkway Repairs', 'Malibu Park Drainage Improvements', 'Malibu Park Resurfacing Project', 'Malibu Park Storm Drain Repairs', 'Permanent Skate Park', 'Trancas Canyon Park Planting and Irrigation Repairs', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Trancas Canyon Park Playground', 'Trancas Canyon Park Playground Resurfacing', 'Trancas Canyon Park Slope Stabilization Project', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Trancas Canyon Park Upper and Lower Slopes Repair'], 'var_call_rrriuml9XLKsVYGvFK30M9Od': ['Trancas Canyon Park Slope Stabilization Project', 'Malibu Bluffs Park South Walkway Repairs', 'Malibu Bluffs Park Roof Replacement Project', 'Legacy Park Benches and Arbors Renovation', 'Malibu Park Storm Drain Repairs', 'Legacy Park Paver Repair Project', 'Trancas Canyon Park Playground Resurfacing', 'Malibu Park Drainage Improvements', 'Bluffs Park Workout Station', 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Trancas Canyon Park Playground', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Malibu Bluffs Park South Walkway', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Bluffs Park Shade Structure', 'Trancas Canyon Park Planting and Irrigation Repairs', 'Permanent Skate Park', 'Malibu Park Resurfacing Project', 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)']}

exec(code, env_args)
