# Tagup Data Science Exercise

## Getting Started

You will need the following programs available:

- git
- python3
- conda ([download/install conda](https://www.anaconda.com/distribution/))

Once these are properly installed and configured, you are ready to begin.  First, you will need to fork this repository, then,
1. run `conda create -n dschallenge python=3.6.9 numpy pandas scipy scikit-learn matplotlib pytest ipython jupyter`
2. run `conda activate dschallenge`
3. execute `jupyter notebook`
This will open a browser tab to the jupyter interface. Open the data science exercise notebook, and follow the instructions it contains. Those instructions are repeated below for convenience.

## The Exercise

ExampleCo, Inc is gathering several types of data for its fleet of very expensive machines.  These very expensive machines have three operating modes: *normal*, *faulty* and *failed*.   The machines run all the time, and usually they are in normal mode.  However, in the event that the machine enters faulty mode, the company would like to be aware of this as soon as possible.  This way they can take preventative action to avoid entering failed mode and hopefully save themselves lots of money.

They collect four kinds of timeseries data for each machine in their fleet of very expensive machines.  When a machine is operating in *normal* mode the data behaves in a fairly predictable way, but with a moderate amount of noise.  Before a machine fails it will ramp into *faulty* mode, during which the data appears visibly quite different.  Finally, when a machine fails it enters a third, and distinctly different, *failed* mode where all signals are very close to 0.

You can download the data here: [exampleco_data](https://drive.google.com/open?id=1b12u6rzkG1AxB6wLGl7IBVoaoSoZLHNR)

Your objectives:
- There are some clear outliers in the data due to communication errors from the sensor equipment. These bad measurements have no bearing on the problem you’re trying to solve, and a good place to start is to find a way to filter them out.
- Develop an approach to detect the beginning of the “faulty” period, ideally giving the ExampleCo engineers as much time as possible to shut down their machines before failure occurs (at which time all measurements drop close to 0). The best solutions are automated in the sense that they would generalize to similar but slightly different data; simpler methods are acceptable but are less likely to receive full credit.
- Demonstrate the efficacy of your approach using visualizations. You must also include a simple explanation of these figures and why your approach is effective, written in language that non-technical executives could understand.
- Finally, discuss the strengths and limitations of your approach (written for a technical audience), and be sure to mention other approaches that you would have liked to try if you had more time.

A few notes to help:
1. Feel free to use any libraries you like. Your final results should be 
   presented in this Python notebook.
2. There are no constraints on the techniques you bring to bear, we are curious
   to see how you think and what sort of resources you have in your toolbox.
3. Don't feel compelled to use all the data if you're not sure how. Feel free to 
   focus on data from a single unit, and use that as a jumping-off point to draw 
   inferences about the rest of the fleet.
4. Before submitting the challenge, make sure to run all cells so that the content 
   in the notebook can be evaluated without running any code. Failure to do so will 
   result in an automatic rejection.
5. Don't hesitate to reach out to datasciencejobs@tagup.io with any questions!
