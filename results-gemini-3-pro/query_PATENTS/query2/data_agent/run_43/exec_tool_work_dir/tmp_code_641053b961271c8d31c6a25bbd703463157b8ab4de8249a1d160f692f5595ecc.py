code = """import json

# Previous results (from execute_python, likely a JSON string)
results_raw = locals()['var_function-call-15678702396413894506']
if isinstance(results_raw, str):
    results = json.loads(results_raw)
else:
    results = results_raw

# Titles (from query_db, likely a list)
titles_raw = locals()['var_function-call-12278865680812567591']
if isinstance(titles_raw, str):
    # It might be a file path if large, but here it was small.
    # Or it might be a JSON string if the system converts it?
    # Let's try to check.
    try:
        titles_data = json.loads(titles_raw)
    except:
        # Maybe it's a file path?
        if titles_raw.endswith('.json'):
             with open(titles_raw, 'r') as f:
                 titles_data = json.load(f)
        else:
             # It might be the list itself if the variable is magically a list? 
             # But the error said "JSON object must be str... not list".
             # This implies titles_raw WAS a list in the previous failed call.
             titles_data = titles_raw 
else:
    titles_data = titles_raw

# Create a map for titles
title_map = {item['symbol']: item['titleFull'] for item in titles_data}

# Merge
final_list = []
for item in results:
    code = item['cpc_code']
    final_list.append({
        "Full Title": title_map.get(code, "Unknown"),
        "CPC Group Code": code,
        "Best Year": item['best_year'],
        "EMA": item['max_ema']
    })

# Sort by EMA descending
final_list.sort(key=lambda x: x['EMA'], reverse=True)

# Clean up for final output
output_list = []
for item in final_list:
    output_list.append({
        "Full Title": item['Full Title'],
        "CPC Group Code": item['CPC Group Code'],
        "Best Year": item['Best Year']
    })

print("__RESULT__:")
print(json.dumps(output_list))"""

