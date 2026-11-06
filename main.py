from groq import generate_response

def reinforcement_learning_activity():
    print("\n=== Reinforcement Learning Activity ===\n")
    prompt = input("Enter a prompt for the AI model (eg., 'Describe the lion')").strip()
    if not prompt:
        print("Please enter a prompt to run the activity.")
        return
    
    initial_response = generate_response(prompt, temperature=0.3, max_tokens=1024)
    print(f"\nInitial AI Response: {initial_response}")

    try:
        rating= int(input("\nRate the response on a scale of 1 to 5 (1=Poor, 5=Excellent): ").strip())
        if rating <1 or rating >5:
            print("Invalid rating. Using 3.")
            rating = 3
    except ValueError:
        print("Invalid input. Using 3.")
        rating = 3

    feedback = input("Provide feedback for the AI model for improvement: ").strip()
    improved_prompt = f"{initial_response} (improved with your feedback: {feedback})"
    improved_response = generate_response(improved_prompt, temperature=0.3, max_tokens=1024) 
    print(f"\nImproved AI Response: {improved_response}")

    print("\nReflection:")
    print("1. How did the model's response with the feedback?")
    print("2. How does reinforcement learning help improve AI models?")

def role_based_prompt_activity():
    print("\n=== Role-Based Prompt Activity ===\n")
    category= input("Enter a category (eg., science, history, maths): ").strip()
    item=input(f"Enter a specific {category} topic (eg., 'Quantum Mechanics' for science): ").strip()

    if not category or not item:
        print("Please fill in both fields to run the activity.")
        return

    #teacher_prompt = f"You are a teacher. Explain {item} in simple terms."
    expert_prompt = f"You are an expert in {category}. Explain {item} in a detailed and technical manner."

    #teacher_response = generate_response(teacher_prompt, temperature=0.3, max_tokens=1024)
    expert_response = generate_response(expert_prompt, temperature=0.3, max_tokens=1024)

    #print(f"\n---- Teacher's Perspective -----\n {teacher_response}")
    print(f"\n---- Expert's Perspective -----\n {expert_response}")

    print("\nReflection:")
    print("1. How did the AI's response differ between the teacher's and expert's perspectives?")
    print("2. How can role-based prompts help tailor AI responses for different contexts?")

def run_activity():
    print("\n=== AI Learning Activities ===\n")
    print("Choose an activity to run:")
    print("1) Reinforcement Learning Activity")
    print("2) Role-Based Prompts")
    choice =input("> ").strip()
    if choice == "1":
        reinforcement_learning_activity()
    elif choice == "2":
        role_based_prompt_activity()
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    run_activity()