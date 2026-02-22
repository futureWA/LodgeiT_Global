---
"@context": "ipfs://bafkreifcontext...[Base_Context]"
"@id": "urn:uuid:registry-namespaces-core"
ontological_class: "RegistryIndex"
domain_tags: ["SBRM", "System", "Namespaces"]

namespaces:
  - prefix: "sbrm"
    uri: "http://www.xbrl.org/wg/sbrm/core#"
    description: "Standard Business Reporting Model core vocabulary"
  - prefix: "gist"
    uri: "https://ontologies.semanticarts.com/gist#"
    description: "Gist minimal upper ontology for enterprise semantic models"
  - prefix: "oim"
    uri: "http://www.xbrl.org/wg/oim/core#"
    description: "Open Information Model vocabulary"
---
# Core Namespace Registry

This registry index explicitly defines the base URIs for all semantic prefixes used within the SBRM hypercube. By maintaining this registry locally, agents can dynamically resolve shorthand prefixes into their full, globally addressable URIs.