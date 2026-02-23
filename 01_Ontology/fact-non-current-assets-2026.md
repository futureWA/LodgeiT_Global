---
"@context": "ipfs://bafkreifcontext...[Base_Context]"
"@id": "urn:uuid:fact-non-current-assets-sample-001"
ontological_class: "FinancialFact"
gist_equivalent: "gist:MonetaryAmount"
domain_tags:
  - "SBRM"
  - "BalanceSheet"
execution_parameters: null
parameters_exposed:
  fact_value:
    sbrm_label: "sbrm:FactValue"
  fact_unit:
    sbrm_label: "sbrm:FactUnit"
  fact_decimals:
    sbrm_label: "sbrm:FactDecimals"
  fact_rounding:
    sbrm_label: "sbrm:FactRounding"
fact_value: 75000.00
fact_unit: "AUD"
fact_decimals: 2
fact_rounding: "inf"
edges:
  - rel: "sbrm:hasReportingEntity"
    target: "urn:uuid:def-sbrm-reporting-entity"
  - rel: "sbrm:hasReportingPeriod"
    target: "urn:uuid:def-sbrm-reporting-period"
  - rel: "sbrm:isInstanceOfConcept"
    target: "urn:uuid:def-sbr-non-current-assets"
integrity:
  source_authority: "nostr:pubkey:a1b2c3d4...[LodgeiT_Hex_Pubkey]"
  staleness_flag: false
  source_uri: null
  content_hash: "23dd3c1ffb3df56c7ba668799362ffeba19586f476befe47b11c49c4e708bfd3"
---
# Fact: Non-Current Assets
As of the 2026 reporting period, the entity holds Non-Current Assets valued at $75,000.00 AUD.