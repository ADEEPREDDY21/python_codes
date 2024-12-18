def disease_diagnosis():
    print("Welcome to the Disease Diagnosis Expert System!")
    print("Answer the following questions with 'yes' or 'no'.\n")
    
    # Collect symptoms as facts
    symptoms = {}
    symptoms['fever'] = input("Do you have a fever? ").strip().lower() == 'yes'
    symptoms['cough'] = input("Do you have a cough? ").strip().lower() == 'yes'
    symptoms['fatigue'] = input("Do you feel fatigued or weak? ").strip().lower() == 'yes'
    symptoms['headache'] = input("Do you have a headache? ").strip().lower() == 'yes'
    symptoms['sore_throat'] = input("Do you have a sore throat? ").strip().lower() == 'yes'
    symptoms['body_ache'] = input("Do you have body aches? ").strip().lower() == 'yes'
    symptoms['runny_nose'] = input("Do you have a runny or stuffy nose? ").strip().lower() == 'yes'
    symptoms['nausea'] = input("Do you have nausea or vomiting? ").strip().lower() == 'yes'
    symptoms['diarrhea'] = input("Do you have diarrhea? ").strip().lower() == 'yes'

    # Define rules
    rules = [
        {
            "conditions": ["fever", "cough", "fatigue", "headache"],
            "disease": "Influenza (Flu)"
        },
        {
            "conditions": ["fever", "sore_throat", "runny_nose", "body_ache"],
            "disease": "Common Cold"
        },
        {
            "conditions": ["nausea", "diarrhea", "fever"],
            "disease": "Food Poisoning"
        },
        {
            "conditions": ["fever", "cough", "fatigue", "sore_throat"],
            "disease": "COVID-19"
        }
    ]

    # Inference engine: Match facts with rules
    for rule in rules:
        if all(symptoms.get(condition, False) for condition in rule["conditions"]):
            print(f"\nBased on your symptoms, you might have: {rule['disease']}")
            print("Please consult a healthcare professional for an accurate diagnosis.")
            return

    # Default response if no rule matches
    print("\nNo specific diagnosis found based on your symptoms.")
    print("Please consult a healthcare professional for further evaluation.")

# Run the expert system
disease_diagnosis()
