from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from get_llm import get_llm
from pydantic import BaseModel, Field
from typing import Optional

llm= get_llm()

class leave_form(BaseModel):
    """form for the employee to apply for a leave"""

    employee_name:  Optional[str] = Field(default=None,description="The name of the employee filling the form")
    request_type: str = Field(description="The type of request e.g. leave, work-from-home")
    details: Optional[str] = Field(
        default=None, description="details of the leave that has been made like the number of days or so"
    )
    department: str = Field(default=None, description="Department of the employee")
    start_date: str = Field( description="start date for the leave")
    end_date: str = Field( description="end date for the leave")
    
def form():
    structured_llm = llm.with_structured_output(leave_form)
    system_message='''
    You are an HR Assistant.  
    Your role is to collect structured information from employees in order to process HR-related requests such as leave, payroll, or benefits.

    Instructions:
    - Extract all relevant details from the employee’s input.  
    - Dates must always be identified and written in YYYY-MM-DD format.  
    - If any required information is missing (such as employee name, ID, request type, or dates),do not give null.  
    - Instead, politely ask the employee to re-enter the missing data.  
    - Clearly mention which fields are missing if the employee doesn't enter the re.  
    - Always return the collected information in a structured and professional manner.  
    - If all required information is present, provide the complete structured data back to the user.
    '''
    form_prompt = ChatPromptTemplate([
        ("system", system_message),
        # ("placeholder", "{msgs}"),
        ("human", "{input}")
    ])
    form_chain =  form_prompt | structured_llm
    return form_chain


