---
"@context": "ipfs://bafkreifcontext...[Base_Context]"
"@id": "urn:uuid:fact-profit-loss-sample-001"
ontological_class: "FinancialFact"
domain_tags: ["SBRM", "Equity", "IncomeStatement"]

fact_value: 20000.00
fact_unit: "AUD"

edges:
  - rel: "sbrm:hasReportingEntity"
    target: "urn:uuid:def-sbrm-reporting-entity"
  - rel: "sbrm:hasReportingPeriod"
    target: "urn:uuid:def-sbrm-reporting-period-2026-duration" # Points to the year duration
  - rel: "sbrm:isInstanceOfConcept"
    target: "urn:uuid:def-sbr-profit-loss" 
---
# Fact: Profit & Loss (2026 Duration)
For the 2026 duration, the entity generated a Net Profit of $20,000.00 AUD.