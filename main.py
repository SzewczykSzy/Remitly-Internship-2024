import argparse
import json
import os
import sys


def verify_json_file(filename):
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"File '{filename}' not found.")
    
    if not filename.endswith('.json'):
        raise TypeError("File must have a '.json' extension.")
    
    with open(filename, 'r') as file:
        data = json.load(file)

    if not data:
        raise ValueError("JSON file is empty.")

    if not isinstance(data.get('PolicyName', 0), str) or not isinstance(data.get('PolicyDocument', 0), dict):
        raise ValueError("JSON file does not follow the `AWS::IAM::Role Policy` data format.")
    
    statement = data['PolicyDocument'].get('Statement', [])
    if not statement or not isinstance(statement, list) or not isinstance(statement[0].get('Resource'), str):
        raise ValueError("JSON file does not contain valid `AWS::IAM::Role Policy` data.")

    return statement[0]['Resource'] != "*"


def main():
    parser = argparse.ArgumentParser(description='Verify JSON file for `AWS::IAM::Role Policy`.')
    parser.add_argument('filename', type=str, help='Path to the JSON file.')
    args = parser.parse_args()

    try:
        result = verify_json_file(args.filename)
        if result:
            print("`Resource` field does not contain a single asterisk.")
        else:
            print("`Resource` field contains a single asterisk.")
    except (FileNotFoundError, TypeError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()