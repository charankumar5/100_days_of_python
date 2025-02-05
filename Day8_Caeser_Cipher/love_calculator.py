def calculate_love_score(name1, name2):
  # your code here
    final_name = (name1 + name2).upper()
    true_occurance = 0
    for letter in "TRUE":
        for match in final_name:
            if letter == match:
                true_occurance +=1
    print(true_occurance, end="")
    love_occurance = 0
    for letter in "LOVE":
        for match in final_name:
            if letter == match:
                love_occurance +=1
    print(love_occurance, end="")
 
# Call your function with hard coded values
calculate_love_score("Kanye West", "Kim Kardashian")