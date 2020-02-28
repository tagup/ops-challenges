# Tagup data science exercise

## Getting started

You will need the following programs available:
- git
- python3

Once all are properly installed and configured, you are ready to begin.  First,
fork this repository. Then run `make jupyter`; this will download the dataset,
install dependencies, and start a jupyter server in the current directory. It
should also open a browser tab to the jupyter interface. Open the data science
challenge notebook, and follow the instructions it contains. Those instructions
are repeated here for convenience.

## The data science challenge

ExampleCo, Inc is gathering several types of data for one of its very expensive machines.  The very expensive machine has three operating modes: normal, fault and failure.  The machine runs all the time, and usually it is in normal mode.  However, in the event that the machine enters fault mode, the company would like to know as soon as possible.  This way they can take preventative action to avoid the failure and hopefully save themselves lots of money.

They collect four kinds of data on their very expensive machine.  When the machine is operating in normal mode the data behaves in a fairly predictable way, but with a moderate amount of noise.  Before the very expensive machine fails it will enter a fault mode, during which the data appears visibilty quite different.  Finally, when a machine fails it enters a third distinctly different mode.

The difficulty here is that while the modes do appear visibly different, the change in the operating modes is difficult to detect in any kind of automated way.  As the data scientist, it is your job to analyze some historical data from one fialure to determine exactly when the machine entered fault mode and when it entered faiure mode.

__Your main objective: to develop an automated method to pinpoint the times of fault and failure in this machine__.  Keep in mind that you will be sharing these results with the executives at ExampleCo, so to the best of your ability, try to explain what you are doing, what you've shown, and why you think your predictions are good.


A few notes to help:
1. Feel free to use any libraries you like, or even other programming
   languages. Your final results should be presented in this notebook, however.
2. There are no constraints on the techniques you bring to bear, we are curious
   to see how you think and what sort of resources you have in your toolbox.
3. Be sure to clearly articulate what you did, why you did it, and how the
   results should be interpreted. In particular you should be aware of the
   limitations of whatever approach or approaches you take.
4. Don't hesitate to reach out with any questions!
