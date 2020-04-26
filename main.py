#!/usr/bin/env python3
"""
Have fun trying to get max complex query expressed by imperfect human language :-)
"""

from classes import parser as p, lexer as l, translator as t


def main():
    try:
        while True:
            print("Hi. Please enter your query: ")
            user_string = input()
            if not user_string:
                example_query = "all users sorted by id desc"
                print("We need something better than that. Try: {}".format(example_query))

            lexer = l.Lexer()
            parser = p.Parser()
            translator = t.Translator()

            token_list = lexer.read(user_string)
            ast = parser.parse(token_list)
            query = translator.translate(ast)

            print(query)
            exit("Remove this exit after debug")

    except KeyboardInterrupt:
        print("Thanks. Goodbye.")


if __name__ == '__main__':
    main()
