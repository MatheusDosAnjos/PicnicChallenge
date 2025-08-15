from collections import Counter

from models import Ticket, TicketCategory


def display_summary(categorized_tickets: dict[TicketCategory, list[Ticket]]):
    """Displays an initial summary of ticket counts."""
    print("\n-> Ticket count by category:")

    sorted_categories = sorted(
        categorized_tickets.items(), key=lambda item: len(item[1]), reverse=True
    )

    for category_enum, ticket_list in sorted_categories:
        print(f"- {category_enum.value}: {len(ticket_list)} tickets")


def display_menu(category_map: dict[int, TicketCategory]):
    """Displays the main interactive menu."""
    print("\n Choose a category to analyse the tickets:")

    for index, category in category_map.items():
        print(f"  {index}. {category.value}")

    print("\n Other options:")
    print("  U. Users with the most tickets")
    print("---------------------------------------------")


def display_tickets(tickets: list[Ticket], title: str):
    """Displays a formatted list of tickets."""
    print(f"\n--- {title} ({len(tickets)} tickets) ---")

    if not tickets:
        print("No ticket found.")
        return

    for i, ticket in enumerate(tickets, 1):
        print(f"  {i}. Subject: '{ticket.subject}'")
        print(
            f"     Requester: {ticket.requester.name} | Created at: {ticket.created_at.strftime('%Y-%m-%d %H:%M')}"
        )


def display_top_users(all_tickets: list[Ticket], limit: int = 5) -> None:
    """Displays a formatted list of users with the most tickets opened."""

    print("\n--- Users with the most tickets opened ---")
    user_counts = Counter(ticket.requester.name for ticket in all_tickets)

    for i, (user, count) in enumerate(user_counts.most_common(limit), 1):
        print(f"  {i}. {user}: {count} tickets")


def start_shell(
    all_tickets: list[Ticket], categorized_tickets: dict[TicketCategory, list[Ticket]]
):
    """Starts an interactive shell loop."""
    display_summary(categorized_tickets)

    category_map = dict(enumerate(TicketCategory, 1))

    while True:
        display_menu(category_map)
        choice = input("\n Choose an option and press enter: ").strip().upper()

        if choice.isdigit() and int(choice) in category_map:
            selected_category = category_map[int(choice)]
            tickets_to_show = categorized_tickets.get(selected_category, [])
            display_tickets(tickets_to_show, f"{selected_category.value}'")
        elif choice == "U":
            display_top_users(all_tickets)
        else:
            print("\nInvalid option, try again!")
