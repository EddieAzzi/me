# -*- coding: UTF-8 -*-
"""Refactoring.

This exercise contains a complete and working example, but it's very poorly written.

Your job is to go through it and make it as good as you can.

That means making it self-documenting wherever possible, adding comments where
it isn't. Take repeated code and make it into a function. Also use functions
to encapsulate concepts. If something is done many times, maybe a map or a loop
is called for. Etc.

Some functions will have directions as external comments, once you think you
are on top of it, take these comments out. Others won't have comments and
you'll need to figure out for yourself what to do.
"""
import math

# return a list of countdown messages, much like in the bad function above.
# It should say something different in the last message.
def countdown(message, start, stop, completion_message):
    countdown = []
    for i in range(start,stop-1,-1):
        print(message + " " + str(i))
        countdown.append(message + " " + str(i))
    print(completion_message)
    countdown.append(completion_message)
    return countdown

# TRIANGLES

# This should be a series of functions that are ultimatly used by
# triangle_master
# It should eventually return a dictionary of triangle facts. It should
# optionally print information as a nicely formatted string. Make printing
# turned off by default but turned on with an optional argument.
# The stub functions are made for you, and each one is tested, so this should
# hand hold quite nicely.
def calculate_hypotenuse(base, height):
    hyp = math.sqrt(base ** 2 + height ** 2)
    #print("Calculalte hyp: base, height = " + str(base) + " " + str(height) + " " + str(hyp))
    return hyp


def calculate_area(base, height):
    area = 0.5 * (base * height)
    #print("area = " + str((base * height) / 2))
    return area


def calculate_perimeter(base, height):
    hyp = calculate_hypotenuse(base, height)
    perimeter = base + height + hyp
    return perimeter


def calculate_aspect(base, height):
    #c = calculate_hypotenuse(base, height)
    #s = 0.5 * (base + height + c)
    #aspect = (base * height * c) / ((8) * (s - base) * (s - height) * (s - c))
    if (base == height):
        return "equal"
    elif ( base < height):
        return "tall"
    else:
        return "wide"


# Make sure you reuse the functions you've already got
# Don't reinvent the wheel
def get_triangle_facts(base, height, units="mm"):
    return {
        "area": calculate_area(base, height),
        "perimeter": calculate_perimeter(base, height),
        "height": height,
        "base": base,
        "hypotenuse": calculate_hypotenuse(base, height),
        "aspect": calculate_aspect(base, height),
        "units": units,
    }


# this should return a multi line string that looks a bit like this:
#
# 15
# |
# |     |\
# |____>| \  17.0
#       |  \
#       |   \
#       ------
#       8
# This triangle is 60.0mm²
# It has a perimeter of 40.0mm
# This is a tall triangle.
#
# but with the values and shape that relate to the specific
# triangle we care about.
def tell_me_about_this_right_triangle(facts_dictionary):
    tall = """
            {height}
            |
            |     |\\
            |____>| \\  {hypotenuse}
                  |  \\
                  |   \\
                  ------
                  {base}"""
    wide = """
            {hypotenuse}
             ↓         ∕ |
                   ∕     | <-{height}
               ∕         |
            ∕------------|
              {base}"""
    equal = """
            {height}
            |
            |     |⋱
            |____>|  ⋱ <-{hypotenuse}
                  |____⋱
                  {base}"""

    b = facts_dictionary.get("base")
    h = facts_dictionary.get("height")
    text = ""
    aspect = ""
    if (b == h):
        text = equal
        aspect = "equal"
    elif ( b < h):
        text = tall
        aspect = "tall"
    else:
        text = wide
        aspect = "wide"

    pattern = (
        "This triangle is {area}{units}²\n"
        "It has a perimeter of {perimeter}{units}\n"
        "This is a " + aspect + " triangle.\n"
    )

    facts = text.format(**facts_dictionary) + "\n" + pattern.format(**facts_dictionary)
    return facts


def triangle_master(base, height, return_diagram=False, return_dictionary=False):
    if return_diagram and return_dictionary:
        return {"diagram": tell_me_about_this_right_triangle(get_triangle_facts(base, height, units="mm")), "facts": get_triangle_facts(base, height, units="mm")}
    elif return_diagram:
        return tell_me_about_this_right_triangle(get_triangle_facts(base, height, units="mm"))
    elif return_dictionary:
        return get_triangle_facts(base, height, units="mm")
    else:
        print("You're an odd one, you don't want anything!")

def wordy_pyramid(api_key):
    import requests
    
    pyramid_list = []
    for i in range(3, 21, 2):
        word = get_a_word_of_length_n(i)
        pyramid_list.append(word)
    for i in range(20, 3, -2):
        word = get_a_word_of_length_n(i)
        pyramid_list.append(word)
    return pyramid_list


def get_a_word_of_length_n(length):
    import requests
    baseURL = (
        "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?"
        "wordlength={length}" 
        # "http://api.wordnik.com/v4/words.json/randomWords?"
        # "api_key=n8o442zwoedg02xlpw8bqb0d9zz2sqz6nl03g4otebnjabpew"
        # "&minLength={length}"
        # "&maxLength={length}"
        #"&limit=1"
    )
        
    url = baseURL.format(length=length)
    r = requests.get(url)
    if r.status_code is 200:
        return r.text
    else:
        print("failed a request", r.status_code, length)


def list_of_words_with_lengths(list_of_lengths):    
    word_list = []
    for i in list_of_lengths:
        word = get_a_word_of_length_n(i)
        word_list.append(word)
    return word_list

if __name__ == "__main__":
    #do_bunch_of_bad_things()
    wlist = wordy_pyramid("n8o442zwoedg02xlpw8bqb0d9zz2sqz6nl03g4otebnjabpew")
    for word in wlist:
        print(word)

