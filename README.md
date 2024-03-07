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

In the author's experience (as a former Science teacher) classrooms can be hectic environments! There is a lot of content to cover, and limited time to learn it. Whilst teachers do their best to address misconceptions and questions of every student in the class, it is inevitable that some students may still leave the room with unanswered questions.

The goals this platform seeks to achieve are two-fold:
- For the TEACHER to provide topic content, address student questions, and hopefully set quizzes.
- For the STUDENT to access relevant content (according to their teacher and class), and improve their understanding by asking questions (via comments) and completing quizzes.

User are divided into three main groups:
- Teacher: to teach using website by posting topic notes.
- Superuser: to set up schools, subjects and classes.

Their needs are defined and managed as user stories via GitHub Projects.

## Scope

Following an initial brainstorm of desired and possible functionality, a set of user stories was tabulated. These were grouped into Epics and Themes for Agile purposes,  categorized using MoSCoW, and allocated Story Points. By assigning values 1, 2 and 3 to M, S and C respectively, and multiplying by the number of Story Points, functionality could be prioritized and the Minimum Viable Product (MVP) could be identified:

![MVP](/docs/MVP.png)

A review of [edublogs](https://edublogs.org/) which appears to be the dominant platform in educational blogs revealed a few additional features . 

## Structure

The following Entity Relationship Diagram (ERD) describes how the database models will relate to each other.

![ERD](/docs/ERD/whiteboard_ERD.png)

**One-to-many relationships:**

- A School has many Teachers and Students.
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
- [Balsamiq](https://balsamiq.com/) is a user interface design tool for creating wireframes.
- [Cascading Style Sheets)](https://www.w3.org/Style/CSS/Overview.en.html) (CSS) is a stylesheet language used to describe the presentation of a document written in HTML or XML.
- [Cloudinary](https://cloudinary.com/) is a cloud service that offers a solution to a web application's entire image management pipeline.
- [Django](https://www.djangoproject.com/) is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- [Heroku](https://www.heroku.com/) is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
- [HTML](https://html.spec.whatwg.org/) is the standard markup language for documents designed to be displayed in a web browser.
- [JavaScript](https://www.javascript.com/) is a programming language that adds interactivity to your website.
- [Jest JS](https://jestjs.io/) is a JavaScript Testing Framework with a focus on simplicity.
- [PostgreSQL](https://www.postgresql.org/) is a powerful, open source object-relational database system.
- [Python](https://www.python.org/) is an interpreted, high-level and general-purpose programming language.
- [UnitTest](https://docs.python.org/3/library/unittest.html) comes standard with Python and is a testing framework.

# Testing

Manual and automated testing was completed and [documented](docs/TESTING.md) throughout.

# Deployment, Forking and Cloning

[Instructions](docs/DEPLOYMENT.md) are provided for deployment, forking and cloning.

# References
- [Portfolio Project 4: The guide to MVP](https://www.youtube.com/watch?v=vIv1c6RLBac), Code Institute LMS
- [PP4 - MVP & Community Walkthrough](https://app.box.com/s/s6xkp4gp3d9orwkp9fp4ep0igdcwsjm7), Code Institute LMS
- [ChatGPT](https://chat.openai.com/) for generating fixtures content during development.
- Django blog walkthrough, Code Institute LMS
- Principles of Agile Development, Code Institute LMS
- [The five elements of UX design & their common pitfalls](https://despark.com/blog/five-elements-ux-design-common-pitfalls), Despark.
- [How to Use the Fibonacci Scale to Estimate Story Points](https://www.scalablepath.com/project-management/agile-points-fibonacci-sequence), Scalable Path
