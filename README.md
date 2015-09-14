## Introduction
This repository is for the final project on [Text Mining](http://www.cs.virginia.edu/~hw5x/Course/Text-Mining-2015-Spring/_site/)(CS 6501). In this project, we propose a system called Question Recommendation System (QRS) with which users could input a new question, they would get a list of existing questions that may already have good answers. The way to get those questions is to mine the existing similar questions and related answers, from an online community environment. 

In our system, we offer users a short-cut of a faster and more straightforward way of getting the information they desire, without necessarily digging into large data set. The common community Q&A sites would simply match the newly submitted query with existing questions. 

## Project Highlights
Our comparison implementation is the question recommendation on StackOverflow. We have three major improvements.

1. When user hover the recommended questions, the question overview will be given in Stackoverflow system. What we do is to offer the overview of answer with the highest upvotes. In that case, people may not need open the answer page and can judge it quickly, or even get what they want. And also our preview page(by using stackoverflow API) is way faster than stackover implementation.

2. In StackOverflow system, they would show the number of answers and the number of upvotes for question in preview. However, it misses a very important question quality indicator which is the highest number of upvotes for that answer. 

3. Our search function is supported by Apache Solr, in which the search results consider both question titles and tags. Since stackoverflow is not open source, so we can't do a comparsion here.

In summary, we have developed a user-friendly question recommendation system based on Apache Solr. We believe our evaluation shows our system outperform the existing question recommendation system on Stack Overflow at least in terms of user experience. :)

For more details, please review our [final report](https://github.com/haoyuchen1992/StackOverFlow-Question-Search/blob/master/Project-Docs/question-recommendation-system.pdf)   
Our demo website is [here](https://stackoverflow-search.appspot.com/)

## Implementation Techniques
1. Search Server -- [Amaonz EC2](https://aws.amazon.com/ec2/)
2. Search -- [Apache Solr](http://lucene.apache.org/solr/)
3. Website Server -- [Google App Engine](https://cloud.google.com/appengine/docs)
