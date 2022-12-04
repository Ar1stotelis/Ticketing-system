class Labels:
    ticket_labels = []

    def __init__(self, labels_array):
        self.ticket_labels = labels_array.copy()

    def add_label(self):
        label_input = input("Please, enter the name of the new label :")
        self.ticket_labels.append(label_input)

    def delete_label(self):
        i = int(1)
        j = int(0)
        for n in self.ticket_labels:
            print(i, ". ", self.ticket_labels[j])
            i+=1
            j+=1



        i = int(input("Please, choose the label you wish to delete : "))
        j = 0
        flag = False
        i-= 1
        while(i > -1 and i < len(self.ticket_labels)):
            if i == j:
                del self.ticket_labels[j]
                i = -1
                flag = True
            j+= 1

        if flag:
            print("Label deleted")

    def print_labels(self):
        print(self.ticket_labels)
