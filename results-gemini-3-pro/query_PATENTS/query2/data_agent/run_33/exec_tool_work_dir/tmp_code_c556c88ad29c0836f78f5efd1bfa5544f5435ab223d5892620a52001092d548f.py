code = """import json
import re

with open(locals()['var_function-call-4974488808225168135'], 'r') as f:
    patents = json.load(f)

debug_info = []
debug_info.append(f"Total patents: {len(patents)}")

count = 0
for p in patents:
    if count >= 10: break
    
    g_date = p.get('grant_date', '')
    p_info = p.get('Patents_info', '')
    
    info_str = f"Grant: {g_date} | Info: {p_info[:100]}..."
    debug_info.append(info_str)
    
    if "DE" in p_info:
        debug_info.append("   -> Contains DE")
    else:
        debug_info.append("   -> NO DE")
        
    count += 1

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-543765259574918097': 'file_storage/function-call-543765259574918097.json', 'var_function-call-4974488808225165482': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-4974488808225168135': 'file_storage/function-call-4974488808225168135.json', 'var_function-call-15178168180992510459': [{'symbol': 'H', 'level': '2.0', 'titleFull': 'ELECTRICITY'}, {'symbol': 'H01', 'level': '4.0', 'titleFull': 'ELECTRIC ELEMENTS'}, {'symbol': 'H01L', 'level': '5.0', 'titleFull': 'SEMICONDUCTOR DEVICES NOT COVERED BY CLASS H10'}, {'symbol': 'H01L21/00', 'level': '7.0', 'titleFull': 'Processes or apparatus adapted for the manufacture or treatment of semiconductor or solid state devices or of parts thereof'}], 'var_function-call-4381654191407381320': 'file_storage/function-call-4381654191407381320.json', 'var_function-call-6590596862173077174': []}

exec(code, env_args)
