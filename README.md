# Introduction 

Learning platform for teachers to post topic notes, tutorials and tests. Students can comment (ask questions) and teacher moderates.
Topics can be tagged with skills. Results can be filtered by tags.
GitHub's burger bun (top left) can be used to navigate to the desired section.

# Agile Development

This project was developed and [documented](docs/AGILE.md) using Agile principles.

# 5 planes of User Experience
The project was planned using the five planes of User Experience, as summarised below:

![UX5planes](/docs/screenshots/UX5planes.png)

## Strategy

In the author's experience (as a former Science teacher) classrooms can be hectic environments! There is a lot of content to teach, and limited time to cover it. Whilst teachers do their best to address misconceptions and questions of every student in the class, it is inevitable that some students may still leave the room with unanswered questions.

The goals this platform seeks to achieve are two-fold:
- For the TEACHER to provide topic content, address student questions, and hopefully set quizzes to test student knowledge and understanding.
- For the STUDENT to access relevant content (according to their teacher and class), and improve their understanding by asking questions (via comments) and completing quizzes.

User are divided into three main groups: Superuser, Teacher and Student. In the context of a school, the Superuser would likely be the headteacher, admin or IT department. For safeguarding reasons, they would be responsible for creating teachers logins, subjects and sets. They are also responsible for resetting passwords if required.

Their needs were defined as user stories and managed via GitHub Issues/Projects.

## Scope

Following an initial brainstorm of desired and possible functionality, a set of user stories was tabulated. These were grouped into Epics and Themes for Agile purposes, categorized using MoSCoW, and allocated Story Points. By assigning values 1, 2 and 3 to M, S and C respectively, and multiplying by the number of Story Points, functionality could be prioritized and the Minimum Viable Product (MVP) could be identified:

![MVP](/docs/screenshots/MVP.png)

A review of [edublogs](https://edublogs.org/) which appears to be the dominant platform in educational blogs revealed a few additional features, which were not included in the scope of this project:
- Archive section of older posts
- Superuser customisation of page theme, layout, colours, widgets etc.

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

Infinite scroll discounted because it tends to be used for aimless browsing - our users will be looking for specific content. Last 9 posts should be enough to show, but not too many to overwhelm the user.

### Colour schemes

The colour scheme is based on the default image placeholder, which may be prevalent if the blog author doesn't customize their post image:

![default image](/static/images/default.jpg)

The dominant colour is yellow, which promotes [positivity, attention and creativity](https://blog.hope-education.co.uk/classroom-psychology-which-colours-are-best-for-education/) in the classroom. This was chosen as the **primary colour**.

The [Coolors image picker](https://coolors.co/image-picker) was used to generate a colour pallette based on the primary colour yellow. The [consensus](https://whitesharkmedia.com/blog/web-tracking/choose-the-best-color-palette-for-your-website/) for website colour palettes is that in addition to white, three colours should be used - primary, seconday and accent - in a ratio of 60:30:10.

The colour combination was regenerated until the three colours generated a positive response in the author and provided suitable contrast, which was checked using [eightshapes](https://eightshapes.com/).

![contrast](/docs/screenshots/contrast.png)

It was noted that the colours should be used as follows:
- Yellow: text on dark blue or background to dark blue.
- Light blue: text on dark blue or background to dark blue.
- Dark blue: text or background with any colour.

### Fonts

# Features

## Implemented
- “if comment.author == request.user:” in view is used to check at the back-end for authorship.
- Use metadata for enhanced superuser UX in admin panel.
- Pros and cons of classes vs functions.

## Not implemented yet...

# Technologies

## Django customisations
- [Django](https://www.djangoproject.com/) is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- [Cloudinary](https://cloudinary.com/) is a cloud service that offers a solution to a web application's entire image management pipeline.
- [AllAuth](https://docs.allauth.org/) is a Django package that provides a set of views, templates, and helper functions to handle user authentication, registration, and account management..
- [Summernote](https://summernote.org/) is a simple WYSIWYG editor which allows you to embed Summernote into Django.
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/#) is a third-party Django app that helps you manage Django forms using Bootstrap styles.
- [gunicorn](https://gunicorn.org/) is a WSGI (Web Server Gateway Interface) HTTP server for running Python web applications. It acts as a bridge between the web application and the web server, handling requests and responses efficiently.
- [whitenoise](https://whitenoise.readthedocs.io/en/stable/index.html) is a Python library that simplifies serving static files in a Django web applications without relying on a separate web server.

## Other technologies
- [Balsamiq](https://balsamiq.com/) is a user interface design tool for creating wireframes.
- [Cascading Style Sheets)](https://www.w3.org/Style/CSS/Overview.en.html) (CSS) is a stylesheet language used to describe the presentation of a document written in HTML or XML.
- [Heroku](https://www.heroku.com/) is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
- [HTML](https://html.spec.whatwg.org/) is the standard markup language for documents designed to be displayed in a web browser.
- [JavaScript](https://www.javascript.com/) is a programming language that adds interactivity to your website.
- [Jest JS](https://jestjs.io/) is a JavaScript Testing Framework with a focus on simplicity.
- [PostgreSQL](https://www.postgresql.org/) is a powerful, open source object-relational database system.
- [Python](https://www.python.org/) is an interpreted, high-level and general-purpose programming language.
- [UnitTest](https://docs.python.org/3/library/unittest.html) comes standard with Python and is a testing framework.

# Testing

It was not necessary to complete both automated and manual testing, so the latter was completed and [documented](docs/TESTING.md) throughout. The following things were tested: responsiveness, browser compatibility, bugs, Lighthouse, code validation, user stories, features.

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
- [Classroom psychology: Which colours are best for education?](https://blog.hope-education.co.uk/classroom-psychology-which-colours-are-best-for-education/), Hope Education.
- [How to choose the best colour palette for your website](https://whitesharkmedia.com/blog/web-tracking/choose-the-best-color-palette-for-your-website/), White Shark Media
- [Eightshapes](https://eightshapes.com/)