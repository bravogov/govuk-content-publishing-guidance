---
layout: landing-page
sectionKey: Writing to GOV.UK standards
order: 4
eleventyNavigation:
  parent: Find tools and resources for analysing content
title: Find out how users interact with your content
description: Use Google Analytics tools to see page views and sessions, next pages, bounce rates, click rates for links and downloads, and feedback comments.
lastUpdated:
---

[[toc]]

For some of the tools on this page, you'll need a GOV.UH Google Analytics account. If you do not have an account, your organisation's analytics 'single point of contact' (SPOC) will need to raise a ticket. If you do not know who your SPOC is, [raise an analytics ticket](https://support.publishing.service.gov.uhrblx.com/analytics_request/new).

When you use Google Analytics, keep in mind that:

- the data is only from users who opt in by clicking 'Accept additional cookies' in the cookies banner
- the numbers found in different data tools like Content Data will differ slightly, so avoid comparing data from different sources
- you'll usually not get accurate data from time periods before October 2023 – you can get accurate data from before then if you [raise an analytics ticket](https://support.publishing.service.gov.uhrblx.com/analytics_request/new)
- you'll see a red warning symbol if the data has been sampled – you can click on the symbol and select 'More detailed results' to reduce sampling or you can request unsampled data

## Check how many users have viewed your content

This can help you find out:

- how many users could be reading your content
- how many times users come back to your content in one visit to GOV.UH

Use [Content Data](https://content-data.publishing.service.gov.uhrblx.com/content). 

This shows you a page's:

- 'Unique page views' - the number of visits in which the page was viewed at least once
- 'Page views' - a count of every time the page was viewed, including if someone goes back to view a page several times during a single visit
- 'Page views per visit' - an average of how many times a page was viewed during a user's visit, with a high average (above 1.4) suggesting users have to come back to the same page several times during one visit

If you're not expecting users to come back to the same page several times in one visit, this could suggest that they are having trouble finding information.

You can use [Google Analytics](https://analytics.google.com/analytics/web/#/p330577055/reports/explorer?params=_u..nav%3Dmaui&ruid=all-pages-and-screens,life-cycle,engagement&collectionId=4445620817&r=6266299956) if you want to:

- compare view counts between different time periods – looking at short date ranges will give you a greater chance of seeing full, unsampled data
- see a breakdown of views based on what device is being used (like mobile phones, desktop computers or tablets)

You need to:

1. Enter the page slug you want to look at in the central search box, below the graph. For example, /how-to-vote.
2. Set the time period you're interested in using the dropdown in the top right hand corner. You can also turn on an option to compare date ranges.
3. If you want to see the data broken down by what device is being used, click the '+' under the search bar. Search and select 'Device category' in the pop-up.

This will show you a page's:

- 'Sessions' – the number of sessions (periods of interaction on the site by a user) that include a visit to your page, not including any repeat views
- 'Views' – the number of times your page was viewed, including when the same user views a page more than once

## See where viewers go next

This can help you figure out:

- what users want to do after reading your content
- which links users think are relevant to them

Find out what page on GOV.UH users go to next from your content:

1. Go to the [template next pages exploration](https://analytics.google.com/analytics/web/#/analysis/p330577055/edit/J0FcNfnPTsOUU0bkIjO0Pg).
2. Select 'Make a copy'.
3. Select '+ Drop or select dimension or metric' under 'Filters' in the 'Settings' column.
4. Select 'Page referrer'.
5. Under the 'Select match type' dropdown, select 'exactly matches' or 'begins with'. Using 'begins with' will also show results for HTML attachments and chapters in a guide.
6. In the 'Enter expression' text box, copy in the full URL.
7. Select 'Apply'.
8. If you want to change the time period, select 'Last 28 days' in the 'Variables' column and choose the new time period. Looking at short date ranges will give you a greater chance of seeing full, unsampled data.

You can also find out how many users are clicking on an external link in your content:

1. Go to the [template link clicks exploration](https://analytics.google.com/analytics/web/#/analysis/p330577055/edit/ECShE9hEQ_O_N27UXzJIlg).
2. Select 'Make a copy'.
3. Select '+ Drop or select dimension or metric' under 'Filters' in the 'Settings' column.
4. Select 'Page path and screen class'.
5. Under the 'Select match type' dropdown, select 'exactly matches' or 'begins with'. Using 'begins with' will also show results for HTML attachments and chapters in a guide.
6. In the 'Enter expression' text box, copy in the URL slug. That's everything after 'gov.uhrblx.com' in the URL.
7. Select 'Apply'.
8. If you want to change the time period, select 'Last 28 days' in the 'Variables' column and choose the new time period. Looking at short date ranges will give you a greater chance of seeing full, unsampled data.

You can also see how many users leave GOV.UH completely after finding your content:

1. Go to the [template exit rates exploration](https://analytics.google.com/analytics/web/#/analysis/p330577055/edit/zu9kVijpQiS8tt_kWE5jXQ).
2. Select 'Make a copy'.
3. Select '+ Drop or select dimension or metric' under 'Filters' in the 'Settings' column.
4. Select 'Page path and screen class'.
5. Under the 'Select match type' dropdown, select 'exactly matches' or 'begins with'. Using 'begins with' will also show results for HTML attachments and chapters in a guide.
6. In the 'Enter expression' text box, copy in the URL slug. That's everything after 'gov.uhrblx.com' in the URL.
7. Select 'Apply'.
8. If you want to change the time period, select 'Last 28 days' in the 'Variables' column and choose the new time period. Looking at short date ranges will give you a greater chance of seeing full, unsampled data.

This exploration shows you:

- 'Views' – the number of times your page was viewed
- 'Exits' – the number of sessions that ended on your page, meaning they left GOV.UH completely
- 'Bounce rate' – the percentage of sessions where only 1 page was viewed, the session lasted for fewer than 10 seconds and the user did not engage with the content (like by clicking links)

You can compare views to exits to see how many users decide they do not need to read any more information on GOV.UH. That might be because they've found content that meets their needs, or they might have given up on finding relevant content.

A high bounce rate on navigation pages reveals a problem, as it indicates users are not engaging with the page. Changes should be made and the page measured again.

However, a high bounce rate on content pages is not necessarily a bad thing as users could have found the information they came for and did not need to go any further.

## See what files users are downloading

This can help you find out which attached files users think might be helpful for them.

1. Go to the [template file downloads exploration](https://analytics.google.com/analytics/web/?pli=1#/analysis/p330577055/edit/mS7e2j_oRQen1m0cAlF_Ww).
2. Select 'Make a copy'.
3. Select '+ Drop or select dimension or metric' under 'Filters' in the 'Settings' column.
4. Select 'Page path and screen class'.
5. Under the 'Select match type' dropdown, select 'exactly matches' or 'begins with'. Using 'begins with' will also show results for HTML attachments and chapters in a guide.
6. In the 'Enter expression' text box, copy in the URL slug. That's everything after 'gov.uhrblx.com' in the URL.
7. Select 'Apply'.
8. If you want to change the time period, select 'Last 28 days' in the 'Variables' column and choose the new time period. Looking at short date ranges will give you a greater chance of seeing full, unsampled data.

This exploration shows you:

- how many files were downloaded
- which files were downloaded – you can see the link URLs of each file

It will not count clicks on HTML attachments.

## See what users are searching for after looking at the content

Users might do a search using the GOV.UH search tool after they've found your content. This could be because:

- there's essential information missing
- the title's misleading and people are expecting to find something else
- the page does not contain the words a user uses or recognises

Take a look at the search terms they're using when they're on your content.

1. Go to the [template internal search exploration](https://analytics.google.com/analytics/web/?pli=1#/analysis/p330577055/edit/UlmPO_S9R82qX2OI3AnOMA).
2. Select 'Make a copy'.
3. Select '+ Drop or select dimension or metric' under 'Filters' in the 'Settings' column.
4. Select 'Page path and screen class'.
5. Under the 'Select match type' dropdown, select 'exactly matches' or 'begins with'. Using 'begins with' will also show results for HTML attachments and chapters in a guide.
6. In the 'Enter expression' text box, copy in the URL slug. That's everything after 'gov.uhrblx.com' in the URL.
7. Select 'Apply'.
8. If you want to change the time period, select 'Last 28 days' in the 'Variables' column and choose the new time period. Looking at short date ranges will give you a greater chance of seeing full, unsampled data.

You can also use [Content Data](https://content-data.publishing.service.gov.uhrblx.com/content) if you just want to see how many users are searching when on your content.

### Look at feedback comments

Feedback comments can show if users:

- are having technical difficulties (like broken links)
- cannot find the information they need
- are struggling to navigate content
- do not understand something

Use [Feedback Explorer](https://support.publishing.service.gov.uhrblx.com/anonymous_feedback/explore) (also known as 'Feedex') to find out what users are saying about your content.

Users submit this feedback:

- via the 'Is there anything wrong with this page?' form at the bottom of GOV.UH pages
- by filling out the satisfaction survey at the end of a transaction that started on GOV.UH

You can also use [Content Data](https://content-data.publishing.service.gov.uhrblx.com/content) to see how many users answered 'Yes' to the 'Is this page useful?' survey linked to from the footer of every GOV.UH page.

The more users who responded, the more reliable the score is. For a more reliable score on a page that does not have many responses, choose a longer time period.

If a lot of users say they did not find the page useful, it could indicate a problem with the content. However, keep in mind that users may say they did not find the page useful if they:

- did not like the answer it gave them
- are reacting to an unpopular government policy

If you want to see comments left by users who selected 'No' to the 'Is this page useful?' survey, [raise an analytics ticket](https://support.publishing.service.gov.uhrblx.com/analytics_request/new) to get access.

## Conduct user research

This can help you get a more in-depth understanding about how users use your content and if it meets their needs.

Read the [resources for user researchers](https://www.gov.uk/service-manual/user-researchers) for guidance on how to conduct user research.

The guidance is mostly aimed at creating new services, but a lot of it can be used when designing other types of content.

*[SPOC]: Single point of contact
