code = """import json
# Variables available from previous tool calls:
# var_call_nKxvnLMziqJgtlOu7k6HGETp (stockinfo results)
# avg result variables from parallel queries:
# var_call_g9s57oFfYQUXS6JG2IrWA3g7,
# var_call_XhiF6bP8GAg0cbLlUQhf8NMv,
# var_call_dXcR4LjKVqZcvOhe0cRehbfG,
# var_call_Fcpr6HKBdFT9NWbCaWm8MMpy,
# var_call_LulVJoaxrB8EJrd2Cic2BLGS,
# var_call_V0ZSrdoYrVFPqFts8rAJIahA,
# var_call_NDXUsCi756hlrPOIvjBHqwMS,
# var_call_ciJUvSjKEXB2Bmwg7AZH9IfP,
# var_call_hYgrcnqF4dJOQXsURor4e1EI,
# var_call_C0m7OKMKaFjNX1Biqiwb9QCi,
# var_call_Aw5O20aTyeJ2vsfCBtCqsbQr,
# var_call_nVmML99TfwvUP8rJR6nKN3sA,
# var_call_FIzriC69nDSmw0dxAYPcnwYm,
# var_call_cuHp7G6ILKDjsfL3H2zJffyk,
# var_call_yUFwOJfeKXZ5BOgOaaJaac3s,
# var_call_gYTkLjg7Xb12LMOWaXsmfDm1,
# var_call_qEr1pHec4jInNs5uNwmaUUBn,
# var_call_SBUnux9K0YLMgodNFGc7EOAK,
# var_call_BHLRtnHndoTfXzxVqMMkgG52,
# var_call_osf0TYxgATbt0PxmsTrUQ6BW,
# var_call_zd0jV3EFLMs5b0Xaqd0UxVBX,
# var_call_H3G8JgTooZXHxjVIrEh0RtV4,
# var_call_gCBiyyz2Z7MDaObvFQJWm0SJ,
# var_call_oqa9vlljvIAc8U7ft3iEefqn

avg_vars = [
    var_call_g9s57oFfYQUXS6JG2IrWA3g7,
    var_call_XhiF6bP8GAg0cbLlUQhf8NMv,
    var_call_dXcR4LjKVqZcvOhe0cRehbfG,
    var_call_Fcpr6HKBdFT9NWbCaWm8MMpy,
    var_call_LulVJoaxrB8EJrd2Cic2BLGS,
    var_call_V0ZSrdoYrVFPqFts8rAJIahA,
    var_call_NDXUsCi756hlrPOIvjBHqwMS,
    var_call_ciJUvSjKEXB2Bmwg7AZH9IfP,
    var_call_hYgrcnqF4dJOQXsURor4e1EI,
    var_call_C0m7OKMKaFjNX1Biqiwb9QCi,
    var_call_Aw5O20aTyeJ2vsfCBtCqsbQr,
    var_call_nVmML99TfwvUP8rJR6nKN3sA,
    var_call_FIzriC69nDSmw0dxAYPcnwYm,
    var_call_cuHp7G6ILKDjsfL3H2zJffyk,
    var_call_yUFwOJfeKXZ5BOgOaaJaac3s,
    var_call_gYTkLjg7Xb12LMOWaXsmfDm1,
    var_call_qEr1pHec4jInNs5uNwmaUUBn,
    var_call_SBUnux9K0YLMgodNFGc7EOAK,
    var_call_BHLRtnHndoTfXzxVqMMkgG52,
    var_call_osf0TYxgATbt0PxmsTrUQ6BW,
    var_call_zd0jV3EFLMs5b0Xaqd0UxVBX,
    var_call_H3G8JgTooZXHxjVIrEh0RtV4,
    var_call_gCBiyyz2Z7MDaObvFQJWm0SJ,
    var_call_oqa9vlljvIAc8U7ft3iEefqn,
]

stockinfos = var_call_nKxvnLMziqJgtlOu7k6HGETp
results = []
for i, info in enumerate(stockinfos):
    sym = info.get('Symbol')
    comp = info.get('Company Description')
    avg_entry = avg_vars[i]
    # avg_entry is a list like [{'avg_vol': 'nan'}]
    if not isinstance(avg_entry, list) or len(avg_entry)==0:
        continue
    raw = avg_entry[0].get('avg_vol')
    try:
        if raw is None:
            continue
        # raw might be string 'nan'
        if isinstance(raw, str) and raw.lower()=='nan':
            continue
        avg = float(raw)
    except Exception:
        continue
    # include only non-null averages
    results.append({'Symbol': sym, 'Company Description': comp, 'AverageDailyVolume2008': avg})

# Print result as JSON string per required format
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_nKxvnLMziqJgtlOu7k6HGETp': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Financial Status': 'D'}, {'Symbol': 'AMTX', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'Financial Status': 'D'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'Financial Status': 'D'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'Financial Status': 'D'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'Financial Status': 'D'}, {'Symbol': 'CBAT', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'Financial Status': 'D'}, {'Symbol': 'CCCL', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'Financial Status': 'D'}, {'Symbol': 'CORV', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'Financial Status': 'D'}, {'Symbol': 'CPAH', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'Financial Status': 'D'}, {'Symbol': 'DZSI', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'Financial Status': 'D'}, {'Symbol': 'FAMI', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'Financial Status': 'D'}, {'Symbol': 'FTFT', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'Financial Status': 'D'}, {'Symbol': 'FTR', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'Financial Status': 'D'}, {'Symbol': 'IDEX', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'Financial Status': 'D'}, {'Symbol': 'ISDS', 'Company Description': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'Financial Status': 'D'}, {'Symbol': 'MCEP', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'Financial Status': 'D'}, {'Symbol': 'NXTD', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'Financial Status': 'D'}, {'Symbol': 'OPTT', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'Financial Status': 'D'}, {'Symbol': 'PEIX', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'Financial Status': 'D'}, {'Symbol': 'RBZ', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'Financial Status': 'D'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'Financial Status': 'D'}, {'Symbol': 'SPI', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'Financial Status': 'D'}, {'Symbol': 'SYPR', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'Financial Status': 'D'}, {'Symbol': 'VTIQW', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'Financial Status': 'D'}], 'var_call_g9s57oFfYQUXS6JG2IrWA3g7': [{'avg_vol': 'nan'}], 'var_call_XhiF6bP8GAg0cbLlUQhf8NMv': [{'avg_vol': 'nan'}], 'var_call_dXcR4LjKVqZcvOhe0cRehbfG': [{'avg_vol': '23781.422924901184'}], 'var_call_Fcpr6HKBdFT9NWbCaWm8MMpy': [{'avg_vol': 'nan'}], 'var_call_LulVJoaxrB8EJrd2Cic2BLGS': [{'avg_vol': '10988.142292490118'}], 'var_call_V0ZSrdoYrVFPqFts8rAJIahA': [{'avg_vol': '86223.32015810277'}], 'var_call_NDXUsCi756hlrPOIvjBHqwMS': [{'avg_vol': '4366.798418972332'}], 'var_call_ciJUvSjKEXB2Bmwg7AZH9IfP': [{'avg_vol': '145247.8260869565'}], 'var_call_hYgrcnqF4dJOQXsURor4e1EI': [{'avg_vol': '375.49407114624506'}], 'var_call_C0m7OKMKaFjNX1Biqiwb9QCi': [{'avg_vol': '15578.656126482214'}], 'var_call_Aw5O20aTyeJ2vsfCBtCqsbQr': [{'avg_vol': 'nan'}], 'var_call_nVmML99TfwvUP8rJR6nKN3sA': [{'avg_vol': '9.845238095238095'}], 'var_call_FIzriC69nDSmw0dxAYPcnwYm': [{'avg_vol': '254397.62845849802'}], 'var_call_cuHp7G6ILKDjsfL3H2zJffyk': [{'avg_vol': '10.276679841897232'}], 'var_call_yUFwOJfeKXZ5BOgOaaJaac3s': [{'avg_vol': 'nan'}], 'var_call_gYTkLjg7Xb12LMOWaXsmfDm1': [{'avg_vol': 'nan'}], 'var_call_qEr1pHec4jInNs5uNwmaUUBn': [{'avg_vol': 'nan'}], 'var_call_SBUnux9K0YLMgodNFGc7EOAK': [{'avg_vol': '254.1501976284585'}], 'var_call_BHLRtnHndoTfXzxVqMMkgG52': [{'avg_vol': '10706.719367588932'}], 'var_call_osf0TYxgATbt0PxmsTrUQ6BW': [{'avg_vol': 'nan'}], 'var_call_zd0jV3EFLMs5b0Xaqd0UxVBX': [{'avg_vol': '781.8181818181819'}], 'var_call_H3G8JgTooZXHxjVIrEh0RtV4': [{'avg_vol': 'nan'}], 'var_call_gCBiyyz2Z7MDaObvFQJWm0SJ': [{'avg_vol': '36836.36363636364'}], 'var_call_oqa9vlljvIAc8U7ft3iEefqn': [{'avg_vol': 'nan'}]}

exec(code, env_args)
