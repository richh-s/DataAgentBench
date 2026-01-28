code = """import json
# load previous query results
with open(var_call_nqJ5iVHTY5TMjwpaf0Lfi4eQ, 'r') as f:
    top5 = json.load(f)
with open(var_call_kX7MBuLuYb2R2bG9UCJpvXe0, 'r') as f:
    descriptions = json.load(f)
# top5 symbols order corresponds to top5 list
symbols = [rec['Symbol'] for rec in top5]
# map symbols to company descriptions from descriptions list (in same order as query)
symbol_to_desc = {symbols[i]: descriptions[i]['Company Description'] for i in range(len(symbols))}
# prepare final list of company names (extract name before first comma or ' Inc.' etc - but we can return full description? User asked 'company names please' so extract first token up to first occurrence of ',' or ' Inc.' or ' Corporation' or ' Company' or ' Ltd' etc
import re
def extract_name(desc):
    # try common separators
    m = re.split(',| Inc\.|, Inc\.| Corporation| Co\.| Company| Ltd\.| LLC|,', desc)
    name = m[0]
    return name.strip()
company_names = [extract_name(symbol_to_desc[s]) for s in symbols]
# build output mapping symbol->company name
out = [{'Symbol': symbols[i], 'Company Name': company_names[i], 'Days Above 20%': int(top5[i]['cnt'])} for i in range(len(symbols))]
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Nnffy5WqwlKBUYMC5Opf1NhG': 'file_storage/call_Nnffy5WqwlKBUYMC5Opf1NhG.json', 'var_call_CS7wPfP4rUVF9gBDQtifhV7n': 'file_storage/call_CS7wPfP4rUVF9gBDQtifhV7n.json', 'var_call_C4KRajZFiVKMpbaSReYCbJiE': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_nqJ5iVHTY5TMjwpaf0Lfi4eQ': [{'Symbol': 'SES', 'cnt': '51'}, {'Symbol': 'GLG', 'cnt': '42'}, {'Symbol': 'TMSR', 'cnt': '40'}, {'Symbol': 'VERB', 'cnt': '38'}, {'Symbol': 'SNSS', 'cnt': '32'}], 'var_call_kX7MBuLuYb2R2bG9UCJpvXe0': [{'Company Description': 'TD Holdings, Inc. is involved in commodity trading and supply chain management, specializing in the distribution of non-ferrous metals and other industrial materials.'}, {'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.'}, {'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.'}, {'Company Description': 'TMSR Holding Company Limited engages in the development and distribution of advanced industrial materials, focusing on enhancing efficiency and sustainability in various manufacturing processes.'}, {'Company Description': 'Verb Technology Company, Inc. specializes in developing interactive video-based sales and marketing applications designed to enhance customer engagement and drive business growth.'}]}

exec(code, env_args)
