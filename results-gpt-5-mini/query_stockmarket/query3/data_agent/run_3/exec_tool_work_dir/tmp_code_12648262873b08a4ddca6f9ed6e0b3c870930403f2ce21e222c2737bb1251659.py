code = """import json
# Load troubled stock info
stockinfo = var_call_qW3pEfwKstIZFiwWVwHusXKc
# Symbols present from earlier
symbols_present = var_call_NtNqbYOUQTLqchbdB49GgJhD
# Map symbols to company description
sym_to_name = {r['Symbol']: r['Company Description'] for r in stockinfo}
# Load avg vol results in the same order as symbols_present
results_vars = [
    var_call_Adsl7JFSAXxxDaIlEBGkcmx7,
    var_call_aQYKXSzmi3mRox86wLTYRQEy,
    var_call_RQV9ZALDHAZVuuKHWh10A7Dv,
    var_call_0kx0946KnOeb5OAAM9L8Q1R9,
    var_call_eRHsDEZ4KjJWm2vaAD5LKNap,
    var_call_05gGuuhUM2hge8DDTvNMDGb1,
    var_call_3AobYroxa1lL5hUe6DKwiM8z,
    var_call_Gmnj29EBXHOJ9LGo4HUxaIuB,
    var_call_RDyGnqTHgKju8Qsa4yCP1p3w,
    var_call_qc83U9Gmluahi4f7SUfnkVs1,
    var_call_Zt96Rkr6maINPGz9apPlddnd,
    var_call_sxlZBrl4rYRZMfsejYDFNEvf,
    var_call_HACuTGidbGxvzi6UNONZKdYi,
    var_call_8ZfLCnC54b5dzoODDglQJ5ih,
    var_call_slxR9WFxWIdls2F8XqfFOhFe,
    var_call_dMUz99wLnjbOVcWvpU9cPKWE,
    var_call_bMjjLTIeaVWYWTFjRwiB7FPv,
    var_call_kZEavC2SILtFrHJacFal65jf,
    var_call_6Bac48eHYU2B0udyUY8ZsObh,
    var_call_PRHMILaNozHLkFWynBhYx80Z,
    var_call_V5BGJPkaUW6zuFBcyhHzvpZN,
    var_call_jA2W2Zys9hHnkmuRgurPOhZu,
    var_call_zcn5wssedrLLoF5NpZbPGTRO,
    var_call_HulerkhtEqMDlb4dDX1dRqre,
    var_call_KfUxNf5TzQYEjyMuktijyKTV
]

output = []
for sym, var in zip(symbols_present, results_vars):
    # each var is a list containing one dict with 'avg_vol'
    try:
        rec = var[0]
        val = rec.get('avg_vol')
    except Exception:
        val = None
    # interpret 'nan' or None as missing
    try:
        if val is None:
            continue
        # If it's a string 'nan'
        if isinstance(val, str) and val.lower() == 'nan':
            continue
        avg = float(val)
        # If avg is NaN
        if avg != avg:
            continue
    except Exception:
        continue
    company = sym_to_name.get(sym, None)
    output.append({'Symbol': sym, 'Company Description': company, 'AvgDailyVolume2008': avg})

# Print in required format
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_qW3pEfwKstIZFiwWVwHusXKc': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'AMTX', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'Market Category': 'G', 'Financial Status': 'D'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'CBAT', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'CCCL', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'CORV', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'CPAH', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'DZSI', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'FAMI', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'FTFT', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'FTR', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'Market Category': 'Q', 'Financial Status': 'D'}, {'Symbol': 'IDEX', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'ISDS', 'Company Description': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'Market Category': 'G', 'Financial Status': 'D'}, {'Symbol': 'MCEP', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'NXTD', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'OPTT', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'PEIX', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'RBZ', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'Market Category': 'G', 'Financial Status': 'D'}, {'Symbol': 'SES', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'Market Category': 'S', 'Financial Status': 'H'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'SPI', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'Market Category': 'Q', 'Financial Status': 'D'}, {'Symbol': 'SYPR', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'Market Category': 'G', 'Financial Status': 'D'}, {'Symbol': 'VTIQW', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'Market Category': 'S', 'Financial Status': 'D'}], 'var_call_7wBQhyitmwRYJjHrnGtprPaC': 'file_storage/call_7wBQhyitmwRYJjHrnGtprPaC.json', 'var_call_NtNqbYOUQTLqchbdB49GgJhD': ['AGMH', 'AMTX', 'APEX', 'BIOC', 'BKYI', 'CBAT', 'CCCL', 'CORV', 'CPAH', 'DZSI', 'FAMI', 'FTFT', 'FTR', 'IDEX', 'ISDS', 'MCEP', 'NXTD', 'OPTT', 'PEIX', 'RBZ', 'SES', 'SNSS', 'SPI', 'SYPR', 'VTIQW'], 'var_call_Adsl7JFSAXxxDaIlEBGkcmx7': [{'avg_vol': 'nan'}], 'var_call_aQYKXSzmi3mRox86wLTYRQEy': [{'avg_vol': 'nan'}], 'var_call_RQV9ZALDHAZVuuKHWh10A7Dv': [{'avg_vol': '23781.422924901184'}], 'var_call_0kx0946KnOeb5OAAM9L8Q1R9': [{'avg_vol': 'nan'}], 'var_call_eRHsDEZ4KjJWm2vaAD5LKNap': [{'avg_vol': '10988.142292490118'}], 'var_call_05gGuuhUM2hge8DDTvNMDGb1': [{'avg_vol': '86223.32015810277'}], 'var_call_3AobYroxa1lL5hUe6DKwiM8z': [{'avg_vol': '4366.798418972332'}], 'var_call_Gmnj29EBXHOJ9LGo4HUxaIuB': [{'avg_vol': '145247.8260869565'}], 'var_call_RDyGnqTHgKju8Qsa4yCP1p3w': [{'avg_vol': '375.49407114624506'}], 'var_call_qc83U9Gmluahi4f7SUfnkVs1': [{'avg_vol': '15578.656126482214'}], 'var_call_Zt96Rkr6maINPGz9apPlddnd': [{'avg_vol': 'nan'}], 'var_call_sxlZBrl4rYRZMfsejYDFNEvf': [{'avg_vol': '9.845238095238095'}], 'var_call_HACuTGidbGxvzi6UNONZKdYi': [{'avg_vol': '254397.62845849802'}], 'var_call_8ZfLCnC54b5dzoODDglQJ5ih': [{'avg_vol': '10.276679841897232'}], 'var_call_slxR9WFxWIdls2F8XqfFOhFe': [{'avg_vol': 'nan'}], 'var_call_dMUz99wLnjbOVcWvpU9cPKWE': [{'avg_vol': 'nan'}], 'var_call_bMjjLTIeaVWYWTFjRwiB7FPv': [{'avg_vol': 'nan'}], 'var_call_kZEavC2SILtFrHJacFal65jf': [{'avg_vol': '254.1501976284585'}], 'var_call_6Bac48eHYU2B0udyUY8ZsObh': [{'avg_vol': '10706.719367588932'}], 'var_call_PRHMILaNozHLkFWynBhYx80Z': [{'avg_vol': 'nan'}], 'var_call_V5BGJPkaUW6zuFBcyhHzvpZN': [{'avg_vol': '2390.513833992095'}], 'var_call_jA2W2Zys9hHnkmuRgurPOhZu': [{'avg_vol': '781.8181818181819'}], 'var_call_zcn5wssedrLLoF5NpZbPGTRO': [{'avg_vol': 'nan'}], 'var_call_HulerkhtEqMDlb4dDX1dRqre': [{'avg_vol': '36836.36363636364'}], 'var_call_KfUxNf5TzQYEjyMuktijyKTV': [{'avg_vol': 'nan'}]}

exec(code, env_args)
