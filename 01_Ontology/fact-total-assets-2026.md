---
# 1. Epistemic Identity (Keys over Domains)
"@context": "ipfs://bafkreifcontext...[Base_Context]"
"@id": "urn:uuid:fact-total-assets-sample-001"
ontological_class: "FinancialFact"
gist_equivalent: "gist:MonetaryAmount"
domain_tags: 
  - "SBRM"
  - "OIM"
  - "BalanceSheet"
parameters_exposed: {}

# 2. Polymorphic Execution Interface (Rule 2)
# Since this is a Data Node, execution parameters are null.
execution_parameters: null

# 3. Deterministic SBRM Bridge (Rule 3 - The Fact Values)
# This is the "Data Payload" for the Logic Engine.
fact_value: 125000.00
fact_unit: "AUD"
fact_decimals: 2
fact_rounding: "inf"

# 4. Explicit Edges (Rule 6 - The Hypercube Intersection)
edges:
  - rel: "sbrm:hasReportingEntity"
    target: "urn:uuid:def-sbrm-reporting-entity"
  - rel: "sbrm:hasReportingPeriod"
    target: "urn:uuid:def-sbrm-reporting-period"
  - rel: "sbrm:isInstanceOfConcept"
    target: "urn:uuid:def-sbr-total-assets" # Assumes a Concept node exists

# 5. Cryptographic Agentic Healing (Rule 5)
integrity:
  content_hash: "fc3ec8ee977a84f63062cd47f044877c5c31c2937407a3aeb5dc8877f72abe23"
  source_authority: "nostr:pubkey:a1b2c3d4...[LodgeiT_Hex_Pubkey]"
  validity_horizon: "2027-10-31" # Aligns with your Hillarys property strategy
  staleness_flag: false
  source_uri: null

# 6. L402 Economic Layer (Rule 7)
economics:
  author_id: "nostr:pubkey:a1b2c3d4...[LodgeiT_Hex_Pubkey]"
  payment_pointer: null
  l402_rate: 0
  access_tier: "private_ledger"
---

# Fact: Total Assets (Sample)

## 1. Raw Source Text
As of the 2026 reporting period, the entity holds Total Assets valued at **$125,000.00 AUD**.

## 2. Ontological Commentary
This node represents a single point in the SBRM hypercube. It is not a rule; it is an assertion of reality. By linking to both the Entity and Period nodes, it inherits the context required for high-speed AI reasoning. If the Entity's legal status changes or the Period is redefined, this fact node remains cryptographically tied to its original context, preventing "context drift" in your accounting records.

## 3. Epistemological Definition (Logical English)
```logical-english
the fact 001 asserts that 
    the reporting entity has total assets of 125000.00 AUD
    at the reporting period 2026.
```