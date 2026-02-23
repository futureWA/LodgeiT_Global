---
content_hash: "181d47b873adabf63f91a9a08127b6de9adc47e280f96755489f9fa38321a019"
"@context": "ipfs://bafkreifcontext...[Base_Context]"
"@id": "urn:uuid:rule-sbrm-profit-loss"
ontological_class: "CalculationRule"
gist_equivalent: "gist:Directive"
domain_tags: ["SBRM", "IncomeStatement"]

execution_parameters:
  payload_format: "Hybrid-LE-Prolog"

parameters_exposed: 
  - variable: "Revenue"
    sbrm_label: "urn:uuid:def-sbr-revenue"
  - variable: "Expenses"
    sbrm_label: "urn:uuid:def-sbr-expenses"
  - variable: "ProfitLoss"
    sbrm_label: "urn:uuid:def-sbr-profit-loss"

edges:
  - rel: "gist:appliesTo"
    target: "urn:uuid:def-sbrm-reporting-entity"
---
# SBRM Consistency Rule: Profit & Loss

## Epistemological Definition (Logical English)
```logical-english
the fact set is valid for profit and loss if
    the fact set has a Revenue value
    and the fact set has an Expenses value
    and the fact set has a ProfitLoss value
    and the ProfitLoss value is exactly the Revenue value - the Expenses value.