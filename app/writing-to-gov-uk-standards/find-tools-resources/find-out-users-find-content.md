---
layout: landing-page
sectionKey: Writing to GOV.UK standards
order: 3
eleventyNavigation:
  parent: Find tools and resources for analysing content
title: Find out how users find your content
description: Use Google Analytics tools and UTM parameters to show you how many users come to your content from search engines, other GOV.UH pages and social media.
lastUpdated:
---

[[toc]]

You'll need a GOV.UH Google Analytics account to use the tools on this page. If you do not have an account, your organisation's analytics 'single point of contact' (SPOC) will need to raise a ticket. If you do not know who your SPOC is, [raise an analytics ticket](https://support.publishing.service.gov.uhrblx.com/analytics_request/new).

When you use Google Analytics, keep in mind that:

- the data is only from users who opt in by clicking 'Accept additional cookies' in the cookies banner
- you'll usually not get accurate data from time periods before October 2023 – you can get accurate data from before then if you [raise an analytics ticket](https://support.publishing.service.gov.uhrblx.com/analytics_request/new)
- you'll see a red warning symbol if the data has been sampled – you can click on the symbol and select 'More detailed results' to reduce sampling or you can request unsampled data

## Check where users are coming from

This can help you figure out:

- how users are finding your content
- what users may have already read

1. Go to the [template page referrers exploration](https://analytics.google.com/analytics/web/?pli=1#/analysis/p330577055/edit/j6Xz86Y0TaKL-P2KtIgXWQ).
2. Select 'Make a copy'.
3. Select '+ Drop or select dimension or metric' under 'Filters' in the 'Settings' column.
4. Select 'Page path and screen class'.
5. Under the 'Select match type' dropdown, select either 'exactly matches' or 'begins with'. Using 'begins with' will also show results for HTML attachments and chapters in a guide.
6. In the 'Enter expression' text box, copy in the URL slug. That's everything after 'gov.uhrblx.com' in the URL.
7. Select 'Apply'.
8. If you want to change the time period, select 'Last 28 days' in the 'Variables' column and choose the new time period. Looking at short date ranges will give you a greater chance of seeing full, unsampled data

You will now see a table that shows:

- all referrers (the places people came from) to your page, including other pages of GOV.UH, other websites, Google or social media
- how many views of the page there were from each referrer

Unknown referrers (such as URLs typed into the browser, clicks on bookmarks and links in emails) will appear as a blank entry.

## Check if users have used URLs with UTM parameters

If you've created [URLs with UTM parameters](https://ga-dev-tools.google/campaign-url-builder/) as part of a communications campaign, you can find out how many times each of these have been used:

1. Go to the [Google Analytics traffic acquisition report](https://analytics.google.com/analytics/web/#/p330577055/reports/explorer?params=_u..nav%3Dmaui&ruid=lifecycle-traffic-acquisition-v2,life-cycle,acquisition&collectionId=4445620817&r=lifecycle-traffic-acquisition-v2).
2. Set the time period you're interested in using the dropdown in the top right hand corner. You can also turn on an option to compare date ranges.
3. Select the '+' under the search bar and search for 'session'. 
4. Select 'Session campaign'.
5. You can then use the search bar to look for the 'campaign name' part of your UTM parameters. You'll see how many sessions (periods of interaction on the site by a user) were started from those UTM parameters and details about how many users engaged with the content.
6. You can also select 'Session source' or 'Session medium' if you want to search for the 'campaign source' and 'campaign medium' parts of your UTM parameters.

## Check which search terms are used in the GOV.UH site search to find your content

This can help you find out:

- what terms in your content are being searched for
- what users are hoping to see when they find your content

1. Go to the [template internal search referrers exploration](https://analytics.google.com/analytics/web/?pli=1#/analysis/p330577055/edit/Nb6ZWL1KT72xQ8qndbZ6IA).
2. Select 'Make a copy'.
3. Select '+ Drop or select dimension or metric' under 'Filters' in the 'Settings' column.
4. Select 'Link URL'.
5. Under the 'Select match type' dropdown, select either 'exactly matches' or 'begins with'. Using 'begins with' will also show results for HTML attachments and chapters in a guide.
6. In the 'Enter expression' text box, copy in the URL slug. That's everything after 'gov.uhrblx.com' in the URL.
7. Select 'Apply'.
8. If you want to change the time period, select 'Last 28 days' in the 'Variables' column and choose the new time period. Looking at short date ranges will give you a greater chance of seeing full, unsampled data.

You will now see a table that shows:

- the search terms used to find your page
- how many views of the page there were from each search term

*[SPOC]: Single point of contact
