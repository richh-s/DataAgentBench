code = """import json
# stockinfo list
stockinfo = var_call_udNb2F1NYp8p6QEbB7a2BXBq

# mapping symbol -> company description
sym_to_desc = {entry['Symbol']: entry.get('Company Description') for entry in stockinfo}

# mapping of trade result variables to symbols
trade_results = {
    'APEX': var_call_HgIK4Gmv5LwKQvhcNxCM09ew,
    'BKYI': var_call_hnd2T1OsYaK1mN8LKXuFqf2l,
    'CBAT': var_call_mMBmnT0V3JuhZslgkercglFx,
    'CCCL': var_call_gZ425p0YFT5nElLv2z2OsAUd,
    'CORV': var_call_T1ceIGYKEzxPNBv9M9KFEmnE,
    'CPAH': var_call_gCzGjU17KJuvcgg14asNrDQ5,
    'DZSI': var_call_Owm25iRZlfBGqAJ61UotnFIz,
    'FTFT': var_call_Uf2poxVGbHcU2E6G6JMjlVbs,
    'IDEX': var_call_CMdhNrEITZ0OGMmoUIKYGGwq,
    'OPTT': var_call_3thFscF9DBdAXQcUPdgdjTOi,
    'PEIX': var_call_54O8nB7IUL7oLr72rF6byRBd,
    'SES': var_call_qjDLBcBAeq4LL6mHcGZ2B1ZL,
    'SNSS': var_call_8UDBV0oQCl2MBxGmqKTXFFrj,
    'SYPR': var_call_Q0pEyHBlWdBtqUgSmPcBAt77,
    'FTR': var_call_LLOAI9bxoGDBsdg9MJQg40u6,
}

results = []
for sym, res_var in trade_results.items():
    # each res_var is a list with one dict
    try:
        rec = res_var[0]
    except Exception:
        # skip if missing
        continue
    avg = rec.get('avg_vol')
    count = rec.get('count_vol')
    # convert values
    try:
        if avg is None or str(avg).lower() == 'nan':
            avg_val = None
        else:
            avg_val = float(avg)
    except Exception:
        avg_val = None
    try:
        cnt = int(count)
    except Exception:
        cnt = 0
    if cnt > 0 and avg_val is not None:
        results.append({
            'Symbol': sym,
            'Company Description': sym_to_desc.get(sym),
            'avg_daily_volume_2008': avg_val
        })

# sort results by Symbol for consistency
results = sorted(results, key=lambda x: x['Symbol'])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_udNb2F1NYp8p6QEbB7a2BXBq': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'AMTX', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CBAT', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CCCL', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CORV', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CPAH', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'DZSI', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FAMI', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FTFT', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FTR', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'Financial Status': 'D', 'Market Category': 'Q'}, {'Symbol': 'IDEX', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'ISDS', 'Company Description': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'MCEP', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'NXTD', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'OPTT', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'PEIX', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'RBZ', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'SES', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'Financial Status': 'H', 'Market Category': 'S'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'SPI', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'Financial Status': 'D', 'Market Category': 'Q'}, {'Symbol': 'SYPR', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'VTIQW', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'Financial Status': 'D', 'Market Category': 'S'}], 'var_call_mytAhfy6Pa9qwMivEjhNTQdN': [{'avg_vol': 'nan', 'count_vol': '0'}], 'var_call_xq1CfpmexukAkD9OuUOK8pMX': [{'avg_vol': 'nan', 'count_vol': '0'}], 'var_call_tBuObxHPhOHa7X5b7zgdHXvx': [{'avg_vol': 'nan', 'count_vol': '0'}], 'var_call_HgIK4Gmv5LwKQvhcNxCM09ew': [{'avg_vol': '23781.422924901184', 'count_vol': '253'}], 'var_call_xSFqhNeQDz24mJQM6a43z55y': [{'avg_vol': 'nan', 'count_vol': '0'}], 'var_call_hnd2T1OsYaK1mN8LKXuFqf2l': [{'avg_vol': '10988.142292490118', 'count_vol': '253'}], 'var_call_mMBmnT0V3JuhZslgkercglFx': [{'avg_vol': '86223.32015810277', 'count_vol': '253'}], 'var_call_gZ425p0YFT5nElLv2z2OsAUd': [{'avg_vol': '4366.798418972332', 'count_vol': '253'}], 'var_call_T1ceIGYKEzxPNBv9M9KFEmnE': [{'avg_vol': '145247.8260869565', 'count_vol': '253'}], 'var_call_gCzGjU17KJuvcgg14asNrDQ5': [{'avg_vol': '375.49407114624506', 'count_vol': '253'}], 'var_call_Owm25iRZlfBGqAJ61UotnFIz': [{'avg_vol': '15578.656126482214', 'count_vol': '253'}], 'var_call_aIGrVb6epHm1i6zUPXTZ7zbC': [{'avg_vol': 'nan', 'count_vol': '0'}], 'var_call_Uf2poxVGbHcU2E6G6JMjlVbs': [{'avg_vol': '9.845238095238095', 'count_vol': '168'}], 'var_call_CMdhNrEITZ0OGMmoUIKYGGwq': [{'avg_vol': '10.276679841897232', 'count_vol': '253'}], 'var_call_IPLVx7VbXYisNq6WDBVHwCsn': [{'avg_vol': 'nan', 'count_vol': '0'}], 'var_call_ByYSzSmFk2zcbbXu9onE3Dm5': [{'avg_vol': 'nan', 'count_vol': '0'}], 'var_call_c7wYPfzrzYFie4WWignRqg08': [{'avg_vol': 'nan', 'count_vol': '0'}], 'var_call_3thFscF9DBdAXQcUPdgdjTOi': [{'avg_vol': '254.1501976284585', 'count_vol': '253'}], 'var_call_54O8nB7IUL7oLr72rF6byRBd': [{'avg_vol': '10706.719367588932', 'count_vol': '253'}], 'var_call_GNY1hOvDcMxMWBNm2golGJ10': [{'avg_vol': 'nan', 'count_vol': '0'}], 'var_call_qjDLBcBAeq4LL6mHcGZ2B1ZL': [{'avg_vol': '2390.513833992095', 'count_vol': '253'}], 'var_call_8UDBV0oQCl2MBxGmqKTXFFrj': [{'avg_vol': '781.8181818181819', 'count_vol': '253'}], 'var_call_5gr4Yhf6lFfMOdatmYWomXfq': [{'avg_vol': 'nan', 'count_vol': '0'}], 'var_call_Q0pEyHBlWdBtqUgSmPcBAt77': [{'avg_vol': '36836.36363636364', 'count_vol': '253'}], 'var_call_bxUKDnsDPnQGTCknxduNVIQI': [{'avg_vol': 'nan', 'count_vol': '0'}], 'var_call_LLOAI9bxoGDBsdg9MJQg40u6': [{'avg_vol': '254397.62845849802', 'count_vol': '253'}]}

exec(code, env_args)
