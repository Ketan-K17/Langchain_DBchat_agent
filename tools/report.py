from langchain.tools import StructuredTool
from pydantic.v1 import BaseModel

def write_report(filename, html):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

class WriteReportsArgsSchema(BaseModel):
    filename: str
    html: str

write_report_tool = StructuredTool.from_function(
    name = "write_report",
    description="Write an HTML file to the disk. Use this tool whenever someone asks for a report.",
    func = write_report,
    args_schema=WriteReportsArgsSchema
)

