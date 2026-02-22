---
"@context": "ipfs://bafkreifcontext...[Base_Context]"
"@id": "urn:uuid:fact-dividends-paid-sample-001"
ontological_class: "FinancialFact"
domain_tags: ["SBRM", "Equity", "Distributions"]

fact_value: 5000.00
fact_unit: "AUD"

edges:
  - rel: "sbrm:hasReportingEntity"
    target: "urn:uuid:def-sbrm-reporting-entity"
  - rel: "sbrm:hasReportingPeriod"
    target: "urn:uuid:def-sbrm-reporting-period-2026-duration"
  - rel: "sbrm:isInstanceOfConcept"
    target: "urn:uuid:def-sbr-dividends-paid" 
---
# Fact: Dividends Paid (2026 Duration)
During the 2026 period, the entity paid dividends of $5,000.00 AUD.