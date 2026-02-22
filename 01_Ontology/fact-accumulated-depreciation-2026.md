---
"@context": "ipfs://bafkreifcontext...[Base_Context]"
"@id": "urn:uuid:fact-accumulated-depreciation-sample-001"
ontological_class: "FinancialFact"
domain_tags: ["SBRM", "FixedAssets", "ContraAsset"]

fact_value: 25000.00
fact_unit: "AUD"

edges:
  - rel: "sbrm:hasReportingEntity"
    target: "urn:uuid:def-sbrm-reporting-entity"
  - rel: "sbrm:hasReportingPeriod"
    target: "urn:uuid:def-sbrm-reporting-period-2026"
  - rel: "sbrm:isInstanceOfConcept"
    target: "urn:uuid:def-sbr-accumulated-depreciation" 
---
# Fact: Accumulated Depreciation
The accumulated depreciation against the Plant & Equipment is $25,000.00 AUD.