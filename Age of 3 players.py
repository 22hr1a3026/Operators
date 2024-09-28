"""
It were the days of domination from the traditional metros in the team selections and everytime the team is announced for the Indian Squad, mere disappointment was left with this small town player. Dhoni’ill fate continued even during the team selections for the India A squad to tour to Zimbabwe.3 new players from Mumbai were on the list for the Indian team and it was claimed by the selectors that Dhoni was a bit younger than the 3 selected players.
  Assume the 3 players are Named X,Y and Z. The ages of the players X and Y are the same and the age of the Z is 10 more than other 2 players. Given the total age of the 3 players, find the age of the 3 players.
Input format:
First line of the input is an integer that corresponds to the total age of the 3 players.
Output format:
Output should display the ages of the three players in 3 lines. The age of the eldest player should be displayed in the last line.
Sample input and output 1:
70
20
20
30
Sample input and output 2:
100
30
30
40
7)
You are given principal amount, rate of interest per annum, and time in years. You need to calculate the simple interest.
Input and Output Format
Input Format:
The first line contains the principal amount (principal).
The second line contains the rate of interest (rate) per annum.
The third line contains the time (time) in years.
Output Format:
A single line containing the simple interest calculated.
Sample Input 1
1000
5
2
Sample Output 1
100.0
Sample Input 2
5000
8.5
3
Sample Output 2
1275.0
Sample Input 3
5000
8.5
3
Sample Output 3
525.0
"""
def calculate_ages(total_age):
    # Calculate age of players
    a = (total_age - 10) // 3
    x_age = y_age = a
    z_age = a + 10

    return x_age, y_age, z_age

def calculate_simple_interest(principal, rate, time):
    # Calculate simple interest
    simple_interest = (principal * rate * time) / 100
    return simple_interest

# Input for ages of players
total_age = int(input("Enter the total age of the three players: "))
x_age, y_age, z_age = calculate_ages(total_age)

# Output ages
print(x_age)
print(y_age)
print(z_age)

# Input for simple interest
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
simple_interest = calculate_simple_interest(principal, rate, time)

# Output simple interest
print(simple_interest)
