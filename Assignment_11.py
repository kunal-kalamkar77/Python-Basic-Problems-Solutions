#Problem Statement - There was a set of cards with numbers from 1 to N.
#  One of the card is now lost. Determine the number on that lost card given the numbers for the remaining cards. 
# Given a number N, followed by N − 1 integers - representing the numbers on the remaining cards 
# (distinct integers in the range from 1 to N). Find and print the number on the lost card.
N = int(input("Enter the total number of cards (N): "))
remaining_cards = list(map(int, input(f"Enter the numbers on the remaining {N-1} cards (separated by space): ").split()))
total_sum = N * (N + 1) // 2
remaining_sum = sum(remaining_cards)
lost_card = total_sum - remaining_sum
print(f"The number on the lost card is: {lost_card}")
