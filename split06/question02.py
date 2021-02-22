import json
import logging


logging.basicConfig(filename='app.log',
                    filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')



def is_unique(uniq_values: list, name: str) -> bool:
    for i in uniq_values:
        if i['name'] == name:
            return False
    return True


def parse_user(output_file, *input_files):
    only_uniq = []
    for file in input_files:
        try:
            with open(file) as f:
                json_read = json.loads(f.read())

                for dictionary in json_read:
                    try:
                        if is_unique(only_uniq, dictionary['name']):
                            only_uniq.append(dictionary)
                    except KeyError:
                        only_uniq = []
                        break
        except FileNotFoundError:
            logging.error(f'File {file} doesn\'t exists')

    with open(output_file, 'w') as f:
        json.dump(only_uniq, f, indent=4)