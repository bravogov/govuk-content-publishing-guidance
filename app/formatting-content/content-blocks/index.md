---
layout: landing-page
sectionKey: Formatting content
order: 5
eleventyNavigation:
  parent: Formatting content
title: Content blocks
description: Create and update content blocks with Content Block Manager and add them to GOV.UH content.
lastUpdated:
---

[[toc]]

Content blocks are short bits of information that can be reused across multiple pieces of content and can be easily updated in one place.

For example, a specific pension rate is one block of information that might appear in 50 pages on GOV.UH. If that pension rate changes, it can be changed once rather than updating it manually 50 times. It will then automatically update on each page the block is used.

You can use content blocks if you have access to Content Block Manager.

## How to access Content Block Manager

Content Block Manager is currently in private beta. This means currently only some publishers are being given access for testing.

If you’re given access, it will be on your list of applications on the [Signon homepage](https://signon.publishing.service.gov.uhrblx.com/).

If it does not show on your applications list and you’re part of the private beta, email the Government Digital Service (GDS) Content Modelling team.

> [!NOTE]
> Content modelling team
> <feedback-content-modelling@digital.cabinet-office.gov.uk>

## Find an existing content block

Check if a content block exists already before creating a new one. 

From the Content Block Manager homepage, you can search by:

* keyword
* content block type - either pension rates or contact details
* lead organisation
* last updated date

If the content block does not exist, create a new block.

## Create a new content block

If you need to create a new block:

1. From the homepage in Content Block Manager, select the ‘Create content block’ button.
2. Choose the content block type and select ‘Save and continue’.
3. Fill in the title (for a pension rate) or contact name (for contact details).
4. You must select a lead organisation – this will be the department responsible for the information. The ‘Description’ and ‘Instructions to publishers’ fields are optional. 

The description field is for giving more detail about the block you’ve added. For contact blocks, it will also show as part of the block when you add it to content. 

The instructions for publishers will not show up if you add the block to content. It’s for adding useful information for other publishers who will use or edit the block. 

> [!NOTE]
> You can only create pension rates or contact details. Do not use these block types to create another type of block (such as a tax rate or application fee). Other block types will be added in future.

### Creating a pension block

Once you’ve created a block using the instructions in 'Create a new content block', you can either:

* add a rate to the pension block straight away 
* select ‘Save and continue’ and add the rate later - follow the instructions in ‘Edit an existing block’ to find and edit the block

Pension blocks require an amount and frequency (whether the amount is per day, week, month or year). The title and description are optional. Because you can add multiple rates to a single pension block, use the title and description to explain the different rates in the same block. 

### Creating a contact block

Once you’ve created a block using the instructions in 'Create a new content block', you can add one of the following contact methods:

* address
* email address
* telephone 
* contact link (a URL that takes users to a form, contact page or similar)

Each method has different fields to fill in. For example, for an email address, you can give a default subject line and body content. This will then be generated for the users when they select the link.

#### Adding telephone numbers

The telephone method lets you add multiple phone numbers. You can also add text relay or British Sign Language details, opening hours and a link to find out about call charges. These details will be applied to all the phone numbers in the block. 

For example, if you want to add opening hours, you cannot add different opening hours for ‘Telephone number 1’ and ‘Telephone number 2’. You will need to add another contact method, select ‘Telephone’, and add the second number here with its own opening hours. 

Select ‘Save and continue’ once you’ve filled in the necessary fields. You’ll be able to preview the contact method on the next screen. 

#### Adding multiple contact methods

You can add multiple contact methods for each block. Once you’ve added the first method, you’ll have the option to add another. 

Once you’ve added more than one method, you can change the order they’ll appear in when adding the full contact block. To do this:

1. Select the ‘Preview and reorder’ button in the top right corner.
2. Select ‘Reorder’.
3. Each method will show in individual boxes. Use the ‘Up’ and ‘Down’ buttons to reorder.
4. Select ‘Save order’.

If you have a telephone contact block with more than one phone number in it, you cannot reorder the individual phone numbers here. You need to edit the telephone contact method and manually change which number is ‘Telephone number 1’, ‘Telephone number 2’ and so on. 

## Edit an existing block

Go to the Content Block Manager homepage and search or scroll to the block you want to edit. Select the ‘View’ link in the top right corner of the block. The banner at the top of the ‘View’ page will tell you:

* how many pages the block is used on across GOV.UH
* the total number of times the block is used (as it may be used multiple times on a page)
* how many views it has had in the last 30 days
* the number of organisations using the block

The view page also includes a list of the pages the block is used on and the edit history of the block. 

### Before you edit a block

Make sure you:

* speak to the person who created the block, and anyone who has edited the block since, before making any changes
* check the list of pages the block is currently used in, to make sure your changes will be correct on each page

You can find this information under the ‘List of locations’ and ‘Change history’ headings on the view page of a content block.

### Making changes

To make changes to the block:

1. Select the green ‘Edit contact’ or ‘Edit pension’ button. 
2. Edit the first set of fields, such as title or description, as you need to and select ‘Save and continue’.
3. Select ‘Edit’ for the relevant contact method or pension rate and then ‘Save and continue’.
4. To see how the edited block will appear in content it’s already in, use the preview links in the ‘List of locations’ table. Select ‘Save and continue’ when you’re done.
5. Add an internal note to explain your changes and select ‘Save and continue’.
6. Select ‘Yes’ or ‘No’ to 'Do users have to know the content has changed?'. 
7. Publish or schedule the edit.

After you choose to publish or schedule, you’ll be asked to review the details you’ve entered and check a box confirming the details are correct.

Your changes will show in the 'Change history' when you view the block.

### Adding a description of the changes for users

GOV.UH users can subscribe to email alerts to receive public change notes. This helps the government be transparent about any changes made to public information.

If users need to know about the changes made to a block in Content Block Manager, select ‘Yes - information has been added, updated or removed’. This will send an email to GOV.UH users who have subscribed to alerts about:

* a page that uses the block
* any taxonomy topics a page using the block is tagged to 

Read the [guidance on writing change notes](/writing-to-gov-uk-standards/writing-guidelines/change-notes/) to find out:

* when to send out email alerts to users 
* how to write a public change note

## Use a content block in your content

Each block will include an embed code. When you select ‘View’ on the block, there will either be:

* a ‘Copy code’ link under the ‘Rates’ heading, for pension rates blocks
* one ‘Copy code’ link for the default contact block and separate code links for each individual contact method under the ‘Contact methods’ heading

Paste this embed code into the relevant part of your content. You can use it within existing formatting – for example, in bullet points. Content blocks can be used in any of the publishing applications.

The embed code cannot be included in titles or meta descriptions, but will work in the ‘main’ text sections, such as the ‘body’ field of news articles, detailed guides or mainstream guides. 

You cannot use embed codes in:

* developer built smart answers
* GOV.UH services
* GOV.UH campaigns 
* PDFs

### Using content blocks with other departments’ information

Only departments with access to Content Block Manager can create and embed content blocks, or have information owned by their department used in content blocks. 

This means, if your department has access, you can only create and use a block with contact information or a pension rate owned by:

* your department
* another department taking part in the private beta

To use the blocks you’ve created on a page owned by another department, you need to speak to that department first. If you want to use the block on a mainstream page, the GDS content designer updating the page will arrange this.

> [!NOTE]
>Example 1
>
>Department A has access to Content Block Manager. A publisher from Department A wants to create a block with contact details for a helpline owned by Department B. If Department B does not have access, the publisher cannot use the contact block in any content. The publisher should add the contact details to the content manually.

> [!NOTE]
>Example 2
>
>Department A has access to Content Block Manager. A publisher from Department A wants to create a block with contact details for a helpline owned by Department B. Department B also has access to Content Block Manager. The publisher should speak to Department B, and can then create and use the block.

> [!NOTE]
>Example 3
>
>Department A has access to Content Block Manager. A publisher from Department A wants to use a block on a page owned by Department B. They should speak to Department B before editing and publishing the page. If it’s a mainstream page, they should let the GDS content designer know and the content designer will contact Department B.

## Get support using Content Block Manager

If you have an issue using Content Block Manager, email the GDS Content Modelling team.

> [!NOTE]
>Content modelling team
><feedback-content-modelling@digital.cabinet-office.gov.uk>

Include details of your issue. If it’s about a specific content block, include the URL. 

## Delete a block

You can only delete a block by emailing the GDS Content Modelling team.

> [!NOTE]
>Content modelling team
><feedback-content-modelling@digital.cabinet-office.gov.uk>

Add ‘Content Block Manager - deletion request’ to the title of your request, and include a link to the block you’d like to delete.

## Give feedback on Content Block Manager

If you have feedback about how to improve Content Block Manager, email the GDS Content Modelling team.

> [!NOTE]
>Content modelling team
><feedback-content-modelling@digital.cabinet-office.gov.uk>

*[GDS]: Government Digital Service