env_args = {'var_function-call-14016306173097755035': 'file_storage/function-call-14016306173097755035.json', 'var_function-call-14016306173097755288': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-3425986448742959405': [{'symbol': 'C01', 'level': '4.0', 'titleFull': 'INORGANIC CHEMISTRY'}, {'symbol': 'C01B', 'level': '5.0', 'titleFull': 'NON-METALLIC ELEMENTS; COMPOUNDS THEREOF; METALLOIDS OR COMPOUNDS THEREOF NOT COVERED BY SUBCLASS C01C'}, {'symbol': 'C01B33/00', 'level': '7.0', 'titleFull': 'Silicon; Compounds thereof'}], 'var_function-call-3595820558278827425': [{'COUNT(*)': '55'}], 'var_function-call-14505097301841626708': [{'COUNT(*)': '12225'}], 'var_function-call-14453105091914346968': 'file_storage/function-call-14453105091914346968.json', 'var_function-call-15678702396413894506': [{'cpc_code': 'B60', 'best_year': 2021, 'max_ema': 38.57460379673363}, {'cpc_code': 'Y02', 'best_year': 2019, 'max_ema': 26.652548570930875}, {'cpc_code': 'G01', 'best_year': 2019, 'max_ema': 25.105454752397634}, {'cpc_code': 'F16', 'best_year': 2020, 'max_ema': 23.8508120095806}, {'cpc_code': 'H01', 'best_year': 2022, 'max_ema': 23.199342525177297}, {'cpc_code': 'A61', 'best_year': 2006, 'max_ema': 18.081913447582316}, {'cpc_code': 'Y10', 'best_year': 2006, 'max_ema': 17.11493892142644}, {'cpc_code': 'H02', 'best_year': 2022, 'max_ema': 13.813606643236245}, {'cpc_code': 'H04', 'best_year': 2005, 'max_ema': 12.158479714381368}, {'cpc_code': 'F02', 'best_year': 2016, 'max_ema': 11.289877215748232}, {'cpc_code': 'C07', 'best_year': 2002, 'max_ema': 9.770289067729793}, {'cpc_code': 'B62', 'best_year': 2021, 'max_ema': 8.887763005838973}, {'cpc_code': 'F01', 'best_year': 2019, 'max_ema': 8.213257541875148}, {'cpc_code': 'B01', 'best_year': 2004, 'max_ema': 7.216693327279564}, {'cpc_code': 'B23', 'best_year': 2021, 'max_ema': 6.571805863417892}, {'cpc_code': 'A47', 'best_year': 2021, 'max_ema': 6.308844420168036}, {'cpc_code': 'B29', 'best_year': 2019, 'max_ema': 6.080223623524964}, {'cpc_code': 'G02', 'best_year': 2019, 'max_ema': 5.834038756101203}, {'cpc_code': 'G08', 'best_year': 2020, 'max_ema': 4.733687244544231}, {'cpc_code': 'E05', 'best_year': 2013, 'max_ema': 4.6347396775977066}, {'cpc_code': 'F04', 'best_year': 2019, 'max_ema': 4.182669890882644}, {'cpc_code': 'H03', 'best_year': 2005, 'max_ema': 3.973216286438753}, {'cpc_code': 'C09', 'best_year': 2006, 'max_ema': 3.9480543469969676}, {'cpc_code': 'B41', 'best_year': 2007, 'max_ema': 3.8958507016456227}, {'cpc_code': 'F24', 'best_year': 2017, 'max_ema': 3.6934211721081147}, {'cpc_code': 'F05', 'best_year': 2019, 'max_ema': 3.347647125651038}, {'cpc_code': 'G07', 'best_year': 2014, 'max_ema': 2.8070849902870396}, {'cpc_code': 'B64', 'best_year': 2019, 'max_ema': 2.125910637557568}, {'cpc_code': 'B63', 'best_year': 1919, 'max_ema': 2.0}, {'cpc_code': 'C04', 'best_year': 2001, 'max_ema': 1.9566758419502572}, {'cpc_code': 'B66', 'best_year': 2021, 'max_ema': 1.9421514110887297}, {'cpc_code': 'F23', 'best_year': 2014, 'max_ema': 1.7523206692896691}, {'cpc_code': 'E02', 'best_year': 2017, 'max_ema': 1.563229482045147}, {'cpc_code': 'E21', 'best_year': 2008, 'max_ema': 1.242109359920371}, {'cpc_code': 'F41', 'best_year': 2020, 'max_ema': 1.030754538563516}, {'cpc_code': 'A21', 'best_year': 1964, 'max_ema': 1.0}, {'cpc_code': 'F42', 'best_year': 1885, 'max_ema': 1.0}, {'cpc_code': 'A43', 'best_year': 1911, 'max_ema': 1.0}, {'cpc_code': 'A24', 'best_year': 1905, 'max_ema': 1.0}], 'var_function-call-12278865680812567591': [{'symbol': 'B29', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL'}, {'symbol': 'A24', 'titleFull': "TOBACCO; CIGARS; CIGARETTES; SIMULATED SMOKING DEVICES; SMOKERS' REQUISITES"}, {'symbol': 'A61', 'titleFull': 'MEDICAL OR VETERINARY SCIENCE; HYGIENE'}, {'symbol': 'A43', 'titleFull': 'FOOTWEAR'}, {'symbol': 'A47', 'titleFull': 'FURNITURE; DOMESTIC ARTICLES OR APPLIANCES; COFFEE MILLS; SPICE MILLS; SUCTION CLEANERS IN GENERAL'}, {'symbol': 'A21', 'titleFull': 'BAKING; EDIBLE DOUGHS'}, {'symbol': 'B66', 'titleFull': 'HOISTING; LIFTING; HAULING'}, {'symbol': 'B62', 'titleFull': 'LAND VEHICLES FOR TRAVELLING OTHERWISE THAN ON RAILS'}, {'symbol': 'B64', 'titleFull': 'AIRCRAFT; AVIATION; COSMONAUTICS'}, {'symbol': 'B01', 'titleFull': 'PHYSICAL OR CHEMICAL PROCESSES OR APPARATUS IN GENERAL'}, {'symbol': 'B63', 'titleFull': 'SHIPS OR OTHER WATERBORNE VESSELS; RELATED EQUIPMENT'}, {'symbol': 'B60', 'titleFull': 'VEHICLES IN GENERAL'}, {'symbol': 'B41', 'titleFull': 'PRINTING; LINING MACHINES; TYPEWRITERS; STAMPS'}, {'symbol': 'C07', 'titleFull': 'ORGANIC CHEMISTRY'}, {'symbol': 'C04', 'titleFull': 'CEMENTS; CONCRETE; ARTIFICIAL STONE; CERAMICS; REFRACTORIES'}, {'symbol': 'C09', 'titleFull': 'DYES; PAINTS; POLISHES; NATURAL RESINS; ADHESIVES; COMPOSITIONS NOT OTHERWISE PROVIDED FOR; APPLICATIONS OF MATERIALS NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'E05', 'titleFull': 'LOCKS; KEYS; WINDOW OR DOOR FITTINGS; SAFES'}, {'symbol': 'E21', 'titleFull': 'EARTH OR ROCK DRILLING; MINING'}, {'symbol': 'E02', 'titleFull': 'HYDRAULIC ENGINEERING; FOUNDATIONS; SOIL SHIFTING'}, {'symbol': 'F41', 'titleFull': 'WEAPONS'}, {'symbol': 'F01', 'titleFull': 'MACHINES OR ENGINES IN GENERAL; ENGINE PLANTS IN GENERAL; STEAM ENGINES'}, {'symbol': 'F04', 'titleFull': 'POSITIVE - DISPLACEMENT MACHINES FOR LIQUIDS; PUMPS FOR LIQUIDS OR ELASTIC FLUIDS'}, {'symbol': 'F16', 'titleFull': 'ENGINEERING ELEMENTS AND UNITS; GENERAL MEASURES FOR PRODUCING AND MAINTAINING EFFECTIVE FUNCTIONING OF MACHINES OR INSTALLATIONS; THERMAL INSULATION IN GENERAL'}, {'symbol': 'F05', 'titleFull': 'INDEXING SCHEMES RELATING TO ENGINES OR PUMPS IN VARIOUS SUBCLASSES OF CLASSES F01-F04'}, {'symbol': 'F42', 'titleFull': 'AMMUNITION; BLASTING'}, {'symbol': 'F02', 'titleFull': 'COMBUSTION ENGINES; HOT-GAS OR COMBUSTION-PRODUCT ENGINE PLANTS'}, {'symbol': 'F23', 'titleFull': 'COMBUSTION APPARATUS; COMBUSTION PROCESSES'}, {'symbol': 'F24', 'titleFull': 'HEATING; RANGES; VENTILATING'}, {'symbol': 'G08', 'titleFull': 'SIGNALLING'}, {'symbol': 'G02', 'titleFull': 'OPTICS'}, {'symbol': 'G01', 'titleFull': 'MEASURING; TESTING'}, {'symbol': 'G07', 'titleFull': 'CHECKING-DEVICES'}, {'symbol': 'H03', 'titleFull': 'ELECTRONIC CIRCUITRY'}, {'symbol': 'H04', 'titleFull': 'ELECTRIC COMMUNICATION TECHNIQUE'}, {'symbol': 'H01', 'titleFull': 'ELECTRIC ELEMENTS'}, {'symbol': 'H02', 'titleFull': 'GENERATION; CONVERSION OR DISTRIBUTION OF ELECTRIC POWER'}, {'symbol': 'Y02', 'titleFull': 'TECHNOLOGIES OR APPLICATIONS FOR MITIGATION OR ADAPTATION AGAINST CLIMATE CHANGE'}, {'symbol': 'Y10', 'titleFull': 'TECHNICAL SUBJECTS COVERED BY FORMER USPC'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}]}

exec(code, env_args)
