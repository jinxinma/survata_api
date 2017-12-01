# Survata Take-home Exercise

I built a simple API where user can use `curl` to make `GET` requests and retrieve data from the backend.

### Files in this repository
* `survata_api.py`: the main script for API
* `helper_function.py`: user defined functions for data processing
* `api_test.py`: the test script for API and helper functions
* `user_definition.py`: contains the path and file name of data
* `data`: folder that contain `take_home.csv` and `test_file.csv`

### How to run this API
* Clone the repository to local machine
* Use `cd` in terminal to get to the current working directory where the downloaded scripts sit
* Open `user_definition.py` and change `input_path` to the `data` directory. For example, `input_path = '/Users/jinxin/survata_api/data/'`. Also, make sure `file_name = take_home.csv`
* In terminal, run `python survata_api.py`. Then open a new terminal to make `GET` requests using `curl`. Example URL includes:
  *123

