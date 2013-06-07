Peace Corps Med Kit App

Create Dev Server Database.  Replace 'localhost:8080' with your dev server IP:PORT

    appcfg.py upload_data --config_file=seed_data/bulkloader.yaml --filename=seed_data/DeliveryEvent.csv --kind=DeliveryEvent --url=http://localhost:8080/_ah/remote_api; \
    appcfg.py upload_data --config_file=seed_data/bulkloader.yaml --filename=seed_data/PostDefault.csv --kind=PostDefault --url=http://localhost:8080/_ah/remote_api; \
    appcfg.py upload_data --config_file=seed_data/bulkloader.yaml --filename=seed_data/Volunteer.csv --kind=Volunteer --url=http://localhost:8080/_ah/remote_api; \
    appcfg.py upload_data --config_file=seed_data/bulkloader.yaml --filename=seed_data/Supply.csv --kind=Supply --url=http://localhost:8080/_ah/remote_api