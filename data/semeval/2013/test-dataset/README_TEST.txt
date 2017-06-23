TEST datasets for SemEval-2013 Task #2: Sentiment Analysis on Twitter

Task organizers:
Theresa Wilson   Johns Hopkins University, HLTCOE
Zornitsa Kozareva  University of Southern California, ISI
Preslav Nakov  Qatar Computing Research Institute, Qatar Foundation
Sara Rosenthal  Columbia University
Veselin Stoyanov Johns Hopkins University 
Alan Ritter  University of Washington


NOTE

Please note that by downloading the Twitter data you agree to abide
by the Twitter terms of service (https://twitter.com/tos),
and in particular you agree not to redistribute the data
and to delete tweets that are marked deleted in the future.
You MUST NOT re-distribute the tweets, the annotations or the corpus obtained,
as this violates the Twitter Terms of Use.


Version 1.1: July 16, 2013

Fixed release: March 10, 2014

SUMMARY

TASK A:
twitter-test-input-A.tsv -- test input for task A, Twitter messages
sms-test-input-A.tsv     -- test input for task A, SMS messages
twitter-test-gold-A.tsv  -- gold standard for task A, Twitter messages
sms-test-gold-A.tsv      -- gold standard for task A, SMS messages

TASK B:
twitter-test-input-B.tsv -- test input for task B, Twitter messages
sms-test-input-B.tsv     -- test input for task B, SMS messages
twitter-test-gold-B.tsv  -- gold standard for task B, Twitter messages
sms-test-gold-B.tsv      -- gold standard for task B, SMS messages


DOWNLOAD

The SMS data is ready to use, but the Twitter messages have to be downloada from Twitter.

The distribution consists of a set of twitter status IDs, with annotations.  
In order to address privacy concerns, rather than releasing the original Tweets, 
we are providing a python script that downloads the data.  This is similar 
to the mechanism for distributing Twitter data used in the TREC Microblog track.

The download script works for both tasks, and can be used like this:

    	easy_install beautifulsoup4
	python download_tweets.py input_file > output_file

Where the output file contains the text of the Tweets in addition to annotations.

In cases where the Tweet is no longer available, rather then including the text 
of the Tweet, the script outputs "Not Available".

Below we show the data format after the download.


INPUT DATA FORMAT

-----------------------TASK A-----------------------------------------
--Test Data--

The format for the test file is as follows:
id1<TAB>id2<TAB>start_token<TAB>end_token<TAB>unknwn<TAB>tweet_text

for example:
418381654813081609      15115101        2       2       unknwn  amoure wins oscar
418381654813081610      15115101        3       4       unknwn  who's a master brogramer now?

--System Output--
We expect the following format for the prediction file is:
id1<TAB>id2<TAB>start_token<TAB>end_token<TAB>pred_class<TAB>tweet_text

where the text field is optional. For example:
418381654813081609      15115101        2       2       positive  amoure wins oscar
418381654813081610      15115101        3       4       neutral  who's a master brogramer now?


--Gold Standard--
The gold standard following the same format as the system output above 

-----------------------TASK B-----------------------------------------
(Task B uses the same format as Task A, but it excludes the start and end token fields.)
--Test Data--

The format for the test file is as follows:
id1<TAB>id2<TAB>unknwn<TAB>tweet_text

for example:
418381654813081609      15115101       unknwn  amoure wins oscar
418381654813081610      15115101       unknwn  who's a master brogramer now?

--System Output--
We expect the following format for the prediction file is:
id1<TAB>id2<TAB>pred_class<TAB>tweet_text

where the text field is optional. For example:
418381654813081609      15115101        positive  amoure wins oscar
418381654813081610      15115101        neutral  who's a master brogramer now?


--Gold Standard--
The gold standard following the same format as the system output above 


EVALUATION

The evaluation metric is average F-measure (averaged F-positive and F-negative, and ignoring F-neutral; note that this does not make the task binary!), as well as F-measure for each class (positive, negative, neutral), which can be illuminating when comparing the performance of different systems.

See also the scorer for details on scoring the output.


DATASET USE

The development dataset is intended to be used as a development-time evaluation dataset as the participants develop their systems. However, the participants are free to use the dataset in any way they like, e.g., they can add it to their training dataset as well.

Participants should note that there are two test datasets, one composed of Twitter messages and another one composed of SMS messages, for which they have not received any explicit training data. The purpose of having a separate test set of SMS messages is to see how well systems trained on Twitter data can generalize to other types of message data.


ABOUT "OBJECTIVE"

Some of the datasets (e.g., the training dataset) contain "objective" labels, which the participants are free to use on training as they wish. However, we recommend that for task A these labels be ignored since there are no "objective" labels in the testing dataset. For task B, "objective" and "neutral" labels should be merged into "neutral"; the two labels are merged likewise for the test dataset. So, at test time, for both task A and task B, the systems have to predict just three labels: positive, negative and neutral. However, while for task A neutral means just "neutral", for task B, neutral means "neutral OR objective".

In this release, this is an issue for the training data only; we also provide a cleansed version of the training dataset.


USEFUL LINKS:

Google group: semevaltweet-2013@googlegroups.com
Task website: http://www.cs.york.ac.uk/semeval-2013/task2/
SemEval-2013 website: http://www.cs.york.ac.uk/semeval-2013/


NOTE: You can cite the folowing paper when referring to the dataset:

	SemEval'2013: SemEval-2013 Task 2: Sentiment Analysis in Twitter.
	Preslav Nakov, Sara Rosenthal, Zornitsa Kozareva,
	Veselin Stoyanov, Alan Ritter, Theresa Wilson
	http://www.aclweb.org/anthology/S/S13/S13-2052.pdf	


LICENSE

The accompanying dataset is released under a Creative Commons Attribution 3.0 Unported License
(http://creativecommons.org/licenses/by/3.0/).

