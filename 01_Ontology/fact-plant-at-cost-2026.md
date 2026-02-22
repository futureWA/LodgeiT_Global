---
"@context": "ipfs://bafkreifcontext...[Base_Context]"
"@id": "urn:uuid:fact-plant-at-cost-sample-001"
ontological_class: "FinancialFact"
domain_tags: ["SBRM", "FixedAssets", "GrossValue"]

fact_value: 100000.00
fact_unit: "AUD"

edges:
  - rel: "sbrm:hasReportingEntity"
    target: "urn:uuid:def-sbrm-reporting-entity"
  - rel: "sbrm:hasReportingPeriod"
    target: "urn:uuid:def-sbrm-reporting-period-2026"
  - rel: "sbrm:isInstanceOfConcept"
    target: "urn:uuid:def-sbr-plant-at-cost" 
---
# Fact: Plant at Cost
The historical gross cost of Plant & Equipment is $100,000.00 AUD.