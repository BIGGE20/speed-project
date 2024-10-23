def get_attribute(query,default):
    answer = input(query)
    if answer == "":
        answer = default
    print('you chose',answer)
    return answer


hair_color = get_attribute("what is the color of your hair?:","black")
hair_length = get_attribute("what is your hair length?[long or short]: ",'short')
eye_color = get_attribute("what is your eye color?: ",'brown')
gender = get_attribute("are you male or female?: ",'male')
location = get_attribute("where are you located","lagos, Nigeria")

print(f"you are a {eye_color} eyed {gender} with lovely {hair_length} {hair_color}hair. Living in {location}..")
