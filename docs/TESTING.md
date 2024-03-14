# Testing
## Manual Testing

User Stories were assessed and checked, categorised as superuser (headteacher/admin/IT dept), teacher and student, which are both a subset of a user.

These were tracked throughout the project as GitHub issues. Links are provided to see the development notes and screenshots for each.

| As a superuser I can... | ...so that I can... | Checked | Issue |
| - | - | :-: | :-: |
| manage available post fields | standardise and structure posts | &check;

| As a user I can... | ...so that I can... | Checked | Issue |
| - | - | :-: | :-: |
| view all posts summarized | browse topics | &check;

| As a teacher I can... | Checked | Issue |
| - | :-: | :-: |
| iew all posts summarized | &check;

| As a student I can... | Checked | Issue |
| - | :-: | :-: |
| View all posts summarized | &check;

Tables and screenshots of feature testing - Feature, Action and Effect. Expected outcome vs actual outcome.

### Responsiveness

The responsiveness to different screen sizes was checked throughout the project. Results for MVP and final site are shown below.

| Stage | iPhone 6/7/8 | iPad | Laptop
| :-: | :-: | :-: | :-: |
| MVP | ![MVPiPhone678](/docs/testing/response/MVP/iPhone678.png) | ![MVPiPad](/docs/testing/response/MVP/iPadAir.png) | ![MVPMacBookAir](/docs/testing/response/MVP/MacBookAir.png)
| Final | 

### Browser Compatibility

Browser compatibility was tested throughout the project as shown below. Using this [MDN guide](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Cross_browser_testing/Introduction) as a reference, the following was testing in each browser:
- Functionality, navigation and hyperlinks
- Responsiveness
- Aesthetics

| Stage | Chrome | Firefox | Safari
| :-: | :-: | :-: | :-: |
| MVP | &check; | &check; | &check; |
| Final | 

### Bugs
#### Resolved

| # | Problem | Screenshot | Solution | Screenshot |
| --- | --- | --- | --- | --- |
| [#29](https://github.com/alanjameschapman/whiteboard/issues/29) | Edit button not populating comment box for editing | ![#29](/docs/issues/29-1.png) | Javascript amended from "id_body" to "id_content | ![#29](/docs/issues/29-2.png) |
| [#30](https://github.com/alanjameschapman/whiteboard/issues/30) | New create_post template not rendering | <img width="638" alt="Screenshot 2024-03-06 at 10 04 01" src="https://github.com/alanjameschapman/whiteboard/assets/137620143/92e38f97-34e0-48dc-bbad-0bfbaf739215"> | Ordering of edblog/urls.py amended from most specific to least specific | <img width="638" alt="Screenshot 2024-03-06 at 10 04 47" src="https://github.com/alanjameschapman/whiteboard/assets/137620143/53372de8-e38c-4516-b7ab-4d9f4021fb5b"> |
| [#31](https://github.com/alanjameschapman/whiteboard/issues/31) | Duplicate titles cause IntegrityError | ![#31](/docs/issues/31-1.png) | Update create_post function in views | ![#31](/docs/issues/31-2.png) |
| [#37](https://github.com/alanjameschapman/whiteboard/issues/37) | crispy form not resizing to card | ![#37](/docs/issues/37-1.png) | Add SUMMERNOTE_CONFIG in settings.py | ![#37](/docs/issues/37-2.png) |
| [#38](https://github.com/alanjameschapman/whiteboard/issues/38) | Image upload not working | ![#38](/docs/issues/38-1.png) | Add form tag attribute in the HTML, which is necessary for file upload fields | ![#38](/docs/issues/38-2.png) |
| [#39](https://github.com/alanjameschapman/whiteboard/issues/39) | Index template : student1 is only enrolled in astrophysics Y1S1 but is also seeing posts for codebreaking Y1S1. | ![#39](/docs/issues/39-2.png) | Import Enrolment model and update queryset. | ![#39](/docs/issues/39-4.png) |


#### Unresolved

| # | Problem | Screenshot | Solution | Screenshot |
| --- | --- | --- | --- | --- |

### Lighthouse
WAVE and Web Disability Simulator. Disable extensions if they interfere. incognito mode?
### Code Validation
HTML - https://validator.w3.org/

CSS - https://jigsaw.w3.org/css-validator/

JavaScript - https://jshint.com/

Python - http://pep8online.com/


### Features

| Feature | Test | Outcome |
| - | - | - |
|

## Automated Testing
- [Jest JS](https://jestjs.io/) is a JavaScript Testing Framework with a focus on simplicity.
- [UnitTest](https://docs.python.org/3/library/unittest.html) comes standard with Python and is a testing framework.
