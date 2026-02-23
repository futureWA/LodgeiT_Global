---
"@context": "ipfs://bafkreifcontext...[Base_Context]"
"@id": "urn:uuid:fact-current-liabilities-sample-001"
ontological_class: "FinancialFact"
gist_equivalent: "gist:Fact"
domain_tags: ["SBRM", "BalanceSheet"]
integrity:
  source_uri: null
  content_hash: "8b5ec9aeb30ae82c3e4872ef9ec15fe9f644fcc7d58c1cb0388c5169956a95d5"
parameters_exposed: {}
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