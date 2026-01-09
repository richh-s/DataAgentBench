code = """import json

def to_float(x):
    if x is None:
        return None
    if isinstance(x, (int, float)):
        return float(x)
    s = str(x)
    if s.lower() == 'nan':
        return None
    try:
        return float(s)
    except:
        return None

# troubled meta
meta = {r['Symbol']: r['company_name'] for r in var_call_DSqrvggeanV5iCEYXP27gqpN}

vol_rows = []
for key in [
    'var_call_gTAubJvY98Toaxn3XUhrQPL9',
    'var_call_ci6UPicVDeevdRqAYpAXNR1h',
    'var_call_VYel5uDmwo9WID4pYKzCEVu6',
    'var_call_8x6BWQSnovLUdvQXONhUr4Ny',
    'var_call_t5nIq7sJx9R0iZ3hHQ6uoDZf',
    'var_call_DMQf88WynZLuoTpcXCfKOBDv',
    'var_call_UsGl07VoaH8klPGzO7pum34p',
    'var_call_NjOCleUcBJ5VevbzKEAVY0Lt',
    'var_call_klYKMQT9Sfs0qP03V7jtLpLA',
    'var_call_tujUaH4Y1K8s9s4rAf7Jvupt',
    'var_call_gdFf49LNmb0BCaA8qRn5REA6',
    'var_call_2FUw30uFGLJDF3arXLxFjHSj',
    'var_call_Fhuqu5MVDQlDRQwzTZy6VDxF',
    'var_call_HGfoEvbqeQR1WEFx0fGJNzZ0',
    'var_call_v5BmwhuYf5nNHQIpHKFdcE79',
    'var_call_UC5D0nxzrfSeQY5TYy9flOtc',
    'var_call_7sbYVIlPiGmP88yRfSmWQGns',
    'var_call_KqCsCoNX059yCBPlGTX1okZN',
    'var_call_dUL3NS09GQSPMnqRFuo9Lrb6',
    'var_call_Jv5HGMjTe5XxiTvBdni3bm54',
    'var_call_29NCFw1qqXXDFmbimsArHZWQ',
    'var_call_UgwdGpaejWrgvDmA0YgQNTAw',
    'var_call_4BmUsy6kNm7YpMdeAe1CNMWP',
    'var_call_SxcntiJZHQPZkEYbXimOlg3D',
    'var_call_crbI9iRcMhzp1wVI7AomUM0z'
]:
    recs = globals()[key]
    if recs and isinstance(recs, list):
        vol_rows.extend(recs)

# filter to non-null avg volume
final = []
for r in vol_rows:
    sym = r.get('Symbol')
    avg = to_float(r.get('avg_daily_volume_2008'))
    if avg is None:
        continue
    final.append({
        'Symbol': sym,
        'Company Name': meta.get(sym),
        'Avg Daily Volume (2008)': avg
    })

# sort by company name
final = sorted(final, key=lambda x: (x['Company Name'] or '', x['Symbol']))

print('__RESULT__:')
print(json.dumps(final))"""

