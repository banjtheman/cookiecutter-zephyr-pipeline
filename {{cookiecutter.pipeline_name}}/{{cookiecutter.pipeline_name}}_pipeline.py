# Python imports
import logging

# 3rd party imports
from metaflow import FlowSpec, Parameter, step

# Project Imports
REPLACE_PROJECT_IMPORT

# How to run
# python {{cookiecutter.pipeline_name}}_pipeline.py run ARGs
# example : python {{cookiecutter.pipeline_name}}_pipeline.py run --input_dir example_files --output_dir data

# can have the posthook change this file?
class {{cookiecutter.pipeline_name}}Flow(FlowSpec):
    """
    This flow will run the {{cookiecutter.pipeline_name}} pipeline
    """

    # TODO define yoru args, these are ssample input and output dir args
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


        # self.next(self.create_dir, foreach="file_names")

    @step
    def REPLACE_MOUDLE_NAME(self):
        """
        REPLACE_MODULE_DESC
        """
        # TODO insert your module process here

        self.next(
            self.REPLACE_NEXT_MODULE,
        )


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
    {{cookiecutter.pipeline_name}Flow()
