code = """import json
import math
info = var_call_waSFsohGyMmKnOxVTn9r3SPX
symbol_to_desc = {item['Symbol']: item['Company Description'] for item in info}

# mapping of symbols to their corresponding avg result variables
symbol_var_map = {
 'AGMH': var_call_cFjEq9dPXpDDTxhJUS76GEFL,
 'AMTX': var_call_OhDsJFZykR13apYcRCleM3uX,
 'APEX': var_call_uGKsosm6ZvZpLp8BXKsmH7X0,
 'BIOC': var_call_RIvV6nuWtFxhRVGRg6Hu3BBv,
 'BKYI': var_call_yexNpst53KwfsCFhvEFzrGe4,
 'CBAT': var_call_6TSKdKzAQXxTwCgHONQr60e9,
 'CCCL': var_call_2CdngC0VaNqBnjPckVSf4Ur1,
 'CORV': var_call_4UEkJKjplZ9WVRDtc5bpZXTZ,
 'CPAH': var_call_SMqKJ6IGxZy8qjBQm5cILZHv,
 'DZSI': var_call_brW0JzTGkzrQDqA8RyAVarrT,
 'FAMI': var_call_DPKo5ZC4tsCflCKdpPoGc6Cm,
 'FTFT': var_call_whYdgsrQALtxAWa3N20VV396,
 'FTR': var_call_oqCZ75QADXQS1XsqvSEHQIhc,
 'IDEX': var_call_36xOwj0kzF4U2n8ekfChBTCG,
 'ISDS': var_call_T8zJCW4Ugkx0kolCtOofHtCy,
 'MCEP': var_call_c7InLK1rFcQxRTIiNIGUPs3I,
 'NXTD': var_call_IP85cZFtrCUvgqTESFBBlRCD,
 'OPTT': var_call_xc2ezXiDLuLGtJGo9omaKOps,
 'PEIX': var_call_CF12v8Lquqjt14EVxPZjow6u,
 'RBZ': var_call_34pJ5bUphSPReOxaWhXg2tKL,
 'SES': var_call_o8wyNqXOxefHVzkKELoFDwh7,
 'SNSS': var_call_olYi6uajzQYxbl68B1Hty0q0,
 'SPI': var_call_uoMa3fYSi09xLzRlFdu4ESt6,
 'SYPR': var_call_SXh7eheXwGPGxDmlvrrWoNbI,
 'VTIQW': var_call_5QsaEftPX8JLnYBRD74L1FZF
}

results = []
for sym, res in symbol_var_map.items():
    try:
        avg_raw = res[0].get('avg_vol')
    except Exception:
        avg_raw = None
    val = None
    if avg_raw is None:
        val = None
    else:
        # avg_raw might be string 'nan' or numeric string
        try:
            valf = float(avg_raw)
            if math.isnan(valf):
                val = None
            else:
                # keep as float or int if whole
                if abs(valf - round(valf)) < 1e-9:
                    val = int(round(valf))
                else:
                    val = valf
        except Exception:
            val = None
    if val is not None and sym in symbol_to_desc:
        results.append({
            'Symbol': sym,
            'Company Description': symbol_to_desc[sym],
            'AvgDailyVolume2008': val
        })

# sort results by Symbol for consistency
results = sorted(results, key=lambda x: x['Symbol'])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_waSFsohGyMmKnOxVTn9r3SPX': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'AMTX', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CBAT', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CCCL', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CORV', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'CPAH', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'DZSI', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FAMI', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FTFT', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'FTR', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'Financial Status': 'D', 'Market Category': 'Q'}, {'Symbol': 'IDEX', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'ISDS', 'Company Description': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'MCEP', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'NXTD', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'OPTT', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'PEIX', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'RBZ', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'SES', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'Financial Status': 'H', 'Market Category': 'S'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'Financial Status': 'D', 'Market Category': 'S'}, {'Symbol': 'SPI', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'Financial Status': 'D', 'Market Category': 'Q'}, {'Symbol': 'SYPR', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'Financial Status': 'D', 'Market Category': 'G'}, {'Symbol': 'VTIQW', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'Financial Status': 'D', 'Market Category': 'S'}], 'var_call_cFjEq9dPXpDDTxhJUS76GEFL': [{'avg_vol': 'nan'}], 'var_call_OhDsJFZykR13apYcRCleM3uX': [{'avg_vol': 'nan'}], 'var_call_uGKsosm6ZvZpLp8BXKsmH7X0': [{'avg_vol': '23781.422924901184'}], 'var_call_RIvV6nuWtFxhRVGRg6Hu3BBv': [{'avg_vol': 'nan'}], 'var_call_yexNpst53KwfsCFhvEFzrGe4': [{'avg_vol': '10988.142292490118'}], 'var_call_6TSKdKzAQXxTwCgHONQr60e9': [{'avg_vol': '86223.32015810277'}], 'var_call_2CdngC0VaNqBnjPckVSf4Ur1': [{'avg_vol': '4366.798418972332'}], 'var_call_4UEkJKjplZ9WVRDtc5bpZXTZ': [{'avg_vol': '145247.8260869565'}], 'var_call_SMqKJ6IGxZy8qjBQm5cILZHv': [{'avg_vol': '375.49407114624506'}], 'var_call_brW0JzTGkzrQDqA8RyAVarrT': [{'avg_vol': '15578.656126482214'}], 'var_call_DPKo5ZC4tsCflCKdpPoGc6Cm': [{'avg_vol': 'nan'}], 'var_call_whYdgsrQALtxAWa3N20VV396': [{'avg_vol': '9.845238095238095'}], 'var_call_oqCZ75QADXQS1XsqvSEHQIhc': [{'avg_vol': '254397.62845849802'}], 'var_call_36xOwj0kzF4U2n8ekfChBTCG': [{'avg_vol': '10.276679841897232'}], 'var_call_T8zJCW4Ugkx0kolCtOofHtCy': [{'avg_vol': 'nan'}], 'var_call_c7InLK1rFcQxRTIiNIGUPs3I': [{'avg_vol': 'nan'}], 'var_call_IP85cZFtrCUvgqTESFBBlRCD': [{'avg_vol': 'nan'}], 'var_call_xc2ezXiDLuLGtJGo9omaKOps': [{'avg_vol': '254.1501976284585'}], 'var_call_CF12v8Lquqjt14EVxPZjow6u': [{'avg_vol': '10706.719367588932'}], 'var_call_34pJ5bUphSPReOxaWhXg2tKL': [{'avg_vol': 'nan'}], 'var_call_o8wyNqXOxefHVzkKELoFDwh7': [{'avg_vol': '2390.513833992095'}], 'var_call_olYi6uajzQYxbl68B1Hty0q0': [{'avg_vol': '781.8181818181819'}], 'var_call_uoMa3fYSi09xLzRlFdu4ESt6': [{'avg_vol': 'nan'}], 'var_call_SXh7eheXwGPGxDmlvrrWoNbI': [{'avg_vol': '36836.36363636364'}], 'var_call_5QsaEftPX8JLnYBRD74L1FZF': [{'avg_vol': 'nan'}]}

exec(code, env_args)
