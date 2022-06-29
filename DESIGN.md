# Design

## Database design

[dbdiagram.io](https://dbdiagram.io/) was used to create a database design diagram.

The diagram represents the basic structure of the database that will be used for the blog - i.e. how information will be stored, categorized and managed within it.
Each entity/table correlates to a key aspect of the blog that will need to be implemented in order for the blog to function as intended.

*Note: The data types specified here are SQL data types as opposed to their equivalent Django field types once modelled.*

![Database diagram markdown for 'Baked Beauties'](documentation/screenshots/evidence/design/database-design-markdown.png)
![Database diagram for 'Baked Beauties'](documentation/screenshots/evidence/design/database-design-diagram.png)

## Encapsulation

[Lucidchart](https://www.lucidchart.com/) was used to create a [Unified Modeling Language (UML)/class diagram](https://en.wikipedia.org/wiki/Unified_Modeling_Language) diagram as shown below, in order to model the various components of the blog and separate concerns.

![Class diagram for 'Baked Beauties'](documentation/screenshots/evidence/design/class-diagram.png)

## Wireframes

The wireframes for the chosen project idea were created digitally using Balsamiq and based around the [W3Schools Blog Template design](https://www.w3schools.com/bootstrap/tryit.asp?filename=trybs_temp_blog&stacked=h).

### Home page

![Wireframe of home page on desktop for regular user](documentation/wireframes/home-desktop.png)
*Note: Above image is the view for a regular user.*

![Wireframe of home page on desktop for admin user](documentation/wireframes/home-desktop-admin-view.png)
*Note: Above image is the view for an admin user (or logged in user, where the edit and delete icons would only appear on their own).*

![Wireframe of home page on mobile device in portrait mode](documentation/wireframes/home-mobile-portrait.png)
![Wireframe of home page on mobile device in landscape mode](documentation/wireframes/home-mobile-landscape.png)

### Full post view

![Wireframe of full post on desktop for regular user](documentation/wireframes/full-post-desktop.png)
![Wireframe of full post on mobile device in portrait mode](documentation/wireframes/full-post-mobile-portrait.png)
![Wireframe of full post on mobile device in landscape mode](documentation/wireframes/full-post-mobile-landscape.png)

### Recipes page

![Wireframe of recipes page on desktop for regular user](documentation/wireframes/recipes-desktop.png)
![Wireframe of recipes page on mobile device in portrait mode](documentation/wireframes/recipes-mobile-portrait.png)
![Wireframe of recipes page on mobile device in landscape mode](documentation/wireframes/recipes-mobile-landscape.png)

### Visuals page

![Wireframe of visuals page on desktop for regular user](documentation/wireframes/visuals-desktop.png)
![Wireframe of visuals page on mobile device in portrait mode](documentation/wireframes/visuals-mobile-portrait.png)
![Wireframe of visuals page on mobile device in landscape mode](documentation/wireframes/visuals-mobile-landscape.png)

### About page

![Wireframe of about page on desktop for regular user](documentation/wireframes/about-desktop.png)
![Wireframe of about page on mobile device in portrait mode](documentation/wireframes/about-mobile-portrait.png)
![Wireframe of about page on mobile device in landscape mode](documentation/wireframes/about-mobile-landscape.png)

### Contact page

![Wireframe of contact page on desktop for regular user](documentation/wireframes/contact-desktop.png)
![Wireframe of contact page on mobile device in portrait mode](documentation/wireframes/contact-mobile-portrait.png)
![Wireframe of contact page on mobile device in landscape mode](documentation/wireframes/contact-mobile-landscape.png)

### Login page

![Wireframe of login page on desktop for regular user](documentation/wireframes/login-desktop.png)
![Wireframe of login page on mobile device in portrait mode](documentation/wireframes/login-mobile-portrait.png)
![Wireframe of login page on mobile device in landscape mode](documentation/wireframes/login-mobile-landscape.png)

### Sign-up page

![Wireframe of sign-up page on desktop for regular user](documentation/wireframes/sign-up-desktop.png)
![Wireframe of sign-up page on mobile device in portrait mode](documentation/wireframes/sign-up-mobile-portrait.png)
![Wireframe of sign-up page on mobile device in landscape mode](documentation/wireframes/sign-up-mobile-landscape.png)

### User profile page

![Wireframe of user profile page on desktop for regular user](documentation/wireframes/profile-desktop.png)
![Wireframe of user profile page on mobile device in portrait mode](documentation/wireframes/profile-mobile-portrait.png)
![Wireframe of user profile page on mobile device in landscape mode](documentation/wireframes/profile-mobile-landscape.png)

### Stats page

![Wireframe of stats page on desktop for regular user](documentation/wireframes/stats-desktop.png)
![Wireframe of stats page on mobile device in portrait mode](documentation/wireframes/stats-mobile-portrait.png)
![Wireframe of stats page on mobile device in landscape mode](documentation/wireframes/stats-mobile-landscape.png)

## Typography

Google Fonts was used to find and select fonts for the site's typography.

[Lobster Two](https://fonts.google.com/specimen/Lobster+Two)' is used for headings and the navigation bar and footer text.
[Playfair Display](https://fonts.google.com/specimen/Playfair+Display)' is used for all other text.

![Google Fonts Lobster Two selection screenshot](documentation/screenshots/evidence/design/google-fonts-selection-1.png)
![Google Fonts Playfair Display selection screenshot](documentation/screenshots/evidence/design/google-fonts-selection-2.png)

## Colours

The site's colour scheme was chosen using the Adobe Color scheme extraction tool and a random image found from a Google search for 'cupcake'.

![Adobe Color scheme extraction tool screenshot](documentation/screenshots/evidence/design/colour-scheme.png)

## Coding practices

To ensure that the project code is up to standard, the following PEP rules were adhered to:

* [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/) - for best code style practices (i.e. layout, naming conventions, comments, etc.) and programming recommendations on function and variable annotations
* [PEP 257 -- Docstring Conventions](https://www.python.org/dev/peps/pep-0257/) - for general rules on docstrings
* [NumPy Style Guide](https://numpydoc.readthedocs.io/en/latest/format.html) - for a more detailed explanation of what goes where in docstrings, using [this](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html) specifically as an example to follow
* [PEP 3107 -- Function Annotations](https://www.python.org/dev/peps/pep-3107/) - for a specific way to specify function information and avoid confusion
* [PEP 484 -- Type Hints](https://www.python.org/dev/peps/pep-3107/) - also for purposes of clarity (although provisional)
* [PEP 526 -- Syntax for Variable Annotations](https://www.python.org/dev/peps/pep-0526/) - also for purposes of clarity

## Planning and execution

Agile practices were used to carry out this project and documented in Trello [planning/design board](https://trello.com/b/i7BTn4iC/project-planning-design) and [dev board](https://trello.com/b/wsBEYfJM/project-development) and [Github Projects](https://github.com/DebzDK/baked-beauties-blog/projects/1).

*Please note that more task details + resources are available in the Trello boards than in the Github Projects page.*

Each board is divided into 3 swimlanes/columns:
* 'To Do' - used to list tasks that are yet to be done
* 'In Progress' - used to list tasks that are currently being carried out
* 'Done' - used to list completed tasks

After defining the status divisions for a task, the indicators for time constraints were defined using 't-shirt sizes'.

![Card labels screenshot from Trello](documentation/screenshots/evidence/design/task-sizes-and-areas.png)

‘T-shirt sizes’ were defined to provide an estimate for the perceived difficulty of a task and extra labels to further separate tasks by what part of the process they’re related to, i.e. Requirements, Design, Development, and Testing.
The project area labels have been defined as follows:
* ‘Requirements’ - refers to things that are directly taken from or related to the project’s assessment criteria rather than actions derived from a requirements capture process
* 'Design' - refers to steps taken towards the appearance of the website
* 'Development' - refers to steps taken towards the implementation of the website
* 'Testing' - refers to steps taken towards validating the HTML and CSS as well as testing the responsiveness of the website

At this point, user stories were created in order to produce tasks while thinking from a user's perspective.

![Screenshot of first user story made in Trello](documentation/screenshots/evidence/design/first-user-story.png)

All other user stories follow the same kind of format except for where the user story is self-explanatory of the task.