# Introduction 
Learning platform for teachers to post topic notes, tutorials and tests. Students can comment (ask questions) and teacher moderates.
Topics can be tagged with skills. Results can be filtered by tags.
Please use GitHub's burger bun top left for auto-generated Table of Contents

# Agile Development
This project was developed using agile principles. The project took 4 weeks and was divide up into weekly iterations/timeboxes, which roughly coincided with scheduled mentor sessions. In this way, development was iterative and incremental. The Minimum Viable Product was deployed after the first iteration for mentor and peer feedback.
Story Points were assigned to tasks at the start of the project, and after deployment of the MVP a velocity could be calculated from the number of story points completed within that week. In this way, the remaining work could be better prioritized.

- Product Backlog Issues (PBI's) are categorised and labelled as user stories or bugs.
- PBI's are managed and refined using GitHub's built-in Project functionality. Milestones are used to create the iterations/timeboxes.
- Each iteration aimed to have no more than 60% Must-Haves, 20% Should-haves, and 20% Could-haves.
- User Stories were designated with Story Points, which are relative measures of how much work is required to complete a chunk of work.
- Story Point values conform to the Fibonacci sequence i.e. 1, 2, 3, 5 and 8. Anything larger was broken down into smaller chunks.

## Sprint 1 - ends with Mentor Session 1 (Project Planning)


## Sprint 2 - ends with Mentor Session 2 (Mid-Point Project Review)



## Sprint 3 - ends with Mentor Session 3 (Final Project Review)



## Sprint 4 - ends with Submit Full Stack Toolkit Portfolio Project



# User Experience Design
Wireframes, colour schemes, user flow chart go here
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
## Manual Testing
Tables and screenshots of user story testing

Tables and screenshots of feature testing - Feature, Action and Effect. Expected outcome vs actual outcome.

### Responsiveness
Use extension to show screens from each page at each iteration.
- Iteration 1
- Iteration 2
- Iteration 3
### Browser Compatibility
- Iteration 1
- Iteration 2
- Iteration 3
### Bugs
Problem -> solution. Include screenshots.
#### Resolved
#### Unresolved
### Lighthouse
WAVE and Web Disability Simulator. Disable extensions if they interfere. incognito mode?
### Code Validation
HTML - https://validator.w3.org/

CSS - https://jigsaw.w3.org/css-validator/

JavaScript - https://jshint.com/

Python - http://pep8online.com/
### User Stories
### Features
## Automated Testing
Jest and unittest.
# Deployment, Forking and Cloning

## Deployment

The live deployed application can be found at [link](https://link). [Heroku](https://www.heroku.com) is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key                     | Value                                                                |
| ----------------------- | -------------------------------------------------------------------- |
| `CLOUDINARY_URL`        | insert your own Cloudinary API key here                              |
| `DATABASE_URL`          | insert your own ElephantSQL database URL here                        |
| `DISABLE_COLLECTSTATIC` | 1 (_this is temporary, and can be removed for the final deployment_) |
| `SECRET_KEY`            | this can be any random secret key                                    |

Heroku needs two additional files in order to deploy properly.

- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `web: gunicorn app_name.wsgi > Procfile`
- _replace **app_name** with the name of your primary Django app name; the folder where settings.py is located_. In this case, that is `stackportfolio`.

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace _app_name_ with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
  - `git push heroku main`

The project should now be connected and deployed to Heroku!

### ElephantSQL Database

This project uses Code Institute's  Postgres Database for the PostgreSQL Database.

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For _Primary interest_, you can choose _Programmable Media for image and video API_.
- Optional: _edit your assigned cloud name to something more memorable_.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the _requirements.txt_ file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("CLOUDINARY_URL", "insert your own Cloudinary API key here")
os.environ.setdefault("DATABASE_URL", "insert your own ElephantSQL database URL here")
os.environ.setdefault("SECRET_KEY", "this can be any random secret key")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/alanjameschapman/whiteboard)
2. Locate the Code button above the list of files and click it
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:

- `git clone https://github.com/alanjameschapman/whiteboard.git`

7. Press Enter to create your local clone.

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/alanjameschapman/whiteboard)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!
# References
- PP4 MVP YouTube video.
- Code Institute Django blog walkthrough
- [PP4 - MVP & Community Walkthrough](https://app.box.com/s/s6xkp4gp3d9orwkp9fp4ep0igdcwsjm7)
- Principles of Agile Development, Code Institute LMS
- [Scalable Path](https://www.scalablepath.com/project-management/agile-points-fibonacci-sequence) for How to Use the Fibonacci Scale to Estimate Story Points.
