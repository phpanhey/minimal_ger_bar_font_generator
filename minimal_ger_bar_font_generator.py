import svgwrite
import os

def main():
    abc = {
    'A': '#0069b4', 
    'B': '#FF0000', 
    'C': '#00FF00', 
    'D': '#2f4f30', 
    'E': '#191970', 
    'F': '#FF00FF', 
    'G': '#411273', 
    'H': '#009a93', 
    'I': '#312783', 
    'J': '#FF6347', 
    'K': '#808080', 
    'L': '#00FA9A', 
    'M': '#FFA07A', 
    'N': '#1E90FF', 
    'O': '#FFD700', 
    'P': '#511b54', 
    'Q': '#92580c', 
    'R': '#21339e', 
    'S': '#4682B4', 
    'T': '#40E0D0', 
    'U': '#0a8b4d', 
    'V': '#ffed00', 
    'W': '#d74d55', 
    'X': '#703034', 
    'Y': '#f3a600', 
    'Z': '#9c5f65' ,
    }

    create_directories()

    for char, hash in abc.items():
        create_uppercase_lowercase_svg(char,hash)

def create_directories():
    upper_directory = 'upper'
    lower_directory = 'lower'
    if not os.path.exists(upper_directory):
        os.makedirs(upper_directory)  
    if not os.path.exists(lower_directory):
        os.makedirs(lower_directory)  

def create_uppercase_lowercase_svg(character,color):
    upper_svg = f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 -1000 1000 1000'>  <path fill='{color}' d='M50 92V-692H241V92Z'/> </svg>"
    lower_svg = f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 -1000 1000 1000'>  <path fill='{color}' d='M50 86V-479H242V86Z'/> </svg>"
    
    with open(f"upper/{character.upper()}.svg", "w") as file:    
        file.write(upper_svg)

    with open(f"lower/{character.lower()}.svg", "w") as file:    
        file.write(lower_svg)

if __name__ == '__main__':
    main()