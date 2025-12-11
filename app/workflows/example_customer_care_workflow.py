from core.schema import WorkflowSchema, NodeConfig
from core.workflow import Workflow
from schemas.example_customer_care_schema import CustomerCareEventSchema
from workflows.example_customer_care_workflow_nodes.analyze_ticket_node import (
    AnalyzeTicketNode,
)
from workflows.example_customer_care_workflow_nodes.close_ticket_node import (
    CloseTicketNode,
)
from workflows.example_customer_care_workflow_nodes.determine_intent_ticket_node import (
    DetermineTicketIntentNode,
)
from workflows.example_customer_care_workflow_nodes.escalate_ticket_node import (
    EscalateTicketNode,
)
from workflows.example_customer_care_workflow_nodes.filter_spam import FilterSpamNode
from workflows.example_customer_care_workflow_nodes.generate_response_node import (
    GenerateResponseNode,
)
from workflows.example_customer_care_workflow_nodes.process_invoice_node import (
    ProcessInvoiceNode,
)
from workflows.example_customer_care_workflow_nodes.send_reply_node import SendReplyNode
from workflows.example_customer_care_workflow_nodes.ticket_router_node import (
    TicketRouterNode,
)
from workflows.example_customer_care_workflow_nodes.validate_ticket_node import (
    ValidateTicketNode,
)


class ExampleCustomerCareWorkflow(Workflow):
    workflow_schema = WorkflowSchema(
        description="",
        event_schema=CustomerCareEventSchema,
        start=AnalyzeTicketNode,
        nodes=[
            NodeConfig(
                node=AnalyzeTicketNode,
                connections=[TicketRouterNode],
                description="",
                concurrent_nodes=[
                    DetermineTicketIntentNode,
                    FilterSpamNode,
                    ValidateTicketNode,
                ],
            ),
            NodeConfig(
                node=TicketRouterNode,
                connections=[
                    CloseTicketNode,
                    EscalateTicketNode,
                    GenerateResponseNode,
                    ProcessInvoiceNode,
                ],
                description="",
                is_router=True,
            ),
            NodeConfig(
                node=GenerateResponseNode,
                connections=[SendReplyNode],
                description="",
            ),
        ],
    )
