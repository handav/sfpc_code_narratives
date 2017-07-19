# Generating with Text: Text as Input

## Instructor: [Hannah Davis](https://www.hannahishere.com)


## Description: 

In this class, we'll look at unique ways to create generative projects with text, including extracting sentiment from text and using text to generate audio. We'll look at how to use standard tools like the NLTK as well as other APIs. We'll also talk about creating/curating text datasets and about the idea of "subjective datasets," and what that means for our practice. 


## Outline:

We'll start with a roughly 30-40 minute lecture. We'll talk in general about emotional data & sentiment analysis, data sonification (representing data through sound), and subjective datasets. I will show my work on using the texts of novels, debates, news articles, and country constitutions as inputs to generate music.

We'll use the remaining class time to create a read-only Twitter bot that reads tweets and generates audio based on the grammatical structure of the tweet. 

## More Resources:

Midi note numbers:
http://www.electronics.dit.ie/staff/tscarff/Music_technology/midi/midi_note_numbers_for_octaves.htm

MidiUtil documentation: 
https://media.readthedocs.org/pdf/midiutil/latest/midiutil.pdf

Setting up a Twitter application:
https://twython.readthedocs.io/en/latest/usage/starting_out.html#starting-out

Twitter bots in Node.js, including hosting:
https://github.com/handav/twitter-bots

Searching for tweets on Twitter:
https://dev.twitter.com/rest/public/search

## Python Audiobot Setup:

This audiobot requires four packages (you can use 'pip install package_name' or your installer of choice):

os (operating system, to access your environment variables)

twython (for interacting with the Twitter API)

nltk (for tagging text with parts of speech)

midiutil (for creating a midi file)

To run the program, navigate to the py_audiobot folder and type (into terminal): 'python main.py'

