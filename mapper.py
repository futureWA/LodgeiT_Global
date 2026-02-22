import os
import re

VAULT_PATH = r"C:\Users\futur\Documents\LodgeiT_Global"

def run_universal_logic_engine(path):
    print("--- Open-Source SBRM Logic Engine: Universal Execution ---\n")
    facts = {}
    rules = []

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".md"):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    node_id = re.search(r'"?@id"?:\s*"?([^"\n]+)"?', content)
                    node_class = re.search(r'"?ontological_class"?:\s*"?([^"\n]+)"?', content)
                    if not node_id or not node_class: continue
                    
                    nid = node_id.group(1).strip()
                    nclass = node_class.group(1).strip()
                    
                    # UPGRADE 1: Engine now ingests WorkingPaperFacts alongside FinancialFacts
                    if nclass in ["FinancialFact", "WorkingPaperFact"]:
                        val_match = re.search(r'fact_value:\s*([0-9.-]+)', content)
                        # Regex adjusted to catch both def-sbr- and def-wp- concept targets
                        concept_match = re.search(r'"?target"?:\s*"?([^"\n]+(?:def-sbr-|def-wp-)[^"\n]+)"?', content) 
                        if val_match and concept_match:
                            facts[concept_match.group(1).strip()] = float(val_match.group(1))
                            
                    if nclass == "CalculationRule":
                        params = re.findall(r'variable:\s*"?([^"\n]+)"?\s*\n\s*sbrm_label:\s*"?([^"\n]+)"?', content)
                        rules.append({"id": nid, "params": params})

    print(f"Discovered {len(facts)} SBRM Facts & Working Papers.")
    print(f"Discovered {len(rules)} SBRM Rules.\n")
    
    for rule in rules:
        print(f"EXECUTING RULE: {rule['id']}")
        
        rule_vars = {var_name: facts.get(sbrm_urn) for var_name, sbrm_urn in rule['params']}
        
        for name, val in rule_vars.items():
            print(f"  -> Found {name}: {val if val is not None else 'MISSING'}")
            
        print("  --- Result ---")
        
        # Balance Sheet
        if "TotalEquity" in rule_vars and "TotalAssets" in rule_vars and "TotalLiabilities" in rule_vars and None not in rule_vars.values():
            if rule_vars["TotalAssets"] == (rule_vars["TotalLiabilities"] + rule_vars["TotalEquity"]):
                print("  [PASS] Fundamental Accounting Equation balances.\n")
            else:
                print("  [FAIL] Balance Sheet contradiction!\n")

        # Asset Roll-up
        elif "TotalAssets" in rule_vars and "CurrentAssets" in rule_vars and None not in rule_vars.values():
            if rule_vars["TotalAssets"] == (rule_vars["CurrentAssets"] + rule_vars["NonCurrentAssets"]):
                print("  [PASS] Asset Roll-up is mathematically consistent.\n")
            else:
                print("  [FAIL] Asset contradiction!\n")
                
        # Liability Roll-up
        elif "TotalLiabilities" in rule_vars and "CurrentLiabilities" in rule_vars and None not in rule_vars.values():
            if rule_vars["TotalLiabilities"] == (rule_vars["CurrentLiabilities"] + rule_vars["NonCurrentLiabilities"]):
                print("  [PASS] Liability Roll-up is mathematically consistent.\n")
            else:
                print("  [FAIL] Liability contradiction!\n")
                
        # Equity Roll-forward
        elif "OpeningEquity" in rule_vars and "ClosingEquity" in rule_vars and None not in rule_vars.values():
            if rule_vars["ClosingEquity"] == (rule_vars["OpeningEquity"] + rule_vars["ProfitLoss"] - rule_vars["Dividends"]):
                print("  [PASS] Equity Roll-Forward (Time Dimension) is mathematically consistent.\n")
            else:
                print("  [FAIL] Equity Roll-Forward contradiction!\n")
                
        # Dimensional Fan-Out (Revenue)
        elif "TotalRevenue" in rule_vars and "RevRed" in rule_vars and None not in rule_vars.values():
            if rule_vars["TotalRevenue"] == (rule_vars["RevRed"] + rule_vars["RevBlue"] + rule_vars["RevGreen"] + rule_vars["RevYellow"]):
                print("  [PASS] Dimensional Revenue Fan-Out is mathematically consistent.\n")
            else:
                print("  [FAIL] Dimensional contradiction: Parts do not equal the Total!\n")
                
        # Profit & Loss
        elif "Revenue" in rule_vars and "Expenses" in rule_vars and "ProfitLoss" in rule_vars and None not in rule_vars.values():
            if rule_vars["ProfitLoss"] == (rule_vars["Revenue"] - rule_vars["Expenses"]):
                print("  [PASS] Profit & Loss Statement is mathematically consistent.\n")
            else:
                print("  [FAIL] Profit & Loss contradiction!\n")
                
        # UPGRADE 2: Bank Reconciliation Cross-Reference
        elif "LedgerCash" in rule_vars and "StatementCash" in rule_vars and None not in rule_vars.values():
            if rule_vars["LedgerCash"] == rule_vars["StatementCash"]:
                print("  [PASS] Bank Reconciliation Working Paper cross-references correctly.\n")
            else:
                print("  [FAIL] Working Paper contradiction: Ledger does not match Statement!\n")
                
        else:
             print("  [PENDING] Missing facts. Cannot execute proof.\n")

if __name__ == "__main__":
    if os.path.exists(VAULT_PATH):
        run_universal_logic_engine(VAULT_PATH)
    else:
        print("Path not found. Please check VAULT_PATH.")