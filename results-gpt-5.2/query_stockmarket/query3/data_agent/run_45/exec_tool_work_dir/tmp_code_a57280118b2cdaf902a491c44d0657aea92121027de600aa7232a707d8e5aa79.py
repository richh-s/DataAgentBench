code = """import json, math, pandas as pd

stocks = pd.DataFrame(var_call_bt9fyrftJUfXwB7bTTQkTNB5)

avg_map = {
 'AGMH': var_call_2pmdbQlL5YOiWSxrQi4lL3V1[0]['avg_vol'],
 'AMTX': var_call_2F1m4hgDmRvC1rmyiEwzONis[0]['avg_vol'],
 'APEX': var_call_1uMUJmB38e4PMVvuMo7Ba40g[0]['avg_vol'],
 'BIOC': var_call_suNL0ZLgB5Uz28mf09Bf73HL[0]['avg_vol'],
 'BKYI': var_call_SzkQ2XllWzyfcrDSj53EQFHr[0]['avg_vol'],
 'CBAT': var_call_c6lVCsEoUmFCndzFdphLccMs[0]['avg_vol'],
 'CCCL': var_call_DlgsUWzhHeEoVwFOt96TKBmW[0]['avg_vol'],
 'CORV': var_call_GndktVeTHc9k6qrlctlfohQ1[0]['avg_vol'],
 'CPAH': var_call_BjVgUlJonTjSaDK8lr5VE8AN[0]['avg_vol'],
 'DZSI': var_call_qgWqIh73ELHTBK56s2EsTAEw[0]['avg_vol'],
 'FAMI': var_call_5Cn2OsRsYzmKe742cdGlgKqi[0]['avg_vol'],
 'FTFT': var_call_ZiBOKDOlC1R2023nNJkB8fso[0]['avg_vol'],
 'FTR': var_call_QtqmJtXSfGb4lUJEPaBi1cTs[0]['avg_vol'],
 'IDEX': var_call_64fASn1Yl2GSGfgXwwhuG35E[0]['avg_vol'],
 'MCEP': var_call_Z49iGJCkF4Sz8WCot84IGkQA[0]['avg_vol'],
 'NXTD': var_call_FLKAHKwrEQ4kHD7bG3kV1zyO[0]['avg_vol'],
 'OPTT': var_call_eXSraKNs7uuvj4qdFLcbwVYJ[0]['avg_vol'],
 'PEIX': var_call_GOub14IuJHMwuEjnAhDtNKTz[0]['avg_vol'],
 'RBZ': var_call_RfOLWSbEfhjDfunZLkdFUC2X[0]['avg_vol'],
 'SES': var_call_FVH7G8sPuUZvvBfIMSdVkuIq[0]['avg_vol'],
 'SNSS': var_call_ZyQfdimaX1ObXgLc46dhT1B4[0]['avg_vol'],
 'SPI': var_call_rtpKfpehf8176yBarwwkpwhj[0]['avg_vol'],
 'SYPR': var_call_gByyyLVd28DBmjCzZWInrrD3[0]['avg_vol'],
}

rows=[]
for sym,val in avg_map.items():
    if val is None:
        continue
    if isinstance(val,str) and val.lower()=='nan':
        continue
    try:
        f=float(val)
    except:
        continue
    if math.isnan(f):
        continue
    rows.append({'Symbol': sym, 'avg_daily_volume_2008': f})

vols=pd.DataFrame(rows)
out=stocks.merge(vols,on='Symbol',how='inner')
out=out[['company_name','Symbol','financial_status','avg_daily_volume_2008']].sort_values(['company_name','Symbol'])

lines=[]
for _,r in out.iterrows():
    lines.append(f"{r['company_name']} ({r['Symbol']}), Financial Status={r['financial_status']}, Avg daily volume 2008={r['avg_daily_volume_2008']:.2f}")
answer="\n".join(lines) if lines else 'No matching companies found with non-null 2008 average daily volume.'

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_sBuomdXRZ4mjg5mOO3LkWL3u': ['stockinfo'], 'var_call_bt9fyrftJUfXwB7bTTQkTNB5': [{'Symbol': 'AGMH', 'company_name': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'financial_status': 'D', 'market_category': 'S', 'listing_exchange': 'Q'}, {'Symbol': 'AMTX', 'company_name': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'financial_status': 'D', 'market_category': 'G', 'listing_exchange': 'Q'}, {'Symbol': 'APEX', 'company_name': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'financial_status': 'D', 'market_category': 'S', 'listing_exchange': 'Q'}, {'Symbol': 'BIOC', 'company_name': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'financial_status': 'D', 'market_category': 'S', 'listing_exchange': 'Q'}, {'Symbol': 'BKYI', 'company_name': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'financial_status': 'D', 'market_category': 'S', 'listing_exchange': 'Q'}, {'Symbol': 'CBAT', 'company_name': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'financial_status': 'D', 'market_category': 'S', 'listing_exchange': 'Q'}, {'Symbol': 'CCCL', 'company_name': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'financial_status': 'D', 'market_category': 'S', 'listing_exchange': 'Q'}, {'Symbol': 'CORV', 'company_name': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'financial_status': 'D', 'market_category': 'S', 'listing_exchange': 'Q'}, {'Symbol': 'CPAH', 'company_name': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'financial_status': 'D', 'market_category': 'S', 'listing_exchange': 'Q'}, {'Symbol': 'DZSI', 'company_name': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'financial_status': 'D', 'market_category': 'S', 'listing_exchange': 'Q'}, {'Symbol': 'FAMI', 'company_name': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'financial_status': 'D', 'market_category': 'S', 'listing_exchange': 'Q'}, {'Symbol': 'FTFT', 'company_name': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'financial_status': 'D', 'market_category': 'S', 'listing_exchange': 'Q'}, {'Symbol': 'FTR', 'company_name': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'financial_status': 'D', 'market_category': 'Q', 'listing_exchange': 'Q'}, {'Symbol': 'IDEX', 'company_name': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'financial_status': 'D', 'market_category': 'S', 'listing_exchange': 'Q'}, {'Symbol': 'MCEP', 'company_name': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'financial_status': 'D', 'market_category': 'S', 'listing_exchange': 'Q'}, {'Symbol': 'NXTD', 'company_name': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'financial_status': 'D', 'market_category': 'S', 'listing_exchange': 'Q'}, {'Symbol': 'OPTT', 'company_name': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'financial_status': 'D', 'market_category': 'S', 'listing_exchange': 'Q'}, {'Symbol': 'PEIX', 'company_name': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'financial_status': 'D', 'market_category': 'S', 'listing_exchange': 'Q'}, {'Symbol': 'RBZ', 'company_name': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'financial_status': 'D', 'market_category': 'G', 'listing_exchange': 'Q'}, {'Symbol': 'SES', 'company_name': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'financial_status': 'H', 'market_category': 'S', 'listing_exchange': 'Q'}, {'Symbol': 'SNSS', 'company_name': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'financial_status': 'D', 'market_category': 'S', 'listing_exchange': 'Q'}, {'Symbol': 'SPI', 'company_name': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'financial_status': 'D', 'market_category': 'Q', 'listing_exchange': 'Q'}, {'Symbol': 'SYPR', 'company_name': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'financial_status': 'D', 'market_category': 'G', 'listing_exchange': 'Q'}, {'Symbol': 'VTIQW', 'company_name': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'financial_status': 'D', 'market_category': 'S', 'listing_exchange': 'Q'}], 'var_call_bJjWGpr3hoLhagoXjFyzfe1d': 'file_storage/call_bJjWGpr3hoLhagoXjFyzfe1d.json', 'var_call_2pmdbQlL5YOiWSxrQi4lL3V1': [{'avg_vol': 'nan'}], 'var_call_2F1m4hgDmRvC1rmyiEwzONis': [{'avg_vol': 'nan'}], 'var_call_1uMUJmB38e4PMVvuMo7Ba40g': [{'avg_vol': '23781.422924901184'}], 'var_call_suNL0ZLgB5Uz28mf09Bf73HL': [{'avg_vol': 'nan'}], 'var_call_SzkQ2XllWzyfcrDSj53EQFHr': [{'avg_vol': '10988.142292490118'}], 'var_call_c6lVCsEoUmFCndzFdphLccMs': [{'avg_vol': '86223.32015810277'}], 'var_call_DlgsUWzhHeEoVwFOt96TKBmW': [{'avg_vol': '4366.798418972332'}], 'var_call_GndktVeTHc9k6qrlctlfohQ1': [{'avg_vol': '145247.8260869565'}], 'var_call_BjVgUlJonTjSaDK8lr5VE8AN': [{'avg_vol': '375.49407114624506'}], 'var_call_qgWqIh73ELHTBK56s2EsTAEw': [{'avg_vol': '15578.656126482214'}], 'var_call_5Cn2OsRsYzmKe742cdGlgKqi': [{'avg_vol': 'nan'}], 'var_call_ZiBOKDOlC1R2023nNJkB8fso': [{'avg_vol': '9.845238095238095'}], 'var_call_QtqmJtXSfGb4lUJEPaBi1cTs': [{'avg_vol': '254397.62845849802'}], 'var_call_64fASn1Yl2GSGfgXwwhuG35E': [{'avg_vol': '10.276679841897232'}], 'var_call_Z49iGJCkF4Sz8WCot84IGkQA': [{'avg_vol': 'nan'}], 'var_call_FLKAHKwrEQ4kHD7bG3kV1zyO': [{'avg_vol': 'nan'}], 'var_call_eXSraKNs7uuvj4qdFLcbwVYJ': [{'avg_vol': '254.1501976284585'}], 'var_call_GOub14IuJHMwuEjnAhDtNKTz': [{'avg_vol': '10706.719367588932'}], 'var_call_RfOLWSbEfhjDfunZLkdFUC2X': [{'avg_vol': 'nan'}], 'var_call_FVH7G8sPuUZvvBfIMSdVkuIq': [{'avg_vol': '2390.513833992095'}], 'var_call_ZyQfdimaX1ObXgLc46dhT1B4': [{'avg_vol': '781.8181818181819'}], 'var_call_rtpKfpehf8176yBarwwkpwhj': [{'avg_vol': 'nan'}], 'var_call_gByyyLVd28DBmjCzZWInrrD3': [{'avg_vol': '36836.36363636364'}]}

exec(code, env_args)
