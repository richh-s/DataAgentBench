code = """import json
import re
from datetime import datetime

# Load data
file_path = locals()['var_function-call-5965053505380751305']
with open(file_path, 'r') as f:
    data = json.load(f)

def parse_date(date_str):
    if not date_str: return None
    clean = re.sub(r'\b(dated|on|the|of)\b', '', date_str, flags=re.IGNORECASE).strip()
    clean = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', clean)
    clean = re.sub(r'\s+', ' ', clean).replace(',', '')
    formats = [
        '%d %B %Y', '%B %d %Y', '%Y %B %d', 
        '%d %b %Y', '%b %d %Y', '%Y %b %d'
    ]
    for fmt in formats:
        try:
            return datetime.strptime(clean, fmt)
        except ValueError:
            continue
    return None

total = len(data)
german_count = 0
h2_2019_count = 0
both_count = 0

for entry in data:
    p_info = entry.get('Patents_info', '')
    # Relaxed Germany Check
    is_de = False
    if 'DE-' in p_info or 'Germany' in p_info or 'DE' in p_info.split(): # Simple check
        is_de = True
    
    g_date_str = entry.get('grant_date', '')
    g_date = parse_date(g_date_str)
    
    is_h2 = False
    if g_date and g_date.year == 2019 and g_date.month >= 7:
        is_h2 = True
        
    if is_de:
        german_count += 1
    if is_h2:
        h2_2019_count += 1
    if is_de and is_h2:
        both_count += 1

print('__RESULT__:')
print(json.dumps({
    'total': total,
    'german_count': german_count,
    'h2_2019_count': h2_2019_count,
    'both_count': both_count,
    'sample_dates': [data[i].get('grant_date') for i in range(min(5, len(data)))]
}))"""

env_args = {'var_function-call-18028440708686650123': [{'symbol': 'A01K2227/108', 'level': '9.0', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'level': '9.0', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'level': '9.0', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'level': '9.0', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'level': '9.0', 'titleFull': 'Ovine'}], 'var_function-call-14121556978734837448': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-9930715917777594238': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}], 'var_function-call-6217904583302428661': 'file_storage/function-call-6217904583302428661.json', 'var_function-call-14928006443128475187': [{'symbol': 'C01B', 'level': '5.0', 'titleFull': 'NON-METALLIC ELEMENTS; COMPOUNDS THEREOF; METALLOIDS OR COMPOUNDS THEREOF NOT COVERED BY SUBCLASS C01C'}], 'var_function-call-372215383101891581': [{'symbol': 'C01', 'level': '4.0', 'titleFull': 'INORGANIC CHEMISTRY'}], 'var_function-call-5965053505380751305': 'file_storage/function-call-5965053505380751305.json', 'var_function-call-14590075051570926846': []}

exec(code, env_args)
