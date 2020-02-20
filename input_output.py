

class Data:
    def __init__(self, no_of_diff_books, libraries, no_of_signup_days):
        self.no_of_diff_books = no_of_diff_books
        self.libraries = libraries
        self.no_of_signup_days = no_of_signup_days

    def get_no_of_diff_books(self):
        return self.no_of_diff_books

    def get_libraries(self):
        return self.libraries

    def get_no_of_signup_days(self):
        return self.no_of_signup_days


class Library:
    def __init__(self, no_of_books, set_of_books, prepare_time, daily_scan_cap):
        self.no_of_books = no_of_books
        self.set_of_books = set_of_books
        self.prepare_time = prepare_time
        self.daily_scan_cap = daily_scan_cap

    def get_no_of_books(self):
        return self.no_of_books

    def get_set_of_books(self):
        return self.set_of_books

    def get_prepare_time(self):
        return self.prepare_time

    def get_daily_scan_cap(self):
        return self.daily_scan_cap


def clean_line(line):
    first_line = line.split(" ")
    first_line[-1] = first_line[-1].rstrip()
    return first_line


def read_file(filepath):
    libraries = []
    with open(filepath) as fp:
        # READ FIRST LINE
        line = fp.readline()
        line = clean_line(line)
        no_of_diff_books = int(line[0])
        no_of_libraries = int(line[1])
        no_of_signup_days = int(line[2])

        # READ SECOND LINE
        line = fp.readline()
        line = clean_line(line)
        books = dict(map(lambda t: (t[0], int(t[1])), enumerate(line)))

        for library_index in range(no_of_libraries):
            # READ FIRST LIBRARY LINE
            lib_line = fp.readline()
            lib_line = clean_line(lib_line)
            no_of_books = int(lib_line[0])
            prepare_time = int(lib_line[1])
            daily_scan_cap = int(lib_line[2])

            # READ SECOND LIBRARY LINE
            lib_line = fp.readline()
            lib_line = clean_line(lib_line)
            lib_books = {int(x): books[int(x)] for x in lib_line}
            libraries.append(Library(no_of_books, lib_books, prepare_time, daily_scan_cap))

        return Data(no_of_diff_books, libraries, no_of_signup_days)


def output(libraries):
    f = open("output/output_file.txt", "w+")
    f.write(str(len(libraries)))
    f.write("\n")
    for i, library in enumerate(libraries):
        f.write(str(i) + " " + str(library.get_no_of_books()) + "\n")
        for j, book in enumerate(library.get_set_of_books()):
            if j == len(library.get_set_of_books()) - 1:
                f.write(str(book[0]))
            else:
                f.write(str(book[0]) + " ")
        f.write("\n")


def get_data():
    data = read_file('data/a_example.txt')
    return data

    # libraries = data.get_libraries()
    # print(libraries)
    # output(libraries)


# if __name__ == "__main__":
#     get_data()
