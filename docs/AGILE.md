# Agile Development

This project was developed using agile principles. The project took 4 weeks and was divide up into weekly iterations/timeboxes, which roughly coincided with scheduled mentor sessions. In this way, development was iterative and incremental. The Minimum Viable Product (MVP) was deployed after the first iteration for mentor and peer feedback.

Story Points were assigned to tasks at the start of the project, and after deployment of the MVP a velocity could be calculated from the number of story points completed within that week. In this way, the remaining work could be better prioritized.

- Product Backlog Issues (PBI's) are categorised and labelled as **user stories** or **bugs**.
- PBI's are managed and refined using GitHub's built-in Project functionality. Milestones are used to create the iterations/timeboxes.
- User Stories were designated with Story Points, which are relative measures of how much work is required to complete a chunk of work.
- Story Point values conform to the Fibonacci sequence i.e. 1, 2, 3, 5 and 8. Anything larger was broken down into smaller chunks.
- A Kanban board was used as an Information Radiator, which was precise, accurate and updated coninuously.
- Each iteration aimed to have no more than 60% Must-Haves, 20% Should-haves, and 20% Could-haves, as shown below.

![sprint1](/docs/sprints/distributing-priorities.png)

## Sprint 1

Having created all user stories and added them to the backlog, I prioritized planning and admin tasks using MoSCoW categorization as follows:

![sprint1](/docs/sprints/sprint1.png)

The Kanban was tailored to visualise work in progress and to be 

### Sprint 1 plan

![sprint1_plan](/docs/sprints/sprint1_plan.png)

At the end of sprint 1 it was calculated that with 20 hours of work, 6 user story points were completed, giving a velocity of 6/20 = 0.3 pts/hr.

![sprint1_complete](/docs/sprints/sprint1_complete.png)

It was established that the story points for sprint 1 issues were underestimated.

### Minutes from Mentor Meeting 1

It was discussed at the mentor meeting that:

- A detailed user flow diagram could be deprioritized, as there was enough information on the wireframes to help build the project. Story points reduced from 2 to 1 due to some of the tasks within [user story #13](https://github.com/alanjameschapman/whiteboard/issues/13) being completed.
- Focus on making the site work for a single school initially, then broaden to multiple schools.
- Agreed that site could be split into two apps: **blog** and **profile**.
- Branching can be used per user story, but first branch named **MVP** because a lot of the user stories were interconnected and couldn't be completed in series.
- Summernote Rich Text Formatting (RTF) can be displayed on front-end form for post creation.
- Bringing functionality to the front end gives a better UX - credit will not be given to any work done on the admin panel.
- Automated testing not required, but manual testing must be exhaustive/detailed.
- Prioritisation plan for sprint2 reviewed and agreed.

## Sprint 2 - ends with Mentor Session 2 (Mid-Point Project Review)

Sprint 2 focused on creating a Minimum Viable Product for deployment on due date, where all merit criteria would be met. All user stories required for the MVP were added to this sprint.

### Sprint 2 plan

![sprint2_plan](/docs/sprints/sprint2_plan.png)

Based on time taken for the django blog walkthrough, it was anticipated that these issues could be accomplished within the timebox.

At the end of sprint 2 it was calculated that with 30 hours of work, 15 user story points were completed, giving a velocity of 15/30 = 0.5 pts/hr.

![sprint2_complete](/docs/sprints/sprint2_complete.png)

### Minutes from Mentor Meeting 2

- Confirmed that MVP has been achieved so can be posted on slack for peer review. Can add styling if desired, but not necessary for MVP.
- OK to distribute usernames and passwords for teacher1 and student1 but ensure peers can't log in to admin.
- Colour scheme reviewed. No problems envisaged with only  proposed colours but can use another 1 or 2 if struggling with visuals.
- Teachers can currently post for classes they don't teach but not deemed a problem and can investigate later if desired.
- Include Delete buttons on posts for teachers.
- Front-end approval needs getCookies function and csrf's etc.
- Problems with passwordReset discussed - to check django setup.
- Prioritisation plan for sprint3 reviewed and agreed.

## Sprint 3 - ends with Mentor Session 3 (Final Project Review)

It was deemed necessary that peers should be able to reset their password so this was the first priority alongside styling before posting for review:

### Sprint 3 plan

![sprint3_plan](/docs/sprints/sprint3_plan.png)

At the end of sprint 3, it was calculated that with 20 hours of work, 11 user story points were completed, giving a velocity of 11/20 = 0.55 pts/hr. NB. this doesn't account for [bug #39](https://github.com/alanjameschapman/whiteboard/issues/39) which took around 4 hours to resolve.

Any open issues were moved to the backlog and downgraded to could-haves. The only exception is [issue #40](https://github.com/alanjameschapman/whiteboard/issues/40) for implementing custom error pages.

![sprint3_complete](/docs/sprints/sprint3_complete.png)

### Minutes from Mentor Meeting 3

- Custom error pages could be resolved by adding 'handlers' to project urls.py
- Console errors on page load due to Cloudinary and can be fixed by a couple of lines in base.html 'head' section
- User groups could be implemented in admin panel so teachers can log in and have limited functionality such as creating sets and moderating comments
- Focus on post draft functionality, by either removing draft button from edit_post template or ensuring drafts appear frontend.

## Sprint 4 - ends with Submit Full Stack Toolkit Portfolio Project

Sprint 4 focused on completing the readme and testing documentation.

All actions from the previous mentor meeting were completed, except for custom error pages which were not deemed necessary because Django's default error pages are sufficient. This user story was moved to the backlog and left as a could-have.

| Project Sprints Summary | Future Implementation |
| :-: | :-: |
| ![project-complete](/docs/sprints/project-complete.png) | ![future-implementation](/docs/sprints/future-implementation.png) |