---
"@context": "ipfs://bafkreifcontext...[Base_Context]"
"@id": "urn:uuid:fact-non-current-assets-sample-001"
ontological_class: "FinancialFact"
gist_equivalent: "gist:MonetaryAmount"
domain_tags: 
  - "SBRM"
  - "BalanceSheet"

execution_parameters: null

# The Value: $75,000
fact_value: 75000.00
fact_unit: "AUD"
fact_decimals: 2
fact_rounding: "inf"

edges:
  - rel: "sbrm:hasReportingEntity"
    target: "urn:uuid:def-sbrm-reporting-entity"
  - rel: "sbrm:hasReportingPeriod"
    target: "urn:uuid:def-sbrm-reporting-period"
  # This target is what the Logic Engine is actively looking for
  - rel: "sbrm:isInstanceOfConcept"
    target: "urn:uuid:def-sbr-non-current-assets" 

integrity:
  source_authority: "nostr:pubkey:a1b2c3d4...[LodgeiT_Hex_Pubkey]"
  staleness_flag: false
---
# Fact: Non-Current Assets
As of the 2026 reporting period, the entity holds Non-Current Assets valued at $75,000.00 AUD.