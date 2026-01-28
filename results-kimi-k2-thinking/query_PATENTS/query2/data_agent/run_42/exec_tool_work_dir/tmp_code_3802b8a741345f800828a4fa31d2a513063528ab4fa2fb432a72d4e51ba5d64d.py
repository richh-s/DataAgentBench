code = """import json
import re
from collections import defaultdict

# Get file path
file_path = locals()['var_functions.query_db:28']

# Read all German patents
de_patents = []
try:
    with open(file_path, 'r') as f:
        de_patents = json.load(f)
except Exception as e:
    print(f"Error: {e}")

# Filter for second half 2019
def extract_month(date_str):
    if not date_str:
        return None
    patterns = [
        r'([A-Za-z]+)\s+(?:\d{1,2})[th|st|nd|rd]?[\s,]*2019',
        r'(?:\d{1,2})[th|st|nd|rd]?\s+([A-Za-z]+)[\s,]*2019',
        r'2019\s+on\s+([A-Za-z]+)\s+(?:\d{1,2})[th|st|nd|rd]?',
        r'2019,\s+([A-Za-z]+)\s+(?:\d{1,2})[th|st|nd|rd]?',
        r'dated\s+(?:\d{1,2})[th|st|nd|rd]?\s+([A-Za-z]+)\s+2019'
    ]
    month_map = {
        'jan': 1, 'january': 1, 'feb': 2, 'february': 2,
        'mar': 3, 'march': 3, 'apr': 4, 'april': 4,
        'may': 5, 'jun': 6, 'june': 6, 'jul': 7, 'july': 7,
        'aug': 8, 'august': 8, 'sep': 9, 'september': 9,
        'oct': 10, 'october': 10, 'nov': 11, 'november': 11,
        'dec': 12, 'december': 12
    }
    for pattern in patterns:
        match = re.search(pattern, date_str, re.IGNORECASE)
        if match:
            month_str = match.group(1).lower()
            for key, val in month_map.items():
                if month_str.startswith(key):
                    return val
    return None

# Get CPC level 4
def get_cpc_level4(cpc_code):
    if not cpc_code or len(cpc_code) < 7:
        return None
    try:
        section = cpc_code[0]
        class_num = cpc_code[1:3]
        subclass = cpc_code[3]
        slash_pos = cpc_code.find('/')
        if slash_pos == -1:
            return None
        group_start = slash_pos + 1
        group_digits = ""
        for i in range(group_start, len(cpc_code)):
            if cpc_code[i].isdigit():
                group_digits += cpc_code[i]
            else:
                break
        if not group_digits:
            return None
        return f"{section}{class_num}{subclass}/{group_digits[0]}"
    except:
        return None

# Extract filing year
def extract_filing_year(date_str):
    if not date_str:
        return None
    year_match = re.search(r'(\d{4})', date_str)
    if year_match:
        return int(year_match.group(1))
    return None

# Get relevant patents and their CPC level 4 codes
second_half_2019_patents = []
cpc_level4_set = set()

for patent in de_patents:
    grant_date = patent.get('grant_date', '')
    month = extract_month(grant_date)
    if month and 7 <= month <= 12:
        second_half_2019_patents.append(patent)
        cpc_str = patent.get('cpc', '[]')
        try:
            cpc_list = json.loads(cpc_str) if isinstance(cpc_str, str) else cpc_str
            for cpc_item in cpc_list:
                code = cpc_item.get('code', '')
                level4 = get_cpc_level4(code)
                if level4:
                    cpc_level4_set.add(level4)
        except:
            pass

# Now get all German patents to build historical filing data
all_de_patents = de_patents

# Build historical filing counts per CPC level 4 and year
filing_counts = defaultdict(lambda: defaultdict(int))

for patent in all_de_patents:
    filing_date = patent.get('filing_date', '')
    filing_year = extract_filing_year(filing_date)
    if filing_year:
        cpc_str = patent.get('cpc', '[]')
        try:
            cpc_list = json.loads(cpc_str) if isinstance(cpc_str, str) else cpc_str
            for cpc_item in cpc_list:
                code = cpc_item.get('code', '')
                level4 = get_cpc_level4(code)
                if level4 and level4 in cpc_level4_set:
                    filing_counts[level4][filing_year] += 1
        except:
            pass

# Calculate EMA for each CPC level 4
alpha = 0.1  # smoothing factor
cpc_ema_results = {}

for cpc_code, year_counts in filing_counts.items():
    if not year_counts:
        continue
    
    # Get sorted years
    years = sorted(year_counts.keys())
    if len(years) < 2:
        continue
    
    # Calculate EMA for each year
    ema_values = {}
    ema = None
    
    for year in years:
        count = year_counts[year]
        if ema is None:
            ema = count  # Initialize with first value
        else:
            ema = alpha * count + (1 - alpha) * ema
        ema_values[year] = ema
    
    # Find year with highest EMA
    best_year = max(ema_values.items(), key=lambda x: x[1])[0]
    
    cpc_ema_results[cpc_code] = {
        'best_year': best_year,
        'best_ema': ema_values[best_year],
        'year_counts': dict(year_counts),
        'ema_values': ema_values
    }

print('__RESULT__:')
print(json.dumps({
    'total_second_half_2019_patents': len(second_half_2019_patents),
    'unique_cpc_level4_codes': len(cpc_level4_set),
    'cpc_codes_with_ema': len(cpc_ema_results),
    'sample_results': {k: v for k, v in list(cpc_ema_results.items())[:5]}
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In RU, the patent filing (app. number RU-2017142236-A) is held by Sletov Aleksandr Anatolevich and has publication no. RU-2682615-C1.', 'grant_date': 'Mar 19th, 2019', 'cpc': '[\n  {\n    "code": "A61D1/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/645",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/6425",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/64",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/60",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/58",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The RU patent application (number RU-2018105657-A) is held by OBSHCHESTVO S OGRANICHENNOJ OTVETSTVENNOSTYU VORMKHOLS VNEDRENIE and has publication no. RU-2681783-C1.', 'grant_date': 'Mar 12th, 2019', 'cpc': '[\n  {\n    "code": "E21B33/136",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E21B33/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th', 'cpc': '[\n  {\n    "code": "G01S13/42",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S5/18",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41G3/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41H13/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'Patent application (number RU-2016134259-A) from RU, owned by KVINETIK LTD, with publication number RU-2681957-C2.', 'grant_date': 'on March 14th, 2019', 'cpc': '[\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/37",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DK patent application (number DK-14719221-T) is held by JASKE WOLFGANG and has publication number DK-2965013-T3.', 'grant_date': 'July 8th, 2019', 'cpc': '[\n  {\n    "code": "F25B2339/047",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D17/02",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B2400/061",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02B10/70",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D2200/20",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02B30/52",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D17/0005",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02B30/18",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D2200/123",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DK patent filing (application number DK-14835716-T) is owned by UNIV OSLO HF and has pub. number DK-3069138-T3.', 'grant_date': '8th April 2019', 'cpc': '[\n  {\n    "code": "G01N33/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N33/56977",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N33/56977",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/572",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61K39/39",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N2333/70539",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/55527",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C07K14/70503",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C07K14/70539",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/5158",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61K39/0011",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N33/505",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K39/0011",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/5158",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The RU patent application (ID RU-2018146701-U) is held by [] and has publication no. RU-189707-U1.', 'grant_date': '2019, May 30th', 'cpc': '[\n  {\n    "code": "B60P1/48",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The ES patent application (ID ES-11727548-T) is assigned to LOHR IND and has pub. number ES-2713511-T3.', 'grant_date': '22nd May 2019', 'cpc': '[\n  {\n    "code": "B61D3/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B61D3/182",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B61D3/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B61D3/16",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02T30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In RU, the patent filing (application no. RU-2019124341-U) is owned by [] and has pub. number RU-193787-U1.', 'grant_date': '2019 on Nov 14th', 'cpc': '[\n  {\n    "code": "F16K17/192",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16L43/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.execute_python:8': {'total_de_patents': 68, 'second_half_2019_patents': 10, 'sample_patent': {'Patents_info': 'In DE, the patent application (number DE-102011108701-A) is belonging to SUMITOMO HEAVY INDUSTRIES and has pub. number DE-102011108701-B4.', 'grant_date': '2019, December 24th', 'cpc': '[\n  {\n    "code": "F16C33/4676",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16C33/4682",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16C33/4635",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'title_localized': '[\n  {\n    "language": "de",\n    "text": "Getriebevorrichtung der oszillierend innen eingreifenden Bauart",\n    "truncated": false\n  }\n]'}}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'german_patents_2019_total': 68, 'second_half_2019_patents': 10, 'unique_cpc_level4_codes': 32, 'cpc_level4_codes': ['B60K/0', 'B60K/3', 'B60N/3', 'B62D/0', 'B62D/1', 'F01D/0', 'F02D/0', 'F02D/1', 'F02D/2', 'F04D/6', 'F05D/1', 'F05D/8', 'F16C/4', 'F16D/0', 'F16D/1', 'F16F/3', 'G01L/0', 'G01L/2', 'G01M/2', 'G01N/6', 'G02B/0', 'G02B/1', 'G02B/2', 'G08B/0', 'H01L/0', 'H01L/1', 'H01L/3', 'H01L/4', 'H03L/0', 'H03L/1', 'H04L/0', 'Y02T/4']}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'total_level4_cpcs': 137, 'sample_cpcs': [{'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0'}, {'symbol': 'F28', 'titleFull': 'HEAT EXCHANGE IN GENERAL', 'level': '4.0'}, {'symbol': 'F25', 'titleFull': 'REFRIGERATION OR COOLING; COMBINED HEATING AND REFRIGERATION SYSTEMS; HEAT PUMP SYSTEMS; MANUFACTURE OR STORAGE OF ICE; LIQUEFACTION SOLIDIFICATION OF GASES', 'level': '4.0'}]}, 'var_functions.query_db:20': [{'symbol': 'B60K', 'titleFull': 'ARRANGEMENT OR MOUNTING OF PROPULSION UNITS OR OF TRANSMISSIONS IN VEHICLES; ARRANGEMENT OR MOUNTING OF PLURAL DIVERSE PRIME-MOVERS IN VEHICLES; AUXILIARY DRIVES FOR VEHICLES; INSTRUMENTATION OR DASHBOARDS FOR VEHICLES; ARRANGEMENTS IN CONNECTION WITH COOLING, AIR INTAKE, GAS EXHAUST OR FUEL SUPPLY OF PROPULSION UNITS IN VEHICLES', 'level': '5.0'}, {'symbol': 'B60K1/00', 'titleFull': 'Arrangement or mounting of electrical propulsion units', 'level': '7.0'}, {'symbol': 'B60K1/02', 'titleFull': 'Arrangement or mounting of electrical propulsion units comprising more than one electric motor', 'level': '8.0'}, {'symbol': 'B60K1/04', 'titleFull': 'Arrangement or mounting of electrical propulsion units of the electric storage means for propulsion', 'level': '8.0'}, {'symbol': 'B60K11/00', 'titleFull': 'Arrangement in connection with cooling of propulsion units', 'level': '7.0'}, {'symbol': 'B60K11/02', 'titleFull': 'Arrangement in connection with cooling of propulsion units with liquid cooling', 'level': '8.0'}, {'symbol': 'B60K11/04', 'titleFull': 'Arrangement or mounting of radiators, radiator shutters, or radiator blinds', 'level': '9.0'}, {'symbol': 'B60K11/06', 'titleFull': 'Arrangement in connection with cooling of propulsion units with air cooling', 'level': '8.0'}, {'symbol': 'B60K11/08', 'titleFull': 'Air inlets for cooling; Shutters or blinds therefor', 'level': '8.0'}, {'symbol': 'B60K11/085', 'titleFull': 'Air inlets for cooling; Shutters or blinds therefor with adjustable shutters or blinds', 'level': '9.0'}, {'symbol': 'B60K13/00', 'titleFull': 'Arrangement in connection with combustion air intake or gas exhaust of propulsion units', 'level': '7.0'}, {'symbol': 'B60K13/02', 'titleFull': 'Arrangement in connection with combustion air intake or gas exhaust of propulsion units concerning intake', 'level': '8.0'}, {'symbol': 'B60K13/04', 'titleFull': 'Arrangement in connection with combustion air intake or gas exhaust of propulsion units concerning exhaust', 'level': '8.0'}, {'symbol': 'B60K13/06', 'titleFull': 'Arrangement in connection with combustion air intake or gas exhaust of propulsion units using structural parts of the vehicle as ducts, e.g. frame parts', 'level': '8.0'}, {'symbol': 'B60K15/00', 'titleFull': 'Arrangement in connection with fuel supply of combustion engines or other fuel consuming energy converters, e.g. fuel cells; Mounting or construction of fuel tanks', 'level': '7.0'}, {'symbol': 'B60K15/01', 'titleFull': 'Arrangement of fuel conduits', 'level': '8.0'}, {'symbol': 'B60K15/013', 'titleFull': 'Arrangement of fuel conduits of gas conduits', 'level': '9.0'}, {'symbol': 'B60K15/03', 'titleFull': 'Fuel tanks', 'level': '8.0'}, {'symbol': 'B60K15/03006', 'titleFull': 'Gas tanks', 'level': '9.0'}, {'symbol': 'B60K15/03177', 'titleFull': 'Fuel tanks made of non-metallic material, e.g. plastics, or of a combination of non-metallic and metallic material', 'level': '9.0'}, {'symbol': 'B60K15/035', 'titleFull': 'Fuel tanks characterised by venting means', 'level': '9.0'}, {'symbol': 'B60K15/03504', 'titleFull': 'Fuel tanks characterised by venting means adapted to avoid loss of fuel or fuel vapour, e.g. with vapour recovery systems', 'level': '10.0'}, {'symbol': 'B60K15/03519', 'titleFull': 'Valve arrangements in the vent line', 'level': '10.0'}, {'symbol': 'B60K15/04', 'titleFull': 'Tank inlets', 'level': '9.0'}, {'symbol': 'B60K15/0403', 'titleFull': 'Anti-siphoning devices', 'level': '10.0'}, {'symbol': 'B60K15/0406', 'titleFull': 'Filler caps for fuel tanks', 'level': '10.0'}, {'symbol': 'B60K15/0409', 'titleFull': 'Provided with a lock', 'level': '11.0'}, {'symbol': 'B60K15/05', 'titleFull': 'Inlet covers', 'level': '10.0'}, {'symbol': 'B60K15/06', 'titleFull': 'Fuel tanks characterised by fuel reserve systems', 'level': '9.0'}, {'symbol': 'B60K15/061', 'titleFull': 'Fuel tanks characterised by fuel reserve systems with level control', 'level': '10.0'}, {'symbol': 'B60K15/063', 'titleFull': 'Arrangement of tanks', 'level': '9.0'}, {'symbol': 'B60K15/067', 'titleFull': 'Mounting of tanks', 'level': '10.0'}, {'symbol': 'B60K15/07', 'titleFull': 'Mounting of tanks of gas tanks', 'level': '11.0'}, {'symbol': 'B60K15/073', 'titleFull': 'Tank construction specially adapted to the vehicle', 'level': '9.0'}, {'symbol': 'B60K15/077', 'titleFull': 'Fuel tanks with means modifying or controlling distribution or motion of fuel, e.g. to prevent noise, surge, splash or fuel starvation', 'level': '9.0'}, {'symbol': 'B60K15/10', 'titleFull': 'Arrangement in connection with fuel supply of combustion engines or other fuel consuming energy converters, e.g. fuel cells; Mounting or construction of fuel tanks concerning gas-producing plants', 'level': '8.0'}, {'symbol': 'B60K16/00', 'titleFull': 'Arrangements in connection with power supply of propulsion units in vehicles from forces of nature, e.g. sun or wind', 'level': '7.0'}, {'symbol': 'B60K17/00', 'titleFull': 'Arrangement or mounting of transmissions in vehicles', 'level': '7.0'}, {'symbol': 'B60K17/02', 'titleFull': 'Arrangement or mounting of transmissions in vehicles characterised by arrangement, location, or kind of clutch', 'level': '8.0'}, {'symbol': 'B60K17/04', 'titleFull': 'Arrangement or mounting of transmissions in vehicles characterised by arrangement, location, or kind of gearing', 'level': '8.0'}, {'symbol': 'B60K17/043', 'titleFull': 'Transmission unit disposed in on near the vehicle wheel, or between the differential gear unit and the wheel', 'level': '9.0'}, {'symbol': 'B60K17/046', 'titleFull': 'Transmission unit disposed in on near the vehicle wheel, or between the differential gear unit and the wheel with planetary gearing having orbital motion', 'level': '10.0'}, {'symbol': 'B60K17/06', 'titleFull': 'Arrangement or mounting of transmissions in vehicles characterised by arrangement, location, or kind of gearing of change-speed gearing', 'level': '9.0'}, {'symbol': 'B60K17/08', 'titleFull': 'Arrangement or mounting of transmissions in vehicles characterised by arrangement, location, or kind of gearing of change-speed gearing of mechanical type', 'level': '10.0'}, {'symbol': 'B60K17/10', 'titleFull': 'Arrangement or mounting of transmissions in vehicles characterised by arrangement, location, or kind of gearing of fluid gearing', 'level': '9.0'}, {'symbol': 'B60K17/105', 'titleFull': 'Units comprising at least a part of the gearing and a torque-transmitting axle, e.g. transaxles', 'level': '10.0'}, {'symbol': 'B60K17/12', 'titleFull': 'Arrangement or mounting of transmissions in vehicles characterised by arrangement, location, or kind of gearing of electric gearing', 'level': '9.0'}, {'symbol': 'B60K17/14', 'titleFull': 'Arrangement or mounting of transmissions in vehicles characterised by arrangement, location, or kind of gearing the motor of fluid or electric gearing being disposed in or adjacent to traction wheel', 'level': '9.0'}, {'symbol': 'B60K17/145', 'titleFull': 'Arrangement or mounting of transmissions in vehicles characterised by arrangement, location, or kind of gearing the motor of fluid or electric gearing being disposed in or adjacent to traction wheel the electric gearing being disposed in or adjacent to traction wheel', 'level': '10.0'}, {'symbol': 'B60K17/16', 'titleFull': 'Arrangement or mounting of transmissions in vehicles characterised by arrangement, location, or kind of gearing of differential gearing', 'level': '9.0'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_second_half_2019_patents': 61, 'years_with_data': [2008, 2009, 2010, 2011, 2014, 2015, 2017, 2018], 'sample_counts': {'B60K/0': {'2014': 1}, 'B60K/3': {'2014': 1}, 'F16D/1': {'2014': 2}, 'F16D/0': {'2014': 1}, 'B62D/0': {'2010': 1}}}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
