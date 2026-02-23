```yaml
---
"@context": "ipfs://bafkreifcontext...[Base_Context]"
"@id": "urn:uuid:rule-sbrm-fixed-assets-net"
ontological_class: "CalculationRule"
gist_equivalent: "gist:Directive"
domain_tags: ["SBRM", "FixedAssets", "NetBookValue"]
content_hash: "febb658e2319b2d1fa9c4e7a3a39f06bb526f69fa7df860e78ede0c6e006773e"
execution_parameters:
  payload_format: "Hybrid-LE-Prolog"
  execution_context: null
  shacl_shape_ref: null
parameters_exposed:
  - variable: "PlantAtCost"
    sbrm_label: "urn:uuid:def-sbr-plant-at-cost"
  - variable: "AccumulatedDep"
    sbrm_label: "urn:uuid:def-sbr-accumulated-depreciation"
  - variable: "NonCurrentAssets"
    sbrm_label: "urn:uuid:def-sbr-non-current-assets" # Links to your existing Balance Sheet fact
edges:
  - rel: "gist:appliesTo"
    target: "urn:uuid:def-sbrm-reporting-entity"
---
# SBRM Consistency Rule: Net Fixed Assets

## Epistemological Definition (Logical English)
```logical-english
the fact set is valid for net fixed assets if
    the fact set has a PlantAtCost value
    and the fact set has an AccumulatedDep value
    and the fact set has a NonCurrentAssets value
    and the NonCurrentAssets value is exactly the PlantAtCost value - the AccumulatedDep value.