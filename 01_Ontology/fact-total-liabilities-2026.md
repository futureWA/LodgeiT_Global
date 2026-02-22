---
"@context": "ipfs://bafkreifcontext...[Base_Context]"
"@id": "urn:uuid:fact-total-liabilities-sample-001"
ontological_class: "FinancialFact"
gist_equivalent: "gist:MonetaryAmount"
domain_tags: ["SBRM", "BalanceSheet"]

execution_parameters: null

fact_value: 80000.00
fact_unit: "AUD"
fact_decimals: 2
fact_rounding: "inf"

edges:
  - rel: "sbrm:hasReportingEntity"
    target: "urn:uuid:def-sbrm-reporting-entity"
  - rel: "sbrm:hasReportingPeriod"
    target: "urn:uuid:def-sbrm-reporting-period"
  - rel: "sbrm:isInstanceOfConcept"
    target: "urn:uuid:def-sbr-total-liabilities" 

integrity:
  source_authority: "nostr:pubkey:a1b2c3d4...[LodgeiT_Hex_Pubkey]"
  staleness_flag: false
---
# Fact: Total Liabilities
As of the 2026 reporting period, the entity holds Total Liabilities valued at $80,000.00 AUD.