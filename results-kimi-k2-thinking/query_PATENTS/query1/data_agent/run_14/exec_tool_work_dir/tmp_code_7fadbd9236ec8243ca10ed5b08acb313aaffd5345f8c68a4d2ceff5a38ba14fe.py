code = """import json
import pandas as pd
from datetime import datetime
import re
import os

# Load the full data from the file path stored in the variable
file_path = var_functions.query_db:6
print(f"Loading data from: {file_path}")

with open(file_path, 'r') as f:
    data = json.load(f)

print(f"Total records loaded: {len(data)}")

# Parse CPC codes and extract years
parsed_data = []
for record in data:
    cpc_str = record.get('cpc', '[]')
    pub_date_str = record.get('publication_date', '')
    
    # Extract year from publication date (format: "Aug 3rd, 2021")
    year_match = re.search(r',\s*(\d{4})', pub_date_str)
    if year_match:
        year = int(year_match.group(1))
    else:
        continue
    
    # Parse CPC JSON
    try:
        if isinstance(cpc_str, str):
            cpc_list = json.loads(cpc_str)
        else:
            cpc_list = cpc_str
        
        if isinstance(cpc_list, list):
            for cpc_item in cpc_list:
                if isinstance(cpc_item, dict):
                    code = cpc_item.get('code', '')
                    if code:  # Only add if code is not empty
                        parsed_data.append({
                            'year': year,
                            'cpc_code': code
                        })
    except:
        continue

print(f"Parsed CPC records: {len(parsed_data)}")
if parsed_data:
    print(f"Sample data: {parsed_data[:5]}")

# Create DataFrame if we have data
if parsed_data:
    df = pd.DataFrame(parsed_data)
    print(f"DataFrame shape: {df.shape}")
    print(f"Year range: {df['year'].min()} to {df['year'].max()}")
    print(f"Unique CPC codes: {df['cpc_code'].nunique()}")
    
    # Group by year and CPC code to count filings
    yearly_counts = df.groupby(['year', 'cpc_code']).size().reset_index(name='count')
    print(f"Yearly counts shape: {yearly_counts.shape}")
    print(f"Sample yearly counts: {yearly_counts.head()}")
else:
    print("No data parsed successfully")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:5': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}, {'symbol': 'A01N', 'level': '5.0', 'titleFull': 'PRESERVATION OF BODIES OF HUMANS OR ANIMALS OR PLANTS OR PARTS THEREOF; BIOCIDES, e.g. AS DISINFECTANTS, AS PESTICIDES OR AS HERBICIDES; PEST REPELLANTS OR ATTRACTANTS; PLANT GROWTH REGULATORS'}, {'symbol': 'A01P', 'level': '5.0', 'titleFull': 'BIOCIDAL, PEST REPELLANT, PEST ATTRACTANT OR PLANT GROWTH REGULATORY ACTIVITY OF CHEMICAL COMPOUNDS OR PREPARATIONS'}, {'symbol': 'A01D', 'level': '5.0', 'titleFull': 'HARVESTING; MOWING'}, {'symbol': 'A01L', 'level': '5.0', 'titleFull': 'SHOEING OF ANIMALS'}, {'symbol': 'A01K', 'level': '5.0', 'titleFull': 'ANIMAL HUSBANDRY; AVICULTURE; APICULTURE; PISCICULTURE; FISHING; REARING OR BREEDING ANIMALS, NOT OTHERWISE PROVIDED FOR; NEW BREEDS OF ANIMALS'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
