code = """import json
import pandas as pd

# Load stockinfo result
stockinfo_res = locals()['var_function-call-1009607585021740635']
# Load trade result
trade_res = locals()['var_function-call-224386476385062048']

df_info = pd.DataFrame(stockinfo_res)
df_trade = pd.DataFrame(trade_res)

# Convert AvgVolume to numeric, coercing errors (nan)
df_trade['AvgVolume'] = pd.to_numeric(df_trade['AvgVolume'], errors='coerce')

# Filter non-null and > 0 (though volume usually >=0)
df_trade = df_trade[df_trade['AvgVolume'].notna()]

# Merge
merged = pd.merge(df_trade, df_info, on='Symbol')

# Select relevant columns
result = merged[['Company Description', 'AvgVolume']]

# Format output
output_list = []
for index, row in result.iterrows():
    # Extract just the name if possible, or use the whole description. 
    # Usually the description starts with the name. 
    # "AGM Group Holdings Inc. specializes in..." -> "AGM Group Holdings Inc."
    # A simple heuristic might be to take the string up to the first " specializes" or " is a" or similar, 
    # but the prompt asks for "company names". I'll try to keep it clean but maybe just return the description if not sure.
    # Looking at the previous output:
    # "AGM Group Holdings Inc. specializes..."
    # "Aemetis, Inc is an..."
    # "Apex Global Brands Inc. specializes..."
    # "Biocept, Inc. specializes..."
    # "BIO-key International, Inc. specializes..."
    # "CBAK Energy Technology, Inc. specializes..."
    # "China Ceramics Co., Ltd. specializes..."
    # "Correvio Pharma Corp., based in Canada, specializes..."
    # "CounterPath Corporation specializes..."
    # "DASAN Zhone Solutions, Inc. specializes..."
    # "Future FinTech Group Inc. specializes..."
    # "Frontier Communications Corporation provides..."
    # "Ideanomics, Inc. is at the forefront..."
    # "NXT-ID Inc. specializes..." (Wait, NXTD was nan)
    # "Ocean Power Technologies, Inc. harnesses..."
    # "Pacific Ethanol, Inc. specializes..."
    # "Synthesis Energy Systems, Inc. specializes..."
    # "Sunesis Pharmaceuticals, Inc. is dedicated..."
    # "Sypris Solutions, Inc. specializes..."
    
    # I will split by " specializes", " is ", " provides ", " harnesses ", " based in ", " offers ".
    # Or simpler: The user asked for company names. The field is "Company Description". 
    # I'll just print "Company: <Description> (Avg Volume: <Vol>)" or similar. 
    # Actually, the user says "List all company names ... report its exisiting ... volume".
    # I will provide the full Company Description string to be safe, or try to truncate slightly for readability if it's very long.
    # But usually, extracting the name is better.
    # Let's try to extract the name.
    
    desc = row['Company Description']
    avg_vol = row['AvgVolume']
    
    # Simple extraction attempt
    # Split by " specializes", " is ", " provides ", " harnesses ", " offers ", " dedicated ".
    separators = [" specializes", " is ", " provides ", " harnesses ", " offers ", " dedicated ", ", based in"]
    name = desc
    for sep in separators:
        if sep in name:
            name = name.split(sep)[0]
            # Keep the shortest split? No, usually the first match is the main verb/clause.
            # But "Biocept, Inc. specializes..." -> "Biocept, Inc."
            # "Ideanomics, Inc. is at..." -> "Ideanomics, Inc."
            # "Frontier ... provides..." -> "Frontier ..."
            # "Correvio ... based in..." -> "Correvio ..."
            # So taking the first occurrence of ANY separator seems okay.
            # But we need the earliest one in the string.
            
    # Better logic: find the minimum index of any separator
    min_idx = len(desc)
    found = False
    for sep in separators:
        idx = desc.find(sep)
        if idx != -1 and idx < min_idx:
            min_idx = idx
            found = True
    
    if found:
        name = desc[:min_idx]
        
    output_list.append(f"{name}: {avg_vol:.2f}")

print("__RESULT__:")
print(json.dumps(output_list))"""

