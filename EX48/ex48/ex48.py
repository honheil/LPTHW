class Lexicon(object):
    def scan(self, userinput):
        #first split up input into a list of words.
        words = userinput.split()
        output = []
        #next go through the list, for each word give it a label
        #from a list of words for each label
        for item in words:
            result = self.label(item)
            output.append(result)
           # Return a list of all of these labelled words
        return output

    def label(self, item):
        #label the item and package it up in a tuple
        if item in ['north', 'south', 'east']:
            return ('direction', item)
        elif item in ['go', 'kill', 'eat']:
            return ('verb', item)
        elif item in ['the', 'in', 'of']:
            return ('stop', item)
        elif item in ['bear', 'princess']:
            return ('noun', item)
        else:
            try:
                number = int(item)
                return ('number', number)
            except ValueError:
                return ('error', item)
                # What else could it be

            #test if its a direction
            #test if its an verb
            #test if its a stop
            #test if its a noun

lexicon = Lexicon()
