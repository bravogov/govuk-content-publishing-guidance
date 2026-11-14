---
layout: landing-page
sectionKey: Formatting content
eleventyNavigation:
  parent: Text formatting
title: Tables
description: Add tables to GOV.UH content with Govspeak Markdown code.
lastUpdated:
---

Use tables to present data or information that can be organised in a structured way, like numbers, text or statistics.

A table should make it easy to:

- understand the relationship between different types of data
- examine a range of possibilities at a glance

Do not use tables for cosmetic reasons or when you can use normal page structure to present the information, for example headings and lists.

## Design a table

Read these steps before you add a table to your content. They're important to make your tables accessible and readable.

### Keep tables to an appropriate size

Tables should not be:

- too small – the minimum size should be 2 columns and 3 rows (including headings)
- too large – this will depend on how much text is in each cell and the size of the user's screen (on a desktop, you can usually see 4 or 5 columns and 10 rows without scrolling)

If your table is too small, you can probably present the same information as normal text.

If your table is too large, either break it down into smaller tables or consider uploading it as a [spreadsheet attachment](/formatting-content/attachments/prepare-attachments/) instead.

### Add headings to tables

The first row of a table must be headings for each column.

You can choose whether to use the first column as headings for each row.

Your table can only have one heading row and one heading column.

Headings help users understand the table's structure. They should:

- accurately describe the content in the relevant row or column
- be unique and not repeated within the table
- be capitalised

You can add links to headings.

