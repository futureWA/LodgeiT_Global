---
"@context": "ipfs://bafkreifcontext...[Base_Context]"
"@id": "urn:uuid:rule-sbrm-liability-rollup"
ontological_class: "CalculationRule"
gist_equivalent: "gist:Directive"
domain_tags: ["SBRM", "AccountingEquation"]
integrity:
  source_uri: null
  content_hash: "9f5eb33835ffaa524f8c9c5466ec255ee2403ae6b3f8d9266894e1374a98ede7"

execution_parameters:
  payload_format: null
  execution_context: null
  shacl_shape_ref: null

parameters_exposed:
  - variable: "TotalLiabilities"
    sbrm_label: "urn:uuid:def-sbr-total-liabilities"
  - variable: "CurrentLiabilities"
    sbrm_label: "urn:uuid:def-sbr-current-liabilities"
  - variable: "NonCurrentLiabilities"
    sbrm_label: "urn:uuid:def-sbr-non-current-liabilities"

edges:
  - rel: "gist:appliesTo"
    target: "urn:uuid:def-sbrm-reporting-entity"
  - rel: "gist:appliesTo"
    target: "urn:uuid:def-sbrm-reporting-period"
---
# SBRM Consistency Rule: Liability Roll-Up

## Epistemological Definition (Logical English)
```logical-english
the fact set is valid for liability rollup if
    the fact set has a TotalLiabilities value
    and the fact set has a CurrentLiabilities value
    and the fact set has a NonCurrentLiabilities value
    and the TotalLiabilities value is exactly the CurrentLiabilities value + the NonCurrentLiabilities value.