# Introduction
[The Peace Corps Med Kit App](https://pcmedkit.appspot.com) came about during the National Day of Civic Hacking on the weekend of Jun 1-2 2013.  The purpose of the app is to empower Volunteer and Medical Secretaries stationed across the globe to be more systematic about the way in which they manage supply requests for the standard issue Medical Kits.  Using the app, each MedKit would be issued a code through which they could log to request new items or check the status of previous requests.  Medical Secretaries or "Post Admin" log on to a similar dashboard to managing income and outgoing items, and update status.  

# Dependencies
The app uses the `webapp2` with [Google App Engine Python](https://developers.google.com/appengine/docs/python/) for its web framework, `jinja2` for templates and `WTForms` for form automation.  

# Demo
- [Jerey Sinefeld's Antartica Medkit (Code: NZ-967-505)](https://pcmedkit.appspot.com/ant/21036/status?k=agpzfnBjbWVka2l0cg4LEgZNZWRLaXQYrKQBDA)
- [Antartica Post Admin](https://pcmedkit.appspot.com/admin/ant)

# How to Contribute
There are a number of features that still need to be worked out.   If you are interested in contributing, first check out [our trello board](https://trello.com/board/pcmedkit/51b1135bc82e803239006ae4) where more details about each subsection of the app  are laid out in detail.  You can post a comment under the section you are interested in working on.  

# Getting Started
To create your development server database navigate to the app root and run the following command (Replacing 'localhost:8080' with your dev server IP:PORT)

    appcfg.py upload_data --config_file=seed_data/bulkloader.yaml --filename=seed_data/DeliveryEvent.csv --kind=DeliveryEvent --url=http://localhost:8080/_ah/remote_api; \
    appcfg.py upload_data --config_file=seed_data/bulkloader.yaml --filename=seed_data/PostDefault.csv --kind=PostDefault --url=http://localhost:8080/_ah/remote_api; \
    appcfg.py upload_data --config_file=seed_data/bulkloader.yaml --filename=seed_data/Volunteer.csv --kind=Volunteer --url=http://localhost:8080/_ah/remote_api; \
    appcfg.py upload_data --config_file=seed_data/bulkloader.yaml --filename=seed_data/Supply.csv --kind=Supply --url=http://localhost:8080/_ah/remote_api
