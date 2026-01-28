code = """import json, pandas as pd, math

stocks = pd.DataFrame(var_call_J8PbgZSXXroEQfHYpgNLC4JM)[['symbol','company_name']]

avg_parts = [
    var_call_h6e7ClJYqdCpFuCHARj3ICKx,
    var_call_QEIS1AqfHlusucFruqIX9Maj,
    var_call_mDaIVN4hnyeyxxNfdAynIaed,
    var_call_z8sGUflk9a42JVedNCYYnDlv,
    var_call_9cePs5SE7QRC1advTgFPokEl,
    var_call_88k5yoIuAVhPQfNpZuNuvfVK,
    var_call_wuBQIaqOfzKexkMyIoUgIkfE,
    var_call_Uhj7vuu1lxoRNG1hv2B3csgg,
    var_call_hDOdPv85pcbzWnFHL6bQAnTn,
    var_call_R5VErGNWm2Sys42m4o50PvG5,
    var_call_P95VQvmfDRh7HLUC4PJp0EJT,
    var_call_FVAMYxXCGAQVmuCkZHU1fYzC,
    var_call_zYF4nizYAZrD5YmLKYrgLl21,
    var_call_hfcr1ZDt2OIelhs42v66obTk,
    var_call_G1G6jW6Gg8G513Jykytajypy,
    var_call_xali7owlnKaENxBWzicSD19V,
    var_call_4DALcofgig9abxqqbDAbmH1m,
    var_call_mW9ernOBIa70azKvHA6iRnnX,
    var_call_qZZ5oT8GXlA4IEQhjMFoDi7v,
    var_call_EQwcvvDcI7Wj7qGnDkNmKoT5,
    var_call_8dRe4Gfc9kQUhu6L6tQQo04o,
    var_call_8OWJ5TvTVx984tH9f0jgjQRi,
    var_call_1xYKxJANlO40EPsjROODUgv0,
    var_call_T60pIK4xrHCmFHkDOF4JLqVk,
    var_call_jVK1X8D6XwisBWuMboJPZYhk,
]

rows=[]
for part in avg_parts:
    rows.extend(part)

df_avg = pd.DataFrame(rows)

def to_num(x):
    if x is None:
        return None
    try:
        v = float(x)
        if math.isnan(v):
            return None
        return v
    except Exception:
        return None

df_avg['avg_daily_volume_2008'] = df_avg['avg_daily_volume_2008'].map(to_num)

df = df_avg.merge(stocks, on='symbol', how='left')
# keep only non-null avg volumes
out = df[df['avg_daily_volume_2008'].notna()].copy()
out = out.sort_values(['company_name','symbol'])

# format answer lines
lines = []
for _, r in out.iterrows():
    lines.append(f"{r['company_name']} ({r['symbol']}): {r['avg_daily_volume_2008']:.2f}")

print('__RESULT__:')
print(json.dumps({'lines': lines, 'count': int(len(lines))}))"""

