## Exercise 2.7: Data Analysis and Visualization in Django
### Learning Goals
- Work on elements of two-way communication like creating forms and buttons
- Implement search and visualization (reports/charts) features
- Use QuerySet API, DataFrames (with pandas), and plotting libraries (with matplotlib)

### Reflection Questions
1.	Consider your favorite website/application (you can also take CareerFoundry). Think about the various data that your favorite website/application collects. Write down how analyzing the collected data could help the website/application.

- I don't necessarily have a favorite website or application. However, if I use a social media site such as Twitter or Facebook, there are several areas in which data is collected and/or analyzed. One such example with Twitter is the `Trending` feature that takes either hashtags (`#`) or consistent keywords and provides those in a specific view or section on Twitter wherein users can see what things are currently being "discussed".

2.	Read the Django official documentation on QuerySet API. Note down the different ways in which you can evaluate a QuerySet.

- `.all()` - Retrieves all records from a specified object.
- `.filter()` - Narrows/filters results of a query from specified search criteria.
- `.exclude()` - Opposite of `filter`, omits results not matching specified criteria.

3.	In the Exercise, you converted your QuerySet to DataFrame. Now do some research on the advantages and disadvantages of QuerySet and DataFrame, and explain the ways in which DataFrame is better for data processing.

- QuerySets tends to be better suited for large data sets from databases as they don't require a lot of resources from systems (memory, processing, etc.). DataFrames provide agile functions for data manipulation, integration, and analysis.
