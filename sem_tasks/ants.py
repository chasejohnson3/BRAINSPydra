"""
Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator.
"""

import attr
from nipype.interfaces.base import (
    Directory,
    File,
    InputMultiPath,
    OutputMultiPath,
    traits,
)
from pydra import ShellCommandTask
from pydra.engine.specs import SpecInfo, ShellSpec, MultiInputFile, MultiOutputFile
import pydra


class ANTSRegistration:
    def __init__(self, name="BRAINSResample", executable="BRAINSResample"):
        self.name = name
        self.executable = executable

    """
    title: Resample Image (BRAINS)
    category: Registration
    description: This program collects together three common image processing tasks that all involve resampling an image volume: Resampling to a new resolution and spacing, applying a transformation (using an ITK transform IO mechanisms) and Warping (using a vector image deformation field).  Full documentation available here: http://wiki.slicer.org/slicerWiki/index.php/Documentation/4.1/Modules/BRAINSResample.
    version: 5.2.0
    documentation-url: http://www.slicer.org/slicerWiki/index.php/Documentation/4.1/Modules/BRAINSResample
    license: https://www.nitrc.org/svn/brains/BuildScripts/trunk/License.txt
    contributor: This tool was developed by Vincent Magnotta, Greg Harris, and Hans Johnson.
    acknowledgements: The development of this tool was supported by funding from grants NS050568 and NS40068 from the National Institute of Neurological Disorders and Stroke and grants MH31593, MH40856, from the National Institute of Mental Health.
    """

    def get_task(self):
        input_fields = [
            # (
            #     "verbose",
            #     attr.ib(
            #         type=str,
            #         metadata={
            #             "argstr": "--verbose ",
            #             "help_string": "",
            #         },
            #     ),
            # ),
            # (
            #     "collapse_output_transforms",
            #     attr.ib(
            #         type=traits.Int,
            #         metadata={
            #             "argstr": "--collapse-output-transforms ",
            #             "help_string": "",
            #         },
            #     ),
            # ),
            # (
            #     "dimensionality",
            #     attr.ib(
            #         type=traits.Int,
            #         metadata={
            #             "argstr": "--dimensionality ",
            #             "help_string": "",
            #         },
            #     ),
            # ),
            # (
            #     "float",
            #     attr.ib(
            #         type=traits.Int,
            #         metadata={
            #             "argstr": "--float ",
            #             "help_string": "",
            #         },
            #     ),
            # ),
            # (
            #     "initial_moving_transform",
            #     attr.ib(
            #         type=MultiInputFile,
            #         metadata={
            #             "argstr": "--initial-moving-transform ...",
            #             "help_string": "",
            #         },
            #     ),
            # ),
            # (
            #     "initialize_transforms_per_stage",
            #     attr.ib(
            #         type=traits.Int,
            #         metadata={
            #             "argstr": "--initialize-transforms-per-stage ",
            #             "help_string": "",
            #         },
            #     ),
            # ),
            # (
            #     "interpolation",
            #     attr.ib(
            #         type=str,
            #         metadata={
            #             "argstr": "--interpolation ",
            #             "help_string": "",
            #         },
            #     ),
            # ),
            (
                "output",
                attr.ib(
                    type=File,
                    metadata={
                        "argstr": "--output",
                        "help_string": "",
                    },
                ),
            ),
            # (
            #     "metric",
            #     attr.ib(
            #         type=MultiInputFile,
            #         metadata={
            #             "argstr": "--metric ...",
            #             "help_string": "",
            #         },
            #     ),
            # ),
            # (
            #     "convergence",
            #     attr.ib(
            #         type=list,
            #         metadata={
            #             "argstr": "--convergence ",
            #             "help_string": "",
            #         },
            #     ),
            # ),
            # (
            #     "smoothing_sigmas",
            #     attr.ib(
            #         type=str,
            #         metadata={
            #             "argstr": "--smoothing-sigmas ",
            #             "help_string": "",
            #         },
            #     ),
            # ),
            # (
            #     "shrink_factors",
            #     attr.ib(
            #         type=str,
            #         metadata={
            #             "argstr": "--shrink-factors ",
            #             "help_string": "",
            #         },
            #     ),
            # ),
            # (
            #     "use_estimate_learning_rate_once",
            #     attr.ib(
            #         type=int,
            #         metadata={
            #             "argstr": "--use-estimate-learning-rate-once ",
            #             "help_string": "",
            #         },
            #     ),
            # ),
            # (
            #     "use_histogram_matching",
            #     attr.ib(
            #         type=int,
            #         metadata={
            #             "argstr": "--use-histogram-matching ",
            #             "help_string": "",
            #         },
            #     ),
            # ),
            # (
            #     "masks",
            #     attr.ib(
            #         type=MultiInputFile,
            #         metadata={
            #             "argstr": "--masks ...",
            #             "help_string": "",
            #         },
            #     ),
            # ),
            # (
            #     "transform",
            #     attr.ib(
            #         type=str,
            #         metadata={
            #             "argstr": "--transform ",
            #             "help_string": "",
            #         },
            #     ),
            # ),
            # (
            #     "metric",
            #     attr.ib(
            #         type=list,
            #         metadata={
            #             "argstr": "--metric ",
            #             "help_string": "",
            #         },
            #     ),
            # ),
            # (
            #     "convergence",
            #     attr.ib(
            #         type=list,
            #         metadata={
            #             "argstr": "--convergence ",
            #             "help_string": "",
            #         },
            #     ),
            # ),
            # (
            #     "smoothing_sigmas",
            #     attr.ib(
            #         type=str,
            #         metadata={
            #             "argstr": "--smoothing-sigmas ",
            #             "help_string": "",
            #         },
            #     ),
            # ),
            # (
            #     "shrink_factors",
            #     attr.ib(
            #         type=str,
            #         metadata={
            #             "argstr": "--shrink-factors ",
            #             "help_string": "",
            #         },
            #     ),
            # ),
            # (
            #     "use_estimate_learning_rate_once",
            #     attr.ib(
            #         type=int,
            #         metadata={
            #             "argstr": "--use-estimate-learning-rate-once ",
            #             "help_string": "",
            #         },
            #     ),
            # ),
            # (
            #     "use_histogram_matching",
            #     attr.ib(
            #         type=int,
            #         metadata={
            #             "argstr": "--use-histogram-matching ",
            #             "help_string": "",
            #         },
            #     ),
            # ),
            # (
            #     "winsorize_image_intensities",
            #     attr.ib(
            #         type=list,
            #         metadata={
            #             "argstr": "--winsorize-image-intensities ",
            #             "help_string": "",
            #         },
            #     ),
            # ),
            # (
            #     "write-composite-transform",
            #     attr.ib(
            #         type=int,
            #         metadata={
            #             "argstr": "--write-composite-transform ",
            #             "help_string": "",
            #         },
            #     ),
            # ),
        ]
        output_fields = [            (
                "output",
                attr.ib(
                    type=pydra.specs.File,
                    metadata={
                        "help_string": "Resulting deformed image",
                        "output_file_template": "{output}",
                    },
                ),
            ),
        ]

        input_spec = SpecInfo(name="Input", fields=input_fields, bases=(ShellSpec,))
        output_spec = SpecInfo(
            name="Output", fields=output_fields, bases=(pydra.specs.ShellOutSpec,)
        )

        task = ShellCommandTask(
            name=self.name,
            executable=self.executable,
            input_spec=input_spec,
            output_spec=output_spec,
        )
        return task

