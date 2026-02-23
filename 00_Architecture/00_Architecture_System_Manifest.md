---
@context: "ipfs://bafkreifcontext...[Base_Context]"
@id: "urn:uuid:arch-system-manifest-lodgeit-global"
ontological_class: "SystemManifest"
domain_tags:
  - "SBRM"
  - "Decentralized-Knowledge-Graph"
  - "L402-Monetization"

project_context:
  platform: "LodgeiT & ClientRelay Global Fleet"
  objective: "Index of the decentralized financial rule execution and semantic standardization architecture."

integrity:
  source_uri: "internal://architect/00_architecture/system_manifest"
  content_hash: "PENDING_HASH"
---

# LodgeiT Global Fleet: System Manifest

## 1. Core Paradigm
This repository operates on a strict **"File Over App"** and **Neurosemantic AI** architecture. Financial facts, logical rules, and system registries are completely decoupled from relational databases, existing as cryptographically signed Markdown files with JSON-LD/YAML frontmatter. 

This enables deterministic, zero-hallucination proofs of financial data across a decentralized multidimensional hypercube.

## 2. Directory Structure & Domain Roles

### `00_Architecture/` (The Constitution)
Governs the structural rules, JSON-LD frames, and distribution protocols of the fleet.
* **Key File:** `JSON-LD_Frame.md` (Maps internal taxonomy to Gist and SBRM standards).
* **Key File:** `00_Architecture_Cryptographic_Sovereignty.md` (Defines the SHA-256 node hashing protocol).

### `01_Ontology/` (The State)
The active, machine-readable ledger. Contains the "Ground Truth" financial facts, reporting entities, and periods.
* **Dynamics:** Expanded automatically via the `Uplift_Agent.py`. Peer nodes form the current state of the graph.

### `02_Rules/` (The Logic)
The immutable laws of accounting and reporting. Written as deterministic predicates mapping variables to explicit SBRM labels.
* **Scope:** Covers Fundamental Accounting Equations, Roll-Ups, Fan-Outs, and Profit Verification.

### `03_Registry/` (The Controllers)
Master indexes for namespace resolution and commercial access.
* **Key File:** `reg-access-control.md` (Defines L402 Lightning Network API pricing and Macaroon caveats).

## 3. The Agentic Immune System (Python Fleet)
The vault's integrity and execution are maintained by a suite of automated scripts:

| Agent | Function |
| :--- | :--- |
| **`heal_vault.py`** | Uses Gemini Flash to enforce strict YAML/Dictionary standardization across all nodes. |
| **`sync_signatures.py`** | Surgically hashes node bodies and updates YAML frontmatter without disrupting logic. |
| **`00_Architecture_Integrity_Scanner.py`** | The Gatekeeper. Audits the vault to ensure $N/N$ nodes are cryptographically perfect. |
| **`Uplift_Agent.py`** | Ingests flat ERP data (CSVs) and dynamically mints new, hashed semantic peer nodes. |
| **`logic.py`** | The Universal Inference Engine. Reads the YAML dictionary mappings and executes the deterministic proofs. |
| **`l402_middleware.py`** | The Gateway. intercepts API requests, issues Lightning invoices, verifies Macaroons, and triggers logic. |

---
**Vault Status**: Fleet-Ready
**Monetization**: L402 Lightning Active