import os
from transformers import pipeline

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

def main():
    print("==========================================")
    print("   GENERATIVE AI & HUGGING FACE   ")
    print("==========================================\n")

    print("[TASK 1] Generating Text with GPT-2...")
    gen_pipe = pipeline("text-generation", model="gpt2")
    prompt = "Large Language Models are useful because"
    gen_out = gen_pipe(prompt, max_length=50, num_return_sequences=1)
    print(f"Output: {gen_out[0]['generated_text']}\n")

    print("[TASK 2] Analyzing Sentiment...")
    sent_pipe = pipeline("sentiment-analysis")
    sent_out = sent_pipe("I am really impressed by how fast this AI generates code!")
    print(f"Sentiment: {sent_out[0]['label']} (Score: {round(sent_out[0]['score'], 4)})\n")

    print("[TASK 3] Summarizing Long Text...")
    sum_pipe = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    text = (
        "Generative AI refers to systems that can create new content such as text, images, "
        "music, or even code. These systems learn patterns from data and use them to "
        "generate new, similar content. Examples include ChatGPT and DALL-E."
    )
    sum_out = sum_pipe(text, max_length=25, min_length=10)
    print(f"Summary: {sum_out[0]['summary_text']}\n")

    print("==========================================")
    print("         TASKS COMPLETED            ")
    print("==========================================")

if __name__ == "__main__":
    main()