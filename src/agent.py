from transformers import pipeline

# Load the model
llm = pipeline("text2text-generation", model="google/flan-t5-large")

def draft_reply_tool(comment):
    return f"📝 DRAFT REPLY: Thanks for the feedback! We are working on more content like this."

def ignore_tool():
    return "🗑️ ACTION: Ignore (Low value/Spam)"

def decide_and_act(user_input):
    prompt = f"Decide if this YouTube comment is a good engagement opportunity. Respond TOOL_REPLY or TOOL_IGNORE: {user_input}"
    decision = llm(prompt)[0]['generated_text'].strip().upper()
    
    if "REPLY" in decision:
        return draft_reply_tool(user_input)
    else:
        return ignore_tool()

if __name__ == "__main__":
    print("YouTube Agent Active.")
    sample = "This video helped me so much with Python!"
    print(f"Test Input: {sample}")
    print(decide_and_act(sample))
