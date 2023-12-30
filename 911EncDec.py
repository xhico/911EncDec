# -*- coding: utf-8 -*-
# !/usr/bin/python3

import os
import base64


def enc911(file_path):
    """
    Encode the contents of a file using base64 and save the encoded output to a new file.

    Args:
        file_path (str): The path to the input file to be encoded.
    """
    with open(file_path, "rb") as in_file:
        data = in_file.read()
    encoded_data = base64.b64encode(data)

    # Create a new file name by adding "_enc" before the file extension
    file_name, file_extension = os.path.splitext(file_path)
    new_file_name = file_name + "_enc" + file_extension
    with open(new_file_name, "wb") as out_file:
        out_file.write(encoded_data)


if __name__ == '__main__':
    # Get the absolute path of the current script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Define input and output file paths relative to the script directory
    input_file_path = os.path.join(script_dir, "911")
    output_file_path = os.path.join(script_dir, "911_enc")

    # Encode the contents of the input file and save to a new file
    enc911(input_file_path)
