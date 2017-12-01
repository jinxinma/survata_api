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
2. Use `cd` in terminal to get to the folder where the downloaded scripts sit
3. Open `user_definition.py` and change `input_path` to the `data` directory. For example, `input_path = '/Users/jinxin/survata_api/data/'`. Also, make sure `file_name = take_home.csv`
4. In terminal, run `python survata_api.py` and remember the server address, e.g. `http://127.0.0.1:5000/`
5. Open a new terminal to make `GET` requests using `curl`. The returned data will be in JSON format. Example commands include:
  * `curl "http://127.0.0.1:5000/"` -> this brings user to the homepage, make sure to put URL in double quotes
  * `curl "http://127.0.0.1:5000/head"` -> this returns the first row of data
  * `curl "http://127.0.0.1:5000/query?id=1a&id=2b&col=Gender"` -> this returns the gender information for id 1a & 2b. You can change `id` value to the actual Survata interview ID's and change `col` value to a column name, for example `id=b4b7e743-516d-4055-abb9-2b973fede411&col=Country`. This will return country information for the corresponding ID. Note that `col` value is case sensitive, `Country` will work but `country` won't. The first letter of each word in the column name needs to be capital
  * When column name contains spaces or parenthesis, for example `Metro Area`, please do `curl -G "http://127.0.0.1:5000/query?id=1a&id=2b" --data-urlencode "col=Metro Area"`
  * To return the number of `exposure id` for user, you can do something like `curl "http://127.0.0.1:5000/query?id=1a&id=3c&exp_id=405947524"`
  
### How to test API
1. In `user_definition.py`, change the value of `file_name` from `take_home.csv` to `test_file.csv`
2. In terminal, spin up server using `python survata_api.py`
3. Open a new terminal and run `python api_test.py`

