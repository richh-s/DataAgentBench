code = """import json
import math
# Load stockinfo records
records = var_call_kkULyF4fIxGXrrVHRWzH038W
# Symbols in the same order as the parallel queries
symbols = [r['Symbol'] for r in records]
# Corresponding query result variable names in order
result_vars = [
    var_call_Ln2W9G1wfgBiQVTj6VsJJhl4,
    var_call_vy0Hq5FFpji9u9jhzjkSGPDV,
    var_call_DTA3IJWXaiZ4z7Ss6bpnrqur,
    var_call_V6ZXgDUhKkvM7jNdtmZx6i9B,
    var_call_wCcfzXqZPmBbyqsKPWLaE445,
    var_call_AZaEjRRYjGmjEfYMdzaP8Vdg,
    var_call_ZxqJqpRGbH2Xf45xedsjxCjs,
    var_call_eB3oFdj0DeTMhtZfkj9NkdFX,
    var_call_MW5hb3rYhjLbHk8GvnnmjHbG,
    var_call_EHYC4y81AzoQLPfdFQJ3b5TW,
    var_call_p5qIeHBbDH1ITTJRehSaGwtD,
    var_call_p7mmzAQKg9xhoFY3fsWuS85l,
    var_call_s03C8HYkKzLR3kAJ7Qsrlapf,
    var_call_NClRN0AHxXKNISFwpwrkmymd,
    var_call_Kp7gDnMpwVcyld0OCJH54PtE,
    var_call_gmPovVuhrkvYN4N82wqEkOYc,
    var_call_OPwPQ486oOLmthclMKph1pr2,
    var_call_cGM2DnGDjJ09wD5xovDqq6kI,
    var_call_mrle8qMB3yT6Tvt1BwwkQtNo,
    var_call_t0tI8VawbUqLevsVyzriQ6cG,
    var_call_x12NJR8gvDqC4jfgYGqFFG2C,
    var_call_3dSFxAEIZ96kbPG3uP9jQV0t,
    var_call_NnxfgXajARNiauq9nF5B3gBb,
    var_call_lUucx3uAMlPy47KGD2T0LcPY,
    var_call_ALhIZcisEPjp8TKspIcspJeH
]

# Build mapping symbol -> avg_volume if non_null_count > 0
results = []
for sym, res_var, rec in zip(symbols, result_vars, records):
    # Each res_var is a list with one dict
    entry = None
    if isinstance(res_var, list) and len(res_var) > 0:
        d = res_var[0]
        # attempt to parse non_null_count
        try:
            non_null = int(d.get('non_null_count'))
        except Exception:
            # sometimes might be numeric
            try:
                non_null = int(float(d.get('non_null_count')))
            except Exception:
                non_null = 0
        if non_null > 0:
            # parse avg_volume
            avg_raw = d.get('avg_volume')
            try:
                avg = float(avg_raw)
                if math.isnan(avg):
                    avg = None
            except Exception:
                avg = None
            if avg is not None:
                results.append({
                    'Symbol': sym,
                    'Company Description': rec.get('Company Description'),
                    'avg_volume_2008': avg
                })

# Print JSON serializable string
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_kkULyF4fIxGXrrVHRWzH038W': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'AMTX', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CBAT', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CCCL', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CORV', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CPAH', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'DZSI', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FAMI', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FTFT', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FTR', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'Financial Status': 'D', 'Market Category': 'Q'}, {'Symbol': 'IDEX', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'ISDS', 'Company Description': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'MCEP', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'NXTD', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'OPTT', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'PEIX', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'RBZ', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'SES', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'Financial Status': 'H', 'Market Category': 'S'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'SPI', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'Financial Status': 'D', 'Market Category': 'Q'}, {'Symbol': 'SYPR', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'VTIQW', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'Financial Status': 'D', 'Market Category': 'S'}], 'var_call_Ln2W9G1wfgBiQVTj6VsJJhl4': [{'avg_volume': 'nan', 'non_null_count': '0'}], 'var_call_vy0Hq5FFpji9u9jhzjkSGPDV': [{'avg_volume': 'nan', 'non_null_count': '0'}], 'var_call_DTA3IJWXaiZ4z7Ss6bpnrqur': [{'avg_volume': '23781.422924901184', 'non_null_count': '253'}], 'var_call_V6ZXgDUhKkvM7jNdtmZx6i9B': [{'avg_volume': 'nan', 'non_null_count': '0'}], 'var_call_wCcfzXqZPmBbyqsKPWLaE445': [{'avg_volume': '10988.142292490118', 'non_null_count': '253'}], 'var_call_AZaEjRRYjGmjEfYMdzaP8Vdg': [{'avg_volume': '86223.32015810277', 'non_null_count': '253'}], 'var_call_ZxqJqpRGbH2Xf45xedsjxCjs': [{'avg_volume': '4366.798418972332', 'non_null_count': '253'}], 'var_call_eB3oFdj0DeTMhtZfkj9NkdFX': [{'avg_volume': '145247.8260869565', 'non_null_count': '253'}], 'var_call_MW5hb3rYhjLbHk8GvnnmjHbG': [{'avg_volume': '375.49407114624506', 'non_null_count': '253'}], 'var_call_EHYC4y81AzoQLPfdFQJ3b5TW': [{'avg_volume': '15578.656126482214', 'non_null_count': '253'}], 'var_call_p5qIeHBbDH1ITTJRehSaGwtD': [{'avg_volume': 'nan', 'non_null_count': '0'}], 'var_call_p7mmzAQKg9xhoFY3fsWuS85l': [{'avg_volume': '9.845238095238095', 'non_null_count': '168'}], 'var_call_s03C8HYkKzLR3kAJ7Qsrlapf': [{'avg_volume': '254397.62845849802', 'non_null_count': '253'}], 'var_call_NClRN0AHxXKNISFwpwrkmymd': [{'avg_volume': '10.276679841897232', 'non_null_count': '253'}], 'var_call_Kp7gDnMpwVcyld0OCJH54PtE': [{'avg_volume': 'nan', 'non_null_count': '0'}], 'var_call_gmPovVuhrkvYN4N82wqEkOYc': [{'avg_volume': 'nan', 'non_null_count': '0'}], 'var_call_OPwPQ486oOLmthclMKph1pr2': [{'avg_volume': 'nan', 'non_null_count': '0'}], 'var_call_cGM2DnGDjJ09wD5xovDqq6kI': [{'avg_volume': '254.1501976284585', 'non_null_count': '253'}], 'var_call_mrle8qMB3yT6Tvt1BwwkQtNo': [{'avg_volume': '10706.719367588932', 'non_null_count': '253'}], 'var_call_t0tI8VawbUqLevsVyzriQ6cG': [{'avg_volume': 'nan', 'non_null_count': '0'}], 'var_call_x12NJR8gvDqC4jfgYGqFFG2C': [{'avg_volume': '2390.513833992095', 'non_null_count': '253'}], 'var_call_3dSFxAEIZ96kbPG3uP9jQV0t': [{'avg_volume': '781.8181818181819', 'non_null_count': '253'}], 'var_call_NnxfgXajARNiauq9nF5B3gBb': [{'avg_volume': 'nan', 'non_null_count': '0'}], 'var_call_lUucx3uAMlPy47KGD2T0LcPY': [{'avg_volume': '36836.36363636364', 'non_null_count': '253'}], 'var_call_ALhIZcisEPjp8TKspIcspJeH': [{'avg_volume': 'nan', 'non_null_count': '0'}]}

exec(code, env_args)
