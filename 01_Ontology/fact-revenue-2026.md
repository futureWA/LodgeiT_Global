---
"@context": "ipfs://bafkreifcontext...[Base_Context]"
"@id": "urn:uuid:fact-revenue-sample-001"
ontological_class: "FinancialFact"
domain_tags: ["SBRM", "IncomeStatement", "Revenue"]

fact_value: 100000.00
fact_unit: "AUD"

edges:
  - rel: "sbrm:hasReportingEntity"
    target: "urn:uuid:def-sbrm-reporting-entity"
  - rel: "sbrm:hasReportingPeriod"
    target: "urn:uuid:def-sbrm-reporting-period-2026-duration"
  - rel: "sbrm:isInstanceOfConcept"
    target: "urn:uuid:def-sbr-revenue" 
---
# Fact: Revenue (2026 Duration)
For the 2026 duration, the entity generated Revenue of $100,000.00 AUD.