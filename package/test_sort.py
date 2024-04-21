'''
Unit tests for the project function that checks output and plot generation.
'''

import pytest
import sys
from io import StringIO
import os
import matplotlib.pyplot as plt
from .result import project  # Ensure this import path matches the actual location

@pytest.fixture()
def setup():
    """Prepare environment for testing."""
    yield
    # Teardown can include closing database connections, cleaning up data, etc.

def test_project_output_and_plot():
    """Test the project function for correct output and plot generation."""
    # Redirect stdout to capture prints
    sys.stdout = StringIO()

    # Execute the function
    project('polymer', 2019, 2024)  # Remove save_plot=True argument

    # Reset standard output and capture output
    output = sys.stdout.getvalue()
    sys.stdout = sys.__stdout__

    # Check if the expected introductory text is in the output
    assert "Top 30 Most Common Professional Terms:" in output

    # Extract the dictionary printed by the function
    try:
        output_dict = eval(output.split('\n')[1])  # Assumes the dictionary is printed on the second line
    except SyntaxError:
        pytest.fail("Output format is not a dictionary")

    # Verify that the output is a dictionary
    assert isinstance(output_dict, dict), "Output is not a dictionary"

    # Verify that the words are sorted by frequency in non-increasing order
    counts = list(output_dict.values())
    assert all(counts[i] >= counts[i + 1] for i in range(len(counts) - 1)), "Word frequencies are not in non-increasing order"
