class TimetamleController:
    fob = "Fobidden"
    user_owner = ['is_superpuper', 'is_staff','user_owner']
    is_staff = ['is_superpuper', 'is_staff']
    is_superpuper = ['is_superpuper']
    errorValue = "Не верный тип данных - "
    
    def __init__ (self,model):
        self.model = model
    
    def get_default_action (self):
        return "Добро пожаловать на страницу расписания курсов."
    
    def get_times_auth (self, role = 'guest'):
        if role in self.user_owner:
            if self.model.get_times():
                return self.model.get_times()
            return
        return self.fob

    def get_only_curse_list(self):
        curses = []
        data = self.model.get_times()
        if data:
            for el in data:
                curses.append(el['course'])
            return curses
        return
    
    def get_only_mounthDay_list(self):
        mounthDay = []
        data = self.model.get_times()
        if data:
            for el in data:
                mounthDay.append(el['mounthDay'])
            return mounthDay
        return
    
    def get_all_times(self):
        data = self.model.get_times()
        if data:
            return self.get_only_curse_list(),self.get_only_mounthDay_list()
        return

    def add_time_auth (self, course, mounthDay, fileName, role = 'guest'):
        if role not in self.is_superpuper:
            return self.fob
        elif not isinstance(course,str):
            return self.errorValue + str(course)
        elif not isinstance(mounthDay,str):
            return self.errorValue + str(mounthDay)
        return self.model.add_time(course, mounthDay, fileName)

    def update_time_course_auth (self, course, mounthDay, fileName, role = 'guest'):
        if role not in self.is_staff:
            return self.fob
        elif not isinstance(course,str):
            return self.errorValue + str(course)
        elif not isinstance(mounthDay,str):
            return self.errorValue + str(mounthDay)
        return self.model.update_time_course(course, mounthDay, fileName)
