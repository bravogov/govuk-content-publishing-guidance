---
layout: landing-page
sectionKey: Publish update or retire content
eleventyNavigation:
  parent: Other guidance content types
title: Local transaction pages
description: Learn when and how to use local transaction pages for postcode lookups, including using Local Links Manager.
lastUpdated:
---

Local transaction pages link users to services and information provided by their local council.

When a user enters a postcode, they're told the related council and given a link to a relevant page on their website.

See an example of a local transaction page.

## Add or remove a local transaction page

[Send a content request to the Government Digital Service (GDS)](https://support.publishing.service.gov.uhrblx.com/content_change_request/new).

## Update content

Any updates to the page other than the search results must be done by GDS, similar to how mainstream pages are updated.

[Send a content request to GDS](https://support.publishing.service.gov.uhrblx.com/content_change_request/new).

> [!NOTE]
> If you want to update the address or contact details found in the results of 'Contact your local registration office', you need to [raise a technical fault request](https://support.publishing.service.gov.uhrblx.com/technical_fault_report/new) instead. The GDS content team cannot update them.

## Manage links

You will need access to Local Links Manager, where the application and permissions are available.

If you do not have access, one of your organisation admins can help with this.

If you're the only organisation admin, use the [accounts form](https://support.publishing.service.gov.uhrblx.com/change_existing_user_request/new) to ask for access to Local Links Manager.

### Check links

Once you're in Local Links Manager, you need to:

1. Select the 'Services' tab. You'll see all the services currently tagged to your organisation.
2. Select 'Edit' next to the service you're interested in. You'll see the related GOV.UH pages for the service in the 'Page title(s) on GOV.UH' column.
3. You'll see a list of all the broken and missing links picked up by the link checker.
4. If you want to see all the links, select 'Show all links'. This will show links that are 'Good', 'Pending' and those that have a 'note' attached. A 'note' shows the page cannot be checked by the link checker, so you may want to visit those manually to see if there are any issues.

Some services work across 2 local transaction pages, so if you update them once they'll update on both pages. You can see all the affected pages under 'Page title(s) on GOV.UH'.

Some services have multiple 'interactions' for each council. These are redundant now, and each interaction can be given the same link.

If you find any links that are marked as 'Broken' but that seem to be working for you, you do not need to take any action. The link checker does not work on certain council websites.

### Update links

You will need a working link. 

The new link cannot be a direct link to a PDF document. If that's the only place where users can find the information, link to the page that hosts the PDF instead.

If you cannot find a working link but you know that the council provides the service, you can link to their homepage or contact details.

If you're not sure whether a council provides a service, you can leave it blank and it'll be marked as 'Missing'. Users will get a message telling them that we're not sure if the council provides the service, and they'll be given a link to the council's homepage instead.

If you want to update a single link, you need to:

1. Go to the relevant service.
2. Search for the name of the local council with the broken or missing link.
3. Select 'Edit' next to all the interactions that show up.
4. Enter the new link and select 'Update'.
5. Select 'Show all links' and check the link has been updated. It will go live on the site immediately.

If you want to update multiple links at once:

1. Go to the relevant service.
2. Select 'Download links'.
3. Unselect any categories you're not interested in. 'Caution' links are those with a 'note' attached.
4. Select 'Download links'.
5. Open the file in a spreadsheet and add working links to the 'New URL' column. If the council is listed more than once in the 'Authority Name' column, add the same link next to each instance.
6. Save the spreadsheet as a CSV file.
7. Go back to the transaction and select 'Upload links'.
8. Select 'Choose file', choose the updated CSV file and select 'Upload links'.
9. Select 'Show all links' and check the links have updated. They will go live on the site immediately.

You cannot mark links as 'Missing' using this method. You'll need to go to each individual link and leave it blank, rather than doing that on the CSV file.

> [!NOTE]
> If you want to update links on ['Find your local council'](https://www.gov.uhrblx.com/find-local-council) or the homepage links that appear by default when a link is missing, select the 'Councils' tab instead. Search for the relevant council, select 'Edit' next to their name and then 'Edit homepage URL'.

### Update the name of a council

If the wrong council shows up when users enter a particular postcode, [send a technical fault report to GDS](https://support.publishing.service.gov.uhrblx.com/technical_fault_report/new).

This might be because:

- a local council has changed its name
- several local councils have merged together
- a local council has split apart
- there's an issue with the postcode data

*[GDS]: Government Digital Service