env_args = {'var_call_DSqrvggeanV5iCEYXP27gqpN': [{'Symbol': 'AGMH', 'company_name': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'market_category': 'S', 'financial_status': 'D'}, {'Symbol': 'AMTX', 'company_name': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'market_category': 'G', 'financial_status': 'D'}, {'Symbol': 'APEX', 'company_name': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'market_category': 'S', 'financial_status': 'D'}, {'Symbol': 'BIOC', 'company_name': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'market_category': 'S', 'financial_status': 'D'}, {'Symbol': 'BKYI', 'company_name': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'market_category': 'S', 'financial_status': 'D'}, {'Symbol': 'CBAT', 'company_name': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'market_category': 'S', 'financial_status': 'D'}, {'Symbol': 'CCCL', 'company_name': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'market_category': 'S', 'financial_status': 'D'}, {'Symbol': 'CORV', 'company_name': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'market_category': 'S', 'financial_status': 'D'}, {'Symbol': 'CPAH', 'company_name': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'market_category': 'S', 'financial_status': 'D'}, {'Symbol': 'DZSI', 'company_name': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'market_category': 'S', 'financial_status': 'D'}, {'Symbol': 'FAMI', 'company_name': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'market_category': 'S', 'financial_status': 'D'}, {'Symbol': 'FTFT', 'company_name': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'market_category': 'S', 'financial_status': 'D'}, {'Symbol': 'FTR', 'company_name': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'market_category': 'Q', 'financial_status': 'D'}, {'Symbol': 'IDEX', 'company_name': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'market_category': 'S', 'financial_status': 'D'}, {'Symbol': 'ISDS', 'company_name': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'market_category': 'G', 'financial_status': 'D'}, {'Symbol': 'MCEP', 'company_name': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'market_category': 'S', 'financial_status': 'D'}, {'Symbol': 'NXTD', 'company_name': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'market_category': 'S', 'financial_status': 'D'}, {'Symbol': 'OPTT', 'company_name': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'market_category': 'S', 'financial_status': 'D'}, {'Symbol': 'PEIX', 'company_name': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'market_category': 'S', 'financial_status': 'D'}, {'Symbol': 'RBZ', 'company_name': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'market_category': 'G', 'financial_status': 'D'}, {'Symbol': 'SES', 'company_name': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'market_category': 'S', 'financial_status': 'H'}, {'Symbol': 'SNSS', 'company_name': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'market_category': 'S', 'financial_status': 'D'}, {'Symbol': 'SPI', 'company_name': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'market_category': 'Q', 'financial_status': 'D'}, {'Symbol': 'SYPR', 'company_name': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'market_category': 'G', 'financial_status': 'D'}, {'Symbol': 'VTIQW', 'company_name': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'market_category': 'S', 'financial_status': 'D'}], 'var_call_ORlS5nzFzDWcpfjccxGefGmO': 'file_storage/call_ORlS5nzFzDWcpfjccxGefGmO.json', 'var_call_gTAubJvY98Toaxn3XUhrQPL9': [{'Symbol': 'AGMH', 'avg_daily_volume_2008': 'nan'}], 'var_call_ci6UPicVDeevdRqAYpAXNR1h': [{'Symbol': 'AMTX', 'avg_daily_volume_2008': 'nan'}], 'var_call_VYel5uDmwo9WID4pYKzCEVu6': [{'Symbol': 'APEX', 'avg_daily_volume_2008': '23781.422924901184'}], 'var_call_8x6BWQSnovLUdvQXONhUr4Ny': [{'Symbol': 'BIOC', 'avg_daily_volume_2008': 'nan'}], 'var_call_t5nIq7sJx9R0iZ3hHQ6uoDZf': [{'Symbol': 'BKYI', 'avg_daily_volume_2008': '10988.142292490118'}], 'var_call_DMQf88WynZLuoTpcXCfKOBDv': [{'Symbol': 'CBAT', 'avg_daily_volume_2008': '86223.32015810277'}], 'var_call_UsGl07VoaH8klPGzO7pum34p': [{'Symbol': 'CCCL', 'avg_daily_volume_2008': '4366.798418972332'}], 'var_call_NjOCleUcBJ5VevbzKEAVY0Lt': [{'Symbol': 'CORV', 'avg_daily_volume_2008': '145247.8260869565'}], 'var_call_klYKMQT9Sfs0qP03V7jtLpLA': [{'Symbol': 'CPAH', 'avg_daily_volume_2008': '375.49407114624506'}], 'var_call_tujUaH4Y1K8s9s4rAf7Jvupt': [{'Symbol': 'DZSI', 'avg_daily_volume_2008': '15578.656126482214'}], 'var_call_gdFf49LNmb0BCaA8qRn5REA6': [{'Symbol': 'FAMI', 'avg_daily_volume_2008': 'nan'}], 'var_call_2FUw30uFGLJDF3arXLxFjHSj': [{'Symbol': 'FTFT', 'avg_daily_volume_2008': '9.845238095238095'}], 'var_call_Fhuqu5MVDQlDRQwzTZy6VDxF': [{'Symbol': 'FTR', 'avg_daily_volume_2008': '254397.62845849802'}], 'var_call_HGfoEvbqeQR1WEFx0fGJNzZ0': [{'Symbol': 'IDEX', 'avg_daily_volume_2008': '10.276679841897232'}], 'var_call_v5BmwhuYf5nNHQIpHKFdcE79': [{'Symbol': 'ISDS', 'avg_daily_volume_2008': 'nan'}], 'var_call_UC5D0nxzrfSeQY5TYy9flOtc': [{'Symbol': 'MCEP', 'avg_daily_volume_2008': 'nan'}], 'var_call_7sbYVIlPiGmP88yRfSmWQGns': [{'Symbol': 'NXTD', 'avg_daily_volume_2008': 'nan'}], 'var_call_KqCsCoNX059yCBPlGTX1okZN': [{'Symbol': 'OPTT', 'avg_daily_volume_2008': '254.1501976284585'}], 'var_call_dUL3NS09GQSPMnqRFuo9Lrb6': [{'Symbol': 'PEIX', 'avg_daily_volume_2008': '10706.719367588932'}], 'var_call_Jv5HGMjTe5XxiTvBdni3bm54': [{'Symbol': 'RBZ', 'avg_daily_volume_2008': 'nan'}], 'var_call_29NCFw1qqXXDFmbimsArHZWQ': [{'Symbol': 'SES', 'avg_daily_volume_2008': '2390.513833992095'}], 'var_call_UgwdGpaejWrgvDmA0YgQNTAw': [{'Symbol': 'SNSS', 'avg_daily_volume_2008': '781.8181818181819'}], 'var_call_4BmUsy6kNm7YpMdeAe1CNMWP': [{'Symbol': 'SPI', 'avg_daily_volume_2008': 'nan'}], 'var_call_SxcntiJZHQPZkEYbXimOlg3D': [{'Symbol': 'SYPR', 'avg_daily_volume_2008': '36836.36363636364'}], 'var_call_crbI9iRcMhzp1wVI7AomUM0z': [{'Symbol': 'VTIQW', 'avg_daily_volume_2008': 'nan'}]}

exec(code, env_args)
