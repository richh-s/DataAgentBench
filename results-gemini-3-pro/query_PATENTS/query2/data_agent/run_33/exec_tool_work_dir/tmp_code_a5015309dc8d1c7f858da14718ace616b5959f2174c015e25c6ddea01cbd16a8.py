code = """import json
import re

with open(locals()['var_function-call-4974488808225168135'], 'r') as f:
    patents = json.load(f)

h2_count = 0
countries = {}

months_h2 = ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 
             'July', 'August', 'September', 'October', 'November', 'December']

for p in patents:
    g_date = p.get('grant_date', '')
    if '2019' in g_date:
        is_h2 = False
        for m in months_h2:
            if m in g_date:
                is_h2 = True
                break
        
        if is_h2:
            h2_count += 1
            p_info = p.get('Patents_info', '')
            # Extract country rough guess (word after "from" or "In")
            # Or just look for country codes
            found_cc = []
            for cc in ['DE', 'US', 'RU', 'EP', 'CN', 'JP', 'KR', 'DK', 'ES']:
                if cc in p_info:
                    found_cc.append(cc)
            
            # Look for specific phrases
            origin = "Unknown"
            m = re.search(r'\bfrom ([A-Z]{2})\b', p_info)
            if m:
                origin = m.group(1)
            else:
                m = re.search(r'\bIn ([A-Z]{2})\b', p_info)
                if m:
                    origin = m.group(1)
            
            countries[origin] = countries.get(origin, 0) + 1

print("__RESULT__:")
print(json.dumps({"h2_count": h2_count, "countries": countries}))"""

env_args = {'var_function-call-543765259574918097': 'file_storage/function-call-543765259574918097.json', 'var_function-call-4974488808225165482': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-4974488808225168135': 'file_storage/function-call-4974488808225168135.json', 'var_function-call-15178168180992510459': [{'symbol': 'H', 'level': '2.0', 'titleFull': 'ELECTRICITY'}, {'symbol': 'H01', 'level': '4.0', 'titleFull': 'ELECTRIC ELEMENTS'}, {'symbol': 'H01L', 'level': '5.0', 'titleFull': 'SEMICONDUCTOR DEVICES NOT COVERED BY CLASS H10'}, {'symbol': 'H01L21/00', 'level': '7.0', 'titleFull': 'Processes or apparatus adapted for the manufacture or treatment of semiconductor or solid state devices or of parts thereof'}], 'var_function-call-4381654191407381320': 'file_storage/function-call-4381654191407381320.json', 'var_function-call-6590596862173077174': [], 'var_function-call-1330180563282511566': ['Total patents: 4833', 'Grant: 14th Mar 2019 | Info: Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-1020...', '   -> Contains DE', 'Grant: Mar 19th, 2019 | Info: In RU, the patent filing (app. number RU-2017142236-A) is held by Sletov Aleksandr Anatolevich and h...', '   -> NO DE', 'Grant: Mar 12th, 2019 | Info: The RU patent application (number RU-2018105657-A) is held by OBSHCHESTVO S OGRANICHENNOJ OTVETSTVEN...', '   -> NO DE', 'Grant: 2019 on Jul 12th | Info: Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE O...', '   -> Contains DE', 'Grant: on March 14th, 2019 | Info: Patent application (number RU-2016134259-A) from RU, owned by KVINETIK LTD, with publication number ...', '   -> NO DE', 'Grant: July 8th, 2019 | Info: The DK patent application (number DK-14719221-T) is held by JASKE WOLFGANG and has publication numbe...', '   -> NO DE', 'Grant: 8th April 2019 | Info: The DK patent filing (application number DK-14835716-T) is owned by UNIV OSLO HF and has pub. number...', '   -> NO DE', 'Grant: 2019, May 30th | Info: The RU patent application (ID RU-2018146701-U) is held by [] and has publication no. RU-189707-U1....', '   -> NO DE', 'Grant: 22nd May 2019 | Info: The ES patent application (ID ES-11727548-T) is assigned to LOHR IND and has pub. number ES-2713511-...', '   -> NO DE', 'Grant: 2019 on Nov 14th | Info: In RU, the patent filing (application no. RU-2019124341-U) is owned by [] and has pub. number RU-193...', '   -> NO DE'], 'var_function-call-18171548689147745344': []}

exec(code, env_args)
