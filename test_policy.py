import json
import os
import pytest
from main import verify_json_file
from pytest_fixture import empty_json, invalid_filename, invalid_extension, fully_empty_json, invalid_policy_document_type\
    , invalid_policy_name_type, invalid_policy_structure, invalid_policy_structure_without_resource, valid_policy_single_asterisk\
    , valid_policy_other


# Test cases
def test_invalid_filename(invalid_filename):
    with pytest.raises(FileNotFoundError, match="File 'inv.json' not found."):
        verify_json_file(invalid_filename)

def test_invalid_extension(invalid_extension):
    with pytest.raises(TypeError, match="File must have a '.json' extension."):
        verify_json_file(invalid_extension)

def test_verify_json_file_empty_file(empty_json):
    with pytest.raises(ValueError, match="JSON file is empty."):
        verify_json_file(empty_json)

def test_verify_json_file_fully_empty_file(fully_empty_json):
    with pytest.raises(ValueError, match="Expecting value: .*"):
        verify_json_file(fully_empty_json)

def test_verify_json_file_invalid_policy_document_type(invalid_policy_document_type):
    with pytest.raises(ValueError, match="JSON file does not follow the `AWS::IAM::Role Policy` data format."):
        verify_json_file(invalid_policy_document_type)

def test_verify_json_file_invalid_policy_name_type(invalid_policy_name_type):
    with pytest.raises(ValueError, match="JSON file does not follow the `AWS::IAM::Role Policy` data format."):
        verify_json_file(invalid_policy_name_type)

def test_verify_json_file_invalid_policy_structure(invalid_policy_structure):
    with pytest.raises(ValueError, match="JSON file does not follow the `AWS::IAM::Role Policy` data format."):
        verify_json_file(invalid_policy_structure)

def test_verify_json_file_invalid_policy_structure_without_resource(invalid_policy_structure_without_resource):
    with pytest.raises(ValueError, match="JSON file does not contain valid `AWS::IAM::Role Policy` data."):
        verify_json_file(invalid_policy_structure_without_resource)

def test_verify_json_file_valid_policy_single_asterisk(valid_policy_single_asterisk):
    assert verify_json_file(valid_policy_single_asterisk) == False

valid_policy_other
def test_verify_json_file_valid_policy_other(valid_policy_other):
    assert verify_json_file(valid_policy_other) == True