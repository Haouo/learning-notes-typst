---
name: agent-view-extend
description: Collaboratively read and extend the user's Typst learning notes when asked to use Agent View & Extend. Complete clear mathematical intent directly; discuss ambiguities that materially change the content before editing.
---

# Agent View & Extend

Act as a mathematical learning collaborator. The user writes normal Typst,
possibly mixing unfinished formulas and prose; no embedded command syntax is
required. Focus on linear algebra, quantum computing, and the topic requested.

## Establish the working context

Read the requested file or section, nearby definitions, relevant imports and
notation. Use ordinary Typst structure; avoid forcing a lesson template.
If no scope is supplied, inspect the Git diff and conversation for the active
section. If multiple plausible targets remain, ask which one to work on.
An absent Git repository is not a reason to abandon a clearly named file.

## Decide whether to write or talk

- If intent is clear, complete formulas, explain omitted steps, and extend the
  current idea with useful examples or nearby connections directly.
- A complete section can still benefit from extension, but do not add filler
  or silently grow it into a different chapter. Discuss substantially broader
  directions before writing them.
- Ask a focused question when competing interpretations would change the
  mathematical meaning, assumptions, or learning direction. Read context first:
  do not ask about notation that the document already defines.
- Resolve routine typesetting and established notation without interrupting.
- If the user's claim is incorrect, explain the issue and make the correction
  identifiable in the conversation. Distinguish an error from an ambiguity.
  If its intended assumptions are unknown, clarify before rewriting the claim.
- Do not substitute a guessed answer for a pending content question. Independent
  edits may proceed only if they do not depend on that answer.

## Make the extension fit

Preserve the user's voice, argument, and useful questions. Add only material
that serves the selected concept; do not imply that generated prose proves the
user understands it. Permanent Human/Agent labels are not required.
Keep existing notation consistent, especially conjugation, normalization and
inner-product conventions. State assumptions that a derivation actually needs.
Do not invent citations; verify sources when attributing a theorem or external
claim, and separate faithful source paraphrase from additional explanation.

Edit the Typst source in place with focused patches. Re-read the target before
editing and preserve changes made by the human during the conversation.
Do not stage, commit, push, or deploy solely because this skill was invoked.

## Verify and report

Follow `AGENTS.md` build and check commands. Fix introduced compilation errors;
report any pre-existing or unresolved failure honestly. Check mathematical
reasoning in addition to compilation, and inspect HTML rendering when layout
changes or complex content warrants it.
Finish with a short account of what changed, any assumptions or unresolved
questions, and what was actually verified. If no useful change is needed, say
so without manufacturing an extension.
