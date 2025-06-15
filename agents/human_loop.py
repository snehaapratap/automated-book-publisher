def get_human_input(spun, reviewed):
    print("AI Writer Output:\n", spun)
    print("AI Reviewer Output:\n", reviewed)
    return input("Enter any manual edits or press Enter to accept reviewed version:\n") or reviewed
