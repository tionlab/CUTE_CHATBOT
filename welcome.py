class Welcome:
    def __init__(self):
        welcome = '''
        ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬛⬛⬛⬛⬛⬜⬜⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬛⬜⬛⬜⬜⬛⬜⬛⬛⬛⬜⬛⬜⬜🏽⬛⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬛⬜🏽⬜⬛⬜⬜⬛⬛⬛⬜⬛⬛⬜🏽🏽⬛⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬛⬜🏽🏽⬜⬛⬛⬛⬛⬛⬛⬛⬛🏽⬛🏽⬛⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬛⬜🏽🏽🏽⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬛⬜🏽⬛⬛⬛⬛⬛⬛⬛🏽⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬛⬛🏽⬛⬛⬛⬛⬛⬛⬛🏽⬜⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬜⬜⬜⬜
        ⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛🏽⬜⬜⬜⬜⬜⬛⬜🏽⬛⬛⬛⬛⬜⬛⬛⬜
        ⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬜⬜⬛
        ⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬛⬜⬜⬛⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬛
        ⬜⬜⬛⬜⬜⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜🏽⬜⬜⬛⬛⬛⬛⬜⬜⬛⬜
        ⬜⬜⬛⬜⬜⬜⬛⬛⬛⬛🏽⬜⬜⬜⬛⬜⬜⬛⬛⬜⬜⬛⬛⬛⬛⬛⬛⬜⬜
        ⬜⬜⬜⬛⬜⬜⬛⬛⬛⬛⬛⬜⬜⬜⬜⬛⬛⬜⬜⬜⬛⬛⬛⬛⬛⬜⬜⬜⬜
        ⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜
        ⬜⬛⬛⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜
        ⬛⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛🟦⬛🏽🏽🏽⬛⬛⬜⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜
        ⬛⬜⬜⬜⬜🏽⬜🟦⬛⬛⬛🟦🟦⬛⬛🟦🟦⬛⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜
        ⬜⬛⬜⬜🏽⬜⬜🟦🟦⬛⬛🟦🟦🟦🟦🟦🟦⬛⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜
        ⬜⬜⬛⬛⬛⬜⬜🟦🟦🟦⬛🟦🟦🟦⬛🟦🟦⬛⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬛⬜⬜🟦🟦🟦🟦🟦🟦⬛🟦🟦⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬛⬜⬜⬛⬛⬛⬜⬜⬛⬛⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬛⬜⬛⬜⬜⬜⬛⬜⬛⬜⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬛⬛⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜'''
        print(welcome)

