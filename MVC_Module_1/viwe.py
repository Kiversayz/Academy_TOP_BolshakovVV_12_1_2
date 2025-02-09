class TimeViwe:
    fob = "Fobidden"
    def __init__(self,controller):
        self.controller = controller
        
    
    def display_def_action(self):
        print(self.controller.get_default_action())
    
    def display_times_auth (self, role = 'guest'):
        result = self.controller.get_times_auth(role)
        if result == self.fob:
            print(self.fob)
            return
        if result:
            for item in result:
                print(f'Курс - {item['course']}: {item['mounthDay']}')
            return
        print('В базе нет данных о расписании.')
        return
    
    def display_all_times(self):
        courses, mounthDays = self.controller.get_all_times()
        if courses and mounthDays:
            print('Расписание курсов:')
            for i in range(len(courses)):
                print(f'{courses[i]}: {mounthDays[i]}')
            return
        print('Расписание занятий - не запланированно.')
    
    def post_add_time_auth (self, course, mounthDay, fileName, role = 'guest'):
        result = self.controller.add_time_auth(course, mounthDay, fileName, role)
        if result == True:
            print(f'Курс - {course}: {mounthDay} успешно добавлен.')
        elif result == False:
            print(f'Курс с наименованием - {course}, уже существует.')
        elif result == self.fob:
            print("У вас недостаточно прав доступа.")        
    
    def post_update_time_course_auth (self, course, mounthDay, fileName, role = 'guest'):
        result = self.controller.update_time_course_auth(course, mounthDay, fileName, role)
        if result == True:
            print(f'Изменения успешно внесены, у {course} сменилась дата на {mounthDay}.')
        elif result == False:
            print(f'К сожелению данного курса - {course} нет в программе.')
        elif result == self.fob:
            print("У вас недостаточно прав доступа.")