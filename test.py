from UnlimitedGPT import ChatGPT
import sys
sys.path.append("../")
from globalvars import get_session_token, get_conversation_id

session_token = get_session_token()
conversation_id = "2bf0f184-fc44-4494-b977-b25a95f13dc0"

api = ChatGPT(
    session_token,
    conversation_id=conversation_id,
    proxy=None,
    chrome_args=[],
    disable_moderation=False,
    verbose=True
)

message = api.send_message(
    "Tell a joke.",
    input_mode="SLOW",  # Can be INSTANT or SLOW
    input_delay=0.0001
)
print(message.response, message.conversation_id)
