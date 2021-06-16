import kfp
import kfp.components as comp
from kfp import dsl

@dsl.pipeline(
    name='sheum-iris-test',
    description='sheum iris test ... '
)

def sheum_pipeline():
    mypreprocessing = dsl.ContainerOp(
        name="load iris data pipeline",
        image="shilf1/sheum-iris-preprocess:latest",
        arguments=[
            '--data_path', './orig_iris.csv'
        ],
        file_outputs={'m_iris' : '/m_iris.csv'}
    )

    ml = dsl.ContainerOp(
        name="training pipeline",
        image="shilf1/sheum-iris-train:latest",
        arguments=[
            '--data', mypreprocessing.outputs['m_iris']
        ]
    )

    ml.after(mypreprocessing)

if __name__ == "__main__":
    import kfp.compiler as compiler
    compiler.Compiler().compile(sheum_pipeline, __file__ + ".tar.gz")
