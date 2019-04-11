# Tagup data science challenge

## Getting started

You will need the following programs available:
- git
- python3
- [the AWS client](https://docs.aws.amazon.com/cli/latest/userguide/installing.html)
- [pipenv](https://docs.pipenv.org/install/)

In addition, you will need to 

1) [Set up an AWS account](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/)
2) Run "aws configure" at the command line. This will prompt you for several pieces of information related to your account; see [this link](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) for additional details.

Once all are properly installed and configured, you are ready to begin.  First,
fork this repository. Then run `make jupyter`; this will download the dataset,
install dependencies, and start a jupyter server in the current directory. It
should also open a browser tab to the jupyter interface. Open the data science
challenge notebook, and follow the instructions it contains. Those instructions
are repeated here for convenience.

## The data science challenge

ExampleCo, Inc has a problem: maintenance on their widgets is expensive. They
have contracted with Tagup to help them implement predictive maintenance. They
want us to provide a model that will allow them to prioritize maintenance for
those units most likely to fail, and in particular to gain some warning---even
just a few hours!---before a unit does fail.

They collect two kinds of data for each unit. First, they have a remote
monitoring system for the motors in each unit, which collects information about
the motor (rotation speed, voltage, current) as well as two temperature probes
(one on the motor and one at the inlet). Unfortunately, this system is
antiquated and prone to communication errors, which manifest as nonsense
measurements. Second, they have a rule-based alarming system, which can emit
either warnings or errors; the system is known to be noisy, but it's the best
they've got. 

They have given us just over 100MB of historical remote monitoring data from
twenty of their units that failed in the field. The shortest-lived units failed
after a few days; the longest-lived units failed after several years. Typical
lifetimes are on the order of a year. This data is available in .csv files
under `data/train` in this repository. In addition, they have provided us with
operating data from their thirty active units for the past month; this data is
available under `data/test` in this repository.

You have two main objectives. First, **tell us as much as you can about the
process that generated the data**. Does it show meaningful clustering? Do the
observations appear independent? How accurately can we forecast future
observations, and how long a window do we need to make an accurate forecast?
Feel free to propose multiple models, but be sure to discuss the ways each is
useful and the ways each is not useful. Second, **predict which of the thirty
active units are most likely to fail**. The data from these units are in
`data/test`. Be sure to quantify these predictions, and especially your
certainty.

A few notes to help:
1. A good place to start is by addressing the noise due to comm errors. 
2. There is a signal in the data that you can identify and exploit to predict
   failure. Each machine failed immediately after the last recorded timestamp 
   in the remote monitoring timeseries data.
4. If you can't find the signal in the noise, don't despair! We're much more
   interested in what you try and how you try it than in how successful you are
   at helping a fictional company with their fictional problems.
5. Feel free to use any libraries you like, or even other programming
   languages. Your final results should be presented in this notebook, however.
6. There are no constraints on the models or algorithms you can bring to bear.
   Some ideas include: unsupervised clustering algorithms such as k-means;
   hidden Markov models; forecasting models like ARMA; neural networks;
   survival models built using features extracted from the data; etc.
7. Don't feel compelled to use all the data if you're not sure how. Feel free
   to focus on data from a single unit if that makes it easier to get started.
8. Be sure to clearly articulate what you did, why you did it, and how the
   results should be interpreted. In particular you should be aware of the
   limitations of whatever approach or approaches you take.
9. Don't hesitate to reach out with any questions.
