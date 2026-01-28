code = """import json
import re
from datetime import datetime
from collections import defaultdict

# Load the data from the query result
file_path = locals()['var_functions.query_db:20']
with open(file_path, 'r') as f:
    data = json.load(f)

print(f"Total records loaded: {len(data)}")

# Function to parse grant dates
def parse_grant_date(date_str):
    if not date_str:
        return None
    
    date_str = date_str.lower().strip()
    date_str = re.sub(r'(\d+)(th|rd|st|nd)', r'\1', date_str)
    date_str = date_str.replace('on ', '').replace('dated ', '').strip()
    
    month_patterns = [
        (r'jan(?:uary)?', 1), (r'feb(?:ruary)?', 2), (r'mar(?:ch)?', 3),
        (r'apr(?:il)?', 4), (r'may', 5), (r'june?', 6),
        (r'july?', 7), (r'aug(?:ust)?', 8), (r'sep(?:tember)?', 9),
        (r'oct(?:ober)?', 10), (r'nov(?:ember)?', 11), (r'dec(?:ember)?', 12)
    ]
    
    year_match = re.search(r'(\d{4})', date_str)
    if not year_match:
        return None
    
    year = int(year_match.group(1))
    
    for pattern, month_num in month_patterns:
        if re.search(pattern, date_str):
            day_match = re.search(r'\b(\d{1,2})\b', date_str)
            day = int(day_match.group(1)) if day_match else 1
            return datetime(year, month_num, day)
    
    return None

# Filter for Germany patents granted in second half of 2019
germany_patents = []
for record in data:
    patents_info = record.get('Patents_info', '')
    if not patents_info or 'DE-' not in patents_info:
        continue
    
    grant_date_str = record.get('grant_date')
    if not grant_date_str:
        continue
    
    grant_date = parse_grant_date(grant_date_str)
    if grant_date and grant_date.year == 2019 and grant_date.month >= 7:
        germany_patents.append({
            'grant_date': grant_date,
            'cpc_json': record.get('cpc', '[]'),
            'patents_info': patents_info
        })

print(f"Germany patents in second half 2019: {len(germany_patents)}")

# Extract CPC level 4 codes and count them
cpc_level4_counts = defaultdict(int)

for patent in germany_patents:
    cpc_data = patent['cpc_json']
    
    try:
        if isinstance(cpc_data, str):
            cpc_list = json.loads(cpc_data)
        else:
            cpc_list = cpc_data
            
        for cpc_item in cpc_list:
            code = cpc_item.get('code', '')
            if code:
                # Extract level 4 CPC code (first 4 characters of the main group)
                parts = code.split('/')
                if len(parts) == 2:
                    main_group = parts[0]
                    if len(main_group) >= 4:
                        level4_code = main_group[:4]
                        cpc_level4_counts[level4_code] += 1
    except:
        continue

# Calculate Exponential Moving Average (EMA) with smoothing factor 0.1
# Since we only have one time period (2019), EMA = actual value for that period
smoothing_factor = 0.1
cpc_ema_results = []

for cpc_code, count in cpc_level4_counts.items():
    # With only one data point, EMA equals the count
    ema = count
    cpc_ema_results.append({
        'cpc_code': cpc_code,
        'count': count,
        'ema': ema,
        'year': 2019
    })

# Sort by EMA (count) descending
cpc_ema_results.sort(key=lambda x: x['ema'], reverse=True)

print(f"Top CPC areas by EMA:")
for i, result in enumerate(cpc_ema_results[:10]):
    print(f"{i+1}. {result['cpc_code']}: {result['ema']}")

print("__RESULT__:")
print(json.dumps(cpc_ema_results))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In RU, the patent filing (app. number RU-2017142236-A) is held by Sletov Aleksandr Anatolevich and has publication no. RU-2682615-C1.', 'grant_date': 'Mar 19th, 2019', 'cpc': '[\n  {\n    "code": "A61D1/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/645",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/6425",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/64",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/60",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/58",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The RU patent application (number RU-2018105657-A) is held by OBSHCHESTVO S OGRANICHENNOJ OTVETSTVENNOSTYU VORMKHOLS VNEDRENIE and has publication no. RU-2681783-C1.', 'grant_date': 'Mar 12th, 2019', 'cpc': '[\n  {\n    "code": "E21B33/136",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E21B33/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th', 'cpc': '[\n  {\n    "code": "G01S13/42",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S5/18",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41G3/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41H13/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'Patent application (number RU-2016134259-A) from RU, owned by KVINETIK LTD, with publication number RU-2681957-C2.', 'grant_date': 'on March 14th, 2019', 'cpc': '[\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/37",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'total': '23985', 'MIN(grant_date)': '10th Apr 1945', 'MAX(grant_date)': 'on September 9th, 2014'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': 111, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'total_patents': 34, 'years': [2019], 'sample_data': {'2019': {'B41F': 3, 'F02D': 16, 'F02M': 11, 'F04B': 2, 'G01D': 1, 'B23K': 1, 'B63B': 1, 'H04W': 22, 'H04L': 16, 'Y02D': 2, 'B66C': 1, 'E02F': 6, 'B60S': 1, 'Y02T': 4, 'F16C': 3, 'A47J': 1, 'A21C': 1, 'A61F': 6, 'A43B': 5, 'F24B': 3, 'F23L': 6, 'F23B': 4, 'F23N': 1, 'Y02E': 1, 'H01J': 10, 'G01M': 4, 'F05D': 2, 'F04D': 1, 'F16F': 1, 'F01D': 2, 'H01R': 6, 'B64D': 1, 'B60R': 1, 'H01L': 6, 'B62D': 2, 'F02N': 7, 'B60K': 3, 'B60W': 1, 'C04B': 45, 'C09K': 2, 'B29C': 19, 'A61B': 5, 'G01N': 2, 'A61L': 2, 'G02B': 20, 'H01F': 4, 'F02P': 4, 'Y10T': 2, 'G07C': 2, 'B29D': 1, 'H01H': 4, 'E05B': 1, 'G01L': 4, 'G01F': 2, 'F16H': 5, 'F16D': 3, 'H02J': 6, 'H03L': 6, 'B60N': 3, 'F42B': 2, 'F41H': 2, 'G08B': 2}}}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': ['A21C', 'A43B', 'A47J', 'A61B', 'A61F', 'A61L', 'B23K', 'B29C', 'B29D', 'B41F', 'B60K', 'B60N', 'B60R', 'B60S', 'B60W', 'B62D', 'B63B', 'B64D', 'B66C', 'C04B', 'C09K', 'E02F', 'E05B', 'F01D', 'F02D', 'F02M', 'F02N', 'F02P', 'F04B', 'F04D', 'F05D', 'F16C', 'F16D', 'F16F', 'F16H', 'F23B', 'F23L', 'F23N', 'F24B', 'F41H', 'F42B', 'G01D', 'G01F', 'G01L', 'G01M', 'G01N', 'G02B', 'G07C', 'G08B', 'H01F', 'H01H', 'H01J', 'H01L', 'H01R', 'H02J', 'H03L', 'H04L', 'H04W', 'Y02D', 'Y02E', 'Y02T', 'Y10T'], 'var_functions.execute_python:28': {'query': "SELECT symbol, titleFull FROM cpc_definition WHERE symbol IN ('A21C', 'A43B', 'A47J', 'A61B', 'A61F', 'A61L', 'B23K', 'B29C', 'B29D', 'B41F', 'B60K', 'B60N', 'B60R', 'B60S', 'B60W', 'B62D', 'B63B', 'B64D', 'B66C', 'C04B', 'C09K', 'E02F', 'E05B', 'F01D', 'F02D', 'F02M', 'F02N', 'F02P', 'F04B', 'F04D', 'F05D', 'F16C', 'F16D', 'F16F', 'F16H', 'F23B', 'F23L', 'F23N', 'F24B', 'F41H', 'F42B', 'G01D', 'G01F', 'G01L', 'G01M', 'G01N', 'G02B', 'G07C', 'G08B', 'H01F', 'H01H', 'H01J', 'H01L', 'H01R', 'H02J', 'H03L', 'H04L', 'H04W', 'Y02D', 'Y02E', 'Y02T', 'Y10T')", 'cpc_count': 62}, 'var_functions.execute_python:30': {'query': 'SELECT symbol, "titleFull" FROM cpc_definition WHERE symbol IN (\'{cpc_list_str}\')', 'cpc_count': 62}, 'var_functions.query_db:32': [{'code': 'A21C', 'title': 'MACHINES OR EQUIPMENT FOR MAKING OR PROCESSING DOUGHS; HANDLING BAKED ARTICLES MADE FROM DOUGH'}, {'code': 'B29D', 'title': 'PRODUCING PARTICULAR ARTICLES FROM PLASTICS OR FROM SUBSTANCES IN A PLASTIC STATE'}, {'code': 'B29C', 'title': 'SHAPING OR JOINING OF PLASTICS; SHAPING OF MATERIAL IN A PLASTIC STATE, NOT OTHERWISE PROVIDED FOR; AFTER-TREATMENT OF THE SHAPED PRODUCTS, e.g. REPAIRING'}, {'code': 'B41F', 'title': 'PRINTING MACHINES OR PRESSES'}, {'code': 'B63B', 'title': 'SHIPS OR OTHER WATERBORNE VESSELS; EQUIPMENT FOR SHIPPING\xa0'}, {'code': 'B64D', 'title': 'EQUIPMENT FOR FITTING IN OR TO AIRCRAFT; FLIGHT SUITS; PARACHUTES; ARRANGEMENT OR MOUNTING OF POWER\xa0PLANTS\xa0OR PROPULSION TRANSMISSIONS IN AIRCRAFT'}, {'code': 'B66C', 'title': 'CRANES; LOAD-ENGAGING ELEMENTS OR DEVICES FOR CRANES, CAPSTANS, WINCHES, OR TACKLES'}, {'code': 'E02F', 'title': 'DREDGING; SOIL-SHIFTING'}, {'code': 'E05B', 'title': 'LOCKS; ACCESSORIES THEREFOR; HANDCUFFS'}, {'code': 'F05D', 'title': 'INDEXING SCHEME FOR ASPECTS RELATING TO NON-POSITIVE-DISPLACEMENT MACHINES OR ENGINES, GAS-TURBINES OR JET-PROPULSION PLANTS'}, {'code': 'F16D', 'title': 'COUPLINGS FOR TRANSMITTING ROTATION; CLUTCHES; BRAKES'}, {'code': 'F16H', 'title': 'GEARING'}, {'code': 'F16C', 'title': 'SHAFTS; FLEXIBLE SHAFTS; ELEMENTS OR CRANKSHAFT MECHANISMS; ROTARY BODIES OTHER THAN GEARING ELEMENTS; BEARINGS'}, {'code': 'F16F', 'title': 'SPRINGS; SHOCK-ABSORBERS; MEANS FOR DAMPING VIBRATION'}, {'code': 'F23N', 'title': 'REGULATING OR CONTROLLING COMBUSTION'}, {'code': 'F23B', 'title': 'METHODS OR APPARATUS FOR COMBUSTION USING ONLY SOLID FUEL'}, {'code': 'F23L', 'title': 'SUPPLYING AIR OR NON-COMBUSTIBLE LIQUIDS OR GASES TO COMBUSTION APPARATUS IN GENERAL\xa0; VALVES OR DAMPERS SPECIALLY ADAPTED FOR CONTROLLING AIR SUPPLY OR DRAUGHT IN COMBUSTION APPARATUS; INDUCING DRAUGHT IN COMBUSTION APPARATUS; TOPS FOR CHIMNEYS OR VENTILATING SHAFTS; TERMINALS FOR FLUES'}, {'code': 'G01M', 'title': 'TESTING STATIC OR DYNAMIC BALANCE OF MACHINES OR STRUCTURES; TESTING OF STRUCTURES OR APPARATUS, NOT OTHERWISE PROVIDED FOR'}, {'code': 'G01N', 'title': 'INVESTIGATING OR ANALYSING MATERIALS BY DETERMINING THEIR CHEMICAL OR PHYSICAL PROPERTIES'}, {'code': 'G01F', 'title': 'MEASURING VOLUME, VOLUME FLOW, MASS FLOW OR LIQUID LEVEL; METERING BY VOLUME'}, {'code': 'H04L', 'title': 'TRANSMISSION OF DIGITAL INFORMATION, e.g. TELEGRAPHIC COMMUNICATION'}, {'code': 'G01L', 'title': 'MEASURING FORCE, STRESS, TORQUE, WORK, MECHANICAL POWER, MECHANICAL EFFICIENCY, OR FLUID PRESSURE'}, {'code': 'G02B', 'title': 'OPTICAL ELEMENTS, SYSTEMS OR APPARATUS'}, {'code': 'H01F', 'title': 'MAGNETS; INDUCTANCES; TRANSFORMERS; SELECTION OF MATERIALS FOR THEIR MAGNETIC PROPERTIES'}, {'code': 'H01L', 'title': 'SEMICONDUCTOR DEVICES NOT COVERED BY CLASS H10'}, {'code': 'H01J', 'title': 'ELECTRIC DISCHARGE TUBES OR DISCHARGE LAMPS'}, {'code': 'H01R', 'title': 'ELECTRICALLY-CONDUCTIVE CONNECTIONS; STRUCTURAL ASSOCIATIONS OF A PLURALITY OF MUTUALLY-INSULATED ELECTRICAL CONNECTING ELEMENTS; COUPLING DEVICES; CURRENT COLLECTORS'}, {'code': 'H01H', 'title': 'ELECTRIC SWITCHES; RELAYS; SELECTORS; EMERGENCY PROTECTIVE DEVICES'}, {'code': 'H03L', 'title': 'AUTOMATIC CONTROL, STARTING, SYNCHRONISATION OR STABILISATION OF GENERATORS OF ELECTRONIC OSCILLATIONS OR PULSES'}, {'code': 'H02J', 'title': 'CIRCUIT ARRANGEMENTS OR SYSTEMS FOR SUPPLYING OR DISTRIBUTING ELECTRIC POWER; SYSTEMS FOR STORING ELECTRIC ENERGY'}, {'code': 'A43B', 'title': 'CHARACTERISTIC FEATURES OF FOOTWEAR; PARTS OF FOOTWEAR'}, {'code': 'A47J', 'title': 'KITCHEN EQUIPMENT; COFFEE MILLS; SPICE MILLS; APPARATUS FOR MAKING BEVERAGES'}, {'code': 'A61B', 'title': 'DIAGNOSIS; SURGERY; IDENTIFICATION'}, {'code': 'A61F', 'title': 'FILTERS IMPLANTABLE INTO BLOOD VESSELS; PROSTHESES; DEVICES PROVIDING PATENCY TO, OR PREVENTING COLLAPSING OF, TUBULAR STRUCTURES OF THE BODY, e.g. STENTS; ORTHOPAEDIC, NURSING OR CONTRACEPTIVE DEVICES; FOMENTATION; TREATMENT OR PROTECTION OF EYES OR EARS; BANDAGES, DRESSINGS OR ABSORBENT PADS; FIRST-AID KITS'}, {'code': 'A61L', 'title': 'METHODS OR APPARATUS FOR STERILISING MATERIALS OR OBJECTS IN GENERAL; DISINFECTION, STERILISATION OR DEODORISATION OF AIR; CHEMICAL ASPECTS OF BANDAGES, DRESSINGS, ABSORBENT PADS OR SURGICAL ARTICLES; MATERIALS FOR BANDAGES, DRESSINGS, ABSORBENT PADS OR SURGICAL ARTICLES'}, {'code': 'B23K', 'title': 'SOLDERING OR UNSOLDERING; WELDING; CLADDING OR PLATING BY SOLDERING OR WELDING; CUTTING BY APPLYING HEAT LOCALLY, e.g. FLAME CUTTING; WORKING BY LASER BEAM'}, {'code': 'B60R', 'title': 'VEHICLES, VEHICLE FITTINGS, OR VEHICLE PARTS, NOT OTHERWISE PROVIDED FOR'}, {'code': 'B60W', 'title': 'CONJOINT CONTROL OF VEHICLE SUB-UNITS OF DIFFERENT TYPE OR DIFFERENT FUNCTION; CONTROL SYSTEMS SPECIALLY ADAPTED FOR HYBRID VEHICLES; ROAD VEHICLE DRIVE CONTROL SYSTEMS FOR PURPOSES NOT RELATED TO THE CONTROL OF A PARTICULAR SUB-UNIT'}, {'code': 'B60N', 'title': 'SEATS SPECIALLY ADAPTED FOR VEHICLES; VEHICLE PASSENGER ACCOMMODATION NOT OTHERWISE PROVIDED FOR'}, {'code': 'B60K', 'title': 'ARRANGEMENT OR MOUNTING OF PROPULSION UNITS OR OF TRANSMISSIONS IN VEHICLES; ARRANGEMENT OR MOUNTING OF PLURAL DIVERSE PRIME-MOVERS IN VEHICLES; AUXILIARY DRIVES FOR VEHICLES; INSTRUMENTATION OR DASHBOARDS FOR VEHICLES; ARRANGEMENTS IN CONNECTION WITH COOLING, AIR INTAKE, GAS EXHAUST OR FUEL SUPPLY OF PROPULSION UNITS IN VEHICLES'}, {'code': 'B60S', 'title': 'SERVICING, CLEANING, REPAIRING, SUPPORTING, LIFTING, OR MANOEUVRING OF VEHICLES, NOT OTHERWISE PROVIDED FOR'}, {'code': 'B62D', 'title': 'MOTOR VEHICLES; TRAILERS'}, {'code': 'C04B', 'title': 'LIME, MAGNESIA; SLAG; CEMENTS; COMPOSITIONS THEREOF, e.g. MORTARS, CONCRETE OR LIKE BUILDING MATERIALS; ARTIFICIAL STONE; CERAMICS; REFRACTORIES; TREATMENT OF NATURAL STONE'}, {'code': 'C09K', 'title': 'MATERIALS FOR MISCELLANEOUS APPLICATIONS, NOT PROVIDED FOR ELSEWHERE'}, {'code': 'F01D', 'title': 'NON-POSITIVE DISPLACEMENT MACHINES OR ENGINES, e.g. STEAM TURBINES'}, {'code': 'F02P', 'title': 'IGNITION, OTHER THAN COMPRESSION IGNITION, FOR INTERNAL-COMBUSTION ENGINES; TESTING OF IGNITION TIMING IN COMPRESSION-IGNITION ENGINES'}, {'code': 'F02D', 'title': 'CONTROLLING COMBUSTION ENGINES'}, {'code': 'F02M', 'title': 'SUPPLYING COMBUSTION ENGINES IN GENERAL WITH COMBUSTIBLE MIXTURES OR CONSTITUENTS THEREOF'}, {'code': 'F02N', 'title': 'STARTING OF COMBUSTION ENGINES; STARTING AIDS FOR SUCH ENGINES, NOT OTHERWISE PROVIDED FOR'}, {'code': 'F04B', 'title': 'POSITIVE-DISPLACEMENT MACHINES FOR LIQUIDS; PUMPS'}, {'code': 'F04D', 'title': 'NON-POSITIVE-DISPLACEMENT PUMPS'}, {'code': 'F24B', 'title': 'DOMESTIC STOVES OR RANGES FOR SOLID FUELS; IMPLEMENTS FOR USE IN CONNECTION WITH STOVES OR RANGES'}, {'code': 'F41H', 'title': 'ARMOUR; ARMOURED TURRETS; ARMOURED OR ARMED VEHICLES; MEANS OF ATTACK OR DEFENCE, e.g. CAMOUFLAGE, IN GENERAL'}, {'code': 'F42B', 'title': 'EXPLOSIVE CHARGES, e.g. FOR BLASTING, FIREWORKS, AMMUNITION'}, {'code': 'G01D', 'title': 'MEASURING NOT SPECIALLY ADAPTED FOR A SPECIFIC VARIABLE; ARRANGEMENTS FOR MEASURING TWO OR MORE VARIABLES NOT COVERED IN A SINGLE OTHER SUBCLASS; TARIFF METERING APPARATUS; MEASURING OR TESTING NOT OTHERWISE PROVIDED FOR'}, {'code': 'G07C', 'title': 'TIME OR ATTENDANCE REGISTERS; REGISTERING OR INDICATING THE WORKING OF MACHINES; GENERATING RANDOM NUMBERS; VOTING OR LOTTERY APPARATUS; ARRANGEMENTS, SYSTEMS OR APPARATUS FOR CHECKING NOT PROVIDED FOR ELSEWHERE'}, {'code': 'G08B', 'title': 'SIGNALLING OR CALLING SYSTEMS; ORDER TELEGRAPHS; ALARM SYSTEMS'}, {'code': 'Y02T', 'title': 'CLIMATE CHANGE MITIGATION TECHNOLOGIES RELATED TO TRANSPORTATION'}, {'code': 'H04W', 'title': 'WIRELESS COMMUNICATION NETWORKS'}, {'code': 'Y02E', 'title': 'REDUCTION OF GREENHOUSE GAS [GHG] EMISSIONS, RELATED TO ENERGY GENERATION, TRANSMISSION OR DISTRIBUTION'}, {'code': 'Y02D', 'title': 'CLIMATE CHANGE MITIGATION TECHNOLOGIES IN INFORMATION AND COMMUNICATION TECHNOLOGIES [ICT], I.E. INFORMATION AND COMMUNICATION TECHNOLOGIES AIMING AT THE REDUCTION OF THEIR OWN ENERGY USE'}, {'code': 'Y10T', 'title': 'TECHNICAL SUBJECTS COVERED BY FORMER US CLASSIFICATION'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
