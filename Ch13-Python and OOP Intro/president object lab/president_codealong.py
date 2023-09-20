

class President:
    def __init__(self, term_number):
        with open ('Ch13-Python and OOP Intro/president object lab/presidents.txt') as file:
            for line in file:
                line_list = line.split(":")
                if term_number == int(line_list[0]):
                    self._term_num = term_number
                    self._last_name = line_list[1]
                    self._first_name = line_list[2]
                    self._birth_date = line_list[3]
                    self._death_date = line_list[4]
                    self._birth_place = line_list[5]
                    self._birth_state = line_list[6]
                    self._term_start_date = line_list[7]
                    self._term_end_date = line_list[8]
                    self._party = line_list[9]

                    break

    @property
    def term_num(self):
        return self._term_num
    
    @property
    def last_name(self):
        return self._last_name
    
    @property
    def first_name(self):
        return self._first_name
    
    @property
    def birth_date(self):
        return self._birth_date
    
    @property
    def death_date(self):
        return self._death_date
    
    @property
    def birth_place(self):
        return self._birth_place
    
    @property
    def birth_state(self):
        return self._birth_state
    
    @property
    def term_start(self):
        return self._term_start_date
    
    @property
    def term_end(self):
        return self._term_end_date
    
    @property
    def party(self):
        return self._party