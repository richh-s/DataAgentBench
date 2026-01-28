code = """import json, re
# use stored variables directly
top5 = var_call_nqJ5iVHTY5TMjwpaf0Lfi4eQ
descs = var_call_8wRr69Q1lDsIax8Cmxi8FcEV
sym2desc = {rec['Symbol']: rec['Company Description'] for rec in descs}

def extract_name(desc):
    parts = re.split(',| Inc\.| Corporation| Co\.| Company| Ltd\.| LLC| Limited', desc)
    return parts[0].strip()

out = []
for rec in top5:
    s = rec['Symbol']
    cnt = int(rec['cnt'])
    desc = sym2desc.get(s, '')
    name = extract_name(desc) if desc else s
    out.append({'Symbol': s, 'Company Name': name, 'Days Above 20%': cnt})

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Nnffy5WqwlKBUYMC5Opf1NhG': 'file_storage/call_Nnffy5WqwlKBUYMC5Opf1NhG.json', 'var_call_CS7wPfP4rUVF9gBDQtifhV7n': 'file_storage/call_CS7wPfP4rUVF9gBDQtifhV7n.json', 'var_call_C4KRajZFiVKMpbaSReYCbJiE': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_nqJ5iVHTY5TMjwpaf0Lfi4eQ': [{'Symbol': 'SES', 'cnt': '51'}, {'Symbol': 'GLG', 'cnt': '42'}, {'Symbol': 'TMSR', 'cnt': '40'}, {'Symbol': 'VERB', 'cnt': '38'}, {'Symbol': 'SNSS', 'cnt': '32'}], 'var_call_kX7MBuLuYb2R2bG9UCJpvXe0': [{'Company Description': 'TD Holdings, Inc. is involved in commodity trading and supply chain management, specializing in the distribution of non-ferrous metals and other industrial materials.'}, {'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.'}, {'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.'}, {'Company Description': 'TMSR Holding Company Limited engages in the development and distribution of advanced industrial materials, focusing on enhancing efficiency and sustainability in various manufacturing processes.'}, {'Company Description': 'Verb Technology Company, Inc. specializes in developing interactive video-based sales and marketing applications designed to enhance customer engagement and drive business growth.'}], 'var_call_8wRr69Q1lDsIax8Cmxi8FcEV': [{'Symbol': 'GLG', 'Company Description': 'TD Holdings, Inc. is involved in commodity trading and supply chain management, specializing in the distribution of non-ferrous metals and other industrial materials.'}, {'Symbol': 'SES', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.'}, {'Symbol': 'TMSR', 'Company Description': 'TMSR Holding Company Limited engages in the development and distribution of advanced industrial materials, focusing on enhancing efficiency and sustainability in various manufacturing processes.'}, {'Symbol': 'VERB', 'Company Description': 'Verb Technology Company, Inc. specializes in developing interactive video-based sales and marketing applications designed to enhance customer engagement and drive business growth.'}]}

exec(code, env_args)
