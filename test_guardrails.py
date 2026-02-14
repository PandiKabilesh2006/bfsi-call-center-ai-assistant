from src.guardrails import run_guardrails

query=input("Enter query: ")

blocked,message=run_guardrails(query)

if blocked:
    print("\nBlocked:")
    print(message)
else:
    print("\nQuery is safe.")
