import re

def validate(llm_output: str) -> (bool, str):
    """
    Validate:
    - number 31 is present somewhere in LLM output
    - all gt names are present (case-insensitive)
    """
    ground_truth_names = [
        "ProShares Ultra Bloomberg Natural Gas",
        "ProShares UltraShort MSCI Brazil Capped",
        "Direxion Auspice Broad Commodity Strategy ETF",
        "Direxion Daily Gold Miners Index Bear 2X Shares",
        "Direxion Emerging Markets Bear 3X Shares",
        "Direxion Energy Bull 2X Shares",
        "Direxion Financial Bear 3X Shares",
        "ProShares Ultrashort FTSE China 50",
        "Goldman Sachs Motif Finance Reimagined ETF",
        "Direxion Daily S&P Oil & Gas Exp. & Prod. Bull 2X Shares",
        "Xtrackers High Beta High Yield Bond ETF",
        "Direxion Daily Junior Gold Miners Index Bear 2X Shares",
        "Direxion Daily Junior Gold Miners Index Bull 2X Shares",
        "Xtrackers Japan JPX-Nikkei 400 Equity ETF",
        "Direxion Daily S&P Biotech Bear 3X Shares",
        "Direxion Daily S&P Biotech Bull 3X Shares",
        "Direxion Daily Latin America 3x Bull Shares",
        "SPDR MidCap Trust Series I",
        "Pacer Trendpilot International ETF",
        "Pacer Benchmark Retail Real Estate SCTR ETF",
        "UltraPro Short Dow30",
        "Direxion Daily Semiconductor Bear 3x Shares",
        "ProShares UltraShort Semiconductors",
        "Direxion Technology Bear 3X Shares",
        "Direxion Small Cap Bear 3X Shares",
        "ProShares Trust Ultra VIX Short Term Futures ETF",
        "ProShares Trust VIX Short-Term Futures ETF",
        "Virtus Private Credit Strategy ETF",
        "SPDR Series Trust SPDR S&P Oil & Gas Equipment & Services ETF",
        "SPDR S&P Oil & Gas Explor & Product",
        "Direxion Daily FTSE China Bear 3x Shares",
    ]

    llm_lower = llm_output.lower()

    matches = re.findall(r"\b\d+\b", llm_output)
    if not any(int(m) == 31 for m in matches):
        reason = "Missing number: 31"
        print(f"❌ {reason}")
        return False, reason

    for name in ground_truth_names:
        if name.lower() not in llm_lower:
            reason = f"Missing name: {name}"
            print(f"❌ {reason}")
            return False, reason

    print("✅ Number 31 and all names found.")
    return True, "OK"
