from app.memory.memory import Memory
from app.tools.faq_tool import FAQTool
from app.llm.llm_service import LLMService

from app.prompts.system_prompts import SYSTEM_PROMPT
from app.prompts.intent_prompts import INTENT_CLASSIFICATION_PROMPT
from app.prompts.generation_prompts import GENERATION_PROMPT_TEMPLATE


class Agent:

    def __init__(self):
        self.memory = Memory()
        self.faq_tool = FAQTool()
        self.llm = LLMService()

    def handle_message(self, user_id: str, message: str) -> str:

        # 1️⃣ Get conversation history
        history = self.memory.get_last_messages(user_id)

        # 2️⃣ Intent Classification (LLM Call 1)
        intent = self.llm.classify_intent(
            system_prompt=INTENT_CLASSIFICATION_PROMPT,
            user_message=message
        )

        # 3️⃣ FAQ Tool Check (only if classified as faq)
        if intent == "faq":
            faq_answer = self.faq_tool.lookup(message)
            if faq_answer:
                self.memory.add_message(user_id, message, faq_answer)
                return faq_answer

        # 4️⃣ Generation (LLM Call 2)

        # Format history into readable string
        formatted_history = ""
        for msg in history:
            formatted_history += f"User: {msg['user']}\nAssistant: {msg['assistant']}\n"

        user_prompt = GENERATION_PROMPT_TEMPLATE.format(
            history=formatted_history,
            message=message
        )

        response = self.llm.generate(
            system_prompt=SYSTEM_PROMPT,
            user_prompt=user_prompt
        )

        # 5️⃣ Save conversation
        self.memory.add_message(user_id, message, response)

        return response
