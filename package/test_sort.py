"""Tests for the project function that checks output and plot generation."""

import pytest
import sys
from io import StringIO
import os
import matplotlib.pyplot as plt
from .result import project


@pytest.fixture()
def setup():
    """Prepare environment for testing."""
    yield


def test_project_output_and_plot():
    """Test the project function for correct output and plot generation."""
    sys.stdout = StringIO()
    project("polymer", 2019, 2024)
    output = sys.stdout.getvalue()
    sys.stdout = sys.__stdout__

    assert "Top 30 Most Common Professional Terms:" in output

    try:
        output_dict = eval(output.split("\n")[1])
    except SyntaxError:
        pytest.fail("Output format is not a dictionary")

    assert isinstance(output_dict, dict), "Output is not a dictionary"

    counts = list(output_dict.values())
    assert all(
        counts[i] >= counts[i + 1] for i in range(len(counts) - 1)
    ), "Word frequencies are not in non-increasing order"

    assert plt.gcf().get_axes(), "No plot generated"
