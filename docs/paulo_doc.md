# Paulo's Documentation

## Purpose

This document is used to retain text relating to every task that is completed as part of Shaka-Show. I am doing this to have text snippets to use for my 496 written report.

## Tasks

### Add JS libraries to static/dep for offline use

Date: 9/24/2017
Expected DD: 1
Actual DD: 0.5

I downloaded both jQuery and Underscore and added both js files to dep/js/ so we can use them offline for our web app. Shaka-Show does not require internet despite it being a web app, so now we can use these libraries no problem.
I learned a couple things while doing this:

I learned about \*.min.\* files, which are files that have been condensed or compiled into equivalent but much shorter files. This is very useful to reduce the amount of text that must be streamed over the internet for a website to use a library or code snippet.

I also heard about map files. I'm not sure what they are, but it looks from first impression like they assist with debugging or diagnostics.


### Add argParse contents to Web App settings

Date: 9/24/2017
Expected DD: 1
actual DD: 0.5

Using the arg\_parse function written by Jared, I modified the init\_settings function in our primary WebApp class to add the parsed args to the settings dict of the app. This allows us to access the settings content from any handler in the program.

