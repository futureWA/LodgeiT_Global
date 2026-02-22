---
"@context": "ipfs://bafkreifcontext...[Base_Context]"
"@id": "urn:uuid:fact-revenue-blue-sample-001"
ontological_class: "FinancialFact"
domain_tags: ["SBRM", "IncomeStatement", "Revenue", "Dimension:Blue"]

fact_value: 25000.00
fact_unit: "AUD"

edges:
  - rel: "sbrm:hasReportingEntity"
    target: "urn:uuid:def-sbrm-reporting-entity"
  - rel: "sbrm:hasReportingPeriod"
    target: "urn:uuid:def-sbrm-reporting-period-2026-duration"
  - rel: "sbrm:isInstanceOfConcept"
    target: "urn:uuid:def-sbr-revenue-blue" 
---
# Fact: Revenue (Blue Dimension)
Revenue attributed to the Blue segment for 2026 is $25,000.00 AUD.