env_args = {'var_call_J8PbgZSXXroEQfHYpgNLC4JM': [{'symbol': 'AGMH', 'company_name': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'financial_status': 'D', 'market_category': 'S', 'listing_exchange': 'Q'}, {'symbol': 'AMTX', 'company_name': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'financial_status': 'D', 'market_category': 'G', 'listing_exchange': 'Q'}, {'symbol': 'APEX', 'company_name': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'financial_status': 'D', 'market_category': 'S', 'listing_exchange': 'Q'}, {'symbol': 'BIOC', 'company_name': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'financial_status': 'D', 'market_category': 'S', 'listing_exchange': 'Q'}, {'symbol': 'BKYI', 'company_name': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'financial_status': 'D', 'market_category': 'S', 'listing_exchange': 'Q'}, {'symbol': 'CBAT', 'company_name': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'financial_status': 'D', 'market_category': 'S', 'listing_exchange': 'Q'}, {'symbol': 'CCCL', 'company_name': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'financial_status': 'D', 'market_category': 'S', 'listing_exchange': 'Q'}, {'symbol': 'CORV', 'company_name': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'financial_status': 'D', 'market_category': 'S', 'listing_exchange': 'Q'}, {'symbol': 'CPAH', 'company_name': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'financial_status': 'D', 'market_category': 'S', 'listing_exchange': 'Q'}, {'symbol': 'DZSI', 'company_name': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'financial_status': 'D', 'market_category': 'S', 'listing_exchange': 'Q'}, {'symbol': 'FAMI', 'company_name': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'financial_status': 'D', 'market_category': 'S', 'listing_exchange': 'Q'}, {'symbol': 'FTFT', 'company_name': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'financial_status': 'D', 'market_category': 'S', 'listing_exchange': 'Q'}, {'symbol': 'FTR', 'company_name': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'financial_status': 'D', 'market_category': 'Q', 'listing_exchange': 'Q'}, {'symbol': 'IDEX', 'company_name': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'financial_status': 'D', 'market_category': 'S', 'listing_exchange': 'Q'}, {'symbol': 'ISDS', 'company_name': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'financial_status': 'D', 'market_category': 'G', 'listing_exchange': 'Q'}, {'symbol': 'MCEP', 'company_name': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'financial_status': 'D', 'market_category': 'S', 'listing_exchange': 'Q'}, {'symbol': 'NXTD', 'company_name': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'financial_status': 'D', 'market_category': 'S', 'listing_exchange': 'Q'}, {'symbol': 'OPTT', 'company_name': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'financial_status': 'D', 'market_category': 'S', 'listing_exchange': 'Q'}, {'symbol': 'PEIX', 'company_name': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'financial_status': 'D', 'market_category': 'S', 'listing_exchange': 'Q'}, {'symbol': 'RBZ', 'company_name': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'financial_status': 'D', 'market_category': 'G', 'listing_exchange': 'Q'}, {'symbol': 'SES', 'company_name': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'financial_status': 'H', 'market_category': 'S', 'listing_exchange': 'Q'}, {'symbol': 'SNSS', 'company_name': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'financial_status': 'D', 'market_category': 'S', 'listing_exchange': 'Q'}, {'symbol': 'SPI', 'company_name': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'financial_status': 'D', 'market_category': 'Q', 'listing_exchange': 'Q'}, {'symbol': 'SYPR', 'company_name': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'financial_status': 'D', 'market_category': 'G', 'listing_exchange': 'Q'}, {'symbol': 'VTIQW', 'company_name': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'financial_status': 'D', 'market_category': 'S', 'listing_exchange': 'Q'}], 'var_call_42g5jWIGAyTTf5JJT5Fetn46': 'file_storage/call_42g5jWIGAyTTf5JJT5Fetn46.json', 'var_call_A7aQQjIWxgDbseAqvg42EU8Z': {'symbols': ['AGMH', 'AMTX', 'APEX', 'BIOC', 'BKYI', 'CBAT', 'CCCL', 'CORV', 'CPAH', 'DZSI', 'FAMI', 'FTFT', 'FTR', 'IDEX', 'ISDS', 'MCEP', 'NXTD', 'OPTT', 'PEIX', 'RBZ', 'SES', 'SNSS', 'SPI', 'SYPR', 'VTIQW'], 'n': 25}, 'var_call_5DzIbFie9ywv51vy7KZaHjsA': 'file_storage/call_5DzIbFie9ywv51vy7KZaHjsA.json', 'var_call_h6e7ClJYqdCpFuCHARj3ICKx': [{'symbol': 'AGMH', 'avg_daily_volume_2008': 'nan'}], 'var_call_QEIS1AqfHlusucFruqIX9Maj': [{'symbol': 'AMTX', 'avg_daily_volume_2008': 'nan'}], 'var_call_mDaIVN4hnyeyxxNfdAynIaed': [{'symbol': 'APEX', 'avg_daily_volume_2008': '23781.422924901184'}], 'var_call_z8sGUflk9a42JVedNCYYnDlv': [{'symbol': 'BIOC', 'avg_daily_volume_2008': 'nan'}], 'var_call_9cePs5SE7QRC1advTgFPokEl': [{'symbol': 'BKYI', 'avg_daily_volume_2008': '10988.142292490118'}], 'var_call_88k5yoIuAVhPQfNpZuNuvfVK': [{'symbol': 'CBAT', 'avg_daily_volume_2008': '86223.32015810277'}], 'var_call_wuBQIaqOfzKexkMyIoUgIkfE': [{'symbol': 'CCCL', 'avg_daily_volume_2008': '4366.798418972332'}], 'var_call_Uhj7vuu1lxoRNG1hv2B3csgg': [{'symbol': 'CORV', 'avg_daily_volume_2008': '145247.8260869565'}], 'var_call_hDOdPv85pcbzWnFHL6bQAnTn': [{'symbol': 'CPAH', 'avg_daily_volume_2008': '375.49407114624506'}], 'var_call_R5VErGNWm2Sys42m4o50PvG5': [{'symbol': 'DZSI', 'avg_daily_volume_2008': '15578.656126482214'}], 'var_call_P95VQvmfDRh7HLUC4PJp0EJT': [{'symbol': 'FAMI', 'avg_daily_volume_2008': 'nan'}], 'var_call_FVAMYxXCGAQVmuCkZHU1fYzC': [{'symbol': 'FTFT', 'avg_daily_volume_2008': '9.845238095238095'}], 'var_call_zYF4nizYAZrD5YmLKYrgLl21': [{'symbol': 'FTR', 'avg_daily_volume_2008': '254397.62845849802'}], 'var_call_hfcr1ZDt2OIelhs42v66obTk': [{'symbol': 'IDEX', 'avg_daily_volume_2008': '10.276679841897232'}], 'var_call_G1G6jW6Gg8G513Jykytajypy': [{'symbol': 'ISDS', 'avg_daily_volume_2008': 'nan'}], 'var_call_xali7owlnKaENxBWzicSD19V': [{'symbol': 'MCEP', 'avg_daily_volume_2008': 'nan'}], 'var_call_4DALcofgig9abxqqbDAbmH1m': [{'symbol': 'NXTD', 'avg_daily_volume_2008': 'nan'}], 'var_call_mW9ernOBIa70azKvHA6iRnnX': [{'symbol': 'OPTT', 'avg_daily_volume_2008': '254.1501976284585'}], 'var_call_qZZ5oT8GXlA4IEQhjMFoDi7v': [{'symbol': 'PEIX', 'avg_daily_volume_2008': '10706.719367588932'}], 'var_call_EQwcvvDcI7Wj7qGnDkNmKoT5': [{'symbol': 'RBZ', 'avg_daily_volume_2008': 'nan'}], 'var_call_8dRe4Gfc9kQUhu6L6tQQo04o': [{'symbol': 'SES', 'avg_daily_volume_2008': '2390.513833992095'}], 'var_call_8OWJ5TvTVx984tH9f0jgjQRi': [{'symbol': 'SNSS', 'avg_daily_volume_2008': '781.8181818181819'}], 'var_call_1xYKxJANlO40EPsjROODUgv0': [{'symbol': 'SPI', 'avg_daily_volume_2008': 'nan'}], 'var_call_T60pIK4xrHCmFHkDOF4JLqVk': [{'symbol': 'SYPR', 'avg_daily_volume_2008': '36836.36363636364'}], 'var_call_jVK1X8D6XwisBWuMboJPZYhk': [{'symbol': 'VTIQW', 'avg_daily_volume_2008': 'nan'}]}

exec(code, env_args)
