from nipype.interfaces.ants import JointFusion
from pydra.tasks.nipype1.utils import Nipype1Task
import pydra

antsJointFusion_task = JointFusion()
antsJointFusion_task.set_default_num_threads(28)
antsJointFusion_task.inputs.num_threads = 28
antsJointFusion_task = Nipype1Task(antsJointFusion_task)

antsJointFusion_task.inputs.atlas_image = [
    [
        "/localscratch/Users/cjohnson30/output_dir/sub-052823_ses-43817_run-002_T1w/91300_2subject.nii.gz"
    ],
    [
        "/localscratch/Users/cjohnson30/output_dir/sub-052823_ses-43817_run-002_T1w/91626_2subject.nii.gz"
    ],
]
antsJointFusion_task.inputs.atlas_segmentation_image = [
    "/localscratch/Users/cjohnson30/output_dir/sub-052823_ses-43817_run-002_T1w/91300_2_subj_lbl.nii.gz",
    "/localscratch/Users/cjohnson30/output_dir/sub-052823_ses-43817_run-002_T1w/91626_2_subj_lbl.nii.gz",
]

antsJointFusion_task.inputs.beta = 2.0
antsJointFusion_task.inputs.dimension = 3
antsJointFusion_task.inputs.search_radius = [3]
antsJointFusion_task.inputs.target_image = [
    "/localscratch/Users/cjohnson30/output_dir/sub-052823_ses-43817_run-002_T1w/t1_average_BRAINSABC.nii.gz"
]
antsJointFusion_task.inputs.mask_image = "/localscratch/Users/cjohnson30/output_dir/sub-052823_ses-43817_run-002_T1w/fixedImageROIAutoMask.nii.gz"
antsJointFusion_task.inputs.out_label_fusion = "JointFusion_HDAtlas20_2015_label.nii.gz"
antsJointFusion_task.inputs.verbose = True

with pydra.Submitter(plugin="cf") as sub:
    sub(antsJointFusion_task)
result = antsJointFusion_task.result()
print(result)
