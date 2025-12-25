code = """import json
import math

# Previous results
query_result = locals()['var_function-call-8932392574969812428']
stock_info_result = locals()['var_function-call-17930376727204981730'] # This is a dict {"valid_symbols": ..., "symbol_map": ...}
symbol_map = stock_info_result['symbol_map']

# Filter and format
final_list = []
for item in query_result:
    sym = item['Symbol']
    avg_vol = item['AvgVol']
    
    if avg_vol is not None and avg_vol != 'nan':
        # Check if avg_vol is numeric and > 0
        try:
            val = float(avg_vol)
            if val > 0:
                # Get company name
                desc = symbol_map.get(sym, "Unknown")
                # Extract name (heuristic: take text before first period or specifically look for common patterns)
                # Or just use the full name if it's cleaner. The prompt asks for "company names".
                # Looking at descriptions: "Name Inc. specializes..."
                # I'll split by " specializes" or " is " or " provides ".
                
                name = desc
                # Simple extraction:
                # Most descriptions start with the name.
                # "AGM Group Holdings Inc. specializes..." -> "AGM Group Holdings Inc."
                # "Aemetis, Inc is..." -> "Aemetis, Inc"
                # "Frontier Communications Corporation provides..." -> "Frontier Communications Corporation"
                
                split_keywords = [" specializes", " is ", " provides ", " offers ", " harness ", " dedicated ", " based "]
                # "Ocean Power Technologies, Inc. harnesses..." -> handle case-insensitively?
                # "Ocean Power Technologies, Inc. harnesses" -> " harness"
                
                # Let's try to split by the first occurrence of any of these key phrases.
                lower_desc = desc.lower()
                min_idx = len(desc)
                
                # Check for " specializes"
                idx = lower_desc.find(" specializes")
                if idx != -1 and idx < min_idx: min_idx = idx
                
                # Check for " is "
                idx = lower_desc.find(" is ")
                if idx != -1 and idx < min_idx: min_idx = idx

                # Check for " provides "
                idx = lower_desc.find(" provides ")
                if idx != -1 and idx < min_idx: min_idx = idx
                
                # Check for " offers "
                idx = lower_desc.find(" offers ")
                if idx != -1 and idx < min_idx: min_idx = idx
                
                # Check for " harnesses "
                idx = lower_desc.find(" harnesses ")
                if idx != -1 and idx < min_idx: min_idx = idx
                
                # Check for " dedicated "
                idx = lower_desc.find(" dedicated ")
                if idx != -1 and idx < min_idx: min_idx = idx

                if min_idx < len(desc):
                    name = desc[:min_idx].strip()
                    # Remove trailing comma if any
                    if name.endswith(","):
                        name = name[:-1]
                else:
                    # Fallback: take first 5 words or something? Or just the whole string?
                    # Let's try to verify if it ends with Inc/Corp/Ltd/LP/Group
                    pass
                
                final_list.append(f"{name}: {val}")
        except ValueError:
            pass

print("__RESULT__:")
print(json.dumps(final_list))"""

env_args = {'var_function-call-6388901114399056105': [{'Financial Status': 'None'}, {'Financial Status': 'N'}, {'Financial Status': 'D'}, {'Financial Status': 'H'}], 'var_function-call-18210191594220716603': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'}, {'Symbol': 'AMTX', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.'}, {'Symbol': 'CBAT', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.'}, {'Symbol': 'CCCL', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.'}, {'Symbol': 'CORV', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.'}, {'Symbol': 'CPAH', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.'}, {'Symbol': 'DZSI', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.'}, {'Symbol': 'FAMI', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.'}, {'Symbol': 'FTFT', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.'}, {'Symbol': 'FTR', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.'}, {'Symbol': 'IDEX', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.'}, {'Symbol': 'ISDS', 'Company Description': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.'}, {'Symbol': 'MCEP', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.'}, {'Symbol': 'NXTD', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.'}, {'Symbol': 'OPTT', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.'}, {'Symbol': 'PEIX', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.'}, {'Symbol': 'RBZ', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.'}, {'Symbol': 'SES', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.'}, {'Symbol': 'SPI', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.'}, {'Symbol': 'SYPR', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.'}, {'Symbol': 'VTIQW', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.'}], 'var_function-call-1909174541786619686': 'file_storage/function-call-1909174541786619686.json', 'var_function-call-17930376727204981730': {'valid_symbols': ['AGMH', 'AMTX', 'APEX', 'BIOC', 'BKYI', 'CBAT', 'CCCL', 'CORV', 'CPAH', 'DZSI', 'FAMI', 'FTFT', 'FTR', 'IDEX', 'ISDS', 'MCEP', 'NXTD', 'OPTT', 'PEIX', 'RBZ', 'SES', 'SNSS', 'SPI', 'SYPR', 'VTIQW'], 'symbol_map': {'AGMH': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'AMTX': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'APEX': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'BIOC': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'BKYI': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'CBAT': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'CCCL': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'CORV': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'CPAH': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'DZSI': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'FAMI': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'FTFT': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'FTR': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'IDEX': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'ISDS': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'MCEP': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'NXTD': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'OPTT': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'PEIX': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'RBZ': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'SES': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'SNSS': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'SPI': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'SYPR': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'VTIQW': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.'}}, 'var_function-call-8932392574969812428': [{'Symbol': 'AGMH', 'AvgVol': 'nan'}, {'Symbol': 'AMTX', 'AvgVol': 'nan'}, {'Symbol': 'APEX', 'AvgVol': '23781.422924901184'}, {'Symbol': 'BIOC', 'AvgVol': 'nan'}, {'Symbol': 'BKYI', 'AvgVol': '10988.142292490118'}, {'Symbol': 'CBAT', 'AvgVol': '86223.32015810277'}, {'Symbol': 'CCCL', 'AvgVol': '4366.798418972332'}, {'Symbol': 'CORV', 'AvgVol': '145247.8260869565'}, {'Symbol': 'CPAH', 'AvgVol': '375.49407114624506'}, {'Symbol': 'DZSI', 'AvgVol': '15578.656126482214'}, {'Symbol': 'FAMI', 'AvgVol': 'nan'}, {'Symbol': 'FTFT', 'AvgVol': '9.845238095238095'}, {'Symbol': 'FTR', 'AvgVol': '254397.62845849802'}, {'Symbol': 'IDEX', 'AvgVol': '10.276679841897232'}, {'Symbol': 'ISDS', 'AvgVol': 'nan'}, {'Symbol': 'MCEP', 'AvgVol': 'nan'}, {'Symbol': 'NXTD', 'AvgVol': 'nan'}, {'Symbol': 'OPTT', 'AvgVol': '254.1501976284585'}, {'Symbol': 'PEIX', 'AvgVol': '10706.719367588932'}, {'Symbol': 'RBZ', 'AvgVol': 'nan'}, {'Symbol': 'SES', 'AvgVol': '2390.513833992095'}, {'Symbol': 'SNSS', 'AvgVol': '781.8181818181819'}, {'Symbol': 'SPI', 'AvgVol': 'nan'}, {'Symbol': 'SYPR', 'AvgVol': '36836.36363636364'}, {'Symbol': 'VTIQW', 'AvgVol': 'nan'}]}

exec(code, env_args)
