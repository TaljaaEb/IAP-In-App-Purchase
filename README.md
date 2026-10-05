                    ┌──────────────────┐<br>
                    │ webhook_server   │<br>
                    │                  │<br>
                    │  event collector │<br>
                    └────────┬─────────┘<br>
                             │<br>
              ┌──────────────┼──────────────┐<br>
              ▼              ▼              ▼<br>
          /iap           /merchant       /itemlines<br>
              │              │              │<br>
              ▼              ▼              ▼<br>
        entitlement       A/B logic          C<br>
              │<br>
              ▼<br>
           Tkinter<br>
