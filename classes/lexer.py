from re import match


class Lexer:
    """
    The job of the tokenizer is to
    read tokens one at a time from the input stream and pass the tokens to the parser.

    Also: determine type of the token
    """
    def read(self, user_string):
        # I.e. I gotta go symbol by symbol to properly split tokens
        raw_tok_list = user_string.split(' ')

        token_list = []
        for tok in raw_tok_list:
            tok_type = self.get_tok_type(tok)
            token_list.append({
                    'token': tok,
                    'type': tok_type
                })
        print(token_list)
        return token_list

    def get_tok_type(self, token):
        glob_res_words = ('all', 'from', 'in', 'for', 'with')
        ctx_res_words = ('???')

        types_map = {
            'glob_res_word': glob_res_words,
            'ctx_res_word': ctx_res_words,
        }

        #           (* glob_res_word_table is a table (possibly a     *)
        #           (* binary search tree) of reserved words.         *)
        # wx: BST?

        for type, map in types_map.items():
            if token in map:
                return type

        # if it's not in map - it's likely an identifier
        if match('[0-9]+', token):
            return 'number'

        if match("['a-zA-Z0-9,./\\_\-?!\'\"']+", token):    # wx: bad regex, better incl all punctuation
            return 'string'

        return 'unknown'

    # def please(self):
    #     """
    #     Find please - raise query priority :-)
    #     :return:
    #     """

# Recommended re-reading:
# http://www.cs.man.ac.uk/~pjj/farrell/comp3.html
# (ctrl+f 'ivory t', have a laugh)
