# BrIO migration note for v0.1.1

## Scope

This note accompanies `BrIO_ontology_v0_1_1_cleaned.ttl`.

Version `0.1.1` is a **clean-up release**. It applies non-breaking formal improvements and introduces canonical replacement IRIs for selected spelling and naming issues while keeping the legacy IRIs available for backward compatibility.

## What changed in v0.1.1

### Metadata
- ontology version updated to `0.1.1`
- added `owl:versionIRI <https://w3id.org/brio/0.1.1>`
- added `dcterms:editor` entries for:
  - Patricia Peralta
  - Sebastian Seiß
  - Yuan Zheng
- added preferred namespace metadata for `https://w3id.org/brio#`

### Annotations
- added or retained meaningful `rdfs:label` and `rdfs:comment` annotations in **English** and **German**
- covered ontology metadata, classes, object properties, datatype properties, and example individuals
- added explicit deprecation annotations for legacy misspelled IRIs

### Formal non-breaking fixes
- replaced the incorrect multiple-domain pattern on `ocqa:hasDocumentation` with an explicit `owl:unionOf (ocqa:Evaluation ocqa:Inspection)` domain
- added domain/range axioms for:
  - `ocqa:hasActualCharacteristic`
  - `ocqa:hasAssignedCharacteristicValue`
  - `ocqa:hasInspCharacteristic`
  - `brio:hasMaxValue`
  - `brio:hasUnit`
  - `brio:hasValue`
  - `brio:equipmentID`
  - `brio:equipmentName`
  - `brio:inspectionFrequency`
- removed redundant `rdfs:subPropertyOf owl:topObjectProperty` and `rdfs:subPropertyOf owl:topDataProperty` assertions
- corrected the semantic description of `brio:accessibility` so that it matches the current qualitative string-based modelling
- added `brio:TrafficSafetyMeasure` typing for `brio:TrafficSafety01`
- added `ocqa:Image` typing for `brio:2018S3_Damage_669-02`

## Canonical IRIs introduced in v0.1.1

The following canonical IRIs are now available and should be used in **new data**, **new SPARQL queries**, and **new documentation**.

| Legacy IRI | Canonical replacement | Status in v0.1.1 |
|---|---|---|
| `brio:preceeds` | `dicp:precedes` | legacy IRI retained, marked deprecated, linked with `owl:equivalentProperty` |
| `ocqa-reg:requiredby` | `ocqa-reg:requiredBy` | legacy IRI retained, marked deprecated, linked with `owl:equivalentProperty` |
| `brio:BridgeAttachementInspection` | `brio:BridgeAttachmentInspection` | legacy IRI retained, marked deprecated, linked with `owl:equivalentClass` |

## Recommended query and data-writing policy from now on

Use the canonical forms below in all new work:

- `dicp:precedes`
- `ocqa-reg:requiredBy`
- `brio:BridgeAttachmentInspection`

The legacy IRIs remain readable in `v0.1.1`, but they should be treated as deprecated compatibility aliases.

## Breaking IRI changes planned for the next major version

The following changes are recommended for the next major release, for example `v0.2.0`:

1. remove `brio:preceeds`
2. remove `ocqa-reg:requiredby`
3. remove `brio:BridgeAttachementInspection`

At that point, only the canonical IRIs should remain.

## Migration guidance for instance data

### 1. Property migration
Replace all triples of the form:

```turtle
?s brio:preceeds ?o .
```

with:

```turtle
?s dicp:precedes ?o .
```

Replace all triples of the form:

```turtle
?s ocqa-reg:requiredby ?o .
```

with:

```turtle
?s ocqa-reg:requiredBy ?o .
```

### 2. Class migration
Replace all class assertions of the form:

```turtle
?x rdf:type brio:BridgeAttachementInspection .
```

with:

```turtle
?x rdf:type brio:BridgeAttachmentInspection .
```

## SPARQL UPDATE snippets

### Replace `brio:preceeds`
```sparql
PREFIX brio: <https://w3id.org/brio#>
PREFIX dicp: <https://w3id.org/digitalconstruction/0.5/Processes#>

DELETE { ?s brio:preceeds ?o }
INSERT { ?s dicp:precedes ?o }
WHERE  { ?s brio:preceeds ?o } ;
```

### Replace `ocqa-reg:requiredby`
```sparql
PREFIX ocqa-reg: <https://w3id.org/ocqa/regulation#>

DELETE { ?s ocqa-reg:requiredby ?o }
INSERT { ?s ocqa-reg:requiredBy ?o }
WHERE  { ?s ocqa-reg:requiredby ?o } ;
```

### Replace `brio:BridgeAttachementInspection`
```sparql
PREFIX brio: <https://w3id.org/brio#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

DELETE { ?x rdf:type brio:BridgeAttachementInspection }
INSERT { ?x rdf:type brio:BridgeAttachmentInspection }
WHERE  { ?x rdf:type brio:BridgeAttachementInspection } ;
```

## Notes for the example case and competency questions

For the recreated example file and the combined competency-question query, the recommended terms are already the canonical ones:

- use `dicp:precedes`
- use `ocqa-reg:requiredBy`
- use `brio:BridgeAttachmentInspection` if that class is needed

This means the next reconstruction of the example should directly target the cleaned namespace policy and will not need an additional spelling-correction pass.
