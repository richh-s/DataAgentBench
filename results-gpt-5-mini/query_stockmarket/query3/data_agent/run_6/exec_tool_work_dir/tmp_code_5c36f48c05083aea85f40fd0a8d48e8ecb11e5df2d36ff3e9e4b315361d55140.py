code = """import json
import math
# Load stock info
info = var_call_3apNFEcPMCGH57ifXDpiBPJ2
# List of trade result variables in the same order as symbols from info
trade_vars = [
    var_call_iDrnP9v6NK8XoXZIiKHXg6WW,
    var_call_2Yy7AtKXDiGp3DCEGSZnvRxr,
    var_call_fSe18YYw6l5mNJksA7u2gVnc,
    var_call_IeXpaw4xVYav5YDhJsD6Qy2x,
    var_call_qQy1pHN17MaaZxQQWLHEkj3q,
    var_call_FlDS7DMNjDt6GZfNnWrRSqJc,
    var_call_ycRpJzcM8wJOH2EmEmqNgM1L,
    var_call_mlWrVFzyiUNfvTg8aJcuRrVh,
    var_call_yfnRyj9vldatpfY3VKYYkLKK,
    var_call_q5NcWDmOO2iUp6ocCoXjbNov,
    var_call_PHnqKXsyEiDL6nVcZC7q5TVW,
    var_call_QGdhUF3ehVtL30UtNqDTabrg,
    var_call_dDgXN8mvw6JO58pl3X7RxdoC,
    var_call_zLXxY6FehwqXSWVOighIfam1,
    var_call_H0UQYNLBfq6rh7EItDZm2x5P,
    var_call_Y2bqaw2j2RE4OpvV5Ki2xs31,
    var_call_gFCufpUeEIF3ClmLKPlUqdaA,
    var_call_XGd2bpGQffvOI3lCfQX5MGCL,
    var_call_LRZFwCcMMTe9sKwam1NoXGVI,
    var_call_tDVk2s7obIbsZNUky8O8uaM7,
    var_call_TOmMoMnqfXk7DC5JbIzCXR6p,
    var_call_Hr8v51JoSCV6st1X7p9008cJ,
    var_call_0qsJjiakDBHEvpBTPU8oGILC,
    var_call_vYttDSEuHEjv7Dfd32QnwfvB,
    var_call_ZyTl6mZIa0fZA0IURugjvr3v,
]

results = []
for idx, entry in enumerate(info):
    sym = entry.get('Symbol')
    comp = entry.get('Company Description')
    # corresponding trade result
    trade_res = trade_vars[idx]
    # trade_res is a list with a single dict
    if isinstance(trade_res, list) and len(trade_res) > 0:
        tr = trade_res[0]
        avg_raw = tr.get('avg_vol')
        cnt_raw = tr.get('cnt')
        # convert
        try:
            cnt = int(cnt_raw)
        except Exception:
            try:
                cnt = int(float(cnt_raw))
            except Exception:
                cnt = 0
        try:
            avg = float(avg_raw)
        except Exception:
            avg = float('nan')
        if cnt > 0 and not math.isnan(avg):
            # include
            # round avg to reasonable digits
            if abs(avg) >= 1:
                avg_out = round(avg, 6)
            else:
                avg_out = round(avg, 12)
            results.append({
                'Symbol': sym,
                'Company Description': comp,
                'Average Daily Volume 2008': avg_out
            })

# Print result as JSON string
print("__RESULT__:")
print(json.dumps(results, ensure_ascii=False))"""

env_args = {'var_call_3apNFEcPMCGH57ifXDpiBPJ2': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'AMTX', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CBAT', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CCCL', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CORV', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CPAH', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'DZSI', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FAMI', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FTFT', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FTR', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'Financial Status': 'D', 'Market Category': 'Q'}, {'Symbol': 'IDEX', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'ISDS', 'Company Description': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'MCEP', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'NXTD', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'OPTT', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'PEIX', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'RBZ', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'SES', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'Financial Status': 'H', 'Market Category': 'S'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'SPI', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'Financial Status': 'D', 'Market Category': 'Q'}, {'Symbol': 'SYPR', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'VTIQW', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'Financial Status': 'D', 'Market Category': 'S'}], 'var_call_iDrnP9v6NK8XoXZIiKHXg6WW': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_2Yy7AtKXDiGp3DCEGSZnvRxr': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_fSe18YYw6l5mNJksA7u2gVnc': [{'avg_vol': '23781.422924901184', 'cnt': '253'}], 'var_call_IeXpaw4xVYav5YDhJsD6Qy2x': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_qQy1pHN17MaaZxQQWLHEkj3q': [{'avg_vol': '10988.142292490118', 'cnt': '253'}], 'var_call_FlDS7DMNjDt6GZfNnWrRSqJc': [{'avg_vol': '86223.32015810277', 'cnt': '253'}], 'var_call_ycRpJzcM8wJOH2EmEmqNgM1L': [{'avg_vol': '4366.798418972332', 'cnt': '253'}], 'var_call_mlWrVFzyiUNfvTg8aJcuRrVh': [{'avg_vol': '145247.8260869565', 'cnt': '253'}], 'var_call_yfnRyj9vldatpfY3VKYYkLKK': [{'avg_vol': '375.49407114624506', 'cnt': '253'}], 'var_call_q5NcWDmOO2iUp6ocCoXjbNov': [{'avg_vol': '15578.656126482214', 'cnt': '253'}], 'var_call_PHnqKXsyEiDL6nVcZC7q5TVW': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_QGdhUF3ehVtL30UtNqDTabrg': [{'avg_vol': '9.845238095238095', 'cnt': '168'}], 'var_call_dDgXN8mvw6JO58pl3X7RxdoC': [{'avg_vol': '254397.62845849802', 'cnt': '253'}], 'var_call_zLXxY6FehwqXSWVOighIfam1': [{'avg_vol': '10.276679841897232', 'cnt': '253'}], 'var_call_H0UQYNLBfq6rh7EItDZm2x5P': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_Y2bqaw2j2RE4OpvV5Ki2xs31': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_gFCufpUeEIF3ClmLKPlUqdaA': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_XGd2bpGQffvOI3lCfQX5MGCL': [{'avg_vol': '254.1501976284585', 'cnt': '253'}], 'var_call_LRZFwCcMMTe9sKwam1NoXGVI': [{'avg_vol': '10706.719367588932', 'cnt': '253'}], 'var_call_tDVk2s7obIbsZNUky8O8uaM7': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_TOmMoMnqfXk7DC5JbIzCXR6p': [{'avg_vol': '2390.513833992095', 'cnt': '253'}], 'var_call_Hr8v51JoSCV6st1X7p9008cJ': [{'avg_vol': '781.8181818181819', 'cnt': '253'}], 'var_call_0qsJjiakDBHEvpBTPU8oGILC': [{'avg_vol': 'nan', 'cnt': '0'}], 'var_call_vYttDSEuHEjv7Dfd32QnwfvB': [{'avg_vol': '36836.36363636364', 'cnt': '253'}], 'var_call_ZyTl6mZIa0fZA0IURugjvr3v': [{'avg_vol': 'nan', 'cnt': '0'}]}

exec(code, env_args)
