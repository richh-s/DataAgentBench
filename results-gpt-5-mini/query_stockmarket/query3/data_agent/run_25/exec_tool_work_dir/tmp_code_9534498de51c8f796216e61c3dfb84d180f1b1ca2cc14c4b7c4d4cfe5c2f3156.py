code = """import json
# stockinfo list
stockinfo = var_call_AkFYsea3Wzk0YndSc13iAZmn
# mapping of symbol to avg result variables
symbol_vars = [
    ("AGMH", var_call_dVz3aIRJtdjNMl8E6iY6ZFzU),
    ("AMTX", var_call_VG4wG6bchgQi6bYgwbH1tVAS),
    ("APEX", var_call_D9iWXxUW3tTabaBU6w1NzhhF),
    ("BIOC", var_call_uk6WrE1NYO3TDlvNe39d8Ujb),
    ("BKYI", var_call_Bp09v6g0RkCE4U3a1xH0XYc2),
    ("CBAT", var_call_ivpp2E49fPIEszV4Std6ay8W),
    ("CCCL", var_call_W9jKvoFTTneced7lvKdgHPOe),
    ("CORV", var_call_gUtBVYCVbZ2opHM2ChbgbWD7),
    ("CPAH", var_call_KWqj2MwGKxq4travdV3gB8qq),
    ("DZSI", var_call_AK37LJxDaLvsQbMYQDlSg0R6),
    ("FAMI", var_call_aC1nlsAnXsgiij14Bkk5gSFn),
    ("FTFT", var_call_P4UUpCYxp02924QfbvQGxkut),
    ("FTR", var_call_O7ylXttZhSNb5aIOy2giU4FC),
    ("IDEX", var_call_RCuD0q9oIvhN8xNTmx9fbu3h),
    ("ISDS", var_call_6Vk3bsbLL4H3wZ5beQFASWhS),
    ("MCEP", var_call_4NZbiMmRwiucAfhy7AyH3E2W),
    ("NXTD", var_call_50FWdUOkcQbMNDdNxkLxnM3L),
    ("OPTT", var_call_8ZHILjJz7h1pdtdoQ0JgIKTN),
    ("PEIX", var_call_dfycPUozU2X4DuwfdSNGTBd1),
    ("RBZ", var_call_29T1WuDW3x7zCRic4MmVolF8),
    ("SES", var_call_YSaJ9Cvk3fJMGzrOk8BSYUFa),
    ("SNSS", var_call_0RI90aJndm5349gRiOQaeunM),
    ("SPI", var_call_SFwNJlrvyvHFdrgRegj7NnUy),
    ("SYPR", var_call_cmrZXqr5y57UQvFwUmwzSSWc),
    ("VTIQW", var_call_BWv5js1OVTGmkIPAGE0bbfH4),
]

# build symbol->avg mapping
sym_to_avg = {}
for sym, var in symbol_vars:
    try:
        v = var[0].get('avg_vol')
    except Exception:
        # fallback if structure different
        v = None
    if v is None:
        avg = None
    else:
        if isinstance(v, str) and v.lower() == 'nan':
            avg = None
        else:
            try:
                avg = float(v)
            except Exception:
                avg = None
    sym_to_avg[sym] = avg

# Now match with stockinfo entries and include only non-null averages
results = []
for rec in stockinfo:
    sym = rec.get('Symbol')
    comp = rec.get('Company Description')
    avg = sym_to_avg.get(sym)
    if avg is not None:
        # format avg to 2 decimal places
        avg_formatted = round(avg, 2)
        results.append({
            'Symbol': sym,
            'Company Description': comp,
            'avg_volume_2008': avg_formatted
        })

# Print result as JSON serializable string
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_AkFYsea3Wzk0YndSc13iAZmn': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'AMTX', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CBAT', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CCCL', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CORV', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CPAH', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'DZSI', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FAMI', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FTFT', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FTR', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'Financial Status': 'D', 'Market Category': 'Q'}, {'Symbol': 'IDEX', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'ISDS', 'Company Description': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'MCEP', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'NXTD', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'OPTT', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'PEIX', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'RBZ', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'SES', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'Financial Status': 'H', 'Market Category': 'S'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'SPI', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'Financial Status': 'D', 'Market Category': 'Q'}, {'Symbol': 'SYPR', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'VTIQW', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'Financial Status': 'D', 'Market Category': 'S'}], 'var_call_dVz3aIRJtdjNMl8E6iY6ZFzU': [{'avg_vol': 'nan'}], 'var_call_VG4wG6bchgQi6bYgwbH1tVAS': [{'avg_vol': 'nan'}], 'var_call_D9iWXxUW3tTabaBU6w1NzhhF': [{'avg_vol': '23781.422924901184'}], 'var_call_uk6WrE1NYO3TDlvNe39d8Ujb': [{'avg_vol': 'nan'}], 'var_call_Bp09v6g0RkCE4U3a1xH0XYc2': [{'avg_vol': '10988.142292490118'}], 'var_call_ivpp2E49fPIEszV4Std6ay8W': [{'avg_vol': '86223.32015810277'}], 'var_call_W9jKvoFTTneced7lvKdgHPOe': [{'avg_vol': '4366.798418972332'}], 'var_call_gUtBVYCVbZ2opHM2ChbgbWD7': [{'avg_vol': '145247.8260869565'}], 'var_call_KWqj2MwGKxq4travdV3gB8qq': [{'avg_vol': '375.49407114624506'}], 'var_call_AK37LJxDaLvsQbMYQDlSg0R6': [{'avg_vol': '15578.656126482214'}], 'var_call_aC1nlsAnXsgiij14Bkk5gSFn': [{'avg_vol': 'nan'}], 'var_call_P4UUpCYxp02924QfbvQGxkut': [{'avg_vol': '9.845238095238095'}], 'var_call_O7ylXttZhSNb5aIOy2giU4FC': [{'avg_vol': '254397.62845849802'}], 'var_call_RCuD0q9oIvhN8xNTmx9fbu3h': [{'avg_vol': '10.276679841897232'}], 'var_call_6Vk3bsbLL4H3wZ5beQFASWhS': [{'avg_vol': 'nan'}], 'var_call_4NZbiMmRwiucAfhy7AyH3E2W': [{'avg_vol': 'nan'}], 'var_call_50FWdUOkcQbMNDdNxkLxnM3L': [{'avg_vol': 'nan'}], 'var_call_8ZHILjJz7h1pdtdoQ0JgIKTN': [{'avg_vol': '254.1501976284585'}], 'var_call_dfycPUozU2X4DuwfdSNGTBd1': [{'avg_vol': '10706.719367588932'}], 'var_call_29T1WuDW3x7zCRic4MmVolF8': [{'avg_vol': 'nan'}], 'var_call_YSaJ9Cvk3fJMGzrOk8BSYUFa': [{'avg_vol': '2390.513833992095'}], 'var_call_0RI90aJndm5349gRiOQaeunM': [{'avg_vol': '781.8181818181819'}], 'var_call_SFwNJlrvyvHFdrgRegj7NnUy': [{'avg_vol': 'nan'}], 'var_call_cmrZXqr5y57UQvFwUmwzSSWc': [{'avg_vol': '36836.36363636364'}], 'var_call_BWv5js1OVTGmkIPAGE0bbfH4': [{'avg_vol': 'nan'}]}

exec(code, env_args)
