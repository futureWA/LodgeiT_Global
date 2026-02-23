---
"@context": "ipfs://bafkreifcontext...[Base_Context]"
"@id": "urn:uuid:rule-sbrm-asset-rollup"
ontological_class: "CalculationRule"
gist_equivalent: "gist:Directive"
domain_tags:
  - "SBRM"
  - "OIM"
  - "AccountingEquation"
execution_parameters:
  payload_format: "Hybrid-LE-Prolog"
  execution_context: "Any-Compliant-L402-Prolog-Node"
parameters_exposed:
  - variable: "TotalAssets"
    sbrm_label: "urn:uuid:def-sbr-total-assets"
  - variable: "CurrentAssets"
    sbrm_label: "urn:uuid:def-sbr-current-assets"
  - variable: "NonCurrentAssets"
    sbrm_label: "urn:uuid:def-sbr-non-current-assets"
edges:
  - rel: "gist:appliesTo"
    target: "urn:uuid:def-sbrm-reporting-entity"
  - rel: "gist:appliesTo"
    target: "urn:uuid:def-sbrm-reporting-period"
integrity:
  source_uri: null
  source_authority: "nostr:pubkey:a1b2c3d4...[LodgeiT_Hex_Pubkey]"
  validity_horizon: null
  staleness_flag: false
  content_hash: "b0da331b494c1830cd0bfbe0a25761cea2337713379e4f7bdb4dc83ffc526a48"
economics:
  author_id: "nostr:pubkey:a1b2c3d4...[LodgeiT_Hex_Pubkey]"
  payment_pointer: "$ln.top/lodgeit.com/logic"
  l402_rate: 5
  access_tier: "public_infrastructure"
---

# SBRM Consistency Rule: Asset Roll-Up

## 1. Raw Source Text
According to standard accounting frameworks, Total Assets must equal the sum of Current Assets and Non-Current Assets for any given Reporting Entity within the same Reporting Period.

## 2. Ontological Commentary
This rule acts as a consistency crosscheck. The logic engine uses the `parameters_exposed` block to find the Fact Nodes representing Total Assets, Current Assets, and Non-Current Assets. It binds their `fact_value` properties to the variables below and runs a deterministic evaluation. If the math fails, the entire hypercube state is rejected.

## 3. Epistemological Definition (Logical English)
```logical-english
% Operative Logic: Asset Roll-Up

the fact set is valid for asset rollup if
    the fact set has a reporting entity
    and the fact set has a reporting period
    and the fact set has a TotalAssets value
    and the fact set has a CurrentAssets value
    and the fact set has a NonCurrentAssets value
    and the TotalAssets value is exactly the CurrentAssets value + the NonCurrentAssets value.
```