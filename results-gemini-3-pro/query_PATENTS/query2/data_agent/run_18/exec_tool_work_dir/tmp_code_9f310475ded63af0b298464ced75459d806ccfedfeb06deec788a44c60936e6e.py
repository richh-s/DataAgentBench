code = """import json
import re
from datetime import datetime

# Load full dataset
file_path = locals()['var_function-call-6127737537195675355']
with open(file_path, 'r') as f:
    records = json.load(f)

# Target CPCs from previous step
target_cpcs = ["E21", "E05", "F23", "G08", "A01", "F17", "A43", "B01", "B62", "F42", "G02", "F16", "C09", "F05", "Y02", "H03", "Y04", "B63", "B33", "B60", "F02", "A45", "H02", "B23", "F24", "A21", "Y10", "G05", "A23", "B82", "B22", "B02", "A47", "B30", "C08", "E02", "G06", "E01", "C07", "C25", "A61", "C04", "A24", "G07", "F04", "F21", "F01", "B66", "B41", "C23", "B29", "C12", "B27", "H01", "H05", "F41", "H04", "B42", "C22", "B64", "G01", "B81"]
target_set = set(target_cpcs)

# Dictionary to store counts: counts[cpc][year] = count
counts = {c: {} for c in target_cpcs}

def parse_year(date_str):
    if not date_str: return None
    s = date_str.replace(',', ' ').replace('.', ' ')
    s = re.sub(r'(\d+)(st|nd|rd|th)', lambda m: m.group(1), s)
    tokens = s.split()
    stop_words = {'on', 'dated', 'the', 'of', 'in'}
    clean_tokens = [t for t in tokens if t.lower() not in stop_words]
    s = ' '.join(clean_tokens)
    formats = ["%d %b %Y", "%Y %b %d", "%B %d %Y", "%d %B %Y", "%Y %B %d", "%b %d %Y", "%Y %m %d"]
    for fmt in formats:
        try:
            dt = datetime.strptime(s, fmt)
            return dt.year
        except:
            pass
    return None

for r in records:
    y = parse_year(r.get('filing_date', ''))
    if y is None:
        continue
    
    try:
        cpc_list = json.loads(r.get('cpc', '[]'))
        # We need to count each filing once per CPC code?
        # Usually yes. If a patent has multiple codes in same group, counts as 1 or multiple?
        # Usually distinct.
        seen_in_record = set()
        for item in cpc_list:
            code = item.get('code', '')
            if len(code) >= 3:
                c4 = code[:3]
                if c4 in target_set:
                    seen_in_record.add(c4)
        
        for c4 in seen_in_record:
            counts[c4][y] = counts[c4].get(y, 0) + 1
    except:
        pass

# Calculate EMA and find best year
alpha = 0.1
results = []

for cpc in target_cpcs:
    yr_counts = counts[cpc]
    if not yr_counts:
        continue
    
    years = sorted(yr_counts.keys())
    # Fill missing years? EMA usually runs on time series.
    # If there are gaps, should we assume 0? Yes.
    min_year = years[0]
    max_year = years[-1]
    
    ema = 0
    max_ema = -1
    best_year = None
    
    # Initialize with first year data?
    # Standard: EMA_0 = X_0.
    # But if we iterate from min to max filling zeros:
    
    # Let's do a strict time series from min_year to max_year
    first = True
    for y in range(min_year, max_year + 1):
        cnt = yr_counts.get(y, 0)
        if first:
            ema = cnt
            first = False
        else:
            ema = alpha * cnt + (1 - alpha) * ema
        
        if ema > max_ema:
            max_ema = ema
            best_year = y
            
    results.append({"cpc": cpc, "best_year": best_year, "max_ema": max_ema})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-4575975267135224610': 'file_storage/function-call-4575975267135224610.json', 'var_function-call-3559050311259836928': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-9512409107012440047': [{'symbol': 'A', 'level': '2.0'}, {'symbol': 'A01', 'level': '4.0'}, {'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01B1/00', 'level': '7.0'}, {'symbol': 'A01B1/22', 'level': '8.0'}, {'symbol': 'A01B1/16', 'level': '8.0'}, {'symbol': 'A01B1/20', 'level': '8.0'}, {'symbol': 'A01B1/06', 'level': '8.0'}, {'symbol': 'A01B1/02', 'level': '8.0'}, {'symbol': 'A01B1/24', 'level': '8.0'}], 'var_function-call-13552412906166802932': [{'count(*)': '277813'}], 'var_function-call-11062304279063144868': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th'}, {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019'}, {'Patents_info': 'In US, the patent application (no. US-201314655932-A) is held by SERINPET LTDA REPRESENTACIONES Y SERVICIOS DE PETROLEOS and has pub. number US-10465517-B2.', 'grant_date': 'on November 5th, 2019'}, {'Patents_info': 'Patent application (number US-201415314902-A) from US, held by HEWLETT PACKARD ENTPR DEV LP, with publication number US-10176043-B2.', 'grant_date': '8th Jan 2019'}, {'Patents_info': 'The US patent application (ID US-201615761951-A) is held by HEWLETT PACKARD DEVELOPMENT CO and has publication no. US-10436614-B2.', 'grant_date': 'dated 8th October 2019'}, {'Patents_info': 'The US application (number US-201715791853-A) is owned by DENSO INT AMERICA INC and has pub. number US-10348153-B2.', 'grant_date': 'July the 9th, 2019'}, {'Patents_info': 'In US, the patent filing (application number US-201616068918-A) is owned by DENSO CORP and has publication no. US-10369965-B2.', 'grant_date': 'August the 6th, 2019'}, {'Patents_info': 'Application (no. US-201815940839-A) from US, held by GE VIDEO COMPRESSION LLC, with publication number US-10248966-B2.', 'grant_date': 'Apr 2nd, 2019'}, {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019'}], 'var_function-call-16421393693204446287': [{'avg(length(cpc))': '903.0832322461512'}], 'var_function-call-6383820464758651535': 'file_storage/function-call-6383820464758651535.json', 'var_function-call-13717256898465498863': [], 'var_function-call-13525821902365425732': 'Done', 'var_function-call-6323908389233321967': ['Total records: 211', 'Raw: 14th Mar 2019 | Clean: \x01 Mar 2019 | Parsed: None', 'Raw: 2019 on Jul 12th | Clean: 2019 on Jul \x01 | Parsed: None', 'Raw: on October 31st, 2019 | Clean: on October \x01 2019 | Parsed: None', 'Raw: on November 5th, 2019 | Clean: on November \x01 2019 | Parsed: None', 'Raw: 8th Jan 2019 | Clean: \x01 Jan 2019 | Parsed: None', 'Raw: dated 8th October 2019 | Clean: dated \x01 October 2019 | Parsed: None', 'Raw: July the 9th, 2019 | Clean: July the \x01 2019 | Parsed: None', 'Raw: August the 6th, 2019 | Clean: August the \x01 2019 | Parsed: None', 'Raw: Apr 2nd, 2019 | Clean: Apr \x01 2019 | Parsed: None', 'Raw: dated 21st November 2019 | Clean: dated \x01 November 2019 | Parsed: None'], 'var_function-call-6494689462284093505': [], 'var_function-call-10513484846751932178': [], 'var_function-call-9968064909538923249': ['None', 'None', 'None', 'None', 'None'], 'var_function-call-4941573539046070950': ["Orig: 2019 on Jul 12th => Clean: '2019 on Jul 12'", "Orig: on October 31st, 2019 => Clean: 'on October 31 2019'", "Orig: dated 21st November 2019 => Clean: 'dated 21 November 2019'"], 'var_function-call-758753091584893277': [], 'var_function-call-634252136171018112': 'Done', 'var_function-call-13507337967032403441': ['Processing target record: In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'Date: dated 21st November 2019 -> Parsed: 2019-11-21 00:00:00', 'CPC count: 3', 'Code: B41F21/102', 'Code: B41F22/00', 'Code: B41F21/00'], 'var_function-call-17248440331804547639': ['E21', 'E05', 'F23', 'G08', 'A01', 'F17', 'A43', 'B01', 'B62', 'F42', 'G02', 'F16', 'C09', 'F05', 'Y02', 'H03', 'Y04', 'B63', 'B33', 'B60', 'F02', 'A45', 'H02', 'B23', 'F24', 'A21', 'Y10', 'G05', 'A23', 'B82', 'B22', 'B02', 'A47', 'B30', 'C08', 'E02', 'G06', 'E01', 'C07', 'C25', 'A61', 'C04', 'A24', 'G07', 'F04', 'F21', 'F01', 'B66', 'B41', 'C23', 'B29', 'C12', 'B27', 'H01', 'H05', 'F41', 'H04', 'B42', 'C22', 'B64', 'G01', 'B81'], 'var_function-call-6127737537195675355': 'file_storage/function-call-6127737537195675355.json'}

exec(code, env_args)
