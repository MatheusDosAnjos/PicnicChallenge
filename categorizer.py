from collections import defaultdict

from models import Ticket, TicketCategory

category_keywords = {
    TicketCategory.AUTHENTICATION: [
        "locked",
        "password",
        "2fa",
        "login",
        "logging in",
    ],
    TicketCategory.PAYMENT: [
        "payment",
        "charge",
        "credit",
        "gift card",
    ],
    TicketCategory.PROMOTIONS: [
        "promo",
        "price match",
        "price adjustment",
        "rejected",
        "price dropped",
    ],
    TicketCategory.RETURNS: [
        "return",
        "exchange",
        "swap",
        "didn't fit",
        "too small",
        "refund",
    ],
    TicketCategory.PRODUCT_QUALITY: [
        "damaged",
        "scratched",
        "wrong item",
        "missing parts",
        "defect",
        "broken",
    ],
    TicketCategory.SHIPPING_TRACKING: [
        "where is",
        "tracking stuck",
        "delivered but",
        "delayed package",
        "label created",
    ],
    TicketCategory.ORDER_MODIFICATION: [
        "add an item",
        "update address",
        "cancel",
        "change shipping",
    ],
}


def categorize_ticket(ticket: Ticket) -> TicketCategory:
    subject = ticket.subject.lower()

    for category, keywords in category_keywords.items():
        if any(keyword in subject for keyword in keywords):
            return category

    return TicketCategory.OTHER


def group_tickets_by_category(
    all_tickets: list[Ticket],
) -> dict[TicketCategory, list[Ticket]]:
    """Groups a list of tickets into a dictionary by category."""
    categorized_tickets = defaultdict(list)

    for ticket in all_tickets:
        category = categorize_ticket(ticket)
        categorized_tickets[category].append(ticket)

    return categorized_tickets
