from segmentation.specialized import BRAINSConstellationDetector
from pathlib import Path


def fill_bcd_task(input_vol_path="/localscratch/Users/cjohnson30/BCD_Practice/t1w_examples2/",
                  input_vol_glob="*",
                  sess_output_dir="/localscratch/Users/cjohnson30/output_dir",
                  inputTemplateModel = "/Shared/sinapse/CACHE/20200915_PREDICTHD_base_CACHE/Atlas/20141004_BCD/T1_50Lmks.mdl",
                  LLSModel = "/Shared/sinapse/CACHE/20200915_PREDICTHD_base_CACHE/Atlas/20141004_BCD/LLSModel_50Lmks.h5",
                  acLowerBound = 80.000000,
                  atlasLandmarkWeights = "/Shared/sinapse/CACHE/20200915_PREDICTHD_base_CACHE/Atlas/20141004_BCD/template_weights_50Lmks.wts",
                  atlasLandmarks = "/Shared/sinapse/CACHE/20200915_PREDICTHD_base_CACHE/Atlas/20141004_BCD/template_landmarks_50Lmks.fcsv",
                  houghEyeDetectorMode = 1,
                  interpolationMode = "Linear",
                  ):
 # Get the SEM generated pydra task for BRAINSToolsBrainsConstellationDetector
    bcd = BRAINSConstellationDetector()
    task_bcd = bcd.task
    input_spec_bcd = bcd.input_spec
    output_spec_bcd = bcd.output_spec
    
    # Make a list of all the paths to be used as input paths
    p = Path("/localscratch/Users/cjohnson30/BCD_Practice/t1w_examples2/")
    all_t1 = p.glob("*")
    filename_objs = list(all_t1)
    input_vols = []
    for t1 in filename_objs:
        input_vols.append(str(t1))
    
    # Define the inputs to the pydra task
    task_bcd.inputs.inputTemplateModel = inputTemplateModel
    task_bcd.inputs.LLSModel = LLSModel
    task_bcd.inputs.acLowerBound = acLowerBound
    task_bcd.inputs.atlasLandmarkWeights = atlasLandmarkWeights 
    task_bcd.inputs.atlasLandmarks = atlasLandmarks
    task_bcd.inputs.houghEyeDetectorMode = houghEyeDetectorMode
    task_bcd.inputs.interpolationMode = interpolationMode
    task_bcd.inputs.inputVolume = input_vols
    task_bcd.inputs.resultsDir = f"{sess_output_dir}"
    task_bcd.inputs.outputLandmarksInInputSpace = [
        f"{task_bcd.inputs.resultsDir}/{Path(x).with_suffix('').with_suffix('').name}_BCD_Original.fcsv"
        for x in input_vols
    ]
    task_bcd.inputs.outputResampledVolume = [
        f"{task_bcd.inputs.resultsDir}/{Path(x).with_suffix('').with_suffix('').name}_BCD_ACPC.nii.gz"
        for x in input_vols
    ]
    task_bcd.inputs.outputTransform = [
        f"{task_bcd.inputs.resultsDir}/{Path(x).with_suffix('').with_suffix('').name}_BCD_Original2ACPC_transform.h5"
        for x in input_vols
    ]
    task_bcd.inputs.outputLandmarksInACPCAlignedSpace = [
        f"{task_bcd.inputs.resultsDir}/{Path(x).with_suffix('').with_suffix('').name}_BCD_ACPC_Landmarks.fcsv"
        for x in input_vols
    ]
    
    # Scalar Split the inputs based on input volume and the files generated by BCD
    task_bcd.split(
        (
            "inputVolume",
            "outputLandmarksInACPCAlignedSpace",
            "outputLandmarksInInputSpace",
            "outputResampledVolume",
            "outputTransform",
        )
    )
    return task_bcd
