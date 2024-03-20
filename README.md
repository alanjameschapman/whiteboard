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

![mvp](/docs/screenshots/mvp.png)

A review of [edublogs](https://edublogs.org/) which appears to be the dominant platform in educational blogs revealed a few additional features, which were not included in the scope of this project:
- Archive section of older posts
- Superuser customisation of page theme, layout, colours, widgets etc.

## Structure

[Lucidchart](https://www.lucidchart.com) was used to structure the site navigation as shown in the user flow diagram below. This was later developed into wireframes.

![user-flow](/docs/wireframes/user-flow.svg)

The Entity Relationship Diagram (ERD) below shows how the database models will relate to each other.

![ERD](/docs/ERD/whiteboard_ERD.png)

**One-to-many relationships:**

- A School has many Teachers and Students.
- A Teacher teaches many Sets.
- A Teachers or Student can make many Comments.
- A Subject is offered with many Sets.
- A Post can have many Comments.

**Many-to-many relationships:**

- Students can have many enrolments
- Teachers can teach multiple Subjects
- Comments can be made by either Students or Teachers on a Blog.

Note that a grade_level attribute was included in the Student entity in the event that the Homework functionality was implemented.

## Skeleton

[Balsamiq](https://balsamiq.com/) was used to create wireframes for the website.

![wireframes](/docs/wireframes/wireframes-user-journey.png)

A mobile-first approach was used, with subsequent wireframes for larger screens developed thereafter.

Testing of interface and navigation has been [documented](docs/TESTING.md).

## Surface

### Colour schemes

The colour scheme is based on the default image placeholder, which may be prevalent if the blog author doesn't customize their post image:

![default image](/static/images/default.jpg)

The dominant colour is yellow, which promotes [positivity, attention and creativity](https://blog.hope-education.co.uk/classroom-psychology-which-colours-are-best-for-education/) in the classroom.

The [Coolors image picker](https://coolors.co/image-picker) was used to generate a colour pallette based on the primary colour yellow. The [consensus](https://whitesharkmedia.com/blog/web-tracking/choose-the-best-color-palette-for-your-website/) for website colour palettes is that in addition to white, three colours should be used - primary, seconday and accent - in a ratio of 60:30:10.

The colour combination was regenerated until the three colours generated a positive response in the author and provided suitable contrast, which was checked using [eightshapes](https://eightshapes.com/).

![contrast](/docs/screenshots/contrast.png)

It was noted that the colours should be used as follows:
- Yellow: text on dark blue or background to dark blue.
- Light blue: text on dark blue or background to dark blue.
- Dark blue: text or background with any colour.

During development it was noted that it was easier to implementation dark blue and light blue as primary and secondary colours respectively. Yellow was therefore used to highlight calls-to-action such as buttons.

### Fonts

[iloveewp](https://www.ilovewp.com/resources/education/wordpress-for-schools/most-used-google-fonts-on-school-websites/) lists the "Most Used Google Fonts on School Websites". The top fonts were reviewed and Raleway was selected for its unique 'w' which would be used as the branding, navbar, footer and favicon to represent the 'w' in whiteboard:

[fontjoy](https://fontjoy.com/) was used to find suitable pairing fonts. Martel Sans was chosen because it has serif and sans-serif variants for headings and paragraphs respectively. Sans-serif was chosen because serifs can be difficult to read on screens.

![fonts](/docs/screenshots/fonts.png)

[favicon.io](https://favicon.io/favicon-generator/) was used to generate the favicon, based on the colour pallet.

![favicon](/docs/screenshots/favicon.png)

### Navigation

Infinite scroll of blog posts was discounted because it tends to be used for aimless browsing - our users will be looking for specific content. Last 9 posts should be enough to show, but not too many to overwhelm the user.

# Features

## Implemented

The website can only be accessed by registered users. The following features are available across the site:

### All Pages

#### Navbar

The navbar is present on all screens and is responsive to different screen sizes. It is not fixed to the top of the page because it is not necessary to be visible at all times.
To minimise user clicks, a 'burger bun' is not used because there is enough space to display the logo and links, even for mobile devices.

| Teacher | Student |
| :-: | :-: |
| ![navbar-teacher](/docs/features/navbar-teacher.png) | ![navbar-student](/docs/features/navbar-student.png) |

| Element | Description | Visibility |
| - | - | - |
| Logo | Link to the home page | Both
| Logout | Link to Logout confirmation screen | Both
| Post | Link to create new post | Teacher
| Django Message | Dismissable message confirming user action | Both |
| User status | Permanent message advising which user is logged in | Both |

#### Footer

The footer is applied to all screens and is responsive to different screen sizes. It is not fixed to the bottom of the page because it is not necessary to be visible at all times.

| Both Users |
| :-: |
| ![footer](/docs/features/footer.png) |

| Element | Description | Visibility |
| - | - | - |
| GitHub icon | Link to the author's GitHub profile | Both
| LinkedIn icon | Link to the author's LinkedIn profile | Both

### Register (register.html)

The register screen allows the user to register for the site. The user can enter their username, email and password, and click the register button.

| Both Users |
| :-: |
| ![register](/docs/features/register.png) |

| Element | Description | Visibility |
| - | - | - |
| Login link | Link to login | Both |
| Username | Input for username | Both |
| Email (optional) | Input for email | Both |
| Password | Input for password | Both |
| Password confirmation | Input for password confirmation | Both |
| Sign Up button | Link to sign up | Both |

### Login (login.html)

The login screen allows the user to log in to the site. The user can enter their username and password, and click the login button. The user can also click the register link to register for the site.

| Both Users |
| :-: |
| ![login](/docs/features/login.png) |

| Element | Description | Visibility |
| - | - | - |
| Register link | Link to register | Both |
| Username | Input for username | Both |
| Password | Input for password | Both |
| Login button | Link to login | Both |

### Home (index.html)

The home screen is the first screen the user sees when they log in. It displays the last 9 posts, with the most recent at the top. The user can click on the post to view the full content or click through to the next 9 posts.

For a teacher, it displays all published and draft posts they have created.

For a student, it displays only the published posts for the classes that the student has been enroled in.

| Teacher | Student |
| :-: | :-: |
| ![home-teacher](/docs/features/home-teacher.png) | ![home-student](/docs/features/home-student.png) |

| Element | Description | Visibility |
| - | - | - |
| Post card (published) | Summary of post | Both |
| Post card (draft) | Summary of post | Teacher |
| Post title | Title of post | Both |
| Post set | Set of post | Both |
| Post author | Author of post | Both |
| Post excerpt | Excerpt of post | Both |
| Post date | Date of post | Both |
| Pagination | Links to older posts | Both |

### Post Detail (post_detail.html)

The post detail screen displays the full content of the post. The user can comment on the post, and view approved comments made by other users. The teacher can edit or delete the post. The teacher can also approve comments made by students. Unapproved comments appear faded and student are marked as 'awaiting approval'.

| Teacher | Student |
| :-: | :-: |
| ![post-detail-teacher](/docs/features/post-detail-teacher.png) | ![post-detail-student](/docs/features/post-detail-student.png) |

| Element | Description | Visibility |
| - | - | - |
| Post title | Title of post | Both |
| Post set | Set of post | Both |
| Post author | Author of post | Both |
| Post content | Full content of post | Both |
| Edit post button | Link to edit post | Teacher |
| Delete post button | Link to delete post | Teacher |
| Comment count | Number of approved comments | Both |
| Comment card | All approved comments | Both |
| Comment form | Form to add a comment | Both |
| Edit comment button | Link to edit comment | Author |
| Delete comment button | Link to delete comment | Author |
| Approve comment button | Link to approve comment | Teacher |

### Post Create (post_create.html)

The post create screen allows the teacher to create a new post. The teacher can add a title, set, content and tags. The teacher can also save the post as a draft, or publish it immediately.

| Teacher |
| :-: |
| ![post-create](/docs/features/post-create.png) |

| Element | Description | Visibility |
| - | - | - |
| Post title | Title of post | Teacher |
| Post subject | Subject of post | Teacher
| Post set | Set of post | Teacher |
| Featured image | Retain default image or upload custom image | Teacher
| Post content | Full content of post | Teacher |
| Status | Set status of draft before submitting | Teacher
| Submit button | Submit post | Teacher
| Cancel button | Cancel post creation | Teacher

### Post Update (post_update.html)

The post update screen allows the teacher to update an existing post. The teacher can edit the title, set, content and tags. The teacher can also save the post as a draft, or publish it immediately.

| Teacher |
| :-: |
| ![post-update](/docs/features/post-update.png) |

| Element | Description | Visibility |
| - | - | - |
| Post title | Title of post | Teacher |
| Post subject | Subject of post | Teacher
| Post set | Set of post | Teacher |
| Featured image | Retain default image or upload custom image | Teacher
| Post content | Full content of post | Teacher |
| Status | Set status of draft before submitting | Teacher
| Submit button | Submit post | Teacher
| Cancel button | Cancel post creation | Teacher

### Post Confirm Delete (post_confirm_delete.html)

The post confirm delete screen allows the teacher to confirm they want to delete a post.

| Teacher |
| :-: |
| ![post-confirm-delete](/docs/features/post-confirm-delete.png) |

| Element | Description | Visibility |
| - | - | - |
| Delete button | Link to delete post | Teacher |
| Cancel button | Link to cancel delete and return to post | Teacher |


### Logout (logout.html)

The logout screen allows the user to log out of the site. The user can click the logout button to confirm they want to log out or click the whiteboard logo to return home.

| Both Users |
| :-: |
| ![logout](/docs/features/logout.png) |

| Element | Description | Visibility |
| - | - | - |
| Sign Out button | Link to logout | Both |

### Admin panel

The admin panel is accessible by superusers and teachers. The intention is that:
- the superuser (school admin/IT) will be responsible for creating teachers and students from the users registered on the site. Alternatively, the superuser could create the users directly and notify students of their login details, but this would require a secure method of communication.
- the teacher will be responsible for creating the sets and subjects that they teach, and enrolling students in their sets.

The admin panel has been customised by registering models via the admin.py and specifying displays, fields and filters among others. Furthermore, a teacher group has been created and assigned permissions to manage posts, comments, sets, subjects, students and enrolments.

| Superuser | Teacher |
| :-: | :-: |
| ![admin-panel-superuser](/docs/features/admin-panel-superuser.png) | ![admin-panel-teacher](/docs/features/admin-panel-teacher.png) |

## Not implemented...yet

| Issue# | User Story | Wireframe |
| :-: | - | :-: |
| [24](https://github.com/alanjameschapman/whiteboard/issues/24) | As a user I can search for content so that I can quickly find help on any given topic. | ![wireframe](/docs/features/search.png) |
| [14](https://github.com/alanjameschapman/whiteboard/issues/14) | As a teacher I can tag content so that I can enable students to search for a specific topic or skill | ![wireframe](/docs/features/tags.png) |
| [22](https://github.com/alanjameschapman/whiteboard/issues/22) | As a user I can bookmark topics so that I can quickly find saved content. | ![wireframe](/docs/features/bookmarks.png) |
| [2](https://github.com/alanjameschapman/whiteboard/issues/2) | As a teacher I can set quizzes so that I can assess my students' understanding. | ![wireframe](/docs/features/quiz-teacher.png) |
| [3](https://github.com/alanjameschapman/whiteboard/issues/3) | As a student I can answer quizzes so that I can get feedback on my understanding on a given topic. | ![wireframe](/docs/features/quiz-student.png) |
| [7](https://github.com/alanjameschapman/whiteboard/issues/7) | As a user I can reset my password so that I can access the site if I have forgotten my password. |  User clicks 'forgot password' button, then enters email, then receives email to reset password, then inputs new password (twice), then updates authentication details. |
| [41](https://github.com/alanjameschapman/whiteboard/issues/41) | As a teacher I can enrol student frontend so that I can provide content to relevant users. | ![wireframe](/docs/features/enrolment.png) |
| [6](https://github.com/alanjameschapman/whiteboard/issues/6) | As a user I can log in with email/socials so that I can access the site. |  User can select Google, Twitter or Facebook, then notified of login. |
| [20](https://github.com/alanjameschapman/whiteboard/issues/20) | As a user I can update my user profile so that I can personalise my UX. | ![wireframe](/docs/features/profile.png) |

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
- [Lucidchart](https://www.lucidchart.com) is a web-based diagramming tool used for creating flowcharts, process maps, wireframes, org charts, and other visual representations of ideas and concepts.
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
- [iloveewp](https://www.ilovewp.com/resources/education/wordpress-for-schools/most-used-google-fonts-on-school-websites/) as inspiration for commonly-used fonts in educational websites.
- [fontjoy](https://fontjoy.com/) for pairing fonts.
- [favicon.io](https://favicon.io/favicon-generator/) was used to generate the favicon.