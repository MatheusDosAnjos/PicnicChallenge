from pydantic_core import ValidationError

from categorizer import group_tickets_by_category
from models import TicketData
from gui import start_shell

try:
    file_path = "zendesk_mock_tickets_llm_flavor.json"

    with open(file_path, "r", encoding="utf-8") as f:
        json_content = f.read()

    data = TicketData.model_validate_json(json_content)

    categorized_tickets = group_tickets_by_category(data.tickets)

    start_shell(data.tickets, categorized_tickets)

except FileNotFoundError:
    print(f"File '{file_path}' has not been found.")

except ValidationError as e:
    print("JSON content does not match the model structure.", e)

except Exception as e:
    print("An unexpected error occurred.", e)
