from pathlib import Path
from BIDSFilename import *
import nest_asyncio
import time
import uuid

import attr
from nipype.interfaces.base import (
    Directory,
    File,
    InputMultiPath,
    OutputMultiPath,
    traits,
)
from pydra import ShellCommandTask
from pydra.engine.specs import SpecInfo, ShellSpec


"""
Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator.
"""
class BRAINSConstellationDetector:
    """
    title: Brain Landmark Constellation Detector (BRAINS)
    category: Segmentation.Specialized
    description: This program will find the mid-sagittal plane, a constellation of landmarks in a volume, and create an AC/PC aligned data set with the AC point at the center of the voxel lattice (labeled at the origin of the image physical space.)  Part of this work is an extention of the algorithms originally described by Dr. Babak A. Ardekani, Alvin H. Bachman, Model-based automatic detection of the anterior and posterior commissures on MRI scans, NeuroImage, Volume 46, Issue 3, 1 July 2009, Pages 677-682, ISSN 1053-8119, DOI: 10.1016/j.neuroimage.2009.02.030.  (http://www.sciencedirect.com/science/article/B6WNP-4VRP25C-4/2/8207b962a38aa83c822c6379bc43fe4c)
    version: 5.2.0
    documentation-url: http://www.nitrc.org/projects/brainscdetector/
    license: https://www.nitrc.org/svn/brains/BuildScripts/trunk/License.txt
    contributor: Hans J. Johnson (hans-johnson -at- uiowa.edu), Ali Ghayoor
    acknowledgements: Hans Johnson(1,2,3); Ali Ghayoor(3); Wei Lu(3) 1=University of Iowa Department of Psychiatry, 2=University of Iowa Department of Biomedical Engineering, 3=University of Iowa Department of Electrical and Computer Engineering
    """

    input_fields = [
        (
            "houghEyeDetectorMode",
            attr.ib(
                type=traits.Int,
                metadata={
                    "argstr": "--houghEyeDetectorMode",
                    "help_string": ",                 This flag controls the mode of Hough eye detector.  By default, value of 1 is for T1W images, while the value of 0 is for T2W and PD images.,             ",
                },
            ),
        ),
        (
            "inputTemplateModel",
            attr.ib(
                type=File,
                metadata={
                    "argstr": "--inputTemplateModel",
                    "help_string": "User-specified template model.,             ",
                    ##"mandatory: "True",
                },
            ),
        ),
        (
            "LLSModel",
            attr.ib(
                type=File,
                metadata={
                    "argstr": "--LLSModel",
                    "help_string": "Linear least squares model filename in HD5 format",
                    #"mandatory: "True",
                },
            ),
        ),
        (
            "inputVolume",
            attr.ib(
                type=File,
                metadata={
                    "argstr": "--inputVolume",
                    "help_string": "Input image in which to find ACPC points",
                    #"mandatory: "True",
                },
            ),
        ),
        (
            "outputVolume",
            attr.ib(
                type=File,
                metadata={
                    "argstr": "--outputVolume",
                    "help_string": "ACPC-aligned output image with the same voxels as the input image, but updated origin, and direction cosign so that the AC point would fall at the physical location (0.0,0.0,0.0), and the mid-sagital plane is the plane where physical L/R coordinate is 0.0. No interpolation method is involved to create the 'outputVolume', and this output image is created using 'resample in place' filter.",
                },
            ),
        ),
        (
            "outputResampledVolume",
            attr.ib(
                type=File,
                metadata={
                    "argstr": "--outputResampledVolume",
                    "help_string": "ACPC-aligned output image in a resampled uniform isotropic space.  Currently this is a 1mm, 256^3 image with identity direction cosign. Choose desired interpolation mode to generate the outputResampledVolume.",
                },
            ),
        ),
        (
            "outputTransform",
            attr.ib(
                type=File,
                metadata={
                    "argstr": "--outputTransform",
                    "help_string": "The filename for the original space to ACPC alignment to be written (in .h5 format).,             ",
                },
            ),
        ),
        (
            "outputLandmarksInInputSpace",
            attr.ib(
                type=File,
                metadata={
                    "argstr": "--outputLandmarksInInputSpace",
                    "help_string": ",               The filename for the new subject-specific landmark definition file in the same format produced by Slicer3 (.fcsv) with the landmarks in the original image space (the detected RP, AC, PC, and VN4) in it to be written.,             ",
                },
            ),
        ),
        (
            "outputLandmarksInACPCAlignedSpace",
            attr.ib(
                type=File,
                metadata={
                    "argstr": "--outputLandmarksInACPCAlignedSpace",
                    "help_string": ",               The filename for the new subject-specific landmark definition file in the same format produced by Slicer3 (.fcsv) with the landmarks in the output image space (the detected RP, AC, PC, and VN4) in it to be written.,             ",
                },
            ),
        ),
        (
            "outputMRML",
            attr.ib(
                type=File,
                metadata={
                    "argstr": "--outputMRML",
                    "help_string": ",               The filename for the new subject-specific scene definition file in the same format produced by Slicer3 (in .mrml format). Only the components that were specified by the user on command line would be generated. Compatible components include inputVolume, outputVolume, outputLandmarksInInputSpace, outputLandmarksInACPCAlignedSpace, and outputTransform.,             ",
                },
            ),
        ),
        (
            "outputVerificationScript",
            attr.ib(
                type=File,
                metadata={
                    "argstr": "--outputVerificationScript",
                    "help_string": ",               The filename for the Slicer3 script that verifies the aligned landmarks against the aligned image file.  This will happen only in conjunction with saveOutputLandmarks and an outputVolume.,             ",
                },
            ),
        ),
        (
            "mspQualityLevel",
            attr.ib(
                type=traits.Int,
                metadata={
                    "argstr": "--mspQualityLevel",
                    "help_string": ",                 Flag cotrols how agressive the MSP is estimated. 0=quick estimate (9 seconds), 1=normal estimate (11 seconds), 2=great estimate (22 seconds), 3=best estimate (58 seconds), NOTE: -1= Prealigned so no estimate!.,             ",
                },
            ),
        ),
        (
            "otsuPercentileThreshold",
            attr.ib(
                type=traits.Float,
                metadata={
                    "argstr": "--otsuPercentileThreshold",
                    "help_string": ",                 This is a parameter to FindLargestForegroundFilledMask, which is employed when acLowerBound is set and an outputUntransformedClippedVolume is requested.,             ",
                },
            ),
        ),
        (
            "acLowerBound",
            attr.ib(
                type=traits.Float,
                metadata={
                    "argstr": "--acLowerBound",
                    "help_string": ",                 When generating a resampled output image, replace the image with the BackgroundFillValue everywhere below the plane This Far in physical units (millimeters) below (inferior to) the AC point (as found by the model.)  The oversize default was chosen to have no effect.  Based on visualizing a thousand masks in the IPIG study, we recommend a limit no smaller than 80.0 mm.,             ",
                },
            ),
        ),
        (
            "cutOutHeadInOutputVolume",
            attr.ib(
                type=traits.Bool,
                metadata={
                    "argstr": "--cutOutHeadInOutputVolume ",
                    "help_string": ",                 Flag to cut out just the head tissue when producing an (un)transformed clipped volume.,             ",
                },
            ),
        ),
        (
            "outputUntransformedClippedVolume",
            attr.ib(
                type=File,
                metadata={
                    "argstr": "--outputUntransformedClippedVolume",
                    "help_string": "Output image in which to store neck-clipped input image, with the use of --acLowerBound and maybe --cutOutHeadInUntransformedVolume.",
                },
            ),
        ),
        (
            "rescaleIntensities",
            attr.ib(
                type=traits.Bool,
                metadata={
                    "argstr": "--rescaleIntensities ",
                    "help_string": ",                 Flag to turn on rescaling image intensities on input.,             ",
                },
            ),
        ),
        (
            "trimRescaledIntensities",
            attr.ib(
                type=traits.Float,
                metadata={
                    "argstr": "--trimRescaledIntensities",
                    "help_string": ",                 Turn on clipping the rescaled image one-tailed on input.  Units of standard deviations above the mean.  Very large values are very permissive.  Non-positive value turns clipping off.  Defaults to removing 0.00001 of a normal tail above the mean.,             ",
                },
            ),
        ),
        (
            "rescaleIntensitiesOutputRange",
            attr.ib(
                type=InputMultiPath,
                metadata={
                    "argstr": "--rescaleIntensitiesOutputRange",
                    "help_string": ",                 This pair of integers gives the lower and upper bounds on the signal portion of the output image.  Out-of-field voxels are taken from BackgroundFillValue.,             ",
                    "sep": ",",
                },
            ),
        ),
        (
            "BackgroundFillValue",
            attr.ib(
                type=traits.Str,
                metadata={
                    "argstr": "--BackgroundFillValue",
                    "help_string": "Fill the background of image with specified short int value. Enter number or use BIGNEG for a large negative number.",
                },
            ),
        ),
        (
            "interpolationMode",
            attr.ib(
                type=traits.Enum,
                metadata={
                    "argstr": "--interpolationMode",
                    "help_string": "Type of interpolation to be used when applying transform to moving volume to create OutputResampledVolume.  Options are Linear, NearestNeighbor, BSpline, or WindowedSinc",
                },
            ),
        ),
        (
            "forceACPoint",
            attr.ib(
                type=InputMultiPath,
                metadata={
                    "argstr": "--forceACPoint",
                    "help_string": ",                 Manually specify the AC point from the original image in RAS coordinates (i.e. Slicer coordinates).,             ",
                    "sep": ",",
                },
            ),
        ),
        (
            "forcePCPoint",
            attr.ib(
                type=InputMultiPath,
                metadata={
                    "argstr": "--forcePCPoint",
                    "help_string": ",                 Manually specify the PC point from the original image in RAS coordinates (i.e. Slicer coordinates).,             ",
                    "sep": ",",
                },
            ),
        ),
        (
            "forceVN4Point",
            attr.ib(
                type=InputMultiPath,
                metadata={
                    "argstr": "--forceVN4Point",
                    "help_string": ",                 Manually specify the VN4 point from the original image in RAS coordinates (i.e. Slicer coordinates).,             ",
                    "sep": ",",
                },
            ),
        ),
        (
            "forceRPPoint",
            attr.ib(
                type=InputMultiPath,
                metadata={
                    "argstr": "--forceRPPoint",
                    "help_string": ",                 Manually specify the RP point from the original image in RAS coordinates (i.e. Slicer coordinates).,             ",
                    "sep": ",",
                },
            ),
        ),
        (
            "inputLandmarksEMSP",
            attr.ib(
                type=File,
                metadata={
                    "argstr": "--inputLandmarksEMSP",
                    "help_string": ",               The filename for the new subject-specific landmark definition file in the same format produced by Slicer3 (in .fcsv) with the landmarks in the estimated MSP aligned space to be loaded. The detector will only process landmarks not enlisted on the file.,             ",
                    #"mandatory: "True",
                },
            ),
        ),
        (
            "forceHoughEyeDetectorReportFailure",
            attr.ib(
                type=traits.Bool,
                metadata={
                    "argstr": "--forceHoughEyeDetectorReportFailure ",
                    "help_string": ",                 Flag indicates whether the Hough eye detector should report failure,             ",
                },
            ),
        ),
        (
            "rmpj",
            attr.ib(
                type=traits.Float,
                metadata={
                    "argstr": "--rmpj",
                    "help_string": ",               Search radius for MPJ in unit of mm,             ",
                },
            ),
        ),
        (
            "rac",
            attr.ib(
                type=traits.Float,
                metadata={
                    "argstr": "--rac",
                    "help_string": ",               Search radius for AC in unit of mm,             ",
                },
            ),
        ),
        (
            "rpc",
            attr.ib(
                type=traits.Float,
                metadata={
                    "argstr": "--rpc",
                    "help_string": ",               Search radius for PC in unit of mm,             ",
                },
            ),
        ),
        (
            "rVN4",
            attr.ib(
                type=traits.Float,
                metadata={
                    "argstr": "--rVN4",
                    "help_string": ",               Search radius for VN4 in unit of mm,             ",
                },
            ),
        ),
        (
            "debug",
            attr.ib(
                type=traits.Bool,
                metadata={
                    "argstr": "--debug ",
                    "help_string": ",               Show internal debugging information.,             ",
                },
            ),
        ),
        (
            "verbose",
            attr.ib(
                type=traits.Bool,
                metadata={
                    "argstr": "--verbose ",
                    "help_string": ",               Show more verbose output,             ",
                },
            ),
        ),
        (
            "writeBranded2DImage",
            attr.ib(
                type=File,
                metadata={
                    "argstr": "--writeBranded2DImage",
                    "help_string": ",               The filename for the 2D .png branded midline debugging image.  This will happen only in conjunction with requesting an outputVolume.,             ",
                },
            ),
        ),
        (
            "resultsDir",
            attr.ib(
                type=Directory,
                metadata={
                    "argstr": "--resultsDir",
                    "help_string": ",               The directory for the debuging images to be written.,             ",
                },
            ),
        ),
        (
            "writedebuggingImagesLevel",
            attr.ib(
                type=traits.Int,
                metadata={
                    "argstr": "--writedebuggingImagesLevel",
                    "help_string": ",                 This flag controls if debugging images are produced.  By default value of 0 is no images.  Anything greater than zero will be increasing level of debugging images.,             ",
                },
            ),
        ),
        (
            "numberOfThreads",
            attr.ib(
                type=traits.Int,
                metadata={
                    "argstr": "--numberOfThreads",
                    "help_string": "Explicitly specify the maximum number of threads to use.",
                },
            ),
        ),
        (
            "atlasVolume",
            attr.ib(
                type=File,
                metadata={
                    "argstr": "--atlasVolume",
                    "help_string": "Atlas volume image to be used for BRAINSFit registration to redefine the final ACPC-aligned transform by registering original input image to the Atlas image. The initial registration transform is created by passing BCD_ACPC_Landmarks and atlasLandmarks to BRAINSLandmarkInitializer. This flag should be used with atlasLandmarks and atlasLandmarkWeights flags. Note that using this flag causes that AC point in the final acpcLandmark file not be exactly placed at 0,0,0 coordinates.,             ",
                    #"mandatory: "True",
                },
            ),
        ),
        (
            "atlasLandmarks",
            attr.ib(
                type=File,
                metadata={
                    "argstr": "--atlasLandmarks",
                    "help_string": "Atlas landmarks to be used for BRAINSFit registration initialization,             ",
                    #"mandatory: "True",
                },
            ),
        ),
        (
            "atlasLandmarkWeights",
            attr.ib(
                type=File,
                metadata={
                    "argstr": "--atlasLandmarkWeights",
                    "help_string": "Weights associated with atlas landmarks to be used for BRAINSFit registration initialization,             ",
                    #"mandatory: "True",
                },
            ),
        ),

	(
            "outputResampledVolume",
            attr.ib(
                type=File,
                metadata={
                    "help_string": "ACPC-aligned output image in a resampled uniform isotropic space.  Currently this is a 1mm, 256^3 image with identity direction cosign. Choose desired interpolation mode to generate the outputResampledVolume.",
                    #"output_file_template": "{SESS_OUTPUT_DIR}/{inputVolume}_BCD_ACPC.nii.gz",
                    "argstr": "--outputResampledVolume"
		    #"output_file_template": "xxx_BCD_ACPC.nii.gz",
		    #"mandatory: "True",
                },
            ),
        ),
        (
            "outputTransform",
            attr.ib(
                type=File,
                metadata={
                    "help_string": "The filename for the original space to ACPC alignment to be written (in .h5 format).,             ",
                    "argstr": "--outputTransform",
		    #"output_file_template": "{SESS_OUTPUT_DIR}/{inputVolume}_BCD_Original2ACPC_transform.h5"
                    #"output_file_template": "xxx_BCD_Original2ACPC_transform.h5",
		    #"mandatory: "True",
                },
            ),
        ),
        (
            "outputLandmarksInInputSpace",
            attr.ib(
                type=File,
                metadata={
                    "help_string": ",               The filename for the new subject-specific landmark definition file in the same format produced by Slicer3 (.fcsv) with the landmarks in the original image space (the detected RP, AC, PC, and VN4) in it to be written.,             ",
                    "argstr": "--outputLandmarksInInputSpace",
		    #"output_file_template": "{SESS_OUTPUT_DIR}/{inputVolume}_BCD_Original.fcsv"
                    #"output_file_template": "xxx_BCD_Original.fcsv",
		    #"mandatory: "True",
                },
            ),
        ),
        (
            "outputLandmarksInACPCAlignedSpace",
            attr.ib(
                type=File,
                metadata={
                    "help_string": ",               The filename for the new subject-specific landmark definition file in the same format produced by Slicer3 (.fcsv) with the landmarks in the output image space (the detected RP, AC, PC, and VN4) in it to be written.,             ",
                    "argstr": "--outputLandmarksInACPCAlignedSpace",
		    #"output_file_template": "{SESS_OUTPUT_DIR}/{inputVolume}_BCD_ACPC_Landmarks.fcsv"
                    #"output_file_template": "xxx_BCD_ACPC_Landmarks.fcsv",
		    #"mandatory: "True",
                },
            ),
        ),


    ]



    SESS_OUTPUT_DIR = "/localscratch/Users/cjohnson30/output_dir"

    output_fields = [
 	(
            "outputResampledVolume",
            attr.ib(
                type=File,
                metadata={
                    "help_string": "ACPC-aligned output image in a resampled uniform isotropic space.  Currently this is a 1mm, 256^3 image with identity direction cosign. Choose desired interpolation mode to generate the outputResampledVolume.",
                    "output_file_template": "{SESS_OUTPUT_DIR}/{inputVolume}_BCD_ACPC.nii.gz",
                    "argstr": "--outputResampledVolume"
		    #"output_file_template": "xxx_BCD_ACPC.nii.gz",
		    #"mandatory: "True",
                },
            ),
        ),
        (
            "outputTransform",
            attr.ib(
                type=File,
                metadata={
                    "help_string": "The filename for the original space to ACPC alignment to be written (in .h5 format).,             ",
                    "argstr": "--outputTransform",
		    "output_file_template": "{SESS_OUTPUT_DIR}/{inputVolume}_BCD_Original2ACPC_transform.h5"
                    #"output_file_template": "xxx_BCD_Original2ACPC_transform.h5",
		    #"mandatory: "True",
                },
            ),
        ),
        (
            "outputLandmarksInInputSpace",
            attr.ib(
                type=File,
                metadata={
                    "help_string": ",               The filename for the new subject-specific landmark definition file in the same format produced by Slicer3 (.fcsv) with the landmarks in the original image space (the detected RP, AC, PC, and VN4) in it to be written.,             ",
                    "argstr": "--outputLandmarksInInputSpace",
		    "output_file_template": "{SESS_OUTPUT_DIR}/{inputVolume}_BCD_Original.fcsv"
                    #"output_file_template": "xxx_BCD_Original.fcsv",
		    #"mandatory: "True",
                },
            ),
        ),
        (
            "outputLandmarksInACPCAlignedSpace",
            attr.ib(
                type=File,
                metadata={
                    "help_string": ",               The filename for the new subject-specific landmark definition file in the same format produced by Slicer3 (.fcsv) with the landmarks in the output image space (the detected RP, AC, PC, and VN4) in it to be written.,             ",
                    "argstr": "--outputLandmarksInACPCAlignedSpace",
		    "output_file_template": "{SESS_OUTPUT_DIR}/{inputVolume}_BCD_ACPC_Landmarks.fcsv"
                    #"output_file_template": "xxx_BCD_ACPC_Landmarks.fcsv",
		    #"mandatory: "True",
                },
            ),
        ),
	( 
            "outputVolume",
            attr.ib(
                type=File,
                metadata={
                    "help_string": "ACPC-aligned output image with the same voxels as the input image, but updated origin, and direction cosign so that the AC point would fall at the physical location (0.0,0.0,0.0), and the mid-sagital plane is the plane where physical L/R coordinate is 0.0. No interpolation method is involved to create the 'outputVolume', and this output image is created using 'resample in place' filter.",
                    #"mandatory: "True",
                },
            ),
        ),
        (
            "outputMRML",
            attr.ib(
                type=File,
                metadata={
                    "help_string": ",               The filename for the new subject-specific scene definition file in the same format produced by Slicer3 (in .mrml format). Only the components that were specified by the user on command line would be generated. Compatible components include inputVolume, outputVolume, outputLandmarksInInputSpace, outputLandmarksInACPCAlignedSpace, and outputTransform.,             ",
                    #"mandatory: "True",
                },
            ),
        ),
        (
            "outputVerificationScript",
            attr.ib(
                type=File,
                metadata={
                    "help_string": ",               The filename for the Slicer3 script that verifies the aligned landmarks against the aligned image file.  This will happen only in conjunction with saveOutputLandmarks and an outputVolume.,             ",
                    #"mandatory: "True",
                },
            ),
        ),
        (
            "outputUntransformedClippedVolume",
            attr.ib(
                type=File,
                metadata={
                    "help_string": "Output image in which to store neck-clipped input image, with the use of --acLowerBound and maybe --cutOutHeadInUntransformedVolume.",
                    #"mandatory: "True",
                },
            ),
        ),
        (
            "writeBranded2DImage",
            attr.ib(
                type=File,
                metadata={
                    "help_string": ",               The filename for the 2D .png branded midline debugging image.  This will happen only in conjunction with requesting an outputVolume.,             ",
                    #"mandatory: "True",
                },
            ),
        ),
        (
            "resultsDir",
            attr.ib(
                type=Directory,
                metadata={
                    "help_string": ",               The directory for the debuging images to be written.,             ",
                    #"mandatory: "True",
                },
            ),
        ),
    ]

    input_spec = SpecInfo(name="Input", fields=input_fields, bases=(ShellSpec,))
    output_spec = SpecInfo(name="Output", fields=output_fields, bases=(ShellSpec,))
    
    task = ShellCommandTask(
    name="BRAINSConstellationDetector",
    executable="BRAINSConstellationDetector",
    input_spec=input_spec,
    #output_spec=output_spec,
    ) 
##### END BCD input_spec and output_spec definition ######


