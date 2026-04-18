# BrIO ontology review

## Scope
File reviewed: `BrIO_ontology.ttl`  
Parse status: valid Turtle, parsed successfully with RDFLib  
Size: 236 triples, 43 classes, 12 object properties, 16 datatype properties, 21 named individuals

## Overall assessment
The ontology is syntactically valid and can be parsed without error. There is no immediate RDF syntax problem.  
However, there are several **formal ontology issues**, **modelling issues**, and **naming consistency issues** that should be addressed before publication.

## High-priority issues

### 1. Misspelled object property IRI
- **Line 41**: `brio:preceeds`
- Problem: the local name is misspelled.
- Recommendation: replace it with `dicp:precedes` if you want to reuse the DICP property, or rename it to `brio:precedes` in the next major version.

### 2. Misspelled class IRI
- **Line 210**: `brio:BridgeAttachementInspection`
- Problem: `Attachement` is misspelled; standard spelling is `Attachment`.
- Recommendation: introduce `brio:BridgeAttachmentInspection` in the next major version and deprecate the current IRI.

### 3. Misleading property name and casing
- **Line 90**: `ocqa-reg:requiredby`
- Problems:
  - non-standard camel case (`requiredby` instead of `requiredBy`)
  - semantically unclear wording
- Recommendation: prefer `ocqa-reg:requiredBy` or a more explicit property such as `brio:governedBy` or `brio:definedByRegulation`.

### 4. Accessibility property is formally inconsistent with its own comment
- **Lines 100–103**: `brio:accessibility`
- Problem:
  - range is `xsd:string`
  - current examples use values such as `"complex"`
  - comment says `(true, false)`, which implies boolean semantics
- Recommendation:
  - either change the range to `xsd:boolean` and use boolean values, or
  - keep it qualitative and revise the comment accordingly, or
  - model accessibility as a controlled vocabulary / concept scheme.

### 5. Multiple domain statements on `ocqa:hasDocumentation`
- **Lines 56–59**
- Problem: two `rdfs:domain` axioms mean **intersection semantics** in RDFS/OWL, not union semantics.
  - Current effect: every subject using `ocqa:hasDocumentation` is inferred to be both `ocqa:Evaluation` and `ocqa:Inspection`.
- Recommendation:
  - use an explicit union class, or
  - split the modelling, or
  - keep one broader domain only.

### 6. Missing class assignment for an individual that clearly represents a measure
- **Lines 521–522**: `brio:TrafficSafety01`
- Problem: the individual is only typed as `owl:NamedIndividual`, but not as `brio:TrafficSafetyMeasure`.
- Recommendation: add  
  `brio:TrafficSafety01 rdf:type brio:TrafficSafetyMeasure .`

### 7. Underspecified placeholder individual
- **Lines 525–526**: `brio:2018S3_Damage_669-02`
- Problem: only typed as `owl:NamedIndividual`; no class, no relation, no descriptive role.
- Recommendation:
  - if this is an image, type it as `ocqa:Image`
  - if it is documentation more generally, type it as `brio:Documentation`
  - otherwise remove it until it has a clear modelling role.

## Medium-priority issues

### 8. Missing domain/range axioms for core properties
The following properties currently lack useful formal constraints:
- `ocqa:hasActualCharacteristic`
- `ocqa:hasAssignedCharacteristicValue`
- `ocqa:hasInspCharacteristic`
- `ocqa:hasInspection` (missing domain)
- `brio:hasMaxValue`
- `brio:hasUnit`
- `brio:hasValue`
- `brio:equipmentID` (missing range)
- `brio:equipmentName` (missing range)
- `brio:inspectionFrequency` (missing range)

