<<<<<<< HEAD
=======
# 6.00.1x Problem Set 7
>>>>>>> 595447144f6bca0ee61e60c1fb356dc9ac4de979
# RSS Feed Filter

import feedparser
import string
import time
from project_util import translate_html
from Tkinter import *


#-----------------------------------------------------------------------
<<<<<<< HEAD
=======
#
# Problem Set 7
>>>>>>> 595447144f6bca0ee61e60c1fb356dc9ac4de979

#======================
# Code for retrieving and parsing RSS feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret
#======================

#======================
# Part 1
# Data structure design
#======================

<<<<<<< HEAD
class NewsStory(object):
    def __init__(self, rss_guid, rss_title, rss_subject, rss_summary, rss_link):
        self.rss_guid = rss_guid
        self.rss_title = rss_title
        self.rss_subject = rss_subject
        self.rss_summary = rss_summary
        self.rss_link = rss_link

    def getGuid(self):
        # Getter method for a NewsStory object's rss guid.
        return self.rss_guid

    def getTitle(self):
        # Getter method for a NewsStory object's rss title.
        return self.rss_title

    def getSubject(self):
        # Getter method for a NewsStory object's rss subject.
        return self.rss_subject

    def getSummary(self):
        # Getter method for a NewsStory object's rss summary.
        return self.rss_summary

    def getLink(self):
        # Getter method for a NewsStory object's rss subject.
        return self.rss_link

=======
# Problem 1

class NewsStory(object):
    def __init__(self, guid, title, subject, summary, link):
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link

    def getGuid(self):
        return self.guid

    def getTitle(self):
        return self.title

    def getSubject(self):
        return self.subject

    def getSummary(self):
        return self.summary

    def getLink(self):
        return self.link
>>>>>>> 595447144f6bca0ee61e60c1fb356dc9ac4de979

#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
<<<<<<< HEAD

class WordTrigger(Trigger):

    def __init__(self, word):
        self.word = word

    def isWordIn(self, text):

        # Deals with apostrophe problem
        rss_text = text.replace("'", " ")

        # Strips punctuation from text 
        rss_text = rss_text.translate(None,string.punctuation)

        # Change text and trigger word to lower case
        rss_text = rss_text.lower()
        word_lower = self.word.lower()

        # Split text into list of strings
        rss_text = rss_text.split()

        # Search for word in parsed version of text
        for text_word in rss_text:
            if text_word == word_lower:
                return True

        return False

class TitleTrigger(WordTrigger):

=======
# Problems 2-5

class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word.lower()

    def isWordIn(self, text):
        text = text.lower()
        for char in string.punctuation:
            text = text.replace(char, " ")
        tmp = text.split(" ")
        if self.word in tmp:
            return True
        else:
            return False

class TitleTrigger(WordTrigger):
>>>>>>> 595447144f6bca0ee61e60c1fb356dc9ac4de979
    def evaluate(self, story):
        return self.isWordIn(story.getTitle())

class SubjectTrigger(WordTrigger):
<<<<<<< HEAD

=======
>>>>>>> 595447144f6bca0ee61e60c1fb356dc9ac4de979
    def evaluate(self, story):
        return self.isWordIn(story.getSubject())

class SummaryTrigger(WordTrigger):
<<<<<<< HEAD

=======
>>>>>>> 595447144f6bca0ee61e60c1fb356dc9ac4de979
    def evaluate(self, story):
        return self.isWordIn(story.getSummary())

# Composite Triggers
<<<<<<< HEAD

class NotTrigger(Trigger):

=======
# Problems 6-8

class NotTrigger(Trigger):
>>>>>>> 595447144f6bca0ee61e60c1fb356dc9ac4de979
    def __init__(self, trigger):
        self.trigger = trigger

    def evaluate(self, story):
        return not self.trigger.evaluate(story)

class AndTrigger(Trigger):
<<<<<<< HEAD

    def __init__(self, *trigger):
        self.trigger = trigger

    def evaluate(self, story):
        triggerList = []
        for t in self.trigger:
            triggerList.append(t.evaluate(story))
        return all(triggerList)

class OrTrigger(Trigger):

    def __init__(self, *trigger):
        self.trigger = trigger

    def evaluate(self, story):
        triggerList = []
        for t in self.trigger:
            triggerList.append(t.evaluate(story))
        return any(triggerList)

# Phrase Trigger

class PhraseTrigger(Trigger):

    def __init__(self,phrase):
        self.phrase = phrase

    def evaluate(self, story):
        return self.phrase in story.getSummary() or \
               self.phrase in story.getTitle() or \
               self.phrase in story.getSubject()
=======
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        if self.trigger1.evaluate(story) and \
            self.trigger2.evaluate(story):
            return True
        else:
            return False

class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        if self.trigger1.evaluate(story) or \
            self.trigger2.evaluate(story):
            return True
        else:
            return False


# Phrase Trigger
# Question 9

class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase

    def evaluate(self, story):
        if self.phrase in story.getTitle() or \
            self.phrase in story.getSubject() or \
            self.phrase in story.getSummary():
            return True
        else:
            return False

>>>>>>> 595447144f6bca0ee61e60c1fb356dc9ac4de979

#======================
# Part 3
# Filtering
#======================

def filterStories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
<<<<<<< HEAD
    # TODO: Problem 10
    # This is a placeholder (we're just returning all the stories, with no filtering)
    
    filteredStories = []

    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                filteredStories.append(story)
                break

    return filteredStories
