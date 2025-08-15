from pydantic_core import ValidationError
from models import TicketData

try:
    file_path = "zendesk_mock_tickets_llm_flavor.json"

    print(f"Reading file '{file_path}'")
    with open(file_path, "r", encoding="utf-8") as f:
        json_content = f.read()

    ticket_data = TicketData.model_validate_json(json_content)

    print("\n-> Accessing first ticket:")
    first_ticket = ticket_data.tickets[0]
    print(f"Subject: {first_ticket.subject}")
    print(f"Requester: {first_ticket.requester.name}")

    print("\n-> Accessing last ticket:")
    last_ticket = ticket_data.tickets[-1]
    print(f"Subject: {last_ticket.subject}")
    print(f"Requester: {last_ticket.requester.name}")

except FileNotFoundError:
    print(f"File '{file_path}' has not been found.")

except ValidationError as e:
    print("JSON content does not match the model structure.", e)
