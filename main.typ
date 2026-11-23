// import prelude module
#import "prelude.typ": *

// set document metadata
#set document(title: "Learning Notes", author: "Chun-Hao Chang 張峻豪")

// set template (use mousse-notes)
#show: style // from template "mousse-notes"
#set page("us-letter")
#title-page(
  subtitle: [Notes on Mathematics and \ Quantum Computing],
  primary: [Written by Chun-Hao Chang],
  secondary: [Department of Computer Science and Information Engineering \ National Cheng Kung University],
)

// override the some configs over the template 
#set text(
  lang: "zh",
  region: "TW",
  font: (
    (name: "Inter", covers: "latin-in-cjk"),
    "IBM Plex Sans TC",
  ),
)
#set par(leading: 0.85em)
#show math.equation.where(block: true): it => pad(y: 0.75em, it)

// show outline
#outline()

// Mathematics
#include "notes/analysis-measure.typ"
#include "notes/linear-algebra.typ"
#include "notes/probability.typ"
#include "notes/stat-inference.typ"
#include "notes/convex-opt.typ"
// Quantum Information and Computing
#include "notes/qc/basics.typ"
#include "notes/qc/algorithms.typ"
#include "notes/qc/qml.typ"
