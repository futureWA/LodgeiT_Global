import os
import glob
import hashlib
import yaml

TARGET_DIRS = ["./01_Ontology", "./02_Rules", "./03_Registry"]

def sync_file_hash(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    parts = content.split('---')
    if len(parts) < 3: return

    # 1. Re-parse the current state
    header = yaml.safe_load(parts[1])
    body = '---'.join(parts[2:]).strip()
    
    # 2. Generate the "Ground Truth" Hash
    actual_hash = hashlib.sha256(body.encode('utf-8')).hexdigest()
    
    # 3. Update the header dictionary
    if 'integrity' not in header: header['integrity'] = {}
    header['integrity']['content_hash'] = actual_hash

    # 4. Write back to file with standardized YAML formatting
    new_header_yaml = yaml.dump(header, sort_keys=False, allow_unicode=True).strip()
    final_output = f"---\n{new_header_yaml}\n---\n\n{body}"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(final_output)
    print(f"Synced: {filepath}")

if __name__ == "__main__":
    for directory in TARGET_DIRS:
        for filepath in glob.glob(f"{directory}/**/*.md", recursive=True):
            sync_file_hash(filepath)