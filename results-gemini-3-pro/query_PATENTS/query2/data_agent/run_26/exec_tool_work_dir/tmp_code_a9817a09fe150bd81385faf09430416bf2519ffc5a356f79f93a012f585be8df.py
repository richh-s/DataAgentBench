code = """import json
import pandas as pd
import re

# Load data again (or reuse logic)
with open(locals()['var_function-call-3206621542987617848'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Date Parsing Helpers
month_map = {
    'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
    'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
}

def parse_grant_date_check_h2_2019(date_str):
    if not isinstance(date_str, str): return False
    if '2019' not in date_str: return False
    match = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*', date_str, re.IGNORECASE)
    if match:
        m_str = match.group(1).lower()
        m_num = month_map.get(m_str, 0)
        return m_num >= 7
    return False

def parse_filing_year(date_str):
    if not isinstance(date_str, str): return None
    match = re.search(r'(\d{4})', date_str)
    if match:
        return int(match.group(1))
    return None

# Filter Grant Date
df['is_h2_2019'] = df['grant_date'].apply(parse_grant_date_check_h2_2019)
df_filtered = df[df['is_h2_2019']].copy()

# Parse Filing Year
df_filtered['filing_year'] = df_filtered['filing_date'].apply(parse_filing_year)
df_filtered = df_filtered.dropna(subset=['filing_year'])
df_filtered['filing_year'] = df_filtered['filing_year'].astype(int)

# Extract CPCs
def extract_level4_cpcs(cpc_json_str):
    try:
        cpc_list = json.loads(cpc_json_str)
        codes = set()
        for item in cpc_list:
            code = item.get('code', '')
            if len(code) >= 3:
                codes.add(code[:3])
        return list(codes)
    except:
        return []

df_filtered['cpc_codes'] = df_filtered['cpc'].apply(extract_level4_cpcs)
df_exploded = df_filtered.explode('cpc_codes')
df_exploded = df_exploded.dropna(subset=['cpc_codes'])

# Count filings per CPC per Year
counts = df_exploded.groupby(['cpc_codes', 'filing_year']).size().reset_index(name='count')

# Calculate EMA
min_year = counts['filing_year'].min()
max_year = counts['filing_year'].max()
all_years = range(min_year, max_year + 1)

ema_data = {} # {year: {cpc: ema_val}}
cpc_peaks = {} # {cpc: {year: peak_year, max_ema: val}}

# We need to process each CPC
all_cpcs = counts['cpc_codes'].unique()

cpc_ema_series = {}

for cpc in all_cpcs:
    group = counts[counts['cpc_codes'] == cpc]
    g = group.set_index('filing_year').reindex(all_years, fill_value=0)
    g['ema'] = g['count'].ewm(alpha=0.1, adjust=False).mean()
    
    # Store series
    cpc_ema_series[cpc] = g['ema']
    
    # Store peak
    best_idx = g['ema'].idxmax()
    max_ema = g.loc[best_idx, 'ema']
    cpc_peaks[cpc] = {'best_year': int(best_idx), 'max_ema': float(max_ema)}

# Identify Winners (Highest EMA each year)
winners = set()
for year in all_years:
    # Find CPC with max ema in this year
    max_val = -1
    best_cpc = None
    for cpc, series in cpc_ema_series.items():
        val = series.loc[year]
        if val > max_val:
            max_val = val
            best_cpc = cpc
    if best_cpc:
        winners.add(best_cpc)

# Prepare result
# titles from previous tool
titles_list = locals()['var_function-call-11345915269554895275']
# Convert list of dicts to dict map
title_map = {item['symbol']: item['titleFull'] for item in titles_list}

final_output = []
for cpc in winners:
    info = cpc_peaks[cpc]
    final_output.append({
        "Full title": title_map.get(cpc, "Unknown"),
        "CPC group code": cpc,
        "Best year": info['best_year']
    })

print("__RESULT__:")
print(json.dumps(final_output))"""

