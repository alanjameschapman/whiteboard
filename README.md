# Introduction 
Learning platform for teachers to post topic notes, tutorials and tests. Students can comment (ask questions) and teacher moderates.
Topics can be tagged with skills. Results can be filtered by tags.
Please use GitHub's burger bun top left for auto-generated Table of Contents

# Agile Development
This project was developed and [documented](docs/AGILE.md) using Agile principles.

# 5 planes of User Experience
The project was planned using the five planes of User Experience:

![UX5planes](/docs/UX5planes.png)

## Strategy

In the author's experience (as a former Science teacher) classrooms can be hectic environments. There is a lot of content to cover, and limited time to learn it. Whilst teachers do their best to address the misconceptions and questions of every student in the class, it is inevitable that some may still leave the room with unanswered questions.

This platform seeks to provide the teacher a means to address these questions, clarify lesson content, and provide teachers the ability to give further reading or perhaps set homework.

User are divided into three main groups:
- Student: to learn using the website by accessing relevant content according to their teacher and class.
- Teacher: to teach using website by posting topic notes.
- Superuser: to set up schools, subjects and classes.

Their needs are defined and managed as user stories via GitHub Projects.

## Scope

Functional and content requirements HERE.

The dominant platform in educational blogs is [edublogs](https://edublogs.org/). 

## Structure

The following Entity Relationship Diagram (ERD) describes how the database models will relate to each other.

![ERD](/docs/ERD/whiteboard_ERD.png)

**One-to-many relationships:**

- A School has many Teachers, Students, and Sets.
- A Teacher teaches many Sets.
- A Subject is offered within many Sets.
- A Blog can have many Comments.

**Many-to-many relationships:**

- Students enroll in many Sets, and Sets have many Students (represented by the Enrollment entity).
- Comments can be made by either Students or Teachers on a Blog.

Note that for now a grade_level attribute has been included in the Student entity in the event that the Homework functionality is implemented. 

Some site navigation is shown in the wireframes, but 

User flow chart HERE

## Skeleton

![wireframes](/docs/wireframes/wireframes-user-journey.png)

Testing of interface and navigation has been [documented](docs/TESTING.md).

## Surface

Colour schemes, fonts go HERE.

# Features
## Implemented
- “if comment.author == request.user:” in view is used to check at the back-end for authorship.
- Use metadata for enhanced superuser UX in admin panel.
- Pros and cons of classes vs functions.
- AllAuth used because it is a widely-used and secure thingy with many advanced features, and is simpler to implement than by using Django (avoids having to write extra code, forms and permissions).
- Set Debug to True for development but False before deployment/submission

## Not implemented yet...

# Technologies
- [Django](https://www.djangoproject.com/) is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- [JavaScript](https://www.javascript.com/) is a programming language that adds interactivity to your website.
- [Cascading Style Sheets)](https://www.w3.org/Style/CSS/Overview.en.html) (CSS) is a stylesheet language used to describe the presentation of a document written in HTML or XML.
- [HTML](https://html.spec.whatwg.org/) is the standard markup language for documents designed to be displayed in a web browser.
- [Python](https://www.python.org/) is an interpreted, high-level and general-purpose programming language.
- [PostgreSQL](https://www.postgresql.org/) is a powerful, open source object-relational database system.
- [Cloudinary](https://cloudinary.com/) is a cloud service that offers a solution to a web application's entire image management pipeline.
- [Heroku](https://www.heroku.com/) is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
- [Jest JS](https://jestjs.io/) is a JavaScript Testing Framework with a focus on simplicity.
- [UnitTest](https://docs.python.org/3/library/unittest.html) comes standard with Python and is a testing framework.

# Testing

Manual and automated testing was completed and [documented](docs/TESTING.md) throughout.

# Deployment, Forking and Cloning

[Instructions](docs/DEPLOYMENT.md) are provided for deployment, forking and cloning.

# References
- [Portfolio Project 4: The guide to MVP](https://www.youtube.com/watch?v=vIv1c6RLBac), Code Institute LMS
- [PP4 - MVP & Community Walkthrough](https://app.box.com/s/s6xkp4gp3d9orwkp9fp4ep0igdcwsjm7), Code Institute LMS
- Django blog walkthrough, Code Institute LMS
- Principles of Agile Development, Code Institute LMS
- [The five elements of UX design & their common pitfalls](https://despark.com/blog/five-elements-ux-design-common-pitfalls), Despark.
- [How to Use the Fibonacci Scale to Estimate Story Points](https://www.scalablepath.com/project-management/agile-points-fibonacci-sequence), Scalable Path
