from enum import Enum

from workflows.example_customer_care_workflow import ExampleCustomerCareWorkflow
from workflows.example_streaming_workflow import ExampleStreamingWorkflow


class WorkflowRegistry(Enum):
    EXAMPLE_STREAMING_WORKFLOW = ExampleStreamingWorkflow
    EXAMPLE_CUSTOMER_CARE_WORKFLOW = ExampleCustomerCareWorkflow
