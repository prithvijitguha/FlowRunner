"""Module for cli commands"""
import click
import inspect
from flowrunner import BaseFlow
from flowrunner.system.logger import logger
from pydoc import importfile

@click.group()
def cli():
    click.echo("Welcome to FlowRunner!")


@cli.command()
@click.argument("filepath")
def validate(filepath):
    """Command to validate a python file containing a
    Flow

    Examples:
        - python -m flowrunner validate /my_path/to/flow_file.py

    Args:
        - filepath: A string value of python file containing a Flow i.e subclass of BaseFlow

    Returns:
        - Output regarding the validation of the flow
    """
    flow = _read_python_file(filepath)
    logger.info(f"Found flow {flow.__name__}")
    flow.validate_flow()

@cli.command()
@click.argument("filepath")
def show(filepath):
    """Command to show the flow of a python file containing a
    Flow

    Examples:
        - python -m flowrunner show /my_path/to/flow_file.py

    Args:
        - filepath: A string value of python file containing a Flow i.e subclass of BaseFlow

    Returns:
        - Output regarding the validation of the flow
    """
    flow = _read_python_file(filepath)
    logger.info(f"Found flow {flow.__name__}")
    flow.show()


@cli.command()
@click.argument("filepath")
def run(run_filepath):
    """Command to run a Flow inside a python file

    Examples:
        - python -m flowrunner run /my_path/to/flow_file.py

    Args:
        - filepath: A string value of python file containing a Flow i.e subclass of BaseFlow

    Returns:
        - Output regarding the validation of the flow
    """
    flow = _read_python_file(run_filepath)
    logger.info(f"Found flow {flow.__name__}")
    flow.run_flow()




def _read_python_file(file_path: str) -> BaseFlow:
    """Function to read Python file from path
    An internal function that is used to read a file from a string value.

    Args:
        - file_path: A string value of file path

    Returns:
        - flows: A list value of all subclasses of BaseFlow

    Raises:
        - ValueError: If more than 1 flow is found in the python file
    """
    module = importfile(file_path)
    #module = importfile(file_path)
    module_elements_dict = vars(module) # get module elements in dict eg. {'BaseFlow': <class 'flowrunner.runner.flow.BaseFlow'>, 'ExampleFlow': <class 'testing.ExampleFlow'>}
    # iterate over all and check if subclass of BaseFlow unless its __name__ is BaseFlow itself
    #flows = [] # a list to store all the subclass of BaseFlow
    flows = [element for element in module_elements_dict.values() if inspect.isclass(element) and issubclass(element, BaseFlow) and element.__name__ != BaseFlow.__name__]
    if len(flows) > 1:
        raise ValueError(f"Only 1 Flow are allowed per python file. Found {len(flows)}")
    return flows[0]


if __name__=="__main__":
    cli()