class ANTSJointFusion:
    def __init__(self, name="BRAINSResample", executable="BRAINSResample"):
        self.name = name
        self.executable = executable

    """
    title: Resample Image (BRAINS)
    category: Registration
    description: This program collects together three common image processing tasks that all involve resampling an image volume: Resampling to a new resolution and spacing, applying a transformation (using an ITK transform IO mechanisms) and Warping (using a vector image deformation field).  Full documentation available here: http://wiki.slicer.org/slicerWiki/index.php/Documentation/4.1/Modules/BRAINSResample.
    version: 5.2.0
    documentation-url: http://www.slicer.org/slicerWiki/index.php/Documentation/4.1/Modules/BRAINSResample
    license: https://www.nitrc.org/svn/brains/BuildScripts/trunk/License.txt
    contributor: This tool was developed by Vincent Magnotta, Greg Harris, and Hans Johnson.
    acknowledgements: The development of this tool was supported by funding from grants NS050568 and NS40068 from the National Institute of Neurological Disorders and Stroke and grants MH31593, MH40856, from the National Institute of Mental Health.
    """

    def get_task(self):
        input_fields = [
        ]
        output_fields = [
        ]

        input_spec = SpecInfo(name="Input", fields=input_fields, bases=(ShellSpec,))
        output_spec = SpecInfo(
            name="Output", fields=output_fields, bases=(pydra.specs.ShellOutSpec,)
        )

        task = ShellCommandTask(
            name=self.name,
            executable=self.executable,
            input_spec=input_spec,
            output_spec=output_spec,
        )
        return task

class ANTSApplyTransform:
    def __init__(self, name="BRAINSResample", executable="BRAINSResample"):
        self.name = name
        self.executable = executable

    """
    title: Resample Image (BRAINS)
    category: Registration
    description: This program collects together three common image processing tasks that all involve resampling an image volume: Resampling to a new resolution and spacing, applying a transformation (using an ITK transform IO mechanisms) and Warping (using a vector image deformation field).  Full documentation available here: http://wiki.slicer.org/slicerWiki/index.php/Documentation/4.1/Modules/BRAINSResample.
    version: 5.2.0
    documentation-url: http://www.slicer.org/slicerWiki/index.php/Documentation/4.1/Modules/BRAINSResample
    license: https://www.nitrc.org/svn/brains/BuildScripts/trunk/License.txt
    contributor: This tool was developed by Vincent Magnotta, Greg Harris, and Hans Johnson.
    acknowledgements: The development of this tool was supported by funding from grants NS050568 and NS40068 from the National Institute of Neurological Disorders and Stroke and grants MH31593, MH40856, from the National Institute of Mental Health.
    """

    def get_task(self):
        input_fields = [
        ]
        output_fields = [
        ]

        input_spec = SpecInfo(name="Input", fields=input_fields, bases=(ShellSpec,))
        output_spec = SpecInfo(
            name="Output", fields=output_fields, bases=(pydra.specs.ShellOutSpec,)
        )

        task = ShellCommandTask(
            name=self.name,
            executable=self.executable,
            input_spec=input_spec,
            output_spec=output_spec,
        )
        return task
