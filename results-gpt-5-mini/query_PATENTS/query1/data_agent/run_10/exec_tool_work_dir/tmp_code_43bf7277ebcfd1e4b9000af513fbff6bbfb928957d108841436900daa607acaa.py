code = """import json, re
from collections import defaultdict

# Use the symbols found in 2022 (stored as a Python list in storage)
symbols_2022 = var_call_saaGx1xwSsEL6pG7KHrgrdXA

# Load level-5 symbols
with open(var_call_YE2zqtqcVqTWgh47MXYr8BqH, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)
level5_all = set(rec.get('symbol') for rec in cpc_defs if rec.get('symbol'))

# Filter interest to true level-5 symbols present in 2022
interest = [s for s in symbols_2022 if s in level5_all]
interest_set = set(interest)

# Map by first 4 characters (common CPC group length)
prefix_map = {}
for s in interest:
    pref = s[:4]
    prefix_map.setdefault(pref, []).append(s)

# Year files mapping
year_files = {
    2015: var_call_TX7dPjy9i4Lbx9xDR5cnNNxn,
    2016: var_call_kyFyQT16lqANKzws3pouKIdA,
    2017: var_call_UG281eiESlJTKizU318F3Fy6,
    2018: var_call_RUYNAsfs51QDJAiNgrjXVEB2,
    2019: var_call_FWJhC0kDziIpNNx6nquMDPVe,
    2020: var_call_J7ihqL93BJ4cVetWLPQgyyxr,
    2021: var_call_GrbLq6SkqczaOnkIYaf4XiAC,
    2022: var_call_HKhiFOFs3nWlSQqAZCYYOhPt,
}

code_regex = re.compile(r'[A-Z]\d{2}[A-Z]\d*(?:/\d+)?')

# Initialize counts only for interest symbols
counts = {s: defaultdict(int) for s in interest}

# Helper to parse cpc field quickly

def extract_codes(cpc_field):
    if not cpc_field or not isinstance(cpc_field, str):
        return []
    try:
        lst = json.loads(cpc_field)
        return [d.get('code') for d in lst if isinstance(d, dict) and d.get('code')]
    except Exception:
        return code_regex.findall(cpc_field)

# Matching: use first 4 chars

def match_code_to_interest(code):
    if not code:
        return None
    code_no_slash = code.split('/')[0]
    pref4 = code_no_slash[:4]
    candidates = prefix_map.get(pref4)
    if not candidates:
        return None
    # If multiple, choose the one that is exact match or first
    for c in candidates:
        if code.startswith(c) or code_no_slash.startswith(c):
            return c
    return candidates[0]

# Process each year file
for year, path in year_files.items():
    # path is a filename
    try:
        with open(path, 'r', encoding='utf-8') as f:
            recs = json.load(f)
    except Exception:
        recs = []
    for rec in recs:
        codes = extract_codes(rec.get('cpc'))
        for code in codes:
            sym = match_code_to_interest(code)
            if sym:
                counts[sym][year] += 1

# Compute EMA alpha=0.2 over years 2015..2022
alpha = 0.2
years = [2015,2016,2017,2018,2019,2020,2021,2022]
result = []
for sym, yc in counts.items():
    ema = None
    ema_by_year = {}
    for y in years:
        c = yc.get(y, 0)
        if ema is None:
            ema = c
        else:
            ema = alpha * c + (1 - alpha) * ema
        ema_by_year[y] = ema
    max_ema = max(ema_by_year.values())
    best_years = [y for y,v in ema_by_year.items() if abs(v-max_ema) < 1e-9]
    if 2022 in best_years:
        result.append(sym)

result = sorted(list(set(result)))
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_KOAe9jSTh9Mbmi1RCVQS58Hp': ['publicationinfo'], 'var_call_tAgqIyi2aU92W9WzynRcveR3': ['cpc_definition'], 'var_call_YE2zqtqcVqTWgh47MXYr8BqH': 'file_storage/call_YE2zqtqcVqTWgh47MXYr8BqH.json', 'var_call_Mnu7ZA99v6zlg0eU5qFuAnGn': 'file_storage/call_Mnu7ZA99v6zlg0eU5qFuAnGn.json', 'var_call_HKhiFOFs3nWlSQqAZCYYOhPt': 'file_storage/call_HKhiFOFs3nWlSQqAZCYYOhPt.json', 'var_call_saaGx1xwSsEL6pG7KHrgrdXA': ['A01B', 'A01C', 'A01D', 'A01F', 'A01G', 'A01H', 'A01K', 'A01M', 'A01N', 'A01P', 'A21B', 'A21C', 'A21D', 'A22B', 'A22C', 'A23B', 'A23C', 'A23D', 'A23F', 'A23G', 'A23J', 'A23K', 'A23L', 'A23N', 'A23P', 'A23V', 'A24B', 'A24C', 'A24D', 'A24F', 'A41B', 'A41D', 'A41G', 'A41H', 'A42B', 'A42C', 'A43B', 'A43C', 'A43D', 'A44B', 'A44C', 'A44D', 'A45B', 'A45C', 'A45D', 'A45F', 'A46B', 'A47B', 'A47C', 'A47D', 'A47F', 'A47G', 'A47H', 'A47J', 'A47K', 'A47L', 'A61B', 'A61C', 'A61D', 'A61F', 'A61G', 'A61H', 'A61J', 'A61K', 'A61L', 'A61M', 'A61N', 'A61P', 'A61Q', 'A62B', 'A62C', 'A62D', 'A63B', 'A63C', 'A63D', 'A63F', 'A63G', 'A63H', 'A63J', 'A63K', 'B01D', 'B01F', 'B01J', 'B01L', 'B02B', 'B02C', 'B03B', 'B03C', 'B03D', 'B04B', 'B04C', 'B05B', 'B05C', 'B05D', 'B06B', 'B07B', 'B07C', 'B08B', 'B09B', 'B09C', 'B21B', 'B21C', 'B21D', 'B21F', 'B21H', 'B21J', 'B21K', 'B21L', 'B22C', 'B22D', 'B22F', 'B23B', 'B23C', 'B23D', 'B23G', 'B23H', 'B23K', 'B23P', 'B23Q', 'B24B', 'B24C', 'B24D', 'B25B', 'B25C', 'B25D', 'B25F', 'B25G', 'B25H', 'B25J', 'B26B', 'B26D', 'B26F', 'B27B', 'B27C', 'B27D', 'B27F', 'B27G', 'B27H', 'B27J', 'B27K', 'B27M', 'B27N', 'B28B', 'B28C', 'B28D', 'B29B', 'B29C', 'B29D', 'B29K', 'B29L', 'B30B', 'B31B', 'B31F', 'B32B', 'B33Y', 'B41F', 'B41J', 'B41K', 'B41M', 'B41P', 'B42B', 'B42C', 'B42D', 'B42F', 'B43K', 'B43L', 'B43M', 'B44B', 'B44C', 'B44D', 'B60B', 'B60C', 'B60D', 'B60F', 'B60G', 'B60H', 'B60J', 'B60K', 'B60L', 'B60M', 'B60N', 'B60P', 'B60Q', 'B60R', 'B60S', 'B60T', 'B60W', 'B60Y', 'B61B', 'B61C', 'B61D', 'B61F', 'B61G', 'B61H', 'B61K', 'B61L', 'B62B', 'B62D', 'B62H', 'B62J', 'B62K', 'B62L', 'B62M', 'B63B', 'B63C', 'B63G', 'B63H', 'B63J', 'B64B', 'B64C', 'B64D', 'B64F', 'B64G', 'B64U', 'B65B', 'B65C', 'B65D', 'B65F', 'B65G', 'B65H', 'B66B', 'B66C', 'B66D', 'B66F', 'B67B', 'B67C', 'B67D', 'B81B', 'B81C', 'B82B', 'B82Y', 'C01B', 'C01C', 'C01D', 'C01F', 'C01G', 'C01P', 'C02F', 'C03B', 'C03C', 'C04B', 'C05B', 'C05D', 'C05F', 'C05G', 'C06B', 'C06C', 'C07B', 'C07C', 'C07D', 'C07F', 'C07G', 'C07H', 'C07J', 'C07K', 'C08B', 'C08C', 'C08F', 'C08G', 'C08H', 'C08J', 'C08K', 'C08L', 'C09B', 'C09C', 'C09D', 'C09J', 'C09K', 'C10B', 'C10C', 'C10G', 'C10L', 'C10M', 'C10N', 'C11B', 'C11C', 'C11D', 'C12C', 'C12F', 'C12G', 'C12H', 'C12M', 'C12N', 'C12P', 'C12Q', 'C12R', 'C12Y', 'C13B', 'C13K', 'C14B', 'C14C', 'C21B', 'C21C', 'C21D', 'C22B', 'C22C', 'C22F', 'C23C', 'C23D', 'C23F', 'C23G', 'C25B', 'C25C', 'C25D', 'C30B', 'C40B', 'D01D', 'D01F', 'D01G', 'D02G', 'D02H', 'D02J', 'D03D', 'D03J', 'D04B', 'D04C', 'D04H', 'D05B', 'D06B', 'D06C', 'D06F', 'D06H', 'D06L', 'D06M', 'D06N', 'D06P', 'D07B', 'D10B', 'D21B', 'D21C', 'D21D', 'D21F', 'D21G', 'D21H', 'D21J', 'E01B', 'E01C', 'E01D', 'E01F', 'E01H', 'E02B', 'E02C', 'E02D', 'E02F', 'E03B', 'E03C', 'E03D', 'E03F', 'E04B', 'E04C', 'E04D', 'E04F', 'E04G', 'E04H', 'E05B', 'E05C', 'E05D', 'E05F', 'E05G', 'E05Y', 'E06B', 'E06C', 'E21B', 'E21C', 'E21D', 'E21F', 'F01B', 'F01C', 'F01D', 'F01K', 'F01L', 'F01M', 'F01N', 'F01P', 'F02B', 'F02C', 'F02D', 'F02F', 'F02G', 'F02K', 'F02M', 'F02N', 'F02P', 'F03B', 'F03C', 'F03D', 'F03G', 'F04B', 'F04C', 'F04D', 'F04F', 'F05B', 'F05C', 'F05D', 'F15B', 'F16B', 'F16C', 'F16D', 'F16F', 'F16G', 'F16H', 'F16J', 'F16K', 'F16L', 'F16M', 'F16N', 'F17B', 'F17C', 'F17D', 'F21K', 'F21S', 'F21V', 'F21W', 'F21Y', 'F22B', 'F22D', 'F23C', 'F23D', 'F23G', 'F23J', 'F23K', 'F23L', 'F23N', 'F23Q', 'F23R', 'F24B', 'F24C', 'F24D', 'F24F', 'F24H', 'F24S', 'F24T', 'F24V', 'F25B', 'F25C', 'F25D', 'F25J', 'F26B', 'F27B', 'F27D', 'F28B', 'F28C', 'F28D', 'F28F', 'F41A', 'F41B', 'F41C', 'F41F', 'F41H', 'F41J', 'F42B', 'F42C', 'F42D', 'G01B', 'G01C', 'G01D', 'G01F', 'G01G', 'G01H', 'G01J', 'G01K', 'G01L', 'G01M', 'G01N', 'G01P', 'G01Q', 'G01R', 'G01S', 'G01T', 'G01V', 'G01W', 'G02B', 'G02C', 'G02F', 'G03B', 'G03F', 'G03G', 'G03H', 'G04B', 'G04C', 'G04F', 'G04G', 'G04R', 'G05B', 'G05D', 'G05F', 'G05G', 'G06F', 'G06J', 'G06K', 'G06M', 'G06N', 'G06Q', 'G06T', 'G06V', 'G07B', 'G07C', 'G07D', 'G07F', 'G07G', 'G08B', 'G08C', 'G08G', 'G09B', 'G09C', 'G09F', 'G09G', 'G10D', 'G10G', 'G10H', 'G10K', 'G10L', 'G11B', 'G11C', 'G16B', 'G16C', 'G16H', 'G16Y', 'G21B', 'G21C', 'G21D', 'G21F', 'G21G', 'G21K', 'H01B', 'H01C', 'H01F', 'H01G', 'H01H', 'H01J', 'H01L', 'H01M', 'H01P', 'H01Q', 'H01R', 'H01S', 'H01T', 'H02B', 'H02G', 'H02H', 'H02J', 'H02K', 'H02M', 'H02N', 'H02P', 'H02S', 'H03B', 'H03D', 'H03F', 'H03G', 'H03H', 'H03K', 'H03L', 'H03M', 'H04B', 'H04H', 'H04J', 'H04K', 'H04L', 'H04M', 'H04N', 'H04Q', 'H04R', 'H04S', 'H04W', 'H05B', 'H05F', 'H05G', 'H05H', 'H05K', 'H10B', 'H10K', 'H10N', 'Y02A', 'Y02B', 'Y02C', 'Y02D', 'Y02E', 'Y02P', 'Y02T', 'Y02W', 'Y04S', 'Y10S', 'Y10T'], 'var_call_GrbLq6SkqczaOnkIYaf4XiAC': 'file_storage/call_GrbLq6SkqczaOnkIYaf4XiAC.json', 'var_call_TX7dPjy9i4Lbx9xDR5cnNNxn': 'file_storage/call_TX7dPjy9i4Lbx9xDR5cnNNxn.json', 'var_call_kyFyQT16lqANKzws3pouKIdA': 'file_storage/call_kyFyQT16lqANKzws3pouKIdA.json', 'var_call_UG281eiESlJTKizU318F3Fy6': 'file_storage/call_UG281eiESlJTKizU318F3Fy6.json', 'var_call_RUYNAsfs51QDJAiNgrjXVEB2': 'file_storage/call_RUYNAsfs51QDJAiNgrjXVEB2.json', 'var_call_FWJhC0kDziIpNNx6nquMDPVe': 'file_storage/call_FWJhC0kDziIpNNx6nquMDPVe.json', 'var_call_J7ihqL93BJ4cVetWLPQgyyxr': 'file_storage/call_J7ihqL93BJ4cVetWLPQgyyxr.json'}

exec(code, env_args)
