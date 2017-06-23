******************************************
* Semeval 2013 Task 2 Data
*
* http://www.cs.york.ac.uk/semeval-2013/task2/
* 
* Task Co-organizers:
* Theresa Wilson, Johns Hopkins University (taw@jhu.edu)
* Zornitsa Kozareva, Information Sciences Institute, University of Southern California (kozareva@isi.edu)
* Preslav Nakov, Qatar Computing Research Institute, Qatar Foundation (pnakov@qf.org.qa)
* Alan Ritter, University of Washington (aritter@cs.washington.edu)
* Sara Rosenthal, Columbia University (sara@cs.columbia.edu)
* Veselin Stoyanov, Johns Hopkins University (ves@cs.jhu.edu)
******************************************

The distribution consists of a set of twitter status IDs, with annotations.  
In order to address privacy concerns, rather than releasing the original Tweets, 
we are providing a python script that downloads the data.  This is similar 
to the mechanism for distributing Twitter data used in the TREC Microblog track.

The download script works for both tasks, and can be used like so:

    	easy_install beautifulsoup4
	python download_tweets.py input_file > output_file

Where the output file contains the text of the Tweets in addition to annotations.

In cases where the Tweet is no longer available, rather then including the text 
of the Tweet, the script outputs "Not Available".


The data is formatted as follows:

*** For task A:
<SID><tab><UID><tab><START_WORD_POSITION><tab><END_WORD_POSITION><tab><positive|negative|neutral|objective><tab><TWITTER_MESSAGE>

Example:
100032373000896513	15486118	14	14	positive	Wow!! Lady Gaga is actually at the Britney Spears Femme Fatale Concert tonight!!! She still listens to her music!!!! WOW!!!


*** For task B:
<SID><tab><UID><tab><TOPIC><tab><positive|negative|neutral|objective><tab><TWITTER_MESSAGE>

Example:
100032373000896513	15486118	lady gaga	"positive"	Wow!! Lady Gaga is actually at the Britney Spears Femme Fatale Concert tonight!!! She still listens to her music!!!! WOW!!!


For your reference, here are the task definitions:

Task A: Contextual Polarity Disambiguation
Given a message containing a marked instance of a word or phrase from a sentiment lexicon, determine whether that instance is positive, negative or neutral in that context.
 
Task B: Message Polarity Classification
Given a message, classify whether the message is of positive, negative, or neutral sentiment. For messages conveying both a positive and negative sentiment, whichever is the stronger sentiment should be chosen.
