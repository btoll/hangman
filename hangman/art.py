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


def _head():
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


def _torso():
    print("   |                      |")
    print("   |                      |")
    print("   |                      |")
    print("   |                      |")
    print("   |                      |")


def _one_arm():
    print("   |                      |")
    print("   |                   \  |")
    print("   |                    \ |")
    print("   |                     \|")
    print("   |                      |")


def _two_arms():
    print("   |                      |")
    print("   |                   \  |  /")
    print("   |                    \ | /")
    print("   |                     \|/")
    print("   |                      |")


def _one_leg():
    print("   |                      |")
    print("   |                      |")
    print("   |                     /")
    print("   |                    /")
    print("   |                   /")


def _two_legs():
    print("   |                      |")
    print("   |                      |")
    print("   |                     / \\")
    print("   |                    /   \\")
    print("   |                   /     \\")


def _spacer():
    print("   |")
    print("   |")
    print("   |")
    print("   |")
    print("   |")


hanging_man = (
    [_head, _spacer, _spacer, scaffold_base],
    [_head, _torso, _spacer, scaffold_base],
    [_head, _one_arm, _spacer, scaffold_base],
    [_head, _two_arms, _spacer, scaffold_base],
    [_head, _two_arms, _one_leg, scaffold_base],
    [_head, _two_arms, _two_legs, scaffold_base]
)


def draw(index):
    """
    Draws the scaffold and the current state of the hanging man.

    :param index: The index into the `hanging_man` tuple.
    :type index: int
    """

    for piece in hanging_man[index]:
        piece()


def draw_all():
    """
    Draws the entire scaffold and the whole hanging man.

    """

    draw(len(hanging_man) - 1)


def start():
    """
    Draws a new scaffold, minus any piece of the hanging man.

    """

    scaffold_top_and_middle()
    scaffold_base()
