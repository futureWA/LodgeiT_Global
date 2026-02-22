---
"@context": "ipfs://bafkreifcontext...[Base_Context]"
"@id": "urn:uuid:wp-bank-statement-sample-001"
ontological_class: "WorkingPaperFact"
domain_tags: ["SBRM", "AuditEvidence", "BankReconciliation"]

fact_value: 50000.00
fact_unit: "AUD"

edges:
  - rel: "sbrm:hasReportingEntity"
    target: "urn:uuid:def-sbrm-reporting-entity"
  - rel: "sbrm:hasReportingPeriod"
    target: "urn:uuid:def-sbrm-reporting-period-2026"
  - rel: "sbrm:isInstanceOfConcept"
    target: "urn:uuid:def-wp-bank-statement-balance" 
  - rel: "prov:wasDerivedFrom"
    target: "ipfs://[CID_of_Scanned_Bank_Statement_PDF]"
---
# Working Paper: Bank Statement Balance
Per the external bank statement provided by the institution, the balance is $50,000.00 AUD.