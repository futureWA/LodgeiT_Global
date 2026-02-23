import os
import glob
import hashlib
import time
import google.generativeai as genai

# Configure the Gemini API client
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# Use the Gemini 2.0 Flash model for fast, high-context extraction
model = genai.GenerativeModel('gemini-2.5-flash')

TARGET_DIRS = ["./01_Ontology", "./02_Rules", "./03_Registry"]

SYSTEM_INSTRUCTION = """
You are an Ontological Extraction and Serialization Agent for a Global Notes architecture.
I am providing you with a raw Markdown file representing a node in an SBRM multidimensional hypercube. 
Inside 'parameters_exposed', you MUST use a dictionary format { variable_name: { sbrm_label: label_value } }. DO NOT use bulleted lists or arrays.

YOUR MISSION: Repair and standardize the YAML frontmatter. If fields are 'Empty' or 'null', you MUST initialize them into valid YAML dictionary structures so they are machine-parsable.

STRICT RULES:
1. **Structural Initialization**: If 'integrity' or 'parameters_exposed' are empty, initialize them.
   - 'integrity' MUST contain 'source_uri' and 'content_hash: "[INJECT_HASH_HERE]"'.
   - 'parameters_exposed' MUST be a dictionary '{}' or contain variables with 'sbrm_label'.
2. **Polymorphic Nullification**: For epistemic nodes (Definitions/Registry), set 'payload_format', 'execution_context', and 'shacl_shape_ref' inside 'execution_parameters' to 'null'.
3. **Gist Enforcement**: Ensure 'gist_equivalent' maps to a Gist Upper Ontology term (e.g., gist:Directive, gist:Category, gist:Event).
4. **No Wrappers**: Output ONLY the raw Markdown text. Do not use ```markdown backticks.

Do NOT alter the body, Prolog code, or logical edges.
"""

def calculate_body_hash(markdown_content):
    """Calculates SHA-256 of the body to ensure cryptographic integrity."""
    parts = markdown_content.split('---')
    if len(parts) >= 3:
        body = '---'.join(parts[2:]).strip()
        return hashlib.sha256(body.encode('utf-8')).hexdigest()
    return None

def heal_markdown_file(filepath):
    print(f"Healing: {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        original_content = f.read()

    prompt = f"{SYSTEM_INSTRUCTION}\n\nFILE_CONTENT:\n{original_content}"

    try:
        response = model.generate_content(prompt)
        healed_content = response.text.strip()
        
        # Clean potential model formatting artifacts
        if healed_content.startswith("```"):
            healed_content = "\n".join(healed_content.split("\n")[1:-1]) if "```" in healed_content else healed_content

        new_hash = calculate_body_hash(healed_content)
        if not new_hash:
            print(f"  [X] Hash failure on {filepath}.")
            return False

        # Inject the real hash into the standardized structure
        final_content = healed_content.replace("[INJECT_HASH_HERE]", new_hash)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(final_content)
            
        print(f"  [v] Integral and Socketed.")
        return True

    except Exception as e:
        print(f"  [X] Error on {filepath}: {e}")
        return False

def run_vault_crawler():
    print("Initiating Global Fleet Semantic Repair Sequence...")
    print("-" * 50)
    
    for directory in TARGET_DIRS:
        if not os.path.exists(directory): continue
        for filepath in glob.glob(f"{directory}/**/*.md", recursive=True):
            heal_markdown_file(filepath)
            time.sleep(1) # Flash is fast; minimal delay needed

if __name__ == "__main__":
    run_vault_crawler()