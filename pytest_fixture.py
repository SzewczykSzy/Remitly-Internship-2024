import pytest
import json

@pytest.fixture
def empty_json():
    data = {}
    file_path = "test_file.json"
    with open(file_path, 'w') as file:
        json.dump(data, file)
    return str(file_path)

@pytest.fixture
def invalid_filename():
    return str('inv.json')

@pytest.fixture
def invalid_extension():
    file_path = "test_file.txt"
    with open(file_path, 'w') as file:
        file.write("Something")
    return str(file_path)

@pytest.fixture
def fully_empty_json():
    file_path = "test_file.json"
    with open(file_path, 'w') as file:
        pass
    return str(file_path)

@pytest.fixture
def invalid_policy_document_type():
    data = {"PolicyName": "root",
        "PolicyDocument": 1
}
    file_path = "test_file.json"
    with open(file_path, 'w') as file:
        json.dump(data, file)
    return str(file_path)

@pytest.fixture
def invalid_policy_name_type():
    data = {"PolicyName": [1, 2],
        "PolicyDocument": {"sample": "result"}}
    file_path = "test_file.json"
    with open(file_path, 'w') as file:
        json.dump(data, file)
    return str(file_path)

@pytest.fixture
def invalid_policy_structure():
    data = {"PolicyNames": "root",
        "PolicyDocuments": {"sample": "result"}}
    file_path = "test_file.json"
    with open(file_path, 'w') as file:
        json.dump(data, file)
    return str(file_path)

@pytest.fixture
def invalid_policy_structure_without_resource():
    data = {
    "PolicyName": "root",
    "PolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "IamListAccess",
                "Effect": "Allow",
                "Action": [
                    "iam:ListRoles",
                    "iam:ListUsers"
                ],
            }
        ]
    }
}
    file_path = "test_file.json"
    with open(file_path, 'w') as file:
        json.dump(data, file)
    return str(file_path)

@pytest.fixture
def valid_policy_single_asterisk():
    data = {
    "PolicyName": "root",
    "PolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "IamListAccess",
                "Effect": "Allow",
                "Action": [
                    "iam:ListRoles",
                    "iam:ListUsers"
                ],
                "Resource": "*"
            }
        ]
    }
}
    file_path = "test_file.json"
    with open(file_path, 'w') as file:
        json.dump(data, file)
    return str(file_path)

@pytest.fixture
def valid_policy_other():
    data = {
    "PolicyName": "root",
    "PolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "IamListAccess",
                "Effect": "Allow",
                "Action": [
                    "iam:ListRoles",
                    "iam:ListUsers"
                ],
                "Resource": "arn:aws:s3:::confidential-data/*"
            }
        ]
    }
}
    file_path = "test_file.json"
    with open(file_path, 'w') as file:
        json.dump(data, file)
    return str(file_path)