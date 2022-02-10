import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_demo_python.cdk_demo_python_stack import CdkDemoPythonStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_demo_python/cdk_demo_python_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkDemoPythonStack(app, "cdk-demo-python")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