Recommended modelling:
- `ocqa:hasActualCharacteristic` domain `ocqa:Characteristic`, range `ocqa:ActualCharacteristicValue`
- `ocqa:hasAssignedCharacteristicValue` domain `ocqa:Characteristic`, range `ocqa:AssignedCharacteristicValue`
- `ocqa:hasInspCharacteristic` domain `ocqa:Inspection`, range `ocqa:Characteristic`
- `brio:hasValue` domain `ocqa:ActualCharacteristicValue`, range numeric datatype
- `brio:hasMaxValue` domain `ocqa:AssignedCharacteristicValue`, range numeric datatype
- `brio:hasUnit` domain characteristic-value classes, range `xsd:string` or a unit ontology resource
- `brio:equipmentID` range `xsd:string`
- `brio:equipmentName` range `xsd:string`
- `brio:inspectionFrequency` range `xsd:string` or preferably `xsd:duration`

### 9. `inspectionFrequency` is not machine-actionable
- **Line 165** and inspection-type individuals
- Problem: values such as `"Every 6 years"` and `"When requested"` are easy to read but difficult to query or compare formally.
- Recommendation:
  - for fixed intervals use `xsd:duration` where possible
  - for event-triggered inspections use a dedicated event-based modelling pattern.

### 10. Quantity is represented as one string with embedded unit
- **Lines 183–186** and individual `brio:Insp_Girder_S3_OuterSurface_2018`
- Problem: `"94.15 m"` is not machine-friendly and is inconsistent with the separate `hasValue` / `hasUnit` pattern used elsewhere.
- Recommendation: model quantity using a structured value+unit pattern.

### 11. No `owl:imports` for reused ontologies
- Problem: the ontology reuses `ocqa:` and `dicp:` namespaces, but there is no `owl:imports`.
- Consequence: consumers do not automatically receive the intended external semantics.
- Recommendation: add `owl:imports` when those ontologies are published and stable.

### 12. Metadata still contains manuscript-style footnote markers
- **Lines 18–19**: `Patricia Peralta1`, `Sebastian Seiß2`
- Problem: these look like paper affiliation markers, not ontology metadata values.
- Recommendation: keep plain person names in ontology metadata, and keep footnote numbering only in the manuscript.

### 13. The ontology lacks publication metadata
Recommended additions:
- `dcterms:license`
- `dcterms:issued`
- `dcterms:modified`
- `owl:versionIRI`
- optionally `vann:preferredNamespacePrefix` and `vann:preferredNamespaceUri`

## Low-priority / style issues

### 14. Inconsistent IRI naming style
Examples:
- `Material-basedInspection`
- `Non-destructiveTestingEquipment`
- `Sub-componentInspection`
- `AASHTO-Manual`
- `In-depthInspection`

These IRIs are valid, but the naming style is inconsistent.  
Recommendation: choose one style and use it consistently for future terms.

### 15. Redundant subProperty axioms
- `ocqa:hasAssignedCharacteristicValue rdfs:subPropertyOf owl:topObjectProperty`
- `brio:equipmentName rdfs:subPropertyOf owl:topDataProperty`
- `brio:inspectionScope rdfs:subPropertyOf owl:topDataProperty`

These axioms add no useful semantics and can be removed.

### 16. No multilingual annotations in the original ontology
Before annotation, the ontology had:
- 43 classes without labels/comments
- 12 object properties without labels/comments
- 16 datatype properties without labels/comments
- 21 named individuals without labels/comments

## Suggested disjointness axioms
If intended by the conceptual model, consider adding disjointness for:
- `brio:Material-basedInspection`
- `brio:Sub-componentInspection`
- `brio:SiteInspection`

and possibly for:
- `ocqa:Conformity`
- `ocqa:Nonconformity`

This will improve validation and reasoning.

## Files produced
1. `BrIO_ontology_annotated_bilingual.ttl`  
   Original ontology plus bilingual `rdfs:label` and `rdfs:comment` annotations in English and German.
2. This review report.

## Important note
The annotated ontology file **does not rename IRIs** such as `brio:preceeds` or `brio:BridgeAttachementInspection`, because renaming would be a breaking change for existing instance data.  
Instead, the file adds clear labels and comments, while this report lists the recommended structural corrections.
