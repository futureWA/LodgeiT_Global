---
"@context": "ipfs://bafkreifcontext...[Base_Context]"
"@id": "urn:uuid:fact-expenses-sample-001"
ontological_class: "FinancialFact"
domain_tags: ["SBRM", "IncomeStatement", "Expenses"]

fact_value: 80000.00
fact_unit: "AUD"

edges:
  - rel: "sbrm:hasReportingEntity"
    target: "urn:uuid:def-sbrm-reporting-entity"
  - rel: "sbrm:hasReportingPeriod"
    target: "urn:uuid:def-sbrm-reporting-period-2026-duration"
  - rel: "sbrm:isInstanceOfConcept"
    target: "urn:uuid:def-sbr-expenses" 
---
# Fact: Expenses (2026 Duration)
For the 2026 duration, the entity incurred Expenses of $80,000.00 AUD.