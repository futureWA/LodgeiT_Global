---
"@context": "https://schema.clientrelay.io/v1/context.jsonld"
"@id": "urn:uuid:registry-sbrm-master-ruleset"
ontological_class: "RuleRegistry"
gist_equivalent: "gist:Collection"
domain_tags: 
  - "SBRM"
  - "OperativeLogic"
  - "MasterIndex"

# Polymorphic Nullification Protocol: This is an epistemic index, so execution is null.
execution_parameters: null
parameters_exposed: null

# Graph Integrity via Explicit Edges: This defines the complete set of all rules.
edges:
  - rel: "gist:hasPart"
    target: "urn:uuid:rule-sbrm-accounting-equation"
  - rel: "gist:hasPart"
    target: "urn:uuid:rule-sbrm-asset-rollup"
  - rel: "gist:hasPart"
    target: "urn:uuid:rule-sbrm-equity-rollforward"
  - rel: "gist:hasPart"
    target: "urn:uuid:rule-sbrm-fixed-assets-net"
  - rel: "gist:hasPart"
    target: "urn:uuid:rule-sbrm-liability-rollup"
  - rel: "gist:hasPart"
    target: "urn:uuid:rule-sbrm-profit-loss"
  - rel: "gist:hasPart"
    target: "urn:uuid:rule-sbrm-revenue-fanout"
  - rel: "gist:hasPart"
    target: "urn:uuid:rule-wp-crossref-bank"

integrity:
  source_uri: "internal://clientrelay/registry/master_ruleset"
  content_hash: "[SHA-256]"
  validity_horizon: null
  staleness_flag: false

economics:
  author_id: "System_Architect"
  payment_pointer: null
  l402_rate: 0
  access_tier: "public_infrastructure"
---

# SBRM Master Rule Registry

## Ontological Commentary
This node acts as the definitive index of all operative calculation rules within the Open-Source SBRM hypercube. It does not contain executable payloads itself. Instead, the `edges` array cryptographically links to the atomic Markdown nodes residing in the `02_Rules` directory.

The Python-based universal logic engine must query this node first to retrieve the `@id` targets, subsequently loading only the required sub-graphs into active memory for deterministic execution.