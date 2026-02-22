---
"@context": "ipfs://bafkreifcontext...[Base_Context]"
"@id": "urn:uuid:fact-revenue-red-sample-001"
ontological_class: "FinancialFact"
domain_tags: ["SBRM", "IncomeStatement", "Revenue", "Dimension:Red"]

fact_value: 25000.00
fact_unit: "AUD"

edges:
  - rel: "sbrm:hasReportingEntity"
    target: "urn:uuid:def-sbrm-reporting-entity"
  - rel: "sbrm:hasReportingPeriod"
    target: "urn:uuid:def-sbrm-reporting-period-2026-duration"
  - rel: "sbrm:isInstanceOfConcept"
    target: "urn:uuid:def-sbr-revenue-red" 
---
# Fact: Revenue (Red Dimension)
Revenue attributed to the Red segment for 2026 is $25,000.00 AUD.