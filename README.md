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

User are divided into three main groups:
- Student: to learn using the website by accessing relevant content according to their teacher and class.
- Teacher: to teach using website by posting topic notes.
- Superuser: to set up schools, subjects and classes.

Their needs are defined and managed as user stories via GitHub Projects.

## Scope

Functional and content requirements HERE.

## Structure

User flow chart, ERD

## Skeleton

Wireframes HERE.

Testing of interface and navigation has been [documented](docs/TESTING.md).

## Surface

Colour schemes, go HERE.

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
