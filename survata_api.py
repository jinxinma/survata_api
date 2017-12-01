from flask import Flask, jsonify, request, abort, make_response
import pandas as pd
from user_definition import *
from helper_function import *


app = Flask(__name__)
data = pd.read_csv(input_path + file_name)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/')
def start_app():
    """
    :return: API welcome message in JSON format
    """
    return jsonify({'message': 'Welcome to Survata API for data retrieval'})


@app.route('/head', methods=['GET'])
def print_head():
    """
    :return: The first row of data in JSON format
    """
    return jsonify(data.head(1).to_dict(orient='records'))


@app.route('/query', methods=['GET'])
def query():
    """
    This function parses the URI provided by user and return required information for each interview ID

    :argument from URI:
    id -- Survata interview ID(s)
    col -- column name of user demographic information
    exp_id -- exposure id from exposure stamp

    :return: list of JSON(s) containing required information for each interview id

    Note that the URI argument can either contain id and col or id and exp_id
    """
    if request.method != 'GET':
        abort(400)
    else:
        # check if the number of arguments is 2 and id is in the arguments
        if len(request.args) != 2 or 'id' not in request.args:
            abort(400)
        # check if user provided extra arguments
        for arg in request.args:
            if arg not in ['id', 'col', 'exp_id']:
                abort(400)

        # check if user provided id values
        id_list = request.args.getlist('id')
        if not id_list:
            abort(400)

        # subset data for provided id(s)
        non_existing_id, subset = subset_data(data, id_list)

        # the following if - elif statement slices data based on argument
        # provided, whether it's a column name or an exp_id
        if 'col' in request.args:
            col_name = request.args.get('col')
            if col_name not in data.columns:
                abort(400)
            subset = subset[['Survata Interview ID', col_name]].to_dict(orient='records')
        elif 'exp_id' in request.args:
            exp_id = request.args.get('exp_id')
            if not exp_id:
                abort(400)
            subset['Exposure ID Count'] = subset['Exposure Stamps'].\
                apply(lambda x: split_exposure_stamps(x, exp_id))
            subset = subset[['Survata Interview ID', 'Exposure ID Count']].to_dict(orient='records')

        subset.extend(non_existing_id)
        return jsonify(subset)


if __name__ == '__main__':
    app.run(debug=True)