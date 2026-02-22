---
"@context": "ipfs://bafkreifcontext...[Base_Context]"
"@id": "urn:uuid:fact-opening-equity-sample-001"
ontological_class: "FinancialFact"
domain_tags: ["SBRM", "Equity", "RollForward"]

fact_value: 30000.00
fact_unit: "AUD"

edges:
  - rel: "sbrm:hasReportingEntity"
    target: "urn:uuid:def-sbrm-reporting-entity"
  - rel: "sbrm:hasReportingPeriod"
    target: "urn:uuid:def-sbrm-reporting-period-2025" # Points to previous year
  - rel: "sbrm:isInstanceOfConcept"
    target: "urn:uuid:def-sbr-opening-equity" 
---
# Fact: Opening Equity (2025)
As of the 2025 reporting period, the entity held Opening Equity valued at $30,000.00 AUD.