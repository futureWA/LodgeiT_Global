---
"@context": "ipfs://bafkreifcontext...[Base_Context]"
"@id": "urn:uuid:fact-cash-ledger-sample-001"
ontological_class: "FinancialFact"
domain_tags: ["SBRM", "TrialBalance", "Asset"]

fact_value: 50000.00
fact_unit: "AUD"

edges:
  - rel: "sbrm:hasReportingEntity"
    target: "urn:uuid:def-sbrm-reporting-entity"
  - rel: "sbrm:hasReportingPeriod"
    target: "urn:uuid:def-sbrm-reporting-period-2026"
  - rel: "sbrm:isInstanceOfConcept"
    target: "urn:uuid:def-sbr-cash-at-bank" 
---
# Fact: Cash at Bank (Ledger)
Per the internal trial balance, the Cash at Bank account holds $50,000.00 AUD.