import os
import re

VAULT_PATH = r"C:\Users\futur\Documents\LodgeiT_Global"

def run_logic_engine(path):
    print("--- LodgeiT SBRM Logic Engine: Execution Audit ---\n")
    
    facts = {}
    rules = []

    # 1. Ingest the Knowledge Graph
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".md"):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    # Extract Metadata
                    node_id = re.search(r'"?@id"?:\s*"?([^"\n]+)"?', content)
                    node_class = re.search(r'"?ontological_class"?:\s*"?([^"\n]+)"?', content)
                    
                    if not node_id or not node_class: continue
                    
                    nid = node_id.group(1).strip()
                    nclass = node_class.group(1).strip()
                    
                    # 2. Extract Fact Values & Target Concepts
                    if nclass == "FinancialFact":
                        val_match = re.search(r'fact_value:\s*([0-9.]+)', content)
                        # Find the specific SBR concept this fact represents
                        concept_match = re.search(r'"?target"?:\s*"?([^"\n]+def-sbr-[^"\n]+)"?', content) 
                        if val_match and concept_match:
                            facts[concept_match.group(1).strip()] = float(val_match.group(1))
                            
                    # 3. Catalog Rules
                    if nclass == "CalculationRule":
                        rules.append(nid)

    # 4. Execute Deterministic Logic
    print(f"Discovered {len(facts)} SBRM Facts.")
    print(f"Discovered {len(rules)} SBRM Rules.\n")
    
    print("EXECUTING RULE: urn:uuid:rule-sbrm-asset-rollup")
    
    # Bind variables based on the parameters_exposed block in your YAML
    total = facts.get("urn:uuid:def-sbr-total-assets")
    current = facts.get("urn:uuid:def-sbr-current-assets")
    non_current = facts.get("urn:uuid:def-sbr-non-current-assets")
    
    print(f"  -> Found Total Assets: {total if total else 'MISSING'}")
    print(f"  -> Found Current Assets: {current if current else 'MISSING'}")
    print(f"  -> Found Non-Current Assets: {non_current if non_current else 'MISSING'}")
    
    print("\n--- Execution Result ---")
    if total is not None and current is not None and non_current is not None:
        if total == (current + non_current):
            print("[PASS] Graph is mathematically consistent. Proof valid.")
        else:
            print(f"[FAIL] Graph contradiction! {total} != {current} + {non_current}")
    else:
        print("[PENDING] Agentic Discovery Triggered: Cannot complete proof. Missing facts in the graph.")
        print("Action Required: The system requires additional Fact Nodes to resolve the equation.")

if __name__ == "__main__":
    if os.path.exists(VAULT_PATH):
        run_logic_engine(VAULT_PATH)
    else:
        print("Path not found. Please check VAULT_PATH.")