import os
from dotenv import load_dotenv
from agents import Agent , Runner , OpenAIChatCompletionsModel , AsyncOpenAI , set_tracing_disabled
import rich

load_dotenv()
set_tracing_disabled(disabled=True)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# ---------------

client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


translator_agent = Agent(
    name="Translator agent", 
    instructions = "You are a translator agent. Translate Urdu to English, English to Urdu, Urdu to Sindhi, Urdu to Punjabi etc.",
    model=OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=client
    )
)

# ----------------

result = Runner.run_sync(
    starting_agent=translator_agent,
    input = "Translate this into English: تعلیم ہمیں اچھے برے کی پہچان کراتی ہے۔ تعلیم کے بغیر زندگی ادھوری ہے۔"
)

rich.print(result.final_output)
