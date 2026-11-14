---
layout: landing-page
sectionKey: Formatting content
eleventyNavigation:
  parent: Text formatting
title: Legislative list
description: Add complicated bullet point lists to GOV.UH content with Govspeak Markdown code, so you can specify the numbering and include multiple indent levels.
lastUpdated:
---

You must only use this code when copying out legislation that has numbered sections and multiple indent levels.

For any other lists, use [bullet points](/formatting-content/text-formatting/bullets/) or [numbered lists](/formatting-content/text-formatting/numbered-lists/).

```
$LegislativeList
* 1. Item 1
* 2. Item 2
  * a) Item 2a
  * b) Item 2b
    * i. Item 2 b i
    * ii. Item 2 b ii
* 3. Item 3
$EndLegislativeList
```

To indent, add 2 spaces.
