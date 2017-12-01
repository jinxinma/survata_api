from collections import Counter

def split_exposure_stamps(value, lookup_id):
    """
    Helper function that parses exposure stamp and return
    number of times a given exposure id appears

    :param value -- an exposure stamp
    :param lookup_id -- an exposure id from exposure stamp
    :return: number of times the exposure id appears in exposure stamp
    """
    final_list = []
    if isinstance(value, str):
        value_split = value.split('|')
        for item in value_split:
            id_list = item.split(':')[-1].strip().split(',')
            final_list += id_list
        return Counter(final_list)[lookup_id]
    else:
        return 0


def subset_data(data, id_list):
    """
    Helper function that subset data based on id_list
    if id not found in data return error info in JSON format

    :param data -- raw data set
    :param id_list -- a list of interview ID's
    :return: a subset of data for interview ID's in id_list
    """
    existing_ids = []
    non_existing_ids = []
    for id_ in id_list:
        if id_ in data['Survata Interview ID'].values:
            existing_ids.append(id_)
        else:
            non_existing_ids.append({'Survata Interview ID': id_,
                                     'error': 'Interview ID not found'})
    return non_existing_ids, data[data['Survata Interview ID'].isin(existing_ids)]