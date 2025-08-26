from langchain_core.tools import tool
import sqlite3
from typing import List
from form_policy import form
from get_llm import get_llm
from mail_policy import mail
from rag_pipeline import load_vector_store
import nest_asyncio


llm = get_llm()
vector_store = load_vector_store()
form_chain = form()
retriever = vector_store.as_retriever(search_kwargs={"k": 3})
mail_chain = mail()



@tool
def get_context(query: str) -> str:
    """get the context for the given query"""
    return retriever.invoke(query)


@tool
def hr_policy_search(query: str) -> str:
    """Search HR policies and return the most relevant content"""
    docs = get_context.invoke(query, k=3)
    return "\n\n".join([d.page_content for d in docs])


# form output
@tool("leave_form_extractor")
def leave_form_extractor(user_query: str) -> str:
    """Extracts a leave form (JSON) from the user's natural language request."""
    result = form_chain.invoke(user_query)
    data = result.model_dump()

    # Check for missing fields
    missing = [field for field, value in data.items() if not value]
    if missing:
        return f"Could you please provide the following info: {', '.join(missing)}?"
    return data

# ------------------------------------------------------------------

DB_PATH = "employee_status.db"

@tool("fetch_employee_leaves", return_direct=False)
def fetch_employee_leaves(employee_name: str) -> List[str]:
    """
    Fetch all leave records for a given employee by name.
    """
    print("Employee name", employee_name.strip())
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    query = """
    SELECT e.name, e.department, l.leave_type, l.days_taken, l.start_date, l.end_date
    FROM leaves l
    JOIN employees e ON e.id = l.employee_id
    WHERE e.name like ?
    """
    cursor.execute(query, (employee_name.strip(),))
    rows = cursor.fetchall()
    
    
    if not rows:
        print(f"No leave records found for {employee_name}.")
        return f"No leave records found for {employee_name}."

    result = []
    for row in rows:
        result.append(
            f"Name: {row[0]}, Dept: {row[1]}, Leave: {row[2]}, Days: {row[3]}, "
            f"From {row[4]} to {row[5]}"
        )
    conn.close()
    return "\n".join(result)

# --------------------------------------------------------------------------------

# mail writer tool
@tool("mail_writer", return_direct=False)
def mail_writer(user_query: str) -> List[str]:
    """Writes a professional HR email based on the user's request."""
    return mail_chain.invoke({"input": user_query})



