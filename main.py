from pydantic_core import ValidationError
from collections import Counter

from categorizer import categorize_ticket
from models import TicketData

try:
    file_path = "zendesk_mock_tickets_llm_flavor.json"

    print(f"Reading file '{file_path}'")
    with open(file_path, "r", encoding="utf-8") as f:
        json_content = f.read()

    data = TicketData.model_validate_json(json_content)

    category_counts = Counter(categorize_ticket(ticket) for ticket in data.tickets)

    print("\n-> Ticket count by category:  ---")
    for category_enum, count in category_counts.most_common():
        print(f"- {category_enum.value}: {count} tickets")

except FileNotFoundError:
    print(f"File '{file_path}' has not been found.")

except ValidationError as e:
    print("JSON content does not match the model structure.", e)

except Exception as e:
    print("An unexpected error occurred.", e)
