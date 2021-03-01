
## The Exercise

ExampleCo, Inc is gathering several types of data for its fleet of very expensive machines. They collect four kinds of time series data for each machine in their fleet of very expensive machines. When a machine is operating in normal mode the data behaves in a fairly predictable way, but with a moderate amount of noise. Before a machine fails it will ramp into faulty mode, during which the data appears visibly quite different. Finally, when a machine fails it enters a third, and distinctly different, failed mode where all signals are very close to zero. There are three common sensors associated with each machine.

The company has contracted you to take their data extracts (linked below), map the data into your database, and summarize the results and process.

You can download the data here: [exampleco_data](https://drive.google.com/open?id=1b12u6rzkG1AxB6wLGl7IBVoaoSoZLHNR)

Your objectives:

-   Map the equipment data into a database of your choosing. You may define the schema however you think best suited to the data.
    
-   This should be scripted, i.e. you should write a script to map the CSV data (that would work on similar equipment data exports) into your database.
    

Bonus points:
    
-   Apply filters to clean the data. For example, there are some clear outliers in the data due to communication errors from the sensor equipment. These bad measurements have no bearing on the problem you’re trying to solve, and a good place to start is to find a way to filter them out.
    
-   Provide summary statistics for the ingressed data, including various statistical moments, and any other relevant descriptive statistics.
    
-   Demonstrate the efficacy of your approach using visualizations. You must also include a simple explanation of these figures and why your approach is effective, written in language that non-technical executives could understand.
    
-   Deploy your solution as a public API using an Amazon EC2 instance or similar.
    

A few notes to help:

1.  Feel free to use any libraries you like. Your final results should be shared via GitHub, including a README file providing documentation (ideally of both your code and your findings in the data).
    
2.  There are no constraints on the techniques you bring to bear, we are curious to see how you think and what sort of resources you have in your toolbox.
    
3.  Don't hesitate to reach out to jon@tagup.io with any questions!
    

## Tips

We value syntax, structure and variable naming, code documentation, and testability.

Try to design and implement your solution as you would do for real production code. Show us how you create clean and maintainable code that produces the target result. Build something that we'd be happy to contribute to.

Feel free to add more features: we're curious about what you can think of. We'd expect the same if you worked with us!

