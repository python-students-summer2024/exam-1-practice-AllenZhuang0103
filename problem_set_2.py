"""
Your job is to complete the definition of the function so that it achieves its indicated behavior.

Do not run this file directly.
Rather, call whichever functions defined in this file that you want to run from within the file named main.py and run that file directly.
"""

def weather_helper():
  """
  Make suggestions based on current weather conditions.

  Program logic - indentations indicate nested logic:
  - Ask the user to enter in the current temperature in degrees Farenheit (i.e. an integer between  -70 and 134, inclusive).
    - If the user enters an invalid temperature (i.e. an integer that is not within the given range), print the text "Invalid temperature!" and do not print or input anything else.
    - If the temperature the user enters is below 40, ask them whether it is snowing.
      - If it is snowing, ask the user whether they are wearing a warm jacket.
        - If the user is wearing a jacket, print the output: "Glad to hear you're dressed appropriately!"
        - If the user is not wearing a jacket, print the output: "What were you thinking when you left home today?!"
      - If it is not snowing, ask the user whether it is raining.
        - If it is raining, ask the user whether they have an umbrella.
          - If the user has an umbrella, print the output: "Good job staying dry!"
          - If the user does not have an umbrella, print the output: "You must enjoy getting wet!"
    - If the temperature is above 90, ask the user whether they have air conditioning.
      - If the user has air conditioning, print the output: "Stay cool indoors."
      - If the user does not have air conditioning, print the output: "I hope you have a fan."

  Additional requirements:
    1. You can assume the user will enter an integer for the temperature.
    2. Assume the user will respond to any yes/no question with an affirmative response such as "yes", "yeah", "yup"; or a negative response such as "no", "nah", or "nope".
    3. Do not print anything more than what is requested in the instructions.
    4. The capitalization of the user's responses must not matter to the outcome of the program.
  """
  temperature = int(input("Enter in the current temperature in degrees Farenheit: "))
  if temperature < -70 or temperature > 134:
    print("Invalid temperature!")
  else:
    if temperature < 40:
      answer_of_snowing = input("Whether it is snowing? ").lower()
      if answer_of_snowing in ["yes", "yeah", "yup"]:
        wearing_a_jacket = input("Whether are you wearing a warm jacket? ").lower()
        if wearing_a_jacket in ["yes", "yeah", "yup"]:
          print("Glad to hear you're dressed appropriately!")
        elif wearing_a_jacket in ["no", "nah", "nope"]:
          print("What were you thinking when you left home today?!")
      elif answer_of_snowing in ["no", "nah", "nope"]:
        answer_of_raining = input("Whether it is raining? ").lower()
        if answer_of_raining in ["yes", "yeah", "yup"]:
          umbrella = input("Whether do you have an umbrella? ").lower()
          if umbrella in ["yes", "yeah", "yup"]:
            print("Good job staying dry!")
          elif umbrella in ["no", "nah", "nope"]:
            print("You must enjoy getting wet!")
    elif temperature > 90:
      airconditioning = input("Whether of you have an airconditioning? ").lower()
      if airconditioning in ["yes", "yeah", "yup"]:
        print("Stay cool indoors.")
      elif airconditioning in ["no", "nah", "nope"]:
        print("I hope you have a fan.")
