code = """import json
# load data from previous query
info = var_call_oDEKHBuhyNVQzN0ZCRre6O5D
avg_list = [
    var_call_NmDKY1oPJYBAuLmYUnLf5JcY,
    var_call_VRi1uanlmQsxqCciJEUgyuc6,
    var_call_TQ7H4mILZipdX5rJInQdjcJZ,
    var_call_fkmLjFGneanImrhRT18oQWNX,
    var_call_SEtctDWAYbFgjF1Mjr8r9NG0,
    var_call_RzFIKtYWjLqnDROUNgndiScB,
    var_call_dvJWLUMC60D12XOeBqVJSXSx,
    var_call_AWgNNWgS6gzQFFHLs3n2jAAo,
    var_call_m91a328z3nN1xU6KmuGjkuVf,
    var_call_3yR3BEJhwnYuVJt100qOsXis,
    var_call_y0dJo1ybEcd2bSe7mMqdzn2c,
    var_call_nRKnaOFGJjnmotxCuc1f7LFD,
    var_call_YenxZG0iUdwfWCYu7RjAv5bN,
    var_call_DXnPiGdMNBR9NDWQchWntAkz,
    var_call_3d74kvmhWpHeVJSYl2c2u6ZN,
    var_call_XmCykbBdo5J1i3P5ESG6Zrw6,
    var_call_5I9Z9yKA9O3Z2JNtEA72ZcTy,
    var_call_mDOY3o9ZeZa5oe3T3dglGCPv,
    var_call_cZbDmU3aJQj4ETr9Vh0L5Z81,
    var_call_Z3P338pdxI43dSUgzTOsBfoM,
    var_call_XJbTUiVEjhIy2Tzl1ztF2b7V,
    var_call_UoJ28K6Tx2j4sS7sE5GrTtKo,
    var_call_LfVqCeDtV2jNNWY1cYrhBtj1,
    var_call_4lBaB8ksU9gcbXixA7xIDIXa,
    var_call_fiOpun7xrWQXFGEGCgApU41m,
]
results = []
for rec, avgrec in zip(info, avg_list):
    symbol = rec.get('Symbol')
    desc = rec.get('Company Description')
    # avgrec is a list like [{"avg_vol": "..."}]
    avg_val = None
    if isinstance(avgrec, list) and len(avgrec)>0:
        v = avgrec[0].get('avg_vol')
        if v is None:
            avg_val = None
        else:
            try:
                # some values may be the string 'nan'
                fv = float(v)
                if fv != fv:  # NaN check
                    avg_val = None
                else:
                    avg_val = fv
            except:
                avg_val = None
    if avg_val is not None:
        results.append({
            'Symbol': symbol,
            'Company Description': desc,
            'avg_daily_volume_2008': avg_val
        })
# convert to JSON string
out = json.dumps(results)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_oDEKHBuhyNVQzN0ZCRre6O5D': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'AMTX', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CBAT', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CCCL', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CORV', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CPAH', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'DZSI', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FAMI', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FTFT', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FTR', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'Financial Status': 'D', 'Market Category': 'Q'}, {'Symbol': 'IDEX', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'ISDS', 'Company Description': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'MCEP', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'NXTD', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'OPTT', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'PEIX', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'RBZ', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'SES', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'Financial Status': 'H', 'Market Category': 'S'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'SPI', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'Financial Status': 'D', 'Market Category': 'Q'}, {'Symbol': 'SYPR', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'VTIQW', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'Financial Status': 'D', 'Market Category': 'S'}], 'var_call_NmDKY1oPJYBAuLmYUnLf5JcY': [{'avg_vol': 'nan'}], 'var_call_VRi1uanlmQsxqCciJEUgyuc6': [{'avg_vol': 'nan'}], 'var_call_TQ7H4mILZipdX5rJInQdjcJZ': [{'avg_vol': '23781.422924901184'}], 'var_call_fkmLjFGneanImrhRT18oQWNX': [{'avg_vol': 'nan'}], 'var_call_SEtctDWAYbFgjF1Mjr8r9NG0': [{'avg_vol': '10988.142292490118'}], 'var_call_RzFIKtYWjLqnDROUNgndiScB': [{'avg_vol': '86223.32015810277'}], 'var_call_dvJWLUMC60D12XOeBqVJSXSx': [{'avg_vol': '4366.798418972332'}], 'var_call_AWgNNWgS6gzQFFHLs3n2jAAo': [{'avg_vol': '145247.8260869565'}], 'var_call_m91a328z3nN1xU6KmuGjkuVf': [{'avg_vol': '375.49407114624506'}], 'var_call_3yR3BEJhwnYuVJt100qOsXis': [{'avg_vol': '15578.656126482214'}], 'var_call_y0dJo1ybEcd2bSe7mMqdzn2c': [{'avg_vol': 'nan'}], 'var_call_nRKnaOFGJjnmotxCuc1f7LFD': [{'avg_vol': '9.845238095238095'}], 'var_call_YenxZG0iUdwfWCYu7RjAv5bN': [{'avg_vol': '254397.62845849802'}], 'var_call_DXnPiGdMNBR9NDWQchWntAkz': [{'avg_vol': '10.276679841897232'}], 'var_call_3d74kvmhWpHeVJSYl2c2u6ZN': [{'avg_vol': 'nan'}], 'var_call_XmCykbBdo5J1i3P5ESG6Zrw6': [{'avg_vol': 'nan'}], 'var_call_5I9Z9yKA9O3Z2JNtEA72ZcTy': [{'avg_vol': 'nan'}], 'var_call_mDOY3o9ZeZa5oe3T3dglGCPv': [{'avg_vol': '254.1501976284585'}], 'var_call_cZbDmU3aJQj4ETr9Vh0L5Z81': [{'avg_vol': '10706.719367588932'}], 'var_call_Z3P338pdxI43dSUgzTOsBfoM': [{'avg_vol': 'nan'}], 'var_call_XJbTUiVEjhIy2Tzl1ztF2b7V': [{'avg_vol': '2390.513833992095'}], 'var_call_UoJ28K6Tx2j4sS7sE5GrTtKo': [{'avg_vol': '781.8181818181819'}], 'var_call_LfVqCeDtV2jNNWY1cYrhBtj1': [{'avg_vol': 'nan'}], 'var_call_4lBaB8ksU9gcbXixA7xIDIXa': [{'avg_vol': '36836.36363636364'}], 'var_call_fiOpun7xrWQXFGEGCgApU41m': [{'avg_vol': 'nan'}]}

exec(code, env_args)