env_args = {'var_function-call-4649531244037871347': 'file_storage/function-call-4649531244037871347.json', 'var_function-call-4649531244037872868': [{'symbol': 'A01K2227/108', 'level': '9.0', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'level': '9.0', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'level': '9.0', 'titleFull': 'Bovine'}], 'var_function-call-485676876898493978': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-485676876898493815': [{'Patents_info': 'In AT, the patent filing (application no. AT-52022-U) is assigned to ST Extruded Products Germany GmbH and has publication no. AT-17758-U1.'}, {'Patents_info': 'Application (no. AU-2006246481-A) from AU, belonging to KAO GERMANY GMBH, with pub. number AU-2006246481-B2.'}, {'Patents_info': 'TRELLEBORG AUTOMOTIVE GERMANY holds the PL patent application (number PL-07728345-T), with publication no. PL-2010798-T3.'}, {'Patents_info': 'The DE application (number DE-102008034343-A) is assigned to CONTINENTAL MECH COMPONENTS GERMANY GMBH and has pub. number DE-102008034343-B4.'}, {'Patents_info': 'In EP, the application (ID EP-18829350-A) is belonging to MEYER BURGER GERMANY GMBH and has pub. number EP-3729486-C0.'}], 'var_function-call-1173670379374644714': [{'symbol': 'A', 'level': '2.0', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'A01', 'level': '4.0', 'titleFull': 'AGRICULTURE; FORESTRY; ANIMAL HUSBANDRY; HUNTING; TRAPPING; FISHING'}, {'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'A01B1/00', 'level': '7.0', 'titleFull': 'Hand tools'}], 'var_function-call-1173670379374644669': [], 'var_function-call-12085292487298471941': [{'count(*)': '4833'}], 'var_function-call-12085292487298470532': [{'count(*)': '68'}], 'var_function-call-12085292487298473219': [{'count(*)': '5'}], 'var_function-call-3206621542987617848': 'file_storage/function-call-3206621542987617848.json', 'var_function-call-11073480054091126375': ['A21', 'A43', 'A47', 'A61', 'B23', 'B29', 'B41', 'B60', 'B62', 'B63', 'B64', 'B66', 'C04', 'C09', 'E02', 'E05', 'F01', 'F02', 'F04', 'F05', 'F16', 'F23', 'F24', 'F41', 'F42', 'G01', 'G02', 'G07', 'G08', 'H01', 'H02', 'H03', 'H04', 'Y02', 'Y10'], 'var_function-call-11345915269554895275': [{'symbol': 'B29', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'A61', 'titleFull': 'MEDICAL OR VETERINARY SCIENCE; HYGIENE'}, {'symbol': 'A43', 'titleFull': 'FOOTWEAR'}, {'symbol': 'A47', 'titleFull': 'FURNITURE; DOMESTIC ARTICLES OR APPLIANCES; COFFEE MILLS; SPICE MILLS; SUCTION CLEANERS IN GENERAL'}, {'symbol': 'A21', 'titleFull': 'BAKING; EDIBLE DOUGHS'}, {'symbol': 'B66', 'titleFull': 'HOISTING; LIFTING; HAULING'}, {'symbol': 'B62', 'titleFull': 'LAND VEHICLES FOR TRAVELLING OTHERWISE THAN ON RAILS'}, {'symbol': 'B64', 'titleFull': 'AIRCRAFT; AVIATION; COSMONAUTICS'}, {'symbol': 'B63', 'titleFull': 'SHIPS OR OTHER WATERBORNE VESSELS; RELATED EQUIPMENT'}, {'symbol': 'B60', 'titleFull': 'VEHICLES IN GENERAL'}, {'symbol': 'B41', 'titleFull': 'PRINTING; LINING MACHINES; TYPEWRITERS; STAMPS'}, {'symbol': 'C04', 'titleFull': 'CEMENTS; CONCRETE; ARTIFICIAL STONE; CERAMICS; REFRACTORIES'}, {'symbol': 'C09', 'titleFull': 'DYES; PAINTS; POLISHES; NATURAL RESINS; ADHESIVES; COMPOSITIONS NOT OTHERWISE PROVIDED FOR; APPLICATIONS OF MATERIALS NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'E05', 'titleFull': 'LOCKS; KEYS; WINDOW OR DOOR FITTINGS; SAFES'}, {'symbol': 'E02', 'titleFull': 'HYDRAULIC ENGINEERING; FOUNDATIONS; SOIL SHIFTING'}, {'symbol': 'F41', 'titleFull': 'WEAPONS'}, {'symbol': 'F01', 'titleFull': 'MACHINES OR ENGINES IN GENERAL; ENGINE PLANTS IN GENERAL; STEAM ENGINES'}, {'symbol': 'F04', 'titleFull': 'POSITIVE - DISPLACEMENT MACHINES FOR LIQUIDS; PUMPS FOR LIQUIDS OR ELASTIC FLUIDS'}, {'symbol': 'F16', 'titleFull': 'ENGINEERING ELEMENTS AND UNITS; GENERAL MEASURES FOR PRODUCING AND MAINTAINING EFFECTIVE FUNCTIONING OF MACHINES OR INSTALLATIONS; THERMAL INSULATION IN GENERAL'}, {'symbol': 'F05', 'titleFull': 'INDEXING SCHEMES RELATING TO ENGINES OR PUMPS IN VARIOUS SUBCLASSES OF CLASSES F01-F04'}, {'symbol': 'F42', 'titleFull': 'AMMUNITION; BLASTING'}, {'symbol': 'F02', 'titleFull': 'COMBUSTION ENGINES; HOT-GAS OR COMBUSTION-PRODUCT ENGINE PLANTS'}, {'symbol': 'F23', 'titleFull': 'COMBUSTION APPARATUS; COMBUSTION PROCESSES'}, {'symbol': 'F24', 'titleFull': 'HEATING; RANGES; VENTILATING'}, {'symbol': 'G08', 'titleFull': 'SIGNALLING'}, {'symbol': 'G02', 'titleFull': 'OPTICS'}, {'symbol': 'G01', 'titleFull': 'MEASURING; TESTING'}, {'symbol': 'G07', 'titleFull': 'CHECKING-DEVICES'}, {'symbol': 'H03', 'titleFull': 'ELECTRONIC CIRCUITRY'}, {'symbol': 'H04', 'titleFull': 'ELECTRIC COMMUNICATION TECHNIQUE'}, {'symbol': 'H01', 'titleFull': 'ELECTRIC ELEMENTS'}, {'symbol': 'H02', 'titleFull': 'GENERATION; CONVERSION OR DISTRIBUTION OF ELECTRIC POWER'}, {'symbol': 'Y02', 'titleFull': 'TECHNOLOGIES OR APPLICATIONS FOR MITIGATION OR ADAPTATION AGAINST CLIMATE CHANGE'}, {'symbol': 'Y10', 'titleFull': 'TECHNICAL SUBJECTS COVERED BY FORMER USPC'}]}

exec(code, env_args)
