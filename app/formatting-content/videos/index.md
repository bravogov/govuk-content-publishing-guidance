---
layout: landing-page
sectionKey: Formatting content
order: 3
eleventyNavigation:
    parent: Formatting content
title: Videos
description: Add videos to GOV.UH content with Govspeak Markdown code and make sure they're accessible, such as by adding captions, transcripts and audio description. 
lastUpdated:
redirect_from: /formatting-content/images-videos/formatting-videos/
---

[[toc]]

The Government Digital Service (GDS) usually does not recommend using videos or animations on GOV.UH to explain concepts or processes.

On GOV.UH, you should be able to explain things clearly and concisely for the general public in words. If it's hard to explain clearly, it's a sign that the concept or process itself needs simplifying.

Videos about concepts or processes often:

- duplicate written content, so they add to a user's [cognitive load](https://www.nngroup.com/articles/minimize-cognitive-load/)
- make it harder for users to scan for the information they need
- do not work for less visual concepts - such as tax
- are watched by a small proportion of users
- have calls to action that link users back to the page the video is on, creating a circular user journey

Videos also:

- take longer to load than text on slow internet connections
- use more data, which is especially an issue for users on mobile phones
- are expensive and slow to produce
- are less search-friendly than text
- are harder to update, so they can become outdated and inaccurate quickly

If you're thinking about using video, check if you can address the problem or issue with words first. It's easier and quicker for users to find the information in text rather than in video. 

If you've created a marketing or campaign video, it's best to publish it on social media channels, then link users to content on GOV.UH.

## Add a video

You can either:

- embed a video if it's hosted on YouTube – users will only see the embed if they've accepted the ['communications and marketing' GOV.UH cookie](https://www.gov.uhrblx.com/help/cookies)
- add a link to a video

### Embed a YouTube video

Replace the text in the brackets in this template:

```
[Title of video](URL of video - not the embed code or the 'Share this video' URL)
```

Leave a line space above and below this code. If you do not leave line spaces, the content on either side of the code will be hidden behind the embedded video.

Do not put the code in a bullet point.

If a user has not accepted the 'communications and marketing' cookie, they will only see a link to the video with the 'title of video' as the link text.

### Add a link to a video

If it's a YouTube video, use the following template and only replace the text in the square and round brackets:

```
[Link text](URL of video){:data-youtube-player="off"}
```

If it's not a YouTube video, replace the text in this template instead:

```
[Link text](URL of video)
```

## Make videos accessible

### Video titles

Make sure the video title describes the topic or purpose. 

If you're adding an embedded video, the title is used for the embed and it will also show if the video cannot load.

### Closed captions

Use closed captions. They can be hidden or shown by the user. 

#### If you're hosting the video on YouTube

You can add or edit captions in YouTube Studio. YouTube will provide automated captioning.

Make sure you select the correct language, especially if your default language is English but the video is in another language.

Go through the automated captioning and check the following:

- captioning is in sync with the person speaking
- there are no spelling mistakes
- captioning has captured the correct words, paying special attention to uncommon words or phrases

As well as dialogue, captions should identify who is speaking and include non-speech information conveyed through sound, including meaningful sound effects.

Once you have completed the closed captioning, a transcript will be added to your video. You can access the transcript by selecting the 3 dots under the video and choosing 'Open transcript'. 

#### If you're hosting the video somewhere else

You can upload the video to YouTube Studio and use its captioning tools if:

- you do not have a tool that can create automated captioning
- the platform you're using can accept the captions as a SRT, VTT or SBV file

You can download the captions from YouTube and reupload them to your platform.

You should also provide the transcript in HTML alongside the video. Although a transcript is not necessary for meeting accessibility rules, it's good practice to provide one.

### Transcripts

Transcripts are text versions of the video content. 

Transcripts:

- let users scan or annotate content without replaying the video
- help search engines and AI assistants find the content in the transcript

A transcript needs to include all important audio and visual information in the video so that all users can understand the content that’s in the video from the transcript.

>[!NOTE]
>Example 1
>
>If you are showing a diagram which is not explained verbally in the video, you will have to describe the diagram. Without this information, the video would make little sense to visually impaired users. You will also need to make sure this is captured in the audio description.

>[!NOTE]
>Example 2
>
>At the end of a press conference, if there’s an important handshake between ministers which signals the closing of a deal and the reporter does not say this, you’ll need to describe it in the transcript.

If your video is on YouTube, the transcript appears below the description of the video, where a “Show transcript” link appears’.

If your video is hosted outside of YouTube, make sure you provide the transcript in HTML and link to the transcript on the page the video is on.

Audio-only recordings, like podcasts, also need a transcript.

### Audio description

Audio description provides a spoken explanation of the visual elements in the video. 

Audio descriptions are essential for making video content accessible to people who are blind or visually impaired. They can also be helpful for people with cognitive disabilities.

Like with transcripts, if your video has visuals which are important in understanding the context, you’ll need to describe this verbally in the audio description.

>[!NOTE]
>Example
>
>If you show a user journey of a new service or product, you’ll need to describe the journey so everyone has access to the context.

You must make sure that any important information that affects people’s understanding of the video is explained verbally, not just through imagery.

### Videos with text only

If your video is text-based, you'll need to provide an alternative. You can add a voice-over or transcript. This will help users who may be unable to see the video or have issues with understanding content or language.

### Flashing images

You should not use flashing images in videos as they can trigger a seizure. 

Flashing refers to any large and bright content that flashes more than 3 times in one second. Users will not be able to switch off the flashing before it can trigger a seizure.

If it is not possible to edit out the flashing, you need to include a trigger warning on the page and in the video.

### Background audio

When your video is mainly speech, make sure you have either no or low background audio.

*[GDS]: Government Digital Service