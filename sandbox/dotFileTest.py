import pydra
import nest_asyncio
import pydot
from pathlib import Path

nest_asyncio.apply()


@pydra.mark.task
def get_self(x):
    print(x)
    return x


@pydra.mark.task
def add2(x):
    return x + 2


@pydra.mark.task
def multiply(x, y):
    return x * y


@pydra.mark.task
def get_num(x):
    return x


@pydra.mark.task
def extract_from_outall_dict(d: dict):
    return list(d.values())


# task1 = add2(name="add2", x=1)
# task2 = add2(name="add2_2", x=task1.lzout.out)

source_node = pydra.Workflow(name="wf_st_3", input_spec=["x"])
# source_node.add(add2(name="add2", x=source_node.lzin.x))
# source_node.add(add2(name="add2_2", x=source_node.add2.lzout.out))
source_node.inputs.x = [1, 6, 9]
source_node.split("x")

# processing_node = pydra.Workflow(name="processing_node", input_spec=["x"], x=source_node.add2.lzout.out)
processing_node = pydra.Workflow(
    name="processing_node", input_spec=["x"], x=source_node.lzin.x
)

processing_node.add(add2(name="add2_1", x=processing_node.lzin.x))
processing_node.add(add2(name="add2_2", x=processing_node.add2_1.lzout.out))
processing_node.set_output(
    [
        ("add2_1", processing_node.add2_1.lzout.out),
        ("add2_2", processing_node.add2_2.lzout.out),
    ]
)

sink_node = pydra.Workflow(
    name="sink_node", input_spec=["x"], x=processing_node.lzout.all_
)
sink_node.add(
    extract_from_outall_dict(name="extract_from_outall_dict", d=sink_node.lzin.x)
)
sink_node.add(
    add2(name="add2", x=sink_node.extract_from_outall_dict.lzout.out).split("x")
)
sink_node.set_output(
    [
        ("out", sink_node.extract_from_outall_dict.lzout.out),
        ("add2", sink_node.add2.lzout.out),
    ]
)

source_node.add(processing_node)
source_node.add(sink_node)

# source_node.set_output([("add2", source_node.add2_2.lzout.out)])
source_node.set_output([("add2", source_node.sink_node.lzout.add2)])

with pydra.Submitter(plugin="cf") as sub:
    sub(source_node)
# with pydra.Submitter(plugin="cf") as sub:
#     sub(task2)

graph_dir = Path("/mnt/c/2020_Grad_School/Research/BRAINSPydra/graphs")
source_node.graph.create_dotfile_nested(outdir=graph_dir, name="source")
(source_dot,) = pydot.graph_from_dot_file(graph_dir / Path("source.dot"))
source_dot.write_png(graph_dir / Path("source.png"))

processing_node.graph.create_dotfile_simple(outdir=graph_dir, name="processing")
(processing_dot,) = pydot.graph_from_dot_file(graph_dir / Path("processing.dot"))
processing_dot.write_png(graph_dir / Path("processing.png"))

# (processing_dot,) = pydot.graph_from_dot_file(processing_node.graph.create_dotfile_simple(outdir="/mnt/c/2020_Grad_School/Research/BRAINSPydra/graphs", name="processing"))
# processing_dot.write_png("processing.png")

results = source_node.result()
print(results)
