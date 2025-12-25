code = """import json
import re

# Load Filings
with open(locals()['var_function-call-7782197232993617340'], 'r') as f:
    filings_data = json.load(f)

# Load Level 5 CPC symbols
with open(locals()['var_function-call-16702837744120307450'], 'r') as f:
    cpc_level5_data = json.load(f)

valid_cpc_level5 = set()
for item in cpc_level5_data:
    if 'symbol' in item:
        valid_cpc_level5.add(item['symbol'])

cpc_counts = {}
global_years = set()

for filing in filings_data:
    f_date = filing.get('filing_date', '')
    if not f_date:
        continue
    
    match = re.search(r'(18|19|20)\d{2}', f_date)
    if match:
        year = int(match.group(0))
        # Sanity check on year
        if 1800 <= year <= 2024:
            global_years.add(year)
        else:
            continue
    else:
        continue
    
    cpc_json_str = filing.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_json_str)
    except:
        continue
    
    seen_codes = set()
    for entry in cpc_list:
        code = entry.get('code', '')
        if len(code) >= 4:
            subclass = code[:4]
            if subclass in valid_cpc_level5:
                seen_codes.add(subclass)
                
    for code in seen_codes:
        if code not in cpc_counts:
            cpc_counts[code] = {}
        cpc_counts[code][year] = cpc_counts[code].get(year, 0) + 1

if not global_years:
    print("__RESULT__:")
    print("[]")
    exit()

min_year = min(global_years)
max_year = max(global_years)

alpha = 0.2
result_cpc_codes = []

# Ensure 2022 is in range if we want to check for it
effective_max_year = max(max_year, 2022)

for cpc, year_counts in cpc_counts.items():
    
    ema = year_counts.get(min_year, 0)
    
    best_ema = ema
    best_year = min_year
        
    for y in range(min_year + 1, effective_max_year + 1):
        count = year_counts.get(y, 0)
        ema = alpha * count + (1 - alpha) * ema
        
        # Use >= to update best_year to the latest year with the max value
        if ema >= best_ema:
            best_ema = ema
            best_year = y
            
    if best_year == 2022:
        result_cpc_codes.append(cpc)

# Sorting the result for deterministic output
result_cpc_codes.sort()

print("__RESULT__:")
print(json.dumps(result_cpc_codes))"""

