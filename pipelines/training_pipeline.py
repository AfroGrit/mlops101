from kfp import dsl


@dsl.component(base_image="python:3.10")
def ci_cd_validation():
    print("CI/CD Pipeline Working!")


@dsl.pipeline(name="mlops101-ci-cd-test")
def validation_pipeline():
    ci_cd_validation()
