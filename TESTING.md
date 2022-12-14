# Testing

To return to the readme click [here.](README.md)

## Code validation

### HTML validation

* Validation for the HTML can be found [here.](https://validator.w3.org)

    - Disclaimer: any warnings shown are to do with section elements not containing any h elements (e.g h1), this was brought up with my mentor and was deemed fine to submit.

    - Reviews page:
    ![html-reviews-validation](docs/testing/html-reviews-validation.png)

    - Games page:
    ![html-games-validation](docs/testing/html-games-validation.png)

    - Login page:
    ![html-login-validation](docs/testing/html-login-validation.png)

    - Register page:
    ![html-register-validation](docs/testing/html-register-validation.png)

    - Add review page:
    ![html-add-review-validation](docs/testing/html-add-review-validation.png)

    - Edit review page:
    ![html-edit-review-validation](docs/testing/html-edit-review-validation.png)

    - Add games page:
    ![html-add-game-validation](docs/testing/html-add-game-validation.png)

    - Edit games page:
    ![html-edit-game-validation](docs/testing/html-edit-game-validation.png)

### CSS validation

* Validation for the CSS can be found [here.](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fvideo-game-review-ms3.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

    - Note: Any errors/warnings that are shown is to do with Materialize. If the CSS code is entered via direct input, there will be no errors, as show below.

    ![css-validation](docs/testing/css-validation.png)

### JS validation

* Validation for the JS can be found [here.](https://jshint.com/)

![js-validation](docs/testing/js-validation.png)

### Python Validation

* Validation for the Python can be found [here.](http://pep8online.com/)

    - routes.py

    ![routes-py-validation](docs/testing/routes-py-validation.png)

    - models.py

    ![models-py-validation](docs/testing/models-py-validation.png)

    - init.py

    ![init-py-validation](docs/testing/init-py-validation.png)

    - run.py

    ![run-py-validation](docs/testing/run-py-validation.png)

## Defensive programming tests

* Making sure the user is logged in, in order to write a review:

    - If the user is logged in, clicking on the review button will direct the user to the "add review" page.

    ![login](docs/testing/add-review-page.png)

    - Otherwise, if the user is not logged in, a alert will flash, notifying the user they must log in to write a review.

    ![login_flash](docs/testing/login-flash.png)

* Notifying the user if their username and/or password is incorrect:

    - ![incorrect_login](docs/testing/incorrect-info.png)

* Notifying the user if the username they select is already taken:

    - ![username_taken](docs/testing/username-taken.png)

* User authentication:

    - The image below is the view from user 'johndoe's account, note the edit and delete buttons are only avaliable for the review user has created.

    ![review_page_user](docs/testing/reviews-page-user.png)

    - The image below is the view from an admins account, note that because the current session user is the admin, all edit and delete buttons are present on each review.

    ![review_page_admin](docs/testing/reviews-page-admin.png)

    - If the user is not the review author nor the admin, an alert flash will notify the user then are not permitted to edit the review.

    ![review_edit_alert](docs/testing/edit-review-flash.png)

* Admin permissions:

    - If the user is an admin, the site allows that user to manage the games, whether it be adding, editing or deleting them

    ![add_games](docs/testing/add-game-page.png)
    ![edit_games](docs/testing/edit-game-page.png)

    - Therefore, if the user is not admin, alerts will flash, notifying the user that they are not permitted to manage the games.

    ![add_games_alert](docs/testing/add-game-alert.png)
    ![edit_games_alert](docs/testing/edit-game-alert.png)


### Error handling

* Error: 404

![404_error](docs/testing/404-error.png)

* Error: 500

![500_error](docs/testing/500-error.png)

## Responsiveness

* The following images will showcase how the project is shown on different devices and shows the responsiveness of the project.

    - Mobile devices:

    ![mobile](docs/testing/mobile-view.png)

    - Tablet devices:

    ![tablet](docs/testing/tablet-view.png)

    - Desktop devices:

    ![desktop](docs/testing/reviews-page-admin.png)

## Browser Compatibility

* The following images shows the project being tested in both Chrome and Safari browsers.

    - Chrome

    ![chrome](docs/testing/chrome-test.png)

    - Safari

    ![safari](docs/testing/safari-test.png)


## User story testing

* I want to be able to register an account with the website to keep track of the reviews I have posted.

![register_page](docs/testing/register-page.png)

* I want to easily log into my already registered account.

![login_page](docs/testing/login-page.png)

* I want to easily log out of the account I am logged into, and be notified that I have successfully been logged out.

    - Once the user has successfully logged out, a message pops up, notifying the user they have logged out successfully.

    ![log_out_flash](docs/testing/log-out-flash.png)

* I would like to access the site easily on a mobile phone or tablet.

    - Mobile:

    ![mobile](docs/testing/mobile-view.png)

    - Tablet:

    ![tablet](docs/testing/tablet-view.png)

* I want to be able to check if there are any additional games that have been added.

![games_page](docs/testing/games-page-user.png)

* I would like to be able to edit the reviews I have created.

![edit_review](docs/testing/edit-review-page.png)

* I would like to be able to delete the reviews I have created.
* I would like the ability to delete any review for any reason deemed neccessary.
* I would like defensive programming to be in effect if I was to attempt to delete a review.
* I would like defensive programming to be in effect if I was to attempt to delete a game.
* I would want the deletion of a game to delete any reviews that is associated with said game.

    - Modals will be triggered if either a review or a game is attempted to be deleted by a user/admin.

    ![game_delete_modal](docs/testing/delete-game-modal.png)

    ![review_delete_modal](docs/testing/delete-review-modal.png)

* I would like the privilage of only the author and of the review to be able to edit their own review.

    - The image below is the view from user 'johndoe's account, note the edit and delete buttons are only avaliable for the review user has created:

    ![review_page_user](docs/testing/reviews-page-user.png)

    - The image below is the view from an admins account, note that because the current session user is the admin, all edit and delete buttons are present on each review:

    ![review_page_admin](docs/testing/reviews-page-admin.png)

![edit_review](docs/testing/edit-review-page.png)

* I would like to add and manage games that users are able to create a review for.

    - Add games:

    ![add_games](docs/testing/add-game-page.png)

    - Edit games:

    ![edit_games](docs/testing/edit-game-page.png)

* I would like to be able to visually be able to see what users have rated the games, using star icons.

    - Take not of the individual reviews star ratings above their review title.

    ![review_page_admin](docs/testing/reviews-page-admin.png)

## Environment testing

* The following images are within two seperate environments, they have different URLs to validate this.

### Local environment

* The images below show the game within the local (development) environment of gitpod.

![local_environment](docs/testing/local-env.png)

### Production environment

* The images below show the game within the production (deployed) environment of Heroku.

![production_environment](docs/testing/production-env.png)

## Bugs



### Unfixed bugs

* There are no unfixed bugs that I am currently aware of.