# Introduction
[PC MedKit](https://pcmedkit.appspot.com) came about during the National Day of Civic Hacking (Jun 1-2 2013).  The purpose of the app is to empower Peace Corps Volunteers and Medical Secretaries more systematic about the way they manage requests for resupply in the field.  Using the app, each MedKit has a code and an associated account.  Volunteers log in to make resupply requests and Medical Secretaries or "Post Admin" log in  to manage incoming and outgoing items, and update status.  

# Dependencies
PCMedKit uses `webapp2` with [Google App Engine Python](https://developers.google.com/appengine/docs/python/) for its web framework, `jinja2` for templates and `WTForms` for form automation.  

# Demo
- [Jerey Sinefeld's Antartica Medkit (Code: NZ-967-505)](https://pcmedkit.appspot.com/ant/21036/status?k=agpzfnBjbWVka2l0cg4LEgZNZWRLaXQYrKQBDA)
- [Antartica Post Admin](https://pcmedkit.appspot.com/admin/ant)

# How to Contribute
There are a number of features that still need to be worked out.   If you are interested in contributing, check out [our trello board](https://trello.com/board/pcmedkit/51b1135bc82e803239006ae4) where details about each feature are laid out in detail.  You can post a comment under the feature or aspect you are interested in working on.  

# Getting Started
To create your development server database navigate to the app root and run the following command (Replacing 'localhost:8080' with your dev server IP:PORT)

    appcfg.py upload_data --config_file=seed_data/bulkloader.yaml --filename=seed_data/DeliveryEvent.csv --kind=DeliveryEvent --url=http://localhost:8080/_ah/remote_api; \
    appcfg.py upload_data --config_file=seed_data/bulkloader.yaml --filename=seed_data/PostDefault.csv --kind=PostDefault --url=http://localhost:8080/_ah/remote_api; \
    appcfg.py upload_data --config_file=seed_data/bulkloader.yaml --filename=seed_data/Volunteer.csv --kind=Volunteer --url=http://localhost:8080/_ah/remote_api; \
    appcfg.py upload_data --config_file=seed_data/bulkloader.yaml --filename=seed_data/Supply.csv --kind=Supply --url=http://localhost:8080/_ah/remote_api
