def is_valid_mobile(number):
    current_state = 'q0'
    valid_states = {'q11'}  # Asl shode be q11

    for char in number:
        if current_state == 'q0':
            current_state = 'q1' if char == '0' else 'q_dead'
        elif current_state == 'q1':
            current_state = 'q2' if char == '9' else 'q_dead'
        elif current_state in ['q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10']:
            if char.isdigit():
                next_state_num = int(current_state[1:]) + 1
                current_state = f'q{next_state_num}'
            else:
                current_state = 'q_dead'
        elif current_state == 'q11':  # Hâlât jadid barâye pardâzesh karaktere 11om
            current_state = 'q_dead'  # Agar tool-e shomâre bishtar az 11 ragham bâshad
        else:
            break  # Vâred hâlât morde shodim

    return current_state in valid_states and len(number) == 11  # Asl shart-e tool

# Test
numbers = [
    '09123456789',  # Mo'tabar
    '0912345678',   # Namo'tabar (10 raghami)
    '0912A56789',   # Namo'tabar (harf-e A)
    '08912345678',  # Namo'tabar (shoroo' ba 089)
    '091234567890'  # Namo'tabar (12 raghami)
]

for num in numbers:
    print(f'{num}: {"✅ Mo'tabar" if is_valid_mobile(num) else "❌ Namo'tabar"}')