=======
    tmp = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story) and not story in tmp:
                tmp.append(story)
    return tmp
>>>>>>> 595447144f6bca0ee61e60c1fb356dc9ac4de979

#======================
# Part 4
# User-Specified Triggers
#======================

def makeTrigger(triggerMap, triggerType, params, name):
    """
    Takes in a map of names to trigger instance, the type of trigger to make,
    and the list of parameters to the constructor, and adds a new trigger
    to the trigger map dictionary.

    triggerMap: dictionary with names as keys (strings) and triggers as values
    triggerType: string indicating the type of trigger to make (ex: "TITLE")
    params: list of strings with the inputs to the trigger constructor (ex: ["world"])
    name: a string representing the name of the new trigger (ex: "t1")

    Modifies triggerMap, adding a new key-value pair for this trigger.

    Returns a new instance of a trigger (ex: TitleTrigger, AndTrigger).
    """
<<<<<<< HEAD
    # TODO: Problem 11
    
    triggerType=triggerType.upper()

    if triggerType=='TITLE':
        triggerMap[name] = TitleTrigger(params[0])

    elif triggerType=='SUBJECT':
        triggerMap[name] = SubjectTrigger(params[0])

    elif triggerType=='SUMMARY':
        triggerMap[name] = SummaryTrigger(params[0])

    elif triggerType=='NOT':
        triggerMap[name] = NotTrigger(triggerMap[params[0]])

    elif triggerType=='AND':
        triggerMap[name] = AndTrigger(triggerMap[params[0]], triggerMap[params[1]])

    elif triggerType=='OR':
        triggerMap[name] = OrTrigger(triggerMap[params[0]], triggerMap[params[1]])

    elif triggerType=='PHRASE':
        triggerMap[name] = PhraseTrigger(' '.join(params))

    return triggerMap[name]
=======
    if triggerType == "TITLE":
        triggerMap[name] = TitleTrigger(" ".join(params))
        return triggerMap[name]
    elif triggerType == "SUBJECT":
        triggerMap[name] = SubjectTrigger(" ".join(params))
        return triggerMap[name]
    elif triggerType == "SUMMARY":
        triggerMap[name] = SummaryTrigger(" ".join(params))
        return triggerMap[name]
    elif triggerType == "NOT":
        triggerMap[name] = NotTrigger(triggerMap[params[0]])
        return triggerMap[name]
    elif triggerType == "AND":
        triggerMap[name] = AndTrigger(triggerMap[params[0]], \
            triggerMap[params[1]])
        return triggerMap[name]
    elif triggerType == "OR":
        triggerMap[name] = OrTrigger(triggerMap[params[0]], \
            triggerMap[params[1]])
        return triggerMap[name]
    elif triggerType == "PHRASE":
        triggerMap[name] = PhraseTrigger(" ".join(params))
        return triggerMap[name]
>>>>>>> 595447144f6bca0ee61e60c1fb356dc9ac4de979

def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """

    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    triggers = []
    triggerMap = {}

    # Be sure you understand this code - we've written it for you,
    # but it's code you should be able to write yourself
    for line in lines:

        linesplit = line.split(" ")

        # Making a new trigger
        if linesplit[0] != "ADD":
            trigger = makeTrigger(triggerMap, linesplit[1],
                                  linesplit[2:], linesplit[0])

        # Add the triggers to the list
        else:
            for name in linesplit[1:]:
                triggers.append(triggerMap[name])

    return triggers
<<<<<<< HEAD
    
=======

>>>>>>> 595447144f6bca0ee61e60c1fb356dc9ac4de979
import thread

SLEEPTIME = 60 #seconds -- how often we poll


def main_thread(master):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    try:
        # These will probably generate a few hits...
        t1 = TitleTrigger("Obama")
        t2 = SubjectTrigger("Romney")
        t3 = PhraseTrigger("Election")
        t4 = OrTrigger(t2, t3)
        triggerlist = [t1, t4]
<<<<<<< HEAD
        
        # TODO: Problem 11
        # After implementing makeTrigger, uncomment the line below:
        triggerlist = readTriggerConfig("C:/Users/Apache/Documents/GitHub/EdX/6.00.1x/Projects/ProblemSet7/triggers.txt")
=======

        # TODO: Problem 11
        # After implementing makeTrigger, uncomment the line below:
        # triggerlist = readTriggerConfig("triggers.txt")
>>>>>>> 595447144f6bca0ee61e60c1fb356dc9ac4de979

        # **** from here down is about drawing ****
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)
<<<<<<< HEAD
        
=======

>>>>>>> 595447144f6bca0ee61e60c1fb356dc9ac4de979
        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)

        # Gather stories
        guidShown = []
        def get_cont(newstory):
            if newstory.getGuid() not in guidShown:
                cont.insert(END, newstory.getTitle()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.getSummary())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.getGuid())

        while True:

            print "Polling . . .",
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

            # Process the stories
            stories = filterStories(stories, triggerlist)

            map(get_cont, stories)
            scrollbar.config(command=cont.yview)


            print "Sleeping..."
            time.sleep(SLEEPTIME)

    except Exception as e:
        print e


if __name__ == '__main__':

    root = Tk()
    root.title("Some RSS parser")
    thread.start_new_thread(main_thread, (root,))
    root.mainloop()

