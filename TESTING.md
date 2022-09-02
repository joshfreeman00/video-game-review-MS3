# Testing

To return to the readme click [here.](README.md)

## Code validation

### HTML validation

* Validation for the HTML can be found [here.](https://validator.w3.org/nu/?doc=https%3A%2F%2Fvideo-game-review-ms3.herokuapp.com%2F)

![css-validation](docs/testing/html-validation.png)

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

## Responsiveness

* The following images will showcase how the project is shown on different devices and shows the responsiveness of the project.

    - Mobile devices:

    ![mobile](*)

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

* I want to understand the context of the website.

-

* I want to be able to register an account with the website to keep track of the reviews I have posted.

![register_page](docs/testing/register-page.png)

* I want to easily log into my already registered account.

![login_page](docs/testing/login-page.png)

* I want to easily log out of the account I am logged into, and be notified that I have successfully been logged out.

    - Once the user has successfully logged out, a message pops up, notifying the user they have logged out successfully.

    ![log_out_flash](docs/testing/log-out-flash.png)

* I would like to access the site easily on a mobile phone or tablet.

    - Mobile:

    ![mobile](*)

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

    - The image below is the view from an admins account, note that because the current session user is the admin, all edit and delte buttons are present on each review:

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