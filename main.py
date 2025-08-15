from models import Ticket

mock_ticket = {
    "subject": "Account locked after too many tries ASAP",
    "requester": {"name": "Marcus Lee", "email": "marcus.lee@inboxhub.com"},
    "created_at": "2025-06-27T12:09:36Z",
    "comment": {
        "body": "2025-06-27T12:09:36Z — Marcus Lee [requester]: Locked out aftre multiple attmepts. Can you unlock my account? 🙏\n2025-06-27T14:23:36Z — Andre Carvalho [agent]: Hey Marcus, I can take care of this. I updated your 2FA to email for now; you can switch back to SMS once you're in Settings > Security. I'm here if you need more help. ⭐",
        "public": True,
    },
    "comments": [
        {
            "author": {
                "role": "requester",
                "name": "Marcus Lee",
                "email": "marcus.lee@inboxhub.com",
            },
            "public": True,
            "body": "Locked out aftre multiple attmepts. Can you unlock my account? 🙏",
            "created_at": "2025-06-27T12:09:36Z",
            "attachments": [],
        },
        {
            "author": {"role": "agent", "name": "Andre Carvalho"},
            "public": True,
            "body": "Hey Marcus, I can take care of this. I updated your 2FA to email for now; you can switch back to SMS once you're in Settings > Security. I'm here if you need more help. ⭐",
            "created_at": "2025-06-27T14:23:36Z",
            "attachments": [],
        },
    ],
}

try:
    ticket_obj = Ticket(**mock_ticket)

    print(f"Subject: {ticket_obj.subject}")
    print(f"Requester: {ticket_obj.requester.name} ({ticket_obj.requester.email})")
    print(f"First customer comment: '{ticket_obj.comments[0].body}'")
except Exception as e:
    print(f"Validation error: {e}")