env_args = {'var_function-call-1009607585021740635': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Listing Exchange': 'Q', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'AMTX', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'Listing Exchange': 'Q', 'Market Category': 'G', 'Financial Status': 'D'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'Listing Exchange': 'Q', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'Listing Exchange': 'Q', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'Listing Exchange': 'Q', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'CBAT', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'Listing Exchange': 'Q', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'CCCL', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'Listing Exchange': 'Q', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'CORV', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'Listing Exchange': 'Q', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'CPAH', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'Listing Exchange': 'Q', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'DZSI', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'Listing Exchange': 'Q', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'FAMI', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'Listing Exchange': 'Q', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'FTFT', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'Listing Exchange': 'Q', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'FTR', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'Listing Exchange': 'Q', 'Market Category': 'Q', 'Financial Status': 'D'}, {'Symbol': 'IDEX', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'Listing Exchange': 'Q', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'ISDS', 'Company Description': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'Listing Exchange': 'Q', 'Market Category': 'G', 'Financial Status': 'D'}, {'Symbol': 'MCEP', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'Listing Exchange': 'Q', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'NXTD', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'Listing Exchange': 'Q', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'OPTT', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'Listing Exchange': 'Q', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'PEIX', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'Listing Exchange': 'Q', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'RBZ', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'Listing Exchange': 'Q', 'Market Category': 'G', 'Financial Status': 'D'}, {'Symbol': 'SES', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'Listing Exchange': 'Q', 'Market Category': 'S', 'Financial Status': 'H'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'Listing Exchange': 'Q', 'Market Category': 'S', 'Financial Status': 'D'}, {'Symbol': 'SPI', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'Listing Exchange': 'Q', 'Market Category': 'Q', 'Financial Status': 'D'}, {'Symbol': 'SYPR', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'Listing Exchange': 'Q', 'Market Category': 'G', 'Financial Status': 'D'}, {'Symbol': 'VTIQW', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'Listing Exchange': 'Q', 'Market Category': 'S', 'Financial Status': 'D'}], 'var_function-call-13970355437470074199': 'file_storage/function-call-13970355437470074199.json', 'var_function-call-10984724608302767825': "SELECT 'AGMH' as Symbol, AVG(Volume) as AvgVolume FROM AGMH WHERE Date LIKE '2008-%' UNION ALL SELECT 'AMTX' as Symbol, AVG(Volume) as AvgVolume FROM AMTX WHERE Date LIKE '2008-%' UNION ALL SELECT 'APEX' as Symbol, AVG(Volume) as AvgVolume FROM APEX WHERE Date LIKE '2008-%' UNION ALL SELECT 'BIOC' as Symbol, AVG(Volume) as AvgVolume FROM BIOC WHERE Date LIKE '2008-%' UNION ALL SELECT 'BKYI' as Symbol, AVG(Volume) as AvgVolume FROM BKYI WHERE Date LIKE '2008-%' UNION ALL SELECT 'CBAT' as Symbol, AVG(Volume) as AvgVolume FROM CBAT WHERE Date LIKE '2008-%' UNION ALL SELECT 'CCCL' as Symbol, AVG(Volume) as AvgVolume FROM CCCL WHERE Date LIKE '2008-%' UNION ALL SELECT 'CORV' as Symbol, AVG(Volume) as AvgVolume FROM CORV WHERE Date LIKE '2008-%' UNION ALL SELECT 'CPAH' as Symbol, AVG(Volume) as AvgVolume FROM CPAH WHERE Date LIKE '2008-%' UNION ALL SELECT 'DZSI' as Symbol, AVG(Volume) as AvgVolume FROM DZSI WHERE Date LIKE '2008-%' UNION ALL SELECT 'FAMI' as Symbol, AVG(Volume) as AvgVolume FROM FAMI WHERE Date LIKE '2008-%' UNION ALL SELECT 'FTFT' as Symbol, AVG(Volume) as AvgVolume FROM FTFT WHERE Date LIKE '2008-%' UNION ALL SELECT 'FTR' as Symbol, AVG(Volume) as AvgVolume FROM FTR WHERE Date LIKE '2008-%' UNION ALL SELECT 'IDEX' as Symbol, AVG(Volume) as AvgVolume FROM IDEX WHERE Date LIKE '2008-%' UNION ALL SELECT 'ISDS' as Symbol, AVG(Volume) as AvgVolume FROM ISDS WHERE Date LIKE '2008-%' UNION ALL SELECT 'MCEP' as Symbol, AVG(Volume) as AvgVolume FROM MCEP WHERE Date LIKE '2008-%' UNION ALL SELECT 'NXTD' as Symbol, AVG(Volume) as AvgVolume FROM NXTD WHERE Date LIKE '2008-%' UNION ALL SELECT 'OPTT' as Symbol, AVG(Volume) as AvgVolume FROM OPTT WHERE Date LIKE '2008-%' UNION ALL SELECT 'PEIX' as Symbol, AVG(Volume) as AvgVolume FROM PEIX WHERE Date LIKE '2008-%' UNION ALL SELECT 'RBZ' as Symbol, AVG(Volume) as AvgVolume FROM RBZ WHERE Date LIKE '2008-%' UNION ALL SELECT 'SES' as Symbol, AVG(Volume) as AvgVolume FROM SES WHERE Date LIKE '2008-%' UNION ALL SELECT 'SNSS' as Symbol, AVG(Volume) as AvgVolume FROM SNSS WHERE Date LIKE '2008-%' UNION ALL SELECT 'SPI' as Symbol, AVG(Volume) as AvgVolume FROM SPI WHERE Date LIKE '2008-%' UNION ALL SELECT 'SYPR' as Symbol, AVG(Volume) as AvgVolume FROM SYPR WHERE Date LIKE '2008-%' UNION ALL SELECT 'VTIQW' as Symbol, AVG(Volume) as AvgVolume FROM VTIQW WHERE Date LIKE '2008-%'", 'var_function-call-224386476385062048': [{'Symbol': 'AGMH', 'AvgVolume': 'nan'}, {'Symbol': 'AMTX', 'AvgVolume': 'nan'}, {'Symbol': 'APEX', 'AvgVolume': '23781.422924901184'}, {'Symbol': 'BIOC', 'AvgVolume': 'nan'}, {'Symbol': 'BKYI', 'AvgVolume': '10988.142292490118'}, {'Symbol': 'CBAT', 'AvgVolume': '86223.32015810277'}, {'Symbol': 'CCCL', 'AvgVolume': '4366.798418972332'}, {'Symbol': 'CORV', 'AvgVolume': '145247.8260869565'}, {'Symbol': 'CPAH', 'AvgVolume': '375.49407114624506'}, {'Symbol': 'DZSI', 'AvgVolume': '15578.656126482214'}, {'Symbol': 'FAMI', 'AvgVolume': 'nan'}, {'Symbol': 'FTFT', 'AvgVolume': '9.845238095238095'}, {'Symbol': 'FTR', 'AvgVolume': '254397.62845849802'}, {'Symbol': 'IDEX', 'AvgVolume': '10.276679841897232'}, {'Symbol': 'ISDS', 'AvgVolume': 'nan'}, {'Symbol': 'MCEP', 'AvgVolume': 'nan'}, {'Symbol': 'NXTD', 'AvgVolume': 'nan'}, {'Symbol': 'OPTT', 'AvgVolume': '254.1501976284585'}, {'Symbol': 'PEIX', 'AvgVolume': '10706.719367588932'}, {'Symbol': 'RBZ', 'AvgVolume': 'nan'}, {'Symbol': 'SES', 'AvgVolume': '2390.513833992095'}, {'Symbol': 'SNSS', 'AvgVolume': '781.8181818181819'}, {'Symbol': 'SPI', 'AvgVolume': 'nan'}, {'Symbol': 'SYPR', 'AvgVolume': '36836.36363636364'}, {'Symbol': 'VTIQW', 'AvgVolume': 'nan'}]}

exec(code, env_args)
