---
"@context": "ipfs://bafkreifcontext...[Base_Context]"
"@id": "urn:uuid:fact-current-liabilities-sample-001"
ontological_class: "FinancialFact"
domain_tags: ["SBRM", "BalanceSheet"]

fact_value: 30000.00
fact_unit: "AUD"

edges:
  - rel: "sbrm:hasReportingEntity"
    target: "urn:uuid:def-sbrm-reporting-entity"
  - rel: "sbrm:hasReportingPeriod"
    target: "urn:uuid:def-sbrm-reporting-period"
  - rel: "sbrm:isInstanceOfConcept"
    target: "urn:uuid:def-sbr-current-liabilities" 
---
# Fact: Current Liabilities
As of 2026, Current Liabilities equal $30,000.00 AUD.