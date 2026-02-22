---
"@context": "ipfs://bafkreifcontext...[Base_Context]"
"@id": "urn:uuid:rule-sbrm-equity-rollforward"
ontological_class: "CalculationRule"
domain_tags: ["SBRM", "EquityStatement"]

execution_parameters:
  payload_format: "Hybrid-LE-Prolog"

parameters_exposed: 
  - variable: "OpeningEquity"
    sbrm_label: "urn:uuid:def-sbr-opening-equity"
  - variable: "ProfitLoss"
    sbrm_label: "urn:uuid:def-sbr-profit-loss"
  - variable: "Dividends"
    sbrm_label: "urn:uuid:def-sbr-dividends-paid"
  - variable: "ClosingEquity"
    sbrm_label: "urn:uuid:def-sbr-total-equity" # Links to your existing 2026 Equity Fact

edges:
  - rel: "gist:appliesTo"
    target: "urn:uuid:def-sbrm-reporting-entity"
---
# SBRM Consistency Rule: Equity Roll-Forward

## Epistemological Definition (Logical English)
```logical-english
the fact set is valid for equity roll-forward if
    the fact set has an OpeningEquity value
    and the fact set has a ProfitLoss value
    and the fact set has a Dividends value
    and the fact set has a ClosingEquity value
    and the ClosingEquity value is exactly the OpeningEquity value + the ProfitLoss value - the Dividends value.