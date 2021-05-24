# Python imports
import logging

# 3rd party imports
from metaflow import FlowSpec, Parameter, step

# Project Imports
REPLACE_PROJECT_IMPORT

# How to run
# python {{cookiecutter.pipeline_name}}_pipeline.py run ARGs
# example : python {{cookiecutter.pipeline_name}}_pipeline.py run --input_dir example_files --output_dir data

class REPLACE_PIPELINE_NAMEFlow(FlowSpec):
    """
    This flow will run the {{cookiecutter.pipeline_name}} pipeline
    """

    # TODO define yoru args, these are sample input and output dir args
    # input_dir = Parameter(
    #     "input_dir",
    #     help="Location of sample inputs",
    #     default="sample_inputs",
    #     required=True,
    # )
    # output_dir = Parameter(
    #     "output_dir",
    #     help="Location of sample outputs",
    #     default="sample_outputs",
    #     required=True,
    # )

    @step
    def start(self):
        """
        This is the 'start' step. All flows must have a step named 'start' that
        is the first step in the flow.
        """
        logging.info("Start step")
        
        # TODO add your own code
        # Example code to process files from input dir
        # self.file_names = []
        # for file_name in os.listdir(self.input_dir):
        #     self.file_names.append(file_name)

        # Example process for each file in a dir
        # self.next(self.create_dir, foreach="file_names")

        REPLACE_START_STEP


    REPLACE_MODULES

    # Example join step if you use a foreach statement
    # @step
    # def pipeline_join(self, inputs):
    #     """
    #     Join our parallel pipeline branches and merge results.
    #     """
    #     self.results = [input.status for input in inputs]
    #     self.next(self.end)

    @step
    def end(self):
        """
        This is the 'end' step. All flows must have an 'end' step, which is the
        last step in the flow.
        """
        logging.info("Job's done")

if __name__ == "__main__":
    loglevel = logging.INFO
    logging.basicConfig(
        format="%(asctime)s |%(levelname)s: %(message)s", level=loglevel
    )
    REPLACE_PIPELINE_NAMEFlow()
