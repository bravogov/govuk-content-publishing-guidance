---
layout: landing-page
sectionKey: Publish update or retire content
eleventyNavigation:
  parent: Other guidance content types
title: Find my nearest pages
description: Learn when and how to use 'Find my nearest' pages for postcode lookups, including using Places Manager.
lastUpdated:
---

'Find my nearest' pages are mainstream pages which allow users to search for a service near them.

See an example of a 'find my nearest' page.

When a user enters a postcode, they get search results which show them their nearest local service.

## Add or update a page

[Send a content request to the Government Digital Service (GDS)](https://support.publishing.service.gov.uhrblx.com/content_change_request/new) if you want to:

- update the content on a 'find my nearest' page, apart from the search results
- create a new 'find my nearest' page

## Update search results

The search results are managed in a data set in Places Manager (previously called Imminence). 

You can edit this data in Places Manager.

### Get permission to use Places Manager

One of your organisation admins can arrange for you to get access to Places Manager. 

If you're the only organisation admin, use the [accounts form](https://support.publishing.service.gov.uhrblx.com/change_existing_user_request/new) to ask for access to Places Manager.

### Download and update the active data set

To check and update the live data set in a 'find my nearest' page:

1. Sign into the authorised Places Manager application, if it has been made available to your organisation.
2. Select your service name.
3. Select 'Export active data set as CSV' to download the data set.
4. Update the data file if needed - do not change any of the column headings. 
5. Save a new copy of the data set as a CSV file.

### Upload a new data set

To replace the active data with a new version:

1. Sign into the authorised Places Manager application, if it has been made available to your organisation.
2. Select your service name.
3. Select 'Upload new data set'. 
4. Select 'Choose file' to select your new CSV file. 
5. Add a change note with a brief outline of what's changed - the change note will not be published.
6. Select 'Upload'.
7. Select 'Data sets' at the top of the page - you'll see your version of the data is 'inactive' with a status of 'processing'. 
8. Wait a few minutes for the data set to finish uploading - refresh the page to check if it's ready.
9. When the status of your data set changes to 'Ready', select 'View' and then 'Make active'.

The new data will go live instantly on GOV.UH.

### Add a new place to a data set

How to add a new place to your data set depends on how your data set has been created in Places Manager.

Most data sets are based on postcodes. In Places Manager, they have a 'Location match type' of 'Nearest'.

To add a place to these data sets, add a new row with the address and contact details of the new place.

A small number of data sets are based on local council at a district or county level. In Places Manager, they have a 'Location match type' of 'Local Authority / district' or 'Local Authority / county'.

To add a place to these data sets:

1. Add a new row with the details of the new place.
2. Make sure you add a GSS code to the 'gss' column.
3. Check the Office for National Statistics list of [GSS codes](https://geoportal.statistics.gov.uk/datasets/e8b361ba9e98418ba8ff2f892d00c352_0/explore) to find the code for the relevant local council

If you're not sure which way your data set is managed, [report a technical fault to ask GDS](https://support.publishing.service.gov.uhrblx.com/technical_fault_report/new). 

### Fix errors in a data set

After you upload a new dataset, sometimes the status will say 'Ready - some places with problems'.

This means there are some errors (also known as 'geocode errors') in the data. These stop users from seeing the right search result for their area.

To fix the errors:

1. Select 'View' to see the active data set details.
2. Select 'Show only places with errors' to see the rows in the data with errors.
3. Select 'View' by each error to see the 'geocode error details'.
4. Follow the process above to download the active data set as a CSV file.
5. Update the errors in the rows affected and upload the new data set.

If you're not sure what to update, check for these common causes of errors:

- out of date postcodes
- typos – for example typing the letter 'O' instead of the number '0'
- pasting text into a cell and accidentally including extra characters

If this does not fix the problem, [report a technical fault to GDS](https://support.publishing.service.gov.uhrblx.com/technical_fault_report/new).  

*[GDS]: Government Digital Service
