import difflib

def calculate_similarity(text1, text2):
    return difflib.SequenceMatcher(None, text1, text2).ratio()

def main():
    # Get input texts
    text1 = input("Enter the first text: ")
    text2 = input("Enter the second text: ")

    # Calculate similarity
    similarity = calculate_similarity(text1, text2)

    # Determine plagiarism threshold
    plagiarism_threshold = 0.8  # You can adjust this based on your requirements

    # Check for plagiarism
    if similarity >= plagiarism_threshold:
        print("Plagiarism detected! Similarity:", similarity)
    else:
        print("No plagiarism detected. Similarity:", similarity)

if __name__ == "__main__":
    main()
