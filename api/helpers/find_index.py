class FindIndex():

    def __init__(self, i, data):
        '''
            indice de entrada e o texto a ser processado.
        '''
        self.i, self.data = (i, data)

    def validation_data(self):
        '''
            Valida se o indice de entrada corresponde ao brackets de abertura
        '''
        return True if self.data[self.i] == '[' else False

    def get_index(self):
        '''
            Retorna o indice de fechamento do brackets
        '''
        self.i += 1
        count = 0
        for index in range(self.i, len(self.data)):
            if self.data[index] == '[':
                count += 1

            elif self.data[index] == ']':
                if count == 0:
                    return index
                count -= 1
