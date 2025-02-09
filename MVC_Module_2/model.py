import json

class Timetable:
    
    def __init__(self):
        """ Создание класса с контейнером для хранения данных. """
        self.__times = []
    
    def get_times (self):
        """ Получить список данных. """
        return self.__times
    
    def add_time (self, course, mounthDay, fileName ):
        """ Добавить курс {course} с датой {mounthDay} и наименование файла сохранения (fileName) """
        if not self.check_course(course):
            data = {}
            data['course'] = course
            data['mounthDay'] = mounthDay
            self.__times.append(data)
            self.update_json(fileName)
            return True
        else:
            return False 
    
    def check_course (self, course):
        for i in range(len(self.__times)):
            if self.__times[i]['course'] == str(course):
                return True
        return False
    
    def update_time_course (self,course, mounthDay,fileName):
        """ Изменить дату {mounthDay} у определенного курса {course}. {fileName} - Имя файла
        Возвращает измененную дату курса.
        Если нет, то в ответе будет None. """
        for i in range(len(self.__times)):
            if self.__times[i]['course'] == str(course):
                dataLast = self.__times[i]['mounthDay']
                self.__times[i]['mounthDay'] = str(mounthDay)
                self.update_json(fileName)
                return True
        return False
    
    
    def update_json (self, fileName):
        fullFaleName = fr'MVC\file\{fileName}_curseTime.json'
        """ Создание файла с наименованем пользователя, и всеми данными о курсах и датах. """
        with open(fullFaleName,'w', encoding='utf-8') as fp:
            json.dump(self.__times,fp, ensure_ascii=False,indent=4)
            
if __name__ == '__main__':
    timeTable = Timetable()
    
    userName = input('Введите свое имя: ')
    curse1 = timeTable.add_time('HTML', '20 Феврала', userName)
    curse2 = timeTable.add_time('CSS', '16 Октября', userName)
    curse3 = timeTable.add_time('Python', '3 Сентября', userName)
    urse3 = timeTable.add_time('Python', '13 Сентября', userName)
    
    timeTable.update_time_course('HTML','33 Декабря', userName)
    timeTable.update_time_course('HРML','33 Декабря', userName)
    
    print(timeTable.get_times())