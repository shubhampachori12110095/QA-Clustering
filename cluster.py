class Cluster:

    def __init__(self, title=""):
        self.title = title
        self.records = []

    # def __str__(self):
    #     res = "    " + self.title + ":\n"
    #     res += "    " + '-' * (len(self.title) + 1) + '\n'
    #     for doc in self.documents:
    #         res += doc[1] + '\n'
    #     res += '\n'
    #     return res
    #
    # def print(self, top_n=-1):
    #     if top_n < 0 or top_n > len(self.documents):
    #         top_n = len(self.documents)
    #     print("    " + self.title + ":\n")
    #     print("    " + '-' * (len(self.title) + 1) + '\n')
    #     for i in range(top_n):
    #         print(self.documents[i][1] + '\n')
    #     print('\n')
