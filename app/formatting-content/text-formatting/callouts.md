---
layout: landing-page
sectionKey: Formatting content
eleventyNavigation:
  parent: Text formatting
title: Callouts
description: Add information, example and warning callouts, as well as call to actions for next steps.
lastUpdated:
redirect_from: /formatting-content/text-formatting/calls-to-action
---

Callouts can be used to highlight content on a page and draw attention to it.

There are a few different types of callout, depending on what you want to highlight.

## Information

Use information callouts for specific sentences that you want users to notice or that do not fit into the flow of content.

To create an information callout, add the sentences to a new line and put ^ before and after. For example:

```
^This is an information callout.^
```

Looks like this:

^This is an information callout.^

## Examples

Use example callouts when you’re giving users an example about how to perform a task.

To create an example callout, use $E above and below the example. For example:

```  
$E
Example
This is an example callout.
$E
```

Looks like this:

$E
Example
This is an example callout.
$E

## Warnings

Use warning callouts to alert users to serious consequences, such as a fine or criminal proceedings. Use them sparingly.

To create a warning callout, add the warning to a new line and put % before and after. For example:

```
%This is a warning callout.%
```

Looks like this:

%This is a warning callout.%

## Calls to action

Use a call to action for short links to tasks that a user can do next. For example, a link to a licence application service. They create a tinted box which highlights the task.

To create the call to action box, use $CTA above and below the link. For example:

```  
$CTA 
You can [read the content and publishing guidance](https://guidance.publishing.service.gov.uhrblx.com/).
$CTA 
``` 
