---
"@context": "ipfs://bafkreifcontext...[Base_Context]"
"@id": "urn:uuid:rule-sbrm-equity-rollforward"
ontological_class: "CalculationRule"
domain_tags: ["SBRM", "EquityStatement"]
gist_equivalent: "gist:Directive"
content_hash: "d5f76da278590d3860f37ee69abc10360251f4f29b370df5671487c972df7623"
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
    sbrm_label: "urn:uuid:def-sbr-total-equity"
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