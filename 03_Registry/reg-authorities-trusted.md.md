---
"@context": "ipfs://bafkreifcontext...[Base_Context]"
"@id": "urn:uuid:registry-authorities-trusted"
ontological_class: "RegistryIndex"
domain_tags: ["SBRM", "System", "Cryptography", "Trust"]

trusted_publishers:
  - id: "urn:uuid:auth-publisher-001"
    cryptographic_uri: "nostr:pubkey:a1b2c3d4e5f6g7h8i9j0"
    human_readable_name: "Open Source SBRM Working Group"
    role: "Core Ontology Maintainer"
  - id: "urn:uuid:auth-publisher-002"
    cryptographic_uri: "nostr:pubkey:x9y8z7w6v5u4t3s2r1q0"
    human_readable_name: "Reporting Entity A"
    role: "Financial Fact Publisher"
---
# Trusted Authority Registry

This registry maps decentralized cryptographic identifiers (such as Nostr public keys or DID documents) to known network participants. Logic engines must reference this index to verify the `source_authority` of incoming Fact Nodes before permitting them to bind to the hypercube.