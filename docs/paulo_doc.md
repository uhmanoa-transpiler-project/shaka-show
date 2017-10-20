# Paulo's Documentation

## Purpose

This document is used to retain text relating to every task that is completed as part of Shaka-Show. I am doing this to have text snippets to use for my 496 written report.

## Tasks

### Understand environment and how data is stored

Date: 10/20/2017
Expected DD: 2
Actual DD:

Troy explained how to VM currently works. He also took me through a small tour of the current Shaka-Scheme design. A decent portion of the work is very similar to last semester, so I have prior familiarity with the structure / design.
At the core, there are lists. Lists I believe are DataPairs, where the car is the first element of the list and the cdr is the rest.
DataPairs hold data. Data pairs are used in lists.
Data can hold the following:
String, Symbol, Boolean, DataPair, Number, Environment(?).

Environment:
The environment is pretty much a linked list of environments, where the current is the most local, and moving up parent environments eventually gets you to the global environment.
Environments are tables where a value is mapped to a key. In this case, the keys are symbols and the values are NodePtrs. I can navigate up through an environment, check if a key has a value in any environment, check if a key is in current environment, get and set values, and get keys.



### Render filename and Sourcecode of file to codetracker.html

Date: 9/24/2017
Expected DD: 2
Actual DD: 2

We figured out how to use Tornado templates. It took a while, because it is not as documented or as clean or trustworthy as Jinja2. We figured it out eventually, learning that to include a html file, we cannot use a python string. The only way to pass in the name of the file we want to include is through the "module" template function.
I wrote the handler that sets up a list of the panels we want to include, and then set up the panelargs dict that we use to pass information for each panel into its template renderer.

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