env_args = {'var_function-call-15891582207541011171': 'file_storage/function-call-15891582207541011171.json', 'var_function-call-11737208954615889978': [{'count(*)': '277813'}], 'var_function-call-16702837744120307450': 'file_storage/function-call-16702837744120307450.json', 'var_function-call-1429926228084239010': [{'symbol': 'A01K2227/108', 'level': '9.0', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'level': '9.0', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'level': '9.0', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'level': '9.0', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'level': '9.0', 'titleFull': 'Ovine'}, {'symbol': 'A01K2227/106', 'level': '9.0', 'titleFull': 'Primate'}, {'symbol': 'A01K2227/706', 'level': '9.0', 'titleFull': 'Insects, e.g. Drosophila melanogaster, medfly'}, {'symbol': 'A01K2227/703', 'level': '9.0', 'titleFull': 'Worms, e.g. Caenorhabdities elegans'}, {'symbol': 'A01K2267/025', 'level': '9.0', 'titleFull': 'Animal producing cells or organs for transplantation'}, {'symbol': 'A01K2267/0393', 'level': '9.0', 'titleFull': 'Animal model comprising a reporter system for screening tests'}], 'var_function-call-7073709861002867650': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}, {'symbol': 'A01N', 'level': '5.0', 'titleFull': 'PRESERVATION OF BODIES OF HUMANS OR ANIMALS OR PLANTS OR PARTS THEREOF; BIOCIDES, e.g. AS DISINFECTANTS, AS PESTICIDES OR AS HERBICIDES; PEST REPELLANTS OR ATTRACTANTS; PLANT GROWTH REGULATORS'}, {'symbol': 'A01P', 'level': '5.0', 'titleFull': 'BIOCIDAL, PEST REPELLANT, PEST ATTRACTANT OR PLANT GROWTH REGULATORY ACTIVITY OF CHEMICAL COMPOUNDS OR PREPARATIONS'}, {'symbol': 'A01D', 'level': '5.0', 'titleFull': 'HARVESTING; MOWING'}, {'symbol': 'A01L', 'level': '5.0', 'titleFull': 'SHOEING OF ANIMALS'}, {'symbol': 'A01K', 'level': '5.0', 'titleFull': 'ANIMAL HUSBANDRY; AVICULTURE; APICULTURE; PISCICULTURE; FISHING; REARING OR BREEDING ANIMALS, NOT OTHERWISE PROVIDED FOR; NEW BREEDS OF ANIMALS'}], 'var_function-call-7782197232993617340': 'file_storage/function-call-7782197232993617340.json', 'var_function-call-2550816962134600101': [], 'var_function-call-1889060731742213001': {'sample_dates': ['dated 5th March 2019', 'March the 18th, 2019', '29th March 2019', 'on March 29th, 2019', '2nd April 2019', 'on April 8th, 2019', '15th April 2019', 'April 19th, 2019', '2019, April 24th', 'April 26th, 2019', 'on April 30th, 2019', 'dated 1st May 2019', '2019, May 15th', 'May 15th, 2019', 'June the 6th, 2019', 'on June 7th, 2019', '14th of June, 2019', '2019 on Jun 14th', 'dated 18th June 2019', 'June the 19th, 2019', '5th of July, 2019', '2019 on Jul 12th', 'July the 16th, 2019', 'on July 17th, 2019', 'on August 13th, 2019', '30th Aug 2019', 'August 30th, 2019', 'September the 3rd, 2019', '2019, September 4th', 'September the 6th, 2019', '2019 on Sep 9th', '10th Sep 2019', 'on September 16th, 2019', '2019, September 18th', 'on September 24th, 2019', '25th September 2019', 'September the 26th, 2019', 'Sep 27th, 2019', 'October 4th, 2019', 'Oct 24th, 2019', 'on October 30th, 2019', 'October 30th, 2019', '30th of October, 2019', '7th of November, 2019', '20th Nov 2019', '21st November 2019', 'dated 22nd November 2019', '2nd Dec 2019', '2019 on Dec 6th', 'dated 16th December 2019', '16th Dec 2019', 'December 23rd, 2019', 'Dec 26th, 2019', '30th of December, 2019', '1st Mar 2019', 'January the 17th, 2019', '19th April 2019', 'June 13th, 2019', '2019, June 29th', '28th of May, 2019', '24th Jan 2020', 'January 29th, 2020', 'on January 31st, 2020', '10th February 2020', '14th of February, 2020', 'on February 28th, 2020', 'Feb 28th, 2020', 'dated 2nd March 2020', '5th of March, 2020', 'dated 11th March 2020', 'on March 13th, 2020', '13th of March, 2020', 'dated 18th March 2020', 'on March 23rd, 2020', 'on March 23rd, 2020', 'Mar 25th, 2020', '26th March 2020', 'Apr 22nd, 2020', 'dated 24th April 2020', '24th April 2020', 'April the 29th, 2020', 'dated 29th April 2020', 'May the 1st, 2020', 'May 21st, 2020', '2nd June 2020', '2020, June 7th', '2020 on Jun 17th', '18th Jun 2020', 'June the 25th, 2020', '29th June 2020', 'Jun 29th, 2020', '30th of June, 2020', '2020 on Jul 7th', '9th Jul 2020', 'July 23rd, 2020', 'on June 29th, 2020', 'August the 3rd, 2020', 'on August 7th, 2020', 'September the 3rd, 2020', 'Sep 9th, 2020'], 'extracted_years': [], 'sample_cpc_codes': ['C01B33/00', 'C01B35/00', 'H01M10/0565', 'H01M10/0562', 'C01G45/006', 'H01M10/0566', 'H01M10/052', 'C01P2002/76', 'C01G45/006', 'Y02E60/10'], 'matched_codes_sample': ['H04W', 'G07C', 'A61Q', 'C09K', 'G05B', 'G06T', 'A23V', 'G06Q', 'H03F', 'G06F', 'B41J', 'H04R', 'G02F', 'H01J', 'C01P', 'A61K', 'A61F', 'H05B', 'F25B', 'C07K', 'Y02E', 'F41C', 'F04B', 'Y02T', 'C07J', 'H04M', 'B08B', 'G10L', 'C01B', 'H01Q', 'H02G', 'A47J', 'B60Y', 'C08J', 'F01P', 'G06K', 'C12P', 'F02C', 'B29K', 'G01N', 'H01L', 'G01L', 'F01D', 'G01T', 'F02M', 'G08B', 'G21K', 'G02B', 'A61L', 'H04N', 'Y02B', 'C11D', 'H01R', 'C08G', 'A61B', 'H04B', 'B22F', 'A01K', 'C12N', 'F04D', 'H03H', 'H04L', 'B81C', 'B33Y', 'B81B', 'H02M', 'C07C', 'E21B', 'A61M', 'A63B', 'G01B', 'Y02P', 'H02K', 'B25B', 'B29L', 'F05D', 'C01G', 'G11C', 'B01D', 'H03K', 'A23L', 'C07D', 'H03M', 'A61P', 'F05B', 'B29C', 'H02S', 'G03G', 'H01H', 'G07F', 'B01J', 'G06N', 'H10N', 'H04J', 'H01M', 'B32B', 'H03G', 'G01J', 'B25J', 'G09G', 'H02J', 'B65H', 'F02K', 'F25J', 'H01S', 'G16H', 'Y02A', 'B25G', 'B64D', 'B25F', 'B60R', 'C09D', 'C08L', 'A61H', 'B60H', 'G06V', 'B60K', 'G01R', 'G01S', 'F16H', 'H10K', 'E04H', 'B62B', 'C12Q', 'Y02D', 'C07H', 'F16B'], 'total_valid_level5': 677, 'valid_level5_sample': ['G01D', 'B64F', 'F05C', 'F01B', 'G05B', 'G06Q', 'D02G', 'H04R', 'B60T', 'B62H']}, 'var_function-call-6204316298425977880': ['H01M', 'Y02E', 'C01G', 'C01P', 'G06V', 'G10L', 'G06Q', 'H02J', 'G16H', 'H03H', 'H02G', 'G08B', 'Y02B', 'F02K', 'Y02T', 'G06T', 'G01L', 'G06N', 'F41C', 'B33Y', 'B22F', 'F25J', 'G01S', 'B08B', 'E04B', 'B60P', 'A61G', 'G09F', 'B60D', 'B60L', 'G01H', 'G01K', 'B65G', 'G01D', 'B05B', 'C21D', 'B21C', 'B21B', 'G01P', 'B22D', 'C21C', 'H02B', 'B07B', 'A23P', 'C01D', 'B25D', 'C07B', 'G04F', 'E02D', 'E04G', 'B04B', 'E03B', 'A41H', 'B21H', 'F23N', 'E03F', 'A24F', 'C21B', 'E01C', 'F16M', 'A62C', 'B02C', 'G21F', 'B66F', 'B09B', 'E03D', 'G21G', 'C01F', 'H04S', 'G16B', 'C22B', 'F42C', 'Y04S', 'B03C', 'E01D', 'F04F', 'E21F', 'A44D', 'D06H', 'B63C', 'B27M', 'G06J', 'B27G', 'F16N', 'A63K', 'B27C', 'B63G', 'B09C', 'A23J', 'D03J', 'G16Y', 'F17B']}

exec(code, env_args)