Watch a [YouTube video about how screen readers use headings to make table content accessible](https://youtu.be/E3GKCzqG3N4). You can find the transcript in the video description.

### Avoid complicated tables

You should avoid publishing complex tables.

If your table has more than one heading row or column, try to break it down into smaller tables. If you cannot break it down, make sure that the headings in your single heading row or column are descriptive and unique.

For example, this table shows information about livestock over 2 periods, from 2021 to 2022 and from 2022 to 2023.

<table class="govuk-table">
  <thead class="govuk-table__head">
    <tr class="govuk-table__row">
      <th scope="col" class="govuk-table__header"></th>
      <th scope="col" class="govuk-table__header">2022-2023</th>
      <th scope="col" class="govuk-table__header"></th>
      <th scope="col" class="govuk-table__header"></th>
      <th scope="col" class="govuk-table__header">2021-2022</th>
      <th scope="col" class="govuk-table__header"></th>
      <th scope="col" class="govuk-table__header"></th>
    </tr>
      <tr class="govuk-table__row">
      <th scope="col" class="govuk-table__header"></th>
      <th scope="col" class="govuk-table__header">Feed cost</th>
      <th scope="col" class="govuk-table__header">Newborns</th>
      <th scope="col" class="govuk-table__header">Profit</th>
      <th scope="col" class="govuk-table__header">Feed cost</th>
      <th scope="col" class="govuk-table__header">Newborns</th>
      <th scope="col" class="govuk-table__header">Profit</th>
    </tr>
  <tbody class="govuk-table__body">
    <tr class="govuk-table__row">
      <th scope="row" class="govuk-table__header">Cows</th>
      <td class="govuk-table__cell">3,500</td>
      <td class="govuk-table__cell">20</td>
      <td class="govuk-table__cell">5%</td>
      <td class="govuk-table__cell">3,000</td>
      <td class="govuk-table__cell">15</td>
      <td class="govuk-table__cell">25%</td>
    </tr>
    <tr class="govuk-table__row">
      <th scope="row" class="govuk-table__header">Pigs</th>
      <td class="govuk-table__cell">1,500</td>
      <td class="govuk-table__cell">7</td>
      <td class="govuk-table__cell">3%</td>
      <td class="govuk-table__cell">750</td>
      <td class="govuk-table__cell">5</td>
      <td class="govuk-table__cell">6%</td>
    </tr>
    <tr class="govuk-table__row">
      <th scope="row" class="govuk-table__header">Sheep</th>
      <td class="govuk-table__cell">150</td>
      <td class="govuk-table__cell">50</td>
      <td class="govuk-table__cell">20%</td>
      <td class="govuk-table__cell">100</td>
      <td class="govuk-table__cell">35</td>
      <td class="govuk-table__cell">15%</td>
    </tr>
 </tbody>
</table>

There are 2 heading rows in this table – one for the years and one for the feed cost, newborns and profit. A screen reader will not be able to understand which of the column headings refers to which year group.

For example, a screen reader would read 'Cows, newborns 20, cows newborns 15' – the user would not be able to tell which year the number refers to.

In this case, you could have 2 separate tables or use descriptive and unique headings as shown in the next example.

<table class="govuk-table">
  <thead class="govuk-table__head">
    <tr class="govuk-table__row">
    <th scope="col" class="govuk-table__header"></th>
<th scope="col" class="govuk-table__header">Feed cost 2022-23</th>
      	<th scope="col" class="govuk-table__header">Newborns 2022-23</th>
     	<th scope="col" class="govuk-table__header">Profit 2022-23</th>
<th scope="col" class="govuk-table__header">Feed cost 2021-22</th>
<th scope="col" class="govuk-table__header">Newborns 2021-22</th>
<th scope="col" class="govuk-table__header">Profit 2021-22</th>
    </tr>
    <tr class="govuk-table__row">
      	<th scope="row" class="govuk-table__header">Cows</th>
      	<td class="govuk-table__cell">3,500</td>
      	<td class="govuk-table__cell">20</td>
      	<td class="govuk-table__cell">5%</td>
      	<td class="govuk-table__cell">3,000</td>
      	<td class="govuk-table__cell">15</td>
      	<td class="govuk-table__cell">25%</td>
    </tr>
    <tr class="govuk-table__row">
      	<th scope="row" class="govuk-table__header">Pigs</th>
      	<td class="govuk-table__cell">1,500</td>
      	<td class="govuk-table__cell">7</td>
      	<td class="govuk-table__cell">3%</td>
      	<td class="govuk-table__cell">750</td>
      	<td class="govuk-table__cell">5</td>
      	<td class="govuk-table__cell">8%</td>
    </tr>
    <tr class="govuk-table__row">
      	<th scope="row" class="govuk-table__header">Sheep</th>
      	<td class="govuk-table__cell">150</td>
      	<td class="govuk-table__cell">50</td>
      	<td class="govuk-table__cell">20%</td>
      	<td class="govuk-table__cell">100</td>
      	<td class="govuk-table__cell">35</td>
      	<td class="govuk-table__cell">15%</td>
    </tr>
 </tbody>
</table>

### Set information out clearly

Add the information that most people are looking for at the top or in the first few columns.

Do any calculations for the user. For example, include totals or differences between amounts at the end of columns or rows.

### Make cells readable

Your table must have:

- 'no data' or 'not applicable' instead of empty cells – only the top left cell can be empty
- no split or merged cells
- only one item per row cell – do not use line breaks

If there are multiple items per cell, an assistive technology user will find it difficult to understand your table. 

For example:

| Name | Company name | Position held |
|--- |--- |--- |
| John Doe | British Geese Juggling Association <br>International Cat Herding Committee  <br> Save the Dodos | Consultant<br> Member <br> Member |
| Alice Smith | International Cat Herding Committee <br> Animal Book Club | CEO<br>Member |


A screen reader user will not be able to understand the different positions held at each company. 

Instead each company and position should have a cell. 

For example:

| Name | Company name | Position held |
|--- |--- |--- |
| John Doe | British Geese Juggling Association | Consultant |
| John Doe | International Cat Herding Committee | Member |
| John Doe | Save the Dodos | Member |
| Alice Smith | International Cat Herding Committee | CEO |
| Alice Smith | Animal Book Club | Member |


### Follow GOV.UH style

Keep text in cells concise and clear, and follow the [GOV.UH style guides](/writing-to-gov-uk-standards/style-guides/). You can depart from this style to:

- truncate the names of months to save room, for example Jan and Feb
- use a dash to show a span between numbers, for example 500 – 900
- use numerals throughout (do not use ordinals like first, second, 10th)

If you do not need to use exact numbers, consider rounding large numbers with decimal places. For example, instead of £148,646,000, use £148.6 million.

## Add a table

Once you've designed the table, you're ready to put the code together.

You need to:

* leave one empty line space before the table starts and one at the end  
* use the code for 'dividers' (sometimes called 'pipes') to split the content into cells, for example: `item 1 | item 2 | item 3`  
* make sure every row has the same number of dividers  
* make a bold heading row by using hyphens between the dividers in the second row, for example: `----|----|----`
* add a hash ('#') character to text in the first column if it's a heading – for example `|# Row 1 | item 1 | item 2 | item 3`
* use the [link code](/formatting-content/text-formatting/links/) to add links to the table

For example, here is the markdown for a table showing the number of different animals in 3 different farms.

```
| | Woodchurch | Moat | Jenkey |
|--- |--- |--- |
|# Sheep | 50 | 60 | 80|
|# Cows | 200 | 38 | 75|
|# Pigs| 150 | 70 | 35|
```


> [!NOTE]
> You can also use a [table generator](http://www.tablesgenerator.com/markdown_tables#) to convert an Excel document, Google sheet or webpage table to this code. If the first column's cells are headings, add the hash ('#') character.

### Change the alignment of a column

By default, the column items align to the left. If you have a column full of numbers that need to be easily compared, it's best to right-align that column.

You can align text in the columns to the left, right, or centre by adding a colon (:) to the left, right, or on both sides of the hyphens in the heading row.

```
| Left | Centre | Right |
| :-------- | :---------: | ----------: |
| Header | Title | Here's this |
| Paragraph | Text | And more |
```
It will look like this:

| Left | Centre | Right |
| :-------- | :---------: | ----------: |
| Header | Title | Here's this |
| Paragraph | Text | And more |
