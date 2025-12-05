import base64
import os

from dotenv import load_dotenv
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider, Tracer
from opentelemetry.sdk.trace.export import SimpleSpanProcessor

load_dotenv()


class LangfuseConfig:
    _initialized = False

    @staticmethod
    def get_tracer() -> Tracer:
        if not LangfuseConfig._initialized:
            # Set up the Langfuse trace exporter FIRST
            LANGFUSE_AUTH = base64.b64encode(
                f"{os.getenv('LANGFUSE_PUBLIC_KEY')}:{os.getenv('LANGFUSE_SECRET_KEY')}".encode()
            ).decode()

            langfuse_host = os.getenv(
                "LANGFUSE_HOST"
            )
            otlp_endpoint = f"{langfuse_host}/api/public/otel/v1/traces"

            trace_provider = TracerProvider()
            otlp_exporter = OTLPSpanExporter(
                endpoint=otlp_endpoint,
                headers={"Authorization": f"Basic {LANGFUSE_AUTH}"},
            )
            trace_provider.add_span_processor(SimpleSpanProcessor(otlp_exporter))
            trace.set_tracer_provider(trace_provider)

            # Then configure logfire to use the existing provider
            import logfire

            logfire.configure(
                send_to_logfire=False,
                scrubbing=False,
            )
            logfire.instrument_pydantic_ai()

            LangfuseConfig._initialized = True

        return trace.get_tracer("workflow-tracer")
