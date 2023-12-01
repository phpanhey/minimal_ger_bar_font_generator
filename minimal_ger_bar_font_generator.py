import os

def main():
    abc = {
    'A' : 	'#0174df',
    'B' :	'#f14d4d',
    'C' :	'#86b404',
    'D' :	'#31b404',
    'E' :	'#0b0b3b',
    'F' :	'#951b81',
    'G' :	'#662483',
    'H' :	'#009a93',
    'I' :	'#312783',
    'J' :	'#8a181f',
    'K' :	'#585858',
    'L' :	'#0f8a09',
    'M' :	'#ea5b0c',
    'N' :	'#3558dc',
    'O' :	'#f1eb42',
    'P' :	'#511b54',
    'Q' :	'#92580c',
    'R' :	'#21339e',
    'S' :	'#055f84',
    'T' :	'#07a5b3',
    'U' :	'#0a8b4d',
    'V' :	'#cc89d4',
    'W' :	'#d74d55',
    'X' :	'#703034',
    'Y' :	'#f3a600',
    'Z' :	'#9c5f65'    
    }

    other_chars = { 
        'germandbls': '#a9f5a9', #'ß'
        'zero': '#2ECCFA', #0
        'one': '#F5A9E1', # '1'
        'two': '#D7DF01', # '2'
        'three': '#D8F781', # '3'
        'four': '#A9A9F5', # '4'
        'five': '#F78181', # '5'
        'six': '#819FF7', # '6'
        'seven': '#A9F5D0', # '7'
        'eight': '#BDBDBD', # '8'
        'nine': '#F3E2A9',  # '9'
    }

    umlauts = { 
        'adieresis' :	'#0b4c5f', # 'ä'
        'odieresis' :	'#f5a9a9', # 'ö'        
        'udieresis' :	'#a9bcf5', # 'ü'        
    }

    create_directories()

    for char, hash in abc.items():
        create_uppercase_lowercase_svg(char,hash)

    for char, hash in other_chars.items():
        create_svg(char,hash)

    for char, hash in umlauts.items():
        create_uppercase_lowercase_umlauts_svg(char,hash)

def create_directories():
    svg_directory = 'svg'
    upper_directory = f'{svg_directory}/upper_characters'
    lower_directory = f'{svg_directory}/lower_characters'
    other_chars_directory = f'{svg_directory}/other_chars'
    if not os.path.exists(svg_directory):
        os.makedirs(svg_directory)  
    if not os.path.exists(upper_directory):
        os.makedirs(upper_directory)  
    if not os.path.exists(lower_directory):
        os.makedirs(lower_directory)  
    if not os.path.exists(other_chars_directory):
        os.makedirs(other_chars_directory)  

def create_uppercase_lowercase_svg(character,color):
    upper_svg = f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 -1000 1000 1000'>  <path fill='{color}' d='M50 92V-692H241V92Z'/> </svg>"
    lower_svg = f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 -1000 1000 1000'>  <path fill='{color}' d='M50 86V-479H242V86Z'/> </svg>"
    
    with open(f"svg/upper_characters/{character.upper()}.svg", "w") as file:    
        file.write(upper_svg)

    with open(f"svg/lower_characters/{character.lower()}.svg", "w") as file:    
        file.write(lower_svg)

def create_svg(character,color):
    svg = f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 -1000 1000 1000'>  <path fill='{color}' d='M50 92V-692H241V92Z'/> </svg>"
    with open(f"svg/other_chars/{character}.svg", "w") as file:    
        file.write(svg)    

def create_uppercase_lowercase_umlauts_svg(character,color):
    upper_svg = f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 -1000 1000 1000'>  <path fill='{color}' d='M50 92V-692H241V92Z'/> </svg>"
    lower_svg = f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 -1000 1000 1000'>  <path fill='{color}' d='M50 86V-479H242V86Z'/> </svg>"
    
    with open(f"svg/upper_characters/{character.capitalize()}.svg", "w") as file:    
        file.write(upper_svg)

    with open(f"svg/lower_characters/{character.lower()}.svg", "w") as file:    
        file.write(lower_svg)

if __name__ == '__main__':
    main()