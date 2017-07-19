import os
import twython
import nltk
import midiutil

APP_KEY=os.environ['APP_KEY']
APP_SECRET=os.environ['APP_SECRET']
authentication = twython.Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = authentication.obtain_access_token()
twitter = twython.Twython(APP_KEY, access_token=ACCESS_TOKEN)

def get_pos(text):
    tokens = nltk.word_tokenize(text)
    tagged_tokens = nltk.pos_tag(tokens)
    return tagged_tokens

def clean_tweet(pos):
    cleaned = []
    is_username = False
    for tag in pos:
        print tag
        #eliminate emojis and punctuation
        if '\u' not in tag[0].encode('unicode-escape') and '\U' not in tag[0].encode('unicode-escape') and '.' not in tag[1] and ',' not in tag[1] and ':' not in tag[1]:
            if '@' in tag[0]:
                #don't add the @ symbol on its own, add it to the username
                is_username = True
            else:
                #add an @ symbol to the username
                if is_username is True:
                    sss = '@' + tag[0]
                    new_tuple = (sss, tag[1])
                    tag = new_tuple
                cleaned.append(tag)
                is_username = False
    return cleaned

def compose_midi(tagged_text):
    track = 0
    channel = 0
    time = 0   # in beats
    duration = 1   # in beats
    tempo = 120  # beats per minute
    volume = 100 # from 0-127
    midi_file = midiutil.MIDIFile(1, adjust_origin=True)
    midi_file.addTempo(track, time, tempo)
    for tag in tagged_text:
        #print tag
        note = 0
        if 'NN' in tag[1]:
            note = 52
        elif 'VB' in tag[1]:
            note = 55
        else:
            note = 48
        midi_file.addNote(track, channel, note, time, duration, volume)
        time = time + 1
    return midi_file

def save_midi(cleaned_tweet, midi_file):
    filename = ''
    for tag in cleaned_tweet:
        filename += tag[0] + ' '
    filename = filename.strip() + '.mid'

    with open(filename, 'wb') as output_file:
        midi_file.writeFile(output_file)
        print 'midi file saved'

if __name__ == '__main__':
    tweets = twitter.search(q='from:@pentametron')
    for status in tweets['statuses'][2:4]:
        tweet = status['text'].split(':')[1]
        pos = get_pos(tweet)
        cleaned_tweet = clean_tweet(pos)
        midi_file = compose_midi(cleaned_tweet)
        save_midi(cleaned_tweet, midi_file)