# Survata Take-home Exercise

I built a simple API where user can use `curl` to make `GET` requests and retrieve data from the backend.

### Files in this repository
1. `survata_api.py`: the main script for API
2. `helper_function.py`: user defined functions for data processing
3. `api_test.py`: the test script for API and helper functions
4. `user_definition.py`: contains the path and file name of data
5. `data`: folder that contain `take_home.csv` and `test_file.csv`

### How to run this API
1. Clone the repository to local machine
2. Use `cd` in terminal to get to the directory where the downloaded scripts sit
3. Open `user_definition.py` and change `input_path` to the `data` directory. For example, `input_path = '/Users/jinxin/survata_api/data/'`. Also, make sure `file_name = take_home.csv`
4. In terminal, run `python survata_api.py` and copy the server address, e.g. `http://127.0.0.1:5000/`
5. Open a new terminal to make `GET` requests using `curl`. Example URL includes:
  * `curl "http://127.0.0.1:5000/"` -> this brings user to the homepage
  * `curl "http://127.0.0.1:5000/head"` -> this returns the first row of data
  * `curl "http://127.0.0.1:5000/query?id=1&id=2&col=Gender"` -> this returns the gender information for id 1 and 2. You can change `id` value to the actual Survata interview ID's and change `col` value to a column name, for example `col=Country` will return country information

