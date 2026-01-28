code = """import json, math
# Load stockinfo results
stockinfo = var_call_AG46vughwYLX8zXsJbRiImgz
# Mapping symbols to company descriptions
sym_to_desc = {entry['Symbol']: entry['Company Description'] for entry in stockinfo}

# List of symbols in the same order as the parallel queries
symbols = ["AGMH","AMTX","APEX","BIOC","BKYI","CBAT","CCCL","CORV","CPAH","DZSI","FAMI","FTFT","FTR","IDEX","ISDS","MCEP","NXTD","OPTT","PEIX","RBZ","SES","SNSS","SPI","SYPR","VTIQW"]
# Corresponding result variable names from the parallel call
avg_vars = [
    var_call_QrcOAgUuPNfsSY7jcPFyL6CV,
    var_call_EAoog0HPOamkZ8vOosCqf69y,
    var_call_uQXADmBrJgBFW3XIWOSbHcYg,
    var_call_n6WIF1e9UEqtFRDlh7SzG9VO,
    var_call_deTeVytbmn68UzAGjTSh5kOY,
    var_call_nRxgi60o21QSJVFGAk25vTsi,
    var_call_GkEefair5jL44Ja58EDqzN7c,
    var_call_zm2NB3sVLLDb3PiGB9LaxXrm,
    var_call_o1b8mnUbz3GEnK7kKZegMSAF,
    var_call_UgqntU3KgfXSvebIHgUuHMyk,
    var_call_w6lbwp2POTywTuUf0xUixcIN,
    var_call_KZNHELWVuigP1kKbc2lD9skg,
    var_call_B0a5bdWbofKgXTkpPv6o2mwG,
    var_call_GeqQ1m9DaCI7BYdL1CdrEOsF,
    var_call_Gnxw1tcCX145Rgz02Dgnsa9C,
    var_call_utea5kvVDCFhY47Klt7Noudz,
    var_call_AwUPq1GE0u4NI3HUfkWwZbwO,
    var_call_7D5BRAzlMjCAozZ9wlCdl7WO,
    var_call_R6icsQuu22dW6RxNSZHmscVy,
    var_call_MY7hc6ubtzuDC5uyVhzqdJ4b,
    var_call_RMZ1Xxq03hXazEVC2mfOC4ld,
    var_call_QeE5krkR7T9U3df7i35a2GVw,
    var_call_i6lRx30jjq7g5dVVR1FuPqBV,
    var_call_fxQx50ueF2grty4whNKC3g2Z,
    var_call_69a6AhlyUtCJYoY9EzL0tRIs
]

results = []
for sym, var in zip(symbols, avg_vars):
    # Each var is a list like [{"avg_vol": "..."}]
    try:
        rec = var[0]
        raw = rec.get('avg_vol')
    except Exception:
        raw = None
    avg = None
    if raw is not None:
        try:
            avgf = float(raw)
            if math.isfinite(avgf):
                avg = avgf
        except Exception:
            avg = None
    if avg is not None:
        results.append({
            'Symbol': sym,
            'Company Description': sym_to_desc.get(sym),
            'AvgDailyVolume2008': avg
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_AG46vughwYLX8zXsJbRiImgz': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'AMTX', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'Financial Status': 'D', 'Market Category': 'G', 'Nasdaq Traded': 'Y'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'CBAT', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'CCCL', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'CORV', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'CPAH', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'DZSI', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'FAMI', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'FTFT', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'FTR', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'Financial Status': 'D', 'Market Category': 'Q', 'Nasdaq Traded': 'Y'}, {'Symbol': 'IDEX', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'ISDS', 'Company Description': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'Financial Status': 'D', 'Market Category': 'G', 'Nasdaq Traded': 'Y'}, {'Symbol': 'MCEP', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'NXTD', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'OPTT', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'PEIX', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'RBZ', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'Financial Status': 'D', 'Market Category': 'G', 'Nasdaq Traded': 'Y'}, {'Symbol': 'SES', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'Financial Status': 'H', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}, {'Symbol': 'SPI', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'Financial Status': 'D', 'Market Category': 'Q', 'Nasdaq Traded': 'Y'}, {'Symbol': 'SYPR', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'Financial Status': 'D', 'Market Category': 'G', 'Nasdaq Traded': 'Y'}, {'Symbol': 'VTIQW', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'Financial Status': 'D', 'Market Category': 'S', 'Nasdaq Traded': 'Y'}], 'var_call_I8nO3DGQOTZ5VBBaX4rwNIZq': 'file_storage/call_I8nO3DGQOTZ5VBBaX4rwNIZq.json', 'var_call_eO7wauFWP89Zb7mdzsFAXr3R': {'symbols_requested': ['AGMH', 'AMTX', 'APEX', 'BIOC', 'BKYI', 'CBAT', 'CCCL', 'CORV', 'CPAH', 'DZSI', 'FAMI', 'FTFT', 'FTR', 'IDEX', 'ISDS', 'MCEP', 'NXTD', 'OPTT', 'PEIX', 'RBZ', 'SES', 'SNSS', 'SPI', 'SYPR', 'VTIQW'], 'symbols_existing_in_trade_db': ['AGMH', 'AMTX', 'APEX', 'BIOC', 'BKYI', 'CBAT', 'CCCL', 'CORV', 'CPAH', 'DZSI', 'FAMI', 'FTFT', 'FTR', 'IDEX', 'ISDS', 'MCEP', 'NXTD', 'OPTT', 'PEIX', 'RBZ', 'SES', 'SNSS', 'SPI', 'SYPR', 'VTIQW']}, 'var_call_SaFwJlImmBoA9yEATRP2W6jU': [{'avg_vol': 'nan'}], 'var_call_QrcOAgUuPNfsSY7jcPFyL6CV': [{'avg_vol': 'nan'}], 'var_call_EAoog0HPOamkZ8vOosCqf69y': [{'avg_vol': 'nan'}], 'var_call_uQXADmBrJgBFW3XIWOSbHcYg': [{'avg_vol': '23781.422924901184'}], 'var_call_n6WIF1e9UEqtFRDlh7SzG9VO': [{'avg_vol': 'nan'}], 'var_call_deTeVytbmn68UzAGjTSh5kOY': [{'avg_vol': '10988.142292490118'}], 'var_call_nRxgi60o21QSJVFGAk25vTsi': [{'avg_vol': '86223.32015810277'}], 'var_call_GkEefair5jL44Ja58EDqzN7c': [{'avg_vol': '4366.798418972332'}], 'var_call_zm2NB3sVLLDb3PiGB9LaxXrm': [{'avg_vol': '145247.8260869565'}], 'var_call_o1b8mnUbz3GEnK7kKZegMSAF': [{'avg_vol': '375.49407114624506'}], 'var_call_UgqntU3KgfXSvebIHgUuHMyk': [{'avg_vol': '15578.656126482214'}], 'var_call_w6lbwp2POTywTuUf0xUixcIN': [{'avg_vol': 'nan'}], 'var_call_KZNHELWVuigP1kKbc2lD9skg': [{'avg_vol': '9.845238095238095'}], 'var_call_B0a5bdWbofKgXTkpPv6o2mwG': [{'avg_vol': '254397.62845849802'}], 'var_call_GeqQ1m9DaCI7BYdL1CdrEOsF': [{'avg_vol': '10.276679841897232'}], 'var_call_Gnxw1tcCX145Rgz02Dgnsa9C': [{'avg_vol': 'nan'}], 'var_call_utea5kvVDCFhY47Klt7Noudz': [{'avg_vol': 'nan'}], 'var_call_AwUPq1GE0u4NI3HUfkWwZbwO': [{'avg_vol': 'nan'}], 'var_call_7D5BRAzlMjCAozZ9wlCdl7WO': [{'avg_vol': '254.1501976284585'}], 'var_call_R6icsQuu22dW6RxNSZHmscVy': [{'avg_vol': '10706.719367588932'}], 'var_call_MY7hc6ubtzuDC5uyVhzqdJ4b': [{'avg_vol': 'nan'}], 'var_call_RMZ1Xxq03hXazEVC2mfOC4ld': [{'avg_vol': '2390.513833992095'}], 'var_call_QeE5krkR7T9U3df7i35a2GVw': [{'avg_vol': '781.8181818181819'}], 'var_call_i6lRx30jjq7g5dVVR1FuPqBV': [{'avg_vol': 'nan'}], 'var_call_fxQx50ueF2grty4whNKC3g2Z': [{'avg_vol': '36836.36363636364'}], 'var_call_69a6AhlyUtCJYoY9EzL0tRIs': [{'avg_vol': 'nan'}]}

exec(code, env_args)
