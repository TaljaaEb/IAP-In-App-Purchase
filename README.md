#               ┌──────────────────┐\
#               │ webhook_server   │\
#               │                  │\
#               │  event collector │\
#               └────────┬─────────┘\
#                        │\
#         ┌──────────────┼──────────────┐\
#         ▼              ▼              ▼\
#     /iap           /merchant       /itemlines\
#         │              │              │\
#         ▼              ▼              ▼\
#   entitlement       A/B logic          C\
#         │\
#         ▼\
#      Tkinter\
