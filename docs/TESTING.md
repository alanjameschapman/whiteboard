# Testing
## Manual Testing

### User Stories

User Stories were assessed and categorised as either superuser (headteacher/admin/IT dept), teacher or user - the latter represents both teachers and students.

These were tracked throughout the project as [GitHub issues](https://github.com/users/alanjameschapman/projects/5). Links are provided to see the development notes and screenshots for each.

#### Users (Teachers and Students)

| As a user I can... | ...so that I can... | Checked | Issue# |
| :- | :- | :-: | :-: |
| view all posts summarized | browse topics | &check; | [23](https://github.com/alanjameschapman/whiteboard/issues/23) |
| register and log in/out with username and password | access the site | &check; | [4](https://github.com/alanjameschapman/whiteboard/issues/4) |
| comment on posts | ask questions to the teacher/student | &check; | [9](https://github.com/alanjameschapman/whiteboard/issues/9) |
| view comments on posts | see discussions relating to a specific post | &check; | [21](https://github.com/alanjameschapman/whiteboard/issues/21) |
| view post detail | read the content for a given topic | &check; | [27](https://github.com/alanjameschapman/whiteboard/issues/27) |
| edit or delete my comments | amend my comments | &check; | [28](https://github.com/alanjameschapman/whiteboard/issues/28) |
| reply to comments | engage in discussions | &check; | [26](https://github.com/alanjameschapman/whiteboard/issues/26) |

#### Teachers

| As a teacher I can... | ...so that I can... | Checked | Issue# |
| :- | :- | :-: | :-: |
| post content | provide information to students on a topic of my choice | &check; | [16](https://github.com/alanjameschapman/whiteboard/issues/16) |
| delete content | remove outdated or incorrect information | &check; | [18](https://github.com/alanjameschapman/whiteboard/issues/18) |
| update posts | correct or update information | &check; | [17](https://github.com/alanjameschapman/whiteboard/issues/17) |
| use Rich Text Formatting | create engaging content | &check; | [15](https://github.com/alanjameschapman/whiteboard/issues/15) |
| post draft content | complete the post at a later date | &check; | [19](https://github.com/alanjameschapman/whiteboard/issues/19) |
| moderate student comments | ensure appropriate content | &check; | [8](https://github.com/alanjameschapman/whiteboard/issues/8) |
| accept or deny requests from students | control which students can access/comment on my posts | &check; | [5](https://github.com/alanjameschapman/whiteboard/issues/5) |
| moderate comments frontend | speed up the comment approval process | &check; | [35](https://github.com/alanjameschapman/whiteboard/issues/35) |

#### Superusers

| As a superuser I can... | ...so that I can... | Checked | Issue# |
| :- | :- | :-: | :-: |
| manage available post fields | standardise and structure posts | &check; | [1](https://github.com/alanjameschapman/whiteboard/issues/1) |

### User Input Validation

User inputs were validated for various incorrect inputs throughout the project. Results for the final site are shown below.

| Page | Input | Test | Outcome | Screenshot | Pass |
| :-: | :-: | :-: | :-: | :-: | :-: |
| [register](https://whiteboard-app-742f545f1848.herokuapp.com/accounts/signup/) | username | no username | prompt to fill in field | ![register-nousername](/docs/testing/register-nousername.png) | &check; |
| [register](https://whiteboard-app-742f545f1848.herokuapp.com/accounts/signup/) | username | username already exists | prompt to choose another username | ![register-usernameexists](/docs/testing/register-usernameexists.png) | &check; |
| [register](https://whiteboard-app-742f545f1848.herokuapp.com/accounts/signup/) | email | bad email | prompt to enter a valid email | ![register-bademail](/docs/testing/register-bademail.png) | &check; |
| [register](https://whiteboard-app-742f545f1848.herokuapp.com/accounts/signup/) | password | no password | prompt to fill in field | ![register-nopassword](/docs/testing/register-nopassword.png) | &check; |
| [register](https://whiteboard-app-742f545f1848.herokuapp.com/accounts/signup/) | password | bad password | prompt to choose another password with criteria reiterated | ![register-badpassword](/docs/testing/register-badpassword.png) | &check; |
| [register](https://whiteboard-app-742f545f1848.herokuapp.com/accounts/signup/) | password | password mismatch | prompt to enter matching passwords | ![register-passwordmismatch](/docs/testing/register-passwordmismatch.png) | &check; |
| [login](https://whiteboard-app-742f545f1848.herokuapp.com/accounts/login/) | username | no username | prompt to fill in field | ![login-nousername](/docs/testing/login-nousername.png) | &check; |
| [login](https://whiteboard-app-742f545f1848.herokuapp.com/accounts/login/) | password | no password | prompt to fill in field | ![login-nopassword](/docs/testing/login-nopassword.png) | &check; |
| [create_post](https://whiteboard-app-742f545f1848.herokuapp.com/create_post/) | title | no title | prompt to fill in field | ![create_post-notitle](/docs/testing/create_post-notitle.png) | &check; |
| [create_post](https://whiteboard-app-742f545f1848.herokuapp.com/create_post/) | title | title already exists | prompt to choose another title | ![create_post-titleexists](/docs/testing/create_post-titleexists.png) | &check; |
| [create_post](https://whiteboard-app-742f545f1848.herokuapp.com/create_post/) | content | no content | prompt to fill in field | ![create_post-nocontent](/docs/testing/create_post-nocontent.png) | &check; |
| [create_post](https://whiteboard-app-742f545f1848.herokuapp.com/create_post/) | image | bad image | prompt to upload a valid image | ![create_post-badimage](/docs/testing/create_post-badimage.png) | &check; |

NB. the create_post form is the same as the edit_post form, so the same validation applies.

### Responsiveness

The responsiveness to different screen sizes was checked throughout the project. Results for MVP and final site are shown below, the main visual difference being fonts.

| Stage | iPhone 6/7/8 | iPad | Laptop
| :-: | :-: | :-: | :-: |
| MVP | ![mvpiphone678](/docs/testing/response/mvpiphone678.png) | ![mvpiad](/docs/testing/response/mvpipadair.png) | ![MVPMacBookAir](/docs/testing/response/mvpmacbookair.png)
| Final | ![finaliphone678](/docs/testing/response/finaliphone678.png) | ![finalipad](/docs/testing/response/finalipadair.png) | ![finalMacBookAir](/docs/testing/response/finalmacbookair.png)

### Browser Compatibility

Browser compatibility was tested throughout the project as shown below. Using this [MDN guide](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Cross_browser_testing/Introduction) as a reference, the following was testing in each browser:
- Functionality, navigation and hyperlinks
- Responsiveness
- Aesthetics

| Stage | Chrome | Firefox | Safari
| :-: | :-: | :-: | :-: |
| MVP | &check; | &check; | &check; |
| Final | &check; | &check; | &check; |

### Bugs

Bugs were tracked throughout the project as GitHub issues. Links are provided to see the development notes and screenshots for each.

#### Resolved

| Issue | Problem | Screenshot | Solution | Screenshot |
| :-: | :-: | :-: | :-: | :-: |
| [#29](https://github.com/alanjameschapman/whiteboard/issues/29) | Edit button not populating comment box for editing | ![#29](/docs/issues/29-1.png) | Javascript amended from "id_body" to "id_content | ![#29](/docs/issues/29-2.png) |
| [#30](https://github.com/alanjameschapman/whiteboard/issues/30) | New create_post template not rendering | <img width="638" alt="Screenshot 2024-03-06 at 10 04 01" src="https://github.com/alanjameschapman/whiteboard/assets/137620143/92e38f97-34e0-48dc-bbad-0bfbaf739215"> | Ordering of edblog/urls.py amended from most specific to least specific | <img width="638" alt="Screenshot 2024-03-06 at 10 04 47" src="https://github.com/alanjameschapman/whiteboard/assets/137620143/53372de8-e38c-4516-b7ab-4d9f4021fb5b"> |
| [#31](https://github.com/alanjameschapman/whiteboard/issues/31) | Duplicate titles cause IntegrityError | ![#31](/docs/issues/31-1.png) | Update create_post function in views | ![#31](/docs/issues/31-2.png) |
| [#37](https://github.com/alanjameschapman/whiteboard/issues/37) | crispy form not resizing to card | ![#37](/docs/issues/37-1.png) | Add SUMMERNOTE_CONFIG in settings.py | ![#37](/docs/issues/37-2.png) |
| [#38](https://github.com/alanjameschapman/whiteboard/issues/38) | Image upload not working | ![#38](/docs/issues/38-1.png) | Add form tag attribute in the HTML, which is necessary for file upload fields | ![#38](/docs/issues/38-2.png) |
| [#39](https://github.com/alanjameschapman/whiteboard/issues/39) | Index template : student1 is only enrolled in astrophysics Y1S1 but is also seeing posts for codebreaking Y1S1. | ![#39](/docs/issues/39-2.png) | Import Enrolment model and update queryset. | ![#39](/docs/issues/39-4.png) |
| [#42](https://github.com/alanjameschapman/whiteboard/issues/42) | "Mixed content" console error due to Cloudinary (http/https) on page load. | ![#42](/docs/issues/42-1.png) | Add meta to base.html to force https | ![#42](/docs/issues/42-2.png) |


#### Unresolved

The only unresolved bug is the password reset not working. This does not affect the website functionality because the admin can reset passwords manually.

| Issue# | Problem | Screenshot | Comment |
| :-: | :-: | :-: | :-: |
[36](https://github.com/alanjameschapman/whiteboard/issues/36) | password reset not working | ![#36](/docs/issues/36-1.png) | This bug and associated [Issue#7](https://github.com/alanjameschapman/whiteboard/issues/7) for password reset moved to backlog for future development. |

### Lighthouse

The WAVE Web Accessibility Evaluation Tool was used throughout the project to check for accessibility issues. Lighthouse was then used to test the performance, accessibility, best practices and SEO of the deployed site. The PWA score not showing is a [known feature](https://stackoverflow.com/questions/60603960/why-lighthouse-pwa-score-is-blank-even-though-the-page-is-audited).

Page | Mobile | Desktop | Comment |
| :-: | :-: | :-: | :-: |
| [register](https://whiteboard-app-742f545f1848.herokuapp.com/accounts/signup/) | ![register-mobile](/docs/testing/lighthouse/register-mobile.png) | ![register-desktop](/docs/testing/lighthouse/register-desktop.png) | None |
| [login](https://whiteboard-app-742f545f1848.herokuapp.com/accounts/login/) | ![login-mobile](/docs/testing/lighthouse/login-mobile.png) | ![login-desktop](/docs/testing/lighthouse/login-desktop.png) | None |
| [index](https://whiteboard-app-742f545f1848.herokuapp.com/) | ![index-mobile](/docs/testing/lighthouse/index-mobile.png) | ![index-desktop](/docs/testing/lighthouse/index-desktop.png) | Performance checked on mobile device - deemed acceptable |
| [post_detail](https://whiteboard-app-742f545f1848.herokuapp.com/post_detail/1/) | ![post_detail-mobile](/docs/testing/lighthouse/post_detail-mobile.png) | ![post_detail-desktop](/docs/testing/lighthouse/post_detail-desktop.png) | None |
| [create_post](https://whiteboard-app-742f545f1848.herokuapp.com/create_post/) | ![create_post-mobile](/docs/testing/lighthouse/create_post-mobile.png) | ![create_post-desktop](/docs/testing/lighthouse/create_post-desktop.png) | Performance checked on mobile and desktop - deemed acceptable |
| [edit_post](https://whiteboard-app-742f545f1848.herokuapp.com/edit_post/1/) | ![edit_post-mobile](/docs/testing/lighthouse/edit_post-mobile.png) | ![edit_post-desktop](/docs/testing/lighthouse/edit_post-desktop.png) | Performance checked on mobile and desktop - deemed acceptable |
| [post_confirm_delete](https://whiteboard-app-742f545f1848.herokuapp.com/post_confirm_delete/1/) | ![post_confirm_delete-mobile](/docs/testing/lighthouse/post_confirm_delete-mobile.png) | ![post_confirm_delete-desktop](/docs/testing/lighthouse/post_confirm_delete-desktop.png) | None |
| [logout](https://whiteboard-app-742f545f1848.herokuapp.com/accounts/logout/) | ![logout-mobile](/docs/testing/lighthouse/logout-mobile.png) | ![logout-desktop](/docs/testing/lighthouse/logout-desktop.png) | None |

### Code Validation

#### HTML

[W3C Markup Validation Service](https://validator.w3.org/) was used to validate the HTML. The Django template language cannot be validated by URI using the W3C validator, so the rendered HTML was copied and pasted into the direct input form for each page.

| Page | W3C URL | Screenshot | Notes | Pass |
| :-: | :-: | :-: | :-: | :-: |
| [register](/registration/signup.html) | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwhiteboard-app-742f545f1848.herokuapp.com%2Faccounts%2Fsignup%2F) | ![register](/docs/testing/register.png) | Errors relate to built-in Django form and don't affect UX or functionality. | &check; |
| [login](/registration/login.html) | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwhiteboard-app-742f545f1848.herokuapp.com%2Faccounts%2Flogin%2F) | ![login](/docs/testing/login.png) | Errors relate to built-in Django form and don't affect UX or functionality. | &check; |
 [index](/edblog/templates/edblog/index.html) | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwhiteboard-app-742f545f1848.herokuapp.com%2F) | ![index](/docs/testing/index.png) | None | &check; |
| [post_detail](/edblog/templates/edblog/post_detail.html) | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwhiteboard-app-742f545f1848.herokuapp.com%2Fpost_detail%2F1%2F) | ![post_detail](/docs/testing/post_detail.png) | None | &check; |
| [create_post](/edblog/templates/edblog/create_post.html) | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwhiteboard-app-742f545f1848.herokuapp.com%2Fcreate_post%2F) | ![create_post](/docs/testing/create_post.png) | Errors relate to built-in summernote widget and don't affect UX or functionality.  | &check; |
| [edit_post](/edblog/templates/edblog/edit_post.html) | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwhiteboard-app-742f545f1848.herokuapp.com%2Fedit_post%2F1%2F) | ![edit_post](/docs/testing/edit_post.png) | Errors relate to built-in summernote widget and don't affect UX or functionality. | &check; |
| [post_confirm_delete](/edblog/templates/edblog/post_confirm_delete.html) | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwhiteboard-app-742f545f1848.herokuapp.com%2Fpost_confirm_delete%2F1%2F) | ![post_confirm_delete](/docs/testing/post_confirm_delete.png) | None | &check; |


#### CSS

CSS was validated by direct input using [jigsaw W3C Validation Service](https://jigsaw.w3.org/css-validator/) and validates as CSS level 3 + SVG:

<p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="https://jigsaw.w3.org/css-validator/images/vcss-blue"
            alt="Valid CSS!"/>
    </a>
</p>

#### JavaScript

[jshint](https://jshint.com/) was used to validate the only custom JavaScript file, [comments.js](/staticfiles/js/comments.js), used to edit, delete and approve comments.

| File | Screenshot | Description | Pass |
| :-: | :-: | :-: | :-: |
| [comments](/staticfiles/js/comments.js) | ![comments.js](/docs/testing/comments-js.png) | One warning about a function 'getCookie' declared in a loop referencing an outer scoped variable. Reviewed but syntax deemed not difficult to understand. | &check; |

#### Python

[CI Python Linter](http://pep8online.com/) was used to validate the custom python files. No errors were found.

| File | Screenshot | Pass |
| :-: | :-: | :-: |
| [admin](/edblog/admin.py) | ![admin](/docs/testing/admin.png) | &check; |
| [forms](/edblog/forms.py) | ![forms](/docs/testing/forms.png) | &check; |
| [models](/edblog/models.py) | ![models](/docs/testing/models.png) | &check; |
| [urls](/edblog/urls.py) | ![urls-app](/docs/testing/urls-app.png) | &check; |
| [views](/edblog/views.py) | ![views](/docs/testing/views.png) | &check; |
| [urls-project](/whiteboard/urls-project.py) | ![urls-project](/docs/testing/urls-project.png) | &check; |
| [settings](/whiteboard/settings.py) | ![settings](/docs/testing/settings.png) | &check; |


## Automated Testing

Automated testing was not required for this project. However, the following frameworks could be used for future development:

- [Jest JS](https://jestjs.io/) is a JavaScript Testing Framework with a focus on simplicity.
- [UnitTest](https://docs.python.org/3/library/unittest.html) comes standard with Python and is a testing framework.
