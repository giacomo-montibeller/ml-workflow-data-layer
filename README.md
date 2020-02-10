# ML Workflow

## Data Layer

In this layer data is fetched from an open data hub and prepared for the model layer.
The dataset produced is not saved in this repositories due to the big size, the need here is to find an alternative to version the dataset.

### DVC

DVC is built to make ML models shareable and reproducible. It is designed to handle large files, data sets, machine learning models, and metrics as well as code.

#### Useful commands

* `dvc init`: to initialize a git repo with DVC
* `dvc remote add ...`: to add a remote where to store your data, for example if using your local machine the full command is `dvc remote add -d myremote /path/to/my/folder`
DVC supports these types of remote:

  * `s3`: Amazon Simple Storage Service
  * `azure`: Microsoft Azure Blob Storage
  * `gdrive` : Google Drive
  * `gs`: Google Cloud Storage
  * `ssh`: Secure Shell (requires SFTP)
  * `hdfs`: Hadoop Distributed File System
  * `http`: HTTP and HTTPS protocols
  * `local`: Directory in the local file system

* `dvc add /data/path`: to add files under DVC control
* `dvc push`: to upload data to remote storage
* `dvc pull`: to download data from remote storage, can be used after a `git pull` or `git checkout`

### Run tests

To run all the tests run the following command:

`python3 -m unittest test_*.py`

To run just the unit tests run the following command:

`python3 -m unittest test_unit_*.py`

To run just the integration tests run the following command:

`python3 -m unittest test_integration_*.py`