Peace Corps Med Kit App

Demo Links:

[Jerey Sinefeld's Antartica Medkit](https://pcmedkit.appspot.com/ant/21036/status?k=agpzfnBjbWVka2l0cg4LEgZNZWRLaXQYrKQBDA)
MedKit Code: NZ-967-505

[Antartica Post Admin](https://pcmedkit.appspot.com/admin/ant)

To create your development server database navigate to the app root and run the following command (Replacing 'localhost:8080' with your dev server IP:PORT)

    appcfg.py upload_data --config_file=seed_data/bulkloader.yaml --filename=seed_data/DeliveryEvent.csv --kind=DeliveryEvent --url=http://localhost:8080/_ah/remote_api; \
    appcfg.py upload_data --config_file=seed_data/bulkloader.yaml --filename=seed_data/PostDefault.csv --kind=PostDefault --url=http://localhost:8080/_ah/remote_api; \
    appcfg.py upload_data --config_file=seed_data/bulkloader.yaml --filename=seed_data/Volunteer.csv --kind=Volunteer --url=http://localhost:8080/_ah/remote_api; \
    appcfg.py upload_data --config_file=seed_data/bulkloader.yaml --filename=seed_data/Supply.csv --kind=Supply --url=http://localhost:8080/_ah/remote_api
