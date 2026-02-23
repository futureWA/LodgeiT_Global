---
@context: "ipfs://bafkreifcontext...[Base_Context]"
@id: "urn:uuid:arch-distribution-protocol-lodgeit-global"
ontological_class: "DistributionDirective"
gist_equivalent: "gist:CommunicationProtocol"
domain_tags:
  - "IPFS"
  - "Decentralized-Web"
  - "Knowledge-Graph"
  - "L402"

project_context:
  platform: "LodgeiT Global Fleet"
  methodology: "Seattle Method, SBRM, OIM"
  objective: "Immutable, content-addressed distribution of financial logic"

integrity:
  source_uri: "internal://architect/00_architecture/distribution_protocol"
  content_hash: "[INJECT_HASH_HERE]"
---

# 00_Architecture: Distribution Protocol

## 1. Decentralized Storage (IPFS/Content-Addressing)
To ensure **File Over App** sovereignty, all nodes are published to the **InterPlanetary File System (IPFS)**. This transforms your local Markdown files into "Knowledge Assets" uniquely resolvable via **Content Identifiers (CIDs)**.

* **Content-Addressability**: Every node's URI is its SHA-256 `content_hash`. If a byte in the financial fact changes, the URI changes, preventing silent data drift.
* **Portable Bundles**: Nodes are packaged into **CAR (Content Addressable aRchives)** for seamless transfer between the LodgeiT Fleet and individual user vaults.

## 2. Semantic Synchronization (The Seattle Method)
The fleet follows the **Seattle Method** to maintain a "provably high quality" knowledge graph.
* **Guardrails**: All distributed nodes must validate against the **Standard Business Report Model (SBRM)** logical conceptualization before being broadcast to the network.
* **Semantic Unification**: Diverse components (Prolog engines, AI agents, ERP extractors) exchange and interpret information via shared semantic representation, ensuring identical facts yield identical conclusions regardless of the local environment.

## 3. Access & Monetization (L402 Protocol)
Distribution is governed by the **L402 protocol** (formerly LSAT) to facilitate "Logic-as-a-Service".
* **Micro-metering**: External consumers pay for logic execution (e.g., a "Profit & Loss" proof) via Lightning Network micropayments.
* **Macaroon-based Auth**: Decentralized authorization tokens allow for tiered access without a central authority.


## 4. Distribution Workflow
1. **Minting**: Local `uplift_agent.py` generates Fact Nodes.
2. **Hashing**: `sync_signatures.py` locks the cryptographic identity.
3. **Pinning**: Node is broadcast to the LodgeiT IPFS Cluster.
4. **Indexing**: The `urn:uuid` is registered in the Global Registry for discovery.

---
**Status**: Ready for Fleet Broadcast
**Last Verified**: 33/33 Nodes Socketed