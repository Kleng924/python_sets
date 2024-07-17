# Python Sets Adventure
# Objective: The aim of this assignment is to deepen your understanding and application of Python sets.

# Task 1: Flight Route Comparison Imagine you work for an airline and need to compare the flight routes of 
# your airline with a competitor. You have two sets of flight destinations, one for each airline. 
# Write a Python program to find out:

# Example Code:

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# 1. Destinations that both airlines fly to
shared_destinations = our_routes.intersection(competitor_routes)
print("Destinations that both airlines fly to:", shared_destinations)

# 2. Destinations unique to your airline
unique_to_our_airline = our_routes.difference(competitor_routes)
print("Destinations unique to our airline:", unique_to_our_airline)

# 3. Whether there are any destinations that neither airline shares
all_destinations = our_routes.union(competitor_routes)
print("All destinations:", all_destinations)

complete_destinations = {"LAX", "JFK", "CDG", "DXB", "LHR", "BKK", "SFO", "SIN"}
neither_fly_to = complete_destinations.difference(all_destinations)
print("Destinations that neither airline shares:", neither_fly_to)


