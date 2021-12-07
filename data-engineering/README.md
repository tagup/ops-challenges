
## The Exercise

ExampleCo, Inc is gathering several types of data for its fleet of very expensive machines. They collect four kinds of time series data for each machine in their fleet. When a machine is operating in normal mode the data behaves in a fairly predictable way, but with a moderate amount of noise. Before a machine fails it will ramp into faulty mode, during which the data appears visibly quite different. Finally, when a machine fails it enters a third, and distinctly different, failed mode where all signals are very close to zero. There are four common sensors associated with each machine. There is also static data associated with each machine.

ExampleCo stores their data in SQL tables. While SQL is useful for storing and querying data, it is less useful as input for machine learning pipelines. At Tagup, our ML Pipelines expect data as a multi-dimensional array, and a common first step is converting a customer's data from SQL to array form.

You can download the data here: [exampleco_data](https://drive.google.com/file/d/1GejVDBoFFVNprqMeTGnXu8hrYLj4aS4q/view?usp=sharing)

Your main objectives are:

- Write a pipeline that reads the equipment data from the SQL database and transforms it into a single multi-dimensional array.
  - To keep things simple, you can ignore the static data to start.
  - Be sure to describe your design choices and explain the choices you made about the structure of the array(s).
- Apply filters to clean the data.
  - There are some clear outliers in the data due to communication errors from the sensor equipment. A good place to start is to find a way to filter them out.
- Explain why your design and approach is effective, in language a non-technical executive can understand.
  - It may be helpful to use visualizations to demonstrate the efficacy of your approach.

You can earn "bonus points" if you:
- Integrate the static data into your design.
- Provide summary statistics for the ingressed data, including various statistical moments, and any other relevant descriptive statistics.
- As part of your data processing pipeline, upload your arrays to AWS S3.

A few notes to help:
1. Feel free to use any libraries you like. At Tagup, we use [xarray](http://xarray.pydata.org/en/stable/) for multidimensional arrays, but you can use whatever methods you prefer. Your final results should be shared via GitHub, including a README file providing documentation (ideally of both your code and your findings in the data). There is a jupyter notebook included to help you get started, but do not feel obligated to submit your solution in notebook form.

2. There are no constraints on the techniques you bring to bear, we are curious to see how you think and what sort of resources you have in your toolbox.

3. Don't hesitate to reach out to challenges@tagup.io with any questions!


## Tips
- We value syntax, structure and variable naming, code documentation, and testability.
- Try to design and implement your solution as you would do for real production code. Show us how you create clean and maintainable code that produces the target result. Build something that we'd be happy to contribute to.
- Feel free to add more features: we're curious about what you can think of. We'd expect the same if you worked with us!
