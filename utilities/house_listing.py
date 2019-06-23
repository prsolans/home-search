class HouseListing:
    """Constructs the message and stores the state of which tasks were completed."""

    WELCOME_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*A new apartment is now on Craigslist:*"
            ),
        },
    }
    DIVIDER_BLOCK = {"type": "divider"}

    def __init__(self, channel):
        self.channel = channel
        self.username = "Craigslist Bot"
        self.icon_emoji = ":house_buildings:"
        self.timestamp = ""
        self.reaction_task_completed = False
        self.pin_task_completed = False

    def get_message_payload(self, address: str):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self.WELCOME_BLOCK,
                self.DIVIDER_BLOCK,
                *self._get_listing_block(address),
                self.DIVIDER_BLOCK
            ],
        }

    def _get_listing_block(self, address: str):
        text = (
            "House Address: " + address
        )
        information = (
            "House Details: "
        )
        return self._get_task_block(text, information)

    @staticmethod
    def _get_task_block(text, information):
        return [
            {"type": "section", "text": {"type": "mrkdwn", "text": text}},
            {"type": "context", "elements": [{"type": "mrkdwn", "text": information}]},
        ]
