import os
import yaml

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
                    
                    # Split YAML from Body
                    parts = content.split('---')
                    if len(parts) < 3: continue
                    
                    try:
                        header = yaml.safe_load(parts[1])
                        if not header: continue
                        
                        nclass = header.get('ontological_class')
                        nid = header.get('@id')

                        # 1. Ingest Facts (Supporting both Financial and Working Paper)
                        if nclass in ["FinancialFact", "WorkingPaperFact"]:
                            val = header.get('fact_value')
                            # Look for the target concept in the edges
                            edges = header.get('edges', [])
                            for edge in edges:
                                if "def-sbr-" in edge.get('target', '') or "def-wp-" in edge.get('target', ''):
                                    facts[edge['target'].strip()] = float(val)

                        # 2. Ingest Rules (Modern Dictionary Handling)
                        if nclass == "CalculationRule":
                            exposed = header.get('parameters_exposed', {})
                            # Reformat into a list for the evaluator
                            params = [(k, v.get('sbrm_label')) for k, v in exposed.items()]
                            rules.append({"id": nid, "params": params})
                            
                    except Exception as e:
                        continue # Skip malformed nodes

    print(f"Discovered {len(facts)} SBRM Facts & Working Papers.")
    print(f"Discovered {len(rules)} SBRM Rules.\n")
    
    # ... (Rest of your evaluation logic remains the same)