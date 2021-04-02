def scaffold_top_and_middle():
    print("\n\tLET'S PLAY HANGMAN!")
    print("")
    print("   ------------------------")
    print("   |                      |")
    print("   |                      |")
    print("   |                      |")
    print("   |")
    print("   |")
    print("   |")
    print("   |")
    print("   |")
    print("   |")
    print("   |")
    print("   |")
    print("   |")
    print("   |")
    print("   |")
    print("   |")
    print("   |")
    print("   |")


def scaffold_base():
    print("   |")
    print("   |")
    print("   |")
    print("   |=====================================|")
    print("   |=====================================|")
    print("   |                                     |")
    print("   |                                     |")
    print("   |                                     |")


def head():
    print("\n\tLET'S PLAY HANGMAN!")
    print("")
    print("   ------------------------")
    print("   |                      |")
    print("   |                      |")
    print("   |                     _|_")
    print("   |                    /   \\")
    print("   |                   {     }")
    print("   |                    \___/")
    print("   |                      |")


def torso():
    print("   |                      |")
    print("   |                      |")
    print("   |                      |")
    print("   |                      |")
    print("   |                      |")


def one_arm():
    print("   |                      |")
    print("   |                   \  |")
    print("   |                    \ |")
    print("   |                     \|")
    print("   |                      |")


def two_arms():
    print("   |                      |")
    print("   |                   \  |  /")
    print("   |                    \ | /")
    print("   |                     \|/")
    print("   |                      |")


def one_leg():
    print("   |                      |")
    print("   |                      |")
    print("   |                     /")
    print("   |                    /")
    print("   |                   /")


def two_legs():
    print("   |                      |")
    print("   |                      |")
    print("   |                     / \\")
    print("   |                    /   \\")
    print("   |                   /     \\")


def spacer():
    print("   |")
    print("   |")
    print("   |")
    print("   |")
    print("   |")


hanging_man = (
    [head, spacer, spacer, scaffold_base],
    [head, torso, spacer, scaffold_base],
    [head, one_arm, spacer, scaffold_base],
    [head, two_arms, spacer, scaffold_base],
    [head, two_arms, one_leg, scaffold_base],
    [head, two_arms, two_legs, scaffold_base]
)


def draw(index):
    for piece in hanging_man[index]:
        piece()


def draw_all():
    draw(len(hanging_man) - 1)


def start():
    scaffold_top_and_middle()
    scaffold_base()
