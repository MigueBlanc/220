from sales_person import SalesPerson


class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        file = open(file_name, "r")
        content = file.read()
        content = content.replace("\n", ", ")
        self.sales_people.append(content)

    def quoata_report(self, quota):
        people_list = []
        for person in self.sales_people:
            people_list.append([person.get_id(), person.get_name(), person.get_sales, person.met_quota(quota)])
            # if person.met_quota(quota):
            #     people.append([person.get_name()])
        return people_list

    def top_seller(self):
        top_seller = []
        for i in range(len(self.sales_people)):
            highest = self.sales_people[i].get_sales()
            pos = i
            for index in range(i, len(self.sales_people)):
                if self.sales_people[i].get_sales() > self.sales_people[highest]:
                    highest = self.sales_people[index]
                    pos = index
                self.sales_people[i], self.sales_people[pos] = self.sales_people[pos], self.sales_people[i]
        top_seller.append(self.sales_people[0])
        for other in range(1, len(self.sales_people)):
            if self.sales_people[other].get_sales() == top_seller[0].get_sales():
                top_seller.append(self.sales_people[other])
        return top_seller

    def individual_sales(self, employeeid):
        for person in self.sales_people:
            if person.get_id() == employeeid:
                return None
        return employeeid
