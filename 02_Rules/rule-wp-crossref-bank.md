---
"@context": "ipfs://bafkreifcontext...[Base_Context]"
"@id": "urn:uuid:rule-wp-crossref-bank"
ontological_class: "CalculationRule"
domain_tags: ["SBRM", "AuditRule", "CrossReference"]

execution_parameters:
  payload_format: "Hybrid-LE-Prolog"

parameters_exposed: 
  - variable: "LedgerCash"
    sbrm_label: "urn:uuid:def-sbr-cash-at-bank"
  - variable: "StatementCash"
    sbrm_label: "urn:uuid:def-wp-bank-statement-balance"

edges:
  - rel: "gist:appliesTo"
    target: "urn:uuid:def-sbrm-reporting-entity"
---
# SBRM Working Paper Rule: Bank Reconciliation Cross-Reference

## Epistemological Definition (Logical English)
```logical-english
the working paper set is valid for bank cross-reference if
    the fact set has a LedgerCash value
    and the working paper set has a StatementCash value
    and the LedgerCash value is exactly the StatementCash value.