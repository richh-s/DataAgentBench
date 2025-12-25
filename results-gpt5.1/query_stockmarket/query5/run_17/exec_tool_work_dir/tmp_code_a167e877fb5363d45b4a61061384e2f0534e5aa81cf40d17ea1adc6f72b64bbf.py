code = """import json, pandas as pd
from pathlib import Path

symbols_info = pd.read_json(Path(var_call_FUfQ4JCVFBKmuGoimQaDHVNz))
trade_tables = pd.read_json(Path(var_call_TgARrzPML3y7pBMFl9SL0jhh))

nasdaq_cap_syms = set(symbols_info['Symbol'].astype(str))
trade_syms = set(trade_tables.iloc[:,0].astype(str))
common_syms = sorted(nasdaq_cap_syms & trade_syms)

result = json.dumps(common_syms)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_TgARrzPML3y7pBMFl9SL0jhh': 'file_storage/call_TgARrzPML3y7pBMFl9SL0jhh.json', 'var_call_FUfQ4JCVFBKmuGoimQaDHVNz': 'file_storage/call_FUfQ4JCVFBKmuGoimQaDHVNz.json', 'var_call_xXWiho8DXjAm5Wh84UwL6sQ6': [], 'var_call_PW0ORgaaIeWkt9da3ZB2Noaz': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP'], 'var_call_CpsO3zO3ypusNmIBzjm5A7fv': ['AAAU', 'AADR', 'AAME', 'AAWW', 'AAXJ', 'ABEQ', 'ABMD', 'ACAD', 'ACES', 'ACIO', 'ACLS', 'ACSG', 'ACSI', 'ACT', 'ACWF', 'ACWI', 'ACWV', 'ACWX', 'ACY', 'ADAP', 'ADES', 'ADI', 'ADMA', 'ADME', 'ADP', 'ADRE', 'ADXS', 'AEFC', 'AESR', 'AFIF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGMH', 'AGND', 'AGQ', 'AGT', 'AGZ', 'AGZD', 'AIA', 'AIEQ', 'AIIQ', 'AIN', 'AIQ', 'AIRR', 'AIV', 'AIZP', 'AJRD', 'AKRO', 'AL', 'ALACU', 'ALFA', 'ALGT', 'ALLT', 'ALO', 'ALT', 'ALTS', 'ALTY', 'AMCA', 'AMHC', 'AMLP', 'AMN', 'AMOM', 'AMP', 'AMRN', 'AMT', 'AMTX', 'AMZA', 'ANDA', 'ANGL', 'AOA', 'AOK', 'AOM', 'AOR', 'APEX', 'APTX', 'ARCM', 'ARD', 'ARGD', 'ARGT', 'ARKF', 'ARKG', 'ARKK', 'ARKQ', 'ARKW', 'ARLO', 'ARMR', 'ARNA', 'ASEA', 'ASET', 'ASG', 'ASHR', 'ASHS', 'ASHX', 'ASYS', 'AUMN', 'AUSF', 'AUTL', 'AVA', 'AVDE', 'AVDV', 'AVEM', 'AVNW', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BANC', 'BANFP', 'BAPR', 'BATRA', 'BATT', 'BAUG', 'BBAX', 'BBC', 'BBCA', 'BBEU', 'BBH', 'BBIN', 'BBJP', 'BBP', 'BBRE', 'BBSA', 'BBU', 'BBUS', 'BBVA', 'BCD', 'BCI', 'BCLI', 'BDCY', 'BDEC', 'BDRY', 'BDXA', 'BFEB', 'BFIT', 'BFOR', 'BGRN', 'BHAT', 'BIB', 'BIBL', 'BICK', 'BIL', 'BIOC', 'BIS', 'BIV', 'BIZD', 'BJAN', 'BJK', 'BJUL', 'BJUN', 'BKF', 'BKH', 'BKLN', 'BKT', 'BKYI', 'BLCN', 'BLD', 'BLES', 'BLFS', 'BLHY', 'BLOK', 'BLV', 'BMAR', 'BND', 'BNDC', 'BNDW', 'BNDX', 'BNO', 'BNOV', 'BNS', 'BOCT', 'BOIL', 'BOKFL', 'BOND', 'BOSC', 'BOSS', 'BOTJ', 'BOTZ', 'BOUT', 'BPOPM', 'BPOPN', 'BRF', 'BRKL', 'BRZU', 'BSAE', 'BSBE', 'BSCE', 'BSCK', 'BSCL', 'BSCM', 'BSCN', 'BSCO', 'BSCP']}

exec(code, env_args)
