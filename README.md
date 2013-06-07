Peace Corps Med Kit App

To create your development server database navigate to the app root and run the following command (Replacing 'localhost:8080' with your dev server IP:PORT)

    appcfg.py upload_data --config_file=seed_data/bulkloader.yaml --filename=seed_data/DeliveryEvent.csv --kind=DeliveryEvent --url=http://localhost:8080/_ah/remote_api; \
    appcfg.py upload_data --config_file=seed_data/bulkloader.yaml --filename=seed_data/PostDefault.csv --kind=PostDefault --url=http://localhost:8080/_ah/remote_api; \
    appcfg.py upload_data --config_file=seed_data/bulkloader.yaml --filename=seed_data/Volunteer.csv --kind=Volunteer --url=http://localhost:8080/_ah/remote_api; \
    appcfg.py upload_data --config_file=seed_data/bulkloader.yaml --filename=seed_data/Supply.csv --kind=Supply --url=http://localhost:8080/_ah/remote_api
